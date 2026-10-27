import Roth.MainLemma
import Mathlib.Analysis.Complex.ExponentialBounds

/-! Evidence for the /overview assessment of `Roth.three_small_factors`.
Each hypothesis `hA`, `hδ0`, `hr₁` is necessary: dropping it admits a counterexample in
which `h32` holds but the first conjunct fails. -/

open Roth

lemma one_lt_log_three : 1 < Real.log 3 := by
  rw [Real.lt_log_iff_exp_lt (by norm_num)]
  exact Real.exp_one_lt_three

-- (1) `hA : 0 ≤ A` is necessary: A = e^{-2} - 1 < 0, δ = m = r₁ = 1, q₁ = 1, α = 0.
example : let A := Real.exp (-2) - 1
    A < 0 ∧
    2 * (1 : ℕ) + 1 + 2 * (1 : ℕ) * Real.log (1 + A) + 2 * (1 : ℕ) * Real.log (1 + |(0 : ℝ)|) ≤
      (1 : ℝ) ^ 2 * Real.log (1 : ℕ) ∧
    ¬ ((2 : ℝ) ^ ((1 : ℕ) * (1 : ℕ)) < (mainCoeffBound 1 1 1 : ℝ) ^ (1 : ℝ)) := by
  intro A
  refine ⟨by simp only [A]; linarith [Real.exp_lt_one_iff.2 (by norm_num : (-2 : ℝ) < 0)], ?_, ?_⟩
  · simp only [A, add_sub_cancel, Real.log_exp]; norm_num
  · simp [mainCoeffBound]

-- (2) `hδ0 : 0 ≤ δ` is necessary: δ = -1, m = 0, q₁ = 3, r₁ = 1, A = α = 0.
example :
    2 * (0 : ℕ) + 1 + 2 * (0 : ℕ) * Real.log (1 + 0) + 2 * (0 : ℕ) * Real.log (1 + |(0 : ℝ)|) ≤
      (-1 : ℝ) ^ 2 * Real.log (3 : ℕ) ∧
    ¬ ((2 : ℝ) ^ ((0 : ℕ) * (1 : ℕ)) < (mainCoeffBound (-1) 3 1 : ℝ) ^ (-1 : ℝ)) := by
  refine ⟨by norm_num; exact one_lt_log_three.le, ?_⟩
  have : mainCoeffBound (-1) 3 1 = 0 := by
    rw [mainCoeffBound, Nat.floor_eq_zero]; norm_num [Real.rpow_neg_one]
  simp [this]

-- (3) `hr₁ : 0 < r₁` is necessary: r₁ = 0, δ = 1, m = 0, q₁ = 3, A = α = 0.
example :
    2 * (0 : ℕ) + 1 + 2 * (0 : ℕ) * Real.log (1 + 0) + 2 * (0 : ℕ) * Real.log (1 + |(0 : ℝ)|) ≤
      (1 : ℝ) ^ 2 * Real.log (3 : ℕ) ∧
    ¬ ((2 : ℝ) ^ ((0 : ℕ) * (0 : ℕ)) < (mainCoeffBound 1 3 0 : ℝ) ^ (1 : ℝ)) := by
  refine ⟨by norm_num; exact one_lt_log_three.le, ?_⟩
  simp [mainCoeffBound]

#check @three_small_factors
