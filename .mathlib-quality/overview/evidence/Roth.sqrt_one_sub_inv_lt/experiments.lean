import Roth.Lattice

open Real

/-! Experiments for `Roth.sqrt_one_sub_inv_lt`. -/

/-- Weakening 1: real `m` with `1 ≤ m` (hypothesis `2 ≤ m` and the ℕ-cast both superfluous). -/
theorem sqrt_one_sub_inv_lt_real {m : ℝ} (hm : 1 ≤ m) {lam : ℝ} (hlam : 2 * √m < lam) :
    √(1 - 1 / m) < 1 - lam⁻¹ ^ 2 := by
  have hsq : 4 * m < lam ^ 2 := by
    nlinarith [Real.sqrt_nonneg m, Real.sq_sqrt (by linarith : (0 : ℝ) ≤ m)]
  have hu : lam⁻¹ ^ 2 < 1 / m / 4 := by
    rw [inv_pow, div_div, ← one_div]
    exact one_div_lt_one_div_of_lt (by positivity) (by linarith)
  have h1 : 1 / m ≤ 1 := by rw [div_le_one (by linarith)]; exact hm
  have hpos : 0 < 1 / m := by positivity
  -- mathlib building block: √(1 + x) ≤ 1 + x / 2
  calc √(1 - 1 / m) = √(1 + -(1 / m)) := by rw [sub_eq_add_neg]
    _ ≤ 1 + -(1 / m) / 2 := Real.sqrt_one_add_le (by linarith)
    _ < 1 - lam⁻¹ ^ 2 := by linarith

/-- The project statement as a one-line corollary of the real version (with `2 ≤ m`). -/
example {m : ℕ} (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2 :=
  sqrt_one_sub_inv_lt_real (by exact_mod_cast (by omega : 1 ≤ m)) hlam

/-- Weakening 2: ℕ form with `1 ≤ m` (m = 1 is fine: √0 = 0 < 1 - λ⁻², λ > 2). -/
example {m : ℕ} (hm : 1 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2 :=
  sqrt_one_sub_inv_lt_real (by exact_mod_cast hm) hlam

/-- `1 ≤ m` cannot be dropped entirely: m = 1/100, λ = 1/2 > 2 √(1/100) = 1/5 is a
counterexample (LHS = √(1 - 100) = 0, RHS = 1 - 4 = -3). -/
example : ¬ (√(1 - 1 / (1/100 : ℝ)) < 1 - (1/2 : ℝ)⁻¹ ^ 2) := by
  norm_num; exact le_trans (by norm_num) (Real.sqrt_nonneg _)
