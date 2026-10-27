import Roth.MainLemma
import Mathlib.Algebra.Order.Floor.Semifield

/-! Evidence for the /overview assessment of `Roth.mul_log_div_two_lt_log_mainCoeffBound`. -/

open Roth

-- (1) The hypothesis cannot be dropped: δ = 0 gives X = 1, B₁ = 1, and the claim `0 < log 1`
-- is false.
example : ¬ ((0 : ℝ) * (1 : ℕ) * Real.log (3 : ℕ) / 2 <
    Real.log (mainCoeffBound 0 3 1)) := by
  simp [mainCoeffBound]

-- (2) The threshold 2 is sharp in the abstract form: for X ∈ [1, 2) the floor is 1, so
-- `log X / 2 < log ⌊X⌋₊ = 0` fails. Witness X = 3/2.
example : ¬ (Real.log (3 / 2 : ℝ) / 2 < Real.log (⌊(3 / 2 : ℝ)⌋₊ : ℝ)) := by
  have h : ⌊(3 / 2 : ℝ)⌋₊ = 1 := by
    rw [Nat.floor_eq_iff (by norm_num)]; norm_num
  rw [h]
  have : 0 < Real.log (3 / 2 : ℝ) := Real.log_pos (by norm_num)
  simp only [Nat.cast_one, Real.log_one, not_lt]
  linarith

-- (3) Abstract (X-only) form, derived from the project's `sqrt_lt_floor` in one chain:
-- `log X / 2 < log ⌊X⌋₊` for `2 ≤ X`.
example {X : ℝ} (hX : 2 ≤ X) : Real.log X / 2 < Real.log (⌊X⌋₊ : ℝ) := by
  have h := Real.log_lt_log (Real.sqrt_pos.2 (by linarith)) (sqrt_lt_floor hX).1
  rwa [Real.log_sqrt (by linarith)] at h

-- (4) Mathlib's nearest floor lemma `Nat.div_two_lt_floor` gives `X/2 < ⌊X⌋₊`, which yields
-- only `log X - log 2 < log ⌊X⌋₊`, not the `log X / 2` form; the sqrt route via the project's
-- `sqrt_lt_floor` is what is needed.
example {X : ℝ} (hX : 1 ≤ X) : X / 2 < ⌊X⌋₊ := Nat.div_two_lt_floor hX

#check @mul_log_div_two_lt_log_mainCoeffBound
