import Roth.Theta

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

-- (1) Composition: `Θ_nonneg` is mathlib's `Real.sSup_nonneg` fed by the project's
-- `index_nonneg` on each member of `indexSet` (no `1 ≤ B`, no nonemptiness needed,
-- since `sSup ∅ = 0` in `ℝ`).
example {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} : 0 ≤ Θ B q r :=
  Real.sSup_nonneg fun _ ⟨_, _, _, _, hx⟩ ↦ hx ▸ index_nonneg _ _ _

-- (2) Via the lower-bound property: with `1 ≤ B` one can also use `le_csSup` at the
-- member `R = 1` (the paper's argument); strictly weaker than the current statement.
example {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} : 0 ≤ Θ B q r := by
  obtain ⟨x, hx⟩ := indexSet_nonempty hB q r
  obtain ⟨_, _, _, _, rfl⟩ := hx
  exact (index_nonneg _ _ _).trans (le_csSup (indexSet_bddAbove B q) ⟨_, ‹_›, _, ‹_›, rfl⟩)

-- (3) Signature check: only `[Fintype σ]`, no `[DecidableEq σ]`, no hypothesis on `B` or `r`.
#check @Θ_nonneg

end Roth
