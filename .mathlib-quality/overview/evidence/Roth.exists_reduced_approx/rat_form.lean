import Roth.Main

/-! Evidence for `Roth.exists_reduced_approx`: its content is the equivalence between the
unreduced pair set `approxSet α κ` and the set of rationals `x` with `|α - x| < 1 / x.den ^ κ`
(irrational `α`, `κ > 0`). -/

open Roth

/-- Forward direction: from `exists_reduced_approx`, the rational set is infinite. -/
theorem rat_set_infinite_of_approxSet {α κ : ℝ} (hα : Irrational α) (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) :
    {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite := by
  intro hfin
  obtain ⟨Q₀, hQ₀⟩ := (hfin.image Rat.den).bddAbove
  obtain ⟨⟨h, q⟩, hmem, hlt, hcop⟩ := exists_reduced_approx hα hκ hinf Q₀
  have hq : 0 < q := hmem.1
  have hden : ((h : ℚ) / q).den = q := by
    have := Rat.den_div_eq_of_coprime (a := h) (b := (q : ℤ)) (by exact_mod_cast hq)
      (Int.isCoprime_iff_gcd_eq_one.1 hcop)
    exact_mod_cast this
  refine absurd (hQ₀ ⟨(h : ℚ) / q, ?_, hden⟩) (not_le.2 hlt)
  change |α - (((h : ℚ) / q : ℚ) : ℝ)| < 1 / ((((h : ℚ) / q).den : ℕ) : ℝ) ^ κ
  rw [hden]
  push_cast
  exact hmem.2

/-- Backward direction (the argument of `Roth.roth_rat`, no hypotheses). -/
theorem approxSet_infinite_of_rat_set {α κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : (approxSet α κ).Infinite := by
  refine (hinf.image (f := fun x : ℚ ↦ (x.num, x.den))
    (fun _ _ _ _ hxy ↦ Rat.ext (congrArg Prod.fst hxy) (congrArg Prod.snd hxy))).mono ?_
  rintro _ ⟨x, hx, rfl⟩
  exact ⟨x.den_pos, by rwa [← Rat.cast_def]⟩

/-- The equivalence that would be the mathlib-facing content. -/
theorem approxSet_infinite_iff_rat {α κ : ℝ} (hα : Irrational α) (hκ : 0 < κ) :
    (approxSet α κ).Infinite ↔ {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite :=
  ⟨rat_set_infinite_of_approxSet hα hκ, approxSet_infinite_of_rat_set⟩
