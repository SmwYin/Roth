import Roth.Theta

open MvPolynomial

namespace Roth.RSetEvidence

/-- (1) `RSet` needs neither `[Fintype σ]` nor `[DecidableEq σ]` (elaborates for bare `σ`). -/
example {σ : Type*} (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ) := Roth.RSet B r

/-- (2) The degree condition of `RSet` is mathlib's `degreesLE` with the multiset of `r`
(for finitely supported `r`). -/
theorem forall_degreeOf_le_iff_mem_degreesLE {σ : Type*} [DecidableEq σ] (R : MvPolynomial σ ℤ)
    (r : σ →₀ ℕ) :
    (∀ j, degreeOf j R ≤ r j) ↔ R ∈ degreesLE ℤ σ (Finsupp.toMultiset r) := by
  simp [mem_degreesLE, Multiset.le_iff_count, degreeOf_def, Finsupp.count_toMultiset]

/-- (3) Hence `RSet` is a composite of mathlib notions: nonzero, `degreesLE`, coefficient box. -/
theorem RSet_eq {σ : Type*} [DecidableEq σ] (B : ℝ) (r : σ →₀ ℕ) :
    Roth.RSet B r = {R | R ≠ 0 ∧ R ∈ degreesLE ℤ σ (Finsupp.toMultiset r) ∧
      ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B} := by
  ext R
  simp only [Roth.RSet, Set.mem_ofPred_eq, forall_degreeOf_le_iff_mem_degreesLE]

end Roth.RSetEvidence
