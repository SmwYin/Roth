import Roth.MainLemma
import Mathlib.Data.Pi.Interval

/-! Evidence for the `/overview` assessment of `Roth.card_le_card_box`, re-aimed at mathlib's
`Finset.Iic` (the parent `Roth.box` is `NO-mathlib-has-it`, being
`Finset.Iic (Finsupp.equivFunOnFinite.symm r)`). `Roth.MainLemma` is imported only for the
`Finsupp.orderBot` instance (as in the `Roth.card_box` evidence), `Mathlib.Data.Pi.Interval`
for `Pi.card_Iic`. -/

open Finset

variable {σ : Type*} [Fintype σ]

/-- 1. Current statement: two mathlib calls (`Finset.card_le_card`, `trans_eq`) plus the
project API `Roth.mem_box`, `Roth.card_box`. -/
example {r : σ → ℕ} {s : Finset (σ →₀ ℕ)} (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) :
    #s ≤ ∏ j, (r j + 1) := by
  classical
  exact (card_le_card fun d hd ↦ Roth.mem_box.2 (hs d hd)).trans_eq (Roth.card_box r)

/-- 2. Re-aimed (finsupp interval `Iic`): `card_le_card` + `Finset.mem_Iic` + `Finsupp.card_Iic`,
`Nat.card_Iic`, `prod_subset` (the last three are the re-aimed `card_box`). -/
example [DecidableEq σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)} (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) :
    #s ≤ ∏ j, (r j + 1) := by
  refine (card_le_card (t := Iic (Finsupp.equivFunOnFinite.symm r)) fun d hd ↦
    mem_Iic.2 fun j ↦ by simpa using hs d hd j).trans_eq ?_
  rw [Finsupp.card_Iic]
  simp only [Nat.card_Iic]
  rw [prod_subset (subset_univ _) fun j _ hj ↦ by simp_all]
  simp

/-- 3. Re-aimed (pi interval, `σ → ℕ`): with `s ⊆ Iic r` the bound is one call chain
`card_le_card` + `Pi.card_Iic` + `Nat.card_Iic`. -/
example [DecidableEq σ] {r : σ → ℕ} {s : Finset (σ → ℕ)} (hs : s ⊆ Iic r) :
    #s ≤ ∏ j, (r j + 1) := by
  simpa only [Pi.card_Iic, Nat.card_Iic] using card_le_card hs

/-- 4. Generality probe: the bound holds for any locally finite codomain with bottom, as
`#s ≤ ∏ i, #(Iic (b i))`; it is just `card_le_card` + `Pi.card_Iic` (nothing new). -/
example {ι : Type*} [Fintype ι] [DecidableEq ι] {α : ι → Type*} [∀ i, DecidableEq (α i)]
    [∀ i, PartialOrder (α i)] [∀ i, LocallyFiniteOrderBot (α i)] {b : ∀ i, α i}
    {s : Finset (∀ i, α i)} (hs : ∀ x ∈ s, x ≤ b) : #s ≤ ∏ i, #(Iic (b i)) :=
  (card_le_card fun x hx ↦ mem_Iic.2 (hs x hx)).trans_eq (Pi.card_Iic b)

/-- 5. Call-site shape (Roth/MainLemma.lean:506, Roth/CoeffNorm.lean:264): the support of a
polynomial with `degreeOf j P ≤ r j` has at most `∏ (r j + 1)` monomials, by the same two-call
composition (no mathlib lemma states this directly). -/
example {R : Type*} [CommSemiring R] {r : σ → ℕ} {P : MvPolynomial σ R}
    (hP : ∀ j, MvPolynomial.degreeOf j P ≤ r j) : #P.support ≤ ∏ j, (r j + 1) := by
  classical
  exact (card_le_card fun d hd ↦ Roth.mem_box.2 fun j ↦
    (MvPolynomial.monomial_le_degreeOf j hd).trans (hP j)).trans_eq (Roth.card_box r)
