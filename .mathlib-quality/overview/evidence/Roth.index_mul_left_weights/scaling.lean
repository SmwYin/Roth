import Roth.Index

/-! Evidence for `Roth.index_mul_left_weights`. -/

open MvPolynomial
open scoped Pointwise

namespace Roth
variable {σ : Type*} [Fintype σ]

/-! (1) The current proof reproduced as a composition. -/
example {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α (fun j ↦ l * r j) = index P α r / l := by
  have himg : weight (fun j ↦ l * r j) '' ((taylor α P).support : Set (σ →₀ ℕ)) =
      (l : ℝ)⁻¹ • (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))) := by
    rw [← Set.image_smul, Set.image_image]
    exact Set.image_congr fun d _ ↦ by rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]
  rw [index, index, himg, Real.sInf_smul_of_nonneg (by positivity), smul_eq_mul, div_eq_inv_mul]

/-! (2) No `0 < l` is needed: the `l = 0` instance holds (both sides are `0`). -/
example (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α (fun j ↦ 0 * r j) = 0 := by
  simpa using index_mul_left_weights (l := 0) P α r

/-! (3) `l • r` spelling is the same statement (defeq). -/
example {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α (l • r) = index P α r / l :=
  index_mul_left_weights P α r

end Roth

/-! (4) Power-series analogue (the ℕ∞-valued weighted order is homogeneous in the weight):
not in mathlib; a short proof from `weightedOrder_le` / `le_weightedOrder`. -/
example {σ R : Type*} [Semiring R] (w : σ → ℕ) {l : ℕ} (hl : l ≠ 0)
    (f : MvPowerSeries σ R) :
    MvPowerSeries.weightedOrder (l • w) f = l * MvPowerSeries.weightedOrder w f := by
  have hw : ∀ d : σ →₀ ℕ, Finsupp.weight (l • w) d = l * Finsupp.weight w d := by
    intro d; simp [Finsupp.weight_apply, Finsupp.mul_sum, mul_comm, mul_left_comm]
  by_cases hf : f = 0
  · subst hf; simp [hl]
  obtain ⟨d, hd, hdw⟩ := MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder w
    ((MvPowerSeries.ne_zero_iff_weightedOrder_finite w).1 hf)
  apply le_antisymm
  · rw [← hdw, ← Nat.cast_mul, ← hw]
    exact MvPowerSeries.weightedOrder_le _ hd
  · refine MvPowerSeries.le_weightedOrder _ fun e he ↦ ?_
    by_contra hne
    have := MvPowerSeries.weightedOrder_le w hne
    rw [hw, Nat.cast_mul] at he
    have h' := mul_le_mul' (le_refl (l : ℕ∞)) this
    exact absurd (he.trans_le h') (lt_irrefl _)
