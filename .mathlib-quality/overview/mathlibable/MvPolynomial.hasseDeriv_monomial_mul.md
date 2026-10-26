---
decl: MvPolynomial.hasseDeriv_monomial_mul
file: Roth/HasseDeriv.lean
line: 225
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private monomial case of hasseDeriv_mul_of_degreeOf_eq_zero (a monomial X^a c with a_j = 0 on supp d commutes with Δ_d), proved by induction_on' on g; single call site; mathlib has no multivariate Hasse derivative.
action: Keep as private helper for its single call site hasseDeriv_mul_of_degreeOf_eq_zero (Roth/HasseDeriv.lean:246); upstream it together with that public lemma if MvPolynomial.hasseDeriv goes to Mathlib/Algebra/MvPolynomial/.
---

# MvPolynomial.hasseDeriv_monomial_mul

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_monomial_mul`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {d a : σ →₀ ℕ}, (∀ j ∈ d.support, a j = 0) → ∀ (c : R) (g : MvPolynomial σ R), hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g`
- **What**: If the exponent vector a vanishes on every variable that the multi-index d differentiates, then the monomial c X^a passes through the Hasse derivative: Δ_d (c X^a · g) = c X^a · Δ_d g. This is the monomial case of the "constants w.r.t. the differentiated variables pull out" rule.
- **How**: Induction on `g` via `MvPolynomial.induction_on'`. Monomial case `g = c' X^b`: rewrite with `monomial_mul_monomial` and the project's `hasseDeriv_monomial` twice; the binomial factor `hasseCoeff d (a + b) = hasseCoeff d b` by `Finset.prod_congr` since `a j = 0` on `d.support`; the exponent identity `a + b - d = a + (b - d)` is proved pointwise (`Finsupp.ext`, case split on `j ∈ d.support`, `simp_all`); then `simp [monomial_mul_monomial, hs, mul_left_comm]`. Additive case: `simp [mul_add, hp, hq]` (uses linearity of `hasseDeriv`).
- **Hypotheses**: `ha : ∀ j ∈ d.support, a j = 0` (needed: otherwise the binomial factor and exponent change); `R` a commutative semiring (file-wide variable).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff`
- **Used by**: Roth/HasseDeriv.lean: `hasseDeriv_mul_of_degreeOf_eq_zero` (l.243, used at l.246) only (grep over `Roth/` and `Roth.lean`). Transitively: Roth/Separation.lean `hasseDeriv_rename_mul_aeval` (l.146, uses `hasseDeriv_mul_of_degreeOf_eq_zero` at l.157 and l.161).
- **Visibility**: private
- **Lines**: 225–236, proof length 10 lines
- **Notes**: Declared with `lemma` (kind recorded as theorem). The hypothesis form `a j = 0` on `d.support` is the monomial-level version of the public lemma's `degreeOf j f = 0`; the public lemma reduces to it via `f.as_sum` and `monomial_le_degreeOf`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `hasseDeriv_mul_of_degreeOf_eq_zero` (Roth/HasseDeriv.lean:246), which is used twice in `Separation.hasseDeriv_rename_mul_aeval`.
- Wrapper of 1–2 mathlib calls? No: a 10-line induction combining `induction_on'`, `monomial_mul_monomial`, the project's `hasseDeriv_monomial`, and a `hasseCoeff` product congruence plus a tsub exponent identity.
- Does mathlib have it? No. Mathlib has no multivariate Hasse derivative (`grep -rln hasseDeriv` over mathlib: only `Algebra/Polynomial/HasseDeriv.lean`, `Algebra/Polynomial/Taylor.lean`, `RingTheory/LaurentSeries.lean`, all univariate). The univariate Leibniz rule `Polynomial.hasseDeriv_mul` (loogle `Polynomial.hasseDeriv _ (_ * _)`) is the only product rule; leansearch for the statement returned only `Polynomial.hasseDeriv`, `pderiv_eq_zero_of_notMem_vars`, `mkDerivation_monomial`, `Polynomial.hasseDeriv_monomial` — none applicable.
- Too specific / inline? It could be inlined into `hasseDeriv_mul_of_degreeOf_eq_zero` as a `have`, but that public proof is a clean 3-line reduction to the monomial case; keeping the monomial case as a separate private lemma is the standard factoring (cf. sum-over-support proofs in mathlib). Alternatively the public lemma could be proved directly by induction on `f`, but the degree hypothesis does not transfer to summands of an `induction_on'` decomposition as cleanly as through `f.as_sum`/`monomial_le_degreeOf`, so the current split is reasonable.
- Well-chosen? Yes as a private helper; public API is the `degreeOf` version.
- Conclusion: `KEEP` — action: keep as private helper for `hasseDeriv_mul_of_degreeOf_eq_zero`; upstream alongside it if `MvPolynomial.hasseDeriv` is ported.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/HasseDeriv.lean:225).

Note for upstreaming: if `MvPolynomial.hasseDeriv` and the public `hasseDeriv_mul_of_degreeOf_eq_zero` go to mathlib, this lemma travels with it as the monomial step (possibly stated with `Disjoint a.support d.support`, matching `hasseDeriv_hasseDeriv_of_disjoint`).

## Evidence
- `grep -rn hasseDeriv_monomial_mul Roth/`: definition l.225, single use l.246 (`hasseDeriv_mul_of_degreeOf_eq_zero`).
- `grep -rn hasseDeriv_mul_of_degreeOf_eq_zero Roth/ Roth.lean`: uses at Roth/Separation.lean:157, 161 (inside `hasseDeriv_rename_mul_aeval`, l.146).
- `grep -rln hasseDeriv .lake/packages/mathlib/Mathlib`: univariate files only.
- `lean_loogle "Polynomial.hasseDeriv _ (_ * _)"`: only `Polynomial.hasseDeriv_mul` (univariate Leibniz).
- `lean_leansearch` (natural-language statement): no multivariate analogue.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
