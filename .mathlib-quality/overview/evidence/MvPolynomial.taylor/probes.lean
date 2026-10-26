import Roth.Taylor
import Mathlib.Algebra.MvPolynomial.Monad
import Mathlib.Algebra.Polynomial.Taylor

/-! Evidence for the `/mathlibable` assessment of `MvPolynomial.taylor`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

-- (1) Composition / defeq probe: `taylor α` is definitionally `bind₁ (X + C ∘ α)` and `aeval`.
example (α : σ → R) : taylor α = bind₁ (fun j ↦ X j + C (α j)) := rfl
example (α : σ → R) : taylor α = aeval (fun j ↦ X j + C (α j)) := rfl

-- (2) Bridge to mathlib's univariate `Polynomial.taylor` (one variable, via `uniqueAlgEquiv`).
theorem uniqueAlgEquiv_taylor [Unique σ] (α : σ → R) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (taylor α P) = Polynomial.taylor (α default) (uniqueAlgEquiv R σ P) := by
  change ((uniqueAlgEquiv R σ : MvPolynomial σ R →ₐ[R] Polynomial R).comp (taylor α)) P =
    ((Polynomial.taylorAlgHom (α default)).comp
      (uniqueAlgEquiv R σ : MvPolynomial σ R →ₐ[R] Polynomial R)) P
  congr 1
  refine algHom_ext fun j ↦ ?_
  obtain rfl := Subsingleton.elim j default
  simp [Polynomial.taylorAlgHom]
  exact (Polynomial.taylor_X _).symm

-- (3) Universe probe: elaborates at mixed universes.
noncomputable example (α : PUnit.{3} → ℤ) : MvPolynomial PUnit.{3} ℤ →ₐ[ℤ] MvPolynomial PUnit.{3} ℤ := taylor α

end MvPolynomial
