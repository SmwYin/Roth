import Roth.LeanEval
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

/-! Evidence for the `/overview` assessment of
`LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`.

(1) `Irrational x` is NOT superfluous in the harness statement: `IsDiophantine 0` is false while
    `0` is algebraic.
(2) The base ring of `IsAlgebraic` is immaterial: the `ℚ` version holds too.
(3) If mathlib had Roth in its own vocabulary (`IsAlgebraic ℤ α → 2 < p → ¬ LiouvilleWith p α`),
    the harness theorem would be a short corollary via the `IsDiophantine` / `LiouvilleWith`
    bridge; the mathlib form itself is proved from `Roth.roth` (see Roth.roth evidence). -/

open Filter LeanEval.NumberTheory.ThueSiegelRothProblem

namespace ThueSiegelRothEvidence

/-- (1) Irrationality is necessary: the harness predicate fails at `0`. -/
theorem not_isDiophantine_zero : ¬ IsDiophantine (0 : ℝ) := by
  intro h
  obtain ⟨C, hC, hb⟩ := h 1 one_pos
  have := hb 0 1 one_pos
  simp only [Int.cast_zero, Int.cast_one, sub_zero, abs_zero, Real.one_rpow,
    div_one] at this
  linarith

example : IsAlgebraic ℤ (0 : ℝ) ∧ ¬ IsDiophantine (0 : ℝ) :=
  ⟨isAlgebraic_zero, not_isDiophantine_zero⟩

/-- (2) Variant with rational coefficients (no `extendScalars` step needed). -/
theorem thueSiegelRoth_rat (x : ℝ) (hx : Irrational x) (halg : IsAlgebraic ℚ x) :
    IsDiophantine x :=
  (isDiophantine_iff hx).mpr (Roth.roth hx halg)

/-- For irrational `α`, infinitely many approximations of quality `κ` give `LiouvilleWith κ α`. -/
theorem liouvilleWith_of_approxSet_infinite {α κ : ℝ} (hα : Irrational α)
    (hinf : (Roth.approxSet α κ).Infinite) : LiouvilleWith κ α := by
  refine ⟨1, Nat.frequently_atTop_iff_infinite.2 ?_⟩
  have himg : (Prod.snd '' Roth.approxSet α κ).Infinite := by
    intro hfin
    obtain ⟨Q, hQ⟩ := hfin.bddAbove
    refine hinf ((Roth.approxSet_den_le_finite α κ Q).subset fun hq hmem ↦ ⟨hmem, ?_⟩)
    exact hQ ⟨hq, hmem, rfl⟩
  refine himg.mono ?_
  rintro _ ⟨⟨m, n⟩, ⟨-, hm⟩, rfl⟩
  exact ⟨m, by simpa using hα.ne_rational m n, hm⟩

/-- (3) The harness theorem from the mathlib-vocabulary form of Roth's theorem. -/
theorem thueSiegelRoth_of_not_liouvilleWith
    (roth : ∀ {α p : ℝ}, IsAlgebraic ℤ α → 2 < p → ¬ LiouvilleWith p α)
    (x : ℝ) (hx : Irrational x) (halg : IsAlgebraic ℤ x) : IsDiophantine x :=
  (isDiophantine_iff hx).mpr fun {_} hinf ↦ le_of_not_gt fun hκ ↦
    roth halg hκ (liouvilleWith_of_approxSet_infinite hx hinf)

end ThueSiegelRothEvidence
