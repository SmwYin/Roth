import Mathlib

/-! Evidence for `Roth.exists_m` (Roth/Main.lean:196). Self-contained (imports only Mathlib):
the declaration's statement is pure real arithmetic. -/

/-- (1) The second conjunct `4 n √m < m` follows from the first, `16 n² < m`. -/
example {n m : ℕ} (hm : 16 * n ^ 2 < m) : 4 * n * √(m : ℝ) < m := by
  have hm' : ((4 * n : ℕ) : ℝ) ^ 2 < (m : ℝ) := by exact_mod_cast (by nlinarith : (4 * n) ^ 2 < m)
  have hlt : (4 * n : ℝ) < √(m : ℝ) := by
    have := Real.lt_sqrt_of_sq_lt hm'; push_cast at this; exact this
  have hpos : 0 < √(m : ℝ) := (by positivity : (0 : ℝ) ≤ 4 * n).trans_lt hlt
  calc 4 * n * √(m : ℝ) < √(m : ℝ) * √(m : ℝ) := mul_lt_mul_of_pos_right hlt hpos
    _ = m := Real.mul_self_sqrt (Nat.cast_nonneg m)

/-- (2) The hypothesis `2 < κ` is necessary: the conclusion forces it. -/
example {n : ℕ} {κ : ℝ} (h : ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧
    2 * m / (m - 4 * n * √(m : ℝ)) < κ) : 2 < κ := by
  obtain ⟨m, -, h2, h3⟩ := h
  have hd : 0 < (m : ℝ) - 4 * n * √(m : ℝ) := sub_pos.2 h2
  have hnn : 0 ≤ 4 * (n : ℝ) * √(m : ℝ) := by positivity
  refine lt_of_le_of_lt ?_ h3
  rw [le_div_iff₀ hd]
  nlinarith
