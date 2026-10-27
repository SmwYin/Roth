import Roth.CoeffNorm

/-! Evidence for the `Roth.eval_diag` mathlibable assessment. -/

open MvPolynomial

namespace EvalDiagEvidence

variable {σ R S : Type*} [CommSemiring R] [CommSemiring S] [Algebra R S]

/-- (1) Re-aimed general form (any `CommSemiring R`, any `R`-algebra `S`): one mathlib lemma
`MvPolynomial.comp_aeval` after folding the composite. -/
theorem aeval_aeval_X (P : MvPolynomial σ R) (x : S) :
    Polynomial.aeval x (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P) = aeval (fun _ ↦ x) P := by
  rw [← AlgHom.comp_apply, comp_aeval]
  simp

/-- (1b) Same, as mathlib's `MvPolynomial.comp_aeval_apply` plus `Polynomial.aeval_X` (the
spelling already used inline at Roth/MainLemma.lean:409-410). -/
example (P : MvPolynomial σ R) (x : S) :
    Polynomial.aeval x (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P) = aeval (fun _ ↦ x) P := by
  simp [comp_aeval_apply, Polynomial.aeval_X]

/-- (2) Same, by `MvPolynomial.induction_on` + `simp_all` (the project's proof shape), general
`R`, `S`. -/
example (P : MvPolynomial σ R) (x : S) :
    Polynomial.aeval x (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P) = aeval (fun _ ↦ x) P := by
  induction P using MvPolynomial.induction_on <;> simp_all

/-- (3) The exact project statement recovered from (1): two `eval_map` rewrites, then (1)
closes the goal up to defeq (`algebraMap ℤ ℝ` is `Int.castRingHom ℝ`, `Roth.diag` unfolds). -/
example (P : MvPolynomial σ ℤ) (x : ℝ) :
    Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (Roth.diag P)) =
      eval (fun _ ↦ x) (map (Int.castRingHom ℝ) P) := by
  rw [Polynomial.eval_map, MvPolynomial.eval_map]
  exact aeval_aeval_X (S := ℝ) P x

end EvalDiagEvidence
