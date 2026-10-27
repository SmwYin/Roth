import Roth.Lattice

/-! Evidence for `Roth.card_filter_weight_le`: the hypothesis `hr : ∀ j, 0 < r j` cannot be
dropped. Counterexample: `m = 9`, `r = 0`, `λ = 7` (so `2 √9 = 6 < 7 ≤ 9`). The box is `{0}`,
whose weight `0 ≤ (9 - 7)/2`, so the count is `1`, but the bound is `2 · 3 / 7 · 1 < 1`. -/

open Roth Finset

example : ¬ ∀ (m : ℕ) (r : Fin m → ℕ) {lam : ℝ}, 0 < lam →
    (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤
      2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by
  intro h
  have h9 := h 9 (fun _ ↦ 0) (lam := 7) (by norm_num)
  have hfilt : ((box (fun _ : Fin 9 ↦ 0)).filter fun d ↦
      weight (fun _ : Fin 9 ↦ 0) d ≤ (((9 : ℕ) : ℝ) - 7) / 2) = box (fun _ : Fin 9 ↦ 0) :=
    Finset.filter_true_of_mem fun d _ ↦ by simp [weight]; norm_num
  rw [hfilt, card_box] at h9
  have hs : √((9 : ℕ) : ℝ) = 3 := by
    rw [show ((9 : ℕ) : ℝ) = 3 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  rw [hs] at h9
  norm_num at h9
