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



/- Mathlib-only monomial evaluation probes; no project declarations imported. -/
open MvPolynomial
namespace HasseMonomialAssessment
variable {σ : Type u} {R : Type v} [CommSemiring R]
#check_failure MvPolynomial.hasseDeriv_monomial
#check Polynomial.hasseDeriv_monomial
#check MvPolynomial.pderiv_monomial
#check Finsupp.lsum_single
#check AddMonoidAlgebra.coeffLinearEquiv

-- Abstract content of the unfolding calculation is already existing API.
example (b : (σ →₀ ℕ) → R →ₗ[R] MvPolynomial σ R) (k : σ →₀ ℕ) (a : R) :
    (Finsupp.lsum R b) ((AddMonoidAlgebra.coeffLinearEquiv R) (monomial k a)) = b k a := by
  simpa using (Finsupp.lsum_single R b k a)

-- A new local witness, not an existing mathlib Hasse operator.
noncomputable def witness (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ =>
    (monomial (k - d)).comp
      (LinearMap.lsmul R R ((d.prod fun j n => (k j).choose n : ℕ) : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

example (d k : σ →₀ ℕ) (a : R) :
    witness d (monomial k a) =
      monomial (k - d) (((d.prod fun j n => (k j).choose n : ℕ) : R) * a) := by
  simpa [witness] using
    (Finsupp.lsum_single R (fun k : σ →₀ ℕ =>
      (monomial (k - d)).comp
        (LinearMap.lsmul R R ((d.prod fun j n => (k j).choose n : ℕ) : R))) k a)
end HasseMonomialAssessment

namespace HasseMonomialAssessment
variable {σ : Type u} {R : Type v} [CommSemiring R]
example (d k : σ →₀ ℕ) (a : R) :
    witness d (monomial k a) =
      monomial (k - d) (((d.prod fun j n => (k j).choose n : ℕ) : R) * a) :=
  Finsupp.lsum_single R (fun k : σ →₀ ℕ =>
    (monomial (k - d)).comp
      (LinearMap.lsmul R R ((d.prod fun j n => (k j).choose n : ℕ) : R))) k a
end HasseMonomialAssessment


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
  exact Finsupp.lsum_apply R b ((AddMonoidAlgebra.coeffLinearEquiv R) P)
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
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    witness d P = ∑ k ∈ P.support,
      monomial (k-d) (((d.prod fun j n => (k j).choose n : ℕ) : R) * P.coeff k) :=
  Finsupp.lsum_apply R (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp
      (LinearMap.lsmul R R ((d.prod fun j n => (k j).choose n : ℕ) : R)))
        ((AddMonoidAlgebra.coeffLinearEquiv R) P)
end HasseApplyOnlyAssessment
