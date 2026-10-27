import Mathlib

open MvPolynomial

/-- (1) Generalisation: arbitrary finite variable type `σ`, any linearly ordered field `K`,
integer denominators `q j > 0`. -/
theorem MvPolynomial.one_le_prod_pow_mul_abs_eval_div {σ K : Type*} [Fintype σ] [Field K]
    [LinearOrder K] [IsStrictOrderedRing K] (Q : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h q : σ → ℤ) (hq : ∀ j, 0 < q j)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : K) ^ r j) * |eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)| := by
  have hqR : ∀ j, (0 : K) < q j := fun j ↦ by exact_mod_cast hq j
  have hP : (0 : K) < ∏ j, (q j : K) ^ r j := Finset.prod_pos fun j _ ↦ pow_pos (hqR j) _
  set N : ℤ := ∑ d ∈ Q.support, Q.coeff d * ∏ j, h j ^ d j * q j ^ (r j - d j) with hN
  have hNeq : (N : K) = (∏ j, (q j : K) ^ r j) *
      eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) := by
    rw [eval_eq', support_map_of_injective _ Int.cast_injective, Finset.mul_sum, hN]
    push_cast
    refine Finset.sum_congr rfl fun d hd ↦ ?_
    rw [coeff_map, mul_left_comm, ← Finset.prod_mul_distrib]
    congr 1
    refine Finset.prod_congr rfl fun j _ ↦ ?_
    rw [← pow_sub_mul_pow (q j : K) ((monomial_le_degreeOf j hd).trans (hQ j)), div_pow]
    rw [mul_assoc, mul_div_cancel₀ _ (pow_ne_zero _ (hqR j).ne'), mul_comm]
  have h1 : (1 : K) ≤ |(N : K)| := by
    rw [← Int.cast_abs]
    exact_mod_cast Int.one_le_abs (Int.cast_ne_zero.mp (hNeq.symm ▸ mul_ne_zero hP.ne' hne))
  rwa [hNeq, abs_mul, abs_of_pos hP] at h1

/-- (2) The project statement is recovered from (1). -/
example {m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : Fin m → ℤ) {q : Fin m → ℕ} (hq : ∀ j, 0 < q j)
    (hne : eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| := by
  have := MvPolynomial.one_le_prod_pow_mul_abs_eval_div (K := ℝ) Q hQ h (fun j ↦ (q j : ℤ))
    (fun j ↦ by exact_mod_cast hq j) (by simpa using hne)
  simpa using this

-- (3) The univariate mathlib analogue, for comparison.
#check @one_le_pow_mul_abs_eval_div.{0}
