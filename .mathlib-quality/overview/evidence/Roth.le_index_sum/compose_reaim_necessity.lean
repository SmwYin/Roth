import Roth.Index

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-- (1) Composition check: `le_index_iff` (both directions) plus mathlib's
`map_sum` and `Finset.exists_ne_zero_of_sum_ne_zero`. -/
example {ι : Type*} {s : Finset ι} {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ}
    (hs : ∑ i ∈ s, f i ≠ 0) {c : ℝ} (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) :
    c ≤ index (∑ i ∈ s, f i) α r :=
  (le_index_iff hs).2 fun d hd ↦ by
    obtain ⟨i, hi, hid⟩ := Finset.exists_ne_zero_of_sum_ne_zero (by simpa [map_sum] using hd)
    have hfi : f i ≠ 0 := fun h0 ↦ hid (by simp [h0])
    exact (le_index_iff hfi).1 (hf i hi hfi) d hid

/-- (2) Re-aim: the finite-sum lower bound for mathlib's `MvPowerSeries.weightedOrder`
composes from `le_weightedOrder` and `coeff_eq_zero_of_lt_weightedOrder` (mathlib has
only the binary `min_weightedOrder_le_add`, no packaged finite-sum version). -/
example {τ ι : Type*} {s : Finset ι} (w : τ → ℕ) (f : ι → MvPowerSeries τ ℝ) {n : ℕ∞}
    (hf : ∀ i ∈ s, n ≤ (f i).weightedOrder w) :
    n ≤ (∑ i ∈ s, f i).weightedOrder w :=
  MvPowerSeries.le_weightedOrder w fun d hd ↦ by
    rw [map_sum]
    exact Finset.sum_eq_zero fun i hi ↦
      MvPowerSeries.coeff_eq_zero_of_lt_weightedOrder w (hd.trans_le (hf i hi))

/-- (3) `hs` is necessary: for the empty sum (= 0) the hypothesis `hf` is vacuous, but
`1 ≤ index 0 α r` fails because of the junk value `index 0 = 0`. -/
example (α : σ → ℝ) (r : σ → ℕ) :
    ¬ (1 : ℝ) ≤ index (∑ _i ∈ (∅ : Finset ℕ), (0 : MvPolynomial σ ℝ)) α r := by
  simp [index]

/-- (4) The `f i ≠ 0 →` guard is a genuine weakening: the unguarded hypothesis fails as soon
as a summand is zero and `c > 0`, e.g. `f = ![0, X i]` at `α = 0` with `c = 1/r i`. Here we
just record that a zero summand has index `0`. -/
example (α : σ → ℝ) (r : σ → ℕ) : index (0 : MvPolynomial σ ℝ) α r = 0 := by
  simp [index]

end Roth
