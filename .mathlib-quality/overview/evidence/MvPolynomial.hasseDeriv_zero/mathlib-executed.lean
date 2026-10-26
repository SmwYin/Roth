import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Nat.Choose.Bounds
#check_failure MvPolynomial.hasseDeriv_zero
namespace ZeroBundledAssessment
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
noncomputable def delta (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R ((d.prod fun j ↦ (k j).choose : ℕ) : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

theorem normalized : delta (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] _) := by
  apply LinearMap.ext
  intro P
  change delta 0 P = P
  simp [delta, Function.comp_def, LinearMap.lsmul_apply, sum_def]
theorem abstract (T : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (h : ∀ P, T P = P) : T = LinearMap.id := LinearMap.ext h
theorem coefficient_preserving (T : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (h : ∀ e P, (T P).coeff e = P.coeff e) : T = LinearMap.id := by
  apply LinearMap.ext
  intro P
  apply MvPolynomial.ext
  intro e
  change (T P).coeff e = P.coeff e
  exact h e P
theorem false_unnormalized : ¬ ∀ T : MvPolynomial Unit ℕ →ₗ[ℕ] MvPolynomial Unit ℕ,
    T = LinearMap.id := by
  intro h
  have hh := LinearMap.congr_fun (h 0) 1
  simp at hh
#check @Polynomial.hasseDeriv_zero
#check @Polynomial.hasseDeriv_zero'
#check @LinearMap.ext
#check @LinearMap.congr_fun
#check @MvPolynomial.support_sum_monomial_coeff
#print axioms normalized
#print axioms abstract
#print axioms coefficient_preserving
#print axioms false_unnormalized
end ZeroBundledAssessment
