import Roth.MainLemma

/-! Evidence for `Roth.exists_delta_bound`: hypothesis necessity and filter-form restatement. -/

open Filter Topology

namespace Roth

/-- (1) Necessity of `hm`: the conclusion at `δ = 0` alone forces `16 n² < m`,
so the hypothesis cannot be weakened (the source's "precisely when"). -/
example {n m : ℕ} (h : ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 ≤ δ → δ ≤ δ₀ → δ < 1 / m ∧
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2) : 16 * n ^ 2 < m := by
  obtain ⟨δ₀, hδ₀, h⟩ := h
  have h0 := (h 0 le_rfl hδ₀.le).2
  simp only [eta, Real.zero_rpow (by positivity : (1 / 2 : ℝ) ^ m ≠ 0), mul_zero,
    zero_add, mul_zero, add_zero, mul_one] at h0
  have hm0 : (0 : ℝ) < m := by
    by_contra hc
    have : (m : ℝ) = 0 := le_antisymm (not_lt.mp hc) (Nat.cast_nonneg _)
    simp [this] at h0
  have hs := Real.sq_sqrt hm0.le
  have hsq : 0 < √(m : ℝ) := Real.sqrt_pos.mpr hm0
  have : 4 * (n : ℝ) < √(m : ℝ) := by nlinarith
  have : (16 * n ^ 2 : ℝ) < m := by nlinarith
  exact_mod_cast this

/-- (2) Filter-form restatement (modern idiom), derived from the project statement. -/
example {n m : ℕ} (hm : 16 * n ^ 2 < m) : ∀ᶠ δ : ℝ in 𝓝[≥] (0 : ℝ),
    δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 := by
  obtain ⟨δ₀, hδ₀, h⟩ := exists_delta_bound hm
  filter_upwards [self_mem_nhdsWithin, Ico_mem_nhdsGE hδ₀] with δ hδ hδ'
  exact h δ hδ hδ'.2.le

end Roth
