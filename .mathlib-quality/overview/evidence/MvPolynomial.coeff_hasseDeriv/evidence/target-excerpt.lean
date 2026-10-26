main computational interface to `hasseDeriv`; most identities below are proved by `ext` followed
by rewriting with it.

Source: §1, Lean implementation note. -/
theorem coeff_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    rw [hasseDeriv_monomial, coeff_monomial, coeff_monomial]
    by_cases hk : k = e + d
    · simp [hk]
    by_cases hdk : d ≤ k
    · simp [hk, tsub_eq_iff_eq_add_of_le hdk]
    · simp [hk, (hasseCoeff_eq_zero_iff d k).2 hdk]
  | add p q hp hq => simp [hp, hq, mul_add]

/-- Over a finite set of variables, `hasseCoeff d k` is the full product
