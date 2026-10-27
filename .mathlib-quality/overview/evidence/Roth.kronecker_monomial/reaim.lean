import Roth.GenWronskian

/-! Evidence for `Roth.kronecker_monomial` (overview Step 9), re-aimed at the generalised
setting of `Roth.kronecker` (weighted substitution) and `Roth.kroneckerExp` (`Finsupp.weight`). -/

open MvPolynomial

namespace Evidence

/-- Placeholder for the proposed `MvPolynomial.weightedSubst`. -/
noncomputable def weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ) :
    MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ w j

/-- 1. Re-aimed lemma: `[CommSemiring R]`, arbitrary `σ` (no `Fintype`), arbitrary weight. -/
theorem weightedSubst_monomial {R σ : Type*} [CommSemiring R] (w : σ → ℕ) (d : σ →₀ ℕ)
    (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]

/-- 2. The weight-`ℕ` image of `X j` (sanity check, `σ = ℕ`, `R = ℤ`). -/
example : weightedSubst (R := ℤ) (σ := ℕ) (fun j ↦ 3 ^ j) (monomial (Finsupp.single 2 1) 5) =
    Polynomial.C 5 * Polynomial.X ^ 9 := by
  rw [weightedSubst_monomial, Finsupp.weight_single]; norm_num

/-- 3. The project lemma is a one-line specialisation of the re-aimed lemma. -/
example {K σ : Type*} [Field K] [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) (a : K) :
    Roth.kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ Roth.kroneckerExp k d := by
  change weightedSubst (fun j : σ ↦ k ^ (Fintype.equivFin σ j : ℕ)) (monomial d a) = _
  have h := weightedSubst_monomial (fun j : σ ↦ k ^ (Fintype.equivFin σ j : ℕ)) d a
  simpa [Finsupp.weight_apply, Finsupp.sum_fintype, Roth.kroneckerExp] using h
  -- `Roth.kronecker k` is `weightedSubst (k ^ equivFin σ ·)` by `rfl`

/-- 4. The lemma is not a bare `aeval_monomial` instance: that lemma leaves
`d.prod fun i k ↦ (X ^ w i) ^ k`, and folding it into one power still needs
`pow_mul` + `Finset.prod_pow_eq_pow_sum` + `Finsupp.weight_apply`. -/
example {R σ : Type*} [CommSemiring R] (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    aeval (fun j ↦ (Polynomial.X : Polynomial R) ^ w j) (monomial d a) =
      Polynomial.C a * d.prod fun i k ↦ (Polynomial.X ^ w i) ^ k := by
  rw [aeval_monomial]; rfl

end Evidence
