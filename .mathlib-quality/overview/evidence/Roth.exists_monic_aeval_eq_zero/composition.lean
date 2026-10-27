import Roth.Main

open Polynomial

/-! Evidence for `Roth.exists_monic_aeval_eq_zero`. -/

-- (1) Composition from `minpoly` (one anonymous constructor of mathlib lemmas).
example {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : ℤ[X], f.Monic ∧ aeval α f = 0 ∧ 2 ≤ f.natDegree :=
  ⟨minpoly ℤ α * X ^ 2, (minpoly.monic hint).mul (monic_X_pow 2), by simp,
    by simp [(minpoly.monic hint).ne_zero]⟩

-- (2) Weakening: any nontrivial commutative ring `R`, any `R`-algebra `A`, any degree bound `n`.
theorem exists_monic_aeval_eq_zero_le_natDegree {R A : Type*} [CommRing R] [Nontrivial R]
    [Ring A] [Algebra R A] {x : A} (hx : IsIntegral R x) (n : ℕ) :
    ∃ f : R[X], f.Monic ∧ aeval x f = 0 ∧ n ≤ f.natDegree := by
  obtain ⟨f, hf, hf0⟩ := hx
  refine ⟨f * X ^ n, hf.mul (monic_X_pow n), ?_, ?_⟩
  · rw [map_mul, aeval_def, hf0, zero_mul]
  · simp [hf.ne_zero]

-- (3) The project lemma is the specialisation R = ℤ, A = ℝ, n = 2.
example {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : ℤ[X], f.Monic ∧ aeval α f = 0 ∧ 2 ≤ f.natDegree :=
  exists_monic_aeval_eq_zero_le_natDegree hint 2

-- (4) Reference use of the project lemma.
example {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : ℤ[X], f.Monic ∧ aeval α f = 0 ∧ 2 ≤ f.natDegree :=
  Roth.exists_monic_aeval_eq_zero hint
