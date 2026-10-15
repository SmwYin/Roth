import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Finsupp.Interval
import Mathlib.Data.Finsupp.Weight
import Mathlib.Data.Fintype.Pi
import Mathlib.Tactic.Positivity

/-!
# Boxes of multi-indices and real weights

This file sets up the two pieces of bookkeeping on multi-indices `d : σ →₀ ℕ` used throughout
the proof of Roth's theorem: the box of multi-indices bounded by a vector `r`, and the real
weight of a multi-index with respect to `r`.

## Main definitions

* `Roth.box r`: the finite set of multi-indices `d : σ →₀ ℕ` with `d j ≤ r j` for all `j`.
* `Roth.weight r d`: the real weight `∑ j, d j / r j` of a multi-index with respect to the
  parameters `r j`; the *index* of a polynomial (`Roth.index`) is the least weight of a
  nonvanishing Taylor coefficient.

## Main results

* `Roth.card_box`: the box `box r` has `∏ j, (r j + 1)` elements.
* `Roth.weight_eq_zero_iff`: for positive `r`, a multi-index has weight zero iff it is zero.
* `Roth.weight_le_card`: a multi-index in the box `box r` has weight at most `card σ`.
* `Roth.weight_mapDomain`: weights are unchanged by an injective change of variables.

## References

* Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §4 (definition of the index) and §6
  (Lemma 8), `.mathlib-quality/references/clean.tex`.
-/

namespace Roth

variable {σ : Type*} [Fintype σ] [DecidableEq σ]

/-- The box `{d | ∀ j, d j ≤ r j}` of multi-indices, as a `Finset`.
Source: §6, Lemma 8 ("`0 ≤ j_1 ≤ r_1, …, 0 ≤ j_m ≤ r_m`"). -/
noncomputable def box (r : σ → ℕ) : Finset (σ →₀ ℕ) :=
  (Fintype.piFinset fun j ↦ Finset.range (r j + 1)).map Finsupp.equivFunOnFinite.symm.toEmbedding

/-- Membership in `box r` is the coordinatewise bound `d j ≤ r j`. Source: §6, Lemma 8. -/
theorem mem_box {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ box r ↔ ∀ j, d j ≤ r j := by
  simp [box, Nat.lt_succ_iff]

/-- The box `box r` has `∏ j, (r j + 1)` elements.
Source: §6, Lemma 9, equation (43) (`r = (r_1 + 1) ⋯ (r_m + 1)`), and §6, Lemma 8 ("the
latter is equal to the number of solutions ... `0 ≤ j_1 ≤ r_1, …`"). -/
theorem card_box (r : σ → ℕ) : (box r).card = ∏ j, (r j + 1) := by
  simp [box]

omit [DecidableEq σ] in
/-- A finset of multi-indices bounded coordinatewise by `r` has at most `∏ j, (r j + 1)`
elements, since it is contained in `box r`.
Source: §3, proof of Lemma 3 ("Pad the monomial expansion of `R` by zero terms ... `N`"). -/
theorem card_le_card_box {r : σ → ℕ} {s : Finset (σ →₀ ℕ)} (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) :
    s.card ≤ ∏ j, (r j + 1) := by
  classical
  exact (Finset.card_le_card fun d hd ↦ mem_box.2 (hs d hd)).trans_eq (card_box r)

/-- The weight `∑ j, d j / r j` of a multi-index. Source: §4, definition of the index. -/
noncomputable def weight (r : σ → ℕ) (d : σ →₀ ℕ) : ℝ := ∑ j, (d j : ℝ) / r j

omit [DecidableEq σ] in
/-- Weights are nonnegative.
Source: §4, proof of the lemma `index ≥ 0` ("Every weight `∑ i_j / r_j` is nonnegative"). -/
theorem weight_nonneg (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ weight r d :=
  Fintype.sum_nonneg fun _ ↦ by positivity

omit [DecidableEq σ] in
/-- The zero multi-index has weight zero. -/
@[simp]
theorem weight_zero (r : σ → ℕ) : weight r 0 = 0 := by
  simp [weight]

/-- The weight is additive in the multi-index.
Source: §4, proof of Lemma `index-of-derivative` (`∑ (i_j + k_j)/r_j = … + ∑ k_j/r_j`). -/
theorem weight_add (r : σ → ℕ) (d e : σ →₀ ℕ) : weight r (d + e) = weight r d + weight r e := by
  simp [weight, add_div, Finset.sum_add_distrib]

/-- For positive parameters `r`, only the zero multi-index has weight zero.
Source: §4, proof of the lemma `index = 0 ↔ P(α) ≠ 0` ("Since each `r_j > 0`, such a weight
is zero exactly when every `i_j = 0`"). -/
theorem weight_eq_zero_iff {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} :
    weight r d = 0 ↔ d = 0 := by
  simp [weight, Finset.sum_eq_zero_iff_of_nonneg, div_nonneg, (hr _).ne', Finsupp.ext_iff]

/-- The weight of the single multi-index `n • e_j` is `n / r j`. -/
theorem weight_single (r : σ → ℕ) (j : σ) (n : ℕ) :
    weight r (Finsupp.single j n) = n / r j := by
  simp [weight, Finsupp.single_apply, ite_div]

/-- A multi-index in the box `box r` has weight at most the number of variables.
Source: §5 ("Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, of weight at
most `m`"). -/
theorem weight_le_card {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) :
    weight r d ≤ Fintype.card σ :=
  (Finset.sum_le_sum fun j _ => div_le_one_of_le₀ (by exact_mod_cast hd j) (by positivity)).trans_eq
    (by simp)

/-- Scaling all parameters by `l` divides the weight by `l`.
Source: §4, end ("`ind(P; α; l r) = (1/l) ind(P; α; r)`"). -/
theorem weight_mul_left {l : ℕ} (hl : 0 < l) (r : σ → ℕ) (d : σ →₀ ℕ) :
    weight (fun j => l * r j) d = weight r d / l := by
  simp [weight, Finset.sum_div, div_div, mul_comm]

/-- If every parameter is at least `m`, a multi-index of total degree `w` has weight at most
`w / m`.
Source: §5, proof of Lemma 6 ("`∑_{j<p} i_j / r_j ≤ w / r_{p-1}`": a multi-index of total
degree `w` has weight at most `w / min r`). -/
theorem weight_le_degree_div {r : σ → ℕ} {m : ℕ} (hm : 0 < m) (hr : ∀ j, m ≤ r j)
    (d : σ →₀ ℕ) : weight r d ≤ d.degree / m := by
  rw [Finsupp.degree_eq_sum, Nat.cast_sum, Finset.sum_div]
  exact Finset.sum_le_sum fun j _ =>
    div_le_div_of_nonneg_left (by positivity) (by exact_mod_cast hm) (by exact_mod_cast hr j)

/-- Weights are invariant under an injective change of variables `f : σ → τ`.
Source: §4, Lemma 4-2 (embedding a polynomial in fewer variables does not change the weights
of its monomials). -/
theorem weight_mapDomain {τ : Type*} [Fintype τ] [DecidableEq τ] {f : σ → τ}
    (hf : Function.Injective f) (r : τ → ℕ) (d : σ →₀ ℕ) :
    weight r (d.mapDomain f) = weight (r ∘ f) d := by
  refine (Fintype.sum_of_injective f hf _ _ (fun i hi => ?_) fun i => ?_).symm
  · simp [Finsupp.mapDomain_of_notMem_range _ _ hi]
  · simp [Finsupp.mapDomain_apply_of_injective hf]

end Roth
