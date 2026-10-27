import Mathlib

/-! Evidence for `Roth.exists_degrees` (Roth/Main.lean:282). Self-contained (statement shape
copied), so only Mathlib is imported. -/

/-- Converse: the conclusion (in fact just eqs. (33) and (53)) forces `0 < δ` and `1 < q j`
for every `j`, so `hδ0` and `hq` are necessary. -/
theorem exists_degrees_converse {m : ℕ} [NeZero m] {δ : ℝ} {q : Fin m → ℕ} (r : Fin m → ℕ)
    (h33 : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j))
    (h53 : ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))) :
    0 < δ ∧ ∀ j, 1 < q j := by
  have hnn : ∀ j, 0 ≤ Real.log (q j) := fun j ↦ Real.log_natCast_nonneg _
  have h0 := h53 0
  have hpos : 0 < (r 0 : ℝ) * Real.log (q 0) := by
    by_contra h
    have : (r 0 : ℝ) * Real.log (q 0) = 0 :=
      le_antisymm (not_lt.1 h) (mul_nonneg (Nat.cast_nonneg _) (hnn 0))
    rw [this] at h0; simp at h0
  refine ⟨?_, fun j ↦ ?_⟩
  · nlinarith
  · have hj : 0 < Real.log (q j) := by
      by_contra h
      have : Real.log (q j) = 0 := le_antisymm (not_lt.1 h) (hnn j)
      have := h33 j; rw [‹Real.log (q j) = 0›, mul_zero] at this; linarith
    by_contra h
    push Not at h
    interval_cases hq : q j <;> simp at hj

/-- `h50` cannot be dropped: with `m = 2`, `q = (2, 2)`, `δ = 1` the conclusion fails
((31b) gives `r 1 < r 0`, (33) gives `r 0 ≤ r 1`). -/
theorem exists_degrees_needs_h50 : ¬ ∃ r : Fin 2 → ℕ,
    (∀ i j : Fin 2, i.val + 1 = j.val → (r j : ℝ) / 1 < r i) ∧
    (∀ j, (r 0 : ℝ) * Real.log ((fun _ ↦ 2 : Fin 2 → ℕ) 0) ≤
      r j * Real.log ((fun _ ↦ 2 : Fin 2 → ℕ) j)) := by
  rintro ⟨r, h31b, h33⟩
  have h1 := h31b 0 1 rfl
  have h2 := h33 1
  have hl : 0 < Real.log 2 := Real.log_pos (by norm_num)
  simp only [Nat.cast_ofNat, div_one] at h1 h2
  have := le_of_mul_le_mul_right h2 hl
  linarith
