section Coeff

@[simp, grind =]
theorem mem_support_iff {p : MvPolynomial σ R} {m : σ →₀ ℕ} : m ∈ p.support ↔ p.coeff m ≠ 0 := by
  simp [support]

theorem notMem_support_iff {p : MvPolynomial σ R} {m : σ →₀ ℕ} : m ∉ p.support ↔ p.coeff m = 0 := by
  simp

theorem sum_def {A} [AddCommMonoid A] {p : MvPolynomial σ R} {b : (σ →₀ ℕ) → R → A} :
    (AddMonoidAlgebra.coeff p).sum b = ∑ m ∈ p.support, b m (p.coeff m) := by
  simp [support, Finsupp.sum]

theorem support_mul [DecidableEq σ] (p q : MvPolynomial σ R) :
