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
