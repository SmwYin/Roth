import Roth.Theta

/-! Evidence for `Roth.Θ_le_card`. -/

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition: one `Real.sSup_le` call fed by the project's `index_le_card` via
`indexSet_bddAbove`'s body. Here we reuse `indexSet_bddAbove`'s witness: its bound is
definitionally `card σ`, so `csSup_le'`/`Real.sSup_le` close the goal without duplicating
the body. -/
example {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Fintype.card σ := by
  classical
  refine Real.sSup_le ?_ (Nat.cast_nonneg _)
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
    (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
          Int.cast_injective] using hRd) _

/-- (2) No hypotheses at all are needed: arbitrary `B` (including `B < 1`, empty
`indexSet`) and arbitrary `r` (including `r = 0`). -/
example (q : σ → ℕ) : Θ (-1) q (fun _ ↦ 0 : σ → ℕ) ≤ Fintype.card σ := Θ_le_card q

-- (3) Signature check: only `[Fintype σ]`.
#check @Θ_le_card

end Roth
