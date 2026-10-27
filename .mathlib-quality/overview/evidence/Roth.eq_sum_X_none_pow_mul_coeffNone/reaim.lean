import Roth.Separation

open MvPolynomial

-- (0) signature of the project theorem
#check @Roth.eq_sum_X_none_pow_mul_coeffNone

section
variable {R : Type*} [CommSemiring R] {τ : Type*}

-- (1) re-aimed at optionEquivLeft: the inverse map is `aevalTower (rename some) (X none)`,
-- so the expansion is `optionEquivLeft_symm_apply` + `Polynomial.eval₂_eq_sum_range'`.
theorem eq_sum_rename_coeff_optionEquivLeft_mul_X_none_pow
    (P : MvPolynomial (Option τ) R) {n : ℕ} (hn : degreeOf none P < n) :
    P = ∑ i ∈ Finset.range n, rename some ((optionEquivLeft R τ P).coeff i) * X none ^ i := by
  conv_lhs => rw [← (optionEquivLeft R τ).symm_apply_apply P, optionEquivLeft_symm_apply]
  exact Polynomial.eval₂_eq_sum_range' _ ((natDegree_optionEquivLeft R P).trans_lt hn) _

-- (2) the exact project statement from (1) (factor order and `≤ n` vs `< n + 1`)
example (P : MvPolynomial (Option τ) R) {n : ℕ} (hn : degreeOf none P ≤ n) :
    P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (Roth.coeffNone P ν) :=
  (eq_sum_rename_coeff_optionEquivLeft_mul_X_none_pow P (Nat.lt_succ_of_le hn)).trans
    (Finset.sum_congr rfl fun _ _ ↦ mul_comm _ _)

-- (3) unconditional form with the natural bound
example (P : MvPolynomial (Option τ) R) :
    P = ∑ i ∈ Finset.range (degreeOf none P + 1),
      rename some ((optionEquivLeft R τ P).coeff i) * X none ^ i :=
  eq_sum_rename_coeff_optionEquivLeft_mul_X_none_pow P (Nat.lt_succ_self _)
end
