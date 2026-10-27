import Roth.LeanEval
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

/-! Evidence for the `/overview` assessment of
`LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`:
`IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`, i.e. the harness predicate is
composable from mathlib's `Irrational` and `LiouvilleWith`, and it already forces irrationality. -/

open Filter LeanEval.NumberTheory.ThueSiegelRothProblem

namespace IsDiophantineEvidence

/-- The harness predicate forces irrationality (take the exact representation `r.num / r.den`). -/
theorem irrational_of_isDiophantine {x : ℝ} (h : IsDiophantine x) : Irrational x := by
  rintro ⟨r, rfl⟩
  obtain ⟨C, hC, hb⟩ := h 1 one_pos
  have hq : (0 : ℤ) < (r.den : ℤ) := by exact_mod_cast r.pos
  have := hb r.num r.den hq
  have hr : ((r : ℝ) - (r.num : ℝ) / ((r.den : ℤ) : ℝ)) = 0 := by
    rw [Int.cast_natCast, sub_eq_zero]; exact_mod_cast (Rat.num_div_den r).symm
  rw [hr, abs_zero] at this
  exact this.not_ge (div_pos hC (Real.rpow_pos_of_pos (by exact_mod_cast r.pos) _)).le

/-- `LiouvilleWith p α` gives infinitely many approximations of every quality `κ < p`
(copied from `evidence/Roth.approxSet/liouvilleWith_bridge.lean`). -/
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

/-- **Composition.** The LeanEval predicate is `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`. -/
theorem isDiophantine_iff_liouvilleWith {x : ℝ} :
    IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x := by
  constructor
  · intro h
    have hx := irrational_of_isDiophantine h
    refine ⟨hx, fun p hp hL ↦ ?_⟩
    have := (isDiophantine_iff hx).1 h
      (approxSet_infinite_of_liouvilleWith hL (by linarith : (p + 2) / 2 < p))
    linarith
  · rintro ⟨hx, h⟩
    exact (isDiophantine_iff hx).2 fun {κ} hinf ↦ le_of_not_gt fun hκ ↦
      h κ hκ (liouvilleWith_of_approxSet_infinite hx hinf)

/-- The harness theorem, restated in mathlib vocabulary. -/
example (x : ℝ) (hx : Irrational x) (halg : IsAlgebraic ℤ x) {p : ℝ} (hp : 2 < p) :
    ¬ LiouvilleWith p x :=
  (isDiophantine_iff_liouvilleWith.1 (thueSiegelRoth x hx halg)).2 p hp

end IsDiophantineEvidence
