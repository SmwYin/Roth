---
decl: MvPolynomial.hasseCoeff_le_two_pow
file: Roth/HasseDeriv.lean
line: 276
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The multi-index analogue of Nat.choose_le_two_pow is missing from mathlib and is the natural basic bound for the proposed Finsupp.choose; but the box hypothesis k ≤ r and Fintype σ are artefacts of the call sites, and the verified general form is binom(k,d) ≤ 2 ^ k.degree (no Fintype, no r), from which the current form is a two-line corollary.
action: Upstream with the Finsupp.choose PR (parent MvPolynomial.hasseCoeff; Mathlib/Data/Nat/Choose/Multinomial.lean or new Mathlib/Data/Finsupp/Choose.lean) as Finsupp.choose_le_two_pow_degree (k d) : k.choose d ≤ 2 ^ k.degree; locally optionally add hasseCoeff_le_two_pow_degree and derive this lemma from it (call sites Roth/CoeffNorm.lean:140 and :157 unchanged).
---

# MvPolynomial.hasseCoeff_le_two_pow

## Inventory entry

### `theorem MvPolynomial.hasseCoeff_le_two_pow`
- **Type**: `∀ {σ : Type*} [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ}, (∀ j, k j ≤ r j) → hasseCoeff d k ≤ 2 ^ ∑ j, r j`
- **What**: On the box `k ≤ r` (componentwise), the multi-index binomial coefficient `binom(k, d) = ∏_j binom(k_j, d_j)` is at most `2^(r_1 + ⋯ + r_m)`.
- **How**: Rewrites with `hasseCoeff_eq_prod` and `Finset.prod_pow_eq_pow_sum` to compare `∏_j binom(k_j,d_j)` with `∏_j 2^(r_j)` factorwise via `Finset.prod_le_prod`, each factor bounded by `Nat.choose_le_two_pow` followed by `Nat.pow_le_pow_right two_pos (hk j)`.
- **Hypotheses**: `[Fintype σ]` (finitely many variables); `hk : ∀ j, k j ≤ r j` (the exponent lies in the degree box `r`). The section `[CommSemiring R]` is not included.
- **Uses from project**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_eq_prod`
- **Used by**: Roth/CoeffNorm.lean: `abs_coeff_hasseDeriv_le` (l.140), `normOne_hasseDeriv_le` (l.157). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 276–280, proof length 3 lines
- **Notes**: Not a glue lemma (real inequality argument), so the full workflow was run. Both hypotheses are avoidable: `hasseCoeff d k ≤ 2 ^ k.degree` holds for any `σ` (evidence file), and the box version follows by monotonicity.

## Junk check (Step 8)
- Used anywhere? Yes, twice (Roth/CoeffNorm.lean:140, :157), both in the coefficient-norm bounds for Hasse derivatives (paper §3 Lemma 3, §6 Lemma 9).
- Wrapper of 1–2 mathlib calls? No: it combines the parent's product formula, `Finset.prod_le_prod`, `Finset.prod_pow_eq_pow_sum`, `Nat.choose_le_two_pow` and `Nat.pow_le_pow_right`; short but a genuine argument.
- Does mathlib have it? No (mathlib has no multi-index binomial; only the scalar `Nat.choose_le_two_pow`).
- Too specific / inline? Two call sites with identical usage; a named lemma is the right grain. The box parameter `r` is call-site-shaped; a `2 ^ k.degree` statement would be cleaner.
- Well-chosen? Mostly; better stated as `≤ 2 ^ k.degree`.
- Conclusion: `KEEP` — action: keep; optionally restate through `hasseCoeff_le_two_pow_degree` and keep this as a corollary for the two call sites.

## Mathlibable assessment (Step 9)

Not private, no pre-filter fires, not a glue lemma: full `/mathlibable` workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles)
- decl `MvPolynomial.hasseCoeff_le_two_pow`: resolved at Roth/HasseDeriv.lean:276
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseCoeff_le_two_pow` is a theorem stating the following:

Let `σ` be a finite set of variables, `d, k ∈ ℕ^σ` multi-indices and `r ∈ ℕ^σ` with `k ≤ r` componentwise. Then the multi-index binomial coefficient satisfies `binom(k, d) = ∏_j binom(k_j, d_j) ≤ 2^{r_1 + ⋯ + r_m}`. This is the binomial-factor estimate behind "a Hasse derivative of a polynomial of multidegree ≤ r multiplies coefficients by at most `2^{|r|}`".

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]` — the finite set of variables.
- `d : σ →₀ ℕ` — the derivative order (lower index).
- `k : σ →₀ ℕ` — the monomial exponent (upper index).
- `r : σ → ℕ` — the degree box.

Hypotheses (Lean side):
- `hk : ∀ j, k j ≤ r j`.

Conclusion (math): `binom(k, d) ≤ 2^{|r|}`.

Conclusion (Lean): `hasseCoeff d k ≤ 2 ^ (∑ j, r j)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: elementary bound lemma for a helper definition; not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index binomial coefficient bound 2^{abs alpha}, sum over beta le alpha of binom(alpha,beta) | yes | `Σ_{β≤α} binom(α,β) = 2^{abs α}`, hence `binom(α,β) ≤ 2^{abs α}` | arXiv 0708.0780; Wikipedia "Multi-index notation"; ProofWiki "Binomial Theorem/Multiindex" |
| 2 | WebSearch (general form) | binomial coefficient at most 2^n, product over coordinates, multivariate Hasse derivative coefficient estimate, Roth | partial | coefficient norms of Hasse derivatives bounded by a power of 2 in the degrees | arXiv 1806.10737 (Roth over function fields), arXiv 2403.19824 (multi-index binomial as product); no source states our box form separately |
| 3 | WebSearch (named-after / aliases) | Siegel lemma Roth proof Hasse derivative coefficients height bound 2^{r_1+...+r_m} | partial | Roth-proof expositions bound heights of derivatives by `2^{r_1+⋯+r_m}` (Bombieri–Gubler ch. 6, Evertse notes, arXiv 2502.00731) | the estimate is folklore inside Roth's proof; stated with the degree box |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `choose` | yes | l.460: `abs(u_i) ∏_j binom(s(i)_j, d_j) ≤ B 2^S` | the paper uses exactly the box form with `S = r_1+⋯+r_m`; l.127 the product definition |
| 6 | nLab | binomial coefficient / multi-index | no | — | elementary combinatorial bound below nLab's granularity |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | elementary combinatorics, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | no dedicated thread; the bound is immediate from `binom(n,k) ≤ 2^n` |
| 10 | recent arXiv (last 5 years) | (results of #2–#3) | partial | arXiv 2502.00731 (2025), 2403.19824 (2024) | same box/degree-based power-of-2 bound in Roth-type arguments |

### Literature summary (Phase 3)

Concept identified as: the multi-index analogue of `binom(n,k) ≤ 2^n`, i.e. `binom(α, β) ≤ 2^{abs α}` (a consequence of the multi-index binomial theorem `Σ_{β≤α} binom(α,β) = 2^{abs α}`).
Sources agree on the standard form: yes — whenever stated intrinsically it is bounded by `2^{abs α}` (the total degree of the upper index); Roth expositions then use `abs α ≤ r_1+⋯+r_m`.
Most general standard form: for any multi-indices `α, β` (finitely supported, any index set), `binom(α, β) ≤ 2^{abs α}`.
Generality dimensions where the literature varies:
  - bound: `2^{abs α}` (intrinsic) versus `2^{abs r}` for a box `α ≤ r` (Roth applications); the intrinsic one is more general.
  - index set: finite in the literature; arbitrary with finite support is fine.
Disagreement with the literature: none mathematically; the project states the application form rather than the intrinsic form.

### Generality analysis — `MvPolynomial.hasseCoeff_le_two_pow`

Literature-standard form (from Phase 3): `binom(k, d) ≤ 2^{abs k}` for all `d, k`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | finite variable type | any type | yes (verified) | `k.degree` (Finsupp.degree) needs no finiteness; evidence file compiles |
| 2 | `r`, `hk : ∀ j, k j ≤ r j` | box bound, conclusion `2^{Σ r}` | conclusion `2^{abs k}`, no box | yes (verified) | `hasseCoeff_le_two_pow_degree d k : hasseCoeff d k ≤ 2 ^ k.degree` compiles; the box form follows via `Finsupp.degree_eq_sum` and `Finset.sum_le_sum` (evidence file) |
| 3 | `d k : σ →₀ ℕ` | finsupps | multi-indices | no | needed for `Finsupp.degree` and the parent def |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (both verified in one evidence file, clean diagnostics).
Proposed restatement:
```lean
theorem hasseCoeff_le_two_pow_degree (d k : σ →₀ ℕ) : hasseCoeff d k ≤ 2 ^ k.degree
-- upstream spelling:
theorem Finsupp.choose_le_two_pow_degree (k d : σ →₀ ℕ) : k.choose d ≤ 2 ^ k.degree
```
with the current lemma as corollary:
`(hasseCoeff_le_two_pow_degree d k).trans <| Nat.pow_le_pow_right two_pos <| by rw [Finsupp.degree_eq_sum]; exact Finset.sum_le_sum fun j _ ↦ hk j`.
Cost of restatement: CHEAP — mechanical; 4-line `calc` proof compiles.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | `[Fintype σ]` is dropped entirely rather than reformulated |
| 2 | sequences to filters? | no | — | finite combinatorial inequality |
| 3 | construction vs universal property? | no | — | a numeric bound |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | ℕ-valued |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | bound by `2 ^ k.degree` using mathlib's `Finsupp.degree` instead of `∑ j, r j` over a finite type | composes with `Finsupp.degree` API (`degree_add`, `degree_eq_sum`, `MvPolynomial.totalDegree` bounds) and works for infinite `σ` |
| 8 | concrete-via-abstract? | yes (inherited) | proof never mentions polynomials; it belongs in `Finsupp` as `Finsupp.choose` API (parent report) | as #7 |
| 9 | false-generalisation guard | no false generalisation | the original statement is recovered exactly as a corollary (evidence file) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.choose_le_two_pow_degree (k d : σ →₀ ℕ) : k.choose d ≤ 2 ^ k.degree`, the direct multi-index analogue of `Nat.choose_le_two_pow (n k) : n.choose k ≤ 2 ^ n`.
  - Cost: CHEAP
  - Mathlib downstream this enables: coefficient bounds for Hasse derivatives in terms of `MvPolynomial.totalDegree` / `Finsupp.degree` without fixing a finite variable set; chaining with `Finsupp.degree` monotonicity lemmas.
  - Real mathematical improvement: removes two call-site artefacts (finite σ, auxiliary box) and states the intrinsic bound.

### Proof strategy — `MvPolynomial.hasseCoeff_le_two_pow`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (mild) | the multi-index binomial theorem `Σ_{d≤k} binom(k,d) = 2^{abs k}` would give the bound via `single_le_sum`; not needed, the factorwise `Nat.choose_le_two_pow` route is shorter | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (factorwise `Nat.choose_le_two_pow` + `Finset.prod_le_prod` + `Finset.prod_pow_eq_pow_sum`). For the general form, the product is over `d.support` and the exponent sum is enlarged to `k.support` with `Finset.sum_le_sum_of_ne_zero`.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseCoeff_le_two_pow`

[A] Lean-Finder       "multi-index binomial coefficient prod_j choose (k j) (d j) bounded by 2 ^ degree k"   only `Nat.choose_le_two_pow`, `Nat.choose_succ_le_two_pow`, `Nat.choose_lt_two_pow`, `Nat.multinomial_two_mul_le_mul_multinomial` (scalar or different quantities)
[B] Loogle            `Nat.choose, Finsupp.degree`   no hits
[C] LeanSearch        "product of binomial coefficients over a finset is at most 2 to the power of sum"   building blocks only: `Nat.choose_le_two_pow`, `Finset.prod_le_pow_card`, `Finset.prod_le_one`
[D] Grep mathlib src  `choose_le_two_pow`, `le_two_pow_degree`, `hasseCoeff`, `multinomial_le` over `.lake/packages/mathlib/Mathlib`   only `Nat.choose_le_two_pow` (Data/Nat/Choose/Bounds.lean:96) and its use in Central.lean; no multi-index version
[E] Name pattern      `choose_le_two_pow` (grep in [D] in place of lean_local_search)   only the scalar lemma

Searched for both the user's form (box bound) and the literature-standard form (`2 ^ abs k`).

Concluded: found building blocks (`Nat.choose_le_two_pow`, `Finset.prod_le_prod`, `Finset.prod_pow_eq_pow_sum`, `Finsupp.degree`); not in mathlib (the parent multi-index binomial itself is absent).

### Normal-form check — `MvPolynomial.hasseCoeff_le_two_pow`

Equivalent formalisms this statement could take: box form `≤ 2 ^ Σ r` (current); intrinsic `≤ 2 ^ k.degree`; `≤ 2 ^ Σ_j k j` over a Fintype.
Does mathlib already have a canonical form for this idea? For scalars, `Nat.choose_le_two_pow (n k) : n.choose k ≤ 2 ^ n` (bound by the upper argument).
Our statement is stated against the canonical form? no — the canonical analogue is `≤ 2 ^ k.degree`; the box form is a derived corollary.
RHS convention respected? yes (inequality with the named def on the left).

### Syntactic generality — `MvPolynomial.hasseCoeff_le_two_pow`

Alternative restatements attempted:
- `hasseCoeff_le_two_pow_degree (d k) : hasseCoeff d k ≤ 2 ^ k.degree` (compiles)
- current box form derived from it (compiles)
Chosen restatement: the `degree` form as the main lemma; keep the box form only if convenient for the two `CoeffNorm` call sites (they supply `k ≤ r` from `monomial_le_degreeOf`).
Justification: the `degree` form has no hypotheses and applies everywhere; the box form is a one-line consequence.

### Superfluous-argument audit — `MvPolynomial.hasseCoeff_le_two_pow`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | no (for the intrinsic bound) | only needed to state `∑ j, r j` |
| 2 | `r`, `hk` | no (for the intrinsic bound) | replaced by `k.degree` |
| 3 | `d`, `k` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (main statement `≤ 2 ^ k.degree`, matching `Nat.choose_le_two_pow`)
Syntactic generality: RESTATE (`hasseCoeff_le_two_pow_degree` / `Finsupp.choose_le_two_pow_degree`)
Superfluous arguments: 2 to drop for the main lemma (`[Fintype σ]`, `r`/`hk`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseCoeff_le_two_pow`

Internal use count: 2 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:140 | `exact_mod_cast hasseCoeff_le_two_pow fun j ↦ (monomial_le_degreeOf j he).trans (hP j)` (in `abs_coeff_hasseDeriv_le`) |
| Roth/CoeffNorm.lean:157 | `exact_mod_cast hasseCoeff_le_two_pow fun j ↦ (monomial_le_degreeOf j hk).trans (hP j)` (in `normOne_hasseDeriv_le`) |

Inline-derivation grep: (none) — `grep -rn choose_le_two_pow Roth/` finds only this lemma's proof (Roth/HasseDeriv.lean:280).

### Composition check (Phase 6)

Can `MvPolynomial.hasseCoeff_le_two_pow` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [hasseCoeff_eq_prod, ← Finset.prod_pow_eq_pow_sum]; exact Finset.prod_le_prod fun j _ ↦ (Nat.choose_le_two_pow _ _).trans (Nat.pow_le_pow_right two_pos (hk j))` (the current proof)
  - Mathlib decls used: `Finset.prod_pow_eq_pow_sum`, `Finset.prod_le_prod`, `Nat.choose_le_two_pow`, `Nat.pow_le_pow_right`, plus the project's `hasseCoeff_eq_prod`
  - Result: succeeds (evidence file), but it is a `rw` + term proof with four mathlib lemmas and a project lemma, and it depends on the non-mathlib definition `hasseCoeff`.
  - Notes: per the 6b heuristics, `rw [...]` followed by a factorwise argument is a real proof, not a composition.

Conclusion: NOT-COMPOSABLE — the multi-index binomial is not in mathlib, so no mathlib composition can state it; the bound is the natural basic inequality of the parent definition.

## Verdict: `MvPolynomial.hasseCoeff_le_two_pow`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the intrinsic multi-index bound `binom(α,β) ≤ 2^{abs α}` follows from the multi-index binomial theorem (arXiv 0708.0780, ProofWiki, Wikipedia); Roth expositions and the project paper (clean.tex l.460) use the box form `2^{r_1+⋯+r_m}`.
- Generality analysis (Phase 4): STRICTLY NARROWER — `[Fintype σ]` and the box `r` both dropped in `hasseCoeff_le_two_pow_degree`, verified clean by `lake env lean` and `lean_diagnostic_messages`; Phase 4c: analogue of `Nat.choose_le_two_pow` via `Finsupp.degree`.
- Mathlib search (Phase 5): not in mathlib; building blocks `Nat.choose_le_two_pow`, `Finset.prod_le_prod`, `Finset.prod_pow_eq_pow_sum`, `Finsupp.degree`.
- Composition check (Phase 6): NOT-COMPOSABLE (parent definition absent from mathlib; the proof is a genuine factorwise argument).

**Rationale:**

The parent `MvPolynomial.hasseCoeff` was assessed YES-but-generalise-first (upstream as `Finsupp.choose k d`). The concrete mathlib gap is that mathlib has the scalar bound `Nat.choose_le_two_pow` but no multi-index binomial and so no multi-index bound; any user bounding coefficients of multivariate Hasse derivatives (as at both CoeffNorm call sites, the coefficient-growth step in Roth's lemma) needs it. Shipped with `Finsupp.choose`, it is the expected basic inequality next to `choose_eq_prod` and `choose_eq_zero_iff`.

The project form is shaped by its call sites: a finite variable type and a degree box `r`. The intrinsic statement `k.choose d ≤ 2 ^ k.degree` needs neither, compiles with a four-step `calc`, and gives back the box form in one line. That is the form to upstream; the box version can stay local (or be dropped in favour of the degree form plus `Finsupp.degree_eq_sum` at the two call sites).

Reason for the generalisation: LITERATURE-WEAKENING (drop `[Fintype σ]` and the box hypothesis; bound by `2^{abs k}`) and MODERN-IDIOM (state with mathlib's `Finsupp.degree`, mirroring `Nat.choose_le_two_pow`); Phase 5.5 RESTATE-BEFORE-SHIP.
Proposed restatement:
```lean
theorem Finsupp.choose_le_two_pow_degree (k d : σ →₀ ℕ) : k.choose d ≤ 2 ^ k.degree := by
  classical
  calc k.choose d = ∏ j ∈ d.support, (k j).choose (d j) := rfl
    _ ≤ ∏ j ∈ d.support, 2 ^ k j := Finset.prod_le_prod fun j _ ↦ Nat.choose_le_two_pow _ _
    _ = 2 ^ ∑ j ∈ d.support, k j := Finset.prod_pow_eq_pow_sum _ _ _
    _ ≤ 2 ^ k.degree := Nat.pow_le_pow_right two_pos <|
        Finset.sum_le_sum_of_ne_zero fun j _ hj ↦ Finsupp.mem_support_iff.2 hj
```
Estimated cost of regeneralisation: CHEAP (verified for `hasseCoeff`; the `Finsupp.choose` spelling is `rfl`-equal per the parent evidence).
Mathlib downstream this enables:
- coefficient-growth bounds for multivariate Hasse derivatives in terms of `Finsupp.degree` / `MvPolynomial.totalDegree`, for arbitrary variable types;
- API parity with `Nat.choose_le_two_pow` for the new `Finsupp.choose`.
Next action: run `/generalise MvPolynomial.hasseCoeff_le_two_pow` together with the parent; upstream in the `Finsupp.choose` PR (Mathlib/Data/Nat/Choose/Multinomial.lean or new Mathlib/Data/Finsupp/Choose.lean, importing `Mathlib/Data/Finsupp/Weight.lean` and `Mathlib/Data/Nat/Choose/Bounds.lean`), PR title "feat(Data/Finsupp): multi-index binomial coefficient `Finsupp.choose`".

---

## Next step

Ship as `Finsupp.choose_le_two_pow_degree` in the `Finsupp.choose` PR (parent `MvPolynomial.hasseCoeff`); locally optionally add `hasseCoeff_le_two_pow_degree` and derive `hasseCoeff_le_two_pow` from it, leaving Roth/CoeffNorm.lean:140 and :157 untouched.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_le_two_pow/weaken_degree.lean`: `hasseCoeff_le_two_pow_degree` (no `Fintype`, no box), the current statement derived as a corollary, and the current proof reproduced as the composition check. `lake env lean` compiled it with only deprecation warnings for `Finset.prod_le_prod'`; after renaming to `Finset.prod_le_prod`, `lean_diagnostic_messages` reports no errors (only the missing-module-docstring style linter).
- Mathlib: LeanSearch / Lean-Finder return only scalar `Nat.choose_le_two_pow` and relatives; Loogle `Nat.choose, Finsupp.degree` no hits; grep for `choose_le_two_pow`, `le_two_pow_degree`, `hasseCoeff`, `multinomial_le` finds only `Nat.choose_le_two_pow` (Mathlib/Data/Nat/Choose/Bounds.lean:96).
- WebSearch: 3 queries (literature table rows 1–3). ChatGPT MCP: n/a (not configured). Local references: clean.tex l.127, l.460.
- Project grep `grep -rn "hasseCoeff_le_two_pow\|choose_le_two_pow" Roth/` for the call-sites table.
- Parent report `.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md` and sibling `MvPolynomial.hasseCoeff_eq_prod.md` read for the upstream plan.
