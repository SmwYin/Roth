import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_mul_le`: submultiplicativity of the ℓ¹ coefficient norm
(1) for `MvPolynomial.l1Norm` over any `[SeminormedCommRing R]` (parent verdict target), with the
project statement recovered for `R = ℤ`; (2) for an `AbsoluteValue`-based ℓ¹ norm on a
`CommSemiring`; (3) for the ℓ¹ norm on `AddMonoidAlgebra R M` over a (noncommutative)
`[SeminormedRing R]` and any `[AddMonoid M]` (the ℓ¹(M) Banach-algebra setting). -/

open MvPolynomial

namespace Evidence84

section Seminormed

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_zero : l1Norm (0 : MvPolynomial σ R) = 0 := by simp [l1Norm]

theorem l1Norm_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1Norm p = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

theorem l1Norm_monomial (e : σ →₀ ℕ) (c : R) : l1Norm (monomial e c) = ‖c‖ := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_monomial_subset]
  simp

theorem l1Norm_add_le (p q : MvPolynomial σ R) : l1Norm (p + q) ≤ l1Norm p + l1Norm q := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_add,
    l1Norm_eq_sum_of_support_subset (s := p.support ∪ q.support) Finset.subset_union_left,
    l1Norm_eq_sum_of_support_subset (s := p.support ∪ q.support) Finset.subset_union_right,
    ← Finset.sum_add_distrib]
  exact Finset.sum_le_sum fun d _ ↦ by simpa using norm_add_le (p.coeff d) (q.coeff d)

theorem l1Norm_sum_le {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ R) :
    l1Norm (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1Norm (f i) :=
  Finset.le_sum_of_subadditive l1Norm l1Norm_zero.le l1Norm_add_le s f

/-- Target statement: the project proof with `abs_mul` replaced by `norm_mul_le`. -/
theorem l1Norm_mul_le (p q : MvPolynomial σ R) : l1Norm (p * q) ≤ l1Norm p * l1Norm q := by
  classical
  rw [MvPolynomial.mul_def]
  refine (l1Norm_sum_le _ _).trans ?_
  rw [l1Norm, l1Norm, Finset.sum_mul_sum]
  exact Finset.sum_le_sum fun a _ ↦ (l1Norm_sum_le _ _).trans <|
    Finset.sum_le_sum fun b _ ↦ (l1Norm_monomial _ _).trans_le (norm_mul_le _ _)

theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- Recovery of the exact project statement. -/
example (P Q : MvPolynomial σ ℤ) : Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q := by
  simpa only [l1Norm_int_eq_normOne] using l1Norm_mul_le P Q

end Seminormed

section AbsVal

variable {σ R : Type*} [CommSemiring R] (v : AbsoluteValue R ℝ)

noncomputable def l1NormAbv (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, v (p.coeff d)

theorem l1NormAbv_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1NormAbv v p = ∑ d ∈ s, v (p.coeff d) :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

theorem l1NormAbv_add_le (p q : MvPolynomial σ R) :
    l1NormAbv v (p + q) ≤ l1NormAbv v p + l1NormAbv v q := by
  classical
  rw [l1NormAbv_eq_sum_of_support_subset v support_add,
    l1NormAbv_eq_sum_of_support_subset v (s := p.support ∪ q.support) Finset.subset_union_left,
    l1NormAbv_eq_sum_of_support_subset v (s := p.support ∪ q.support) Finset.subset_union_right,
    ← Finset.sum_add_distrib]
  exact Finset.sum_le_sum fun d _ ↦ by simpa using v.add_le (p.coeff d) (q.coeff d)

theorem l1NormAbv_sum_le {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ R) :
    l1NormAbv v (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1NormAbv v (f i) :=
  Finset.le_sum_of_subadditive (l1NormAbv v) (by simp [l1NormAbv]) (l1NormAbv_add_le v) s f

theorem l1NormAbv_mul_le (p q : MvPolynomial σ R) :
    l1NormAbv v (p * q) ≤ l1NormAbv v p * l1NormAbv v q := by
  classical
  rw [MvPolynomial.mul_def]
  refine (l1NormAbv_sum_le v _ _).trans ?_
  rw [l1NormAbv, l1NormAbv, Finset.sum_mul_sum]
  refine Finset.sum_le_sum fun a _ ↦ (l1NormAbv_sum_le v _ _).trans <|
    Finset.sum_le_sum fun b _ ↦ ?_
  rw [l1NormAbv_eq_sum_of_support_subset v support_monomial_subset]
  simp

end AbsVal

section MonoidAlgebra

variable {R M : Type*} [SeminormedRing R] [AddMonoid M]

/-- ℓ¹ norm on the additive monoid algebra (noncommutative coefficients, any monoid). -/
noncomputable def l1NormAMA (f : AddMonoidAlgebra R M) : ℝ := ∑ m ∈ f.coeff.support, ‖f.coeff m‖

theorem l1NormAMA_eq_sum_of_support_subset {f : AddMonoidAlgebra R M} {s : Finset M}
    (hs : f.coeff.support ⊆ s) : l1NormAMA f = ∑ m ∈ s, ‖f.coeff m‖ :=
  Finset.sum_subset hs fun m _ hm ↦ by simp [Finsupp.notMem_support_iff.1 hm]

theorem l1NormAMA_add_le (f g : AddMonoidAlgebra R M) :
    l1NormAMA (f + g) ≤ l1NormAMA f + l1NormAMA g := by
  classical
  rw [l1NormAMA_eq_sum_of_support_subset (s := f.coeff.support ∪ g.coeff.support)
      (by rw [AddMonoidAlgebra.coeff_add]; exact Finsupp.support_add),
    l1NormAMA_eq_sum_of_support_subset (s := f.coeff.support ∪ g.coeff.support)
      Finset.subset_union_left,
    l1NormAMA_eq_sum_of_support_subset (s := f.coeff.support ∪ g.coeff.support)
      Finset.subset_union_right, ← Finset.sum_add_distrib]
  exact Finset.sum_le_sum fun m _ ↦ by
    simpa [AddMonoidAlgebra.coeff_add] using norm_add_le (f.coeff m) (g.coeff m)

theorem l1NormAMA_sum_le {ι : Type*} (s : Finset ι) (f : ι → AddMonoidAlgebra R M) :
    l1NormAMA (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1NormAMA (f i) :=
  Finset.le_sum_of_subadditive l1NormAMA (by simp [l1NormAMA]) l1NormAMA_add_le s f

theorem l1NormAMA_single (m : M) (c : R) : l1NormAMA (AddMonoidAlgebra.single m c) = ‖c‖ := by
  classical
  rw [l1NormAMA_eq_sum_of_support_subset (s := {m})
    (by rw [AddMonoidAlgebra.coeff_single]; exact Finsupp.support_single_subset)]
  simp [AddMonoidAlgebra.coeff_single]

theorem l1NormAMA_mul_le (f g : AddMonoidAlgebra R M) :
    l1NormAMA (f * g) ≤ l1NormAMA f * l1NormAMA g := by
  classical
  rw [AddMonoidAlgebra.mul_def]
  refine (l1NormAMA_sum_le _ _).trans ?_
  rw [l1NormAMA, l1NormAMA, Finset.sum_mul_sum]
  exact Finset.sum_le_sum fun a _ ↦ (l1NormAMA_sum_le _ _).trans <|
    Finset.sum_le_sum fun b _ ↦ (l1NormAMA_single _ _).trans_le (norm_mul_le _ _)

end MonoidAlgebra

end Evidence84
