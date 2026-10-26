import Roth.HasseDeriv
open MvPolynomial
namespace HasseApplyAssessment
universe u v
variable {σ : Type u} {R : Type v} [CommSemiring R]
#check @MvPolynomial.hasseDeriv_apply
#print axioms MvPolynomial.hasseDeriv_apply
-- Target has no simp attribute; avoid invoking it in independent proofs.
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  simp [hasseDeriv, sum_def]
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  change Finsupp.lsum R _ ((AddMonoidAlgebra.coeffLinearEquiv R) P) = _
  simpa only [Finsupp.sum] using
    (Finsupp.lsum_apply R (fun k : σ →₀ ℕ =>
      (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R)))
        ((AddMonoidAlgebra.coeffLinearEquiv R) P))
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) (hasseCoeff d k • P.coeff k) := by
  simpa only [nsmul_eq_mul] using (hasseDeriv_apply d P)
end HasseApplyAssessment
section
universe u v
variable {σ : Type u} {S : Type v} [Semiring S]
#check_failure (MvPolynomial.hasseDeriv (σ := σ) (R := S))
end
