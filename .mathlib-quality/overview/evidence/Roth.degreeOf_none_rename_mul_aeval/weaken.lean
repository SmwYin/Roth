import Roth.Separation

/-! Evidence for the overview assessment of `Roth.degreeOf_none_rename_mul_aeval`. -/

open MvPolynomial

#check @Roth.degreeOf_none_rename_mul_aeval

namespace Test

variable {R σ τ : Type*} [CommSemiring R]

/-- (1) API gap (same as the twin's evidence): a variable outside the range of a renaming
does not occur. -/
theorem degreeOf_rename_eq_zero_of_notMem_range {f : σ → τ} {i : τ} (hi : i ∉ Set.range f)
    (p : MvPolynomial σ R) : degreeOf i (rename f p) = 0 := by
  classical
  by_contra h
  have := vars_rename f p (mem_vars_iff_degreeOf_ne_zero.2 h)
  obtain ⟨j, -, rfl⟩ := Finset.mem_image.1 this
  exact hi ⟨j, rfl⟩

/-- (2) General product lemma, left-factor version, `NoZeroDivisors` only. -/
theorem degreeOf_mul_of_degreeOf_eq_zero_left [NoZeroDivisors R] {p q : MvPolynomial σ R}
    {i : σ} (hp : p ≠ 0) (hi : degreeOf i p = 0) : degreeOf i (p * q) = degreeOf i q := by
  by_cases hq : q = 0
  · simp [hq]
  rw [degreeOf_mul_eq hp hq, hi, zero_add]

/-- (3) API gap: the degree of `p(X_i)` in `X_i` is `natDegree p` (over any `CommSemiring`). -/
theorem degreeOf_toMvPolynomial_self (i : σ) (p : Polynomial R) :
    degreeOf i (p.toMvPolynomial i) = p.natDegree := by
  rw [Polynomial.toMvPolynomial_eq_rename_comp, AlgHom.comp_apply,
    degreeOf_rename_of_injective (f := fun _ : Unit ↦ i) (fun _ _ _ ↦ rfl) (),
    AlgEquiv.coe_toAlgHom, Roth.degreeOf_uniqueAlgEquiv_symm]

/-- (4) Literature-standard `Sum` form, second-block version. -/
theorem degreeOf_inr_rename_inl_mul_rename_inr [NoZeroDivisors R] {p : MvPolynomial σ R}
    (hp : p ≠ 0) (q : MvPolynomial τ R) (j : τ) :
    degreeOf (Sum.inr j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j q := by
  rw [degreeOf_mul_of_degreeOf_eq_zero_left
      ((rename_eq_zero_iff_of_injective p Sum.inl_injective).not.mpr hp)
      (degreeOf_rename_eq_zero_of_notMem_range (by simp) p),
    degreeOf_rename_of_injective Sum.inr_injective]

/-- (5) The project statement weakened from `CommRing + IsDomain` to
`CommSemiring + NoZeroDivisors`, proved from (1)-(3) by one `rw`. -/
theorem degreeOf_none_rename_mul_aeval' [NoZeroDivisors R] {U : MvPolynomial τ R} (hU : U ≠ 0)
    (V : Polynomial R) :
    degreeOf none (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      V.natDegree := by
  rw [degreeOf_mul_of_degreeOf_eq_zero_left
      ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      (degreeOf_rename_eq_zero_of_notMem_range (by simp) U)]
  exact degreeOf_toMvPolynomial_self none V

/-- (6) The original proof body, verbatim, under `CommSemiring + NoZeroDivisors`. -/
theorem degreeOf_none_rename_mul_aeval'' [NoZeroDivisors R] {U : MvPolynomial τ R} (hU : U ≠ 0)
    (V : Polynomial R) :
    degreeOf none (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      V.natDegree := by
  classical
  by_cases hV : V = 0
  · simp [hV]
  rw [degreeOf_mul_eq ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      ((map_ne_zero_iff (Polynomial.aeval (X none))
        (Polynomial.toMvPolynomial_injective none)).2 hV),
    (show degreeOf none (rename some U) = 0 by
      simp [degreeOf, degrees_rename_of_injective (Option.some_injective τ)]),
    zero_add, Roth.aeval_X_eq_rename]
  exact (degreeOf_rename_of_injective (f := fun _ : Unit ↦ (none : Option τ))
    (fun _ _ _ ↦ rfl) ()).trans (Roth.degreeOf_uniqueAlgEquiv_symm V)

/-- (7) `hU` cannot be dropped: `U = 0`, `V = X` gives `0 ≠ 1`. -/
example : degreeOf none (rename some (0 : MvPolynomial Unit ℤ) *
    Polynomial.aeval (X none : MvPolynomial (Option Unit) ℤ) (Polynomial.X : Polynomial ℤ)) = 0 ∧
    (Polynomial.X : Polynomial ℤ).natDegree = 1 := by simp

end Test
