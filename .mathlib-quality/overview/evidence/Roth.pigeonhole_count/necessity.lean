import Roth.MainLemma

/-! Necessity of the hypotheses of `Roth.pigeonhole_count`. Each `example` instantiates the
remaining hypotheses and shows the conclusion fails when one hypothesis is dropped. -/

/-- `hB : 0 < B` is necessary: `B = 0`, `c = 1`, `n = D = 1`, `N = 2` satisfies `hc`, `hN`,
`hD` (`1 ≤ 1`), but both sides equal `1`. -/
example : (1 : ℝ) * 1 * 1 ≤ ((2 : ℕ) : ℝ) / 2 ∧
    ¬ (((2 * ⌊(0 : ℝ) ^ (1 : ℝ)⌋₊ + 1 : ℕ) : ℝ) ^ (1 * 1) < ((0 : ℝ) + 1) ^ 2) := by
  refine ⟨by norm_num, ?_⟩
  rw [Real.rpow_one]
  simp

/-- `hc : 1 ≤ c` cannot be dropped: `B = 1`, `c = 1/2`, `n = D = N = 1` satisfies `hB`, `hN`,
`hD` (`1/2 ≤ 1/2`), but the left side is `3` and the right side is `2`. -/
example : (1 / 2 : ℝ) * (1 : ℕ) * (1 : ℕ) ≤ ((1 : ℕ) : ℝ) / 2 ∧
    ¬ (((2 * ⌊(1 : ℝ) ^ (1 / 2 : ℝ)⌋₊ + 1 : ℕ) : ℝ) ^ (1 * 1) < ((1 : ℝ) + 1) ^ 1) := by
  refine ⟨by norm_num, ?_⟩
  rw [Real.one_rpow]
  norm_num

/-- `hN : 0 < N` is necessary: `n = D = N = 0` (any `B`, `c`) makes both sides `1`. -/
example (B c : ℝ) : c * (0 : ℕ) * (0 : ℕ) ≤ ((0 : ℕ) : ℝ) / 2 ∧
    ¬ (((2 * ⌊B ^ c⌋₊ + 1 : ℕ) : ℝ) ^ (0 * 0) < (B + 1) ^ 0) := by
  simp

/-- `hD` is necessary: `B = 1`, `c = 1`, `n = D = N = 1` gives `3 < 2`, false. -/
example : ¬ (((2 * ⌊(1 : ℝ) ^ (1 : ℝ)⌋₊ + 1 : ℕ) : ℝ) ^ (1 * 1) < ((1 : ℝ) + 1) ^ 1) := by
  rw [Real.one_rpow]
  norm_num

/-- `c ≥ 1` is not sharp but any admissible threshold exceeds `log 3 / log 4 ≈ 0.79`
(take `B = 1`); the sanity instantiation of the original statement: -/
example : ((2 * ⌊(3 : ℝ) ^ (1 : ℝ)⌋₊ + 1 : ℕ) : ℝ) ^ (2 * 1) < ((3 : ℝ) + 1) ^ 4 :=
  Roth.pigeonhole_count (by norm_num) le_rfl (by norm_num) (by norm_num)
