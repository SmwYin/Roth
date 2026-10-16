import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt

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

/-- If `m ≥ 2` and `λ > 2 √m`, then `√(1 - 1/m) < 1 - λ⁻²`.

Source: §6, proof of Lemma 8 ("`1 - λ⁻² > 1 - 1/(4m) > √(1 - 1/m) > 0`"). -/
theorem sqrt_one_sub_inv_lt {m : ℕ} (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2 := by
  have hm' : (2 : ℝ) ≤ m := by exact_mod_cast hm
  have hsq : 4 * (m : ℝ) < lam ^ 2 := by
    nlinarith [Real.sqrt_nonneg (m : ℝ), Real.sq_sqrt (Nat.cast_nonneg m)]
  have hu : lam⁻¹ ^ 2 < 1 / m / 4 := by
    rw [inv_pow, div_div, ← one_div]
    exact one_div_lt_one_div_of_lt (by positivity) (by linarith)
  rw [Real.sqrt_lt' (by linarith [one_div_le_one_div_of_le two_pos hm'])]
  nlinarith [sq_nonneg (lam⁻¹ ^ 2)]

private lemma inv_add_inv_le {lam x : ℝ} (hlam : 2 < lam) (hx0 : 0 ≤ x) (hx2 : x ≤ 2) :
    (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1) := by
  have ha : 0 < lam - 1 + x := by linarith
  have hb : 0 < lam - 1 + (2 - x) := by linarith
  rw [inv_add_inv ha.ne' hb.ne', div_le_div_iff₀ (mul_pos ha hb) (by nlinarith)]
  nlinarith [mul_nonneg hx0 (sub_nonneg.2 hx2)]

private lemma sum_inv_le {r : ℕ} (hr : 1 ≤ r) {lam : ℝ} (hlam : 2 < lam) :
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ ≤ (r + 1) * (lam / (lam ^ 2 - 1)) := by
  have hr' : (0 : ℝ) < r := by exact_mod_cast hr
  have h := Finset.sum_le_sum fun j (hj : j ∈ range (r + 1)) ↦ by
    have hjr : j ≤ r := Nat.lt_succ_iff.1 (mem_range.1 hj)
    have hx2 : 2 * (j : ℝ) / r ≤ 2 := by
      rw [div_le_iff₀ hr']
      gcongr
    simpa only [show 2 - 2 * (j : ℝ) / r = 2 * ((r + 1 - 1 - j : ℕ) : ℝ) / r by
      rw [Nat.add_sub_cancel, Nat.cast_sub hjr]
      field_simp] using inv_add_inv_le hlam (by positivity) hx2
  rw [Finset.sum_add_distrib, Finset.sum_range_reflect (fun j : ℕ ↦ (lam - 1 + 2 * (j : ℝ) / r)⁻¹),
    Finset.sum_const, card_range, nsmul_eq_mul, mul_div_assoc] at h
  push_cast at h
  linarith

/-- The harmonic-type sum `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹` is less than `λ⁻¹ √(m/(m-1)) (r+1)`,
by pairing the terms `j` and `r - j`.

Source: §6, proof of Lemma 8 ("Let `r ≥ 1` and `m ≥ 2` be integers and suppose `λ > 2√m`.
Then `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹ < λ⁻¹ (m-1)^{-1/2} m^{1/2} (r+1)`"). -/
theorem sum_inv_lt {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1) := by
  have hm' : (2 : ℝ) ≤ m := by exact_mod_cast hm
  have hlam2 : 2 < lam := by linarith [Real.lt_sqrt_of_sq_lt (by linarith : (1 : ℝ) ^ 2 < m)]
  have hpos1 : 0 < √(1 - 1 / (m : ℝ)) := by
    rw [Real.sqrt_pos, sub_pos, div_lt_one (by linarith)]
    linarith
  have hsqrt : √(1 - 1 / (m : ℝ)) = √((m : ℝ) - 1) / √(m : ℝ) := by
    rw [← Real.sqrt_div' _ (Nat.cast_nonneg m)]
    congr 1
    field_simp
  have hlam' : lam / (lam ^ 2 - 1) = lam⁻¹ / (1 - lam⁻¹ ^ 2) := by
    have : lam ≠ 0 := by linarith
    field_simp
  calc _ ≤ (r + 1) * (lam / (lam ^ 2 - 1)) := sum_inv_le hr hlam2
    _ < (r + 1) * (lam⁻¹ / √(1 - 1 / (m : ℝ))) := by
      rw [hlam']
      gcongr
      exact sqrt_one_sub_inv_lt hm hlam
    _ = _ := by
      rw [hsqrt]
      field_simp

private lemma extend_apply_castSucc {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) (j : Fin m) :
    (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) j.castSucc = d j := by
  simp [Finsupp.mapDomain_apply_of_injective (Fin.castSucc_injective m)]

private lemma extend_apply_last {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) :
    (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) (Fin.last m) = i := by
  simp [Finsupp.mapDomain_of_notMem_range]

private lemma card_filter_box_fiber_aux {m : ℕ} (r : Fin (m + 1) → ℕ)
    (p : (Fin (m + 1) →₀ ℕ) → Prop) [DecidablePred p] {i : ℕ} (hi : i ≤ r (Fin.last m)) :
    ((box (r ∘ Fin.castSucc)).filter fun d ↦
      p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card =
        (((box r).filter p).filter fun d ↦ d (Fin.last m) = i).card := by
  classical
  refine Finset.card_bij
    (fun d _ ↦ d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) ?_ ?_ ?_
  · intro d hd
    simp only [Finset.mem_filter, mem_box, Function.comp_apply] at hd ⊢
    refine ⟨⟨fun j ↦ ?_, hd.2⟩, extend_apply_last d i⟩
    exact Fin.lastCases (by simpa [extend_apply_last] using hi)
      (fun j ↦ by simpa [extend_apply_castSucc] using hd.1 j) j
  · intro d₁ _ d₂ _ h
    ext j
    simpa [extend_apply_castSucc] using congrArg (fun d ↦ d j.castSucc) h
  · intro d hd
    obtain ⟨⟨hdr, hdp⟩, hdi⟩ := (by simpa [mem_box] using hd)
    have hext : (Finsupp.equivFunOnFinite.symm fun j ↦ d j.castSucc).mapDomain Fin.castSucc +
        Finsupp.single (Fin.last m) i = d := by
      ext j
      refine Fin.lastCases ?_ (fun j ↦ ?_) j <;>
        simp [extend_apply_last, extend_apply_castSucc, hdi]
    refine ⟨Finsupp.equivFunOnFinite.symm fun j ↦ d j.castSucc, ?_, hext⟩
    simp [mem_box, hext, hdp, hdr]

/-- Counting a filtered box by fibres over the last coordinate: each fibre is identified with
the box in the first `m` coordinates, filtered by the extended predicate.

Source: §6, Lean implementation note ("induction counts the fibres of the last-coordinate
projection"). -/
theorem card_filter_box_last {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
    [DecidablePred p] : ((box r).filter p).card = ∑ i ∈ range (r (Fin.last m) + 1),
      ((box (r ∘ Fin.castSucc)).filter fun d ↦
        p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card := by
  classical
  rw [Finset.card_eq_sum_card_fiberwise (f := fun d ↦ d (Fin.last m))
    (t := range (r (Fin.last m) + 1)) fun d hd ↦ by
      simp only [Finset.coe_filter, Set.mem_ofPred_eq, mem_box] at hd
      simpa [Nat.lt_succ_iff] using hd.1 (Fin.last m)]
  exact Finset.sum_congr rfl fun i hi ↦
    (card_filter_box_fiber_aux r p (Nat.lt_succ_iff.1 (mem_range.1 hi))).symm

private lemma filter_weight_le_eq_empty {m : ℕ} (r : Fin m → ℕ) {lam : ℝ} (hlam : (m : ℝ) < lam) :
    (box r).filter (fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2) = ∅ :=
  Finset.filter_eq_empty_iff.2 fun d _ h ↦ by linarith [weight_nonneg r d]

private lemma card_filter_fiber_eq {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ) :
    (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight r
      (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last n) i) ≤
        (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) =
      (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight (r ∘ Fin.castSucc) d ≤
        ((n : ℝ) - (lam - 1 + 2 * (i : ℝ) / r (Fin.last n))) / 2).card : ℝ) := by
  congr 2
  refine Finset.filter_congr fun d _ ↦ ?_
  rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]
  grind

/-- **Lemma 8** (lattice count estimate): the number of multi-indices in the box `∏ [0, r_j]`
of weight at most `(m - λ)/2` is at most `2 √m λ⁻¹ ∏ (r_j + 1)`.

Source: §6, Lemma `roth:lem8` ("the number of `m`-tuples ... `∑ j_i/r_i ≤ (m-λ)/2`
does not exceed `2 m^{1/2} λ^{-1} (r_1 + 1) ⋯ (r_m + 1)`"). -/
theorem card_filter_weight_le (m : ℕ) (r : Fin m → ℕ) (hr : ∀ j, 0 < r j) {lam : ℝ}
    (hlam : 0 < lam) :
    (((box r).filter fun d => weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤
      2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by
  classical
  induction m generalizing lam with
  | zero =>
    rw [filter_weight_le_eq_empty r (by simpa using hlam)]
    simp
  | succ n ih =>
    by_cases hA : lam ≤ 2 * √(((n + 1 : ℕ) : ℝ))
    · calc (((box r).filter fun d => weight r d ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ)
          ≤ (box r).card := by exact_mod_cast Finset.card_le_card (Finset.filter_subset _ _)
        _ = ∏ j, ((r j : ℝ) + 1) := by rw [card_box]; push_cast; rfl
        _ ≤ 2 * √(((n + 1 : ℕ) : ℝ)) / lam * ∏ j, ((r j : ℝ) + 1) :=
          le_mul_of_one_le_left (by positivity) (by rw [one_le_div hlam]; exact hA)
    push Not at hA
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · norm_num at hA
      rw [filter_weight_le_eq_empty r (by norm_num; linarith), card_empty, Nat.cast_zero]
      positivity
    set R := r (Fin.last n)
    have hR : 1 ≤ R := hr _
    have hsq1 : 1 ≤ √(((n + 1 : ℕ) : ℝ)) := Real.one_le_sqrt.2 (by simp)
    have hlami : ∀ i ∈ range (R + 1), 0 < lam - 1 + 2 * (i : ℝ) / R := fun i _ => by
      linarith [show 0 ≤ 2 * (i : ℝ) / R by positivity]
    have hs := sum_inv_lt (r := R) (m := n + 1) hR (by omega) hA
    push_cast [add_sub_cancel_right] at hs
    rw [card_filter_box_last, Nat.cast_sum,
      Finset.sum_congr rfl fun i _ => card_filter_fiber_eq r lam i]
    calc ∑ i ∈ range (R + 1), (((box (r ∘ Fin.castSucc)).filter fun d =>
            weight (r ∘ Fin.castSucc) d ≤ ((n : ℝ) - (lam - 1 + 2 * (i : ℝ) / R)) / 2).card : ℝ)
        ≤ ∑ i ∈ range (R + 1), 2 * √(n : ℝ) / (lam - 1 + 2 * (i : ℝ) / R) *
            ∏ j, (((r ∘ Fin.castSucc) j : ℝ) + 1) :=
          Finset.sum_le_sum fun i hi => ih (r ∘ Fin.castSucc) (fun j => hr _) (hlami i hi)
      _ = 2 * √(n : ℝ) * (∏ j, (((r ∘ Fin.castSucc) j : ℝ) + 1)) *
            ∑ i ∈ range (R + 1), (lam - 1 + 2 * (i : ℝ) / R)⁻¹ := by
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun i _ => by ring
      _ ≤ 2 * √(n : ℝ) * (∏ j, (((r ∘ Fin.castSucc) j : ℝ) + 1)) *
            (lam⁻¹ * (√(n : ℝ))⁻¹ * √((n : ℝ) + 1) * (R + 1)) :=
          mul_le_mul_of_nonneg_left hs.le (by positivity)
      _ = 2 * √(((n + 1 : ℕ) : ℝ)) / lam * ∏ j, ((r j : ℝ) + 1) := by
          rw [Fin.prod_univ_castSucc]
          push_cast
          field_simp
          simp [R]

end Roth
