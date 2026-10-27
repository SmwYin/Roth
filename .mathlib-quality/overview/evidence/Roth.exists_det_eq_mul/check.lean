import Roth.Separation

open MvPolynomial

-- (0) elaborated type
#check @Roth.exists_det_eq_mul

-- (1) weakening probe: drop `[Finite τ]` (expected to FAIL: the private helper
-- `exists_rat_factors_det_hasseDeriv_aux` needs it, via `exists_separated_representation`
-- and `exists_genWronskian_ne_zero`). The failure is the evidence.
example {τ : Type*} {P : MvPolynomial (Option τ) ℤ} (hP : P ≠ 0) {r : Option τ → ℕ}
    (hr : ∀ j, degreeOf j P ≤ r j) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ),
      (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
        (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧
        (Matrix.of fun μ ν : Fin l ↦
            hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =
          rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V :=
  Roth.exists_det_eq_mul hP hr
