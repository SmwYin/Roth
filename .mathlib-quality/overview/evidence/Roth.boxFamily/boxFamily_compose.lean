import Roth.MainLemma
import Mathlib.RingTheory.MvPolynomial.Basic

/-! Evidence for the `/overview` assessment of `Roth.boxFamily`.

1. `boxFamily r B` is mathlib's `MvPolynomial.restrictSupport ℤ {d | ∀ j, d j ≤ r j}`
   intersected with the coefficient box `{W | ∀ d, W.coeff d ∈ Set.Icc 0 B}` (no finiteness
   on `σ` needed); for a constant bound it is `restrictDegree σ ℤ m ∩ ...`.
2. The generalised family (any ordered ring with locally finite order, arbitrary finite
   support set `S`, arbitrary coefficient interval `[a, b]`) is finite by the same one-line
   `Finset.finsupp` argument, so the specialisation to `ℤ`, `[0, B]` and boxes is not needed
   for finiteness. -/

open MvPolynomial

variable {σ : Type*}

/-- Composition with `restrictSupport`. -/
example (r : σ → ℕ) (B : ℕ) :
    Roth.boxFamily r B =
      {W | W ∈ restrictSupport ℤ {d : σ →₀ ℕ | ∀ j, d j ≤ r j} ∧
        ∀ d, W.coeff d ∈ Set.Icc (0 : ℤ) B} := by
  ext W
  simp only [Roth.boxFamily, Set.mem_ofPred_eq, mem_restrictSupport_iff, Set.mem_Icc]
  refine and_congr_left fun _ ↦ ⟨fun h d hd j ↦ (monomial_le_degreeOf j hd).trans (h j),
    fun h j ↦ degreeOf_le_iff.2 fun d hd ↦ h hd j⟩

/-- Constant bound: `restrictDegree`. -/
example (m B : ℕ) :
    Roth.boxFamily (fun _ : σ ↦ m) B =
      {W | W ∈ restrictDegree σ ℤ m ∧ ∀ d, W.coeff d ∈ Set.Icc (0 : ℤ) B} := by
  ext W
  simp only [Roth.boxFamily, Set.mem_ofPred_eq, mem_restrictDegree, Set.mem_Icc]
  refine and_congr_left fun _ ↦ ⟨fun h d hd j ↦ (monomial_le_degreeOf j hd).trans (h j),
    fun h j ↦ degreeOf_le_iff.2 fun d hd ↦ h d hd j⟩

/-- Generalised family: finite for any finite support set and any coefficient interval. -/
example {R : Type*} [CommRing R] [PartialOrder R] [LocallyFiniteOrder R]
    (S : Set (σ →₀ ℕ)) (hS : S.Finite) (a b : R) :
    {W : MvPolynomial σ R | (W.support : Set (σ →₀ ℕ)) ⊆ S ∧
      ∀ d, W.coeff d ∈ Set.Icc a b}.Finite := by
  classical
  refine ((hS.toFinset.finsupp fun _ ↦ Finset.Icc a b).finite_toSet.image
    AddMonoidAlgebra.ofCoeff).subset ?_
  rintro W ⟨hW, hc⟩
  refine ⟨W.coeff, ?_, rfl⟩
  rw [Finset.mem_coe, Finset.mem_finsupp_iff]
  exact ⟨fun d hd ↦ hS.mem_toFinset.2 (hW hd), fun d _ ↦ Finset.mem_Icc.2 (hc d)⟩
