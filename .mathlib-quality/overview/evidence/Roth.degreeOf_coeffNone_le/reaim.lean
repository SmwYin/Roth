import Roth.Separation

/-! Evidence for `Roth.degreeOf_coeffNone_le`, re-aimed at mathlib's `optionEquivLeft`. -/

namespace MvPolynomial

variable {R : Type*} [CommSemiring R] {σ : Type*}

-- (1) The re-aimed statement, declared inside `namespace MvPolynomial`: elaborating it without a
-- name clash confirms `MvPolynomial.degreeOf_coeff_optionEquivLeft` is absent from mathlib, and the
-- proof is the 2-line support argument (twin of `degreeOf_coeff_finSuccEquiv`, Equiv.lean:834).
theorem degreeOf_coeff_optionEquivLeft (p : MvPolynomial (Option σ) R) (j : σ) (i : ℕ) :
    degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p := by
  refine degreeOf_le_iff.2 fun d hd ↦ ?_
  simpa using monomial_le_degreeOf (some j) ((mem_support_coeff_optionEquivLeft R).1 hd)

-- (2) The project lemma is literally the re-aimed one (coeffNone unfolds by rfl).
example (P : MvPolynomial (Option σ) R) (ν : ℕ) (j : σ) :
    degreeOf j (Roth.coeffNone P ν) ≤ degreeOf (some j) P :=
  degreeOf_coeff_optionEquivLeft P j ν

-- (3) Conversely the project lemma states the re-aimed form directly (no unfolding needed).
example (p : MvPolynomial (Option σ) R) (j : σ) (i : ℕ) :
    degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p :=
  Roth.degreeOf_coeffNone_le p i j

-- (4) Existing mathlib siblings (for the report): totalDegree twin and finSuccEquiv twin.
#check @totalDegree_coeff_optionEquivLeft_le
#check @degreeOf_coeff_finSuccEquiv

end MvPolynomial
