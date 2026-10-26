import Roth.HasseDeriv

open MvPolynomial

-- Is the expansion definitional? (pure unfolding check)
example {σ R : Type*} [CommSemiring R] (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  rfl

-- The `Finsupp.sum` form, the mathlib-style spelling of the same expansion
example {σ R : Type*} [CommSemiring R] (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = (AddMonoidAlgebra.coeff P).sum fun k a ↦ monomial (k - d) ((hasseCoeff d k : R) * a) := by
  rfl
