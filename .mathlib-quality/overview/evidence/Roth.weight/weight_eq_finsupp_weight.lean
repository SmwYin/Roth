import Roth.Box

/-! Evidence for `Roth.weight` (overview mathlibable assessment). -/

open Finset

namespace Roth.Evidence

variable {σ : Type*} [Fintype σ]

/-- (1) `Roth.weight r` is mathlib's `Finsupp.weight` with real weights `(r j)⁻¹`
(holds for all `r`, including `r j = 0`, since `x / 0 = 0 = x * 0⁻¹`). -/
theorem weight_eq_finsupp_weight (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
  simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]

/-- (2) The project API lemmas then follow from mathlib's `AddMonoidHom` API. -/
example (r : σ → ℕ) (d e : σ →₀ ℕ) : Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e := by
  simp only [weight_eq_finsupp_weight, map_add]

example (r : σ → ℕ) : Roth.weight r 0 = 0 := by
  simp only [weight_eq_finsupp_weight, map_zero]

example [DecidableEq σ] (r : σ → ℕ) (j : σ) (n : ℕ) :
    Roth.weight r (Finsupp.single j n) = n / r j := by
  rw [weight_eq_finsupp_weight, Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]

/-- (3) Generalised form: any coefficient semiring and any weight vector is already
`Finsupp.weight`; nothing new is needed. -/
example {R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M] (w : σ → M) (f : σ →₀ R) :
    Finsupp.weight w f = ∑ i, f i • w i :=
  Finsupp.weight_eq_sum w f

end Roth.Evidence
