import Roth.MainLemma

/-! Evidence for `Roth.exists_delta` (Roth/Main.lean:227): both hypotheses are necessary.
The conclusion of `exists_delta` implies `16 * n ^ 2 < m` and the eq. (47) bound
`2 * m / (m - 4 * n * √m) < κ`. -/

namespace Roth

theorem exists_delta_converse {n m : ℕ} {κ : ℝ} (h : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
    (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ) :
    16 * n ^ 2 < m ∧ 2 * m / (m - 4 * n * √(m : ℝ)) < κ := by
  obtain ⟨δ, hδ, hδm, h30, h49⟩ := h
  have heta : 0 < eta δ m := by unfold eta; positivity
  have hm : (0 : ℝ) < m := by
    by_contra h0
    have : (m : ℝ) = 0 := le_antisymm (not_lt.mp h0) (Nat.cast_nonneg m)
    simp [this] at hδm; linarith
  have hsq := Real.sq_sqrt hm.le
  have hs := Real.sqrt_nonneg (m : ℝ)
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have h4 : 4 * n * √(m : ℝ) < m := by
    nlinarith [mul_nonneg hn hs, mul_nonneg (mul_nonneg hδ.le hn) hs]
  refine ⟨?_, ?_⟩
  · have : (16 * n ^ 2 : ℝ) * m < m * m := by
      nlinarith [mul_pos (sub_pos.mpr h4) (by positivity : (0 : ℝ) < m + 4 * n * √(m : ℝ))]
    exact_mod_cast lt_of_mul_lt_mul_right this hm.le
  · have hgap : 0 < gam δ n m - eta δ m := sub_pos.mpr ((eta_lt_gam_iff δ n m).mp h30)
    refine lt_of_le_of_lt ?_ h49
    have hle : gam δ n m - eta δ m ≤ (m - 4 * n * √(m : ℝ)) / 2 := by
      unfold gam lam; nlinarith [mul_nonneg (mul_nonneg hδ.le hn) hs]
    calc 2 * (m : ℝ) / (m - 4 * n * √(m : ℝ)) = m / ((m - 4 * n * √(m : ℝ)) / 2) := by
          field_simp
      _ ≤ (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) :=
          div_le_div₀ (by positivity) (by nlinarith) hgap hle

end Roth
