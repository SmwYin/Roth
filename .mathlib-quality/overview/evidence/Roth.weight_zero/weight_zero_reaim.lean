import Roth.Box

/-! Evidence for `Roth.weight_zero` (overview mathlibable assessment, re-aimed at
`Finsupp.weight`). -/

namespace Roth.Evidence

variable {σ : Type*} [Fintype σ]

/-- (1) Re-aimed form: mathlib already has `Finsupp.weight w 0 = 0` as `map_zero`
(`Finsupp.weight w` is an `AddMonoidHom`), for any semiring `R` and module `M`. -/
example {τ R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M] (w : τ → M) :
    Finsupp.weight w (0 : τ →₀ R) = 0 :=
  map_zero _

/-- (2) `simp` closes the re-aimed form with no extra lemmas. -/
example {τ M : Type*} [AddCommMonoid M] (w : τ → M) : Finsupp.weight w (0 : τ →₀ ℕ) = 0 := by
  simp

/-- (3) Project lemma recovered through the parent bridge `weight = Finsupp.weight (r ·)⁻¹`. -/
example (r : σ → ℕ) : Roth.weight r 0 = 0 := by
  have : Roth.weight r 0 = Finsupp.weight (R := ℕ) (fun j ↦ ((r j : ℝ))⁻¹) 0 := by
    simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]
  rw [this, map_zero]

/-- (4) Current proof (unfolding + `simp`). -/
example (r : σ → ℕ) : Roth.weight r 0 = 0 := by
  simp [Roth.weight]

/-- (5) `[Fintype σ]` is superfluous for the statement once stated via `Finsupp.weight`;
for the project def it is needed only for `Roth.weight` to typecheck. -/
example {τ : Type*} (r : τ → ℕ) : Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) (0 : τ →₀ ℕ) = 0 :=
  map_zero _

end Roth.Evidence
