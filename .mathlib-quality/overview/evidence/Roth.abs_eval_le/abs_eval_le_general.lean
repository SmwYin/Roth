import Mathlib.Analysis.Normed.Ring.Lemmas
import Mathlib.Analysis.Normed.Group.Int
import Mathlib.Analysis.Normed.Field.Basic
import Roth.CoeffNorm

/-! Evidence for the `Roth.abs_eval_le` mathlibable assessment. -/

open MvPolynomial

namespace AbsEvalLeEvidence

variable {σ R : Type*}

/-- (1) The project bound over any `NormedCommRing` with `‖1‖ = 1`, coefficients and point
in the same ring.  Same proof as the project (triangle inequality, support ⊆ box, box sum
factorises into truncated geometric sums, each `≤ (1 + t)^r`). -/
theorem norm_eval_le [Fintype σ] [NormedCommRing R] [NormOneClass R]
    (P : MvPolynomial σ R) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j)
    {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (x : σ → R) :
    ‖eval x P‖ ≤ B * ∏ j, (1 + ‖x j‖) ^ r j := by
  classical
  have hB0 : 0 ≤ B := (norm_nonneg _).trans (hB 0)
  rw [eval_eq']
  calc ‖∑ k ∈ P.support, P.coeff k * ∏ j, x j ^ k j‖
      ≤ ∑ k ∈ P.support, B * ∏ j, ‖x j‖ ^ k j := by
        refine (norm_sum_le _ _).trans (Finset.sum_le_sum fun k _ ↦ ?_)
        refine (norm_mul_le _ _).trans (mul_le_mul (hB k) ?_ (norm_nonneg _) hB0)
        exact (Finset.norm_prod_le _ _).trans
          (Finset.prod_le_prod₀ (fun _ _ ↦ norm_nonneg _) (fun j _ ↦ norm_pow_le (x j) (k j)))
    _ ≤ ∑ k ∈ Roth.box r, B * ∏ j, ‖x j‖ ^ k j :=
        Finset.sum_le_sum_of_subset_of_nonneg
          (fun k hk ↦ Roth.mem_box.2 fun j ↦ (monomial_le_degreeOf j hk).trans (hP j))
          fun _ _ _ ↦ by positivity
    _ ≤ B * ∏ j, (1 + ‖x j‖) ^ r j := by
        simpa [← Finset.mul_sum, Roth.box, Finset.prod_univ_sum] using
          mul_le_mul_of_nonneg_left (Finset.prod_le_prod₀ (s := Finset.univ)
            (fun _ _ ↦ by positivity)
            fun j _ ↦ Roth.geom_sum_le_one_add_pow (norm_nonneg (x j)) (r j)) hB0

/-- (2) The project statement is recovered from (1) with `R = ℝ` after `eval_map`. -/
example [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j)
    {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (x : σ → ℝ) :
    |eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j := by
  have := norm_eval_le (map (Int.castRingHom ℝ) P) (r := r)
    (fun j ↦ by
      classical rw [degreeOf_def, degrees_map_of_injective _ Int.cast_injective]; exact hP j) (B := B)
    (fun d ↦ by simpa [coeff_map, Real.norm_eq_abs] using hB d) x
  simpa [Real.norm_eq_abs] using this

/-- (3) `Roth.abs_eval_le` itself specialises cleanly; sanity check it still elaborates. -/
example [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j)
    {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (x : σ → ℝ) :
    |eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j :=
  Roth.abs_eval_le P hP hB x

end AbsEvalLeEvidence
