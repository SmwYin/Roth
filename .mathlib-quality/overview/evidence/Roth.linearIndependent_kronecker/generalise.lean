import Roth.GenWronskian
import Mathlib.Combinatorics.Additive.AP.Three.Behrend
import Mathlib.RingTheory.MvPolynomial.Basic

/-! Evidence for `Roth.linearIndependent_kronecker` (overview Step 9).
`weightedSubst`, `coeff_weightedSubst_weight` and the box lemmas are copied from the
`Roth.kronecker` / `Roth.coeff_kronecker` / `Roth.kronecker_eq_zero_iff` evidence. -/

open MvPolynomial

namespace Evidence

noncomputable def weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ) :
    MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ w j

theorem weightedSubst_monomial {R σ : Type*} [CommSemiring R] (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]

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

/-- InjOn on `restrictSupport` over a `CommSemiring` (no subtraction needed). -/
theorem injOn_weightedSubst_restrictSupport {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) :
    Set.InjOn (weightedSubst (R := R) w) (restrictSupport R S) := by
  intro P hP Q hQ h
  rw [SetLike.mem_coe, mem_restrictSupport_iff] at hP hQ
  ext d
  by_cases hd : d ∈ S
  · rw [← coeff_weightedSubst_weight hw hP hd, ← coeff_weightedSubst_weight hw hQ hd, h]
  · rw [notMem_support_iff.1 fun h ↦ hd (hP h), notMem_support_iff.1 fun h ↦ hd (hQ h)]

/-- 1. General form: any `CommSemiring`, any index type, any weight injective on a set `S`
containing all supports. A two-call composition of mathlib's
`LinearMap.linearIndependent_iff_of_injOn` with the InjOn lemma above. -/
theorem linearIndependent_weightedSubst {R σ ι : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {φ : ι → MvPolynomial σ R}
    (hφ : ∀ i, ↑(φ i).support ⊆ S) (h : LinearIndependent R φ) :
    LinearIndependent R (weightedSubst w ∘ φ) :=
  ((weightedSubst w).toLinearMap.linearIndependent_iff_of_injOn <|
    (injOn_weightedSubst_restrictSupport hw).mono <| Submodule.span_le.2 <|
      Set.range_subset_iff.2 fun i ↦ (mem_restrictSupport_iff R).2 (hφ i)).2 h

variable {K σ : Type*} [Field K] [Fintype σ] {l : ℕ}

theorem kroneckerExp_eq_weight (k : ℕ) (d : σ →₀ ℕ) :
    Roth.kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d := by
  simp [Roth.kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]

theorem weight_injOn_box (k : ℕ) :
    Set.InjOn (Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))
      {d : σ →₀ ℕ | ∀ j, d j < k} := by
  rw [show (Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ) : (σ →₀ ℕ) → ℕ) =
      Behrend.map k ∘ fun d i ↦ d ((Fintype.equivFin σ).symm i) by
    ext d; simp [Behrend.map_apply, ← kroneckerExp_eq_weight, Roth.kroneckerExp,
      ← (Fintype.equivFin σ).symm.sum_comp fun j ↦ d j * k ^ (Fintype.equivFin σ j : ℕ)]]
  refine Behrend.map_injOn.comp (fun d _ d' _ h ↦ ?_) fun d hd i ↦ hd _
  ext j; simpa using congrFun h (Fintype.equivFin σ j)

/-- 2. Project statement WITHOUT `hk : 1 < k` (and for any index type `ι`), as a one-line
specialisation of 1. -/
theorem linearIndependent_kronecker' {ι : Type*} {k : ℕ} {φ : ι → MvPolynomial σ K}
    (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent K φ) :
    LinearIndependent K fun ν ↦ Roth.kronecker k (φ ν) :=
  linearIndependent_weightedSubst (weight_injOn_box k)
    (fun ν _ he j ↦ (monomial_le_degreeOf j he).trans_lt (hφ ν j)) h

/-- 3. Agreement with the project lemma's exact statement. -/
example {k : ℕ} (hk : 1 < k) {φ : Fin l → MvPolynomial σ K}
    (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent K φ) :
    LinearIndependent K fun ν ↦ Roth.kronecker k (φ ν) :=
  Roth.linearIndependent_kronecker hk hφ h

end Evidence
