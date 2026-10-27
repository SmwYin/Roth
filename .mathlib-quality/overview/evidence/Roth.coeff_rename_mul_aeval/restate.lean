import Roth.Separation

open MvPolynomial

variable {R τ : Type*} [CommSemiring R]

-- (0) signature
#check @Roth.coeff_rename_mul_aeval

-- (1) missing mathlib API, mirror of `sumAlgEquiv_comp_rename_inr`
theorem optionEquivLeft_comp_rename_some :
    (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom := by
  ext i
  simp

theorem optionEquivLeft_rename_some (p : MvPolynomial τ R) :
    optionEquivLeft R τ (rename some p) = Polynomial.C p :=
  AlgHom.congr_fun optionEquivLeft_comp_rename_some p

theorem optionEquivLeft_aeval_X_none (V : Polynomial R) :
    optionEquivLeft R τ (Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      V.map (algebraMap R (MvPolynomial τ R)) := by
  rw [← Polynomial.aeval_algHom_apply, optionEquivLeft_X_none,
    Polynomial.aeval_X_left_eq_map]

-- (2) restatement in mathlib's canonical `optionElim` spelling
theorem coeff_rename_some_mul_aeval_X_none (U : MvPolynomial τ R) (V : Polynomial R)
    (a : τ →₀ ℕ) (b : ℕ) :
    (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V).coeff
      (a.optionElim b) = U.coeff a * V.coeff b := by
  rw [← optionEquivLeft_coeff_coeff, map_mul, optionEquivLeft_rename_some,
    optionEquivLeft_aeval_X_none, Polynomial.coeff_C_mul, Polynomial.coeff_map, algebraMap_eq,
    mul_comm U, coeff_C_mul, mul_comm]

-- (3) literature-standard disjoint-variables form over `σ ⊕ τ`
theorem coeff_rename_inl_mul_rename_inr {σ : Type*} (p : MvPolynomial σ R)
    (q : MvPolynomial τ R) (a : σ →₀ ℕ) (b : τ →₀ ℕ) :
    (rename Sum.inl p * rename Sum.inr q).coeff (Finsupp.sumElim a b) =
      p.coeff a * q.coeff b := by
  classical
  have key : ∀ (u : σ →₀ ℕ) (v : τ →₀ ℕ),
      u.mapDomain Sum.inl + v.mapDomain Sum.inr = Finsupp.sumElim u v := by
    intro u v
    ext (x | x) <;> simp [Finsupp.mapDomain_apply_of_injective Sum.inl_injective,
      Finsupp.mapDomain_apply_of_injective Sum.inr_injective, Finsupp.mapDomain_of_notMem_range]
  rw [coeff_mul, Finset.sum_eq_single (a.mapDomain Sum.inl, b.mapDomain Sum.inr)]
  · rw [coeff_rename_mapDomain _ Sum.inl_injective, coeff_rename_mapDomain _ Sum.inr_injective]
  · rintro ⟨x, y⟩ hxy hne
    by_contra h0
    obtain ⟨u, rfl, -⟩ := coeff_rename_ne_zero _ _ _ (left_ne_zero_of_mul h0)
    obtain ⟨v, rfl, -⟩ := coeff_rename_ne_zero _ _ _ (right_ne_zero_of_mul h0)
    rw [Finset.mem_antidiagonal, key] at hxy
    have hu : u = a := by ext i; simpa using congrArg (· (Sum.inl i)) hxy
    have hv : v = b := by ext j; simpa using congrArg (· (Sum.inr j)) hxy
    exact hne (by rw [hu, hv])
  · intro h
    exact absurd (Finset.mem_antidiagonal.2 (key a b)) h
