import Roth.CoeffNorm

/-! Evidence for `Roth.degreeOf_det_hasseDeriv_le`. -/

open MvPolynomial

namespace Test

variable {σ n R : Type*} [CommRing R] [Fintype n] [DecidableEq n]

/-- (1) General Leibniz degree bound, column-wise bounds, any commutative ring, any
`Fintype` index. -/
theorem degreeOf_det_le_sum (M : Matrix n n (MvPolynomial σ R)) (j : σ) {c : n → ℕ}
    (hM : ∀ i k, degreeOf j (M i k) ≤ c k) : degreeOf j M.det ≤ ∑ k, c k := by
  rw [Matrix.det_apply]
  refine (degreeOf_sum_le _ _ _).trans (Finset.sup_le fun τ _ ↦ ?_)
  have hprod : degreeOf j (∏ i, M (τ i) i) ≤ ∑ k, c k :=
    (degreeOf_prod_le _ _ _).trans (Finset.sum_le_sum fun i _ ↦ hM _ _)
  rcases Int.units_eq_one_or (Equiv.Perm.sign τ) with h | h
  · simpa [h] using hprod
  · simpa [h, Units.neg_smul, degreeOf_neg] using hprod

/-- (2) Uniform corollary: entries of degree `≤ k` give `card n * k`. -/
theorem degreeOf_det_le (M : Matrix n n (MvPolynomial σ R)) (j : σ) {k : ℕ}
    (hM : ∀ i i', degreeOf j (M i i') ≤ k) : degreeOf j M.det ≤ Fintype.card n * k := by
  simpa using degreeOf_det_le_sum M j (c := fun _ ↦ k) hM

/-- (3) Row-wise version via `det_transpose`. -/
theorem degreeOf_det_le_sum_rows (M : Matrix n n (MvPolynomial σ R)) (j : σ) {c : n → ℕ}
    (hM : ∀ i k, degreeOf j (M i k) ≤ c i) : degreeOf j M.det ≤ ∑ i, c i := by
  simpa using degreeOf_det_le_sum M.transpose j (fun i k ↦ hM k i)

/-- (4) The project statement recovered as a one-line corollary. -/
example {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ)
    {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) (j : σ) :
    degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j := by
  simpa using degreeOf_det_le (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P) j
    fun μ ν ↦ (degreeOf_hasseDeriv_le j (E μ ν) P).trans (hP j)

end Test
