import Roth.Box

/-! Evidence for the `Roth.weight_mul_left` mathlibable assessment. -/

open Finsupp

variable {σ : Type*} [Fintype σ]

/-! (1) Re-aimed general form: `Finsupp.weight` is linear in the weight vector,
`weight (c • w) f = c • weight w f`. Not in mathlib as a named lemma; one `simp`. -/
omit [Fintype σ] in
theorem finsupp_weight_smul {R S M : Type*} [Semiring R] [AddCommMonoid M] [Module R M]
    [Monoid S] [DistribMulAction S M] [SMulCommClass R S M]
    (c : S) (w : σ → M) (f : σ →₀ R) :
    Finsupp.weight (c • w) f = c • Finsupp.weight w f := by
  simp [weight_apply, Finsupp.smul_sum, smul_comm]

/-! (2) Project lemma from the re-aimed form via the parent's bridge
`Roth.weight r = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`. -/
example {l : ℕ} (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / l := by
  have h : ∀ r : σ → ℕ, Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
    intro r; simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]
  have hw : (fun j ↦ (((l * r j : ℕ) : ℝ))⁻¹) = (l : ℝ)⁻¹ • fun j ↦ ((r j : ℝ))⁻¹ := by
    ext j; simp [mul_comm]
  rw [h, h, hw, finsupp_weight_smul, smul_eq_mul, div_eq_inv_mul]

/-! (3) Project lemma directly as a big-operators composition (`Finset.sum_div`). -/
example {l : ℕ} (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / l := by
  simp only [Roth.weight, Finset.sum_div, div_div, Nat.cast_mul, mul_comm]

/-! (4) Edge case `l = 0`: both sides are `0` (Lean's `x / 0 = 0`), so no hypothesis
`0 < l` is needed; the lemma is already maximally general in `l`. -/
example (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight (fun j ↦ 0 * r j) d = Roth.weight r d / (0 : ℕ) :=
  Roth.weight_mul_left r d
