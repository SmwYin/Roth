import Roth.LeanEval
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

/-! Evidence for the `/overview` assessment of
`LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`.

1. The hypothesis `Irrational x` is superfluous: for rational `x` both sides are false.
2. The equivalence factors through the mathlib canonical form `¬ LiouvilleWith p x`. -/

open Filter LeanEval.NumberTheory.ThueSiegelRothProblem

namespace IsDiophantineIffEvidence

theorem irrational_of_isDiophantine {x : ℝ} (h : IsDiophantine x) : Irrational x := by
  rintro ⟨r, rfl⟩
  obtain ⟨C, hC, hb⟩ := h 1 one_pos
  have hq : (0 : ℤ) < (r.den : ℤ) := by exact_mod_cast r.pos
  have := hb r.num r.den hq
  have hr : ((r : ℝ) - (r.num : ℝ) / ((r.den : ℤ) : ℝ)) = 0 := by
    rw [Int.cast_natCast, sub_eq_zero]; exact_mod_cast (Rat.num_div_den r).symm
  rw [hr, abs_zero] at this
  exact this.not_ge (div_pos hC (Real.rpow_pos_of_pos (by exact_mod_cast r.pos) _)).le

/-- For rational `x`, every `approxSet x κ` is infinite (non-reduced representations). -/
theorem approxSet_infinite_of_not_irrational {x : ℝ} (hx : ¬ Irrational x) (κ : ℝ) :
    (Roth.approxSet x κ).Infinite := by
  obtain ⟨r, rfl⟩ : x ∈ Set.range ((↑) : ℚ → ℝ) := by
    by_contra h; exact hx h
  refine Set.infinite_of_injective_forall_mem
    (f := fun k : ℕ ↦ ((r.num * (k + 1) : ℤ), r.den * (k + 1))) ?_ fun k ↦ ?_
  · intro a b hab
    have := congrArg Prod.snd hab
    simp only at this
    have := Nat.eq_of_mul_eq_mul_left r.pos this
    omega
  · refine ⟨Nat.mul_pos r.pos k.succ_pos, ?_⟩
    have hk : ((k : ℝ) + 1) ≠ 0 := by positivity
    have hd : (r.den : ℝ) ≠ 0 := by exact_mod_cast r.den_nz
    have h0 : (r : ℝ) - ((r.num * (k + 1) : ℤ) : ℝ) / ((r.den * (k + 1) : ℕ) : ℝ) = 0 := by
      push_cast
      rw [mul_div_mul_right _ _ hk, sub_eq_zero]
      exact_mod_cast (Rat.num_div_den r).symm
    rw [h0, abs_zero]
    exact one_div_pos.2 (Real.rpow_pos_of_pos (by exact_mod_cast Nat.mul_pos r.pos k.succ_pos) _)

/-- **Weakening.** `isDiophantine_iff` without the `Irrational x` hypothesis. -/
theorem isDiophantine_iff' {x : ℝ} :
    IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2 := by
  by_cases hx : Irrational x
  · exact isDiophantine_iff hx
  · refine iff_of_false (fun h ↦ hx (irrational_of_isDiophantine h)) fun h ↦ ?_
    have := h (approxSet_infinite_of_not_irrational hx 3)
    norm_num at this

/-- `LiouvilleWith p α` gives infinitely many approximations of every quality `κ < p`. -/
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

/-- **Normal form.** For irrational `x`, the RHS of `isDiophantine_iff` is the mathlib form
`∀ p > 2, ¬ LiouvilleWith p x` (the shape of `ae_not_liouvilleWith`). -/
theorem approxSet_bound_iff_not_liouvilleWith {x : ℝ} (hx : Irrational x) :
    (∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2) ↔ ∀ p > 2, ¬ LiouvilleWith p x := by
  constructor
  · intro h p hp hL
    have := h (approxSet_infinite_of_liouvilleWith hL (by linarith : (p + 2) / 2 < p))
    linarith
  · intro h κ hinf
    exact le_of_not_gt fun hκ ↦ h κ hκ (liouvilleWith_of_approxSet_infinite hx hinf)

/-- Composite: the harness predicate in mathlib vocabulary, via `isDiophantine_iff`. -/
theorem isDiophantine_iff_liouvilleWith {x : ℝ} (hx : Irrational x) :
    IsDiophantine x ↔ ∀ p > 2, ¬ LiouvilleWith p x :=
  (isDiophantine_iff hx).trans (approxSet_bound_iff_not_liouvilleWith hx)

end IsDiophantineIffEvidence
