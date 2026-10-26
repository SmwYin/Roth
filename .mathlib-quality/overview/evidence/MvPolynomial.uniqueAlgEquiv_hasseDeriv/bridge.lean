import Roth.HasseDeriv

/-! Evidence for the /overview assessment of `MvPolynomial.uniqueAlgEquiv_hasseDeriv`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Syntactic generalisation: arbitrary multi-index `d` (for `Unique σ` every `d` is
`single default (d default)`), so callers need no `Finsupp.unique_single` rewrite. -/
theorem uniqueAlgEquiv_hasseDeriv' [Unique σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv d P) =
      Polynomial.hasseDeriv (d default) (uniqueAlgEquiv R σ P) := by
  rw [Finsupp.unique_single d, Finsupp.single_eq_same]
  exact uniqueAlgEquiv_hasseDeriv _ P

/-- (1b) Same general form, proved directly by the original coefficient computation. -/
example [Unique σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv d P) =
      Polynomial.hasseDeriv (d default) (uniqueAlgEquiv R σ P) := by
  ext m
  rw [coeff_uniqueAlgEquiv, coeff_hasseDeriv, Polynomial.hasseDeriv_coeff, coeff_uniqueAlgEquiv]
  conv_lhs => rw [Finsupp.unique_single d]
  simp [hasseCoeff, Finsupp.single_add]

/-- (2) Operator (linear-map) form. -/
example [Unique σ] (d : σ →₀ ℕ) :
    (uniqueAlgEquiv R σ).toLinearMap ∘ₗ hasseDeriv d =
      Polynomial.hasseDeriv (d default) ∘ₗ (uniqueAlgEquiv R σ).toLinearMap :=
  LinearMap.ext fun P ↦ uniqueAlgEquiv_hasseDeriv' d P

/-- (3) Composition check: derive from the sibling `hasseDeriv_single_aeval_X`
(`uniqueAlgEquiv.symm = Polynomial.aeval (X default)`). -/
example [Unique σ] (n : ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv (R := R) (Finsupp.single (default : σ) n) P) =
      Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P) := by
  obtain ⟨f, rfl⟩ := (uniqueAlgEquiv R σ).symm.surjective P
  have h : ∀ g : Polynomial R, (uniqueAlgEquiv R σ).symm g =
      Polynomial.aeval (X default : MvPolynomial σ R) g := fun g ↦ by
    rw [Polynomial.aeval_def, algebraMap_eq]; rfl
  rw [AlgEquiv.apply_symm_apply, h, hasseDeriv_single_aeval_X, ← h, AlgEquiv.apply_symm_apply]

end MvPolynomial
