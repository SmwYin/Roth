import Roth.Theta

open Roth

-- (1) Composition: four `one_le_pow₀`/cast facts glued by three `one_le_mul_of_one_le_of_one_le`.
example (p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) : 1 ≤ lem6M p r₁ B l := by
  unfold lem6M
  have h1 : (1 : ℝ) ≤ ((r₁ : ℝ) + 1) ^ (p * l) := one_le_pow₀ (by simp)
  have h2 : (1 : ℝ) ≤ (l.factorial : ℝ) := by exact_mod_cast Nat.one_le_iff_ne_zero.2 l.factorial_ne_zero
  have h3 : (1 : ℝ) ≤ B ^ l := one_le_pow₀ hB
  have h4 : (1 : ℝ) ≤ 2 ^ (p * l * r₁) := one_le_pow₀ (by norm_num)
  exact one_le_mul_of_one_le_of_one_le
    (one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le h1 h2) h3) h4

-- (2) Hypothesis `1 ≤ B` cannot be dropped: B = 0, l = 1 gives lem6M = 0.
example : ¬ (1 ≤ lem6M 1 0 0 1) := by norm_num [lem6M]

-- (3) Nor weakened to `0 < B`: B = 1/2, p = r₁ = 0, l = 1 gives 1/2.
example : ¬ (1 ≤ lem6M 0 0 (1/2) 1) := by norm_num [lem6M]

-- (4) For `l = 0` no hypothesis on B is needed.
example (p r₁ : ℕ) (B : ℝ) : lem6M p r₁ B 0 = 1 := by simp [lem6M]
