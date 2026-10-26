import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseDeriv_zero_apply`:
1. Alternative proof by monomial induction (mirrors mathlib's univariate
   `Polynomial.hasseDeriv_zero'`, which uses `hasseDeriv_apply` + `Nat.choose_zero_right`).
2. Proof with the coefficient spelled via a multi-index `Finsupp.choose` (parent restatement):
   `Finsupp.choose k 0 = 1` closes it just as `hasseCoeff 0 k = 1` does.
3. Composition from mathlib alone is impossible: the operator is not in mathlib. The
   project-level one-call composition `LinearMap.congr_fun hasseDeriv_zero P` would be circular
   (`hasseDeriv_zero` is proved from this lemma).
4. `CommSemiring R` cannot be weakened (forced by `MvPolynomial`, see parent evidence). -/

namespace Finsupp
variable {σ : Type*}
def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
@[simp] theorem choose_zero_right (k : σ →₀ ℕ) : k.choose 0 = 1 := by simp [choose]
end Finsupp

namespace MvPolynomial
variable {σ R : Type*} [CommSemiring R]

theorem hasseDeriv_zero_apply_alt (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by
  induction P using MvPolynomial.induction_on' with
  | monomial k a => simp [-hasseDeriv_zero, hasseCoeff]
  | add p q hp hq => simp [-hasseDeriv_zero, hp, hq]

theorem hasseDeriv_zero_apply_choose (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by
  ext e
  have h : ∀ k : σ →₀ ℕ, hasseCoeff 0 k = k.choose 0 := fun _ ↦ rfl
  simp [-hasseDeriv_zero, coeff_hasseDeriv, h]

/-- Once the bundled `@[simp] hasseDeriv_zero` exists, the pointwise form is `simp`-provable
(as for mathlib's `Polynomial.hasseDeriv_zero'` vs `Polynomial.hasseDeriv_zero`). -/
example (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by simp

end MvPolynomial
