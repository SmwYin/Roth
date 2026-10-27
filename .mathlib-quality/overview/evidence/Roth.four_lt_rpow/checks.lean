import Roth.MainLemma
import Mathlib.Analysis.Complex.ExponentialBounds

/-! Evidence for the /overview assessment of `Roth.four_lt_rpow`. -/

-- (1) `hδ0 : 0 ≤ δ` is needed: δ = -2, q₁ = 3, r₁ = 1 satisfies `3 ≤ δ² log q₁`
--     but `3 ^ (-2) < 4`.
example : 3 ≤ (-2 : ℝ) ^ 2 * Real.log (3 : ℕ) ∧ ¬ (4 < ((3 : ℕ) : ℝ) ^ ((-2 : ℝ) * (1 : ℕ))) := by
  constructor
  · have h : (1 : ℝ) < Real.log 3 := by
      rw [Real.lt_log_iff_exp_lt (by norm_num)]
      linarith [Real.exp_one_lt_d9]
    push_cast; nlinarith
  · push_cast
    rw [not_lt]
    have : (3 : ℝ) ^ ((-2 : ℝ) * 1) ≤ 1 :=
      Real.rpow_le_one_of_one_le_of_nonpos (by norm_num) (by norm_num)
    linarith

-- (2) `hr₁ : 0 < r₁` is needed: r₁ = 0 gives `q₁ ^ 0 = 1`.
example : ¬ (4 < ((3 : ℕ) : ℝ) ^ ((2 : ℝ) * (0 : ℕ))) := by
  simp

-- (3) Composition check: mathlib's `Real.lt_rpow_of_log_lt` reduces the goal to
--     `log 4 < δ r₁ log q₁`; the remaining step is a genuine nlinarith argument.
example {δ : ℝ} {q₁ r₁ : ℕ} (hq : 0 < (q₁ : ℝ)) (h : Real.log 4 < δ * r₁ * Real.log q₁) :
    4 < (q₁ : ℝ) ^ (δ * r₁) :=
  Real.lt_rpow_of_log_lt hq (by linarith)

-- (4) `Real.log_two_lt_d9` gives the `log 2 < 3/4` step directly.
example : Real.log 2 < 3 / 4 := by linarith [Real.log_two_lt_d9]

-- (5) Both callers only use `.le` of the conclusion, at thresholds 2 and 1.
#check @Roth.four_lt_rpow
