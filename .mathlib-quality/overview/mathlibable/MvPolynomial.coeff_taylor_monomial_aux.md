---
decl: MvPolynomial.coeff_taylor_monomial_aux
file: Roth/Taylor.lean
line: 120
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private monomial case of coeff_taylor, a Finsupp.induction on the exponent whose zero case uses hasseDeriv_C and whose step is coeff_taylor_monomial_single_add_aux; used once; mathlib has only the one-variable Polynomial.taylor_coeff.
action: Keep as private helper for its single call site Roth/Taylor.lean:138 (coeff_taylor, monomial case); if coeff_taylor is upstreamed, carry it along with coeff_taylor_monomial_single_add_aux and its three private helpers.
---

# MvPolynomial.coeff_taylor_monomial_aux

## Inventory entry

### `theorem MvPolynomial.coeff_taylor_monomial_aux`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (d k : σ →₀ ℕ) (a : R), (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a))`
- **What**: Multivariate Taylor's theorem (coefficient form) for a single monomial: the coefficient at d of (a·X^k)(X + α) is the value at α of the Hasse derivative Δ_d(a·X^k).
- **How**: `classical`; induction on `k` via mathlib's `Finsupp.induction`, generalizing `d`. Zero case: split `d = 0` (closed by `simp`) or `d ≠ 0` (closed by `simp [← C_apply, hasseDeriv_C hd, hd.symm]`, using the project lemma `hasseDeriv_C` and `taylor_C` as a simp lemma). `single_add i n k hi _ ih` case: `exact coeff_taylor_monomial_single_add_aux α a n (Finsupp.notMem_support_iff.1 hi) ih d`.
- **Hypotheses**: none beyond `[CommSemiring R]` from the section variable (needed by `taylor`, `hasseDeriv`).
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.taylor_C` (simp), `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_C` (Roth/HasseDeriv.lean:126), `MvPolynomial.coeff_taylor_monomial_single_add_aux` (private, Roth/Taylor.lean:101); transitively `coeff_aeval_X_mul`, `hasseCoeff_single_add_eq`, `prod_pow_single_add_tsub`, `hasseDeriv_monomial`.
- **Used by**: Roth/Taylor.lean:138 `coeff_taylor` (monomial case of `MvPolynomial.induction_on'`) only; `grep -rn coeff_taylor_monomial_aux Roth/` gives just the definition (l.120) and that use. Transitively everything downstream of `coeff_taylor` (`degreeOf_taylor_le` l.173, `eq_sum_box_hasseDeriv` l.202, Roth/Index.lean:64,153,158, ...).
- **Visibility**: private
- **Lines**: 120–129, proof length 8 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). Name ends in `_aux`. Mirrors the source's "it suffices to prove the theorem for monomials" step (§4, Theorem on Taylor's expansion).

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_taylor` (Roth/Taylor.lean:138), the public Taylor theorem that Index.lean and the rest of Taylor.lean depend on.
- Wrapper of 1–2 mathlib calls? No. It is an induction on the exponent with a nontrivial base case (constant monomials, needing `hasseDeriv_C`) and delegates the step to a 13-line project lemma.
- Does mathlib have it? No. `lean_leansearch` ("coefficient of multivariate polynomial monomial after substituting X i + C (a i) equals evaluation of Hasse derivative") returned only the one-variable `Polynomial.taylor_coeff` (Mathlib/Algebra/Polynomial/Taylor.lean:68), `Polynomial.hasseDeriv(_monomial)` and `MvPowerSeries.subst`/`coeff_subst` lemmas. Mathlib has no multivariate Hasse derivative (`def hasseDeriv` only in Algebra/Polynomial/HasseDeriv.lean and RingTheory/LaurentSeries.lean), so it cannot contain this.
- Too specific / inline? It could be inlined into the `monomial` branch of `coeff_taylor` (nested induction), but that would make `coeff_taylor` a two-level induction and less readable; the separation into "linearity" and "monomial case" matches the source proof. Factoring is reasonable.
- Well-chosen? Yes; statement is exactly the monomial instance of `coeff_taylor`, with `d` universally quantified so the induction can generalize it.
- Conclusion: `KEEP`. Action: keep as private helper of `coeff_taylor`; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Taylor.lean:120; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent upstreaming (`coeff_taylor` / `MvPolynomial.taylor`): porting `coeff_taylor` with its current proof needs this lemma together with `coeff_taylor_monomial_single_add_aux`, `coeff_aeval_X_mul`, `hasseCoeff_single_add_eq` and `prod_pow_single_add_tsub`, all private helpers.

## Evidence
- `grep -rn coeff_taylor_monomial_aux Roth/`: definition l.120, single use l.138.
- `grep` in Roth/HasseDeriv.lean: `hasseDeriv` l.57, `hasseDeriv_monomial` l.66, `hasseDeriv_C` l.126. Downstream `coeff_taylor` uses: Roth/Taylor.lean:173,202; Roth/Index.lean:64,153,158.
- `grep` in `.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean`: `Polynomial.taylor_coeff` l.68 (one variable only).
- `lean_leansearch` (query above, 6 results): one-variable `Polynomial.taylor_coeff`, `Polynomial.hasseDeriv`, `Polynomial.hasseDeriv_monomial`, MvPowerSeries substitution lemmas; no multivariate analogue.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
