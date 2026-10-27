import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_le_card_mul`: the bound `‖p‖₁ ≤ #support(p) * B` from a uniform
coefficient bound `‖coeff d p‖ ≤ B` holds verbatim (one call to `Finset.sum_le_card_nsmul`) for
`MvPolynomial.l1Norm` over any `[SeminormedCommRing R]` (parent verdict target), and over
any `[CommSemiring R] [Norm R]` (no norm axioms needed).

The project statement is recovered for `R = ℤ`. -/

open MvPolynomial

namespace Evidence86

section Seminormed

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

/-- The project proof, verbatim (with `normOne` replaced by `l1Norm`). -/
theorem l1Norm_le_card_mul (p : MvPolynomial σ R) {B : ℝ} (hB : ∀ d, ‖p.coeff d‖ ≤ B) :
    l1Norm p ≤ p.support.card * B := by
  simpa [l1Norm] using p.support.sum_le_card_nsmul _ _ (fun d _ ↦ hB d)

/-- Weaker hypothesis: the bound is only needed on the support. -/
theorem l1Norm_le_card_mul' (p : MvPolynomial σ R) {B : ℝ}
    (hB : ∀ d ∈ p.support, ‖p.coeff d‖ ≤ B) : l1Norm p ≤ p.support.card * B := by
  simpa [l1Norm] using p.support.sum_le_card_nsmul _ _ hB

theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- Recovery of the exact project statement from the general one. -/
example (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) :
    Roth.normOne P ≤ P.support.card * B := by
  simpa only [l1Norm_int_eq_normOne] using
    l1Norm_le_card_mul P (B := B) fun d ↦ by simpa only [Int.norm_eq_abs] using hB d

/-- Composition check: from mathlib alone (given the def) the statement is the single call
`Finset.sum_le_card_nsmul`, after unfolding `l1Norm`. -/
example (p : MvPolynomial σ R) {B : ℝ} (hB : ∀ d, ‖p.coeff d‖ ≤ B) :
    l1Norm p ≤ p.support.card * B :=
  (p.support.sum_le_card_nsmul _ _ fun d _ ↦ hB d).trans_eq (nsmul_eq_mul _ _)

end Seminormed

section NormOnly

-- The statement needs no ring structure on the norm side: only `[CommSemiring R] [Norm R]`.
variable {σ R : Type*} [CommSemiring R] [Norm R]

noncomputable def l1Norm' (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm'_le_card_mul (p : MvPolynomial σ R) {B : ℝ} (hB : ∀ d, ‖p.coeff d‖ ≤ B) :
    l1Norm' p ≤ p.support.card * B := by
  simpa [l1Norm'] using p.support.sum_le_card_nsmul _ _ (fun d _ ↦ hB d)

end NormOnly

end Evidence86
