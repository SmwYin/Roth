/-! Evidence (expected FAILURE): `MvPolynomial σ R` itself requires `CommSemiring R`, so the
typeclass of `MvPolynomial.hasseDeriv` cannot be weakened to `Semiring R`. -/
import Roth.HasseDeriv
variable {σ R : Type*} [Semiring R]
noncomputable def hd (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (MvPolynomial.monomial (k - d)).comp (LinearMap.lsmul R R (MvPolynomial.hasseCoeff d k : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
