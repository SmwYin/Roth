import Roth.Index

open MvPolynomial Roth

/-! Evidence for `Roth.index_sub_weight_le_index_hasseDeriv`. -/

/-- (1) Direct proof without the sibling attained-minimum lemmas: unfold to `sInf` and use
`csInf_le`, `Set.Nonempty.csInf_mem`, `coeff_taylor`, `hasseDeriv_hasseDeriv`. -/
example {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ}
    (hk : hasseDeriv k P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r - weight r k ≤ index (hasseDeriv k P) α r := by
  obtain ⟨i, hi, hiw⟩ :=
    (show (weight r '' ((taylor α (hasseDeriv k P)).support : Set (σ →₀ ℕ))).Nonempty by
      simpa using hk).csInf_mem ((taylor α _).support.finite_toSet.image (weight r))
  rw [Finset.mem_coe, mem_support_iff, coeff_taylor, hasseDeriv_hasseDeriv, smul_eq_C_mul,
    map_mul, eval_C, mul_ne_zero_iff] at hi
  have hmem : i + k ∈ (taylor α P).support := by
    rw [mem_support_iff, coeff_taylor]; exact hi.2
  have := csInf_le ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
    (Set.mem_image_of_mem (weight r) (Finset.mem_coe.2 hmem))
  rw [index, index, ← hiw]
  rw [weight_add] at this
  linarith

/-- (2) Re-aim at mathlib's canonical object: the weighted order of the Taylor expansion,
over any commutative semiring, with no nonvanishing hypothesis (the `⊤` convention). -/
example {σ R : Type*} [CommSemiring R] (w : σ → ℕ) (P : MvPolynomial σ R) (k : σ →₀ ℕ)
    (α : σ → R) :
    (taylor α P : MvPowerSeries σ R).weightedOrder w ≤
      (taylor α (hasseDeriv k P) : MvPowerSeries σ R).weightedOrder w + Finsupp.weight w k := by
  set F : MvPowerSeries σ R := ↑(taylor α (hasseDeriv k P))
  by_cases hF : F = 0
  · simp [hF]
  obtain ⟨d, hd, hdw⟩ := MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder w (f := F)
    ((MvPowerSeries.ne_zero_iff_weightedOrder_finite w).1 hF)
  rw [← hdw]
  have hd' : MvPowerSeries.coeff (d + k) (taylor α P : MvPowerSeries σ R) ≠ 0 := by
    simp only [F, MvPolynomial.coeff_coe, coeff_taylor, hasseDeriv_hasseDeriv] at hd ⊢
    intro h0
    exact hd (by rw [smul_eq_C_mul, map_mul, h0, mul_zero])
  calc _ ≤ ((Finsupp.weight w (d + k) : ℕ) : ℕ∞) := MvPowerSeries.weightedOrder_le w hd'
    _ = _ := by rw [map_add, Nat.cast_add]

/-- (3) `hk` is necessary: for `P = X 0` in two variables, `k = single 1 1`, `r = ![1, 2]`,
`α = 0`, we have `Δ_k P = 0`, `index P = 1`, `weight r k = 1/2`, so the inequality fails. -/
example : ¬ ∀ (P : MvPolynomial (Fin 2) ℝ) (k : Fin 2 →₀ ℕ) (α : Fin 2 → ℝ) (r : Fin 2 → ℕ),
    index P α r - weight r k ≤ index (hasseDeriv k P) α r := by
  intro h
  have hP : (X 0 : MvPolynomial (Fin 2) ℝ) = rename (fun _ : Unit ↦ (0 : Fin 2)) (X ()) := by
    simp
  have hidx : index (X 0 : MvPolynomial (Fin 2) ℝ) 0 ![1, 2] = 1 := by
    rw [hP, index_rename (fun _ _ _ ↦ rfl), index_unique (X_ne_zero ())]
    change (Polynomial.rootMultiplicity (0 : ℝ) (eval₂ (Polynomial.C : ℝ →+* Polynomial ℝ)
      (fun _ ↦ Polynomial.X) (X () : MvPolynomial Unit ℝ)) : ℝ) / _ = 1
    rw [eval₂_X]
    simpa using Polynomial.rootMultiplicity_X_sub_C_self (x := (0 : ℝ))
  have hzero : hasseDeriv (Finsupp.single 1 1) (X 0 : MvPolynomial (Fin 2) ℝ) = 0 :=
    hasseDeriv_eq_zero_of_degreeOf_lt (j := 1) (by simp [degreeOf_X])
  have hw : weight ![1, 2] (Finsupp.single (1 : Fin 2) 1) = 1 / 2 := by
    simp [weight_single]
  have := h (X 0) (Finsupp.single 1 1) 0 ![1, 2]
  rw [hzero, hidx, hw] at this
  simp [index] at this
  linarith
