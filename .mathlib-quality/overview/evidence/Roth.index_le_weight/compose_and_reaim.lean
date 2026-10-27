import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition check: the statement follows from mathlib's `csInf_le` and
`Set.Finite.bddBelow` plus the project's `coeff_taylor` (no use of `index_le_weight`). -/
example {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ}
    (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d :=
  csInf_le ((taylor α P).support.finite_toSet.image _).bddBelow
    ⟨d, by simpa [mem_support_iff, coeff_taylor] using h, rfl⟩

/-- (2) Re-aim: the same statement for the mathlib-canonical weighted order of the
Taylor expansion is one call to `MvPowerSeries.weightedOrder_le`. -/
example {P : MvPolynomial σ ℝ} {α : σ → ℝ} (w : σ → ℕ) {d : σ →₀ ℕ}
    (h : eval α (hasseDeriv d P) ≠ 0) :
    (taylor α P : MvPowerSeries σ ℝ).weightedOrder w ≤ Finsupp.weight w d :=
  MvPowerSeries.weightedOrder_le w (by simpa [MvPolynomial.coeff_coe, coeff_taylor] using h)

/-- (3) Typical downstream specialisation (as at Index.lean:105): `d = 0` gives
`index P α r ≤ 0` whenever `P(α) ≠ 0`. -/
example {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} (h : eval α P ≠ 0) :
    index P α r ≤ 0 := by
  simpa using index_le_weight (r := r) (d := 0) (by simpa [hasseDeriv_zero_apply] using h)

end Roth
