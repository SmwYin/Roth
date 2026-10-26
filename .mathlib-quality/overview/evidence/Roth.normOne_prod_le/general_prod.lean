import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_prod_le`: the finite-product submultiplicativity of the ℓ¹
coefficient norm over a `[SeminormedCommRing R]`.
(1) with `‖(1 : R)‖ ≤ 1` (in particular `[NormOneClass R]`), any `Finset`;
(2) with no hypothesis on `‖1‖`, for nonempty `Finset`s (cf. `Finset.norm_prod_le'`);
(3) recovery of the exact project statement for `R = ℤ`. -/

open MvPolynomial

namespace Evidence85

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_nonneg (p : MvPolynomial σ R) : 0 ≤ l1Norm p :=
  Finset.sum_nonneg fun _ _ ↦ norm_nonneg _

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

theorem l1Norm_mul_le (p q : MvPolynomial σ R) : l1Norm (p * q) ≤ l1Norm p * l1Norm q := by
  classical
  rw [MvPolynomial.mul_def]
  refine (l1Norm_sum_le _ _).trans ?_
  rw [l1Norm, l1Norm, Finset.sum_mul_sum]
  exact Finset.sum_le_sum fun a _ ↦ (l1Norm_sum_le _ _).trans <|
    Finset.sum_le_sum fun b _ ↦ (l1Norm_monomial _ _).trans_le (norm_mul_le _ _)

/-- `l1Norm 1 = ‖1‖`, so some hypothesis on `‖(1 : R)‖` is needed for the empty product. -/
theorem l1Norm_one : l1Norm (1 : MvPolynomial σ R) = ‖(1 : R)‖ := by
  simpa using l1Norm_monomial (σ := σ) 0 (1 : R)

/-- (1) General form, weakest hypothesis `‖(1 : R)‖ ≤ 1` — the project proof verbatim. -/
theorem l1Norm_prod_le_of_norm_one_le {ι : Type*} (h1 : ‖(1 : R)‖ ≤ 1) (s : Finset ι)
    (f : ι → MvPolynomial σ R) : l1Norm (∏ i ∈ s, f i) ≤ ∏ i ∈ s, l1Norm (f i) :=
  Finset.le_prod_of_submultiplicative_of_nonneg l1Norm l1Norm_nonneg
    (l1Norm_one.trans_le h1) l1Norm_mul_le s f

/-- (1') Mathlib-idiomatic form with `[NormOneClass R]` (cf. `Finset.norm_prod_le`). -/
theorem l1Norm_prod_le [NormOneClass R] {ι : Type*} (s : Finset ι)
    (f : ι → MvPolynomial σ R) : l1Norm (∏ i ∈ s, f i) ≤ ∏ i ∈ s, l1Norm (f i) :=
  l1Norm_prod_le_of_norm_one_le norm_one.le s f

/-- (2) Nonempty form with no hypothesis on `‖1‖` (cf. `Finset.norm_prod_le'`). -/
theorem l1Norm_prod_le' {ι : Type*} (s : Finset ι) (hs : s.Nonempty)
    (f : ι → MvPolynomial σ R) : l1Norm (∏ i ∈ s, f i) ≤ ∏ i ∈ s, l1Norm (f i) := by
  classical
  induction hs using Finset.Nonempty.cons_induction with
  | singleton a => simp
  | cons a s ha hs ih =>
    rw [Finset.prod_cons, Finset.prod_cons]
    exact (l1Norm_mul_le _ _).trans
      (mul_le_mul_of_nonneg_left ih (l1Norm_nonneg _))

theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- (3) Recovery of the exact project statement. -/
example {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i) := by
  simpa only [l1Norm_int_eq_normOne] using l1Norm_prod_le s f

end Evidence85
