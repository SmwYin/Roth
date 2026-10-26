import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_neg`.
1. General form over `[SeminormedCommRing R]` with the verbatim proof `simp [l1Norm]`.
2. Composition from mathlib: `MvPolynomial.support_neg` + `MvPolynomial.coeff_neg` + `norm_neg`.
3. Floor: `[CommRing R] [SeminormedAddGroup R]`-style is not a mathlib class combo; instead we
   record that only `‖-a‖ = ‖a‖` is used (shown with a bare `[Norm R]` plus that hypothesis).
4. `R = ℤ` bridge back to the exact project statement. -/

open MvPolynomial

namespace Evidence5

variable {σ R : Type*}

section Seminormed

variable [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

/-- General form, verbatim proof. -/
@[simp] theorem l1Norm_neg (p : MvPolynomial σ R) : l1Norm (-p) = l1Norm p := by
  simp [l1Norm]

/-- Composition from mathlib primitives. -/
theorem l1Norm_neg' (p : MvPolynomial σ R) : l1Norm (-p) = l1Norm p := by
  simp only [l1Norm, support_neg, coeff_neg, norm_neg]

/-- The project lemma is the `R = ℤ` instance. -/
example (P : MvPolynomial σ ℤ) : Roth.normOne (-P) = Roth.normOne P := by
  have := l1Norm_neg (σ := σ) (R := ℤ) P
  simpa only [l1Norm, Roth.normOne, Int.norm_eq_abs] using this

end Seminormed

/-- Floor: a `Norm` on a commutative ring with `‖-a‖ = ‖a‖` suffices. -/
theorem l1Norm_neg_floor [CommRing R] [Norm R] (hneg : ∀ a : R, ‖-a‖ = ‖a‖)
    (p : MvPolynomial σ R) :
    ∑ d ∈ (-p).support, ‖(-p).coeff d‖ = ∑ d ∈ p.support, ‖p.coeff d‖ := by
  simp [hneg]

end Evidence5
