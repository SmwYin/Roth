import Roth.Theta
import Batteries.Tactic.OpenPrivate

/-! Evidence for `Roth.Θ_option_le`: (1) the per-point Lemma 6 without the unused `_hq`
(copied from evidence/Roth.index_le_lem6); (2) `Θ_option_le` without `hq : ∀ j, 0 < q j`,
proof otherwise verbatim; (3) original recovered in one line; (4) also without `hB : 1 ≤ B`. -/

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

/-- (2) `Θ_option_le` without `hq`; proof verbatim except the call to (1). -/
theorem Θ_option_le_no_hq {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ}
    (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ} (hB : 1 ≤ B) :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (by lia))
      (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
        √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  refine Θ_le_of_forall_index_le hB fun R hR h hh ↦ ?_
  obtain ⟨l, hl, hl', hle⟩ := index_le_lem6_no_hq hδ0 hδ1 hrp hratio hr₁ hR hh
  refine hle.trans (mul_le_mul_of_nonneg_left ?_ (by norm_num))
  exact Finset.le_sup' (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
    √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) (Finset.mem_Icc.2 ⟨hl, hl'⟩)

/-- (3) the original statement is recovered from (2). -/
example {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ))
    (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁)
    {q : Option τ → ℕ} (_hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B) :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (by lia))
      (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
        √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) :=
  Θ_option_le_no_hq hδ0 hδ1 hrp hratio hr₁ hB

/-- (4) additionally without `hB : 1 ≤ B`: for `B < 1` the set `ℛ_p(B; r)` is empty, and
`Real.sSup_le` only needs the right-hand side to be nonnegative. -/
theorem Θ_option_le_no_hq_no_hB {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ}
    (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ} :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (by lia))
      (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
        √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  set f := fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
    √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ
  refine Real.sSup_le ?_ ?_
  · rintro _ ⟨R, hR, h, hh, rfl⟩
    obtain ⟨l, hl, hl', hle⟩ := index_le_lem6_no_hq hδ0 hδ1 hrp hratio hr₁ hR hh
    exact hle.trans (mul_le_mul_of_nonneg_left
      (Finset.le_sup' f (Finset.mem_Icc.2 ⟨hl, hl'⟩)) (by norm_num))
  · have h1 : 0 ≤ f 1 := add_nonneg (add_nonneg (add_nonneg (Θ_nonneg _) (Θ_nonneg _))
      (Real.sqrt_nonneg _)) (Real.sqrt_nonneg _)
    exact mul_nonneg (by norm_num) (h1.trans (Finset.le_sup' f
      (Finset.mem_Icc.2 ⟨le_rfl, by lia⟩)))

end Roth
