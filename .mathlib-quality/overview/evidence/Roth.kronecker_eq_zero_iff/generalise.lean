import Roth.GenWronskian
import Mathlib.Combinatorics.Additive.AP.Three.Behrend
import Mathlib.RingTheory.MvPolynomial.Basic

/-! Evidence for `Roth.kronecker_eq_zero_iff` (overview Step 9). -/

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

/-- InjOn coefficient lemma (verified in the `Roth.coeff_kronecker` evidence). -/
theorem coeff_weightedSubst_weight {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) {d : σ →₀ ℕ} (hd : d ∈ S) :
    (weightedSubst w P).coeff (Finsupp.weight w d) = P.coeff d := by
  classical
  conv_lhs => rw [P.as_sum]
  rw [map_sum, Polynomial.finsetSum_coeff]
  simp_rw [weightedSubst_monomial, Polynomial.coeff_C_mul_X_pow]
  rw [Finset.sum_eq_single d]
  · simp
  · intro e he hed
    exact ite_eq_right fun h ↦ hed (hw (hP he) hd h.symm)
  · intro hdP
    simp [notMem_support_iff.1 hdP]

/-- 1. General `eq_zero_iff`: any `CommSemiring`, any `σ`, any weight injective on a set
containing the support. -/
theorem weightedSubst_eq_zero_iff {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) : weightedSubst w P = 0 ↔ P = 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ by rw [h, map_zero]⟩
  ext d
  by_cases hd : d ∈ P.support
  · simpa [h] using (coeff_weightedSubst_weight hw hP (hP hd)).symm
  · simpa using notMem_support_iff.1 hd

/-- 2. Modern-idiom form: `weightedSubst w` is injective on `restrictSupport R S`
(a linear-map-level statement; `eq_zero_iff` is the kernel form of the same fact). -/
theorem injOn_weightedSubst_restrictSupport {R σ : Type*} [CommRing R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) :
    Set.InjOn (weightedSubst (R := R) w) (restrictSupport R S) := by
  intro P hP Q hQ h
  rw [← sub_eq_zero, ← weightedSubst_eq_zero_iff hw, map_sub, h, sub_self]
  exact (restrictSupport R S).sub_mem hP hQ

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

theorem weight_injOn_box (k : ℕ) :
    Set.InjOn (Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))
      {d : σ →₀ ℕ | ∀ j, d j < k} := fun a ha b hb h ↦
  kroneckerExp_injOn' ha hb (by simpa [kroneckerExp_eq_weight] using h)

/-- 3. Project statement WITHOUT `hk : 1 < k`, as a specialisation of lemma 1. -/
theorem kronecker_eq_zero_iff' {k : ℕ} {P : MvPolynomial σ K}
    (hP : ∀ j, degreeOf j P < k) : Roth.kronecker k P = 0 ↔ P = 0 :=
  weightedSubst_eq_zero_iff (weight_injOn_box k)
    fun _ he j ↦ (monomial_le_degreeOf j he).trans_lt (hP j)

/-- 4. The `weightedSubst` form is definitionally `Roth.kronecker`. -/
example (k : ℕ) : (Roth.kronecker k : MvPolynomial σ K →ₐ[K] Polynomial K) =
    weightedSubst fun j ↦ k ^ (Fintype.equivFin σ j : ℕ) := rfl

/-- 5. Box version phrased with mathlib's `restrictDegree` (degrees `≤ k - 1`). -/
example {k : ℕ} : Set.InjOn (Roth.kronecker (K := K) (σ := σ) k)
    (restrictDegree σ K (k - 1)) := by
  intro P hP Q hQ h
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · -- `k = 0`: the box `{∀ i, n i ≤ 0}` is `{0}`; restrict to it.
    refine injOn_weightedSubst_restrictSupport (S := {n : σ →₀ ℕ | ∀ i, n i ≤ 0})
      (fun a ha b hb _ ↦ ?_) hP hQ h
    ext i; simp only [Set.mem_ofPred_eq, nonpos_iff_eq_zero] at ha hb; simp [ha, hb]
  · exact injOn_weightedSubst_restrictSupport
      ((weight_injOn_box k).mono (s₁ := {n : σ →₀ ℕ | ∀ i, n i ≤ k - 1})
        (s₂ := {d : σ →₀ ℕ | ∀ j, d j < k})
        fun n hn j ↦ by have := hn j; omega) hP hQ h

end Evidence
