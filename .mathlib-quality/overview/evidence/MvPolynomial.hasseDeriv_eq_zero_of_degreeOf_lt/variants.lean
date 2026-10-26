import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Most general vanishing criterion: no monomial of `P` dominates `d`. -/
theorem hasseDeriv_eq_zero_of_forall_not_le {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : ∀ k ∈ P.support, ¬ d ≤ k) : hasseDeriv d P = 0 := by
  ext e
  by_cases he : e + d ∈ P.support
  · exact absurd le_add_self (h _ he)
  · simp [coeff_hasseDeriv, notMem_support_iff.1 he]

/-- (2) The project statement as a corollary of (1). -/
example {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : degreeOf j P < d j) : hasseDeriv d P = 0 :=
  hasseDeriv_eq_zero_of_forall_not_le fun _ hk hdk ↦
    (h.trans_le (hdk j)).not_ge (monomial_le_degreeOf j hk)

/-- (3) Total-degree companion, also a corollary of (1). -/
theorem hasseDeriv_eq_zero_of_totalDegree_lt {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : P.totalDegree < d.degree) : hasseDeriv d P = 0 :=
  hasseDeriv_eq_zero_of_forall_not_le fun _ hk hdk ↦
    (h.trans_le (Finsupp.degree_mono hdk)).not_ge (le_totalDegree hk)

end MvPolynomial
