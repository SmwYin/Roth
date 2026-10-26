/-- A Hasse derivative of a polynomial with `deg_{X_j} P ≤ r_j` increases `normOne` by at most a
factor `2^{∑ r_j}`. Source: §3, proof of Lemma 3 ("An individual Hasse derivative of such a term
is zero or a monomial whose coefficient has absolute value at most `B 2^S`"). -/
theorem normOne_hasseDeriv_le [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P := by
  classical
  rw [hasseDeriv_apply]
  refine (normOne_sum_le _ _).trans ?_
  rw [normOne, Finset.mul_sum]
  refine Finset.sum_le_sum fun k hk ↦ ?_
  rw [normOne_monomial, Int.cast_mul, Int.cast_natCast, abs_mul, Nat.abs_cast]
  refine mul_le_mul_of_nonneg_right ?_ (abs_nonneg _)
  exact_mod_cast hasseCoeff_le_two_pow fun j ↦ (monomial_le_degreeOf j hk).trans (hP j)
