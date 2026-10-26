section AsSum

@[simp]
theorem support_sum_monomial_coeff (p : MvPolynomial σ R) :
    ∑ v ∈ p.support, monomial v (p.coeff v) = p := by
  apply AddMonoidAlgebra.ext; rw [AddMonoidAlgebra.coeff_sum]; exact Finsupp.sum_single _

theorem as_sum (p : MvPolynomial σ R) : p = ∑ v ∈ p.support, monomial v (p.coeff v) :=
  (support_sum_monomial_coeff p).symm

