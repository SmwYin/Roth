import Roth.Box

open Finsupp

variable {σ τ : Type*}

-- (1) Re-aimed form: Finsupp.weight commutes with mapDomain, NO injectivity, general R, M.
--     Direct instance of mathlib's Finsupp.linearCombination_mapDomain.
example {R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M] (w : τ → M) (f : σ → τ)
    (d : σ →₀ R) : Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d :=
  Finsupp.linearCombination_mapDomain (R := R) (v' := w) f d

-- (1') same, closed by simp (linearCombination_mapDomain is @[simp]).
example {R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M] (w : τ → M) (f : σ → τ)
    (d : σ →₀ R) : Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d := by
  simp [Finsupp.weight]

variable [Fintype σ] [Fintype τ]

-- (2) Parent bridge.
theorem bridge {ι : Type*} [Fintype ι] (r : ι → ℕ) (d : ι →₀ ℕ) :
    Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
  simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]

-- (3) Project lemma WITHOUT the injectivity hypothesis, via bridge + linearCombination_mapDomain.
theorem weight_mapDomain' (f : σ → τ) (r : τ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d := by
  rw [bridge, bridge]
  exact Finsupp.linearCombination_mapDomain (R := ℕ) f d

-- (4) Project lemma WITHOUT injectivity, directly via sum_mapDomain_index (no bridge).
example (f : σ → τ) (r : τ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d := by
  simpa [Finsupp.sum_fintype, Roth.weight, add_div] using
    Finsupp.sum_mapDomain_index (s := d) (h := fun j n ↦ (n : ℝ) / r j)
      (fun _ ↦ by simp) (fun _ _ _ ↦ by push_cast; ring)

-- (5) Current (injective) proof still works.
example {f : σ → τ} (hf : Function.Injective f) (r : τ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d := by
  simpa [Finsupp.sum_fintype, Roth.weight] using
    Finsupp.sum_mapDomain_index_inj (s := d) (h := fun j n ↦ (n : ℝ) / r j) hf

-- (6) Non-injective sanity instance: f : Fin 2 → Unit collapses both coordinates.
example (r : Unit → ℕ) (d : Fin 2 →₀ ℕ) :
    Roth.weight r (d.mapDomain fun _ ↦ ()) = Roth.weight (r ∘ fun _ ↦ ()) d :=
  weight_mapDomain' _ r d
