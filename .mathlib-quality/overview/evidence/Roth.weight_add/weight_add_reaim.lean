import Roth.Box

/-! Evidence for `Roth.weight_add` (overview mathlibable assessment, re-aimed at
`Finsupp.weight`). -/

namespace Roth.Evidence

variable {σ : Type*} [Fintype σ]

/-- (1) Re-aimed form: mathlib already has additivity of `Finsupp.weight w` as `map_add`
(`Finsupp.weight w` is an `AddMonoidHom`), for any semiring `R` and module `M`. -/
example {τ R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M] (w : τ → M)
    (d e : τ →₀ R) : Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e :=
  map_add _ d e

/-- (2) `simp` closes the re-aimed form with no extra lemmas (`map_add` is simp). -/
example {τ M : Type*} [AddCommMonoid M] (w : τ → M) (d e : τ →₀ ℕ) :
    Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e := by
  simp

/-- (3) Project lemma recovered through the parent bridge `weight = Finsupp.weight (r ·)⁻¹`
plus `map_add`. -/
example (r : σ → ℕ) (d e : σ →₀ ℕ) :
    Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e := by
  have h : ∀ f : σ →₀ ℕ, Roth.weight r f = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) f := by
    intro f; simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]
  rw [h, h, h, map_add]

/-- (4) Current proof (unfolding + `simp`). -/
example (r : σ → ℕ) (d e : σ →₀ ℕ) :
    Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e := by
  simp [Roth.weight, add_div, Finset.sum_add_distrib]

/-- (5) `[Fintype σ]` is superfluous for the re-aimed statement. -/
example {τ : Type*} (r : τ → ℕ) (d e : τ →₀ ℕ) :
    Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) (d + e) =
      Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d + Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) e :=
  map_add _ d e

end Roth.Evidence
