import Roth.CoeffNorm

/-! Evidence for the `Roth.diag` mathlibable assessment. -/

open MvPolynomial

namespace DiagEvidence

variable {σ R : Type*} [CommSemiring R]

/-- (1) The general-coefficient, bundled form: an `R`-algebra hom. -/
noncomputable abbrev diagHom : MvPolynomial σ R →ₐ[R] Polynomial R := aeval fun _ ↦ Polynomial.X

/-- `Roth.diag` is literally the ℤ-specialisation of `diagHom`. -/
example (P : MvPolynomial σ ℤ) : Roth.diag P = diagHom P := rfl

/-- (2) Equivalent mathlib formulation: rename all variables to one, then `uniqueAlgEquiv`. -/
example (P : MvPolynomial σ R) :
    diagHom P = uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P) := by
  simp [uniqueAlgEquiv_apply, eval₂_rename, aeval_def, Function.comp_def,
    Polynomial.algebraMap_eq]

/-- (3) `diag_eq_sum` holds over any commutative semiring (same proof). -/
example (P : MvPolynomial σ R) :
    diagHom P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) := by
  rw [aeval_def, eval₂_eq]
  simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial]

/-- (4) Degree bound in terms of mathlib's `totalDegree` (general `R`). -/
example (P : MvPolynomial σ R) : (diagHom P).natDegree ≤ P.totalDegree := by
  rw [aeval_def, eval₂_eq]
  refine Polynomial.natDegree_sum_le_of_forall_le _ _ fun k hk ↦ ?_
  simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial]
  exact (Polynomial.natDegree_monomial_le _).trans (le_totalDegree hk)

/-- (5) `eval_diag` in the general algebra form, one mathlib lemma (`comp_aeval`). -/
example {S : Type*} [CommSemiring S] [Algebra R S] (P : MvPolynomial σ R) (x : S) :
    Polynomial.aeval x (diagHom P) = aeval (fun _ ↦ x) P := by
  rw [← AlgHom.comp_apply, comp_aeval]
  simp

/-- (6) `diag_sub` is `map_sub` (already the project proof). -/
example (P Q : MvPolynomial σ ℤ) : Roth.diag (P - Q) = Roth.diag P - Roth.diag Q := map_sub _ _ _

end DiagEvidence
