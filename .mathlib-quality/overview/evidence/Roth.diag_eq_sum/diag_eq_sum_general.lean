import Roth.CoeffNorm

/-! Evidence for the `Roth.diag_eq_sum` mathlibable assessment (re-aimed at
`MvPolynomial.aeval (fun _ ↦ Polynomial.X)`). -/

open MvPolynomial

namespace DiagEqSumEvidence

variable {σ R : Type*} [CommSemiring R]

/-- (1) `diag_eq_sum` re-aimed at the mathlib term, over any commutative semiring. -/
theorem aeval_X_eq_sum (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
      ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) := by
  rw [aeval_def, eval₂_eq]
  simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial]

/-- `Roth.diag_eq_sum` is the `ℤ` case of (1). -/
example (P : MvPolynomial σ ℤ) :
    Roth.diag P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) :=
  aeval_X_eq_sum P

/-- (2) Weighted generalisation: `X_i ↦ X ^ w i` collects monomials by weighted degree. -/
theorem aeval_X_pow_eq_sum (w : σ → ℕ) (P : MvPolynomial σ R) :
    aeval (fun i ↦ (Polynomial.X : Polynomial R) ^ w i) P =
      ∑ k ∈ P.support, Polynomial.monomial (Finsupp.weight w k) (P.coeff k) := by
  rw [aeval_def, eval₂_eq]
  refine Finset.sum_congr rfl fun k _ ↦ ?_
  simp_rw [← pow_mul, Finset.prod_pow_eq_pow_sum, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial, Finsupp.weight_apply, Finsupp.sum, smul_eq_mul,
    mul_comm]

/-- (1) is the `w = 1` case of (2). -/
example (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
      ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) := by
  simpa [Finsupp.degree_eq_weight_one] using aeval_X_pow_eq_sum (fun _ ↦ 1) P

/-- (3) The coefficient formula, the form mathlib is missing. -/
theorem coeff_aeval_X (P : MvPolynomial σ R) (n : ℕ) :
    (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n =
      ∑ k ∈ P.support with k.degree = n, P.coeff k := by
  rw [aeval_X_eq_sum, Polynomial.finsetSum_coeff, Finset.sum_filter]
  exact Finset.sum_congr rfl fun k _ ↦ by rw [Polynomial.coeff_monomial]

/-- (4) Composition attempt through `rename` + `uniqueAlgEquiv` (mathlib's `[Unique σ]` case). -/
example (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
      uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P) := by
  simp [uniqueAlgEquiv_apply, eval₂_rename, aeval_def, Function.comp_def,
    Polynomial.algebraMap_eq]

end DiagEqSumEvidence
