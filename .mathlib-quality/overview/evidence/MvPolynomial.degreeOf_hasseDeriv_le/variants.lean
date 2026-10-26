import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.degreeOf_hasseDeriv_le`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Sharp form, analogue of `Polynomial.natDegree_hasseDeriv_le`. -/
theorem degreeOf_hasseDeriv_le_sub (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j := by
  refine degreeOf_le_iff.2 fun m hm ↦ ?_
  rw [mem_support_iff, coeff_hasseDeriv] at hm
  have := monomial_le_degreeOf j (mem_support_iff.2 (right_ne_zero_of_mul hm))
  simp only [Finsupp.add_apply] at this
  omega

/-- (2) The project statement is a one-line corollary of (1). -/
example (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P :=
  (degreeOf_hasseDeriv_le_sub j d P).trans tsub_le_self

/-- (3) Total-degree companion. -/
theorem totalDegree_hasseDeriv_le (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree := by
  refine Finset.sup_le fun m hm ↦ ?_
  rw [mem_support_iff, coeff_hasseDeriv] at hm
  have h1 := le_totalDegree (mem_support_iff.2 (right_ne_zero_of_mul hm))
  have h2 : ((m + d).sum fun _ e ↦ e) = (m.sum fun _ e ↦ e) + d.degree :=
    map_add Finsupp.degree m d
  omega

end MvPolynomial
