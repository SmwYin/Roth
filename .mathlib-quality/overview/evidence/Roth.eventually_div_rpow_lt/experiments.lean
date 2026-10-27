import Roth.Main

/-! Evidence for `Roth.eventually_div_rpow_lt`. -/

open Filter Topology Asymptotics

/-- (1) Filter form over a real variable: the natural mathlib-shaped statement.
Composition of `tendsto_rpow_atTop`, `Tendsto.eventually_gt_atTop`, `eventually_gt_atTop`
and a pointwise rewrite. -/
example {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ' := by
  filter_upwards [(tendsto_rpow_atTop (sub_pos.2 hκ)).eventually_gt_atTop M,
    eventually_gt_atTop 0] with x hx hx0
  rwa [div_lt_iff₀ (Real.rpow_pos_of_pos hx0 κ), one_div_mul_eq_div, ← Real.rpow_sub hx0]

/-- (2) The project's exact statement recovered from the real filter form
(`tendsto_natCast_atTop_atTop.eventually` + `eventually_atTop`). -/
example {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by
  have h : ∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ' := by
    filter_upwards [(tendsto_rpow_atTop (sub_pos.2 hκ)).eventually_gt_atTop M,
      eventually_gt_atTop 0] with x hx hx0
    rwa [div_lt_iff₀ (Real.rpow_pos_of_pos hx0 κ), one_div_mul_eq_div, ← Real.rpow_sub hx0]
  obtain ⟨N, hN⟩ := eventually_atTop.1 (tendsto_natCast_atTop_atTop.eventually h)
  exact ⟨N, fun q hq ↦ hN q hq.le⟩

/-- (3) The real-exponent analogue of `Asymptotics.isLittleO_pow_pow_atTop_of_lt`
(not in mathlib per the searches). -/
theorem isLittleO_rpow_rpow_atTop_of_lt {a b : ℝ} (hab : a < b) :
    (fun x : ℝ ↦ x ^ a) =o[atTop] fun x ↦ x ^ b := by
  refine (isLittleO_iff_tendsto' ?_).2 ?_
  · filter_upwards [eventually_gt_atTop 0] with x hx h
    exact absurd h (Real.rpow_pos_of_pos hx b).ne'
  · refine (tendsto_rpow_neg_atTop (sub_pos.2 hab)).congr' ?_
    filter_upwards [eventually_gt_atTop 0] with x hx
    rw [← Real.rpow_sub hx, neg_sub]

/-- (4) Exact project statement still elaborates (reference use). -/
example {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' :=
  Roth.eventually_div_rpow_lt hκ
