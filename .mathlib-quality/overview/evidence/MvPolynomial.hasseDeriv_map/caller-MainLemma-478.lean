    {r : σ → ℕ} {α z : σ → ℝ} {C γ c : ℝ} (hP : P ≠ 0) (hd : ∀ j, degreeOf j P ≤ r j)
    (hbound : ∀ i k : σ →₀ ℕ,
      |eval α (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))| < C)
    (hγ : γ ≤ index (map (Int.castRingHom ℝ) P) α r)
    (hz : index (map (Int.castRingHom ℝ) P) z r < c) : ∃ Q : MvPolynomial σ ℤ, Q ≠ 0 ∧
      (∀ j, degreeOf j Q ≤ r j) ∧ γ - c < index (map (Int.castRingHom ℝ) Q) α r ∧
      eval z (map (Int.castRingHom ℝ) Q) ≠ 0 ∧ ∀ i : σ →₀ ℕ,
        |eval α (hasseDeriv i (map (Int.castRingHom ℝ) Q))| < C := by
  obtain ⟨k, hkw, hkev⟩ := exists_hasseDeriv_eval_ne_zero
    ((map_ne_zero_iff _ (MvPolynomial.map_injective _ Int.cast_injective)).2 hP) z r hz
  have hQev : eval z (map (Int.castRingHom ℝ) (hasseDeriv k P)) ≠ 0 := by
    simpa [hasseDeriv_map] using hkev
  refine ⟨hasseDeriv k P, fun h0 ↦ hQev (by rw [h0, map_zero, map_zero]),
    fun j ↦ (degreeOf_hasseDeriv_le j k P).trans (hd j), ?_, hQev, fun i ↦ ?_⟩
  · rw [← hasseDeriv_map]
    exact ((sub_lt_sub_left hkw γ).trans_le (sub_le_sub_right hγ _)).trans_le
      (index_sub_weight_le_index_hasseDeriv (fun h0 ↦ hkev (by rw [h0, map_zero])) α r)
  · simpa [hasseDeriv_map] using hbound i k

