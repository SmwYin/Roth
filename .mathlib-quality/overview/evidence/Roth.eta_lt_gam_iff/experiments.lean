import Roth.MainLemma

namespace Roth

/-! (1) Composition: `gam` is `m/2 - 2(1+3δ)n√m` after unfolding, then mathlib's
`lt_sub_iff_add_lt` closes the iff. -/
theorem gam_eq_evid (δ : ℝ) (n m : ℕ) :
    gam δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √(m : ℝ) := by
  unfold gam lam; ring

example (δ : ℝ) (n m : ℕ) : eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔
    eta δ m < gam δ n m := by
  rw [gam_eq_evid]; exact lt_sub_iff_add_lt.symm

/-! (2) Alternative shape used by both callers (`sub_pos.mpr (… .mp h)`): positivity
of the gap `γ - η`. -/
example (δ : ℝ) (n m : ℕ) : eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔
    0 < gam δ n m - eta δ m :=
  (eta_lt_gam_iff δ n m).trans sub_pos.symm

end Roth
