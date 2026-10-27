import Roth.MainLemma

/-! Evidence for `Roth.sqrt_lt_floor`. -/

-- (1) Composition from mathlib only (no project lemma): the strict half needs
-- `Real.sqrt_lt'`, `Nat.le_floor`, `Nat.lt_floor_add_one` plus `nlinarith`;
-- the upper half is `Nat.floor_le`.
example {X : ℝ} (hX : 2 ≤ X) : √X < ⌊X⌋₊ ∧ (⌊X⌋₊ : ℝ) ≤ X := by
  have hf : (2 : ℝ) ≤ ⌊X⌋₊ := by exact_mod_cast Nat.le_floor hX
  exact ⟨(Real.sqrt_lt' (by positivity)).2 (by nlinarith only [Nat.lt_floor_add_one X, hf]),
    Nat.floor_le (by positivity)⟩

-- (2) The threshold `2 ≤ X` cannot be lowered below 2: at `X = 1` the strict half fails.
example : ¬ (√(1 : ℝ) < ((⌊(1 : ℝ)⌋₊ : ℕ) : ℝ)) := by simp

-- (3) The upper half alone only needs `0 ≤ X` (mathlib `Nat.floor_le`).
example {X : ℝ} (hX : 0 ≤ X) : (⌊X⌋₊ : ℝ) ≤ X := Nat.floor_le hX

-- (4) The cheaper `X - 1` route (`Nat.sub_one_lt_floor`) does not suffice at `X = 2`:
-- `√2 > 2 - 1`, so the strict half is not a 1-call consequence of it.
example : (2 : ℝ) - 1 < √2 := by
  rw [show (2 : ℝ) - 1 = √1 by norm_num]
  exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
