import Roth.GenWronskian
import Mathlib.Combinatorics.Additive.AP.Three.Behrend

/-! Evidence for `Roth.coeff_kronecker` (overview Step 9). -/

open MvPolynomial

namespace Evidence

/-- Weighted substitution `x_j ↦ t^{w j}` (as in the `Roth.kronecker` evidence). -/
noncomputable def weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ) :
    MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ w j

theorem weightedSubst_monomial {R σ : Type*} [CommSemiring R] (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]

/-- 1. General coefficient formula: any `CommSemiring`, any `σ`, no injectivity. -/
theorem coeff_weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ) (P : MvPolynomial σ R)
    (n : ℕ) : (weightedSubst w P).coeff n =
      ∑ e ∈ P.support with Finsupp.weight w e = n, P.coeff e := by
  classical
  conv_lhs => rw [P.as_sum]
  rw [map_sum, Polynomial.finsetSum_coeff, Finset.sum_filter]
  simp_rw [weightedSubst_monomial, Polynomial.coeff_C_mul_X_pow]
  exact Finset.sum_congr rfl fun e _ ↦ by split_ifs <;> simp_all [eq_comm]

/-- 2. Generalised `coeff_kronecker`: weight injective on a set containing the support and `d`. -/
theorem coeff_weightedSubst_weight {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) {d : σ →₀ ℕ} (hd : d ∈ S) :
    (weightedSubst w P).coeff (Finsupp.weight w d) = P.coeff d := by
  classical
  rw [coeff_weightedSubst, Finset.sum_eq_single d]
  · intro e he hed
    exact (hed (hw (hP (Finset.mem_filter.1 he).1) hd (Finset.mem_filter.1 he).2)).elim
  · intro hdP
    by_cases h : d ∈ P.support
    · exact (hdP (Finset.mem_filter.2 ⟨h, rfl⟩)).elim
    · exact notMem_support_iff.1 h

variable {K σ : Type*} [Field K] [Fintype σ]

theorem kroneckerExp_eq_weight (k : ℕ) (d : σ →₀ ℕ) :
    Roth.kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d := by
  simp [Roth.kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]

theorem kroneckerExp_injOn' {k : ℕ} :
    Set.InjOn (Roth.kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by
  rw [show Roth.kroneckerExp (σ := σ) k = Behrend.map k ∘ fun d i ↦ d ((Fintype.equivFin σ).symm i)
    by ext d; simp [Behrend.map_apply, Roth.kroneckerExp,
      ← (Fintype.equivFin σ).symm.sum_comp fun j ↦ d j * k ^ (Fintype.equivFin σ j : ℕ)]]
  refine Behrend.map_injOn.comp (fun d _ d' _ h ↦ ?_) fun d hd i ↦ hd _
  ext j; simpa using congrFun h (Fintype.equivFin σ j)

/-- 3. Project statement WITHOUT `hk : 1 < k`, original proof otherwise unchanged. -/
theorem coeff_kronecker' {k : ℕ} {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k)
    {d : σ →₀ ℕ} (hd : ∀ j, d j < k) :
    (Roth.kronecker k P).coeff (Roth.kroneckerExp k d) = P.coeff d := by
  classical
  conv_lhs => rw [P.as_sum]
  rw [map_sum, Polynomial.finsetSum_coeff]
  simp_rw [Roth.kronecker_monomial, Polynomial.coeff_C_mul_X_pow]
  rw [Finset.sum_eq_single d]
  · simp
  · intro e he hed
    exact ite_eq_right fun h ↦ hed (kroneckerExp_injOn'
      (fun j ↦ (monomial_le_degreeOf j he).trans_lt (hP j)) hd h.symm)
  · intro hdP
    simp [notMem_support_iff.1 hdP]

/-- 4. Project statement (no `hk`) as a specialisation of the general lemma 2. -/
example {k : ℕ} {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k)
    {d : σ →₀ ℕ} (hd : ∀ j, d j < k) :
    (Roth.kronecker k P).coeff (Roth.kroneckerExp k d) = P.coeff d := by
  have hinj : Set.InjOn (Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))
      {d : σ →₀ ℕ | ∀ j, d j < k} := by
    intro a ha b hb h
    exact kroneckerExp_injOn' ha hb (by simpa [kroneckerExp_eq_weight] using h)
  rw [kroneckerExp_eq_weight]
  exact coeff_weightedSubst_weight hinj
    (fun e he j ↦ (monomial_le_degreeOf j he).trans_lt (hP j)) hd

end Evidence
