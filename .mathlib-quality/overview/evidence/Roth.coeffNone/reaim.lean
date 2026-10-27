import Roth.Separation

open MvPolynomial

-- (0) signature of the project def (does it carry the section's Fintype/DecidableEq?)
#check @Roth.coeffNone

section
variable {R : Type*} [CommSemiring R] {τ : Type*}

-- (1) coeffNone is definitionally mathlib's idiom `(optionEquivLeft R τ P).coeff ν`
example (P : MvPolynomial (Option τ) R) (ν : ℕ) :
    Roth.coeffNone P ν = (optionEquivLeft R τ P).coeff ν := rfl

-- (2) coeff_coeffNone in mathlib's `optionElim` spelling is literally `optionEquivLeft_coeff_coeff`
example (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (Roth.coeffNone P ν).coeff d = P.coeff (d.optionElim ν) :=
  optionEquivLeft_coeff_coeff R P ν d

-- (3) the optionEquivLeft analogue of mathlib's `degreeOf_coeff_finSuccEquiv` (absent in mathlib)
theorem degreeOf_coeff_optionEquivLeft (P : MvPolynomial (Option τ) R) (j : τ) (i : ℕ) :
    degreeOf j ((optionEquivLeft R τ P).coeff i) ≤ degreeOf (some j) P := by
  refine degreeOf_le_iff.2 fun d hd ↦ ?_
  simpa using monomial_le_degreeOf (some j) ((mem_support_coeff_optionEquivLeft R).1 hd)

-- (4) the expansion lemma via `Polynomial.as_sum_range'` transported along optionEquivLeft
example (P : MvPolynomial (Option τ) R) {n : ℕ} (hn : degreeOf none P ≤ n) :
    P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (Roth.coeffNone P ν) := by
  have h : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom := by
    ext i; simp
  apply (optionEquivLeft R τ).injective
  simp only [map_sum, map_mul, map_pow, optionEquivLeft_X_none,
    show ∀ Q, optionEquivLeft R τ (rename some Q) = Polynomial.C Q from
      fun Q ↦ AlgHom.congr_fun h Q, Roth.coeffNone]
  conv_lhs => rw [(optionEquivLeft R τ P).as_sum_range' (n + 1)
    (Nat.lt_succ_of_le ((natDegree_optionEquivLeft R P).trans_le hn))]
  refine Finset.sum_congr rfl fun ν _ ↦ ?_
  rw [Polynomial.X_pow_mul_C, Polynomial.C_mul_X_pow_eq_monomial]
end
