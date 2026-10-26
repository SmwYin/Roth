import Roth.HasseDeriv

/-! Current declaration assessment experiments, independent of production edits. -/
namespace HasseZeroAssessment
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
#check @MvPolynomial.hasseDeriv_zero
#print axioms MvPolynomial.hasseDeriv_zero
theorem coefficient_replay : hasseDeriv (0 : σ →₀ ℕ) =
    (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R) := by
  apply LinearMap.ext
  intro P
  apply MvPolynomial.ext
  intro e
  change (hasseDeriv 0 P).coeff e = P.coeff e
  simp only [coeff_hasseDeriv, add_zero, hasseCoeff, Finsupp.prod_zero_index, Nat.cast_one, one_mul]
theorem unfolded : hasseDeriv (0 : σ →₀ ℕ) =
    (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R) := by
  apply LinearMap.ext
  intro P
  change hasseDeriv 0 P = P
  simp [hasseDeriv, hasseCoeff, Function.comp_def, LinearMap.lsmul_apply, sum_def]
#print axioms coefficient_replay
#print axioms unfolded
theorem original_term : hasseDeriv (0 : σ →₀ ℕ) =
    (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R) :=
  LinearMap.ext hasseDeriv_zero_apply
#print axioms original_term
end HasseZeroAssessment
