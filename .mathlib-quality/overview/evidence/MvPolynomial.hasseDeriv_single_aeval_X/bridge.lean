import Roth.HasseDeriv

/-! Evidence for the /overview assessment of `MvPolynomial.hasseDeriv_single_aeval_X`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Same statement phrased with mathlib's named embedding `Polynomial.toMvPolynomial`. -/
example (j : σ) (n : ℕ) (f : Polynomial R) :
    hasseDeriv (Finsupp.single j n) (f.toMvPolynomial j) =
      (Polynomial.hasseDeriv n f).toMvPolynomial j :=
  hasseDeriv_single_aeval_X j n f

/-- (1') Operator form: `Δ_{n e_j} ∘ toMvPolynomial j = toMvPolynomial j ∘ D^(n)`. -/
example (j : σ) (n : ℕ) :
    (hasseDeriv (R := R) (Finsupp.single j n)).comp (Polynomial.toMvPolynomial j).toLinearMap =
      (Polynomial.toMvPolynomial j).toLinearMap.comp (Polynomial.hasseDeriv n) :=
  LinearMap.ext fun f ↦ hasseDeriv_single_aeval_X j n f

/-- (2) Composition check: the statement follows from the project's `hasseDeriv_rename` and
`uniqueAlgEquiv_hasseDeriv` plus mathlib's `Polynomial.toMvPolynomial_eq_rename_comp`. -/
example (j : σ) (n : ℕ) (f : Polynomial R) :
    hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) =
      Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv n f) := by
  have h := AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp (R := R) j)
  simp only [Polynomial.toMvPolynomial, AlgHom.comp_apply, AlgEquiv.coe_toAlgHom] at h
  rw [h, h, ← Finsupp.mapDomain_single (f := fun _ : Unit ↦ j) (a := ()),
    hasseDeriv_rename (Function.injective_of_subsingleton _)]
  congr 1
  apply (uniqueAlgEquiv R Unit).injective
  exact (uniqueAlgEquiv_hasseDeriv n _).trans (by rw [AlgEquiv.apply_symm_apply, AlgEquiv.apply_symm_apply])

private lemma eq_single_of_le_single {j : σ} {d : σ →₀ ℕ} {m : ℕ}
    (h : d ≤ Finsupp.single j m) : d = Finsupp.single j (d j) := by
  classical
  ext k
  by_cases hk : k = j
  · subst hk; simp
  · have := h k
    simp [Ne.symm hk] at this ⊢
    omega

/-- (3) Strict generalisation to an arbitrary multi-index `d`: `Δ_d` kills every polynomial
in `X j` unless `d` is supported on `{j}`. -/
theorem hasseDeriv_aeval_X [DecidableEq σ] (j : σ) (d : σ →₀ ℕ) (f : Polynomial R) :
    hasseDeriv d (Polynomial.aeval (X j : MvPolynomial σ R) f) =
      if d = Finsupp.single j (d j) then
        Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv (d j) f) else 0 := by
  split_ifs with hd
  · rw [hd, Finsupp.single_eq_same, ← hd]
    conv_lhs => rw [hd]
    exact hasseDeriv_single_aeval_X j (d j) f
  · induction f using Polynomial.induction_on' with
    | add p q hp hq => simp [hp, hq]
    | monomial m a =>
      have hz : hasseCoeff d (Finsupp.single j m) = 0 :=
        (hasseCoeff_eq_zero_iff _ _).2 fun hle ↦ hd (eq_single_of_le_single hle)
      simp [X_pow_eq_monomial, C_mul_monomial, hasseDeriv_monomial, hz]

end MvPolynomial
