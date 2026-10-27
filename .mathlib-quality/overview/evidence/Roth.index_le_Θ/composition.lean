import Roth.Theta

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

-- (1) Composition: `index_le_Θ` is exactly one call of mathlib's `le_csSup`, fed by the
-- project's `indexSet_bddAbove` and the anonymous-constructor membership witness.
example {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ} (hR : R ∈ RSet B r) {h : σ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r :=
  le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩

-- (2) Set-membership restatement: any element of `indexSet` is `≤ Θ`.
example {B : ℝ} {q r : σ → ℕ} {x : ℝ} (hx : x ∈ indexSet B q r) : x ≤ Θ B q r :=
  le_csSup (indexSet_bddAbove B q) hx

-- (3) No `[DecidableEq σ]` needed (the section variable is omitted in the source too).
#check @index_le_Θ

end Roth
