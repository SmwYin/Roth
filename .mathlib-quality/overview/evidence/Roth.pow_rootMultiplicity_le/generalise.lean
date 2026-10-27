import Mathlib.RingTheory.Polynomial.GaussLemma
import Mathlib.RingTheory.Polynomial.RationalRoot
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Positivity

/-! Evidence for `Roth.pow_rootMultiplicity_le` (Roth/Theta.lean:206).

(0) Parent lemma (copied from the evidence of `Roth.exists_eq_pow_mul_of_rootMultiplicity`).
(1) General divisibility form: `q ^ mult ∣ leadingCoeff p` over any normalized-GCD domain,
    with `IsRelPrime`, `q ≠ 0`, and no `p ≠ 0` hypothesis.
(2) UFD `num`/`den` form: multiplicity strengthening of `den_dvd_of_is_root`.
(3) The project statement (real bound) recovered from (1). -/

open Polynomial

namespace Evidence

theorem isPrimitive_C_mul_X_sub_C {R : Type*} [CommRing R] {h q : R} (hcop : IsRelPrime h q) :
    (C q * X - C h).IsPrimitive := by
  intro c hc
  rw [C_dvd_iff_dvd_coeff] at hc
  exact hcop (by simpa using hc 0) (by simpa using hc 1)

theorem pow_rootMultiplicity_dvd_of_isRelPrime {R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] (p : R[X]) {h q : R}
    (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    (C q * X - C h) ^ rootMultiplicity (algebraMap R K h / algebraMap R K q)
      (p.map (algebraMap R K)) ∣ p := by
  have hq' : algebraMap R K q ≠ 0 :=
    (map_ne_zero_iff _ (IsFractionRing.injective R K)).2 hq
  have hprim : ∀ t : ℕ, ((C q * X - C h) ^ t).IsPrimitive := fun t ↦
    Nat.rec isPrimitive_one (fun t ih ↦ by
      simpa [pow_succ] using ih.mul (isPrimitive_C_mul_X_sub_C hcop)) t
  apply (hprim _).dvd_of_fraction_map_dvd_fraction_map (K := K)
  have hmap : (C q * X - C h).map (algebraMap R K) =
      C (algebraMap R K q) * (X - C (algebraMap R K h / algebraMap R K q)) := by
    simp [mul_sub, ← C_mul, mul_div_cancel₀ _ hq']
  rw [Polynomial.map_pow, hmap, mul_pow, ← C_pow, C_mul_dvd (pow_ne_zero _ hq')]
  exact pow_rootMultiplicity_dvd _ _

/-- (1) General form: `q ^ mult ∣ leadingCoeff p`. -/
theorem pow_rootMultiplicity_dvd_leadingCoeff {R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] (p : R[X]) {h q : R}
    (hq : q ≠ 0) (hcop : IsRelPrime h q) :
    q ^ rootMultiplicity (algebraMap R K h / algebraMap R K q)
      (p.map (algebraMap R K)) ∣ p.leadingCoeff := by
  obtain ⟨Q, hQ⟩ := pow_rootMultiplicity_dvd_of_isRelPrime (K := K) p hq hcop
  generalize rootMultiplicity (algebraMap R K h / algebraMap R K q)
    (p.map (algebraMap R K)) = t at hQ ⊢
  refine ⟨Q.leadingCoeff, ?_⟩
  rw [hQ, leadingCoeff_mul, leadingCoeff_pow, sub_eq_add_neg, ← C_neg,
    leadingCoeff_linear hq]

/-- (2) UFD form, multiplicity strengthening of `den_dvd_of_is_root`. -/
example {A K : Type*} [CommRing A] [IsDomain A] [UniqueFactorizationMonoid A]
    [NormalizedGCDMonoid A] [Field K] [Algebra A K] [IsFractionRing A K] (p : A[X]) (r : K) :
    (IsFractionRing.den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K)) ∣
      p.leadingCoeff := by
  simpa [IsFractionRing.mk'_num_den'] using
    pow_rootMultiplicity_dvd_leadingCoeff (K := K) p
      (nonZeroDivisors.coe_ne_zero _) (IsFractionRing.num_den_reduced A r)

/-- (3) The project statement recovered from (1). -/
example {R : Polynomial ℤ} (hR : R ≠ 0) {h : ℤ} {q : ℕ} (hq : 0 < q)
    (hcop : IsCoprime h (q : ℤ)) {B : ℝ} (hB : |(R.leadingCoeff : ℝ)| ≤ B) :
    (q : ℝ) ^ Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) ≤ B := by
  have hd := pow_rootMultiplicity_dvd_leadingCoeff (K := ℚ) R (q := (q : ℤ))
    (by exact_mod_cast hq.ne') hcop.isRelPrime
  simp only [algebraMap_int_eq, eq_intCast, Int.cast_natCast] at hd
  have hle := Int.le_of_dvd (abs_pos.2 (leadingCoeff_ne_zero.2 hR)) ((dvd_abs _ _).2 hd)
  refine le_trans ?_ hB
  rw [← Int.cast_abs]
  exact_mod_cast hle

end Evidence
