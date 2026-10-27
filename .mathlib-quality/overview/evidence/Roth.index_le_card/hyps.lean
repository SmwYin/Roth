import Roth.Index

/-! Evidence for the `/overview` assessment of `Roth.index_le_card`. -/

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-! (1) `hP : P ≠ 0` is superfluous: `index 0 α r = sInf ∅ = 0`. -/
theorem index_le_card_noHP {P : MvPolynomial σ ℝ} {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j)
    (α : σ → ℝ) : index P α r ≤ Fintype.card σ := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp [index]
  · exact index_le_card hP hd α

/-! (2) The sharper, hypothesis-free form: the index is at most the weight of the vector of
partial degrees `(degreeOf j P)_j`. `index_le_card` follows from it and `weight_le_card`. -/
theorem index_le_sum_degreeOf (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r ≤ ∑ j, (degreeOf j P : ℝ) / r j := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp [index]
  obtain ⟨d, hd0, hdw⟩ := exists_weight_eq_index hP α r
  rw [← hdw, weight]
  refine Finset.sum_le_sum fun j _ ↦ div_le_div_of_nonneg_right ?_ (Nat.cast_nonneg _)
  have hmem : d ∈ (taylor α P).support := by rwa [mem_support_iff, coeff_taylor]
  exact_mod_cast (monomial_le_degreeOf j hmem).trans (degreeOf_taylor_le α j P)

/-! (3) `hd` is necessary: in one variable, `P = x ^ 2` at `α = 0`, `r = 1` has index `2 > 1`. -/
example : ¬ index (monomial (Finsupp.single () 2) 1 : MvPolynomial Unit ℝ) 0 1 ≤
    Fintype.card Unit := by
  rw [index_unique (by simp) 0 1, uniqueAlgEquiv_monomial, ← Polynomial.X_pow_eq_monomial,
    show (Polynomial.X : Polynomial ℝ) = Polynomial.X - Polynomial.C 0 by simp,
    Pi.zero_apply, Polynomial.rootMultiplicity_X_sub_C_pow]
  norm_num

end Roth
