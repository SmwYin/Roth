import Roth.Lattice

/-! Evidence for `Roth.sum_inv_lt`: both `hr : 1 ≤ r` and `hm : 2 ≤ m` are needed. -/

open Finset

-- `m = 1` (dropping `hm`): the RHS is `λ⁻¹ * (√0)⁻¹ * 1 * (r+1) = 0`, LHS positive.
example : ¬ (∀ {r m : ℕ}, 1 ≤ r → ∀ {lam : ℝ}, 2 * √(m : ℝ) < lam →
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1)) := by
  intro h
  have := @h 1 1 le_rfl 3 (by norm_num)
  norm_num [Finset.sum_range_succ] at this

-- `r = 0` (dropping `hr`), `m = 2`, `λ = 3`: LHS = 1/2, RHS = √2/3 < 1/2.
example : ¬ (∀ {r m : ℕ}, 2 ≤ m → ∀ {lam : ℝ}, 2 * √(m : ℝ) < lam →
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1)) := by
  intro h
  have hs : √(2 : ℝ) < 3 / 2 := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have := @h 0 2 le_rfl 3 (by push_cast; linarith)
  norm_num at this
  linarith

-- Sanity: the project statement as stated.
example {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1) :=
  Roth.sum_inv_lt hr hm hlam
