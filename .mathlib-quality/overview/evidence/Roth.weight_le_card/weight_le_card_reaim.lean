import Roth.Box

/-! Evidence for the `Roth.weight_le_card` mathlibable assessment. -/

open Finsupp

variable {σ : Type*} [Fintype σ]

/-! (1) Re-aimed general form: a weighted degree whose every term `d i • w i` is `≤ c`
is at most `card σ • c`. One call to `Finset.sum_le_card_nsmul` after `weight_eq_sum`. -/
theorem finsupp_weight_le_card_nsmul {M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] (w : σ → M) (d : σ →₀ ℕ) (c : M)
    (h : ∀ i, d i • w i ≤ c) : Finsupp.weight w d ≤ Fintype.card σ • c := by
  rw [weight_eq_sum]
  exact Finset.sum_le_card_nsmul _ _ c fun i _ ↦ h i

/-! (2) Project lemma via the one-call composition on the explicit sum. -/
example {r : σ → ℕ} {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) :
    Roth.weight r d ≤ Fintype.card σ := by
  simpa [Roth.weight] using Finset.sum_le_card_nsmul Finset.univ (fun j ↦ (d j : ℝ) / r j) 1
    fun j _ ↦ div_le_one_of_le₀ (by exact_mod_cast hd j) (by positivity)

/-! (3) Weakening check: the hypothesis `hd` cannot be dropped (counterexample). -/
example : ¬ ∀ (r : Unit → ℕ) (d : Unit →₀ ℕ), Roth.weight r d ≤ Fintype.card Unit := by
  intro h
  have := h (fun _ ↦ 1) (Finsupp.single () 2)
  simp [Roth.weight] at this

/-! (4) Current project proof still compiles. -/
example {r : σ → ℕ} {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) :
    Roth.weight r d ≤ Fintype.card σ :=
  Roth.weight_le_card hd
