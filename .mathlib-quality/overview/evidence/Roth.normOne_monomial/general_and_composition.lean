import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_monomial`.
1. General form over `[SeminormedCommRing R]` (verbatim proof).
2. Composition from mathlib: with `l1Norm` phrased via `Finsupp.sum`, the lemma is
   `MvPolynomial.sum_monomial_eq` + `norm_zero`.
3. `R = ℤ` bridge back to the exact project statement. -/

open MvPolynomial

namespace Evidence3

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1Norm p = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

/-- General form, verbatim proof. -/
theorem l1Norm_monomial (e : σ →₀ ℕ) (c : R) : l1Norm (monomial e c) = ‖c‖ := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_monomial_subset]
  simp

/-- Composition from mathlib primitives (after unfolding to `Finsupp.sum`). -/
theorem l1Norm_monomial' (e : σ →₀ ℕ) (c : R) : l1Norm (monomial e c) = ‖c‖ := by
  rw [l1Norm, ← MvPolynomial.sum_def (b := fun _ a ↦ ‖a‖)]
  exact MvPolynomial.sum_monomial_eq norm_zero

/-- The project lemma is the `R = ℤ` instance. -/
example (e : σ →₀ ℕ) (c : ℤ) : Roth.normOne (monomial e c) = |(c : ℝ)| := by
  have := l1Norm_monomial (R := ℤ) e c
  simpa only [l1Norm, Roth.normOne, Int.norm_eq_abs] using this

end Evidence3
