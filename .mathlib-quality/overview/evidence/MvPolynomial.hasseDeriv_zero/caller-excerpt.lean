theorem le_index_iff {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {α : σ → ℝ} {r : σ → ℕ} {c : ℝ} :
    c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by
  refine ⟨fun h d hd ↦ h.trans (index_le_weight hd), fun h ↦ ?_⟩
  refine le_csInf (by simpa using hP) ?_
  rintro _ ⟨d, hd, rfl⟩
  exact h d (mem_support_taylor_iff.1 hd)

/-- The index is nonnegative. Source: §4, first lemma on the index ("We have `ind(P) ≥ 0`"). -/
theorem index_nonneg (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r :=
  Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)

/-- For nonzero `P` and positive weights, the index vanishes iff `P(α) ≠ 0`.
Source: §4, first lemma on the index ("`ind(P) = 0` if and only if `P(α_1, …, α_p) ≠ 0`"). -/
theorem index_eq_zero_iff {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j)
    (α : σ → ℝ) : index P α r = 0 ↔ eval α P ≠ 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ (index_nonneg P α r).antisymm' ?_⟩
  · obtain ⟨d, hd, hdw⟩ := exists_weight_eq_index hP α r
    rw [h, weight_eq_zero_iff hr] at hdw
    subst hdw
    simpa [hasseDeriv_zero_apply] using hd
  · simpa using index_le_weight (r := r) (d := 0) (by simpa [hasseDeriv_zero_apply] using h)

/-- Applying `Δ_k` lowers the index by at most the weight of `k`.
