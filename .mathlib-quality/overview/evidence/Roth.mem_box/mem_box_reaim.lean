import Roth.MainLemma

/-! Evidence for `/overview` assessment of `Roth.mem_box`, re-aimed at mathlib's `Finset.Iic`
(the parent `Roth.box` is `NO-mathlib-has-it`, being `Finset.Iic (equivFunOnFinite.symm r)`). -/

open Finset

variable {σ : Type*} [Fintype σ] [DecidableEq σ]

/-- Re-aimed statement: membership in mathlib's `Iic` is the coordinatewise bound,
by `Finset.mem_Iic` and `Finsupp.le_def` (no `Fintype` needed). -/
example {τ : Type*} [DecidableEq τ] {r d : τ →₀ ℕ} : d ∈ Iic r ↔ ∀ j, d j ≤ r j :=
  mem_Iic.trans Finsupp.le_def

/-- The project's form, with `box r` replaced by the mathlib interval. -/
example {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ Iic (Finsupp.equivFunOnFinite.symm r) ↔ ∀ j, d j ≤ r j :=
  mem_Iic.trans Finsupp.le_def

/-- With the current definition, `mem_box` follows from the parent's bridge. -/
example {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ Roth.box r ↔ ∀ j, d j ≤ r j := by
  rw [show Roth.box r = Iic (Finsupp.equivFunOnFinite.symm r) by
    ext; simp [Roth.mem_box, Finsupp.le_def]]
  exact mem_Iic.trans Finsupp.le_def
