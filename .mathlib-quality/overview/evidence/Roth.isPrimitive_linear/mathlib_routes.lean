import Mathlib.RingTheory.Polynomial.Content
import Mathlib.Algebra.Polynomial.RingDivision

/-! Evidence for `Roth.isPrimitive_linear` (Roth/Theta.lean:167).
1. The project statement, re-proved verbatim (sanity).
2. Generalisation to any commutative ring (same proof shape).
3. Mathlib-composition route via `irreducible_C_mul_X_add_C` + `Irreducible.isPrimitive`;
   it needs the extra hypothesis `q ≠ 0`, which the project lemma does not need. -/

open Polynomial

-- 1. project statement
example {h : ℤ} {q : ℕ} (hcop : IsCoprime h (q : ℤ)) :
    (C (q : ℤ) * X - C h).IsPrimitive := by
  intro c hc
  rw [C_dvd_iff_dvd_coeff] at hc
  exact hcop.isUnit_of_dvd' (by simpa using hc 0)
    (by simpa only [coeff_sub, coeff_C_mul, coeff_X_one, coeff_C, mul_one, one_ne_zero,
      ↓reduceIte, sub_zero] using hc 1)

-- 2. general commutative ring
example {R : Type*} [CommRing R] {a b : R} (hab : IsCoprime a b) :
    (C a * X + C b).IsPrimitive := by
  intro c hc
  rw [C_dvd_iff_dvd_coeff] at hc
  exact hab.isUnit_of_dvd' (by simpa using hc 1) (by simpa using hc 0)

-- 3. composition from mathlib (needs q ≠ 0)
example {h : ℤ} {q : ℕ} (hq : q ≠ 0) (hcop : IsCoprime h (q : ℤ)) :
    (C (q : ℤ) * X - C h).IsPrimitive := by
  rw [sub_eq_add_neg, ← C_neg]
  refine (irreducible_C_mul_X_add_C (by exact_mod_cast hq)
    (hcop.symm.neg_right).isRelPrime).isPrimitive ?_
  rw [natDegree_linear (by exact_mod_cast hq)]; exact one_ne_zero
