import Roth.Wronskian
import Mathlib.Algebra.Field.ZMod

/-! Evidence for `Roth.wronskian_ne_zero_of_natDegree_injective` (Roth/Wronskian.lean:148).
1. Char-free core: over a commutative domain, nonzero polynomials whose binomial determinant
   `det (C(d ν, μ))` is nonzero have nonzero Wronskian.
2. The `CharZero` + distinct-degree form holds over `[CommRing R] [IsDomain R] [CharZero R]`.
3. The project statement is the field specialisation.
4. `CharZero` cannot simply be dropped: in `ZMod 2`, `1` and `X ^ 2` have distinct degrees but
   zero Hasse Wronskian.
5. `hφ` cannot be dropped: the one-element family `0`. -/

open Polynomial

namespace Evidence

variable {R : Type*} [CommRing R] {l : ℕ}

noncomputable def wronskian (φ : Fin l → R[X]) : R[X] :=
  (Matrix.of fun μ ν : Fin l ↦ hasseDeriv μ (φ ν)).det

theorem coeff_prod_of_natDegree_le' {S ι : Type*} [CommSemiring S] (s : Finset ι)
    (f : ι → S[X]) (n : ι → ℕ) (h : ∀ i ∈ s, (f i).natDegree ≤ n i) :
    (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s has ih =>
    simp only [Finset.forall_mem_insert] at h
    rw [Finset.prod_insert has, Finset.sum_insert has, Finset.prod_insert has,
      coeff_mul_add_eq_of_natDegree_le h.1 ((natDegree_prod_le _ _).trans (Finset.sum_le_sum h.2)),
      ih h.2]

theorem coeff_wronskian (φ : Fin l → R[X]) :
    (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = (∏ ν, (φ ν).leadingCoeff) *
      (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : R)).det := by
  classical
  have key (σ : Equiv.Perm (Fin l)) : (∏ i, hasseDeriv (σ i : ℕ) (φ i)).coeff
      (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      ∏ i, ((φ i).natDegree.choose (σ i) : R) * (φ i).leadingCoeff := by
    by_cases h : ∀ i, (σ i : ℕ) ≤ (φ i).natDegree
    · rw [← Equiv.sum_comp σ (fun i : Fin l ↦ (i : ℕ)), ← Finset.sum_tsub_distrib _ fun i _ ↦ h i,
        coeff_prod_of_natDegree_le' _ _ _ fun i _ ↦ natDegree_hasseDeriv_le _ _]
      refine Finset.prod_congr rfl fun i _ ↦ ?_
      rw [hasseDeriv_coeff, Nat.sub_add_cancel (h i), leadingCoeff]
    · push Not at h
      obtain ⟨i, hi⟩ := h
      rw [Finset.prod_eq_zero (Finset.mem_univ i) (hasseDeriv_eq_zero_of_lt_natDegree _ _ hi),
        coeff_zero]
      exact (Finset.prod_eq_zero (Finset.mem_univ i) (by simp [Nat.choose_eq_zero_of_lt hi])).symm
  rw [wronskian, Matrix.det_apply', Matrix.det_apply', finsetSum_coeff, Finset.mul_sum]
  refine Finset.sum_congr rfl fun σ _ ↦ ?_
  simp [coeff_intCast_mul, key, Finset.prod_mul_distrib, mul_comm, mul_assoc]

theorem det_eval_descPochhammer {l : ℕ} (x : Fin l → R) :
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

theorem prod_factorial_mul_det_choose (d : Fin l → ℕ) :
    (∏ μ : Fin l, ((μ : ℕ).factorial : R)) *
        (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : R)).det =
      ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : R) - d i) := by
  rw [← Matrix.det_mul_column, ← Matrix.det_transpose, ← Matrix.det_vandermonde,
    ← det_eval_descPochhammer]
  congr 1
  ext i j
  simp [descPochhammer_eval_eq_descFactorial, Nat.descFactorial_eq_factorial_mul_choose]

/-- (1) Char-free core over a commutative domain. -/
theorem wronskian_ne_zero_of_det_choose_ne_zero [IsDomain R] {φ : Fin l → R[X]}
    (hφ : ∀ ν, φ ν ≠ 0)
    (hdet : (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : R)).det ≠ 0) :
    wronskian φ ≠ 0 := by
  intro h0
  have := coeff_wronskian φ
  rw [h0, coeff_zero, eq_comm] at this
  exact mul_ne_zero (Finset.prod_ne_zero_iff.2 fun ν _ ↦ leadingCoeff_ne_zero.2 (hφ ν)) hdet this

/-- (2) The distinct-degree statement over a characteristic-zero commutative domain. -/
theorem wronskian_ne_zero_of_natDegree_injective [IsDomain R] [CharZero R] {φ : Fin l → R[X]}
    (hφ : ∀ ν, φ ν ≠ 0) (hd : Function.Injective fun ν ↦ (φ ν).natDegree) :
    wronskian φ ≠ 0 := by
  refine wronskian_ne_zero_of_det_choose_ne_zero hφ fun h ↦ ?_
  have := prod_factorial_mul_det_choose (R := R) fun ν ↦ (φ ν).natDegree
  rw [h, mul_zero, eq_comm, Finset.prod_eq_zero_iff] at this
  obtain ⟨i, -, hi⟩ := this
  obtain ⟨j, hj, hij⟩ := Finset.prod_eq_zero_iff.1 hi
  rw [sub_eq_zero, Nat.cast_inj] at hij
  exact (Finset.mem_Ioi.1 hj).ne (hd hij).symm

/-- (2') It elaborates over `ℤ`. -/
example (φ : Fin 3 → ℤ[X]) (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν ↦ (φ ν).natDegree) : wronskian φ ≠ 0 :=
  wronskian_ne_zero_of_natDegree_injective hφ hd

/-- (3) The project statement is the field specialisation. -/
example {K : Type*} [Field K] [CharZero K] {φ : Fin l → K[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν ↦ (φ ν).natDegree) : Roth.wronskian φ ≠ 0 :=
  wronskian_ne_zero_of_natDegree_injective hφ hd

/-- (4) `CharZero` is needed: `1`, `X ^ 2` over `ZMod 2`. -/
example : Roth.wronskian (K := ZMod 2) ![1, X ^ 2] = 0 := by
  simp [Roth.wronskian, Roth.wronskianMatrix, Matrix.det_fin_two, hasseDeriv_one]
  exact CharTwo.add_self_eq_zero 1

/-- (5) `hφ` is needed. -/
example : Roth.wronskian (![0] : Fin 1 → ℚ[X]) = 0 := by
  simp [Roth.wronskian, Roth.wronskianMatrix]

end Evidence
