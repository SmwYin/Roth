import Roth.Index

open Roth

variable {σ : Type*} [Fintype σ]

-- (1) composition attempt: unfold to sums, then a per-term field identity
example {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) :
    weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i := by
  have hD : (∏ i, (r i : ℝ)) ≠ 0 := Finset.prod_ne_zero_iff.2 fun i _ ↦ by exact_mod_cast (hr i).ne'
  simp only [weight, Finsupp.weight_eq_sum, smul_eq_mul, Nat.cast_sum, Nat.cast_mul, Finset.sum_div,
    Nat.cast_prod]
  refine Finset.sum_congr rfl fun j _ ↦ ?_
  rw [Nat.cast_div_charZero (Finset.dvd_prod_of_mem _ (Finset.mem_univ j)), Nat.cast_prod]
  have : (r j : ℝ) ≠ 0 := by exact_mod_cast (hr j).ne'
  field_simp

-- (2) generalisation: any nonzero common multiple `D` of the `r j`, not just the product
theorem weight_eq_finsuppWeight_div_of_dvd {r : σ → ℕ} {D : ℕ} (hD : D ≠ 0) (hr : ∀ j, r j ∣ D)
    (d : σ →₀ ℕ) : weight r d = (Finsupp.weight (fun j ↦ D / r j) d : ℝ) / D := by
  simp only [weight, Finsupp.weight_eq_sum, smul_eq_mul, Nat.cast_sum, Nat.cast_mul, Finset.sum_div]
  refine Finset.sum_congr rfl fun j _ ↦ ?_
  rw [Nat.cast_div_charZero (hr j)]
  have hrj : (r j : ℝ) ≠ 0 := by
    exact_mod_cast fun h : r j = 0 ↦ hD (Nat.eq_zero_of_zero_dvd (h ▸ hr j))
  have : (D : ℝ) ≠ 0 := by exact_mod_cast hD
  field_simp

-- the project statement is the special case D = ∏ r_i
example {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) :
    weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i := by
  have := weight_eq_finsuppWeight_div_of_dvd (D := ∏ i, r i)
    (Finset.prod_ne_zero_iff.2 fun i _ ↦ (hr i).ne') (fun j ↦ Finset.dvd_prod_of_mem _ (Finset.mem_univ j)) d
  simpa using this

-- (3) `hr` is necessary: r = (0, 1), d = single 1 1 gives LHS = 1, RHS = 0
example : ¬ (weight (σ := Fin 2) ![0, 1] (Finsupp.single 1 1) =
    (Finsupp.weight (fun j ↦ (∏ i, (![0, 1] : Fin 2 → ℕ) i) / (![0, 1] : Fin 2 → ℕ) j)
      (Finsupp.single (1 : Fin 2) 1) : ℝ) / ∏ i, (![0, 1] : Fin 2 → ℕ) i) := by
  simp [weight_single]

-- (4) re-aim at the parent's mathlib form: Roth.weight r = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)
example {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) :
    Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d =
      (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i := by
  rw [← weight_eq_finsuppWeight_div hr, weight, Finsupp.weight_eq_sum]
  simp [div_eq_mul_inv]
