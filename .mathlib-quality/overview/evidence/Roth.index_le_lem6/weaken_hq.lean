import Roth.Theta
import Batteries.Tactic.OpenPrivate

/-! Evidence for `Roth.index_le_lem6`: (1) the positivity hypothesis `_hq : ∀ j, 0 < q j`
is unused — the same proof goes through without it; (2) `Θ_option_le` follows from the
weakened form. -/

namespace Roth
open MvPolynomial

open private index_numeric_bound_aux mapped_det_ne_zero_aux weight_le_delta_aux from Roth.Theta

variable {τ : Type*} [Fintype τ]

/-- (1) `index_le_lem6` without `_hq`; proof copied verbatim. -/
theorem index_le_lem6_no_hq {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ}
    (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ}
    {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤
        2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
          √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  classical
  have hrp0 : (0 : ℝ) < r none := (by norm_num : (0 : ℝ) < 3).trans_le hrp
  have hr0 : ∀ j, 0 < r j := fun j ↦ by
    cases j with
    | none => exact_mod_cast hrp0
    | some j => exact_mod_cast pos_of_mul_pos_right (hrp0.trans_le (hratio j)) hδ0
  obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1
  refine ⟨l, hl, hl', ?_⟩
  let α : Option τ → ℝ := fun j ↦ (h j : ℝ) / q j
  let Φ := lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l
  -- The two bounds for the index of `F`.
  have hlower := sum_max_sub_le_index_det D hD (mapped_det_ne_zero_aux hU hV hF) α hr0
    (fun d hd ↦ weight_le_delta_aux hδ0 hratio (hd.trans (Nat.sub_le_iff_le_add.2 hl')))
  have hupper := index_det_le hr0 hr₁ hR hh hl hU hV hUd hVd hF
  simp only [RingHom.map_det, RingHom.mapMatrix_apply, Matrix.map, Matrix.of_apply] at hupper
  simp only [hasseDeriv_map] at hlower
  -- Both summands of `Φ` are nonnegative.
  apply index_numeric_bound_aux (Φ := Φ) (l := (l : ℝ))
    (add_nonneg (Θ_nonneg _) (Θ_nonneg _)) hδ1 hrp
    (by exact_mod_cast (show 0 < l from hl))
    (by exact_mod_cast hl')
  exact (min_le_sum_max (θ := index (map (Int.castRingHom ℝ) R) α r) (rp := r none) l).trans
    (by simpa only [mul_add] using sub_le_iff_le_add.1 (hlower.trans hupper))

/-- (2) the original statement is recovered from the weakened one. -/
example {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ}
    (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (_hq : ∀ j, 0 < q j) {B : ℝ}
    {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤
        2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
          √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) :=
  index_le_lem6_no_hq hδ0 hδ1 hrp hratio hr₁ hR hh

end Roth
