private lemma mapped_det_ne_zero_aux {R : MvPolynomial (Option τ) ℤ} {l : ℕ} {D : Fin l → (τ →₀ ℕ)}
    {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0)
    (hF : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
        rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +
      Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det ≠ 0 := by
  have hmapdet : map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +
        Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det := by
    rw [RingHom.map_det]
    congr 1
    exact Matrix.ext fun μ ν ↦ by simp [hasseDeriv_map]
  rw [← hmapdet, ne_eq, map_eq_zero_iff _ (map_injective _ Int.cast_injective), hF,
    mul_eq_zero, not_or, map_eq_zero_iff _ (rename_injective _ (Option.some_injective _))]
  refine ⟨hU, ?_⟩
  rw [aeval_X_eq_rename, map_eq_zero_iff _ (rename_injective _ fun a b _ ↦ Subsingleton.elim a b)]
  rwa [map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective]
