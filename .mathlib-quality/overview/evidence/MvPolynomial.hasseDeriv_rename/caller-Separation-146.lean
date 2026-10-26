  rw [← coeff_coeffNone, coeffNone, map_mul,
    (show optionEquivLeft R τ (rename some U) = Polynomial.C U from AlgHom.congr_fun h U),
    ← Polynomial.aeval_algHom_apply, optionEquivLeft_X_none, Polynomial.aeval_X_left_eq_map,
    Polynomial.coeff_C_mul, Polynomial.coeff_map, algebraMap_eq, mul_comm U, coeff_C_mul, mul_comm]

/-- A univariate polynomial in the variable `X i`, as the renaming of a one-variable
`MvPolynomial`. Source: §4, Lemma 4-2 ("the index of the embedded `Q` is its one-variable
index"). -/
theorem aeval_X_eq_rename {σ : Type*} (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f) :=
  AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f

omit [Fintype τ] [DecidableEq τ] in
/-- A Hasse derivative `Δ_{d + ν e_none}` of a separated product `U(x_τ) V(x_none)` acts
factorwise. Source: §2, proof of Lemma 2 ("`Δ_μ (1/ν!) ∂^ν_{x_p} (φ_ρ(x_p) ψ_ρ(x_1, …, x_{p-1}))
= (Δ_μ ψ_ρ) ((1/ν!) ∂^ν φ_ρ)`", the entries of `A Bᵀ`). -/
theorem hasseDeriv_rename_mul_aeval (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R) (V : Polynomial R) :
    hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval
      (X none : MvPolynomial (Option τ) R) V) = rename some (hasseDeriv d U) * Polynomial.aeval
      (X none : MvPolynomial (Option τ) R) (Polynomial.hasseDeriv ν V) := by
  classical
  have hnone : ∀ {o : Option τ}, o ∈ (d.mapDomain some).support → o ≠ none := by
    simp
  have hdisj : Disjoint (d.mapDomain some).support (Finsupp.single none ν).support :=
    Finset.disjoint_left.2 fun _ ho ho' ↦
      hnone ho (Finset.mem_singleton.1 (Finsupp.support_single_subset ho'))
  rw [← hasseDeriv_hasseDeriv_of_disjoint hdisj,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      rw [Finset.mem_singleton.1 (Finsupp.support_single_subset hj)]
      simp [degreeOf, degrees_rename_of_injective (Option.some_injective τ)],
    hasseDeriv_single_aeval_X, mul_comm,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      simp [aeval_X_eq_rename, degreeOf,
        degrees_rename_of_injective (Function.injective_of_subsingleton _), Multiset.mem_replicate,
        hnone hj],
    hasseDeriv_rename (Option.some_injective τ), mul_comm]

/-- Source: §5, proof of Lemma 6 ("`V(x_p) ∈ ℛ_1(M; l r_p)`"): the coefficients of a univariate
