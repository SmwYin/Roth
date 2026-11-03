/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Algebra.Polynomial.RingDivision
import Mathlib.Algebra.Polynomial.Taylor
import Mathlib.Basic.Real.Pointwise
import Mathlib.Data.ENat.BigOperators
import Mathlib.Data.Nat.Cast.Field
import Mathlib.Order.ConditionallyCompleteLattice.Finset
import Mathlib.RingTheory.MvPowerSeries.NoZeroDivisors

import Roth.Box
import Roth.Taylor

/-!
# The index of a polynomial

The *index* of a nonzero polynomial `P` over a commutative ring at a point `α` relative to
positive integers `r j` is the minimum of `∑ j, d j / r j` over all multi-indices `d` with
`(Δ_d P)(α) ≠ 0`, i.e. over the support of the translate `P(X + α)`.  By convention
`index 0 α r = 0` (the source uses `+∞` for the zero polynomial; every lemma below carries explicit
nonvanishing hypotheses instead, which is how the convention is used in the source).

## Main definitions

* `Roth.index P α r`: the index of `P` at `α` relative to the weights `r`.

## Main results

* `Roth.le_index_iff`: lower bounds for the index of a nonzero polynomial.
* `Roth.index_sub_weight_le_index_hasseDeriv`: differentiating lowers the index by at most
  the weight.
* `Roth.le_index_sum`, `Roth.index_mul`, `Roth.index_prod`: the index of sums and products.
* `Roth.index_eq_weightedOrder_div`: the index as a weighted order of a power series.
* `Roth.index_rename`, `Roth.index_eq_rootMultiplicity_div`: the index under renaming and in
  one variable.

## References

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §4 "Index" (definition of the index,
the lemmas `index ≥ 0`, `index-of-derivative`, Lemma 4-1, Lemma 4-2 and the scaling identities)
(`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open MvPolynomial
open scoped Pointwise

variable {σ : Type*} [Fintype σ] {R : Type*} [CommRing R]

/-- The index of `P` at `α` relative to `r`. Source: §4, definition of the index and the Lean
implementation note ("Define the index as the minimum of `∑ d_j/r_j` over its nonzero
coefficients"). -/
noncomputable def index (P : MvPolynomial σ R) (α : σ → R) (r : σ → ℕ) : ℝ :=
  sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))

/-- The index of the zero polynomial is `0`, by convention. -/
@[simp]
theorem index_zero (α : σ → R) (r : σ → ℕ) : index 0 α r = 0 := by
  simp [index]

/-- The index is at most the weight of any multi-index `d` with `(Δ_d P)(α) ≠ 0`.
Source: §4, definition of the index ("the minimum ... over all tuples `(i_1, …, i_p)` such
that `Δ_i P(α) ≠ 0`"). -/
theorem index_le_weight {P : MvPolynomial σ R} {α : σ → R} (r : σ → ℕ) {d : σ →₀ ℕ}
    (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d :=
  csInf_le ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
    (Set.mem_image_of_mem _ (Finset.mem_coe.2 (mem_support_taylor.2 h)))

/-- For nonzero `P`, the index is attained by some multi-index `d` with `(Δ_d P)(α) ≠ 0`.
Source: §4, definition of the index ("Thus this is an attained minimum"). -/
theorem exists_weight_eq_index {P : MvPolynomial σ R} (hP : P ≠ 0) (α : σ → R) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by
  obtain ⟨d, hd, hdw⟩ :=
    (show (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))).Nonempty by
      simpa using hP).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))
  exact ⟨d, mem_support_taylor.1 hd, hdw⟩

/-- The characterisation of lower bounds for the index of a nonzero polynomial: `c ≤ index P α r`
iff every multi-index `d` with `(Δ_d P)(α) ≠ 0` has weight at least `c`. -/
theorem le_index_iff {P : MvPolynomial σ R} (hP : P ≠ 0) {α : σ → R} {r : σ → ℕ} {c : ℝ} :
    c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by
  refine ⟨fun h d hd ↦ h.trans (index_le_weight r hd), fun h ↦ ?_⟩
  refine le_csInf (by simpa using hP) ?_
  rintro _ ⟨d, hd, rfl⟩
  exact h d (mem_support_taylor.1 hd)

/-- The index is nonnegative. Source: §4, first lemma on the index ("We have `ind(P) ≥ 0`"). -/
theorem index_nonneg (P : MvPolynomial σ R) (α : σ → R) (r : σ → ℕ) : 0 ≤ index P α r :=
  Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)

/-- Applying `Δ_k` lowers the index by at most the weight of `k`.
Source: §4, Lemma `lem:index-of-derivative` ("`ind(Δ_k P) ≥ ind(P) - ∑ k_j / r_j`"). -/
theorem index_sub_weight_le_index_hasseDeriv {P : MvPolynomial σ R} {k : σ →₀ ℕ}
    (hk : hasseDeriv k P ≠ 0) (α : σ → R) (r : σ → ℕ) :
    index P α r - weight r k ≤ index (hasseDeriv k P) α r := by
  obtain ⟨i, hi, hiw⟩ := exists_weight_eq_index hk α r
  rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, map_mul, eval_C] at hi
  exact sub_le_iff_le_add.2
    (by simpa [weight_add, hiw] using index_le_weight r (right_ne_zero_of_mul hi))

/-- A common lower bound for the indices of the nonzero summands is a lower bound for the index
of a nonzero sum.
Source: §4, Lemma 4-1 ("`ind(P + Q) ≥ min(ind P, ind Q)`"), in the form used in the proof of
Lemma 6. -/
theorem le_index_sum {ι : Type*} {s : Finset ι} {f : ι → MvPolynomial σ R} {α : σ → R} {r : σ → ℕ}
    (hs : ∑ i ∈ s, f i ≠ 0) {c : ℝ} (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) :
    c ≤ index (∑ i ∈ s, f i) α r := by
  refine (le_index_iff hs).2 fun d hd ↦ ?_
  rw [map_sum, map_sum] at hd
  obtain ⟨i, hi, hid⟩ := Finset.exists_ne_zero_of_sum_ne_zero hd
  have hfi : f i ≠ 0 := fun h0 ↦ hid (by rw [h0, map_zero, map_zero])
  exact (le_index_iff hfi).1 (hf i hi hfi) d hid

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
theorem index_eq_weightedOrder_div (P : MvPolynomial σ R) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (α : σ → R) : index P α r =
      (((taylor α P : MvPowerSeries σ R).weightedOrder fun j ↦ (∏ i, r i) / r j).toNat : ℝ) /
        ∏ i, r i := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp
  set w : σ → ℕ := fun j ↦ (∏ i, r i) / r j
  set F : MvPowerSeries σ R := ↑(taylor α P)
  obtain ⟨d, hd, hdw⟩ := MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder w (f := F)
    ((MvPowerSeries.ne_zero_iff_weightedOrder_finite w).1 (by simpa [F] using hP))
  apply le_antisymm
  · rw [← hdw, ENat.toNat_natCast, ← weight_eq_finsuppWeight_div hr]
    exact index_le_weight r (by simpa [F, MvPolynomial.coeff_coe, coeff_taylor] using hd)
  · refine (le_index_iff hP).2 fun e he ↦ ?_
    rw [weight_eq_finsuppWeight_div hr]
    refine div_le_div_of_nonneg_right ?_ (Nat.cast_nonneg _)
    exact_mod_cast ENat.toNat_le_toNat (MvPowerSeries.weightedOrder_le w (f := F) (d := e)
      (by simpa [F, MvPolynomial.coeff_coe, coeff_taylor] using he)) (by simp)

/-- The index is additive on products of nonzero polynomials.
Source: §4, Lemma 4-1 ("`ind(P Q) = ind(P) + ind(Q)`"). -/
theorem index_mul [NoZeroDivisors R] {P Q : MvPolynomial σ R} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → R)
    {r : σ → ℕ} (hr : ∀ j, 0 < r j) : index (P * Q) α r = index P α r + index Q α r := by
  rw [index_eq_weightedOrder_div P hr, index_eq_weightedOrder_div Q hr,
    index_eq_weightedOrder_div (P * Q) hr, ← add_div, map_mul, MvPolynomial.coe_mul,
    MvPowerSeries.weightedOrder_mul]
  congr 1
  have hfin : ∀ S : MvPolynomial σ R, S ≠ 0 →
      ((taylor α S : MvPowerSeries σ R).weightedOrder fun j ↦ (∏ i, r i) / r j) ≠ ⊤ := by simp
  rw [ENat.toNat_add (hfin P hP) (hfin Q hQ), Nat.cast_add]

/-- The index is additive on finite products of nonzero polynomials.
Source: §4, Lemma 4-1, iterated ("`ind ∏_ν ... = ∑_ν ind ...`", as used in the proof of
Lemma 6). -/
theorem index_prod [IsDomain R] {ι : Type*} (s : Finset ι) {f : ι → MvPolynomial σ R}
    (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → R) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r := by
  rw [index_eq_weightedOrder_div _ hr, map_prod,
    ← MvPolynomial.coeToMvPowerSeries.ringHom_apply, map_prod, MvPowerSeries.weightedOrder_prod,
    ENat.toNat_sum fun i hi ↦ by simp [hf i hi], Nat.cast_sum, Finset.sum_div]
  exact Finset.sum_congr rfl fun i hi ↦ (index_eq_weightedOrder_div _ hr α).symm

/-- Multiplying by a nonzero constant does not change the index.
Source: §4, end ("`ind(cP; α; r) = ind(P; α; r)`" for nonzero `c`). -/
theorem index_C_mul [IsDomain R] {c : R} (hc : c ≠ 0) (P : MvPolynomial σ R) (α : σ → R)
    (r : σ → ℕ) : index (C c * P) α r = index P α r := by
  rw [index, index, map_mul, taylor_C, ← smul_eq_C_mul, support_smul_eq hc]

/-- Scaling all weights by `l` divides the index by `l`.
Source: §4, end ("`ind(P; α; l r) = (1/l) ind(P; α; r)`"). -/
theorem index_mul_left_weights (l : ℕ) (P : MvPolynomial σ R) (α : σ → R) (r : σ → ℕ) :
    index P α (fun j ↦ l * r j) = index P α r / l := by
  have himg : weight (fun j ↦ l * r j) '' ((taylor α P).support : Set (σ →₀ ℕ)) =
      (l : ℝ)⁻¹ • (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))) := by
    rw [← Set.image_smul, Set.image_image]
    refine Set.image_congr fun d _ ↦ ?_
    rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]
  rw [index, index, himg, Real.sInf_smul_of_nonneg (by positivity), smul_eq_mul, div_eq_inv_mul]

/-- The index is invariant under injective renaming of variables.
Source: §4, Lemma 4-2 and its Lean note ("invariance under ... variable renaming": the index
of a polynomial embedded into a larger set of variables is its index in its own variables). -/
theorem index_rename {τ : Type*} [Fintype τ] {f : σ → τ} (hf : Function.Injective f)
    (P : MvPolynomial σ R) (α : τ → R) (r : τ → ℕ) :
    index (rename f P) α r = index P (α ∘ f) (r ∘ f) := by
  classical
  simp [index, taylor_rename, support_rename_of_injective hf, Set.image_image, weight_mapDomain]

/-- If `P` has degree at most `r j` in each `x_j`, its index is at most the number of variables.
Source: §5 ("Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, of weight at
most `m`"). -/
theorem index_le_card {P : MvPolynomial σ R} {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j)
    (α : σ → R) : index P α r ≤ Fintype.card σ := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp
  obtain ⟨d, hd0, hdw⟩ := exists_weight_eq_index hP α r
  exact hdw ▸ weight_le_card fun j ↦
    (monomial_le_degreeOf j (mem_support_taylor.2 hd0)).trans
      ((degreeOf_taylor_le α j P).trans (hd j))

/-- In one variable, the index is the multiplicity of `α` as a root divided by the weight.
Source: §5, proof of Lemma 5 ("Let `t` be the multiplicity of `h_1/q_1` as a root of `R`;
Taylor's theorem gives `ind(R; h_1/q_1; r_1) = t/r_1`"). -/
theorem index_eq_rootMultiplicity_div [Unique σ] (P : MvPolynomial σ R) (α : σ → R) (r : σ → ℕ) :
    index P α r =
      (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv R σ P) : ℝ) / r default := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp
  set q := Polynomial.taylor (α default) (uniqueAlgEquiv R σ P) with hqdef
  have key (d : σ →₀ ℕ) : eval α (hasseDeriv d P) = q.coeff (d default) := by
    rw [Polynomial.taylor_coeff, ← uniqueAlgEquiv_hasseDeriv]
    exact (eval₂_uniqueAlgEquiv (f := hasseDeriv d P) (φ := RingHom.id R) (a := α)).symm
  have hq : q ≠ 0 := by
    rwa [hqdef, Ne, Polynomial.taylor_eq_zero, map_eq_zero_iff _ (uniqueAlgEquiv R σ).injective]
  rw [Polynomial.rootMultiplicity_eq_natTrailingDegree, ← Polynomial.taylor_apply]
  apply le_antisymm
  · simpa [weight, hqdef] using index_le_weight (P := P) (α := α) r
      (d := Finsupp.single default q.natTrailingDegree)
      (by simpa [key] using Polynomial.trailingCoeff_nonzero_iff_nonzero.2 hq)
  · refine (le_index_iff hP).2 fun d hd ↦ ?_
    simpa [weight, hqdef] using div_le_div_of_nonneg_right
      (by exact_mod_cast Polynomial.natTrailingDegree_le_of_ne_zero (key d ▸ hd))
      (Nat.cast_nonneg (r default))

end Roth
