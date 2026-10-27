import Roth.Theta

/-! Evidence for the Roth.Θ_mono assessment. -/

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

-- (1) one-term composition: `csSup_le_csSup` plus monotonicity of `indexSet` in `B`.
example {B B' : ℝ} (hB : 1 ≤ B) (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ} :
    Θ B q r ≤ Θ B' q r :=
  csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r)
    fun _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, hx⟩ ↦ ⟨R, ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩, h, hh, hx⟩

-- (2) weakening: `hB : 1 ≤ B` is superfluous. If `indexSet B q r = ∅` then `Θ B q r = 0`,
-- which is `≤ Θ B' q r` by `Θ_nonneg`.
theorem Θ_mono' {B B' : ℝ} (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ} :
    Θ B q r ≤ Θ B' q r := by
  have hsub : indexSet B q r ⊆ indexSet B' q r :=
    fun _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, hx⟩ ↦
      ⟨R, ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩, h, hh, hx⟩
  rcases (indexSet B q r).eq_empty_or_nonempty with he | hne
  · rw [Θ, he, Real.sSup_empty]
    exact Θ_nonneg q
  · exact csSup_le_csSup (indexSet_bddAbove B' q) hne hsub

-- (3) the old statement is a corollary of the weakened one.
example {B B' : ℝ} (_hB : 1 ≤ B) (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ} :
    Θ B q r ≤ Θ B' q r := Θ_mono' hBB' q

-- (4) `Monotone` form.
example (q r : σ → ℕ) : Monotone fun B : ℝ ↦ Θ B q r := fun _ _ h ↦ Θ_mono' h q

#check @Θ_mono

end Roth
