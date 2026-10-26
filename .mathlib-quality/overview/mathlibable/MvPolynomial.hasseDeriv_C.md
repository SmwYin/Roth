---
decl: MvPolynomial.hasseDeriv_C
file: Roth/HasseDeriv.lean
line: 126
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Delta_d (C a) = 0 for d ne 0 is the multivariate analogue of mathlib's Polynomial.hasseDeriv_C, absent from mathlib (no MvPolynomial Hasse derivative), maximally general (d ne 0 necessary, CommSemiring forced by MvPolynomial); ships unchanged with the parent operator, ideally beside a companion hasseDeriv_monomial_of_not_le.
action: Upstream with MvPolynomial.hasseDeriv to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (proof via the Finsupp.choose spelling), optionally adding hasseDeriv_monomial_of_not_le and hasseDeriv_one (evidence file); locally keep (used at Roth/Taylor.lean:127).
---

# MvPolynomial.hasseDeriv_C

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_C`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ}, d ≠ 0 → ∀ (a : R), (hasseDeriv d) (C a) = 0`
- **What**: A multivariate Hasse derivative of nonzero order annihilates constants: `Δ_d (C a) = 0` for `d ≠ 0`.
- **How**: `rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 _]` then `simp`: `C a = monomial 0 a`, so `Δ_d (C a) = monomial (0 - d) (hasseCoeff d 0 * a)`, and `hasseCoeff d 0 = 0` because `d ≰ 0` (from `d ≠ 0`, discharged by `simpa using hd`).
- **Hypotheses**: `hd : d ≠ 0` (necessary: `Δ_0 = id`); `[CommSemiring R]` (section variable).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff` (and implicitly `MvPolynomial.hasseCoeff`)
- **Used by**: Roth/Taylor.lean:127 (`coeff_taylor_monomial_aux`, zero case of the `Finsupp.induction`: `simp [← C_apply, hasseDeriv_C hd, hd.symm]`).
- **Visibility**: public
- **Lines**: 126–128 (docstring 123–125), proof length 2 lines
- **Notes**: Mathlib's univariate analogue is `Polynomial.hasseDeriv_C (k : ℕ) (r : R) (hk : 0 < k)` (explicit order, hypothesis last); the project form takes `d` implicit and the hypothesis first, which is fine since `d` is inferable from `hd`. `d ≠ 0` (not `0 < d`) is the idiomatic spelling for `σ →₀ ℕ`. Mathlib also has the companion `Polynomial.hasseDeriv_apply_one`; the project has no `hasseDeriv_one`.

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Taylor.lean:127.
- Wrapper of 1–2 mathlib calls? No: it is about the project operator; mathlib has only the univariate analogue.
- Does mathlib have it? No (Loogle `"hasseDeriv_C"` gives only `Polynomial.hasseDeriv_C`; LeanSearch/Lean-Finder only univariate and `MvPolynomial.pderiv_C`).
- Too specific / inline? No: it is the standard "kills constants" API lemma that every derivative-like operator in mathlib carries (`Polynomial.hasseDeriv_C`, `MvPolynomial.pderiv_C`, `Polynomial.iterate_derivative_C`).
- Well-chosen? Yes; a slightly more general companion `hasseDeriv_monomial_of_not_le` would be a natural addition (evidence) but does not replace this lemma's role as the constant-case API.
- Conclusion: `KEEP` — action: keep; upstream with the parent definition.

## Mathlibable assessment (Step 9)

Not a glue lemma (a rewrite chain using the vanishing of the binomial factor, not `rfl`), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles with no errors or warnings)
- decl `MvPolynomial.hasseDeriv_C`: resolved at Roth/HasseDeriv.lean:126
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_C` is a theorem stating the following:

Let `R` be a commutative semiring, `σ` a set of variables and `d ∈ ℕ^(σ)` a nonzero multi-index. Then the Hasse derivative `Δ_d` sends every constant polynomial `a ∈ R ⊆ R[X_σ]` to `0`. Equivalently: a constant is the monomial `a X^0`, and the binomial factor `binom(0, d) = ∏_j binom(0, d_j)` vanishes as soon as some `d_j > 0`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `d : σ →₀ ℕ` — the order (multi-index) of the derivative.
- `a : R` — the constant.

Hypotheses (Lean side):
- `hd : d ≠ 0` — the derivative has positive total order.

Conclusion (math): `Δ_d(a) = 0`.

Conclusion (Lean): `hasseDeriv d (C a) = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the BIG parent definition `MvPolynomial.hasseDeriv`; not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative of a constant polynomial is zero D^(k) c = 0 for k > 0 | yes | `D^(r) X^n = binom(n, r) X^(n-r)` for `n ≥ r`, else `0`; so `D^(k) c = 0` for `k > 0` | Wikipedia "Hasse derivative"; arXiv 0901.2529 (DKSS); immediate from the definition, not usually a numbered statement |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation D_i(c) = 0 constants ring of constants higher derivation | yes | for a HS derivation of a `k`-algebra, `D_i` vanishes on (the image of) `k` for all `i ≥ 1` | arXiv 2305.04537, math/0510235, 0903.0246, 2007.14171; Matsumura's convention `D_i(f(r)) = 0` for `i ≥ 1` |
| 3 | WebSearch (named-after / aliases) | multivariate Hasse derivative multi-index monomial vanishes unless beta ≤ alpha binomial coefficient polynomial method | yes | `D^(β) x^α = binom(α, β) x^(α-β)`, with `binom(α, β) = ∏ binom(α_j, β_j) = 0` unless `β ≤ α` componentwise | arXiv 2403.19824, 1412.5012, 2111.07572, 1310.6482; the constant case is `α = 0` |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for constant / Δ | partial | l.517 "for any constant c, T(cP) = c T(P)" (linearity in Taylor's theorem); the vanishing of `Δ_d` on constants is used implicitly in the monomial case of Taylor's expansion (l.505-525) | matches the single call site in Roth/Taylor.lean (zero case of the monomial induction for Taylor) |
| 6 | nLab | Hasse-Schmidt derivative | yes | HS derivations are `k`-linear with higher components vanishing on `k` | nLab "Hasse-Schmidt derivative" page (surfaced by #1) |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators abstractly (Tag 09CH-style differential operators), no Hasse-derivative-on-constants lemma for polynomial rings |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; treated as immediate from the definition |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | yes | arXiv 2511.04113 (2025), 2403.19824 (2024), 2305.04537 (2023), 2111.07572 | all use the monomial formula with the vanishing convention |

### Literature summary (Phase 3)

Concept identified as: Hasse (divided-power) derivatives of positive order annihilate constants; abstractly, the higher components of a `k`-linear Hasse–Schmidt derivation vanish on `k`.
Sources agree on the standard form: yes.
Most general standard form: for any (semi)ring `R` and any Hasse derivative of nonzero order (univariate or multivariate, polynomials or power series), `D^(β) c = 0`; more generally `D^(β) x^α = 0` whenever `β ≰ α`.
Generality dimensions where the literature varies:
  - object: polynomials / power series / abstract HS derivations (the operator choice belongs to the parent report).
  - monomial vs constant: the vanishing `D^(β) x^α = 0` for `β ≰ α` contains the constant case `α = 0`; both forms are used (mathlib univariate has only the constant and `X` cases: `hasseDeriv_C`, `hasseDeriv_apply_one`, `hasseDeriv_X`).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_C`

Literature-standard form (from Phase 3): `D^(β) c = 0` for `β ≠ 0`, any (semi)ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hd : d ≠ 0` | nonzero multi-index | positive order | no | necessary: `Δ_0 (C 1) = C 1 ≠ 0` over `ℤ` (evidence, counterexample `example`) |
| 2 | `[CommSemiring R]` | commutative semiring | any semiring | no (for `MvPolynomial`) | `MvPolynomial σ R` requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 3 | `C a` | constant | monomial `X^k` with `d ≰ k` | companion, not a weakening | `hasseDeriv_monomial_of_not_le` (evidence, compiles) is a different, stronger statement; `hasseDeriv_C` follows from it in one line, but the constant case remains the standard API name (mirrors `Polynomial.hasseDeriv_C`) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only hypothesis is necessary — verified counterexample; the typeclass is forced by `MvPolynomial`).
Cost of restatement: n/a. A companion lemma `hasseDeriv_monomial_of_not_le {d k} (h : ¬d ≤ k) (a : R) : hasseDeriv d (monomial k a) = 0` is CHEAP (one-line `simp`, compiled in evidence) and worth shipping alongside, but it does not replace this statement.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single hypothesis `d ≠ 0` |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | could be phrased as `algebraMap R _ '' ⊤ ≤ ker (hasseDeriv d)` but pointwise is what `simp`/`rw` use | — |
| 5 | field-specific to semiring? | no | already the minimum (`CommSemiring`) | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | index type `σ →₀ ℕ` already general | — |
| 8 | concrete-via-abstract? | no | proof uses `C a = monomial 0 a` and `binom(0, d) = 0`; the abstract form is the monomial companion, recorded in Phase 4a row 3 | — |
| 9 | false-generalisation guard | no false generalisation | no generalisation of this statement proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is the canonical constant-annihilation API form used by mathlib for `Polynomial.hasseDeriv_C` and `MvPolynomial.pderiv_C`.

### Proof strategy — `MvPolynomial.hasseDeriv_C`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (minor) | `hasseDeriv_monomial_of_not_le` would make this a one-term corollary (evidence); mathlib's univariate proof is the same rewrite chain (`monomial_zero_left`, `hasseDeriv_monomial`, `Nat.choose_eq_zero_of_lt`) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (same shape as mathlib's `Polynomial.hasseDeriv_C`; with the parent's `Finsupp.choose` spelling it becomes `rw [C_apply, hasseDeriv_monomial, Finsupp.choose_eq_zero_iff ...]`, or a one-liner from the optional companion `hasseDeriv_monomial_of_not_le`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_C`

[A] Lean-Finder       "multivariate polynomial Hasse derivative with nonzero multi-index kills constants"   `Polynomial.hasseDeriv_C`, `Polynomial.hasseDeriv_apply_one`, `Polynomial.hasseDeriv_zero`, `MvPolynomial.pderiv_C`, `MvPolynomial.pderiv_one`; no multivariate Hasse
[B] Loogle            `"hasseDeriv_C"`   1 relevant hit: `Polynomial.hasseDeriv_C` (univariate); plus univariate/Laurent coefficient lemmas
[C] LeanSearch        "Hasse derivative of positive order of a constant polynomial is zero"   `Polynomial.hasseDeriv_apply_one`, `Polynomial.hasseDeriv_C`, `Polynomial.iterate_derivative_one`, `Polynomial.iterate_derivative_C`; no multivariate
[D] Grep mathlib src  `hasseDeriv_C`, `hasseDeriv_apply_one`, `hasseDeriv_monomial_of_not_le`, `MvPolynomial.hasseDeriv` across `.lake/packages/mathlib/Mathlib`: only Algebra/Polynomial/HasseDeriv.lean:116,121
[E] Name pattern      `MvPolynomial.hasseDeriv_C` (grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard general form (`D^(β) x^α = 0` for `β ≰ α`, HS-derivation vanishing on constants).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); `Polynomial.hasseDeriv_C` is the univariate template, and the parent operator itself is absent.

### Normal-form check — `MvPolynomial.hasseDeriv_C`

Equivalent formalisms this statement could take: `hasseDeriv d (C a) = 0`; `hasseDeriv d (monomial 0 a) = 0`; `hasseDeriv d (algebraMap R _ a) = 0`; `C a ∈ ker (hasseDeriv d)`.
Does mathlib already have a canonical form for this idea? yes: `Polynomial.hasseDeriv_C`, `MvPolynomial.pderiv_C`, `Polynomial.iterate_derivative_C` all use `op (C a) = 0`.
Our statement is stated against the canonical form? yes.
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.hasseDeriv_C`

Alternative restatements attempted:
- `hasseDeriv d (C a) = 0` with `hd : d ≠ 0` (current)
- `0 < d` instead of `d ≠ 0` (univariate convention)
- monomial form `hasseDeriv_monomial_of_not_le` (evidence)
- explicit `d` like mathlib's `(k : ℕ)`
Chosen restatement: current statement.
Justification: `d ≠ 0` is the idiomatic nondegeneracy condition for `σ →₀ ℕ` and is what the call site has (`eq_or_ne d 0`); `d` implicit is inferable from `hd`; the `C` form matches the call site after `← C_apply`.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_C`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `hd : d ≠ 0` | yes | necessary (counterexample at `d = 0`, evidence) |
| 3 | `a` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `MvPolynomial.hasseDeriv_C`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file (Roth/Taylor.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:127 | `· simp [← C_apply, hasseDeriv_C hd, hd.symm]` (zero case of `coeff_taylor_monomial_aux`) |

Inline-derivation grep: (none) — `grep -rn hasseDeriv Roth/` filtered for `C`/`one` finds no other proof re-deriving `Δ_d (C a) = 0` from `hasseDeriv_monomial`.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_C` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib.
  - Result: fails
  - Notes: no mathlib operator to specialise.

Attempt 2: from the parent's API: `rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 _]; simp`.
  - Mathlib decls used: `MvPolynomial.C_apply`, `Finsupp.le_zero_iff`-style simp, project `hasseDeriv_monomial`, `hasseCoeff_eq_zero_iff`
  - Result: succeeds, but this is the lemma's own proof (a rewrite chain plus side-goal discharge), the standard API lemma of a new operator, exactly as mathlib proves `Polynomial.hasseDeriv_C`.

Conclusion: NOT-COMPOSABLE (from mathlib; the operator is new)

## Verdict: `MvPolynomial.hasseDeriv_C`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): `D^(β) c = 0` for `β ≠ 0` is immediate from the monomial formula with vanishing binomial factor (Wikipedia; arXiv 2403.19824, 1412.5012, 0901.2529) and is the HS-derivation axiom that higher components vanish on constants (arXiv 2305.04537, Matsumura).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (hypothesis necessary, verified counterexample); Phase 4c: no modern idiom move.
- Mathlib search (Phase 5): not in mathlib; univariate template `Polynomial.hasseDeriv_C`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` was assessed YES-but-generalise-first (multivariate Hasse derivative absent from mathlib; ship with `Finsupp.choose` coefficients). Every derivative-like operator in mathlib carries a "kills constants" lemma (`Polynomial.hasseDeriv_C`, `Polynomial.hasseDeriv_apply_one`, `MvPolynomial.pderiv_C`, `Polynomial.iterate_derivative_C`); this is that lemma for the multivariate Hasse derivative, and it is used in the project exactly where one expects (base case of the monomial induction for Taylor's theorem).

The statement needs no change: the single hypothesis is necessary and the typeclass is forced. The parent's `Finsupp.choose` rename only touches the proof. The natural companion `hasseDeriv_monomial_of_not_le` (and `hasseDeriv_one`, mirroring `Polynomial.hasseDeriv_apply_one`) should be added in the same PR — both compile in the evidence file — but they are additions, not a restatement of this lemma. Hence YES-add-as-is, bundled with the parent PR.

WHY add it: `Mathlib/Algebra/MvPolynomial/` has `pderiv` (with `pderiv_C`) but no Hasse derivative, so there is no lemma telling `simp`/`rw` that `Δ_d` annihilates constants; any multivariate Taylor / multiplicity argument (DKSS method of multiplicities, Roth's index) needs it as the base case of monomial induction. With it, `map_mul`-style manipulations of `Δ_d (C a * P)` and the `T(cP) = c T(P)` step of Taylor's theorem reduce cleanly, and it is the multivariate counterpart of `Polynomial.hasseDeriv_C` (to which it specialises via the `uniqueAlgEquiv` compatibility lemma).
Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
Proposed PR title:            "feat(Algebra/MvPolynomial): multivariate Hasse derivatives"
PR grouping (if applicable):  ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`, `coeff_hasseDeriv`, `hasseDeriv_zero(_apply)`, plus new companions `hasseDeriv_monomial_of_not_le`, `hasseDeriv_one`, in one PR.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.hasseDeriv_C` — confirm no easy further weakening (expected none)
  - [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_C` — full audit + diff gates
  - [ ] Pick a mathlib reviewer based on `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/HasseDeriv.lean` recent commits

---

## Next step

Ship unchanged as `MvPolynomial.hasseDeriv_C` (proof adapted to the parent's `Finsupp.choose` spelling, or as a one-line corollary of a new `hasseDeriv_monomial_of_not_le`) in the parent's PR to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, together with `hasseDeriv_one`; locally keep as is (call site Roth/Taylor.lean:127).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_C/variants.lean` (compiles with `lake env lean`, no errors or warnings): `hasseDeriv_monomial_of_not_le` (general monomial vanishing, one-line `simp`), `hasseDeriv_C` as a one-term corollary of it, an alternative `ext` + `coeff_hasseDeriv` proof, the companion `hasseDeriv d 1 = 0`, and a counterexample showing `d ≠ 0` cannot be dropped (`Δ_0 (C 1) ≠ 0` over `ℤ`).
- During experimentation, `simp [← C_apply, hd]` alone made no progress (so the lemma is not derivable by plain `simp` from the current simp set); that variant was removed from the evidence file.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `"hasseDeriv_C"`: only `Polynomial.hasseDeriv_C`; LeanSearch and Lean-Finder: univariate and `pderiv_C` only; grep of mathlib: univariate only. `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1-3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseDeriv_C Roth/` (Used-by, call sites) and `grep -rn hasseDeriv Roth/` filtered for constants (inline derivations: none); `grep -n constant .mathlib-quality/references/clean.tex` (l.517).
