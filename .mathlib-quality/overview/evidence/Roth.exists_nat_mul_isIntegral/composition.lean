import Roth.Main
import Mathlib.RingTheory.Algebraic.Denominator

/-! Evidence for the /overview assessment of `Roth.exists_nat_mul_isIntegral`. -/

open Algebra

/-- Composition 1: mathlib's `Algebra.natDenominator` API (Mathlib/RingTheory/Algebraic/Denominator.lean)
gives the statement directly, with the canonical witness `natDenominator α`. -/
example {α : ℝ} (hα : IsAlgebraic ℚ α) :
    ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α) :=
  ⟨natDenominator α, Nat.pos_of_ne_zero ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα).natDenominator_ne_zero,
    by simpa [nsmul_eq_mul] using isIntegral_natDenominator_smul α⟩

/-- Generality check: the same composition works in any `ℚ`-algebra that is a commutative ring
(no use of `ℝ`). -/
example {A : Type*} [CommRing A] [Algebra ℚ A] {α : A} (hα : IsAlgebraic ℚ α) :
    ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : A) * α) :=
  ⟨natDenominator α, Nat.pos_of_ne_zero (IsAlgebraic.natDenominator_ne_zero ((IsFractionRing.isAlgebraic_iff ℤ ℚ A).2 hα)),
    by simpa [nsmul_eq_mul] using isIntegral_natDenominator_smul α⟩

/-- The project lemma itself, for comparison. -/
example {α : ℝ} (hα : IsAlgebraic ℚ α) : ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α) :=
  Roth.exists_nat_mul_isIntegral hα
