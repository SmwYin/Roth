import Roth.Theta

/-! Necessity of each hypothesis of `Roth.lem7_Φ_bound` (each fails without it). -/

open Roth

-- `hp : 2 ≤ p` is needed: at `p = 1`, `δ = 1` the inequality reads `4 < 3`.
example : ¬ ((1 : ℝ) * (1 + 1 / (1 : ℕ)) + 10 ^ (1 - 1) * ((1 : ℝ) * (1 + 1 / (1 : ℕ))) ^
    ((1 / 2 : ℝ) ^ (1 - 1)) < 3 * 10 ^ (1 - 1) * (1 : ℝ) ^ ((1 / 2 : ℝ) ^ (1 - 1))) := by
  norm_num

-- `hδ0 : 0 < δ` is needed: at `δ = 0` both sides are `0`.
example : ¬ ((0 : ℝ) * (1 + 1 / (2 : ℕ)) + 10 ^ (2 - 1) * ((0 : ℝ) * (1 + 1 / (2 : ℕ))) ^
    ((1 / 2 : ℝ) ^ (2 - 1)) < 3 * 10 ^ (2 - 1) * (0 : ℝ) ^ ((1 / 2 : ℝ) ^ (2 - 1))) := by
  norm_num

-- `hδ1 : δ ≤ 1` cannot be dropped: at `p = 2`, `δ = 10^6` the left side exceeds `1.5·10^6`
-- while the right side is `30 · 10^3`.
example : ¬ ((10 ^ 6 : ℝ) * (1 + 1 / (2 : ℕ)) + 10 ^ (2 - 1) * ((10 ^ 6 : ℝ) * (1 + 1 / (2 : ℕ))) ^
    ((1 / 2 : ℝ) ^ (2 - 1)) < 3 * 10 ^ (2 - 1) * (10 ^ 6 : ℝ) ^ ((1 / 2 : ℝ) ^ (2 - 1))) := by
  have h : (10 ^ 6 : ℝ) ^ ((1 / 2 : ℝ) ^ (2 - 1)) = 1000 := by
    rw [show (1 / 2 : ℝ) ^ (2 - 1) = 1 / 2 by norm_num, ← Real.sqrt_eq_rpow,
      show (10 ^ 6 : ℝ) = 1000 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  rw [h, not_lt]
  have : (0 : ℝ) ≤ 10 ^ (2 - 1) * ((10 ^ 6 : ℝ) * (1 + 1 / (2 : ℕ))) ^ ((1 / 2 : ℝ) ^ (2 - 1)) :=
    by positivity
  norm_num at this ⊢
  linarith

-- sanity: the original statement as stated
example {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) :
    δ * (1 + 1 / (2 : ℕ)) + 10 ^ (2 - 1) * (δ * (1 + 1 / (2 : ℕ))) ^ ((1 / 2 : ℝ) ^ (2 - 1)) <
      3 * 10 ^ (2 - 1) * δ ^ ((1 / 2 : ℝ) ^ (2 - 1)) :=
  lem7_Φ_bound le_rfl hδ0 hδ1
