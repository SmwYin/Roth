import Roth.HasseDeriv

namespace MvPolynomial
variable {σ R : Type*} [CommSemiring R]

-- The bundled statement is exactly `LinearMap.ext` of the pointwise lemma (pure repackaging).
example : hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] _) :=
  LinearMap.ext fun P ↦ hasseDeriv_zero_apply P

-- Conversely the pointwise lemma is `LinearMap.congr_fun` of the bundled one.
example (P : MvPolynomial σ R) : hasseDeriv 0 P = P :=
  LinearMap.congr_fun hasseDeriv_zero P

-- Mathlib's univariate template has the same shape.
#check @Polynomial.hasseDeriv_zero
end MvPolynomial
