import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition check without the sibling API lemmas: `index = 0` iff `0` lies in the finite
nonempty image (`Set.Nonempty.csInf_mem` + `csInf_le`/`Real.sInf_nonneg`), the weight-zero
multi-index is `0` (`weight_eq_zero_iff`), and the `0`-th Taylor coefficient is `P(α)`. -/
example {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) :
    index P α r = 0 ↔ eval α P ≠ 0 := by
  have hfin := (taylor α P).support.finite_toSet.image (weight r)
  have hne : (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))).Nonempty := by simpa using hP
  have key : (0 : σ →₀ ℕ) ∈ (taylor α P).support ↔ eval α P ≠ 0 := by
    rw [mem_support_iff, coeff_taylor, hasseDeriv_zero_apply]
  rw [← key]
  constructor
  · intro h
    obtain ⟨d, hd, hdw⟩ := hne.csInf_mem hfin
    rw [← index, h, weight_eq_zero_iff hr] at hdw
    exact hdw ▸ hd
  · intro h
    refine le_antisymm (le_of_le_of_eq
      (csInf_le hfin.bddBelow (Set.mem_image_of_mem (weight r) h)) (by simp [weight]))
      (index_nonneg P α r)

/-- (2) Re-aim at mathlib's canonical object: for positive natural weights, the weighted order
of the Taylor expansion vanishes iff `P(α) ≠ 0`. Mathlib has the unweighted
`MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` but no weighted version; it composes from
`weightedOrder_le` / `le_weightedOrder`. -/
example {P : MvPolynomial σ ℝ} {α : σ → ℝ} (w : σ → ℕ) (hw : ∀ j, 0 < w j) :
    (taylor α P : MvPowerSeries σ ℝ).weightedOrder w = 0 ↔ eval α P ≠ 0 := by
  have h0 : MvPowerSeries.coeff (0 : σ →₀ ℕ) (taylor α P : MvPowerSeries σ ℝ) = eval α P := by
    rw [MvPolynomial.coeff_coe, coeff_taylor, hasseDeriv_zero_apply]
  constructor
  · intro h hP0
    have : (1 : ℕ∞) ≤ (taylor α P : MvPowerSeries σ ℝ).weightedOrder w := by
      refine MvPowerSeries.le_weightedOrder w fun d hd ↦ ?_
      have hd0 : Finsupp.weight w d = 0 := by exact_mod_cast Order.lt_one_iff.mp hd
      have : d = 0 := by
        ext j
        simpa [hd0] using Finsupp.le_weight w (hw j).ne' d
      simpa [this, h0] using hP0
    rw [h] at this
    exact absurd this (by simp)
  · intro h
    exact nonpos_iff_eq_zero.mp
      (by simpa using MvPowerSeries.weightedOrder_le w (d := 0) (by rw [h0]; exact h))

/-- (3a) `hP` is necessary: `index 0 α r = 0` but `eval α 0 = 0`. -/
example (α : σ → ℝ) (r : σ → ℕ) :
    ¬ (index (0 : MvPolynomial σ ℝ) α r = 0 ↔ eval α (0 : MvPolynomial σ ℝ) ≠ 0) := by
  simp [index]

/-- (3b) `hr` is necessary: with `r = 0` (division by zero gives weight `0`), `P = X ()` at
`α = 0` has index `0` (attained at `d = single () 1`) although `P(0) = 0`. -/
example : ¬ (index (X () : MvPolynomial Unit ℝ) 0 0 = 0 ↔
    eval (0 : Unit → ℝ) (X () : MvPolynomial Unit ℝ) ≠ 0) := by
  have h : index (X () : MvPolynomial Unit ℝ) 0 0 = 0 := by
    refine le_antisymm ?_ (index_nonneg _ _ _)
    have := index_le_weight (P := (X () : MvPolynomial Unit ℝ)) (α := 0) (r := 0)
      (d := Finsupp.single () 1) (by
        rw [← coeff_taylor, taylor_X]
        simp [coeff_X])
    simpa [weight] using this
  simp [h]

end Roth
