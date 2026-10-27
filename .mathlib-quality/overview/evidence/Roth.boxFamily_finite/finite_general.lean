import Roth.MainLemma

/-! Evidence for the `/overview` assessment of `Roth.boxFamily_finite`.

1. General multivariate finiteness lemma (any `CommSemiring R`, finite monomial set `S`,
   finite coefficient set `U`): no order, no `ℤ`, no box shape needed.
2. `Roth.boxFamily_finite` is a corollary of (1).
3. The univariate inline derivation in mathlib (`Polynomial.bUnion_roots_finite`,
   Roots.lean:627-634) follows from the same pattern. -/

open MvPolynomial

theorem MvPolynomial.finite_setOf_support_subset_coeff_mem {σ R : Type*} [CommSemiring R]
    {S : Set (σ →₀ ℕ)} (hS : S.Finite) {U : Set R} (hU : U.Finite) :
    {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d, p.coeff d ∈ U}.Finite := by
  classical
  refine ((hS.toFinset.finsupp fun _ ↦ hU.toFinset).finite_toSet.image
    AddMonoidAlgebra.ofCoeff).subset ?_
  rintro p ⟨hp, hc⟩
  refine ⟨p.coeff, ?_, rfl⟩
  rw [Finset.mem_coe, Finset.mem_finsupp_iff]
  exact ⟨fun d hd ↦ hS.mem_toFinset.2 (hp hd), fun d _ ↦ hU.mem_toFinset.2 (hc d)⟩

/-- `Roth.boxFamily_finite` as a corollary. -/
example {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (Roth.boxFamily r B).Finite := by
  classical
  refine (MvPolynomial.finite_setOf_support_subset_coeff_mem
    (Finset.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))).finite_toSet
    (Set.finite_Icc (0 : ℤ) B)).subset fun W hW ↦ ⟨fun d hd ↦ ?_, fun d ↦ hW.2 d⟩
  exact Finset.mem_Iic.2 fun j ↦ (monomial_le_degreeOf j hd).trans (hW.1 j)

/-- Univariate analogue (the shape re-derived inline in `Polynomial.bUnion_roots_finite`). -/
example {R : Type*} [Semiring R] (n : ℕ) {U : Set R} (hU : U.Finite) :
    {f : Polynomial R | f.natDegree ≤ n ∧ ∀ i, f.coeff i ∈ U}.Finite := by
  classical
  refine (((Finset.range (n + 1)).finsupp fun _ ↦ hU.toFinset).finite_toSet.image
    fun c ↦ Polynomial.ofFinsupp (AddMonoidAlgebra.ofCoeff c)).subset ?_
  rintro f ⟨hf, hc⟩
  refine ⟨f.toFinsupp.coeff, ?_, rfl⟩
  rw [Finset.mem_coe, Finset.mem_finsupp_iff]
  refine ⟨fun i hi ↦ Finset.mem_range_succ_iff.2
    ((Polynomial.le_natDegree_of_mem_supp i hi).trans hf),
    fun i _ ↦ hU.mem_toFinset.2 (hc i)⟩
