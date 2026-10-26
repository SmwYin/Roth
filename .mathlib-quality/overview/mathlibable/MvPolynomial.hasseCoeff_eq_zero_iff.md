---
decl: MvPolynomial.hasseCoeff_eq_zero_iff
file: Roth/HasseDeriv.lean
line: 80
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The vanishing criterion binom(k,d) = 0 iff not d <= k is the basic API companion of the multi-index binomial (analogue of Nat.choose_eq_zero_iff), absent from mathlib; it should ship with the parent as Finsupp.choose_eq_zero_iff plus the positive forms choose_ne_zero_iff and choose_pos_iff.
action: Upstream with MvPolynomial.hasseCoeff (as Finsupp.choose) in Mathlib/Data/Nat/Choose/Multinomial.lean or a new Mathlib/Data/Finsupp/Choose.lean, stated as Finsupp.choose_ne_zero_iff (simp-friendly, proof is simp [choose, Nat.choose_ne_zero_iff, Finsupp.le_iff]) with choose_eq_zero_iff and choose_pos_iff derived; locally keep (used in coeff_hasseDeriv, hasseDeriv_C, Taylor.lean l.113).
---

# MvPolynomial.hasseCoeff_eq_zero_iff

## Inventory entry

### `theorem MvPolynomial.hasseCoeff_eq_zero_iff`
- **Type**: `∀ {σ : Type*} (d k : σ →₀ ℕ), hasseCoeff d k = 0 ↔ ¬d ≤ k`
- **What**: The multi-index binomial coefficient `binom(k, d) = ∏_{j ∈ supp d} (k j).choose (d j)` vanishes exactly when `d ≰ k` (componentwise order).
- **How**: One `simp` call unfolding `hasseCoeff` and `Finsupp.prod`, then `Finset.prod_eq_zero_iff`, `Nat.choose_eq_zero_iff`, `Finsupp.le_iff`, `not_forall`.
- **Hypotheses**: none (the section `[CommSemiring R]` is not included in the statement).
- **Uses from project**: `MvPolynomial.hasseCoeff`
- **Used by**: Roth/HasseDeriv.lean: `coeff_hasseDeriv` (l.99), `hasseDeriv_C` (l.127); Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.113)
- **Visibility**: public
- **Lines**: 80–82, proof length 2 lines
- **Notes**: Not `@[simp]`. Stated in the negative form `= 0 ↔ ¬ …`; the positive form `≠ 0 ↔ d ≤ k` (mirroring `Nat.choose_ne_zero_iff`) is a better simp normal form (see Phase 5.5).

## Junk check (Step 8)
- Used anywhere? Yes: 3 call sites in 2 files (HasseDeriv.lean twice, Taylor.lean once).
- Wrapper of 1–2 mathlib calls? Essentially a `simp` composition of `Finsupp.prod_ne_zero_iff`/`Finset.prod_eq_zero_iff` with `Nat.choose_eq_zero_iff` and `Finsupp.le_iff`; but it is the characteristic vanishing lemma of a named concept, exactly as `Nat.choose_eq_zero_iff` is for `Nat.choose`.
- Does mathlib have it? No (no multi-index binomial in mathlib; see Phase 5).
- Too specific / inline? No: every call site uses the `.2` direction to kill a coefficient; inlining would re-expand `hasseCoeff` (a `Finsupp.prod`) at each site.
- Well-chosen? Yes, modulo the polarity (`≠ 0 ↔ d ≤ k` preferred).
- Conclusion: `KEEP` — action: keep locally; optionally add `hasseCoeff_ne_zero_iff` and derive this from it.

## Mathlibable assessment (Step 9)

Not a glue lemma (proof is a genuine `simp` argument, not `rfl`/`Iff.rfl`), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles)
- decl `MvPolynomial.hasseCoeff_eq_zero_iff`: resolved at Roth/HasseDeriv.lean:80
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseCoeff_eq_zero_iff` is a theorem stating the following:

For finitely supported multi-indices `d, k : σ →₀ ℕ`, the multi-index binomial coefficient `binom(k, d) = ∏_j binom(k_j, d_j)` is zero if and only if `d ≤ k` fails, i.e. iff `k_j < d_j` for some `j`. Equivalently `binom(k, d) ≠ 0 ⇔ d ≤ k`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `d : σ →₀ ℕ` — lower multi-index.
- `k : σ →₀ ℕ` — upper multi-index.

Hypotheses (Lean side):
- none.

Conclusion (math): `binom(k, d) = 0 ⇔ d ≰ k`.

Conclusion (Lean): `hasseCoeff d k = 0 ↔ ¬d ≤ k`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma for a helper definition; not a main result, not a new structure.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2 (one `simp` call)
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index binomial coefficient "alpha choose beta" equals zero unless beta less than or equal alpha | yes | `binom(α,β)` = factorial ratio if `β ≤ α`, `0` otherwise | arXiv 0708.0795 (case-split definition), arXiv 2502.17853 (componentwise order), ProofWiki "Binomial Theorem/Multiindex" |
| 2 | WebSearch (general form) | product of binomial coefficients nonzero iff componentwise inequality multi-index notation | yes | `binom(α,β) = ∏ binom(α_i,β_i)`; `β ≤ α` componentwise | ProofWiki "Definition:Binomial Coefficient/Multiindices", Wikipedia "Multi-index notation"; the iff is the immediate consequence of `binom(a,b)=0 ⇔ a<b` per factor |
| 3 | WebSearch (named-after / aliases) | multivariate Hasse derivative monomial coefficient vanishes if d not less than k | yes | `P^{[i]} = Σ_{j ≥ i} binom(j,i) P_j Y^{j-i}`; terms with `j ≱ i` vanish | arXiv 2403.19824, 2603.03841, 1310.6482 (polynomial method; multiplicity) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for hasse/binom/otherwise | yes | l.122-134: `Δ_i X^k = (∏_j binom(k_j,i_j)) X^{k-i}` if `i ≤ k`, `0` otherwise (l.129) | project source paper §1; exactly this lemma's content |
| 6 | nLab | Hasse-Schmidt derivative (as in parent report) | partial | several-variable HS derivatives; no multi-index binomial vanishing entry | elementary combinatorial fact, below nLab's granularity |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | elementary combinatorics, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #2: multi-index binomial nonzero iff componentwise) | no | — | no dedicated thread surfaced; fact is treated as immediate in all sources |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2502.17853 (2025), 2403.19824 (2024), 2603.03841 (2026) | all use the `β ≤ α` componentwise convention with zero otherwise |

### Literature summary (Phase 3)

Concept identified as: vanishing criterion for the multi-index binomial coefficient `binom(α, β)` (multi-index notation).
Sources agree on the standard form: yes (some sources define `binom(α,β)` only for `β ≤ α`; those defining it as the product set it to `0` otherwise, which is this lemma).
Most general standard form: for multi-indices `α, β`, `binom(α,β) ≠ 0 ⇔ β ≤ α` (componentwise).
Generality dimensions where the literature varies:
  - index set: finite in the literature; arbitrary with finite support here (more general).
  - polarity: literature phrases it positively (`β ≤ α` gives a nonzero coefficient) or as a case split.
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseCoeff_eq_zero_iff`

Literature-standard form (from Phase 3): `binom(α,β) ≠ 0 ⇔ β ≤ α` for finitely supported multi-indices.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `σ : Type*` | arbitrary type | finite index set | no (already more general) | — |
| 2 | `d k : σ →₀ ℕ` | finsupps | multi-indices | `k : σ → ℕ` possible (parent evidence: `hasseCoeff'_eq_zero_iff … ↔ ∃ j, k j < d j` compiles) | not recommended: `d ≤ k` needs both sides in the same order type; parent report kept `k` a finsupp |
| 3 | typeclasses | none | none | no | statement has no ring; section `[CommSemiring R]` not included |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as a statement; the improvement is in name/namespace/polarity, Phase 4c and 5.5).
Number of weakening opportunities found: 0 recommended (the `k : σ → ℕ` variant compiles in the parent evidence but is not recommended).
Cost of restatement: CHEAP

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite combinatorial identity |
| 3 | construction vs universal property? | no | — | a number |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | ℕ-valued |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (inherited from parent) | `Finsupp.choose_eq_zero_iff : k.choose d = 0 ↔ ¬d ≤ k` (and `choose_ne_zero_iff`, `choose_pos_iff`) in `Finsupp` | sits next to `Finsupp.multinomial`; usable by any multi-index binomial/Taylor development, not only Hasse derivatives |
| 8 | concrete-via-abstract? | yes | proof body never mentions polynomials; it is a pure `Finsupp`/`Nat.choose` fact misplaced in `MvPolynomial` | as #7 |
| 9 | false-generalisation guard | no false generalisation | `Finsupp.choose k d` is `rfl`-equal to `hasseCoeff d k` (parent evidence); the restated lemmas compile (this decl's evidence) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `theorem Finsupp.choose_ne_zero_iff {k d : σ →₀ ℕ} : k.choose d ≠ 0 ↔ d ≤ k` (primary, simp-normal), with `Finsupp.choose_eq_zero_iff : k.choose d = 0 ↔ ¬d ≤ k` and `Finsupp.choose_pos_iff : 0 < k.choose d ↔ d ≤ k` derived.
  - Cost: CHEAP (all three compile in the evidence file with one-line proofs)
  - Mathlib downstream this enables: mirrors `Nat.choose_eq_zero_iff`/`Nat.choose_ne_zero_iff`/`Nat.choose_pos`, so `simp` can discharge `k.choose d ≠ 0` side goals from `d ≤ k` in multivariate Taylor/Hasse coefficient lemmas; supports the multi-index binomial theorem summing over `Finset.Iic k`.
  - Real mathematical improvement: places a polynomial-independent combinatorial fact in its natural namespace with mathlib's `Nat.choose` naming and polarity conventions.

### Proof strategy — `MvPolynomial.hasseCoeff_eq_zero_iff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the existing `Finsupp.prod_ne_zero_iff` (simp), `Nat.choose_ne_zero_iff`, `Finsupp.le_iff` suffice; proving the `≠ 0` form first gives a shorter simp set (`simp [choose, Nat.choose_ne_zero_iff, Finsupp.le_iff]`) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a single `simp` with the per-factor characterisation). Minor improvement: prove the `≠ 0` form first and derive this one by `not_not`, as done in the evidence file.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseCoeff_eq_zero_iff`

[A] Lean-Finder       "product over the support of d of binomial coefficients (k j choose d j) is zero iff d is not ≤ k"   no hits for the multi-index form (returns `Nat.choose_ne_zero_iff`, `Nat.choose_eq_zero_iff`, `Nat.multinomial_pos`, `Ring.multichoose_neg_of_lt`: univariate/different quantities)
[B] Loogle            `Finsupp.prod, Nat.choose`   no hits (parent report also: `(_ →₀ ℕ) → (_ →₀ ℕ) → ℕ`, no hits)
[C] LeanSearch        "Finsupp.prod of choose equals zero iff not le"   no multi-index hit (returns `Nat.choose_ne_zero_iff`, `Finsupp.prod_ne_zero_iff`, `Nat.choose_eq_zero_iff`, `Nat.choose_ne_zero`: building blocks)
[D] Grep mathlib src  `hasseCoeff_eq_zero_iff`, `choose_eq_zero_iff` across `.lake/packages/mathlib/Mathlib`, `Finsupp.choose`   only `Nat.choose_eq_zero_iff` (Data/Nat/Choose/Basic.lean:122) and its uses; no multi-index version, no `Finsupp.choose`
[E] Name pattern      `hasseCoeff_eq_zero_iff`, `Finsupp.choose_eq_zero_iff`, `Finsupp.choose_ne_zero_iff`   no hits (only the project decl)

Searched for both the user's form and the literature-standard positive form `binom(α,β) ≠ 0 ↔ β ≤ α`.

Concluded: found building blocks (`Finsupp.prod_ne_zero_iff`, `Nat.choose_ne_zero_iff`, `Finsupp.le_iff`); the parent concept is not in mathlib, so neither is this lemma.

### Normal-form check — `MvPolynomial.hasseCoeff_eq_zero_iff`

Equivalent formalisms this statement could take: `binom(k,d) = 0 ↔ ¬d ≤ k`; `binom(k,d) ≠ 0 ↔ d ≤ k`; `0 < binom(k,d) ↔ d ≤ k`; `binom(k,d) = 0 ↔ ∃ j, k j < d j`.
Does mathlib already have a canonical form for this idea? yes for the univariate analogue: `Nat.choose_eq_zero_iff : n.choose k = 0 ↔ n < k` and `Nat.choose_ne_zero_iff : n.choose k ≠ 0 ↔ k ≤ n`. For `Finsupp` the `≤` side is canonical (`¬d ≤ k` is not simp-normal; `simp` pushes `≠ 0` into `prod_ne_zero_iff`).
Our statement is stated against the canonical form? Partially: RHS `¬d ≤ k` is fine, but the primary lemma should be the positive `≠ 0 ↔ d ≤ k` (RHS `d ≤ k`), as for `Nat`.
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.hasseCoeff_eq_zero_iff`

Alternative restatements attempted:
- `hasseCoeff_ne_zero_iff (d k) : hasseCoeff d k ≠ 0 ↔ d ≤ k` (compiles, evidence file)
- `hasseCoeff_pos_iff (d k) : 0 < hasseCoeff d k ↔ d ≤ k` (compiles)
- `Finsupp.choose_eq_zero_iff {k d} : k.choose d = 0 ↔ ¬d ≤ k` and `choose_ne_zero_iff`, `choose_pos_iff` (compile)
Chosen restatement: `Finsupp.choose_ne_zero_iff` as primary plus `choose_eq_zero_iff` (all three shipped, as for `Nat`), implicit arguments as in `Nat.choose_eq_zero_iff`.
Justification: all three call sites use `.2` with a `¬d ≤ k` proof, so `choose_eq_zero_iff` stays directly applicable; the `≠ 0` form serves `simp` and `positivity`-style side goals.

### Superfluous-argument audit — `MvPolynomial.hasseCoeff_eq_zero_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ` | yes | index type |
| 2 | `d` | yes | — |
| 3 | `k` | yes | — |
| 4 | section `[CommSemiring R]` | not included | no superfluous typeclass in the elaborated type |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (add the positive form `choose_ne_zero_iff` as primary; keep this as a derived lemma)
Syntactic generality: RESTATE (`Finsupp.choose_eq_zero_iff {k d}`, implicit args, Nat.choose argument order)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseCoeff_eq_zero_iff`

Internal use count: 1 outside the declaring file (3 total)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/HasseDeriv.lean:99 | `· simp [hk, (hasseCoeff_eq_zero_iff d k).2 hdk]` (in `coeff_hasseDeriv`) |
| Roth/HasseDeriv.lean:127 | `rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)]` (in `hasseDeriv_C`) |
| Roth/Taylor.lean:113 | `simp [(hasseCoeff_eq_zero_iff e k).2 fun hle ↦ h (le_zero_iff.1 (hi ▸ hle i))] at he` |

Inline-derivation grep: (none) — no other occurrence of `Nat.choose_eq_zero_iff`/`prod_eq_zero_iff` reasoning about `hasseCoeff` in Roth/.

### Composition check (Phase 6)

Can `MvPolynomial.hasseCoeff_eq_zero_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `simp [hasseCoeff, Nat.choose_ne_zero_iff, Finsupp.le_iff]` for the `≠ 0` form (with simp lemma `Finsupp.prod_ne_zero_iff`), then `not_not`.
  - Mathlib decls used: `Finsupp.prod_ne_zero_iff`, `Nat.choose_ne_zero_iff`, `Finsupp.le_iff`
  - Result: succeeds (evidence file)
  - Notes: trivial simp composition; but it needs unfolding of the (not-in-mathlib) definition `hasseCoeff`, so it cannot be inlined at call sites without re-exposing the `Finsupp.prod`.

Conclusion: NOT-COMPOSABLE in the sense required for NO-composable: the composition is the proof of the characteristic lemma of a new definition, not a replacement for it (record: "trivial simp composition; standard API lemma of the parent def").

## Verdict: `MvPolynomial.hasseCoeff_eq_zero_iff`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the multi-index binomial is zero unless `β ≤ α` (arXiv 0708.0795, 2502.17853; ProofWiki multi-index binomial; project paper l.122-134).
- Generality analysis (Phase 4): MAXIMALLY GENERAL as a statement; Phase 4c MODERN-IDIOM: belongs in `Finsupp` with `Nat.choose` naming/polarity conventions (restated forms verified to compile).
- Mathlib search (Phase 5): not in mathlib; building blocks `Finsupp.prod_ne_zero_iff`, `Nat.choose_ne_zero_iff`, `Finsupp.le_iff`.
- Composition check (Phase 6): trivial simp proof, but as the characteristic lemma of a new definition it is NOT-COMPOSABLE as a call-site replacement.

**Rationale:**

The parent `MvPolynomial.hasseCoeff` was assessed YES-but-generalise-first (upstream as `Finsupp.choose k d`). Its vanishing criterion is the first API lemma any such definition needs, exactly as `Nat.choose_eq_zero_iff`/`Nat.choose_ne_zero_iff` accompany `Nat.choose`; all three project call sites use it to kill the off-diagonal terms (`d ≰ k`) of Hasse-derivative coefficients, which is the "`0` otherwise" clause of the source definition. The concrete mathlib gap is the absence of a multi-index binomial and hence of any lemma characterising its support; mathlib's multinomial API (`Nat.multinomial_pos`) covers a different quantity.

The restatement is a namespace/polarity move, not a hypothesis weakening: the proof never mentions polynomials (Q8), so it belongs in `Finsupp`; and mathlib's convention makes the positive form `≠ 0 ↔ d ≤ k` primary. All proposed forms compile with one-line proofs (evidence file). It should ship only bundled with the parent definition, not alone.

Reason for the generalisation: MODERN-IDIOM (namespace, argument order and polarity; Q7/Q8), plus Phase 5.5 RESTATE-BEFORE-SHIP.
Proposed restatement:
```lean
namespace Finsupp
theorem choose_ne_zero_iff {k d : σ →₀ ℕ} : k.choose d ≠ 0 ↔ d ≤ k := by
  simp [choose, Nat.choose_ne_zero_iff, Finsupp.le_iff]
theorem choose_eq_zero_iff {k d : σ →₀ ℕ} : k.choose d = 0 ↔ ¬d ≤ k := by
  rw [← choose_ne_zero_iff, not_not]
theorem choose_pos_iff {k d : σ →₀ ℕ} : 0 < k.choose d ↔ d ≤ k :=
  Nat.pos_iff_ne_zero.trans choose_ne_zero_iff
end Finsupp
```
Estimated cost of regeneralisation: CHEAP (all compile; call sites switch argument order `(hasseCoeff_eq_zero_iff d k).2` to `Finsupp.choose_eq_zero_iff.2` if the parent rename is adopted locally).
Mathlib downstream this enables:
- `simp` discharge of `k.choose d ≠ 0` / `0 < k.choose d` side goals from `d ≤ k`, matching `Nat.choose_ne_zero_iff`/`Nat.choose_pos`;
- support of the multi-index binomial is `Finset.Iic k`, needed for the multi-index binomial theorem and multivariate Taylor/Hasse coefficient formulas (`MvPolynomial.coeff_hasseDeriv`).
Next action: run `/generalise MvPolynomial.hasseCoeff_eq_zero_iff` together with the parent; upstream in the same PR as `Finsupp.choose` (Mathlib/Data/Nat/Choose/Multinomial.lean or a new Mathlib/Data/Finsupp/Choose.lean), PR title "feat(Data/Finsupp): multi-index binomial coefficient `Finsupp.choose`".

---

## Next step

Ship as `Finsupp.choose_ne_zero_iff` / `choose_eq_zero_iff` / `choose_pos_iff` in the `Finsupp.choose` PR (parent `MvPolynomial.hasseCoeff`); locally optionally add `hasseCoeff_ne_zero_iff` and derive this lemma from it.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_eq_zero_iff/restate_and_compose.lean` (compiles with `lake env lean`, no errors or warnings): `hasseCoeff_ne_zero_iff`, `hasseCoeff_pos_iff`, the project form derived from the `≠ 0` form by `not_not`, and `Finsupp.choose_ne_zero_iff` / `choose_eq_zero_iff` / `choose_pos_iff`.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/restate_finsupp_choose.lean` (rfl-equality of `Finsupp.choose k d` and `hasseCoeff d k`; `k : σ → ℕ` variant).
- Mathlib grep for `hasseCoeff_eq_zero_iff`, `choose_eq_zero_iff`, `Finsupp.choose`: only `Nat.choose_eq_zero_iff` and its uses.
- LeanSearch / Lean-Finder: only univariate `Nat.choose` lemmas and `Finsupp.prod_ne_zero_iff`; Loogle `Finsupp.prod, Nat.choose`: no hits.
- WebSearch: 3 queries (summarised in the literature table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseCoeff_eq_zero_iff Roth/` for the call-sites table.
