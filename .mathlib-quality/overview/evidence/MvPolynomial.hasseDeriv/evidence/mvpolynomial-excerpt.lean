
noncomputable section

open Set Function Finsupp AddMonoidAlgebra
open scoped Pointwise

universe u v w x

variable {R : Type u} {S₁ : Type v} {S₂ : Type w}

/-- Multivariate polynomial, where `σ` is the index set of the variables and
  `R` is the coefficient ring -/
abbrev MvPolynomial (σ : Type*) (R : Type*) [CommSemiring R] :=
  AddMonoidAlgebra R (σ →₀ ℕ)

namespace MvPolynomial

variable {σ : Type*} {a a' a₁ a₂ : R} {e : ℕ} {n m : σ} {s : σ →₀ ℕ}

section CommSemiring
variable [CommSemiring R] [CommSemiring S₁] {p q : MvPolynomial σ R}

/-- `monomial s a` is the monomial with coefficient `a` and exponents given by `s` -/
def monomial (s : σ →₀ ℕ) : R →ₗ[R] MvPolynomial σ R :=
  AddMonoidAlgebra.lsingle s

theorem one_def : (1 : MvPolynomial σ R) = monomial 0 1 := rfl
