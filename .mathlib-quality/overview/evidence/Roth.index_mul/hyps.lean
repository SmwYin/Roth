import Roth.Index

/-! Evidence for `Roth.index_mul`. -/

open MvPolynomial

namespace Roth.Evidence

/-- (1) `hP : P ≠ 0` (symmetrically `hQ`) is necessary: with `P = 0`, `Q = X true`, `α = 0`,
`r = 1`, the left side is `index 0 = 0` while the right side is `0 + 1 = 1`
(Lean's `index 0 = sInf ∅ = 0`, not `+∞` as in the source). -/
example : index ((0 : MvPolynomial Bool ℝ) * X true) (fun _ ↦ 0) (fun _ ↦ 1) ≠
    index (0 : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) +
      index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) := by
  have h1 : index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 1 := by
    rw [index, taylor_zero, support_X]
    simp [weight, Finsupp.single_apply]
  rw [h1, zero_mul]
  simp [index]

/-- (2) Sanity check of the current statement through the generic mathlib lemma it rests on:
`MvPowerSeries.weightedOrder_mul` holds for every `w : σ → ℕ`, including zero weights. -/
example {σ : Type*} (w : σ → ℕ) (f g : MvPowerSeries σ ℝ) :
    (f * g).weightedOrder w = f.weightedOrder w + g.weightedOrder w :=
  MvPowerSeries.weightedOrder_mul w f g

end Roth.Evidence
