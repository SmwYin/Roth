import Roth.Taylor

/-! Evidence for `MvPolynomial.eval_eq_sum_box` (overview run). -/

open MvPolynomial

namespace Evidence

-- (1) Semiring form (no subtraction): evaluation at `α + y` is the Taylor sum in powers of `y`,
-- over the support of the translate.  Arbitrary `σ`, `CommSemiring`, no hypotheses.
theorem eval_add_eq_sum_support {σ R : Type*} [CommSemiring R] (α y : σ → R)
    (P : MvPolynomial σ R) :
    eval (fun j ↦ y j + α j) P =
      ∑ d ∈ (taylor α P).support, eval α (hasseDeriv d P) * d.prod fun j n ↦ y j ^ n := by
  rw [← eval_taylor, eval_eq]
  simp [coeff_taylor, Finsupp.prod]

-- (2) Semiring form over any finset containing the support.
theorem eval_add_eq_sum_of_subset {σ R : Type*} [CommSemiring R] (α y : σ → R)
    (P : MvPolynomial σ R) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    eval (fun j ↦ y j + α j) P =
      ∑ d ∈ s, eval α (hasseDeriv d P) * d.prod fun j n ↦ y j ^ n := by
  rw [eval_add_eq_sum_support, Finset.sum_subset hs fun d _ hd ↦ by
    rw [notMem_support_iff, coeff_taylor] at hd; rw [hd, zero_mul]]

-- (3) Ring form with `x - α`, arbitrary `σ`, any superset of the support; no Fintype/DecidableEq.
theorem eval_eq_sum_of_subset {σ A : Type*} [CommRing A] (α x : σ → A)
    (P : MvPolynomial σ A) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    eval x P = ∑ d ∈ s, eval α (hasseDeriv d P) * d.prod fun j n ↦ (x j - α j) ^ n := by
  simpa using eval_add_eq_sum_of_subset α (fun j ↦ x j - α j) P s hs

-- (4) The project statement over mathlib's `Finset.Iic` (Roth.box REPLACE), from (3).
theorem eval_eq_sum_Iic {σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A)
    (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r),
      eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by
  have hs : (taylor α P).support ⊆ Finset.Iic (Finsupp.equivFunOnFinite.symm r) := by
    intro e he
    rw [Finset.mem_Iic, Finsupp.le_def]
    intro j
    by_contra h
    rw [MvPolynomial.mem_support_iff, coeff_taylor,
      hasseDeriv_eq_zero_of_degreeOf_lt ((hP j).trans_lt (not_le.1 h)), map_zero] at he
    exact he rfl
  rw [eval_eq_sum_of_subset α x P _ hs]
  exact Finset.sum_congr rfl fun d _ ↦ by rw [Finsupp.prod_fintype _ _ fun _ ↦ pow_zero _]

-- (5) Original project statement recovered from (4).
example {σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by
  rw [eval_eq_sum_Iic α x r P hP]
  congr 1
  ext d; simp [Roth.mem_box, Finsupp.le_def]

-- (6) Composition: the original is one `congrArg` away from the polynomial-form parent.
example {σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by
  simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)

-- (7) The degree hypothesis cannot be dropped from the box form: `P = X 0`, `r = 0`, `x = 1`.
example : ¬ ∀ (α x : Fin 1 → ℤ) (P : MvPolynomial (Fin 1) ℤ),
    eval x P = ∑ d ∈ Roth.box (fun _ ↦ 0), eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by
  intro h
  have hbox : Roth.box (fun _ : Fin 1 ↦ 0) = {0} := by
    ext d; simp [Roth.mem_box, Finsupp.ext_iff]
  have := h 0 1 (X 0)
  simp [hbox] at this

end Evidence
