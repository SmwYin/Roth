import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition check: `le_csInf_iff` on the finite nonempty image, `Set.forall_mem_image`,
and the project's `coeff_taylor` (no use of `le_index_iff`). -/
example {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {α : σ → ℝ} {r : σ → ℕ} {c : ℝ} :
    c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by
  rw [index, le_csInf_iff ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
    (by simpa using hP), Set.forall_mem_image]
  simp [mem_support_iff, coeff_taylor]

/-- (2) Re-aim: the analogous iff for mathlib's `MvPowerSeries.weightedOrder` of the Taylor
expansion is the pair `le_weightedOrder` / `weightedOrder_le` (mathlib has no packaged iff). -/
example {P : MvPolynomial σ ℝ} {α : σ → ℝ} (w : σ → ℕ) {n : ℕ∞} :
    n ≤ (taylor α P : MvPowerSeries σ ℝ).weightedOrder w ↔
      ∀ d, eval α (hasseDeriv d P) ≠ 0 → n ≤ Finsupp.weight w d := by
  refine ⟨fun h d hd ↦ h.trans (MvPowerSeries.weightedOrder_le w
    (by simpa [MvPolynomial.coeff_coe, coeff_taylor] using hd)), fun h ↦ ?_⟩
  refine MvPowerSeries.le_weightedOrder w fun d hd ↦ ?_
  by_contra h0
  exact (h d (by simpa [MvPolynomial.coeff_coe, coeff_taylor] using h0)).not_gt hd

/-- (3) `hP` is necessary: for `P = 0` the right side holds vacuously for `c = 1`, but
`index 0 α r = 0 < 1`. -/
example (α : σ → ℝ) (r : σ → ℕ) :
    ¬ (1 ≤ index (0 : MvPolynomial σ ℝ) α r ↔
      ∀ d, eval α (hasseDeriv d (0 : MvPolynomial σ ℝ)) ≠ 0 → (1 : ℝ) ≤ weight r d) := by
  simp [index]

end Roth
