import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Current proof: one `Exists.imp` on `exists_weight_eq_index`. -/
example {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) {c : ℝ}
    (hc : index P α r < c) : ∃ k : σ →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 :=
  (exists_weight_eq_index hP α r).imp fun _ ⟨hd, hw⟩ ↦ ⟨hw ▸ hc, hd⟩

/-- (2) Alternative: contrapositive of `le_index_iff` (no attainment needed). -/
example {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) {c : ℝ}
    (hc : index P α r < c) : ∃ k : σ →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 := by
  by_contra! h
  exact hc.not_ge ((le_index_iff hP).2 fun d hd ↦ le_of_not_gt fun hw ↦ hd (h d hw))

/-- (3) `hP` is necessary: for `P = 0` and `c > index 0 α r` there is no nonvanishing
derivative. -/
example (α : σ → ℝ) (r : σ → ℕ) :
    ¬ ∃ k : σ →₀ ℕ, weight r k < index 0 α r + 1 ∧
      eval α (hasseDeriv k (0 : MvPolynomial σ ℝ)) ≠ 0 := by
  simp

/-- (4) Mathlib analogue for the canonical weighted order: the contrapositive of
`MvPowerSeries.le_weightedOrder`, one call. -/
example {R : Type*} [Semiring R] (w : σ → ℕ) (f : MvPowerSeries σ R) {n : ℕ∞}
    (hn : f.weightedOrder w < n) :
    ∃ d : σ →₀ ℕ, (Finsupp.weight w d : ℕ∞) < n ∧ MvPowerSeries.coeff d f ≠ 0 := by
  by_contra! h
  exact hn.not_ge (MvPowerSeries.le_weightedOrder w h)

end Roth
