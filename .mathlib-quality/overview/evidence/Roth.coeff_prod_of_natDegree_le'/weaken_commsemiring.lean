import Mathlib.Algebra.Polynomial.BigOperators

/-! Evidence for `Roth.coeff_prod_of_natDegree_le'` (Roth/Wronskian.lean:93).
1. The project proof goes through verbatim over any `CommSemiring R` (project: `Field K`).
2. Mathlib's uniform-bound `Polynomial.coeff_prod_of_natDegree_le` is the special case
   `n i := n`, so the project lemma strictly generalises it (per-index bounds). -/

open Polynomial

theorem coeff_prod_of_natDegree_le'' {R ι : Type*} [CommSemiring R] (s : Finset ι)
    (f : ι → R[X]) (n : ι → ℕ) (h : ∀ i ∈ s, (f i).natDegree ≤ n i) :
    (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s has ih =>
    simp only [Finset.forall_mem_insert] at h
    rw [Finset.prod_insert has, Finset.sum_insert has, Finset.prod_insert has,
      coeff_mul_add_eq_of_natDegree_le h.1 ((natDegree_prod_le _ _).trans (Finset.sum_le_sum h.2)),
      ih h.2]

example {R ι : Type*} [CommSemiring R] (s : Finset ι) (f : ι → R[X]) (n : ℕ)
    (h : ∀ p ∈ s, (f p).natDegree ≤ n) :
    (∏ i ∈ s, f i).coeff (s.card * n) = ∏ i ∈ s, (f i).coeff n := by
  simpa [Finset.sum_const, smul_eq_mul] using coeff_prod_of_natDegree_le'' s f (fun _ ↦ n) h
