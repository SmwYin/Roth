import Roth.Theta

/-! Evidence for the overview assessment of `Roth.Θ`. -/

open MvPolynomial

namespace Roth.ThetaEvidence

/-- (1) `Θ` needs only `[Fintype σ]` (no `[DecidableEq σ]`). -/
noncomputable example {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : ℝ := Roth.Θ B q r

/-- (2) `Θ` is a single `sSup` of the image of the index map over the admissible pairs:
one mathlib `sSup` over the `Set.image` composition proved for `indexSet`. -/
theorem Θ_eq_sSup_image {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) :
    Roth.Θ B q r =
      sSup ((fun p : MvPolynomial σ ℤ × (σ → ℤ) ↦
          index (map (Int.castRingHom ℝ) p.1) (fun j ↦ (p.2 j : ℝ) / q j) r) ''
        (Roth.RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)})) := by
  unfold Roth.Θ
  congr 1
  ext x
  simp only [Roth.indexSet, Set.mem_image, Set.mem_prod, Prod.exists, Set.mem_ofPred_eq]
  constructor
  · rintro ⟨R, hR, h, hh, rfl⟩; exact ⟨R, h, ⟨hR, hh⟩, rfl⟩
  · rintro ⟨R, h, ⟨hR, hh⟩, rfl⟩; exact ⟨R, hR, h, hh, rfl⟩

/-- (3) Junk value: for `B < 1` the family is empty (all coefficients vanish, but `R ≠ 0`),
so `Θ B q r = sSup ∅ = 0` by `Real.sSup_empty`. -/
theorem Θ_of_lt_one {σ : Type*} [Fintype σ] {B : ℝ} (hB : B < 1) (q r : σ → ℕ) :
    Roth.Θ B q r = 0 := by
  have hempty : Roth.indexSet B q r = ∅ := by
    ext x
    simp only [Set.mem_empty_iff_false, iff_false]
    rintro ⟨R, ⟨hR0, -, hRc⟩, -⟩
    apply hR0
    ext d
    have h1 := hRc d
    have h2 : |R.coeff d| < 1 := by exact_mod_cast h1.trans_lt hB
    simpa [Int.abs_lt_one_iff] using h2
  simp [Roth.Θ, hempty, Real.sSup_empty]

end Roth.ThetaEvidence
