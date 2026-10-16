import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Algebra.Polynomial.RingDivision
import Mathlib.Algebra.Polynomial.Taylor
import Mathlib.Basic.Real.Pointwise
import Mathlib.Data.Nat.Cast.Field
import Mathlib.Order.ConditionallyCompleteLattice.Finset
import Mathlib.RingTheory.MvPowerSeries.NoZeroDivisors

import Roth.Box
import Roth.Taylor

/-!
# The index of a polynomial

The *index* of a nonzero real polynomial `P` at a point `α` relative to positive integers `r j` is
the minimum of `∑ j, d j / r j` over all multi-indices `d` with `(Δ_d P)(α) ≠ 0`, i.e. over the
support of the translate `P(X + α)`.  By convention `index 0 α r = 0` (the source uses `+∞` for
the zero polynomial; every lemma below carries explicit nonvanishing hypotheses instead, which
is how the convention is used in the source).

## Main definitions

* `Roth.index P α r`: the index of `P` at `α` relative to the weights `r`.

## Main results

* `Roth.le_index_iff`: lower bounds for the index of a nonzero polynomial.
* `Roth.index_eq_zero_iff`: the index vanishes iff `P(α) ≠ 0`.
* `Roth.index_hasseDeriv_ge`: differentiating lowers the index by at most the weight.
* `Roth.le_index_sum`, `Roth.index_mul`, `Roth.index_prod`: the index of sums and products.
* `Roth.index_eq_weightedOrder_div`: the index as a weighted order of a power series.
* `Roth.index_rename`, `Roth.index_unique`: the index under renaming and in one variable.

## References

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §4 "Index" (definition of the index,
the lemmas `index ≥ 0`, `index-of-derivative`, Lemma 4-1, Lemma 4-2 and the scaling identities)
(`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open MvPolynomial
open scoped Pointwise

variable {σ : Type*} [Fintype σ] [DecidableEq σ]

/-- The index of `P` at `α` relative to `r`. Source: §4, definition of the index and the Lean
implementation note ("Define the index as the minimum of `∑ d_j/r_j` over its nonzero
coefficients"). -/
noncomputable def index (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : ℝ :=
  sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))

omit [Fintype σ] [DecidableEq σ] in
private lemma mem_support_taylor_iff {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ} :
    d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 := by
  rw [mem_support_iff, coeff_taylor]

omit [DecidableEq σ] in
/-- The index is at most the weight of any multi-index `d` with `(Δ_d P)(α) ≠ 0`.
Source: §4, definition of the index ("the minimum ... over all tuples `(i_1, …, i_p)` such
that `Δ_i P(α) ≠ 0`"). -/
theorem index_le_weight {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ}
    (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d :=
  csInf_le ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
    (Set.mem_image_of_mem _ (Finset.mem_coe.2 (mem_support_taylor_iff.2 h)))

omit [DecidableEq σ] in
/-- For nonzero `P`, the index is attained by some multi-index `d` with `(Δ_d P)(α) ≠ 0`.
Source: §4, definition of the index ("Thus this is an attained minimum"). -/
theorem exists_weight_eq_index {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by
  obtain ⟨d, hd, hdw⟩ :=
    (show (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))).Nonempty by
      simpa using hP).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))
  exact ⟨d, mem_support_taylor_iff.1 hd, hdw⟩

omit [DecidableEq σ] in
/-- The characterisation of lower bounds for the index of a nonzero polynomial: `c ≤ index P α r`
iff every multi-index `d` with `(Δ_d P)(α) ≠ 0` has weight at least `c`. -/
theorem le_index_iff {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {α : σ → ℝ} {r : σ → ℕ} {c : ℝ} :
    c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by
  refine ⟨fun h d hd ↦ h.trans (index_le_weight hd), fun h ↦ ?_⟩
  refine le_csInf (by simpa using hP) ?_
  rintro _ ⟨d, hd, rfl⟩
  exact h d (mem_support_taylor_iff.1 hd)

omit [DecidableEq σ] in
/-- The index is nonnegative. Source: §4, first lemma on the index ("We have `ind(P) ≥ 0`"). -/
theorem index_nonneg (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r :=
  Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)

omit [DecidableEq σ] in
/-- For nonzero `P` and positive weights, the index vanishes iff `P(α) ≠ 0`.
Source: §4, first lemma on the index ("`ind(P) = 0` if and only if `P(α_1, …, α_p) ≠ 0`"). -/
theorem index_eq_zero_iff {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j)
    (α : σ → ℝ) : index P α r = 0 ↔ eval α P ≠ 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ (index_nonneg P α r).antisymm' ?_⟩
  · obtain ⟨d, hd, hdw⟩ := exists_weight_eq_index hP α r
    rw [h, weight_eq_zero_iff hr] at hdw
    subst hdw
    simpa [hasseDeriv_zero_apply] using hd
  · simpa using index_le_weight (r := r) (d := 0) (by simpa [hasseDeriv_zero_apply] using h)

omit [DecidableEq σ] in
/-- Applying `Δ_k` lowers the index by at most the weight of `k`.
Source: §4, Lemma `lem:index-of-derivative` ("`ind(Δ_k P) ≥ ind(P) - ∑ k_j / r_j`"). -/
theorem index_hasseDeriv_ge {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : hasseDeriv k P ≠ 0)
    (α : σ → ℝ) (r : σ → ℕ) : index P α r - weight r k ≤ index (hasseDeriv k P) α r := by
  obtain ⟨i, hi, hiw⟩ := exists_weight_eq_index hk α r
  rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, map_mul, eval_C, mul_ne_zero_iff] at hi
  exact sub_le_iff_le_add.2 (by simpa [weight_add, hiw] using index_le_weight (r := r) hi.2)

omit [DecidableEq σ] in
/-- Source: §4, Lemma 4-1 ("`ind(P + Q) ≥ min(ind P, ind Q)`"), in the form used in the proof of
Lemma 6 (a common lower bound for the nonzero summands is a lower bound for a nonzero sum). -/
theorem le_index_sum {ι : Type*} {s : Finset ι} {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ}
    (hs : ∑ i ∈ s, f i ≠ 0) {c : ℝ} (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) :
    c ≤ index (∑ i ∈ s, f i) α r := by
  refine (le_index_iff hs).2 fun d hd ↦ ?_
  rw [map_sum, map_sum] at hd
  obtain ⟨i, hi, hid⟩ := Finset.exists_ne_zero_of_sum_ne_zero hd
  have hfi : f i ≠ 0 := fun h0 ↦ hid (by rw [h0, map_zero, map_zero])
  exact (le_index_iff hfi).1 (hf i hi hfi) d hid

omit [DecidableEq σ] in
/-- The rational weight of `d` as a natural-number weight divided by `D = ∏ r_j`.
Source: §4, Lean implementation note ("set `D = ∏ r_j` and use the natural weights
`w_j = D / r_j`"). -/
theorem weight_eq_finsuppWeight_div {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) :
    weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i := by
  have hD : (0 : ℝ) < ∏ i, (r i : ℝ) := Finset.prod_pos fun i _ ↦ by exact_mod_cast hr i
  rw [weight, Finsupp.weight_eq_sum, Nat.cast_sum, Finset.sum_div, Nat.cast_prod]
  refine Finset.sum_congr rfl fun j _ ↦ ?_
  rw [smul_eq_mul, Nat.cast_mul,
    Nat.cast_div_charZero (Finset.dvd_prod_of_mem _ (Finset.mem_univ j)), Nat.cast_prod,
    ← mul_div_assoc, div_right_comm, mul_div_cancel_right₀ _ hD.ne']

/-- The index as the weighted order of the Taylor expansion `P(X + α)`, viewed as a power series,
divided by `D = ∏ r_j`. Source: §4, Lean implementation note ("use the natural weights in
`MvPowerSeries.weightedOrder`, then divide the finite value by `D` after embedding `P_α` as a
power series"). -/
theorem index_eq_weightedOrder_div {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (α : σ → ℝ) :
    index P α r =
      (((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j => (∏ i, r i) / r j).toNat : ℝ) /
        ∏ i, r i := by
  set w : σ → ℕ := fun j => (∏ i, r i) / r j
  set F : MvPowerSeries σ ℝ := ↑(taylor α P) with hFdef
  have hF : F ≠ 0 := by rwa [hFdef, Ne, MvPolynomial.coe_eq_zero_iff, taylor_eq_zero_iff]
  have hfin := (MvPowerSeries.ne_zero_iff_weightedOrder_finite w).1 hF
  apply le_antisymm
  · obtain ⟨d, hd, hdw⟩ := MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder w hfin
    rw [MvPolynomial.coeff_coe] at hd
    rw [← hdw, ENat.toNat_natCast, ← weight_eq_finsuppWeight_div hr]
    exact index_le_weight (mem_support_taylor_iff.1 (mem_support_iff.2 hd))
  · obtain ⟨e, he, hew⟩ := exists_weight_eq_index hP α r
    rw [← hew, weight_eq_finsuppWeight_div hr]
    refine div_le_div_of_nonneg_right ?_ (Nat.cast_nonneg _)
    have h1 := MvPowerSeries.weightedOrder_le w (f := F) (d := e)
      (by rw [hFdef, MvPolynomial.coeff_coe]; exact mem_support_iff.1 (mem_support_taylor_iff.2 he))
    rw [← hfin] at h1
    exact_mod_cast h1

/-- The index is additive on products of nonzero polynomials.
Source: §4, Lemma 4-1 ("`ind(P Q) = ind(P) + ind(Q)`"). -/
theorem index_mul {P Q : MvPolynomial σ ℝ} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) : index (P * Q) α r = index P α r + index Q α r := by
  have hPQ : P * Q ≠ 0 := mul_ne_zero hP hQ
  rw [index_eq_weightedOrder_div hP hr, index_eq_weightedOrder_div hQ hr,
    index_eq_weightedOrder_div hPQ hr, ← add_div, map_mul, MvPolynomial.coe_mul,
    MvPowerSeries.weightedOrder_mul]
  congr 1
  have hfin : ∀ R : MvPolynomial σ ℝ, R ≠ 0 →
      ((taylor α R : MvPowerSeries σ ℝ).weightedOrder fun j => (∏ i, r i) / r j) ≠ ⊤ := by
    intro R hR
    rwa [Ne, MvPowerSeries.weightedOrder_eq_top_iff, MvPolynomial.coe_eq_zero_iff,
      taylor_eq_zero_iff]
  rw [ENat.toNat_add (hfin P hP) (hfin Q hQ), Nat.cast_add]

/-- The index is additive on finite products of nonzero polynomials.
Source: §4, Lemma 4-1, iterated ("`ind ∏_ν ... = ∑_ν ind ...`", as used in the proof of
Lemma 6). -/
theorem index_prod {ι : Type*} (s : Finset ι) {f : ι → MvPolynomial σ ℝ} (hf : ∀ i ∈ s, f i ≠ 0)
    (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r := by
  classical
  induction s using Finset.induction_on with
  | empty =>
    rw [Finset.prod_empty, Finset.sum_empty]
    exact (index_eq_zero_iff one_ne_zero hr α).2 (by simp)
  | insert a s has ih =>
    rw [Finset.prod_insert has, Finset.sum_insert has,
      index_mul (hf a (Finset.mem_insert_self a s))
        (Finset.prod_ne_zero_iff.2 fun i hi => hf i (Finset.mem_insert_of_mem hi)) α hr,
      ih fun i hi => hf i (Finset.mem_insert_of_mem hi)]

/-- Source: §5, proof of Lemma 6 ("Multiplication by a sign does not change the index"). -/
theorem index_neg (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index (-P) α r = index P α r := by
  simp [index, support_neg]

/-- Source: §4, end ("`ind(cP; α; r) = ind(P; α; r)`" for nonzero `c`). -/
theorem index_C_mul {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index (C c * P) α r = index P α r := by
  rw [index, index, map_mul, taylor_C, ← smul_eq_C_mul, support_smul_eq hc]

/-- Source: §4, end ("`ind(P; α; l r) = (1/l) ind(P; α; r)`"). -/
theorem index_mul_left_weights {l : ℕ} (hl : 0 < l) (P : MvPolynomial σ ℝ) (α : σ → ℝ)
    (r : σ → ℕ) : index P α (fun j => l * r j) = index P α r / l := by
  have himg : weight (fun j => l * r j) '' ((taylor α P).support : Set (σ →₀ ℕ)) =
      (l : ℝ)⁻¹ • (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))) := by
    rw [← Set.image_smul, Set.image_image]
    refine Set.image_congr fun d _ => ?_
    rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]
  rw [index, index, himg, Real.sInf_smul_of_nonneg (by positivity), smul_eq_mul, div_eq_inv_mul]

/-- The index is invariant under injective renaming of variables.
Source: §4, Lemma 4-2 and its Lean note ("invariance under ... variable renaming": the index
of a polynomial embedded into a larger set of variables is its index in its own variables). -/
theorem index_rename {τ : Type*} [Fintype τ] [DecidableEq τ] {f : σ → τ}
    (hf : Function.Injective f) (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) :
    index (rename f P) α r = index P (α ∘ f) (r ∘ f) := by
  rw [index, index, taylor_rename, support_rename_of_injective hf, Finset.coe_image,
    Set.image_image]
  refine congrArg sInf (Set.image_congr fun d _ => ?_)
  exact weight_mapDomain hf r d

/-- If `P` has degree at most `r j` in each `x_j`, its index is at most the number of variables.
Source: §5 ("Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, of weight at
most `m`"). -/
theorem index_le_card {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j)
    (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) : index P α r ≤ Fintype.card σ := by
  obtain ⟨d, hd0, hdw⟩ := exists_weight_eq_index hP α r
  exact hdw ▸ weight_le_card fun j =>
    (monomial_le_degreeOf j (mem_support_taylor_iff.2 hd0)).trans
      ((degreeOf_taylor_le α j P).trans (hd j))

/-- In one variable, the index is the multiplicity of `α` as a root divided by the weight.
Source: §5, proof of Lemma 5 ("Let `t` be the multiplicity of `h_1/q_1` as a root of `R`;
Taylor's theorem gives `ind(R; h_1/q_1; r_1) = t/r_1`"). -/
theorem index_unique [Unique σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r =
      (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default := by
  set e := uniqueAlgEquiv ℝ σ
  set q := Polynomial.taylor (α default) (e P) with hqdef
  have hevalQ : ∀ Q : MvPolynomial σ ℝ, (e Q).eval (α default) = eval α Q := fun Q =>
    eval₂_uniqueAlgEquiv (f := Q) (φ := RingHom.id ℝ) (a := α)
  have key : ∀ d : σ →₀ ℕ, eval α (hasseDeriv d P) = q.coeff (d default) := fun d => by
    rw [hqdef, Polynomial.taylor_coeff, ← uniqueAlgEquiv_hasseDeriv, hevalQ,
      ← Finsupp.unique_single d]
  have hq : q ≠ 0 := by
    rwa [hqdef, Ne, Polynomial.taylor_eq_zero, map_eq_zero_iff e e.injective]
  have hw : ∀ d : σ →₀ ℕ, weight r d = (d default : ℝ) / r default := fun d => by
    simp [weight]
  rw [Polynomial.rootMultiplicity_eq_natTrailingDegree, ← Polynomial.taylor_apply]
  apply le_antisymm
  · have hN : q.coeff q.natTrailingDegree ≠ 0 :=
      Polynomial.trailingCoeff_nonzero_iff_nonzero.2 hq
    have h1 := index_le_weight (P := P) (α := α) (r := r)
      (d := Finsupp.single default q.natTrailingDegree) (by rw [key]; simpa using hN)
    rwa [hw, Finsupp.single_eq_same] at h1
  · refine (le_index_iff hP).2 fun d hd => ?_
    rw [key] at hd
    rw [hw]
    exact div_le_div_of_nonneg_right
      (by exact_mod_cast Polynomial.natTrailingDegree_le_of_ne_zero hd) (Nat.cast_nonneg _)

end Roth
