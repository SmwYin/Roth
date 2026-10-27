import Roth.Separation

/-! Evidence for the overview assessment of `Roth.degreeOf_rename_mul_aeval`. -/

open MvPolynomial

#check @Roth.degreeOf_rename_mul_aeval

namespace Test

variable {R σ τ : Type*} [CommSemiring R]

/-- (1) API gap: a variable outside the range of the renaming does not occur. -/
theorem degreeOf_rename_eq_zero_of_notMem_range {f : σ → τ} {i : τ} (hi : i ∉ Set.range f)
    (p : MvPolynomial σ R) : degreeOf i (rename f p) = 0 := by
  classical
  by_contra h
  have := vars_rename f p (mem_vars_iff_degreeOf_ne_zero.2 h)
  obtain ⟨j, -, rfl⟩ := Finset.mem_image.1 this
  exact hi ⟨j, rfl⟩

/-- (2) General product lemma, `NoZeroDivisors` only. -/
theorem degreeOf_mul_of_degreeOf_eq_zero_right [NoZeroDivisors R] {p q : MvPolynomial σ R}
    {i : σ} (hq : q ≠ 0) (hi : degreeOf i q = 0) : degreeOf i (p * q) = degreeOf i p := by
  by_cases hp : p = 0
  · simp [hp]
  rw [degreeOf_mul_eq hp hq, hi, add_zero]

/-- (3) Literature-standard `Sum` form: `deg_{x_j}(p(x) q(y)) = deg_{x_j} p` for `q ≠ 0`. -/
theorem degreeOf_inl_rename_inl_mul_rename_inr [NoZeroDivisors R] (p : MvPolynomial σ R)
    {q : MvPolynomial τ R} (hq : q ≠ 0) (j : σ) :
    degreeOf (Sum.inl j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j p := by
  rw [degreeOf_mul_of_degreeOf_eq_zero_right
      ((rename_eq_zero_iff_of_injective q Sum.inr_injective).not.mpr hq)
      (degreeOf_rename_eq_zero_of_notMem_range (by simp) q),
    degreeOf_rename_of_injective Sum.inl_injective]

/-- (4) The project statement weakened from `CommRing + IsDomain` to
`CommSemiring + NoZeroDivisors`, proved from (1) and (2). -/
theorem degreeOf_rename_mul_aeval' [NoZeroDivisors R] (U : MvPolynomial τ R) {V : Polynomial R}
    (hV : V ≠ 0) (j : τ) :
    degreeOf (some j) (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      degreeOf j U := by
  rw [degreeOf_mul_of_degreeOf_eq_zero_right
      ((map_ne_zero_iff (Polynomial.aeval (X none : MvPolynomial (Option τ) R))
        (Polynomial.toMvPolynomial_injective none)).2 hV)
      (by rw [Roth.aeval_X_eq_rename]; exact degreeOf_rename_eq_zero_of_notMem_range (by simp) _),
    degreeOf_rename_of_injective (Option.some_injective τ)]

/-- (5) The original proof body, verbatim, under `CommSemiring + NoZeroDivisors`. -/
theorem degreeOf_rename_mul_aeval'' [NoZeroDivisors R] (U : MvPolynomial τ R) {V : Polynomial R}
    (hV : V ≠ 0) (j : τ) :
    degreeOf (some j) (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      degreeOf j U := by
  classical
  by_cases hU : U = 0
  · simp [hU]
  rw [degreeOf_mul_eq ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      ((map_ne_zero_iff (Polynomial.aeval (X none))
        (Polynomial.toMvPolynomial_injective none)).2 hV),
    degreeOf_rename_of_injective (Option.some_injective τ)]
  simp [Roth.aeval_X_eq_rename, degreeOf,
    degrees_rename_of_injective (Function.injective_of_subsingleton _), Multiset.mem_replicate]

/-- (6) `hV` cannot be dropped: `V = 0` makes the left side `0`. Over `ZMod 4` with
`U = 2 X`, `V = 2`, `NoZeroDivisors` cannot be dropped either (product is `0`). -/
example : degreeOf (some ()) (rename some (X () : MvPolynomial Unit ℤ) *
    Polynomial.aeval (X none : MvPolynomial (Option Unit) ℤ) (0 : Polynomial ℤ)) = 0 := by simp

end Test
