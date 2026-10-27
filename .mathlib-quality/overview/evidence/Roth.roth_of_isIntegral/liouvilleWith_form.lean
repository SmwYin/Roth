import Roth.Main
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

/-! Evidence for the `/overview` assessment of `Roth.roth_of_isIntegral`.

(1) The mathlib-vocabulary form `¬ LiouvilleWith p α` (p > 2) for irrational real algebraic
    integers, derived from `Roth.roth_of_isIntegral` via the `approxSet` ↔ `LiouvilleWith`
    bridges (copied from `evidence/Roth.approxSet/liouvilleWith_bridge.lean`).
(2) `Roth.roth_of_isIntegral` is the special case `IsIntegral ℤ α → IsAlgebraic ℚ α` of
    `Roth.roth` (one term), so it is strictly narrower than the main theorem.
(3) The hypothesis `Irrational α` cannot be dropped: `approxSet 0 3` is infinite. -/

open Filter

theorem approxSet_infinite_of_liouvilleWith {α p κ : ℝ} (h : LiouvilleWith p α) (hκ : κ < p) :
    (Roth.approxSet α κ).Infinite := by
  intro hfin
  have hfr := h.frequently_lt_rpow_neg hκ
  have hinf : {n : ℕ | 0 < n ∧ ∃ m : ℤ, |α - m / n| < 1 / (n : ℝ) ^ κ}.Infinite := by
    refine Nat.frequently_atTop_iff_infinite.1 ?_
    refine ((eventually_gt_atTop 0).and_frequently hfr).mono ?_
    rintro n ⟨hn, m, -, hm⟩
    exact ⟨hn, m, by rwa [Real.rpow_neg (Nat.cast_nonneg n), ← one_div] at hm⟩
  refine hinf ((hfin.image Prod.snd).subset ?_)
  rintro n ⟨hn, m, hm⟩
  exact ⟨(m, n), ⟨hn, hm⟩, rfl⟩

/-- (1) Roth's theorem for algebraic integers in mathlib's `LiouvilleWith` vocabulary. -/
theorem not_liouvilleWith_of_isIntegral {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α)
    {p : ℝ} (hp : 2 < p) : ¬ LiouvilleWith p α := fun hL ↦ by
  have := Roth.roth_of_isIntegral hα hint
    (approxSet_infinite_of_liouvilleWith hL (by linarith : (p + 2) / 2 < p))
  linarith

/-- (2) `roth_of_isIntegral` is a one-term special case of `Roth.roth`. -/
example {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
    (hinf : (Roth.approxSet α κ).Infinite) : κ ≤ 2 :=
  Roth.roth hα (hint.isAlgebraic.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)) hinf

/-- (3) Without irrationality the conclusion fails: `α = 0` (an algebraic integer) has
infinitely many exact "approximations" `(0, q)` of every quality, e.g. `κ = 3`. -/
example : (Roth.approxSet 0 3).Infinite ∧ IsIntegral ℤ (0 : ℝ) ∧ ¬ ((3 : ℝ) ≤ 2) := by
  refine ⟨?_, isIntegral_zero, by norm_num⟩
  have hinj : Function.Injective (fun q : ℕ ↦ ((0 : ℤ), q + 1)) := fun a b h ↦ by
    simpa using congrArg Prod.snd h
  refine (Set.infinite_range_of_injective hinj).mono ?_
  rintro _ ⟨q, rfl⟩
  refine ⟨Nat.succ_pos q, ?_⟩
  simp only [Int.cast_zero, zero_div, sub_zero, abs_zero, one_div]
  positivity
