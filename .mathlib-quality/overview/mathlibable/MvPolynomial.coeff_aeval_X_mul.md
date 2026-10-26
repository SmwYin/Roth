---
decl: MvPolynomial.coeff_aeval_X_mul
file: Roth/Taylor.lean
line: 63
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private coefficient-splitting lemma coeff_d(f(X_i) * B) = f_{d_i} * B_{d.erase i} for B free of X_i, used only in the monomial induction step of coeff_taylor; mathlib has only the monomial case coeff_monomial_mul' and the Fin/Option equivalences.
action: Keep as private helper for its single call site Roth/Taylor.lean:115 (coeff_taylor_monomial_single_add_aux); if coeff_taylor is upstreamed, carry it along privately or state it publicly in Mathlib/Algebra/MvPolynomial/Basic.lean next to coeff_monomial_mul'.
---

# MvPolynomial.coeff_aeval_X_mul

## Inventory entry

### `theorem MvPolynomial.coeff_aeval_X_mul`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (i : σ) (f : Polynomial R) (B : MvPolynomial σ R), (∀ e ∈ B.support, e i = 0) → ∀ (d : σ →₀ ℕ), (Polynomial.aeval (X i) f * B).coeff d = f.coeff (d i) * B.coeff (d.erase i)`
- **What**: If the multivariate polynomial B does not involve the variable X_i (every monomial in its support has i-exponent 0), then the coefficient of the product f(X_i) · B at the multi-index d factors as (coefficient of t^{d_i} in the one-variable polynomial f) times (coefficient of B at d with the i-th entry deleted). It is the "separation of variables" coefficient formula.
- **How**: Expands `Polynomial.aeval (X i) f` as a finite sum `∑_m C(f_m) X_i^m` (`Polynomial.aeval_def`, `Polynomial.eval₂_eq_sum`, `Polynomial.sum_def`, `Finset.sum_mul`, `coeff_sum`), rewrites each term as a monomial (`X_pow_eq_monomial`, `C_mul_monomial`) and uses `coeff_monomial_mul'` to get `if single i m ≤ d then f_m * B.coeff (d - single i m) else 0`. `Finset.sum_eq_single (d i)` isolates the term m = d i, evaluated with `tsub_eq_of_eq_add (Finsupp.erase_add_single i d).symm`; for m ≠ d i with `single i m ≤ d` one has m < d i so `(d - single i m) i ≠ 0`, hence `B.coeff (d - single i m) = 0` by `hB` (`notMem_support_iff`, `Finsupp.single_le_iff`, `Nat.sub_eq_zero_iff_le`); the case d i ∉ f.support is closed by `Polynomial.notMem_support_iff`.
- **Hypotheses**: `[CommSemiring R]`; `hB : ∀ e ∈ B.support, e i = 0` (B free of X_i). `classical` for decidability of `σ`.
- **Uses from project**: `[]` (only mathlib lemmas; it sits in the project namespace `MvPolynomial` but references no project declaration)
- **Used by**: Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.99; `rw [..., coeff_aeval_X_mul i _ _ hsupp, ...]` at l.115) only — `grep -rn coeff_aeval_X_mul Roth/` gives the definition and that use. Transitively: `coeff_taylor_monomial_aux` (l.121) → `coeff_taylor` (l.136) and everything downstream of Taylor's theorem.
- **Visibility**: private
- **Lines**: 63–80, proof length 14 lines
- **Notes**: Declared with `private lemma` (kind recorded as theorem). The `Polynomial.aeval (X i) f` form is chosen to match the call site, where `(X i + C (α i))^n` is rewritten to `Polynomial.aeval (X i) ((Polynomial.X + Polynomial.C (α i))^n)` so that `Polynomial.coeff_X_add_C_pow` applies.

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_taylor_monomial_single_add_aux` (Roth/Taylor.lean:115), the inductive step of the monomial case of `coeff_taylor`.
- Wrapper of 1–2 mathlib calls? No: a 14-line proof combining the sum expansion of `aeval`, `coeff_monomial_mul'` and a `Finset.sum_eq_single` argument using the support hypothesis.
- Does mathlib have it? Not in this form. `grep` over `.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial` and `RingTheory/MvPolynomial` and leansearch ("coefficient of product of polynomial in X i with multivariate polynomial not involving variable i") return only the monomial/variable cases `MvPolynomial.coeff_monomial_mul'`, `coeff_X_mul`, `coeff_mul_X'`, `coeff_X_pow` (Mathlib/Algebra/MvPolynomial/Basic.lean:626–745) and the coefficient lemmas of the variable-splitting equivalences `optionEquivLeft_coeff_coeff` (Equiv.lean:610) and `finSuccEquiv_coeff_coeff` (Equiv.lean:688), which only apply to `Option σ` / `Fin (n+1)` index types and would need a reindexing detour for an arbitrary `i : σ`. No lemma about `Polynomial.aeval (X i) f * B`.
- Too specific / inline? Inlining into `coeff_taylor_monomial_single_add_aux` would add 14 lines to an already long `rw` chain; the separate helper is the cleaner factoring. It is mathematically natural (separation of variables), not call-site junk.
- Well-chosen? Yes as a private helper. A public version would more idiomatically phrase the hypothesis as `i ∉ B.vars` (or `B.degreeOf i = 0`) and could sit next to `coeff_monomial_mul'`.
- Conclusion: `KEEP` — action: keep as private helper for `coeff_taylor_monomial_single_add_aux`; revisit statement shape (`i ∉ B.vars`) only if `coeff_taylor` is upstreamed.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Taylor.lean:63).

Note for the parent upstreaming (`MvPolynomial.taylor` / `coeff_taylor`, see `MvPolynomial.taylor.md`, verdict YES-add-as-is): porting `coeff_taylor` with its current proof requires this lemma; it would go along as a private helper or as a public lemma in Mathlib/Algebra/MvPolynomial/Basic.lean with hypothesis `i ∉ B.vars`.

## Evidence
- `grep -rn coeff_aeval_X_mul Roth/`: definition l.63, single use l.115.
- `grep -rn "theorem coeff_X_pow\|theorem coeff_X_mul\|finSuccEquiv_coeff_coeff\|optionEquivLeft_coeff\|coeff_monomial_mul'"` over mathlib's `Algebra/MvPolynomial`, `RingTheory/MvPolynomial`: only monomial/variable cases and `Option`/`Fin` equivalence coefficient lemmas (locations above).
- `lean_leansearch` (query above, 8 results): `coeffs_X_mul`, `coeff_mul_X'`, `coeff_X_mul`, `coeff_mul_X`, `Polynomial.coeff_X_pow_mul'`, `Polynomial.coeff_mul`, `coeff_monomial_mul`, `coeff_monomial_mul'` — none is the general statement.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
