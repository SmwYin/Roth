import Roth.GenWronskian
import Mathlib.Combinatorics.Additive.AP.Three.Behrend

/-! Evidence for `Roth.kroneckerExp` (overview Step 9). -/

open MvPolynomial

namespace Evidence

variable {σ : Type*} [Fintype σ]

/-- 1. `Roth.kroneckerExp k` is mathlib's `Finsupp.weight` at the weight `j ↦ k ^ e j`,
as functions (so it is an `AddMonoidHom` for free). -/
theorem kroneckerExp_eq_weight (k : ℕ) :
    Roth.kroneckerExp (σ := σ) k = ⇑(Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) := by
  ext d
  simp [Roth.kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]

/-- 1'. Same equality via mathlib's `Finsupp.weight_eq_sum` (`[Fintype σ]` form). -/
example (k : ℕ) (d : σ →₀ ℕ) :
    Roth.kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d := by
  simp [Finsupp.weight_eq_sum, Roth.kroneckerExp]

/-- 2. Additivity (not proved in the project) is now free via `map_add`. -/
example (k : ℕ) (d d' : σ →₀ ℕ) :
    Roth.kroneckerExp k (d + d') = Roth.kroneckerExp k d + Roth.kroneckerExp k d' := by
  simp only [kroneckerExp_eq_weight, map_add]

/-- 3. Base-`k` injectivity stated against `Finsupp.weight`, transferred from the project
lemma (this is the API that would be needed upstream; general injective `e` not attempted). -/
theorem weight_pow_equivFin_injOn {k : ℕ} (hk : 1 < k) :
    Set.InjOn (Finsupp.weight fun j : σ ↦ k ^ (Fintype.equivFin σ j : ℕ))
      {d | ∀ j, d j < k} := by
  rw [← kroneckerExp_eq_weight]
  exact Roth.kroneckerExp_injOn hk

/-- 4. `kronecker_monomial` restated with `Finsupp.weight` (one line from the project lemma). -/
example {K : Type*} [Field K] (k : ℕ) (d : σ →₀ ℕ) (a : K) :
    Roth.kronecker k (monomial d a) =
      Polynomial.C a *
        Polynomial.X ^ Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d := by
  rw [Roth.kronecker_monomial, kroneckerExp_eq_weight]

/-- 5. `kroneckerExp` is also mathlib's `Behrend.map k` (an `AddMonoidHom (Fin n → ℕ) ℕ`,
`a ↦ ∑ i, a i * k ^ i`) after reindexing along `equivFin`. -/
theorem kroneckerExp_eq_behrendMap (k : ℕ) (d : σ →₀ ℕ) :
    Roth.kroneckerExp k d = Behrend.map k fun i ↦ d ((Fintype.equivFin σ).symm i) := by
  rw [Behrend.map_apply, Roth.kroneckerExp,
    ← (Fintype.equivFin σ).symm.sum_comp fun j ↦ d j * k ^ (Fintype.equivFin σ j : ℕ)]
  simp

/-- 6. The project's 12-line `kroneckerExp_injOn` follows from mathlib's `Behrend.map_injOn`
(no `1 < k` hypothesis needed). -/
theorem kroneckerExp_injOn' {k : ℕ} :
    Set.InjOn (Roth.kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by
  intro d hd d' hd' h
  rw [kroneckerExp_eq_behrendMap, kroneckerExp_eq_behrendMap] at h
  have := Behrend.map_injOn (fun i ↦ hd _) (fun i ↦ hd' _) h
  ext j
  simpa using congrFun this (Fintype.equivFin σ j)

end Evidence
