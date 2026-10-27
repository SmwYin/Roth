import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

namespace Evidence88
open MvPolynomial
variable {σ R : Type*}

/-- Multi-index `binom(k,d) ≤ 2^|k|` (from the hasseCoeff_le_two_pow evidence). -/
theorem hasseCoeff_le_two_pow_degree (d k : σ →₀ ℕ) : hasseCoeff d k ≤ 2 ^ k.degree := by
  classical
  calc hasseCoeff d k = ∏ j ∈ d.support, (k j).choose (d j) := rfl
    _ ≤ ∏ j ∈ d.support, 2 ^ k j := Finset.prod_le_prod fun j _ ↦ Nat.choose_le_two_pow _ _
    _ = 2 ^ ∑ j ∈ d.support, k j := Finset.prod_pow_eq_pow_sum _ _ _
    _ ≤ 2 ^ k.degree := Nat.pow_le_pow_right two_pos <|
        Finset.sum_le_sum_of_ne_zero fun j _ hj ↦ Finsupp.mem_support_iff.2 hj

/-- (1) Pointwise form: no `Fintype`, no box `r`, no uniform bound `B`; any seminormed
commutative ring (`norm_nsmul_le`, no `NormOneClass` needed). -/
theorem norm_coeff_hasseDeriv_le [SeminormedCommRing R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    ‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (e + d).degree * ‖P.coeff (e + d)‖ := by
  rw [coeff_hasseDeriv, ← nsmul_eq_mul]
  exact norm_nsmul_le.trans <| mul_le_mul_of_nonneg_right
    (by exact_mod_cast hasseCoeff_le_two_pow_degree d (e + d)) (norm_nonneg _)

/-- (2) The project shape over any seminormed commutative ring. -/
theorem norm_coeff_hasseDeriv_le_of_degreeOf_le [SeminormedCommRing R] [Fintype σ]
    (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ}
    (hB : ∀ e, ‖P.coeff e‖ ≤ B) (e : σ →₀ ℕ) :
    ‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (∑ j, r j) * B := by
  rw [coeff_hasseDeriv, ← nsmul_eq_mul]
  refine norm_nsmul_le.trans ?_
  by_cases he : e + d ∈ P.support
  · exact mul_le_mul (by exact_mod_cast hasseCoeff_le_two_pow fun j ↦
      (monomial_le_degreeOf j he).trans (hP j)) (hB _) (norm_nonneg _) (by positivity)
  · rw [notMem_support_iff.1 he, norm_zero, mul_zero]
    exact mul_nonneg (by positivity) ((norm_nonneg _).trans (hB e))

/-- Recovery of the exact project statement from (2) via `Int.norm_eq_abs`. -/
example [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B)
    (e : σ →₀ ℕ) : |(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B := by
  simpa [Int.norm_eq_abs] using
    norm_coeff_hasseDeriv_le_of_degreeOf_le d P hP (B := B) (by simpa [Int.norm_eq_abs] using hB) e

/-- The project statement is still literally available as `Roth.abs_coeff_hasseDeriv_le`. -/
example [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B)
    (e : σ →₀ ℕ) : |(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B :=
  Roth.abs_coeff_hasseDeriv_le d P hP hB e

end Evidence88
