import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv

/-! Independent mathlib-only specification and composition probes. -/
universe u v
open MvPolynomial
namespace HasseDerivAssessment
variable {σ : Type u} {R : Type v} [CommSemiring R]

-- Name resolution is a pinned-environment fact, not a search-index inference.
#check_failure MvPolynomial.hasseDeriv
#check_failure (Polynomial.hasseDeriv (R := R) 1 : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
#check Polynomial.hasseDeriv
#check MvPolynomial.pderiv
#check Finsupp.lsum
#check AddMonoidAlgebra.coeffLinearEquiv

example (P : Prop) (h : P) : P := by exact?

-- Probe generic search before introducing a local witness of this specification.
example (d : σ →₀ ℕ) :
    ∃ D : MvPolynomial σ R →ₗ[R] MvPolynomial σ R,
      ∀ (k : σ →₀ ℕ) (a : R),
        D (monomial k a) =
          monomial (k - d) (((d.prod fun j n => (k j).choose n : ℕ) : R) * a) := by
  fail_if_success exact?
  refine ⟨(Finsupp.lsum R (fun k : σ →₀ ℕ =>
    (monomial (k - d)).comp
      (LinearMap.lsmul R R ((d.prod fun j n => (k j).choose n : ℕ) : R)))) ∘ₗ
        (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap, ?_⟩
  intro k a
  simp

end HasseDerivAssessment

section
variable {σ : Type u} {S : Type v} [Semiring S]
#check_failure MvPolynomial σ S
end
