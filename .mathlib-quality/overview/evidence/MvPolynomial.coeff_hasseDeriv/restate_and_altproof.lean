import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.coeff_hasseDeriv`:
1. Restatement with the coefficient spelled `Finsupp.choose (e + d) d` (top index first, as in
   `Polynomial.hasseDeriv_coeff`) holds by the project lemma (definitional equality).
2. Alternative proof mirroring mathlib's `Polynomial.hasseDeriv_coeff`
   (`hasseDeriv_apply` + `coeff_sum` + `Finset.sum_eq_single`).
3. Weakening `CommSemiring R` to `Semiring R` is impossible for `MvPolynomial`
   (see parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`); the
   power-series companion over `Semiring R` is in parent evidence
   `MvPolynomial.hasseDeriv/generalise_mvpowerseries.lean` (its coefficient lemma is `rfl`). -/

namespace Finsupp
variable {σ : Type*}
/-- Multi-index binomial coefficient `binom(k, d)`. -/
def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
end Finsupp

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- Restatement in mathlib's univariate shape. -/
theorem coeff_hasseDeriv' (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = ((e + d).choose d : R) * P.coeff (e + d) :=
  coeff_hasseDeriv d e P

/-- Alternative proof following `Polynomial.hasseDeriv_coeff`. -/
theorem coeff_hasseDeriv_alt (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by
  classical
  rw [hasseDeriv_apply, coeff_sum]
  by_cases hP : e + d ∈ P.support
  · rw [Finset.sum_eq_single (e + d)]
    · simp
    · intro k _ hk
      rw [coeff_monomial]
      by_cases hdk : d ≤ k
      · split_ifs with h
        · exact absurd (h ▸ (tsub_add_cancel_of_le hdk).symm) hk
        · rfl
      · simp [(hasseCoeff_eq_zero_iff d k).2 hdk]
    · intro h; exact absurd hP h
  · rw [notMem_support_iff.1 hP, mul_zero]
    refine Finset.sum_eq_zero fun k hk ↦ ?_
    rw [coeff_monomial]
    by_cases hdk : d ≤ k
    · split_ifs with h
      · exact absurd (h ▸ (tsub_add_cancel_of_le hdk).symm ▸ hk) hP
      · rfl
    · simp [(hasseCoeff_eq_zero_iff d k).2 hdk]

end MvPolynomial
