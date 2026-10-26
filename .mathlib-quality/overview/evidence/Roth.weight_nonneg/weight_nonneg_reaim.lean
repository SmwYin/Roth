import Roth.Box

/-! Evidence for `Roth.weight_nonneg` (overview mathlibable assessment), re-aimed at
mathlib's `Finsupp.weight` (the parent `Roth.weight` is `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`). -/

namespace Roth.Evidence

/-- (1) Re-aimed general form: nonnegativity of `Finsupp.weight` for nonnegative weights,
in any ordered additive monoid, with no `Fintype`. One mathlib composition. -/
theorem finsupp_weight_nonneg {σ M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {w : σ → M} (hw : ∀ i, 0 ≤ w i) (f : σ →₀ ℕ) :
    0 ≤ Finsupp.weight w f :=
  Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _

/-- (2) Canonically ordered codomain: it is just `zero_le`. -/
example {σ M : Type*} [AddCommMonoid M] [PartialOrder M] [CanonicallyOrderedAdd M]
    (w : σ → M) (f : σ →₀ ℕ) : 0 ≤ Finsupp.weight w f :=
  zero_le

/-- (3) The project lemma from the re-aimed form via the parent bridge. -/
example {σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ Roth.weight r d := by
  have : Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
    simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]
  exact this ▸ finsupp_weight_nonneg (fun j ↦ by positivity) d

/-- (4) The current project proof is itself a one-call composition. -/
example {σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ Roth.weight r d :=
  Fintype.sum_nonneg fun _ ↦ by positivity

/- (5) Weakening probe: `[Fintype σ]` cannot be dropped from the project form, since
`Roth.weight` itself requires it (sum over `univ`). Nothing else to weaken (no hypotheses). -/

end Roth.Evidence
