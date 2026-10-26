import Roth.Wronskian
import Mathlib.RingTheory.Binomial

/-! Evidence for `Roth.det_choose_eq`: char-free and binomial-ring generalisations,
recovery of the project statement, and necessity of `CharZero` for the stated form. -/

open Polynomial

namespace Evidence

/-- Helper: the evaluation determinant of the falling factorials is the Vandermonde
determinant, over any commutative ring (mathlib's version needs a domain for
`descPochhammer_natDegree`/`monic_descPochhammer`; we reduce to `ℤ` by `map`). -/
theorem det_eval_descPochhammer {R : Type*} [CommRing R] {l : ℕ} (x : Fin l → R) :
    (Matrix.of fun i j : Fin l ↦ (descPochhammer R j).eval (x i)).det =
      (Matrix.vandermonde x).det := by
  have hdeg (j : Fin l) : (descPochhammer R j).natDegree ≤ j := by
    rw [← descPochhammer_map (Int.castRingHom R)]
    exact (natDegree_map_le).trans (descPochhammer_natDegree ℤ _).le
  rw [Matrix.eval_matrixOfPolynomials_eq_vandermonde_mul_matrixOfPolynomials x _ hdeg,
    Matrix.det_mul]
  have h1 : (Matrix.of fun i j : Fin l ↦ (descPochhammer R j).coeff i) =
      (Matrix.of fun i j : Fin l ↦ (descPochhammer ℤ j).coeff i).map (Int.castRingHom R) := by
    ext i j
    rw [Matrix.map_apply, Matrix.of_apply, Matrix.of_apply,
      ← descPochhammer_map (Int.castRingHom R), coeff_map]
  rw [h1, ← RingHom.mapMatrix_apply, ← RingHom.map_det, Matrix.det_matrixOfPolynomials _
    (fun i ↦ descPochhammer_natDegree ℤ _) (fun i ↦ monic_descPochhammer ℤ _), map_one, mul_one]

/-- (1) Char-free form over any commutative ring, natural-number nodes. -/
theorem prod_factorial_mul_det_choose {R : Type*} [CommRing R] {l : ℕ} (d : Fin l → ℕ) :
    (∏ μ : Fin l, ((μ : ℕ).factorial : R)) *
        (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : R)).det =
      ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : R) - d i) := by
  rw [← Matrix.det_mul_column, ← Matrix.det_transpose, ← Matrix.det_vandermonde,
    ← det_eval_descPochhammer]
  congr 1
  ext i j
  simp [descPochhammer_eval_eq_descFactorial, Nat.descFactorial_eq_factorial_mul_choose]

/-- (2) Binomial-ring form: arbitrary nodes `x ν` in a binomial ring, `Ring.choose`. -/
theorem prod_factorial_mul_det_ringChoose {R : Type*} [CommRing R] [BinomialRing R] {l : ℕ}
    (x : Fin l → R) :
    (∏ μ : Fin l, ((μ : ℕ).factorial : R)) *
        (Matrix.of fun μ ν : Fin l ↦ Ring.choose (x ν) μ).det =
      ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, (x j - x i) := by
  rw [← Matrix.det_mul_column, ← Matrix.det_transpose, ← Matrix.det_vandermonde,
    ← det_eval_descPochhammer]
  congr 1
  ext i j
  rw [Matrix.transpose_apply, Matrix.of_apply, Matrix.of_apply, Matrix.of_apply,
    ← descPochhammer_map (algebraMap ℤ R), eval_map_algebraMap, aeval_eq_smeval,
    Ring.descPochhammer_eq_factorial_smul_choose, nsmul_eq_mul]

/-- (3) The project statement follows from (1) in a characteristic-zero field. -/
example {K : Type*} [Field K] [CharZero K] {l : ℕ} (d : Fin l → ℕ) :
    (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det =
      (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) *
        ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i) := by
  rw [← prod_factorial_mul_det_choose, Finset.prod_inv_distrib, inv_mul_cancel_left₀
    (Finset.prod_ne_zero_iff.2 fun μ _ ↦ by exact_mod_cast μ.1.factorial_ne_zero)]

/-- (4) `CharZero` cannot be dropped from the `⁻¹` form: false in `ZMod 2` at `l = 3`. -/
example : ¬ ∀ d : Fin 3 → ℕ,
    (Matrix.of fun μ ν : Fin 3 ↦ ((d ν).choose μ : ZMod 2)).det =
      (∏ μ : Fin 3, ((μ : ℕ).factorial : ZMod 2)⁻¹) *
        ∏ i : Fin 3, ∏ j ∈ Finset.Ioi i, ((d j : ZMod 2) - d i) := by
  intro h
  have := h ![0, 1, 2]
  revert this
  decide

end Evidence
