import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne`: the ℓ¹ coefficient norm and its core API generalise from
`MvPolynomial σ ℤ` to `MvPolynomial σ R` for any `[SeminormedCommRing R]`
(sum of coefficient norms over the support, in the
style of mathlib's `Polynomial.supNorm`); the project def is the
specialisation `R = ℤ`. -/

open MvPolynomial

namespace Evidence

variable {σ R : Type*} [SeminormedCommRing R]

/-- ℓ¹ norm of coefficients, general seminormed coefficient ring. -/
noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ :=
  ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_eq (p : MvPolynomial σ R) : l1Norm p = ∑ d ∈ p.support, ‖p.coeff d‖ := rfl

theorem l1Norm_nonneg (p : MvPolynomial σ R) : 0 ≤ l1Norm p :=
  Finset.sum_nonneg fun _ _ ↦ norm_nonneg _

theorem l1Norm_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1Norm p = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

@[simp] theorem l1Norm_zero : l1Norm (0 : MvPolynomial σ R) = 0 := by simp [l1Norm_eq]

theorem l1Norm_monomial (e : σ →₀ ℕ) (c : R) : l1Norm (monomial e c) = ‖c‖ := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_monomial_subset]
  simp

theorem norm_coeff_le_l1Norm (p : MvPolynomial σ R) (d : σ →₀ ℕ) : ‖p.coeff d‖ ≤ l1Norm p := by
  by_cases hd : d ∈ p.support
  · exact Finset.single_le_sum (f := fun d ↦ ‖p.coeff d‖) (fun _ _ ↦ norm_nonneg _) hd
  · simpa [notMem_support_iff.1 hd] using l1Norm_nonneg p

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

theorem l1Norm_mul_le (p q : MvPolynomial σ R) : l1Norm (p * q) ≤ l1Norm p * l1Norm q := by
  classical
  rw [MvPolynomial.mul_def]
  refine (l1Norm_sum_le _ _).trans ?_
  rw [l1Norm_eq, l1Norm_eq, Finset.sum_mul_sum]
  exact Finset.sum_le_sum fun a _ ↦ (l1Norm_sum_le _ _).trans <|
    Finset.sum_le_sum fun b _ ↦ by rw [l1Norm_monomial]; exact norm_mul_le _ _

/-- Bridge: the project def is the `R = ℤ` specialisation. -/
theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm_eq, Roth.normOne, Int.norm_eq_abs]

end Evidence
