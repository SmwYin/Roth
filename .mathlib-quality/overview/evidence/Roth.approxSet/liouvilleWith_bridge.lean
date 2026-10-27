import Roth.Main
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

/-! Evidence for the `/overview` assessment of `Roth.approxSet`: the infinitude of
`approxSet α κ` is interchangeable with mathlib's `LiouvilleWith`, so Roth's theorem can be
stated as `∀ p > 2, ¬ LiouvilleWith p α` without the project-local set. -/

open Filter

/-- `approxSet` is the image of mathlib-style rationals `{x : ℚ | |α - x| < 1 / x.den ^ κ}` plus
non-reduced pairs; membership unfolds by `Iff.rfl`. -/
example (α κ : ℝ) (h : ℤ) (q : ℕ) :
    (h, q) ∈ Roth.approxSet α κ ↔ 0 < q ∧ |α - h / q| < 1 / (q : ℝ) ^ κ := Iff.rfl

/-- `LiouvilleWith p α` gives infinitely many approximations of every quality `q < p`. -/
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

/-- Conversely, for irrational `α`, infinitely many approximations of quality `κ` give
`LiouvilleWith κ α` (with constant `1`). -/
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

/-- Hence `Roth.roth` is equivalent (for irrational `α`) to the `LiouvilleWith` phrasing. -/
theorem roth_iff_not_liouvilleWith {α : ℝ} (hα : Irrational α) :
    (∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite → κ ≤ 2) ↔ ∀ p > 2, ¬ LiouvilleWith p α := by
  refine ⟨fun h p hp hL ↦ ?_, fun h κ hinf ↦ le_of_not_gt fun hκ ↦
    h κ hκ (liouvilleWith_of_approxSet_infinite hα hinf)⟩
  have := h (approxSet_infinite_of_liouvilleWith hL (by linarith : (p + 2) / 2 < p))
  linarith

/-- Roth's theorem in mathlib's vocabulary, as a one-line corollary of `Roth.roth`. -/
theorem roth_not_liouvilleWith {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {p : ℝ}
    (hp : 2 < p) : ¬ LiouvilleWith p α :=
  (roth_iff_not_liouvilleWith hα).1 (Roth.roth hα halg) p hp
