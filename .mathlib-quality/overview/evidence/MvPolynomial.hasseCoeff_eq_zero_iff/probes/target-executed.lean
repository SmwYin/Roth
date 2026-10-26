import Roth.HasseDeriv

open MvPolynomial
namespace RothOverviewEvidence
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]

#check @MvPolynomial.hasseDeriv
#print MvPolynomial.hasseDeriv
#print axioms MvPolynomial.hasseDeriv
#synth Module R (MvPolynomial σ R)
#check fun (d : σ →₀ ℕ) ↦ (hasseDeriv (R := R) d : MvPolynomial σ R → MvPolynomial σ R)
example (d : σ →₀ ℕ) : hasseDeriv (R := R) d =
    Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ
        (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap := rfl
#check fun (d : ℕ →₀ ℕ) ↦ hasseDeriv (R := ℕ) d
#check fun (d : ULift.{1} ℕ →₀ ℕ) ↦ hasseDeriv (R := ULift.{1} ℕ) d
end RothOverviewEvidence


namespace HasseMonomialAssessment
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]
#check @MvPolynomial.hasseDeriv_monomial
#print axioms MvPolynomial.hasseDeriv_monomial
attribute [-simp] MvPolynomial.hasseDeriv_monomial
example (d k : σ →₀ ℕ) (a : R) :
    MvPolynomial.hasseDeriv d (MvPolynomial.monomial k a) =
      MvPolynomial.monomial (k - d) ((MvPolynomial.hasseCoeff d k : R) * a) := by
  simp [MvPolynomial.hasseDeriv]
example (d k : σ →₀ ℕ) (a : R) :
    MvPolynomial.hasseDeriv d (MvPolynomial.monomial k a) =
      MvPolynomial.monomial (k - d) (MvPolynomial.hasseCoeff d k • a) := by
  simpa only [nsmul_eq_mul] using (MvPolynomial.hasseDeriv_monomial d k a)
end HasseMonomialAssessment

section
universe u v
variable {σ : Type u} {S : Type v} [Semiring S]
#check_failure (MvPolynomial.hasseDeriv (σ := σ) (R := S))
end

section
open MvPolynomial
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]
example (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by
  change Finsupp.lsum R _ ((AddMonoidAlgebra.coeffLinearEquiv R) (monomial k a)) = _
  simpa using (Finsupp.lsum_single R (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) k a)
end

section
open MvPolynomial
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]
example (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) :=
  Finsupp.lsum_single R (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) k a
end

namespace HasseApplyAssessment
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]
open MvPolynomial
#check @MvPolynomial.hasseDeriv_apply
#print axioms MvPolynomial.hasseDeriv_apply
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  simp [hasseDeriv, sum_def]
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) :=
  Finsupp.lsum_apply R (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R)))
      ((AddMonoidAlgebra.coeffLinearEquiv R) P)
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  exact Finsupp.lsum_apply R (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R)))
      ((AddMonoidAlgebra.coeffLinearEquiv R) P)
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) (hasseCoeff d k • P.coeff k) := by
  simpa only [nsmul_eq_mul] using (hasseDeriv_apply d P)
section
variable {S : Type v} [Semiring S]
#check_failure (MvPolynomial.hasseDeriv (σ := σ) (R := S))
end
end HasseApplyAssessment

namespace HasseCoeffZeroAssessment
universe u
variable {σ : Type u}
open MvPolynomial
#check @MvPolynomial.hasseCoeff_eq_zero_iff
#print axioms MvPolynomial.hasseCoeff_eq_zero_iff
example (d k : σ →₀ ℕ) : hasseCoeff d k = 0 ↔ ¬d ≤ k := by
  simp [hasseCoeff, Finsupp.prod, Finset.prod_eq_zero_iff, Nat.choose_eq_zero_iff,
    Finsupp.le_iff, not_forall]
end HasseCoeffZeroAssessment
