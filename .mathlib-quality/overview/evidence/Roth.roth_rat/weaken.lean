import Roth.Main
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith
import Mathlib.NumberTheory.DiophantineApproximation.Basic

/-! Evidence for the `/overview` assessment of `Roth.roth_rat`.

(1) `Irrational α` is superfluous in the `x.den` form: for rational `α` the `κ`-set is contained
    in the `2`-set when `κ ≥ 2`, and the latter is finite by mathlib's
    `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`.
(2) The den-form follows from the LiouvilleWith form `¬ LiouvilleWith p α` (re-proved here
    from `Roth.roth` as in the `Roth.roth` evidence), with no irrationality hypothesis at all.
(3) `IsAlgebraic ℤ` base ring variant, one term. -/

open Filter

/-- Monotonicity in the exponent of the den-form set. -/
theorem ratSet_mono {α κ κ' : ℝ} (h : κ' ≤ κ) :
    {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ} ⊆ {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ'} := by
  intro x (hx : |α - x| < 1 / (x.den : ℝ) ^ κ)
  show |α - x| < 1 / (x.den : ℝ) ^ κ'
  refine hx.trans_le (one_div_le_one_div_of_le (by positivity) ?_)
  exact Real.rpow_le_rpow_of_exponent_le (by exact_mod_cast x.den_pos) h

/-- (1) `Roth.roth_rat` without `Irrational α`. -/
theorem roth_rat' {α : ℝ} (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 := by
  by_contra! hκ
  by_cases hα : Irrational α
  · exact (Roth.roth_rat hα halg hinf).not_gt hκ
  · refine hα ((Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational α).1 ?_)
    refine hinf.mono fun x hx ↦ ?_
    have := ratSet_mono (α := α) hκ.le hx
    simpa [Real.rpow_two] using this

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

theorem IsAlgebraic.not_liouvilleWith' {α p : ℝ} (halg : IsAlgebraic ℚ α) (hp : 2 < p) :
    ¬ LiouvilleWith p α := fun hL ↦ by
  have hα : Irrational α := hL.irrational (by linarith)
  have := Roth.roth hα halg (approxSet_infinite_of_liouvilleWith' hL
    (by linarith : (p + 2) / 2 < p))
  linarith

/-- (2) The den-form from the LiouvilleWith form: an infinite den-set gives `LiouvilleWith κ α`
(constant `1`), after discarding the at most one `x` with `x = α`. -/
theorem roth_rat_of_not_liouvilleWith {α : ℝ} (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 := by
  by_contra! hκ
  refine IsAlgebraic.not_liouvilleWith' halg hκ ⟨1, ?_⟩
  refine Nat.frequently_atTop_iff_infinite.2 ?_
  set S := {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ} \ {x : ℚ | (x : ℝ) = α}
  have hsub : {x : ℚ | (x : ℝ) = α}.Subsingleton := fun a ha b hb ↦ by
    exact_mod_cast (show (a : ℝ) = b from ha.trans hb.symm)
  have hS : S.Infinite := hinf.sdiff hsub.finite
  have himg : (Rat.den '' S).Infinite := by
    intro hfin
    obtain ⟨Q, hQ⟩ := hfin.bddAbove
    have hfinQ := Roth.approxSet_den_le_finite α κ Q
    refine hS ((hfinQ.preimage (f := fun x : ℚ ↦ (x.num, x.den))
      (fun a _ b _ hab ↦ Rat.ext (congrArg Prod.fst hab) (congrArg Prod.snd hab))).subset ?_)
    intro x hx
    exact ⟨⟨x.den_pos, by rw [← Rat.cast_def]; exact hx.1⟩, hQ ⟨x, hx, rfl⟩⟩
  refine himg.mono ?_
  rintro _ ⟨x, ⟨hx, hne⟩, rfl⟩
  refine ⟨x.num, ?_, ?_⟩
  · rw [← Rat.cast_def]; exact fun h ↦ hne h.symm
  · rw [← Rat.cast_def]; exact hx

/-- (3) Base ring `ℤ`. -/
example {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℤ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 :=
  Roth.roth_rat hα (halg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)) hinf
