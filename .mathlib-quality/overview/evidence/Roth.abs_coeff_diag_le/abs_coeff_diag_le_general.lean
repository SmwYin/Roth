import Mathlib.Analysis.Normed.Ring.Lemmas
import Mathlib.Analysis.Normed.Group.Int
import Roth.CoeffNorm

/-! Evidence for the `Roth.abs_coeff_diag_le` mathlibable assessment (re-aimed at
`MvPolynomial.aeval (fun _ ↦ Polynomial.X)`, per the `Roth.diag` / `Roth.diag_eq_sum` reports). -/

open MvPolynomial

namespace AbsCoeffDiagLeEvidence

variable {σ R : Type*}

/-- Weighted expansion (from the `Roth.diag_eq_sum` evidence), over any commutative semiring. -/
theorem aeval_X_pow_eq_sum [CommSemiring R] (w : σ → ℕ) (P : MvPolynomial σ R) :
    aeval (fun i ↦ (Polynomial.X : Polynomial R) ^ w i) P =
      ∑ k ∈ P.support, Polynomial.monomial (Finsupp.weight w k) (P.coeff k) := by
  rw [aeval_def, eval₂_eq]
  refine Finset.sum_congr rfl fun k _ ↦ ?_
  simp_rw [← pow_mul, Finset.prod_pow_eq_pow_sum, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial, Finsupp.weight_apply, Finsupp.sum, smul_eq_mul,
    mul_comm]

/-- (1) The project bound, re-aimed at `aeval (fun i ↦ X ^ w i)`, over any
`SeminormedCommRing` (weighted; the project's `diag` is `w = 1`). Proof is the project proof
with `abs_sum_le_sum_abs` replaced by `norm_sum_le`. -/
theorem norm_coeff_aeval_X_pow_le [SeminormedCommRing R] (w : σ → ℕ) (P : MvPolynomial σ R)
    {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun i ↦ (Polynomial.X : Polynomial R) ^ w i) P).coeff n‖ ≤ P.support.card * B := by
  rw [aeval_X_pow_eq_sum, Polynomial.finsetSum_coeff, ← nsmul_eq_mul]
  refine (norm_sum_le _ _).trans (Finset.sum_le_card_nsmul _ _ B fun k _ ↦ ?_)
  rw [Polynomial.coeff_monomial]
  split_ifs
  · exact hB k
  · simpa using (norm_nonneg _).trans (hB k)

/-- (2) Sharper form: only the monomials of total degree `n` contribute. -/
theorem norm_coeff_aeval_X_le [SeminormedCommRing R] (P : MvPolynomial σ R) {B : ℝ}
    (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n‖ ≤
      (P.support.filter fun k ↦ k.degree = n).card * B := by
  have h : (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n =
      ∑ k ∈ P.support with k.degree = n, P.coeff k := by
    rw [aeval_def, eval₂_eq]
    simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq,
      Polynomial.C_mul_X_pow_eq_monomial, Polynomial.finsetSum_coeff, Polynomial.coeff_monomial,
      Finset.sum_ite, Finset.sum_const_zero, add_zero]
  rw [h, ← nsmul_eq_mul]
  exact (norm_sum_le _ _).trans (Finset.sum_le_card_nsmul _ _ B fun k _ ↦ hB k)

/-- (2) implies (1) in the unweighted case. -/
example [SeminormedCommRing R] (P : MvPolynomial σ R) {B : ℝ}
    (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n‖ ≤ P.support.card * B := by
  have hB0 : 0 ≤ B := (norm_nonneg _).trans (hB 0)
  refine (norm_coeff_aeval_X_le P hB n).trans (mul_le_mul_of_nonneg_right ?_ hB0)
  exact_mod_cast Finset.card_filter_le _ _

/-- `Roth.abs_coeff_diag_le` is the `R = ℤ`, `w = 1` case of (1). -/
example (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (n : ℕ) :
    |(((Roth.diag P).coeff n : ℤ) : ℝ)| ≤ P.support.card * B := by
  have hB' : ∀ d, ‖P.coeff d‖ ≤ B := fun d ↦ by rw [Int.norm_eq_abs]; exact hB d
  have h := norm_coeff_aeval_X_pow_le (R := ℤ) (fun _ ↦ 1) P hB' n
  simpa [Roth.diag, Int.norm_eq_abs] using h

end AbsCoeffDiagLeEvidence
