import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_hasseDeriv_le`:
(1) the box form for `l1Norm` over any `[SeminormedCommRing R]`;
(2) a box-free form `l1Norm (Δ_d P) ≤ 2 ^ P.totalDegree * l1Norm P`, no `Fintype σ`, no `r`;
(3) recovery of the exact project statement for `R = ℤ`. -/

open MvPolynomial

namespace Evidence89

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

/-- Shared core: if every binomial factor on the support is `≤ C`, the ℓ¹ norm grows by `≤ C`. -/
theorem l1Norm_hasseDeriv_le_of_forall (d : σ →₀ ℕ) (P : MvPolynomial σ R) {C : ℕ}
    (hC : ∀ k ∈ P.support, hasseCoeff d k ≤ C) : l1Norm (hasseDeriv d P) ≤ C * l1Norm P := by
  classical
  rw [hasseDeriv_apply]
  refine (l1Norm_sum_le _ _).trans ?_
  rw [l1Norm, Finset.mul_sum]
  refine Finset.sum_le_sum fun k hk ↦ ?_
  rw [l1Norm_monomial, ← nsmul_eq_mul]
  exact norm_nsmul_le.trans <| mul_le_mul_of_nonneg_right (by exact_mod_cast hC k hk)
    (norm_nonneg _)

/-- (1) Project (box) shape over any seminormed commutative ring. -/
theorem l1Norm_hasseDeriv_le [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) : l1Norm (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * l1Norm P := by
  exact_mod_cast l1Norm_hasseDeriv_le_of_forall d P fun k hk ↦
    hasseCoeff_le_two_pow fun j ↦ (monomial_le_degreeOf j hk).trans (hP j)

/-- Multi-index `binom(k,d) ≤ 2^|k|` (as in the abs_coeff_hasseDeriv_le evidence). -/
theorem hasseCoeff_le_two_pow_degree (d k : σ →₀ ℕ) : hasseCoeff d k ≤ 2 ^ k.degree := by
  classical
  calc hasseCoeff d k = ∏ j ∈ d.support, (k j).choose (d j) := rfl
    _ ≤ ∏ j ∈ d.support, 2 ^ k j := Finset.prod_le_prod fun j _ ↦ Nat.choose_le_two_pow _ _
    _ = 2 ^ ∑ j ∈ d.support, k j := Finset.prod_pow_eq_pow_sum _ _ _
    _ ≤ 2 ^ k.degree := Nat.pow_le_pow_right two_pos <|
        Finset.sum_le_sum_of_ne_zero fun j _ hj ↦ Finsupp.mem_support_iff.2 hj

/-- (2) Box-free form: no `Fintype σ`, no degree box. -/
theorem l1Norm_hasseDeriv_le_two_pow_totalDegree (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    l1Norm (hasseDeriv d P) ≤ 2 ^ P.totalDegree * l1Norm P := by
  exact_mod_cast l1Norm_hasseDeriv_le_of_forall d P fun k hk ↦
    (hasseCoeff_le_two_pow_degree d k).trans <| Nat.pow_le_pow_right two_pos <| by
      exact (Finsupp.degree_apply k).symm ▸ le_totalDegree hk

theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- (3) Recovery of the exact project statement. -/
example [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) :
    Roth.normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * Roth.normOne P := by
  simpa only [l1Norm_int_eq_normOne] using l1Norm_hasseDeriv_le d P hP

end Evidence89
