import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_zero`.
1. General form over `[SeminormedCommRing R]` (verbatim proof `simp [l1Norm]`).
2. Composition from mathlib: `MvPolynomial.support_zero` + `Finset.sum_empty`.
3. Even weaker: only `[CommSemiring R] [Norm R]` is needed (no `‖0‖ = 0`, since the sum is
   over the empty support) — recorded but not proposed (the def lives over a seminormed ring).
4. `R = ℤ` bridge back to the exact project statement. -/

open MvPolynomial

namespace Evidence4

variable {σ R : Type*}

section Seminormed

variable [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

/-- General form, verbatim proof. -/
@[simp] theorem l1Norm_zero : l1Norm (0 : MvPolynomial σ R) = 0 := by
  simp [l1Norm]

/-- Composition from mathlib primitives. -/
theorem l1Norm_zero' : l1Norm (0 : MvPolynomial σ R) = 0 := by
  rw [l1Norm, support_zero, Finset.sum_empty]

/-- The project lemma is the `R = ℤ` instance. -/
example : Roth.normOne (0 : MvPolynomial σ ℤ) = 0 := by
  have := l1Norm_zero (σ := σ) (R := ℤ)
  simpa only [l1Norm, Roth.normOne, Int.norm_eq_abs] using this

end Seminormed

/-- Minimal typeclass floor: a `Norm` on a commutative semiring suffices. -/
theorem l1Norm_zero_norm [CommSemiring R] [Norm R] :
    (∑ d ∈ (0 : MvPolynomial σ R).support, ‖(0 : MvPolynomial σ R).coeff d‖) = 0 := by
  simp

end Evidence4
