import Roth.Theta

open Roth

/-! Evidence for `Roth.Θ_unique_le`.
(1) the hypothesis `1 ≤ B` cannot be dropped: at `B = 1/2`, `q = 2`, `r = 1`, the RHS
    `log (1/2) / (1 * log 2) = -1` is negative while `Θ ≥ 0` (`Θ_nonneg`).
(2) signature check. -/

-- (1) `1 ≤ B` is essential.
example : ¬ (Θ (1 / 2 : ℝ) (fun _ : Unit ↦ 2) (fun _ ↦ 1) ≤
    Real.log (1 / 2) / ((1 : ℕ) * Real.log ((2 : ℕ) : ℝ))) := by
  have h0 := Θ_nonneg (B := (1 / 2 : ℝ)) (fun _ : Unit ↦ 2) (r := fun _ ↦ 1)
  have hl : Real.log (1 / 2 : ℝ) < 0 := Real.log_neg (by norm_num) (by norm_num)
  have hl2 : 0 < Real.log ((2 : ℕ) : ℝ) := Real.log_pos (by norm_num)
  have : Real.log (1 / 2) / ((1 : ℕ) * Real.log ((2 : ℕ) : ℝ)) < 0 := by
    push_cast
    exact div_neg_of_neg_of_pos hl (by simpa using hl2)
  intro h
  linarith

-- (2) signature
#check @Θ_unique_le
