import Roth.MainLemma

/-! Evidence for the `/overview` assessment of `Roth.box`:
`box r` is mathlib's lower-set interval `Finset.Iic r` (equivalently `Finset.Icc 0 r`) in the
locally finite order on `σ →₀ ℕ` (`Finsupp.instLocallyFiniteOrder`,
`Mathlib/Data/Finsupp/Interval.lean`). `Roth.MainLemma` is imported only to get the instances
(`Finsupp.orderBot` etc.) that `Roth.Box` alone does not import; `Roth/MainLemma.lean:282`
already uses `Finset.Iic (Finsupp.ofSupportFinite r _)` as an inline box. -/

open Finset

variable {σ : Type*} [Fintype σ] [DecidableEq σ]

/-- `box r` is `Finset.Iic` of `r` viewed as a finsupp. -/
example (r : σ → ℕ) : Roth.box r = Iic (Finsupp.equivFunOnFinite.symm r) := by
  ext d; simp [Roth.mem_box, Finsupp.le_def]

/-- ... and equally `Finset.Icc 0 r` (needs only `Mathlib.Data.Finsupp.Interval`). -/
example (r : σ → ℕ) : Roth.box r = Icc 0 (Finsupp.equivFunOnFinite.symm r) := by
  ext d; simp [Roth.mem_box, Finsupp.le_def]

/-- Membership in `Iic` is the coordinatewise bound (one mathlib call). -/
example (r : σ →₀ ℕ) (d : σ →₀ ℕ) : d ∈ Iic r ↔ ∀ j, d j ≤ r j := by
  simp [Finsupp.le_def]

/-- Cardinality: `Finsupp.card_Iic` plus `Nat.card_Iic`, then pass from `support` to `univ`. -/
example (r : σ →₀ ℕ) : #(Iic r) = ∏ j, (r j + 1) := by
  rw [Finsupp.card_Iic]
  simp only [Nat.card_Iic]
  exact Finset.prod_subset (subset_univ _) fun j _ hj ↦ by simp_all

/-- The `Iic` form needs no `Fintype σ` (only `DecidableEq`, for the finsupp interval instance). -/
example {τ : Type*} [DecidableEq τ] (r : τ →₀ ℕ) (d : τ →₀ ℕ) : d ∈ Iic r ↔ d ≤ r := mem_Iic
