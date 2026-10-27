import Roth.Theta

/-! Evidence for the overview assessment of `Roth.Θ_le_of_forall_index_le`. -/

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

-- (1) Composition: the lemma is one call of mathlib's `csSup_le`, fed by the project's
-- `indexSet_nonempty` and destructuring of `indexSet` membership.
example {B : ℝ} (hB : 1 ≤ B) {q r : σ → ℕ} {c : ℝ}
    (hc : ∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) : Θ B q r ≤ c :=
  csSup_le (indexSet_nonempty hB q r) fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ hc R hR h hh

-- (2) Alternative hypothesis: `0 ≤ c` in place of `1 ≤ B` (via `Real.sSup_le`, which
-- tolerates the empty set because `sSup ∅ = 0` in `ℝ`). Neither hypothesis implies the other.
example {B : ℝ} {q r : σ → ℕ} {c : ℝ} (hc0 : 0 ≤ c)
    (hc : ∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) : Θ B q r ≤ c :=
  Real.sSup_le (fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ hc R hR h hh) hc0

-- (3) Some side condition is needed: for `B < 1`, `RSet B r` is empty (the nonzero
-- polynomial has a coefficient of absolute value at least 1), so `Θ B q r = 0`, and the
-- hypothesis-free statement would give `0 ≤ c` for every `c`, e.g. `c = -1`.
example {q r : σ → ℕ} : Θ (1 / 2) q r = 0 := by
  have : indexSet (1 / 2) q r = ∅ := by
    ext x
    simp only [Set.mem_empty_iff_false, iff_false]
    rintro ⟨R, ⟨hR0, -, hRc⟩, -⟩
    obtain ⟨d, hd⟩ := ne_zero_iff.1 hR0
    have h1 : (1 : ℝ) ≤ |((R.coeff d : ℤ) : ℝ)| := by
      rw [← Int.cast_abs]; exact_mod_cast Int.one_le_abs hd
    linarith [hRc d]
  rw [Θ, this, Real.sSup_empty]

#check @Θ_le_of_forall_index_le

end Roth
