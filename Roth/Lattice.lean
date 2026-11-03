/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Data.Finsupp.Fin

import Roth.Box

/-!
# The lattice count estimate (Lemma 8)

The number of multi-indices `0 ≤ j_i ≤ r_i` with `∑ j_i / r_i ≤ (m - λ)/2` is at most
`2 √m λ⁻¹ ∏ (r_i + 1)`.

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §6 "Lattice count estimate", Lemma 8
(`roth:lem8`) (`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open Finset

/-- If `m ≥ 1` and `λ > 2 √m`, then `√(1 - 1/m) < 1 - λ⁻²`.

Source: §6, proof of Lemma 8 ("`1 - λ⁻² > 1 - 1/(4m) > √(1 - 1/m) > 0`"). -/
theorem sqrt_one_sub_inv_lt {m : ℝ} (hm : 1 ≤ m) {lam : ℝ} (hlam : 2 * √m < lam) :
    √(1 - 1 / m) < 1 - lam⁻¹ ^ 2 := by
  have hm0 : 0 ≤ m := zero_le_one.trans hm
  have hsq : 4 * m < lam ^ 2 := by
    nlinarith [Real.sqrt_nonneg m, Real.sq_sqrt hm0]
  have hu : lam⁻¹ ^ 2 < 1 / m / 4 := by
    rw [inv_pow, div_div, ← one_div]
    exact one_div_lt_one_div_of_lt (by positivity) (by linarith)
  rw [Real.sqrt_lt' (by linarith [one_div_le_one_div_of_le one_pos hm])]
  nlinarith [sq_nonneg (lam⁻¹ ^ 2)]

private lemma inv_add_inv_le_aux {lam x : ℝ} (hlam : 1 < lam) (hx0 : 0 ≤ x) (hx2 : x ≤ 2) :
    (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1) := by
  have ha : 0 < lam - 1 + x := by linarith
  have hb : 0 < lam - 1 + (2 - x) := by linarith
  rw [inv_add_inv ha.ne' hb.ne', div_le_div_iff₀ (mul_pos ha hb) (by nlinarith)]
  nlinarith [mul_nonneg hx0 (sub_nonneg.2 hx2)]

private lemma sum_inv_le_aux {r : ℕ} (hr : 1 ≤ r) {lam : ℝ} (hlam : 1 < lam) :
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ ≤ (r + 1) * (lam / (lam ^ 2 - 1)) := by
  have hr' : (0 : ℝ) < r := by exact_mod_cast hr
  -- pair the terms `j` and `r - j` (`Finset.sum_flip`)
  have h := Finset.sum_le_sum fun j (hj : j ∈ range (r + 1)) ↦ by
    have hjr : j ≤ r := Nat.lt_succ_iff.1 (mem_range.1 hj)
    have hx2 : 2 * (j : ℝ) / r ≤ 2 := (div_le_iff₀ hr').2 (by gcongr)
    simpa only [show 2 - 2 * (j : ℝ) / r = 2 * ((r - j : ℕ) : ℝ) / r by
      rw [Nat.cast_sub hjr]
      field_simp] using inv_add_inv_le_aux hlam (by positivity) hx2
  rw [Finset.sum_add_distrib, Finset.sum_flip (fun j : ℕ ↦ (lam - 1 + 2 * (j : ℝ) / r)⁻¹),
    Finset.sum_const, card_range, nsmul_eq_mul, mul_div_assoc] at h
  push_cast at h
  linarith

/-- The harmonic-type sum `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹` is less than `λ⁻¹ √(m/(m-1)) (r+1)`.

Source: §6, proof of Lemma 8 ("Let `r ≥ 1` and `m ≥ 2` be integers and suppose `λ > 2√m`.
Then `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹ < λ⁻¹ (m-1)^{-1/2} m^{1/2} (r+1)`"). -/
theorem sum_inv_lt {r : ℕ} {m : ℝ} (hr : 1 ≤ r) (hm : 1 < m) {lam : ℝ} (hlam : 2 * √m < lam) :
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√(m - 1))⁻¹ * √m * (r + 1) := by
  have hlam1 : 1 < lam := by linarith [Real.lt_sqrt_of_sq_lt (by linarith : (1 : ℝ) ^ 2 < m)]
  have hpos1 : 0 < √(1 - 1 / m) := by
    rw [Real.sqrt_pos, sub_pos, div_lt_one (by linarith)]
    linarith
  have hsqrt : √(1 - 1 / m) = √(m - 1) / √m := by
    rw [← Real.sqrt_div' _ (by linarith : (0 : ℝ) ≤ m)]
    congr 1
    field_simp
  have hlam' : lam / (lam ^ 2 - 1) = lam⁻¹ / (1 - lam⁻¹ ^ 2) := by
    have : lam ≠ 0 := by linarith
    field_simp
  calc _ ≤ (r + 1) * (lam / (lam ^ 2 - 1)) := sum_inv_le_aux hr hlam1
    _ < (r + 1) * (lam⁻¹ / √(1 - 1 / m)) := by
      rw [hlam']
      gcongr
      exact sqrt_one_sub_inv_lt hm.le hlam
    _ = _ := by
      rw [hsqrt]
      field_simp

/-- The weight of `Finsupp.cons i d` is `i / r 0` plus the weight of `d` relative to the remaining
parameters. -/
theorem weight_cons {m : ℕ} (r : Fin (m + 1) → ℕ) (i : ℕ) (d : Fin m →₀ ℕ) :
    weight r (Finsupp.cons i d) = i / r 0 + weight (r ∘ Fin.succ) d := by
  simp [weight, Fin.sum_univ_succ]

private lemma card_filter_box_fiber_aux {m : ℕ} (r : Fin (m + 1) → ℕ)
    (p : (Fin (m + 1) →₀ ℕ) → Prop) [DecidablePred p] {i : ℕ} (hi : i ≤ r 0) :
    ((box (r ∘ Fin.succ)).filter fun d ↦ p (Finsupp.cons i d)).card =
      (((box r).filter p).filter fun d ↦ d 0 = i).card := by
  -- `Finsupp.cons i` and `Finsupp.tail` are inverse bijections between the two filtered boxes
  refine Finset.card_bij' (fun d _ ↦ Finsupp.cons i d) (fun d _ ↦ Finsupp.tail d) ?_ ?_ ?_ ?_
  · -- `cons i d` lies in the box with first coordinate `i`
    intro d hd
    simp only [Finset.mem_filter, mem_box, Function.comp_apply] at hd ⊢
    refine ⟨⟨fun j ↦ ?_, hd.2⟩, Finsupp.cons_zero i d⟩
    exact Fin.cases (by simpa using hi) (fun j ↦ by simpa using hd.1 j) j
  · -- `tail d` lies in the smaller box
    intro d hd
    simp only [Finset.mem_filter, mem_box, Function.comp_apply] at hd ⊢
    obtain ⟨⟨hdr, hdp⟩, hdi⟩ := hd
    refine ⟨fun j ↦ by simpa [Finsupp.tail_apply] using hdr j.succ, ?_⟩
    rwa [← hdi, Finsupp.cons_tail]
  · intro d _
    exact Finsupp.tail_cons i d
  · intro d hd
    rw [← (Finset.mem_filter.1 hd).2]
    exact Finsupp.cons_tail d

/-- Counting a filtered box by fibres over the first coordinate: each fibre is identified with
the box in the remaining `m` coordinates, filtered by the extended predicate.

Source: §6, Lean implementation note (the induction counts the fibres of a coordinate
projection). -/
theorem card_filter_box_zero {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
    [DecidablePred p] : ((box r).filter p).card =
      ∑ i ∈ range (r 0 + 1), ((box (r ∘ Fin.succ)).filter fun d ↦ p (Finsupp.cons i d)).card := by
  rw [Finset.card_eq_sum_card_fiberwise (f := fun d ↦ d 0) (t := range (r 0 + 1)) fun d hd ↦ by
      simp only [Finset.coe_filter, Set.mem_ofPred_eq, mem_box] at hd
      simpa [Nat.lt_succ_iff] using hd.1 0]
  exact Finset.sum_congr rfl fun i hi ↦
    (card_filter_box_fiber_aux r p (Nat.lt_succ_iff.1 (mem_range.1 hi))).symm

private lemma filter_weight_le_eq_empty_aux {m : ℕ} (r : Fin m → ℕ) {lam : ℝ}
    (hlam : (m : ℝ) < lam) :
    (box r).filter (fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2) = ∅ :=
  Finset.filter_eq_empty_iff.2 fun d _ h ↦ by linarith [weight_nonneg r d]

private lemma card_filter_fiber_eq_aux {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ) :
    (((box (r ∘ Fin.succ)).filter fun d ↦
      weight r (Finsupp.cons i d) ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) =
      (((box (r ∘ Fin.succ)).filter fun d ↦ weight (r ∘ Fin.succ) d ≤
        ((n : ℝ) - (lam - 1 + 2 * (i : ℝ) / r 0)) / 2).card : ℝ) := by
  congr 2
  refine Finset.filter_congr fun d _ ↦ ?_
  rw [weight_cons, mul_div_assoc]
  grind

private lemma card_filter_weight_le_of_le_sqrt_aux {m : ℕ} (r : Fin m → ℕ) {lam : ℝ}
    (hlam : 0 < lam) (h : lam ≤ 2 * √(m : ℝ)) : (((box r).filter fun d ↦
      weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by
  calc _ ≤ ((box r).card : ℝ) := by exact_mod_cast Finset.card_filter_le (box r) _
    _ = ∏ j, ((r j : ℝ) + 1) := by simp [card_box]
    _ ≤ _ := le_mul_of_one_le_left (by positivity) ((one_le_div hlam).2 h)

private lemma card_filter_weight_le_succ_aux {n : ℕ} (r : Fin (n + 1) → ℕ) (hr : 0 < r 0)
    (hn : 0 < n) {lam : ℝ} (hlam : 2 * √((n + 1 : ℕ) : ℝ) < lam) (ih : ∀ {t : ℝ}, 0 < t →
      (((box (r ∘ Fin.succ)).filter fun d ↦ weight (r ∘ Fin.succ) d ≤
        ((n : ℝ) - t) / 2).card : ℝ) ≤ 2 * √(n : ℝ) / t * ∏ j, (((r ∘ Fin.succ) j : ℝ) + 1)) :
    (((box r).filter fun d ↦ weight r d ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) ≤
      2 * √((n + 1 : ℕ) : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by
  set R := r 0
  have hs := sum_inv_lt (r := R) (m := ((n + 1 : ℕ) : ℝ)) hr
    (by exact_mod_cast Nat.succ_lt_succ hn) hlam
  push_cast [add_sub_cancel_right] at hs
  -- count fibrewise over the first coordinate: the fibre over `i` is the `n`-dimensional count
  -- with `λ' = λ - 1 + 2 i / r_0`
  rw [card_filter_box_zero, Nat.cast_sum,
    Finset.sum_congr rfl fun i _ ↦ card_filter_fiber_eq_aux r lam i]
  calc ∑ i ∈ range (R + 1), (((box (r ∘ Fin.succ)).filter fun d ↦
          weight (r ∘ Fin.succ) d ≤ ((n : ℝ) - (lam - 1 + 2 * (i : ℝ) / R)) / 2).card : ℝ)
      ≤ ∑ i ∈ range (R + 1), 2 * √(n : ℝ) / (lam - 1 + 2 * (i : ℝ) / R) *
          ∏ j, (((r ∘ Fin.succ) j : ℝ) + 1) := by
        -- the induction hypothesis on each fibre (`λ' > 0` since `λ > 2 √(n + 1) ≥ 2`)
        refine Finset.sum_le_sum fun i _ ↦ ih ?_
        linarith [Real.one_le_sqrt.2 (by simp : (1 : ℝ) ≤ ((n + 1 : ℕ) : ℝ)),
          show 0 ≤ 2 * (i : ℝ) / R by positivity]
    _ = 2 * √(n : ℝ) * (∏ j, (((r ∘ Fin.succ) j : ℝ) + 1)) *
          ∑ i ∈ range (R + 1), (lam - 1 + 2 * (i : ℝ) / R)⁻¹ := by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun i _ ↦ by ring
    _ ≤ 2 * √(n : ℝ) * (∏ j, (((r ∘ Fin.succ) j : ℝ) + 1)) *
          (lam⁻¹ * (√(n : ℝ))⁻¹ * √((n : ℝ) + 1) * (R + 1)) :=
        mul_le_mul_of_nonneg_left hs.le (by positivity)
    _ = 2 * √((n + 1 : ℕ) : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by
        -- reassemble `∏_{j ≤ n} (r_j + 1) = (r_0 + 1) ∏_{j < n} (r_{j+1} + 1)`
        rw [Fin.prod_univ_succ]
        push_cast
        field_simp
        simp only [R, Function.comp_apply]
        ring

/-- **Lemma 8** (lattice count estimate): the number of multi-indices in the box `∏ [0, r_j]`
of weight at most `(m - λ)/2` is at most `2 √m λ⁻¹ ∏ (r_j + 1)`.

Source: §6, Lemma `roth:lem8` ("the number of `m`-tuples ... `∑ j_i/r_i ≤ (m-λ)/2`
does not exceed `2 m^{1/2} λ^{-1} (r_1 + 1) ⋯ (r_m + 1)`"). -/
theorem card_filter_weight_le_le {m : ℕ} (r : Fin m → ℕ) (hr : ∀ j, 0 < r j) {lam : ℝ}
    (hlam : 0 < lam) :
    (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤
      2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by
  induction m generalizing lam with
  | zero =>
    rw [filter_weight_le_eq_empty_aux r (by simpa using hlam)]
    simp
  | succ n ih =>
    by_cases h : lam ≤ 2 * √(((n + 1 : ℕ) : ℝ))
    · exact card_filter_weight_le_of_le_sqrt_aux r hlam h
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · rw [filter_weight_le_eq_empty_aux r (by
        norm_num at h ⊢
        linarith), card_empty, Nat.cast_zero]
      positivity
    exact card_filter_weight_le_succ_aux r (hr _) hn (lt_of_not_ge h) (ih _ fun j ↦ hr _)

end Roth
