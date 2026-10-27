import Roth.Theta

/-! Evidence for the overview assessment of `Roth.indexSet`. -/

open MvPolynomial

namespace Roth.IndexSetEvidence

/-- (1) `indexSet` needs only `[Fintype σ]` (no `[DecidableEq σ]`). -/
example {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : Set ℝ := Roth.indexSet B q r

/-- (2) `indexSet` is the image of the index map over the admissible pairs `(R, h)`:
a direct `Set.image` composition of mathlib primitives with `RSet` and `index`. -/
theorem indexSet_eq_image {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) :
    Roth.indexSet B q r =
      (fun p : MvPolynomial σ ℤ × (σ → ℤ) ↦
          index (map (Int.castRingHom ℝ) p.1) (fun j ↦ (p.2 j : ℝ) / q j) r) ''
        (Roth.RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)}) := by
  ext x
  simp only [Roth.indexSet, Set.mem_image, Set.mem_prod, Prod.exists, Set.mem_ofPred_eq]
  constructor
  · rintro ⟨R, hR, h, hh, rfl⟩; exact ⟨R, h, ⟨hR, hh⟩, rfl⟩
  · rintro ⟨R, h, ⟨hR, hh⟩, rfl⟩; exact ⟨R, hR, h, hh, rfl⟩

/-- (3) Consequently `Θ` is an `iSup`-free `sSup` over that image (definitional). -/
example {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) :
    Roth.Θ B q r = sSup (Roth.indexSet B q r) := rfl

end Roth.IndexSetEvidence
