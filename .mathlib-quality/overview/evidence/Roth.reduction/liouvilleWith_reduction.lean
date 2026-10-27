import Roth.Main
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith
import Mathlib.RingTheory.Algebraic.Denominator

/-! Evidence for the `/overview` assessment of `Roth.reduction`: in mathlib's `LiouvilleWith`
vocabulary the §6 reduction is a two-call composition (`Algebra.natDenominator` plus
`LiouvilleWith.nat_mul`), with no loss in the exponent; the project statement follows from it
via the `approxSet` ↔ `LiouvilleWith` bridges (copied from
`evidence/Roth.approxSet/liouvilleWith_bridge.lean`). -/

open Filter Algebra

/-- (1) The reduction in mathlib vocabulary: exponent preserved, no `2 < p` needed. -/
theorem reduction_liouvilleWith {α p : ℝ} (halg : IsAlgebraic ℚ α) (h : LiouvilleWith p α) :
    ∃ α' : ℝ, IsIntegral ℤ α' ∧ LiouvilleWith p α' :=
  ⟨natDenominator α * α, by simpa [nsmul_eq_mul] using isIntegral_natDenominator_smul α,
    h.nat_mul ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 halg).natDenominator_ne_zero⟩

/-- Bridge A (copied): `LiouvilleWith p α` gives an infinite `approxSet α κ` for `κ < p`. -/
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

/-- Bridge B (copied): for irrational `α`, an infinite `approxSet α κ` gives `LiouvilleWith κ α`. -/
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

/-- (2) The project's exact statement recovered from (1) and the two bridges. -/
example {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hκ : 2 < κ)
    (hinf : (Roth.approxSet α κ).Infinite) : ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧
    2 < κ' ∧ (Roth.approxSet α' κ').Infinite := by
  obtain ⟨α', hint, hL⟩ :=
    reduction_liouvilleWith halg (liouvilleWith_of_approxSet_infinite hα hinf)
  exact ⟨α', (κ + 2) / 2, hL.irrational (by linarith), hint, by linarith,
    approxSet_infinite_of_liouvilleWith hL (by linarith)⟩

/-- (3) Reference use of the project lemma. -/
example {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hκ : 2 < κ)
    (hinf : (Roth.approxSet α κ).Infinite) : ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧
    2 < κ' ∧ (Roth.approxSet α' κ').Infinite :=
  Roth.reduction hα halg hκ hinf
