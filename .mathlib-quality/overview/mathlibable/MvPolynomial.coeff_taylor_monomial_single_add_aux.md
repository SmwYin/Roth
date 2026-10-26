---
decl: MvPolynomial.coeff_taylor_monomial_single_add_aux
file: Roth/Taylor.lean
line: 101
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private inductive step (single_add case of Finsupp.induction) of the monomial case of coeff_taylor; a 15-line rw chain via monomial_single_add, coeff_aeval_X_mul and Polynomial.coeff_X_add_C_pow, used once; mathlib has only the one-variable Polynomial.taylor_coeff.
action: Keep as private helper for its single call site Roth/Taylor.lean:129 (coeff_taylor_monomial_aux); if coeff_taylor is upstreamed, carry it along with coeff_aeval_X_mul, hasseCoeff_single_add_eq, prod_pow_single_add_tsub.
---

# MvPolynomial.coeff_taylor_monomial_single_add_aux

## Inventory entry

### `theorem MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (a : R) {i : σ} (n : ℕ) {k : σ →₀ ℕ}, k i = 0 → (∀ d, (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a))) → ∀ (d : σ →₀ ℕ), (taylor α (monomial (Finsupp.single i n + k) a)).coeff d = eval α (hasseDeriv d (monomial (Finsupp.single i n + k) a))`
- **What**: Inductive step of multivariate Taylor's theorem on monomials: if the coefficient formula coeff_d(P(X+α)) = (Δ_d P)(α) holds for the monomial a·X^k, and k does not involve variable i, then it holds for a·X_i^n·X^k.
- **How**: Writes `(X i + C (α i))^n` as `Polynomial.aeval (X i) ((Polynomial.X + Polynomial.C (α i))^n)` (`hXC`, by `simp`); shows every exponent in the support of `taylor α (monomial k a)` has i-th entry 0 (`hsupp`, via `ih`, `hasseDeriv_monomial` and `hasseCoeff_eq_zero_iff`); then one `rw` chain: mathlib `monomial_single_add`, `map_mul`, `map_pow`, `taylor_X`, `hXC`, `coeff_aeval_X_mul i _ _ hsupp`, `ih`, mathlib `Polynomial.coeff_X_add_C_pow` (one-variable binomial expansion), back with `← monomial_single_add`, `hasseDeriv_monomial` (twice), `eval_monomial` (twice), `hasseCoeff_single_add_eq hi`, `prod_pow_single_add_tsub α hi`; closes with `simp [mul_assoc, mul_comm, mul_left_comm]`.
- **Hypotheses**: `hi : k i = 0` (k does not involve variable i, as supplied by `Finsupp.induction`'s `single_add` case); `ih` is the induction hypothesis for `monomial k a`, for all d. `[CommSemiring R]` from the section variable (needed by `taylor`, `hasseDeriv`).
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.taylor_X`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff` (Roth/HasseDeriv.lean), `MvPolynomial.coeff_aeval_X_mul` (private), `MvPolynomial.hasseCoeff_single_add_eq` (private), `MvPolynomial.prod_pow_single_add_tsub` (private); implicitly `MvPolynomial.hasseCoeff` via `hasseDeriv_monomial`.
- **Used by**: Roth/Taylor.lean: `coeff_taylor_monomial_aux` (private, l.124; `exact coeff_taylor_monomial_single_add_aux α a n (Finsupp.notMem_support_iff.1 hi) ih d` at l.129) only. `grep -rn coeff_taylor_monomial_single_add_aux Roth/` gives the definition (l.101) and that single use. Transitively: `coeff_taylor` and everything downstream of Taylor's theorem (`degreeOf_taylor_le`, `eq_sum_box_hasseDeriv`, `eval_eq_sum_box`, ...).
- **Visibility**: private
- **Lines**: 101–118, proof length 13 lines
- **Notes**: Declared with `private lemma` (kind recorded as theorem). Name ends in `_aux`. It was split out of `coeff_taylor_monomial_aux` so the induction there stays short; it ties together the three private helpers above it.

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_taylor_monomial_aux` (Roth/Taylor.lean:129), the `single_add` case of the `Finsupp.induction` that proves the monomial case of `coeff_taylor`.
- Wrapper of 1–2 mathlib calls? No. It is a 13-line argument with two `have`s and a 14-step rewrite chain using three project helpers plus mathlib's `monomial_single_add` and `Polynomial.coeff_X_add_C_pow`.
- Does mathlib have it? No. `lean_leansearch` ("coefficient of multivariate polynomial composed with X + C a equals evaluation of Hasse derivative (multivariable Taylor)") returned the one-variable `Polynomial.taylor_coeff` (Mathlib.Algebra.Polynomial.Taylor) and unrelated `MvPowerSeries.coeff_subst` / substitution lemmas. Mathlib has no multivariate Hasse derivative (`grep "def hasseDeriv"` in Mathlib finds only `Polynomial.hasseDeriv` and `HahnSeries`/LaurentSeries `hasseDeriv`), so it cannot have this step.
- Too specific / inline? It is specific to the induction, but inlining it into the `single_add` branch of `coeff_taylor_monomial_aux` would just move 13 lines and make that proof longer and harder to read. Factoring it out is the right choice.
- Well-chosen? Yes as a private helper. Its statement is exactly the induction step, with the induction hypothesis passed explicitly.
- Conclusion: `KEEP`. Action: keep as private helper for `coeff_taylor_monomial_aux`; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Taylor.lean:101; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent upstreaming (`coeff_taylor` / `MvPolynomial.taylor`): porting `coeff_taylor` with its current proof needs this lemma. It would go along as a private helper together with `coeff_aeval_X_mul`, `hasseCoeff_single_add_eq` and `prod_pow_single_add_tsub`.

## Evidence
- `grep -rn coeff_taylor_monomial_single_add_aux Roth/`: definition l.101, single use l.129.
- `grep` in `.lake/packages/mathlib/Mathlib/`: `monomial_single_add` at Algebra/MvPolynomial/Basic.lean:255, `Polynomial.coeff_X_add_C_pow` at Algebra/Polynomial/Coeff.lean:292; `def hasseDeriv` appears only in Algebra/Polynomial/HasseDeriv.lean:59 and RingTheory/LaurentSeries.lean:118 (no multivariate version).
- `lean_leansearch` (query above, 6 results): only the one-variable `Polynomial.taylor_coeff` and MvPowerSeries substitution lemmas.
- No Lean runs and no evidence Lean files. A private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
