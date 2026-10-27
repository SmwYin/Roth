import Roth.MainLemma
import Mathlib.Analysis.Polynomial.Norm
import Mathlib.Algebra.Polynomial.CoeffMem

/-! Evidence for the /overview mathlibable assessment of `Roth.norm_coeff_modByMonic_le`. -/

open Polynomial

-- (1) The mathlib-idiomatic `supNorm` restatement follows from the project lemma
-- (A := f.supNorm, C := P.supNorm, s := P.natDegree) plus mathlib's `le_supNorm`
-- and `exists_eq_supNorm`.
theorem supNorm_modByMonic_le {R : Type*} [SeminormedRing R] (P f : R[X]) :
    (P %ₘ f).supNorm ≤ (1 + f.supNorm) ^ (P.natDegree + 1 - f.natDegree) * P.supNorm := by
  obtain ⟨i, hi⟩ := (P %ₘ f).exists_eq_supNorm
  rw [hi]
  exact Roth.norm_coeff_modByMonic_le (fun j ↦ f.le_supNorm j) P (fun j ↦ P.le_supNorm j)
    le_rfl i

-- (2) The nearest mathlib result is algebraic (submodule membership), not a norm bound.
#check @Polynomial.coeff_modByMonic_mem_pow_natDegree_mul

-- (3) The declaration as stated.
#check @Roth.norm_coeff_modByMonic_le
