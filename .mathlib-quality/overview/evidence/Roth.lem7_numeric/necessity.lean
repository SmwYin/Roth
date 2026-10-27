import Roth.Theta

/-! Necessity of the hypotheses of `Roth.lem7_numeric`. Each `example` shows that the
conclusion fails when one hypothesis is dropped (the remaining hypotheses hold). -/

open Real

/-- `hp : 2 ≤ p` is necessary: at `p = 1`, `δ = 1`, `Φ = 3` the hypothesis `hΦ` holds with
equality but `2 (Φ + √Φ + √δ) = 8 + 2√3 > 10`. -/
example : ¬ (2 * ((3 : ℝ) + √3 + √1) < 10 ^ 1 * (1 : ℝ) ^ ((1 / 2 : ℝ) ^ 1)) := by
  have h3 : (1 : ℝ) < √3 := by
    rw [show (1 : ℝ) = √1 by simp]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  rw [Real.one_rpow, Real.sqrt_one]
  linarith

example : (3 : ℝ) ≤ 3 * 10 ^ (1 - 1) * (1 : ℝ) ^ ((1 / 2 : ℝ) ^ (1 - 1)) := by simp

/-- `hδ0 : 0 < δ` is necessary: at `δ = 0`, `Φ = 0` both sides are `0`. -/
example : ¬ (2 * ((0 : ℝ) + √0 + √0) < 10 ^ 2 * (0 : ℝ) ^ ((1 / 2 : ℝ) ^ 2)) := by
  rw [Real.zero_rpow (by positivity)]
  simp

/-- `hδ1 : δ ≤ 1` cannot be dropped: at `p = 2`, `δ = 16`, `Φ = 3·10·16^{1/2} = 120`
the left side is `> 240` while the right side is `100 · 16^{1/4} = 200`. -/
example : ¬ (2 * ((120 : ℝ) + √120 + √16) < 10 ^ 2 * (16 : ℝ) ^ ((1 / 2 : ℝ) ^ 2)) := by
  have h16 : (16 : ℝ) ^ ((1 / 2 : ℝ) ^ 2) = 2 := by
    rw [show (16 : ℝ) = 2 ^ (4 : ℝ) by norm_num, ← Real.rpow_mul (by norm_num)]
    norm_num
  rw [h16]
  have := Real.sqrt_nonneg 120
  have := Real.sqrt_nonneg 16
  linarith

example : (120 : ℝ) ≤ 3 * 10 ^ (2 - 1) * (16 : ℝ) ^ ((1 / 2 : ℝ) ^ (2 - 1)) := by
  have h : (16 : ℝ) ^ ((1 / 2 : ℝ) ^ (2 - 1)) = 4 := by
    rw [show (16 : ℝ) = 4 ^ (2 : ℝ) by norm_num, ← Real.rpow_mul (by norm_num)]
    norm_num
  rw [h]; norm_num

/-- Sanity instantiation of the original statement. -/
example {δ Φ : ℝ} (h0 : 0 < δ) (h1 : δ ≤ 1)
    (hΦ : Φ ≤ 3 * 10 ^ (2 - 1) * δ ^ ((1 / 2 : ℝ) ^ (2 - 1))) :
    2 * (Φ + √Φ + √δ) < 10 ^ 2 * δ ^ ((1 / 2 : ℝ) ^ 2) :=
  Roth.lem7_numeric le_rfl h0 h1 hΦ
