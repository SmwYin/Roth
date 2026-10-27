import Roth.Separation

/-! Evidence for the /overview assessment of `Roth.hasseDeriv_rename_mul_aeval`. -/

open MvPolynomial

variable {R τ : Type*} [CommSemiring R]

-- (0) signature: only `[CommSemiring R]`
#check @Roth.hasseDeriv_rename_mul_aeval

-- (1) restatement at mathlib's canonical `optionElim` index (cf. `optionEquivLeft_coeff_coeff`)
theorem hasseDeriv_rename_some_mul_aeval_X_none (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R)
    (V : Polynomial R) :
    hasseDeriv (d.optionElim ν) (rename some U * Polynomial.aeval
      (X none : MvPolynomial (Option τ) R) V) = rename some (hasseDeriv d U) * Polynomial.aeval
      (X none : MvPolynomial (Option τ) R) (Polynomial.hasseDeriv ν V) := by
  classical
  have : d.optionElim ν = d.mapDomain some + Finsupp.single none ν := by
    ext (_ | x) <;> simp [Finsupp.mapDomain_of_notMem_range,
      Finsupp.mapDomain_apply_of_injective (Option.some_injective τ)]
  rw [this, Roth.hasseDeriv_rename_mul_aeval]

-- (2) literature-standard disjoint-variables form over `σ ⊕ τ`
theorem hasseDeriv_rename_inl_mul_rename_inr {σ : Type*} (d : σ →₀ ℕ) (e : τ →₀ ℕ)
    (p : MvPolynomial σ R) (q : MvPolynomial τ R) :
    hasseDeriv (Finsupp.sumElim d e) (rename Sum.inl p * rename Sum.inr q) =
      rename Sum.inl (hasseDeriv d p) * rename Sum.inr (hasseDeriv e q) := by
  classical
  have key : d.mapDomain Sum.inl + e.mapDomain Sum.inr = Finsupp.sumElim d e := by
    ext (x | x) <;> simp [Finsupp.mapDomain_apply_of_injective Sum.inl_injective,
      Finsupp.mapDomain_apply_of_injective Sum.inr_injective, Finsupp.mapDomain_of_notMem_range]
  have hdisj : Disjoint (d.mapDomain Sum.inl).support (e.mapDomain Sum.inr).support := by
    refine Finset.disjoint_left.2 fun o ho ho' ↦ ?_
    obtain ⟨a, -, rfl⟩ := Finset.mem_image.1 (Finsupp.mapDomain_support ho)
    obtain ⟨b, -, hb⟩ := Finset.mem_image.1 (Finsupp.mapDomain_support ho')
    exact Sum.inr_ne_inl hb
  rw [← key, ← hasseDeriv_hasseDeriv_of_disjoint hdisj,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      obtain ⟨b, -, rfl⟩ := Finset.mem_image.1 (Finsupp.mapDomain_support hj)
      simp [degreeOf, degrees_rename_of_injective Sum.inl_injective],
    hasseDeriv_rename Sum.inr_injective, mul_comm,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      obtain ⟨a, -, rfl⟩ := Finset.mem_image.1 (Finsupp.mapDomain_support hj)
      simp [degreeOf, degrees_rename_of_injective Sum.inr_injective],
    hasseDeriv_rename Sum.inl_injective, mul_comm]
