import Roth.Taylor

/-! Evidence for `MvPolynomial.eq_sum_box_hasseDeriv` (overview run). -/

open MvPolynomial

namespace Evidence

variable {σ A : Type*} [CommRing A]

-- (1) CommSemiring weakening: the statement does not even typecheck (`X j - C (α j)` needs `Sub`).
section
variable {R : Type*} [CommSemiring R]
#check_failure (fun (α : σ → R) (j : σ) ↦
  (HSub.hSub (X j : MvPolynomial σ R) (C (α j) : MvPolynomial σ R) : MvPolynomial σ R))
end

-- (2) Sum form over the support of the translate: arbitrary `σ`, no `Fintype`, no `DecidableEq`,
-- no degree hypothesis.  Exact multivariate analogue of `Polynomial.sum_taylor_eq`.
theorem sum_taylor_eq (α : σ → A) (P : MvPolynomial σ A) :
    ∑ d ∈ (taylor α P).support, C ((taylor α P).coeff d) * d.prod (fun j n ↦ (X j - C (α j)) ^ n)
      = P := by
  conv_rhs => rw [← taylor_neg_taylor α P, (taylor α P).as_sum, map_sum]
  refine Finset.sum_congr rfl fun d _ ↦ ?_
  simp [taylor_monomial, sub_eq_add_neg]

-- (3) Generic finset form: any `s` containing all multi-indices with nonzero `(Δ_d P)(α)`.
theorem eq_sum_hasseDeriv_of_subset (α : σ → A) (P : MvPolynomial σ A) (s : Finset (σ →₀ ℕ))
    (hs : (taylor α P).support ⊆ s) :
    P = ∑ d ∈ s, C (eval α (hasseDeriv d P)) * d.prod fun j n ↦ (X j - C (α j)) ^ n := by
  conv_lhs => rw [← sum_taylor_eq α P]
  rw [Finset.sum_subset hs fun d _ hd ↦ by
    rw [notMem_support_iff.1 hd, map_zero, zero_mul]]
  simp [coeff_taylor]

-- (4) The project statement, with `Roth.box r` replaced by mathlib's `Finset.Iic`
-- (parent report Roth.box: REPLACE), recovered from (3).
theorem eq_sum_Iic_hasseDeriv [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r),
      C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by
  have hs : (taylor α P).support ⊆ Finset.Iic (Finsupp.equivFunOnFinite.symm r) := by
    intro e he
    rw [Finset.mem_Iic, Finsupp.le_def]
    intro j
    by_contra h
    rw [MvPolynomial.mem_support_iff, coeff_taylor,
      hasseDeriv_eq_zero_of_degreeOf_lt ((hP j).trans_lt (not_le.1 h)), map_zero] at he
    exact he rfl
  conv_lhs => rw [eq_sum_hasseDeriv_of_subset α P _ hs]
  exact Finset.sum_congr rfl fun d _ ↦ by rw [Finsupp.prod_fintype _ _ fun _ ↦ pow_zero _]

-- (5) The original project statement is a one-line corollary of (3).
example [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by
  have := eq_sum_Iic_hasseDeriv α r P hP
  convert this using 2
  ext d; simp [Roth.mem_box, Finsupp.le_def]

-- (6) The degree hypothesis cannot simply be dropped from the box form: `P = X 0`, `r = 0`.
example : ¬ ∀ (α : Fin 1 → ℤ) (P : MvPolynomial (Fin 1) ℤ),
    P = ∑ d ∈ Roth.box (fun _ ↦ 0), C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by
  intro h
  have := congrArg (totalDegree) (h 0 (X 0))
  have hbox : Roth.box (fun _ : Fin 1 ↦ 0) = {0} := by
    ext d; simp [Roth.mem_box, Finsupp.ext_iff]
  simp [hbox] at this

end Evidence
