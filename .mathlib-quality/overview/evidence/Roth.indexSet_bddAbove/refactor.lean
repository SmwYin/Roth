import Roth.Theta

/-! Evidence for `Roth.indexSet_bddAbove`: factor out the shared upper-bound fact. -/

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) The shared content of `indexSet_bddAbove` and `Θ_le_card`: `card σ` is an upper bound
of `indexSet B q r`. Same proof body as `indexSet_bddAbove`. -/
theorem card_mem_upperBounds_indexSet (B : ℝ) (q r : σ → ℕ) :
    (Fintype.card σ : ℝ) ∈ upperBounds (indexSet B q r) := by
  classical
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
    (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
          Int.cast_injective] using hRd) _

/-- (2) `indexSet_bddAbove` becomes a one-term corollary. -/
example (B : ℝ) (q : σ → ℕ) {r : σ → ℕ} : BddAbove (indexSet B q r) :=
  ⟨_, card_mem_upperBounds_indexSet B q r⟩

/-- (3) `Θ_le_card` becomes a one-term corollary (no duplicated body). -/
example {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Fintype.card σ :=
  Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)

/-- (4) Conversely, with the current API `indexSet_bddAbove` follows from nothing smaller than
`index_le_card`; there is no positivity hypothesis on `r` (the docstring's "if every `r j` is
positive" is not a hypothesis of the Lean statement). Statement with arbitrary `r` holds: -/
example (B : ℝ) (q : σ → ℕ) : BddAbove (indexSet B q (fun _ ↦ 0 : σ → ℕ)) :=
  indexSet_bddAbove B q

end Roth
