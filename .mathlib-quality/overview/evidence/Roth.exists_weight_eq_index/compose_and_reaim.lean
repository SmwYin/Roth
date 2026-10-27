import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition check: the statement follows from mathlib's `Set.Nonempty.csInf_mem`
(finite-set version) plus the project's `coeff_taylor` (no use of `exists_weight_eq_index`). -/
example {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by
  obtain ⟨d, hd, hdw⟩ := (show (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))).Nonempty by
    simpa using hP).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))
  exact ⟨d, by simpa [mem_support_iff, coeff_taylor] using hd, hdw⟩

/-- (2) Re-aim: the same statement for the mathlib-canonical weighted order of the Taylor
expansion is one call to `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`
(finiteness from `ne_zero_iff_weightedOrder_finite`). -/
example {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (w : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧
      (Finsupp.weight w d : ℕ∞) = (taylor α P : MvPowerSeries σ ℝ).weightedOrder w := by
  have h0 : (taylor α P : MvPowerSeries σ ℝ) ≠ 0 := by
    rw [Ne, MvPolynomial.coe_eq_zero_iff]
    simpa using hP
  obtain ⟨d, hd, hdw⟩ := MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder w
    ((MvPowerSeries.ne_zero_iff_weightedOrder_finite w).1 h0)
  exact ⟨d, by simpa [MvPolynomial.coeff_coe, coeff_taylor] using hd, hdw⟩

/-- (3) `hP` is necessary: for `P = 0` no multi-index has a nonvanishing derivative,
although `index 0 α r = 0` by the `sInf ∅ = 0` convention. -/
example (α : σ → ℝ) (r : σ → ℕ) :
    ¬ ∃ d, eval α (hasseDeriv d (0 : MvPolynomial σ ℝ)) ≠ 0 ∧
      weight r d = index 0 α r := by
  simp

end Roth
