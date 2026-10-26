import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_eq_sum_of_support_subset`.
1. General form over `[SeminormedCommRing R]` (same proof).
2. If the l1 norm is phrased via `Finsupp.sum`, the lemma is a two-call composition of
   `MvPolynomial.sum_def` and `Finsupp.sum_of_support_subset`. -/

open MvPolynomial

namespace Evidence2

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1Norm p = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

/-- Composition from mathlib primitives (after unfolding to `Finsupp.sum`). -/
theorem l1Norm_eq_sum_of_support_subset' {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1Norm p = ∑ d ∈ s, ‖p.coeff d‖ := by
  rw [l1Norm, ← MvPolynomial.sum_def (b := fun _ a ↦ ‖a‖)]
  exact Finsupp.sum_of_support_subset (AddMonoidAlgebra.coeff p) hs _ fun _ _ ↦ norm_zero

/-- The project lemma is the `R = ℤ` instance. -/
example {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)} (hs : P.support ⊆ s) :
    Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)| := by
  have := l1Norm_eq_sum_of_support_subset (R := ℤ) hs
  simpa only [l1Norm, Roth.normOne, Int.norm_eq_abs] using this

end Evidence2
