import Roth.CoeffNorm

/-! Evidence for `Roth.geom_sum_le_one_add_pow`. -/

/-- Weakening 1: any ordered commutative semiring (the proof is unchanged up to casts). -/
theorem geom_sum_le_one_add_pow' {R : Type*} [CommSemiring R] [PartialOrder R] [IsOrderedRing R]
    {t : R} (ht : 0 ≤ t) (r : ℕ) :
    ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r := by
  rw [add_comm (1 : R) t, add_pow]
  refine Finset.sum_le_sum fun m hm ↦ ?_
  rw [one_pow, mul_one]
  refine le_mul_of_one_le_right (pow_nonneg ht m) ?_
  simpa using Nat.mono_cast (α := R) (Nat.choose_pos (Finset.mem_range_succ_iff.1 hm))

/-- Weakening 2: `Semiring` (non-commutative) works too, via `(Commute.one_right t).add_pow`. -/
theorem geom_sum_le_one_add_pow'' {R : Type*} [Semiring R] [PartialOrder R] [IsOrderedRing R]
    {t : R} (ht : 0 ≤ t) (r : ℕ) :
    ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r := by
  rw [add_comm (1 : R) t, (Commute.one_right t).add_pow]
  refine Finset.sum_le_sum fun m hm ↦ ?_
  rw [one_pow, mul_one]
  refine le_mul_of_one_le_right (pow_nonneg ht m) ?_
  simpa using Nat.mono_cast (α := R) (Nat.choose_pos (Finset.mem_range_succ_iff.1 hm))

/-- The project statement is a one-line specialisation of the general form. -/
example {t : ℝ} (ht : 0 ≤ t) (r : ℕ) :
    ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r :=
  geom_sum_le_one_add_pow'' ht r

/-- `0 ≤ t` is needed: t = -1/2, r = 2 gives 3/4 ≤ 1/4. -/
example : ¬ (∑ s ∈ Finset.range (2 + 1), (-1/2 : ℝ) ^ s ≤ (1 + (-1/2 : ℝ)) ^ 2) := by
  norm_num [Finset.sum_range_succ]
