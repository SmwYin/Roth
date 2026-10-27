import Roth.Theta

/-! Evidence for `Roth.mul_sq_div_three_le_sum_max_aux` (Roth/Theta.lean:347).
Its only caller `min_le_sum_max` passes a *strict* hypothesis `θ * rp < l`, so the
equality branch (which calls `mul_div_two_le_sum_max_aux`) is dead from the call site.
Test: `min_le_sum_max` proved with the aux inlined (r ≤ 0 split + strict case only).
The two private helpers are copied verbatim from Roth/Theta.lean (they use only mathlib). -/

namespace RothEvidence

lemma mul_div_two_le_sum_max_aux {θ r : ℝ} {l : ℕ} (hl : (l : ℝ) ≤ θ * r) :
    l * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) := by
  rcases Nat.eq_zero_or_pos l with rfl | hl0
  · simp
  by_cases hθ : θ ≤ 0
  · exact (div_nonpos_of_nonpos_of_nonneg
      (mul_nonpos_of_nonneg_of_nonpos (Nat.cast_nonneg l) hθ) (by norm_num)).trans
        (Finset.sum_nonneg fun _ _ ↦ le_max_left _ _)
  have hr := pos_of_mul_pos_right ((Nat.cast_pos.mpr hl0).trans_le hl) (le_of_not_ge hθ)
  have hsum := congrArg (Nat.cast (R := ℝ)) (Finset.sum_range_id_mul_two l)
  push_cast [Nat.cast_sub hl0] at hsum
  refine le_trans ?_ (Finset.sum_le_sum fun ν _ ↦ le_max_right 0 (θ - ν / r))
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul,
    ← Finset.sum_div, le_sub_iff_add_le, div_add_div _ _ (by norm_num) hr.ne',
    div_le_iff₀ (by positivity)]
  linarith only [hsum, (Nat.cast_nonneg l : (0 : ℝ) ≤ l),
    mul_nonneg (Nat.cast_nonneg l) (sub_nonneg.mpr hl)]

lemma mul_sq_div_three_le_sum_max_of_pos_aux {θ r : ℝ} (hr : 0 < r) (hθ : 0 ≤ θ) {l : ℕ}
    (hl : θ * r < l) : r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) := by
  set n := ⌊θ * r⌋₊
  have hnle : (n : ℝ) ≤ θ * r := Nat.floor_le (mul_nonneg hθ hr.le)
  have hnlt : θ * r < n + 1 := Nat.lt_floor_add_one _
  have hsum := congrArg (Nat.cast (R := ℝ)) (Finset.sum_range_id_mul_two (n + 1))
  push_cast [Nat.add_sub_cancel] at hsum
  have hbound : (θ * r) ^ 2 / 3 ≤ ∑ ν ∈ Finset.range (n + 1), (θ * r - ν) := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    push_cast
    generalize θ * r = a at hnle hnlt ⊢
    linear_combination hsum / 2 + sq_nonneg a / 6 + (le_trans (Nat.cast_nonneg n) hnle) / 2 +
      mul_nonneg (sub_nonneg.mpr hnle) (sub_nonneg.mpr hnlt.le) / 2
  calc
    r * θ ^ 2 / 3 = (θ * r) ^ 2 / 3 / r := (eq_div_iff hr.ne').2 (by ring)
    _ ≤ (∑ ν ∈ Finset.range (n + 1), (θ * r - ν)) / r :=
      (div_le_div_iff_of_pos_right hr).2 hbound
    _ ≤ ∑ ν ∈ Finset.range (n + 1), max 0 (θ - ν / r) := by
      simp only [Finset.sum_div, sub_div, mul_div_cancel_right₀ _ hr.ne']
      exact Finset.sum_le_sum fun ν _ ↦ le_max_right _ _
    _ ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) :=
      Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_subset_range.2
        ((Nat.floor_lt (mul_nonneg hθ hr.le)).2 hl))
        fun _ _ _ ↦ le_max_left _ _

/-- `min_le_sum_max` with `mul_sq_div_three_le_sum_max_aux` inlined: no equality branch. -/
theorem min_le_sum_max' {θ : ℝ} {rp : ℕ} (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) := by
  have h0 : 0 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) :=
    Finset.sum_nonneg fun _ _ ↦ le_max_left _ _
  by_cases hθ : θ ≤ 0
  · exact (min_le_left _ _).trans ((div_nonpos_of_nonpos_of_nonneg
      (mul_nonpos_of_nonneg_of_nonpos (Nat.cast_nonneg l) hθ) (by norm_num)).trans h0)
  rcases le_or_gt (l : ℝ) (θ * rp) with hl | hl
  · exact (min_le_left _ _).trans (mul_div_two_le_sum_max_aux hl)
  rcases Nat.eq_zero_or_pos rp with rfl | hrp
  · exact (min_le_right _ _).trans (by simpa using h0)
  exact (min_le_right _ _).trans
    (mul_sq_div_three_le_sum_max_of_pos_aux (by exact_mod_cast hrp) (le_of_not_ge hθ) hl)

end RothEvidence
