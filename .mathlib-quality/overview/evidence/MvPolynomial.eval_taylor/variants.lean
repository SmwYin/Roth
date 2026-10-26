import Roth.Taylor

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

-- (1) the statement as in the project, re-proved
example (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  simp [taylor, aeval_def, ← eval_assoc, Function.comp_def]

-- (2a) plain simp (taylor sealed) cannot prove it
example (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  fail_if_success simp
  exact eval_taylor α x P

-- (2b) unfolding `taylor` alone does not close it either: simp stalls at
-- `eval₂ ((eval x).comp C) (fun i ↦ x i + α i) P = eval (fun i ↦ x i + α i) P`,
-- which needs `(eval x).comp C = RingHom.id R` (mathlib: `eval_assoc` / `eval₂_comp_left`)
example (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  simp [taylor]
  fail_if_success done
  rw [show (eval x).comp C = RingHom.id R from RingHom.ext fun a ↦ by simp]
  rfl

-- (3) composition from mathlib: one rewrite chain + simp (eval_assoc is the only real step)
example (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  rw [taylor_apply, aeval_def, algebraMap_eq, ← eval_assoc]
  simp [Function.comp_def]

-- (4) generalisation: evaluation in any commutative R-algebra S (aeval form)
theorem aeval_taylor' {S : Type*} [CommSemiring S] [Algebra R S] (α : σ → R) (x : σ → S)
    (P : MvPolynomial σ R) :
    aeval x (taylor α P) = aeval (fun j ↦ x j + algebraMap R S (α j)) P := by
  rw [taylor_apply, comp_aeval_apply]
  simp

-- (5) the project form is a one-line specialisation of (4) at S = R
example (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  simpa [coe_aeval_eq_eval] using aeval_taylor' α x P

-- (6) simp-attribute probe: as a simp lemma it closes a composite goal without looping
attribute [local simp] eval_taylor in
example (α β x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α (taylor β P)) = eval (fun j ↦ x j + α j + β j) P := by
  simp

end MvPolynomial
