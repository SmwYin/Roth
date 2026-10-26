import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
open MvPolynomial
namespace HasseApplyOnlyAssessment
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]
#check_failure MvPolynomial.hasseDeriv_apply
#check Finsupp.lsum_apply
#check MvPolynomial.sum_def
#check Polynomial.hasseDeriv_apply
-- Generic route in mathlib, before any new witness.
example (b : (σ →₀ ℕ) → R →ₗ[R] MvPolynomial σ R) (P : MvPolynomial σ R) :
    Finsupp.lsum R b ((AddMonoidAlgebra.coeffLinearEquiv R) P) =
      ∑ k ∈ P.support, b k (P.coeff k) := by
  simpa only [Finsupp.sum] using
    (Finsupp.lsum_apply R b ((AddMonoidAlgebra.coeffLinearEquiv R) P))
-- New witness, explicitly not a pre-existing mathlib Hasse operator.
noncomputable def witness (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ =>
    (monomial (k - d)).comp
      (LinearMap.lsmul R R ((d.prod fun j n => (k j).choose n : ℕ) : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    witness d P = ∑ k ∈ P.support,
      monomial (k-d) (((d.prod fun j n => (k j).choose n : ℕ) : R) * P.coeff k) := by
  simp [witness, MvPolynomial.sum_def]
end HasseApplyOnlyAssessment
