import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition check: one call to mathlib's `Real.sInf_nonneg` plus the project's
`weight_nonneg`, after unfolding `index` (no use of `index_nonneg`). -/
example (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r :=
  Real.sInf_nonneg (by rintro _ ⟨d, -, rfl⟩; exact weight_nonneg r d)

/-- (2) Re-aim: the canonical weighted order is `ℕ∞`-valued, so nonnegativity is
`zero_le` (no lemma exists or is needed). -/
example (f : MvPowerSeries σ ℝ) (w : σ → ℕ) : 0 ≤ f.weightedOrder w := zero_le

/-- (3) The statement holds for every `r` (no positivity) and every `P`, including `P = 0`
where the junk value is `sInf ∅ = 0`. -/
example (α : σ → ℝ) (r : σ → ℕ) : index (0 : MvPolynomial σ ℝ) α r = 0 := by
  simp [index]

end Roth
