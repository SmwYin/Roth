import Roth.Theta

/-! Evidence for `Roth.index_det_le`: superfluous `R ≠ 0` part of `hR`. -/

open MvPolynomial

namespace Roth

variable {τ : Type*} [Fintype τ]

/-- (1) `R ≠ 0` in `hR : R ∈ RSet B r` is superfluous: it follows from `hF`, `hU`, `hV`, `1 ≤ l`.
Only the degree and coefficient bounds on `R` are needed. -/
example {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁)
    {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ}
    (hRd : ∀ j, degreeOf j R ≤ r j) (hRc : ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B)
    {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ} (hl : 1 ≤ l)
    {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0)
    (hUd : ∀ j, degreeOf j U ≤ l * r (some j)) (hVd : V.natDegree ≤ l * r none)
    (hF : (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) :
    index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)
      (fun j ↦ (h j : ℝ) / q j) r ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l := by
  classical
  have hR0 : R ≠ 0 := by
    rintro rfl
    have hne : rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V ≠ 0 := by
      refine mul_ne_zero ((map_ne_zero_iff _ (rename_injective _ (Option.some_injective _))).2 hU) ?_
      rw [aeval_X_eq_rename]
      exact (map_ne_zero_iff _ (rename_injective _ fun _ _ _ ↦ Subsingleton.elim _ _)).2
        (by rwa [ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective])
    apply hne
    rw [← hF]
    simp only [map_zero]
    exact Matrix.det_eq_zero_of_column_eq_zero (⟨0, hl⟩ : Fin l) fun _ ↦ rfl
  exact index_det_le hr0 hr₁ ⟨hR0, hRd, hRc⟩ hh hl hU hV hUd hVd hF

end Roth
