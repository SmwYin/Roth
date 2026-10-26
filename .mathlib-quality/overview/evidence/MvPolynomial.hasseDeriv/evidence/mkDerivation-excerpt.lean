@[expose] public section


namespace MvPolynomial

noncomputable section

variable {σ R A : Type*} [CommSemiring R] [AddCommMonoid A] [Module R A]
  [Module (MvPolynomial σ R) A]

section

variable (R)

/-- The derivation on `MvPolynomial σ R` that takes value `f i` on `X i`, as a linear map.
Use `MvPolynomial.mkDerivation` instead. -/
def mkDerivationₗ (f : σ → A) : MvPolynomial σ R →ₗ[R] A :=
  Finsupp.lsum R (fun xs : σ →₀ ℕ =>
    (LinearMap.ringLmapEquivSelf R R A).symm <|
      xs.sum fun i k => monomial (xs - Finsupp.single i 1) (k : R) • f i)
    ∘ₗ (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

end

theorem mkDerivationₗ_monomial (f : σ → A) (s : σ →₀ ℕ) (r : R) :
    mkDerivationₗ R f (monomial s r) =
      r • s.sum fun i k => monomial (s - Finsupp.single i 1) (k : R) • f i :=
  sum_monomial_eq <| map_zero _

