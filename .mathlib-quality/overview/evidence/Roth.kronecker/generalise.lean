import Roth.GenWronskian

/-! Evidence for `Roth.kronecker` (overview Step 9). -/

open MvPolynomial

namespace Evidence

/-- Weighted (Kronecker-type) substitution `x_j ↦ t^{w j}` over any commutative semiring,
for any variable type (no `Fintype`). -/
noncomputable def weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ) :
    MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ w j

/-- 1. `Roth.kronecker` is the special weight `w j = k ^ (equivFin σ j)`, definitionally. -/
example {K σ : Type*} [Field K] [Fintype σ] (k : ℕ) :
    (Roth.kronecker k : MvPolynomial σ K →ₐ[K] Polynomial K) =
      weightedSubst fun j ↦ k ^ (Fintype.equivFin σ j : ℕ) := rfl

/-- 2. `Roth.kroneckerExp` is mathlib's `Finsupp.weight` at that weight. -/
example {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) :
    Roth.kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d := by
  simp [Roth.kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]

/-- 3. General monomial lemma (generalises `Roth.kronecker_monomial`): CommSemiring, any `σ`. -/
theorem weightedSubst_monomial {R σ : Type*} [CommSemiring R] (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]

/-- 4. Elaborates over `ℤ` with an infinite variable type. -/
example : weightedSubst (R := ℤ) (σ := ℕ) (fun j ↦ 2 ^ j) (X 1) = Polynomial.X ^ 2 := by
  simp [weightedSubst]

end Evidence
