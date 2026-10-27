import Roth.CoeffNorm

/-! Evidence for `Roth.abs_coeff_det_hasseDeriv_le`. -/

open MvPolynomial

namespace Test

variable {σ : Type*}

/-- (1) The stronger ℓ¹ form (the paper's proof bounds `‖F‖₁`), with `hB0` dropped:
`0 ≤ B` follows from `hB 0`. -/
theorem normOne_det_hasseDeriv_le [Fintype σ] {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ))
    (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ}
    (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) :
    Roth.normOne (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤
      (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l) := by
  have hB0 : 0 ≤ B := (abs_nonneg _).trans (hB 0)
  have hsupp : (P.support.card : ℝ) ≤ ∏ j, ((r j : ℝ) + 1) := by
    exact_mod_cast Roth.card_le_card_box fun d hd j ↦ (monomial_le_degreeOf j hd).trans (hP j)
  calc _ ≤ l.factorial * (2 ^ (∑ j, r j) * ((∏ j, ((r j : ℝ) + 1)) * B)) ^ l :=
        Roth.normOne_det_le _ fun μ ν ↦
          (Roth.normOne_hasseDeriv_le _ P hP).trans (mul_le_mul_of_nonneg_left
            ((Roth.normOne_le_card_mul P hB).trans (mul_le_mul_of_nonneg_right hsupp hB0))
            (by positivity))
    _ = _ := by ring

/-- (2) The project statement without `hB0`, as a one-line corollary of (1). -/
theorem abs_coeff_det_hasseDeriv_le' [Fintype σ] {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ))
    (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ}
    (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (d : σ →₀ ℕ) :
    |(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤
      (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l) :=
  (Roth.abs_coeff_le_normOne _ _).trans (normOne_det_hasseDeriv_le E P hP hB)

/-- (3) The original statement (with `hB0`) is recovered. -/
example [Fintype σ] {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ))
    (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (_hB0 : 0 ≤ B)
    (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (d : σ →₀ ℕ) :
    |(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤
      (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l) :=
  abs_coeff_det_hasseDeriv_le' E P hP hB d

end Test
