import Roth.MainLemma
import Mathlib.Data.Pi.Interval

/-! Evidence for the `/overview` assessment of `Roth.card_box`, re-aimed at mathlib's
`Finset.Iic` (the parent `Roth.box` is `NO-mathlib-has-it`, being
`Finset.Iic (Finsupp.equivFunOnFinite.symm r)`). `Roth.MainLemma` is imported only for the
`Finsupp.orderBot` instance, `Mathlib.Data.Pi.Interval` for `Pi.card_Iic`. -/

open Finset

variable {σ : Type*} [Fintype σ] [DecidableEq σ]

/-- Current definition: three mathlib simp lemmas (`card_map`, `card_piFinset`, `card_range`). -/
example (r : σ → ℕ) : #(Roth.box r) = ∏ j, (r j + 1) := by
  rw [Roth.box, card_map, Fintype.card_piFinset]; simp only [card_range]

/-- Re-aimed (finsupp interval): `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset`. -/
example (r : σ → ℕ) : #(Iic (Finsupp.equivFunOnFinite.symm r)) = ∏ j, (r j + 1) := by
  rw [Finsupp.card_Iic]
  simp only [Nat.card_Iic]
  rw [prod_subset (subset_univ _) fun j _ hj ↦ by simp_all]
  simp

/-- Re-aimed (pi interval, `σ → ℕ`): `Pi.card_Iic` and `Nat.card_Iic`, two calls. -/
example (r : σ → ℕ) : #(Iic r) = ∏ j, (r j + 1) := by
  simp only [Pi.card_Iic, Nat.card_Iic]

/-- Candidate general mathlib helper (absent): `univ`-product form of `Finsupp.card_Iic`
for a finite index type and any canonically ordered locally finite codomain. -/
example {ι α : Type*} [Fintype ι] [DecidableEq ι] [AddCommMonoid α] [PartialOrder α]
    [IsBotZeroClass α] [OrderBot α] [LocallyFiniteOrder α] [DecidableEq α] (f : ι →₀ α) :
    #(Iic f) = ∏ i, #(Iic (f i)) := by
  rw [Finsupp.card_Iic]
  refine prod_subset (subset_univ _) fun i _ hi ↦ ?_
  rw [Finsupp.notMem_support_iff.1 hi, ← bot_eq_zero, Iic_bot, card_singleton]

/-- `card_box` from the parent's bridge `box r = Iic _` (so a redefinition costs one line). -/
example (r : σ → ℕ) : #(Roth.box r) = ∏ j, (r j + 1) := by
  rw [show Roth.box r = Iic (Finsupp.equivFunOnFinite.symm r) by
    ext; simp [Roth.mem_box, Finsupp.le_def], Finsupp.card_Iic]
  simp only [Nat.card_Iic]
  rw [prod_subset (subset_univ _) fun j _ hj ↦ by simp_all]
  simp
