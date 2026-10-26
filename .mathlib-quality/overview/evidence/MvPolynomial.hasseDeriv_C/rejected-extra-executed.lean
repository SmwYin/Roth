import Roth.Taylor

/-! Constant derivative and affected Taylor branch experiments. -/
#check @MvPolynomial.hasseDeriv_C
#print MvPolynomial.hasseDeriv_C
#print axioms MvPolynomial.hasseDeriv_C
namespace HasseCTargetProbe
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
theorem original {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by
  rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)]
  simp
theorem unfolded {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by
  have hz : hasseCoeff d 0 = 0 := (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)
  rw [C_apply]
  simp [hasseDeriv, hz]
theorem caller (α : σ → R) {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) :
    (taylor α (monomial 0 a)).coeff d = eval α (hasseDeriv d (monomial 0 a)) := by
  simp only [← C_apply, taylor_C, hasseDeriv_C hd, map_zero, coeff_C_of_ne_zero hd]
theorem caller_inline (α : σ → R) {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) :
    (taylor α (monomial 0 a)).coeff d = eval α (hasseDeriv d (monomial 0 a)) := by
  have hz : hasseCoeff d 0 = 0 := (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)
  rw [show hasseDeriv d (monomial 0 a) = 0 by
    simp [hasseDeriv, hz]]
  simp only [← C_apply, taylor_C, coeff_C_of_ne_zero hd, map_zero]
#print axioms original
#print axioms unfolded
#print axioms caller
#print axioms caller_inline
theorem explicit_order (d : σ →₀ ℕ) (a : R) (hd : d ≠ 0) : hasseDeriv d (C a) = 0 :=
  original hd a
theorem all_orders (d : σ →₀ ℕ) (a : R) :
    hasseDeriv d (C a) = if d = 0 then C a else 0 := by
  classical
  by_cases hd : d = 0
  · subst d
    simp
  · rw [if_neg hd]
    exact original hd a
theorem false_arbitrary_linear_map :
    ¬ ∀ L : MvPolynomial Unit ℕ →ₗ[ℕ] MvPolynomial Unit ℕ,
      ∀ a : ℕ, L (C a) = 0 := by
  intro h
  have hh := h LinearMap.id 1
  simp at hh
#print axioms explicit_order
#print axioms all_orders
#print axioms false_arbitrary_linear_map
end HasseCTargetProbe
