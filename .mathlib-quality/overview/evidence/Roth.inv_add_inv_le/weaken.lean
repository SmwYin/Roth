import Mathlib.Analysis.Real.Sqrt

/-! Evidence for `Roth.inv_add_inv_le` (private, Roth/Lattice.lean:40).
1. `2 < lam` can be weakened to `1 < lam` with the identical proof.
2. `0 ≤ x` and `x ≤ 2` are both necessary: counterexamples at x = -1 and x = 3 (lam = 3). -/

example {lam x : ℝ} (hlam : 1 < lam) (hx0 : 0 ≤ x) (hx2 : x ≤ 2) :
    (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1) := by
  have ha : 0 < lam - 1 + x := by linarith
  have hb : 0 < lam - 1 + (2 - x) := by linarith
  rw [inv_add_inv ha.ne' hb.ne', div_le_div_iff₀ (mul_pos ha hb) (by nlinarith)]
  nlinarith [mul_nonneg hx0 (sub_nonneg.2 hx2)]

-- x = -1, lam = 3: LHS = 1 + 1/5 = 6/5 > 3/4 = RHS
example : ¬ (((3 : ℝ) - 1 + (-1))⁻¹ + (3 - 1 + (2 - (-1)))⁻¹ ≤ 2 * 3 / (3 ^ 2 - 1)) := by
  norm_num

-- x = 3, lam = 3 (symmetric)
example : ¬ (((3 : ℝ) - 1 + 3)⁻¹ + (3 - 1 + (2 - 3))⁻¹ ≤ 2 * 3 / (3 ^ 2 - 1)) := by
  norm_num
