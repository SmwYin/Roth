import Roth.Main

/-! Evidence for `Roth.approxSet_den_le_finite`.

1. Generic per-denominator finiteness from mathlib's `Int.tendsto_coe_cofinite`.
2. An alternative proof of the project statement by a finite union over denominators
   (the same shape as mathlib's `Rat.finite_rat_abs_sub_lt_one_div_den_sq`). -/

open Set Metric

/-- For fixed `q > 0` and any bound `r`, only finitely many `h : ℤ` satisfy `|α - h/q| < r`. -/
theorem finite_int_abs_sub_div_lt (α r : ℝ) {q : ℕ} (hq : 0 < q) :
    {h : ℤ | |α - (h : ℝ) / q| < r}.Finite := by
  have hqR : (0 : ℝ) < q := by exact_mod_cast hq
  have key := Filter.mem_cofinite.1
    (Int.tendsto_coe_cofinite (isCompact_closedBall ((q : ℝ) * α) (q * r)).compl_mem_cocompact)
  refine key.subset fun h hh => ?_
  simp only [mem_ofPred_eq] at hh
  simp only [mem_compl_iff, mem_preimage, not_not, mem_closedBall, Real.dist_eq]
  have : |(h : ℝ) - q * α| = q * |α - h / q| := by
    rw [abs_sub_comm, ← abs_of_pos hqR, ← abs_mul, abs_of_pos hqR, mul_sub,
      mul_div_cancel₀ _ hqR.ne']
  rw [this]
  exact mul_le_mul_of_nonneg_left hh.le hqR.le

/-- The project statement from (1) by a finite union over `q ∈ [1, Q₀]`. -/
example (α κ : ℝ) (Q₀ : ℕ) : {hq ∈ Roth.approxSet α κ | hq.2 ≤ Q₀}.Finite := by
  refine ((finite_Icc 1 Q₀).biUnion fun q hq =>
    (finite_int_abs_sub_div_lt α (1 / (q : ℝ) ^ κ) hq.1).prod (finite_singleton q)).subset ?_
  rintro ⟨h, q⟩ ⟨⟨hq0, happ⟩, hqQ⟩
  exact mem_biUnion (x := q) ⟨hq0, hqQ⟩ ⟨happ, rfl⟩

/-- Reference: the project lemma itself. -/
example (α κ : ℝ) (Q₀ : ℕ) : {hq ∈ Roth.approxSet α κ | hq.2 ≤ Q₀}.Finite :=
  Roth.approxSet_den_le_finite α κ Q₀
