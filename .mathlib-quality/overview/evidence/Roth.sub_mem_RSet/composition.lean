import Roth.MainLemma

open MvPolynomial

/-! Evidence for `Roth.sub_mem_RSet`.
1. The lemma is the anonymous-constructor combination of three mathlib facts
   (`sub_ne_zero`, `MvPolynomial.degreeOf_sub_le`, `abs_sub_le_of_nonneg_of_le`).
2. The coefficient bound of the difference uses only the nonnegativity and the upper bound,
   stated for an arbitrary linear ordered additive group (already mathlib's
   `abs_sub_le_of_nonneg_of_le`); there is no further hypothesis to drop. -/

example {σ : Type*} {r : σ → ℕ} {B : ℕ} {W' W'' : MvPolynomial σ ℤ}
    (h' : W' ∈ Roth.boxFamily r B) (h'' : W'' ∈ Roth.boxFamily r B) (hne : W' ≠ W'') :
    W' - W'' ∈ Roth.RSet B r :=
  ⟨sub_ne_zero.2 hne, fun j ↦ (degreeOf_sub_le j W' W'').trans (max_le (h'.1 j) (h''.1 j)),
    fun d ↦ by
      rw [coeff_sub, ← Int.cast_abs]
      exact_mod_cast abs_sub_le_of_nonneg_of_le (h'.2 d).1 (h'.2 d).2 (h''.2 d).1 (h''.2 d).2⟩

-- Coefficient-only form over a general ring: differences of polynomials with coefficients
-- in `[0, B]` have coefficients in `[-B, B]`.
example {σ R : Type*} [CommRing R] [LinearOrder R] [IsOrderedRing R] {B : R}
    {p q : MvPolynomial σ R} (hp : ∀ d, 0 ≤ p.coeff d ∧ p.coeff d ≤ B)
    (hq : ∀ d, 0 ≤ q.coeff d ∧ q.coeff d ≤ B) (d : σ →₀ ℕ) : |(p - q).coeff d| ≤ B := by
  rw [coeff_sub]
  exact abs_sub_le_of_nonneg_of_le (hp d).1 (hp d).2 (hq d).1 (hq d).2
