import Roth.Wronskian

/-! Evidence for `Roth.coeff_wronskian_of_natDegree_injective` (Roth/Wronskian.lean:122).
1. The identity holds over any `CommRing R` (project: `Field K`), with the same proof; the
   per-index product-coefficient helper is needed over `CommSemiring`.
2. The project statement is the `Field` specialisation (definitional via `Roth.wronskian`).
3. No hypothesis on the family is needed (the statement already has none). -/

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

/-- (1) The identity over an arbitrary commutative ring. -/
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

/-- (1') It elaborates over `ℤ`. -/
example (φ : Fin 3 → ℤ[X]) := coeff_wronskian φ

/-- (2) The project statement is the field specialisation. -/
example {K : Type*} [Field K] (φ : Fin l → K[X]) :
    (Roth.wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      (∏ ν, (φ ν).leadingCoeff) *
        (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det :=
  coeff_wronskian φ

end Evidence
