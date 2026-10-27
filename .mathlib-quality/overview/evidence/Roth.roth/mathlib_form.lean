import Roth.Main
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

/-! Evidence for the `/overview` assessment of `Roth.roth` (Roth's theorem).

(1) The mathlib-facing form `IsAlgebraic.not_liouvilleWith`: for algebraic `α` and `2 < p`,
    `¬ LiouvilleWith p α`. In this form the hypothesis `Irrational α` is superfluous
    (it is supplied by mathlib's `LiouvilleWith.irrational`), and `IsAlgebraic ℤ` and
    `IsAlgebraic ℚ` are interchangeable.
(2) The contrapositive "transcendence" form announced in mathlib's `LiouvilleWith` docstring:
    `LiouvilleWith p α` with `2 < p` implies `Transcendental ℤ α`.
(3) Conversely, `Roth.roth` is recovered from (1) (so (1) is not weaker in content).
(4) In the project's `approxSet` form `Irrational α` cannot be dropped: `approxSet 0 3` is
    infinite and `0` is algebraic.
(5) `IsAlgebraic ℤ α` gives `Roth.roth` too (weakening of the base ring, one term). -/

open Filter

theorem approxSet_infinite_of_liouvilleWith' {α p κ : ℝ} (h : LiouvilleWith p α) (hκ : κ < p) :
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

/-- (1) Roth's theorem in mathlib's vocabulary, with no irrationality hypothesis. -/
theorem IsAlgebraic.not_liouvilleWith' {α p : ℝ} (halg : IsAlgebraic ℚ α) (hp : 2 < p) :
    ¬ LiouvilleWith p α := fun hL ↦ by
  have hα : Irrational α := hL.irrational (by linarith)
  have := Roth.roth hα halg (approxSet_infinite_of_liouvilleWith' hL
    (by linarith : (p + 2) / 2 < p))
  linarith

/-- (1') Same with integer coefficients. -/
example {α p : ℝ} (halg : IsAlgebraic ℤ α) (hp : 2 < p) : ¬ LiouvilleWith p α :=
  IsAlgebraic.not_liouvilleWith' (halg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)) hp

/-- (2) The transcendence form of the mathlib docstring. -/
theorem LiouvilleWith.transcendental' {α p : ℝ} (h : LiouvilleWith p α) (hp : 2 < p) :
    Transcendental ℤ α := fun halg ↦
  IsAlgebraic.not_liouvilleWith' (halg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)) hp h

/-- (3) `Roth.roth` back from (1): for irrational `α`, infinitely many approximations of quality
`κ` give `LiouvilleWith κ α` with constant `1`. -/
example {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : (Roth.approxSet α κ).Infinite) : κ ≤ 2 := by
  refine le_of_not_gt fun hκ ↦ IsAlgebraic.not_liouvilleWith' halg hκ ⟨1, ?_⟩
  refine Nat.frequently_atTop_iff_infinite.2 ?_
  have himg : (Prod.snd '' Roth.approxSet α κ).Infinite := by
    intro hfin
    obtain ⟨Q, hQ⟩ := hfin.bddAbove
    refine hinf ((Roth.approxSet_den_le_finite α κ Q).subset fun hq hmem ↦ ⟨hmem, ?_⟩)
    exact hQ ⟨hq, hmem, rfl⟩
  refine himg.mono ?_
  rintro _ ⟨⟨m, n⟩, ⟨-, hm⟩, rfl⟩
  exact ⟨m, by simpa using hα.ne_rational m n, hm⟩

/-- (4) In the `approxSet` form irrationality is necessary. -/
example : (Roth.approxSet 0 3).Infinite ∧ IsAlgebraic ℚ (0 : ℝ) ∧ ¬ ((3 : ℝ) ≤ 2) := by
  refine ⟨?_, isAlgebraic_zero, by norm_num⟩
  have hinj : Function.Injective (fun q : ℕ ↦ ((0 : ℤ), q + 1)) := fun a b h ↦ by
    simpa using congrArg Prod.snd h
  refine (Set.infinite_range_of_injective hinj).mono ?_
  rintro _ ⟨q, rfl⟩
  refine ⟨Nat.succ_pos q, ?_⟩
  simp only [Int.cast_zero, zero_div, sub_zero, abs_zero, one_div]
  positivity

/-- (5) Base ring `ℤ` instead of `ℚ`. -/
example {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℤ α) {κ : ℝ}
    (hinf : (Roth.approxSet α κ).Infinite) : κ ≤ 2 :=
  Roth.roth hα (halg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)) hinf
