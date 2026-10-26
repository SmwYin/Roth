import Roth.Box

open Finsupp

variable {σ : Type*}

-- (1) Re-aimed form: mathlib's Finsupp.weight_single, general R, M.
example {R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M] (w : σ → M) (s : σ) (c : R) :
    Finsupp.weight w (Finsupp.single s c) = c • w s :=
  Finsupp.weight_single w s c

-- (2) Re-aimed form specialised to the project weight vector (no Fintype needed).
example (r : σ → ℕ) (j : σ) (n : ℕ) :
    Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) (Finsupp.single j n) = n / r j := by
  rw [Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]

variable [Fintype σ]

-- (3) Parent bridge.
theorem bridge (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
  simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]

-- (4) Project lemma via bridge + Finsupp.weight_single.
example (r : σ → ℕ) (j : σ) (n : ℕ) : Roth.weight r (Finsupp.single j n) = n / r j := by
  rw [bridge, Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]

-- (5) Current proof still works (sanity).
example (r : σ → ℕ) (j : σ) (n : ℕ) : Roth.weight r (Finsupp.single j n) = n / r j := by
  classical
  simp [Roth.weight, Finsupp.single_apply, ite_div]
