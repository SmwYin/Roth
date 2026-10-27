import Roth.Index

/-! Evidence for the `Roth.index` assessment: relation to `MvPowerSeries.weightedOrder`. -/

open MvPolynomial

namespace Roth.Evidence

variable {σ : Type*} [Fintype σ]

/-- (1) The `P ≠ 0` hypothesis of `index_eq_weightedOrder_div` is superfluous: for `P = 0`
both sides are `0` (`sInf ∅ = 0`, `(⊤ : ℕ∞).toNat = 0`). -/
theorem index_eq_weightedOrder_div' (P : MvPolynomial σ ℝ) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r =
      (((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j ↦ (∏ i, r i) / r j).toNat : ℝ) /
        ∏ i, r i := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp [index]
  · exact index_eq_weightedOrder_div hP hr α

/-- (2) `index_prod` is a one-step consequence of mathlib's `weightedOrder_prod` once the
index is expressed via `weightedOrder` (shown at the `ℕ∞` level). -/
example {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℝ) (α : σ → ℝ) (w : σ → ℕ) :
    ((taylor α (∏ i ∈ s, f i) : MvPolynomial σ ℝ) : MvPowerSeries σ ℝ).weightedOrder w =
      ∑ i ∈ s, ((taylor α (f i) : MvPolynomial σ ℝ) : MvPowerSeries σ ℝ).weightedOrder w := by
  simp only [map_prod, ← MvPolynomial.coeToMvPowerSeries.ringHom_apply]
  exact MvPowerSeries.weightedOrder_prod w _ s

/-- (3) `index_neg` at the `ℕ∞` level is mathlib's `weightedOrder_neg`. -/
example (P : MvPolynomial σ ℝ) (α : σ → ℝ) (w : σ → ℕ) :
    ((taylor α (-P) : MvPolynomial σ ℝ) : MvPowerSeries σ ℝ).weightedOrder w =
      ((taylor α P : MvPolynomial σ ℝ) : MvPowerSeries σ ℝ).weightedOrder w := by
  simp only [map_neg, ← MvPolynomial.coeToMvPowerSeries.ringHom_apply]
  exact MvPowerSeries.weightedOrder_neg w _

/-- (4) The `sInf` definition is total in `r`: with all `r j = 0` every weight is `0` (Lean's
`x / 0 = 0`), so the index is `0`, whereas the natural weights `(∏ r) / r j` all vanish and the
`weightedOrder` formula of (1) reads `0 / 0`. So the `weightedOrder` form genuinely needs `0 < r`. -/
theorem index_zero_weights (P : MvPolynomial σ ℝ) (α : σ → ℝ) : index P α 0 = 0 := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp [index]
  · obtain ⟨d, -, hd⟩ := exists_weight_eq_index hP α 0
    rw [← hd]
    simp [weight]

end Roth.Evidence
