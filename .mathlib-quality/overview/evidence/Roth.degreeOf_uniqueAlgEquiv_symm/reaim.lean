import Mathlib.Algebra.MvPolynomial.Equiv
import Mathlib.Algebra.Polynomial.Degree.Lemmas

/-! Evidence for Roth.degreeOf_uniqueAlgEquiv_symm (Roth/Separation.lean:174).
(1) the forward mathlib-style twin of `natDegree_finSuccEquiv` / `natDegree_optionEquivLeft`
    declared inside `namespace MvPolynomial` (no name clash => name is free);
(2) the project's symm statement as a one-line corollary of (1);
(3) the project's own proof, verbatim, over `[CommSemiring R]` with mathlib-only imports. -/

namespace MvPolynomial

variable {R : Type*} [CommSemiring R] {σ : Type*} [Unique σ]

/-- (1) forward form -/
theorem natDegree_uniqueAlgEquiv (p : MvPolynomial σ R) :
    (uniqueAlgEquiv R σ p).natDegree = degreeOf default p := by
  apply le_antisymm
  · refine Polynomial.natDegree_le_iff_coeff_eq_zero.2 fun n hn ↦ ?_
    rw [coeff_uniqueAlgEquiv, ← notMem_support_iff]
    exact notMem_support_of_degreeOf_lt (i := default) (by simpa using hn)
  · rw [degreeOf_le_iff]
    intro e he
    rw [Finsupp.unique_single e, mem_support_iff, ← coeff_uniqueAlgEquiv] at he
    exact Polynomial.le_natDegree_of_ne_zero he

/-- (2) symm form as a corollary of (1) -/
theorem degreeOf_uniqueAlgEquiv_symm (f : Polynomial R) :
    degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree := by
  rw [← natDegree_uniqueAlgEquiv, AlgEquiv.apply_symm_apply]

end MvPolynomial

open MvPolynomial in
/-- (3) the project's proof, verbatim -/
example {R : Type*} [CommSemiring R] {σ : Type*} [Unique σ] (f : Polynomial R) :
    degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree := by
  apply le_antisymm
  · rw [degreeOf_le_iff]
    intro e he
    rw [mem_support_iff, MvPolynomial.coeff_uniqueAlgEquiv_symm] at he
    exact Polynomial.le_natDegree_of_ne_zero he
  · refine Polynomial.natDegree_le_iff_coeff_eq_zero.2 fun n hn ↦ ?_
    simpa only [mem_support_iff, MvPolynomial.coeff_uniqueAlgEquiv_symm,
      Finsupp.single_eq_same, not_not] using
      (notMem_support_of_degreeOf_lt (p := (uniqueAlgEquiv R σ).symm f) (i := default)
        (s := Finsupp.single default n) (by simpa only [Finsupp.single_eq_same] using hn))
