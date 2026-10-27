import Roth.Index

/-! Evidence for `Roth.index_eq_weightedOrder_div`. -/

open MvPolynomial

namespace Roth.Evidence

variable {σ : Type*} [Fintype σ]

/-- (1) `hP : P ≠ 0` is superfluous: for `P = 0` both sides are `0`. -/
theorem index_eq_weightedOrder_div_noHP (P : MvPolynomial σ ℝ) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r =
      (((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j ↦ (∏ i, r i) / r j).toNat : ℝ) /
        ∏ i, r i := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp [index]
  · exact index_eq_weightedOrder_div hP hr α

/-- (2) `hr : ∀ j, 0 < r j` is genuinely needed: with `σ = Bool`, `r true = 1`,
`r false = 0`, `P = X true`, `α = 0`, the index is `1` but `∏ r = 0`, so the right-hand side
is `x / 0 = 0`. -/
example : index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun b ↦ if b then 1 else 0) ≠
      (((taylor (fun _ ↦ 0) (X true : MvPolynomial Bool ℝ) : MvPowerSeries Bool ℝ).weightedOrder
        fun j ↦ (∏ i : Bool, if i then 1 else 0) / (if j then 1 else 0)).toNat : ℝ) /
        ∏ i : Bool, ((if i then 1 else 0 : ℕ) : ℝ) := by
  have h1 : index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun b ↦ if b then 1 else 0) = 1 := by
    rw [index, taylor_zero, support_X]
    simp [weight, Finsupp.single_apply]
  rw [h1]
  simp

end Roth.Evidence
