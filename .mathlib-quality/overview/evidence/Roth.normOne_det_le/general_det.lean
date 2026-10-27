import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_det_le`: the Leibniz bound `‖det M‖₁ ≤ n! C^n`
(1) for the ℓ¹ coefficient norm on `MvPolynomial σ R`, `[SeminormedCommRing R] [NormOneClass R]`,
    any `Fintype` index type `n` (not just `Fin l`);
(2) the abstract companion for any `[SeminormedCommRing R] [NormOneClass R]` (the
    submultiplicative analogue of mathlib's `Matrix.det_le`, which needs an `AbsoluteValue`);
(3) recovery of the exact project statement for `R = ℤ`, `n = Fin l`. -/

open MvPolynomial

namespace Evidence87

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_nonneg (p : MvPolynomial σ R) : 0 ≤ l1Norm p :=
  Finset.sum_nonneg fun _ _ ↦ norm_nonneg _

theorem l1Norm_zero : l1Norm (0 : MvPolynomial σ R) = 0 := by simp [l1Norm]

theorem l1Norm_neg (p : MvPolynomial σ R) : l1Norm (-p) = l1Norm p := by simp [l1Norm]

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

theorem l1Norm_one : l1Norm (1 : MvPolynomial σ R) = ‖(1 : R)‖ := by
  simpa using l1Norm_monomial (σ := σ) 0 (1 : R)

theorem l1Norm_prod_le [NormOneClass R] {ι : Type*} (s : Finset ι)
    (f : ι → MvPolynomial σ R) : l1Norm (∏ i ∈ s, f i) ≤ ∏ i ∈ s, l1Norm (f i) :=
  Finset.le_prod_of_submultiplicative_of_nonneg l1Norm l1Norm_nonneg
    (l1Norm_one.trans_le norm_one.le) l1Norm_mul_le s f

/-- (1) General ℓ¹ Leibniz bound, any finite index type — the project proof verbatim. -/
theorem l1Norm_det_le [NormOneClass R] {n : Type*} [Fintype n] [DecidableEq n]
    (M : Matrix n n (MvPolynomial σ R)) {C : ℝ} (hM : ∀ i j, l1Norm (M i j) ≤ C) :
    l1Norm M.det ≤ (Fintype.card n).factorial * C ^ Fintype.card n := by
  rw [Matrix.det_apply']
  calc _ ≤ ∑ τ : Equiv.Perm n, l1Norm (_ * ∏ i, M (τ i) i) := l1Norm_sum_le _ _
    _ ≤ ∑ _τ : Equiv.Perm n, C ^ Fintype.card n := Finset.sum_le_sum fun τ _ ↦ ?_
    _ = _ := by simp [Fintype.card_perm]
  rcases Int.units_eq_one_or (Equiv.Perm.sign τ) with h | h <;>
    simpa [h, l1Norm_neg] using (l1Norm_prod_le Finset.univ fun i ↦ M (τ i) i).trans
      ((Finset.prod_le_prod₀ (fun _ _ ↦ l1Norm_nonneg _) fun i _ ↦ hM _ _).trans_eq (by simp))

/-- (2) Abstract companion: Leibniz bound for any seminormed commutative ring with `‖1‖ = 1`
(mathlib's `Matrix.det_le` needs a multiplicative `AbsoluteValue`). -/
theorem norm_det_le [NormOneClass R] {n : Type*} [Fintype n] [DecidableEq n]
    (M : Matrix n n R) {C : ℝ} (hM : ∀ i j, ‖M i j‖ ≤ C) :
    ‖M.det‖ ≤ (Fintype.card n).factorial * C ^ Fintype.card n := by
  rw [Matrix.det_apply']
  calc _ ≤ ∑ τ : Equiv.Perm n, ‖_ * ∏ i, M (τ i) i‖ := norm_sum_le _ _
    _ ≤ ∑ _τ : Equiv.Perm n, C ^ Fintype.card n := Finset.sum_le_sum fun τ _ ↦ ?_
    _ = _ := by simp [Fintype.card_perm]
  rcases Int.units_eq_one_or (Equiv.Perm.sign τ) with h | h <;>
    simpa [h] using (Finset.le_prod_of_submultiplicative_of_nonneg (‖·‖) (fun _ ↦ norm_nonneg _)
        norm_one.le norm_mul_le Finset.univ fun i ↦ M (τ i) i).trans
      ((Finset.prod_le_prod₀ (fun _ _ ↦ norm_nonneg _) fun i _ ↦ hM _ _).trans_eq (by simp))

theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- (3) Recovery of the exact project statement. -/
example {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ}
    (hM : ∀ μ ν, Roth.normOne (M μ ν) ≤ C) : Roth.normOne M.det ≤ l.factorial * C ^ l := by
  simpa [l1Norm_int_eq_normOne] using
    l1Norm_det_le M (C := C) fun μ ν ↦ (l1Norm_int_eq_normOne _).trans_le (hM μ ν)

end Evidence87
