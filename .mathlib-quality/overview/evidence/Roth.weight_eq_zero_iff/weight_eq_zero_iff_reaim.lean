import Roth.Box

/-! Evidence for `Roth.weight_eq_zero_iff` (overview mathlibable assessment), re-aimed at
mathlib's `Finsupp.weight` (the parent `Roth.weight` is `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`).
Mathlib's `Finsupp.weight_eq_zero_iff_eq_zero` needs `[CanonicallyOrderedAdd M]`, which `ℝ`
is not, so it does not apply directly. -/

namespace Roth.Evidence

/-- (1) Re-aimed general form: in any ordered additive monoid, with strictly positive weights,
`weight w f = 0 ↔ f = 0`. No `Fintype`, no canonical order. -/
theorem finsupp_weight_eq_zero_iff_of_pos {σ M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {w : σ → M} (hw : ∀ i, 0 < w i) {f : σ →₀ ℕ} :
    Finsupp.weight w f = 0 ↔ f = 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ h ▸ map_zero _⟩
  by_contra hf
  obtain ⟨s, hs⟩ := Finsupp.ne_iff.1 hf
  exact (hw s).not_ge (h ▸ Finsupp.le_weight_of_ne_zero (fun i ↦ (hw i).le) hs)

/-- (2) Mathlib's canonical-order lemma is a corollary of (1): `NonTorsionWeight ℕ w` gives
`w s ≠ 0`, i.e. `0 < w s` in a canonically ordered monoid. -/
example {σ M : Type*} [AddCommMonoid M] [PartialOrder M] [IsOrderedAddMonoid M]
    [CanonicallyOrderedAdd M] (w : σ → M) [Finsupp.NonTorsionWeight ℕ w] {f : σ →₀ ℕ} :
    Finsupp.weight w f = 0 ↔ f = 0 :=
  finsupp_weight_eq_zero_iff_of_pos fun s ↦
    pos_iff_ne_zero.2 (Finsupp.NonTorsionWeight.ne_zero ℕ w s)

/-- (3) The project lemma from (1) via the parent bridge. -/
example {σ : Type*} [Fintype σ] {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} :
    Roth.weight r d = 0 ↔ d = 0 := by
  have : Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
    simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]
  rw [this]
  exact finsupp_weight_eq_zero_iff_of_pos fun j ↦ by have := hr j; positivity

/-- (4) Current project proof (one `simp` call). -/
example {σ : Type*} [Fintype σ] {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} :
    Roth.weight r d = 0 ↔ d = 0 := by
  simp [Roth.weight, Finset.sum_eq_zero_iff_of_nonneg, div_nonneg, (hr _).ne', Finsupp.ext_iff]

/-- (5) Weakening probe: `hr` cannot be dropped (counterexample with `r = 0`). -/
example : ¬ ∀ (r : Unit → ℕ) (d : Unit →₀ ℕ), Roth.weight r d = 0 ↔ d = 0 := by
  intro h
  have := (h (fun _ ↦ 0) (Finsupp.single () 1)).1 (by simp [Roth.weight])
  simp at this

end Roth.Evidence
