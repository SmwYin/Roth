import Mathlib.RingTheory.Polynomial.GaussLemma
import Mathlib.RingTheory.Polynomial.RationalRoot

/-! Evidence for `Roth.exists_eq_pow_mul_of_rootMultiplicity` (Roth/Theta.lean:184).

(1) Generalisation from `ℤ ⊆ ℚ` to any normalized-GCD domain `R` with fraction field `K`,
    `IsCoprime` weakened to `IsRelPrime`, `0 < q` to `q ≠ 0`, `∃ Q, p = _ * Q` to `_ ∣ p`.
(2) The UFD `num`/`den` form (rational root theorem style).
(3) The project statement recovered as a corollary. -/

open Polynomial

namespace Evidence

/-- `C q * X - C h` is primitive when `h`, `q` are relatively prime (any comm ring). -/
theorem isPrimitive_C_mul_X_sub_C {R : Type*} [CommRing R] {h q : R} (hcop : IsRelPrime h q) :
    (C q * X - C h).IsPrimitive := by
  intro c hc
  rw [C_dvd_iff_dvd_coeff] at hc
  exact hcop (by simpa using hc 0) (by simpa using hc 1)

/-- (1) General form over a GCD domain. -/
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

/-- (2) UFD form with `IsFractionRing.num` / `den`. -/
example {A K : Type*} [CommRing A] [IsDomain A] [UniqueFactorizationMonoid A]
    [NormalizedGCDMonoid A] [Field K] [Algebra A K] [IsFractionRing A K] (p : A[X]) (r : K) :
    (C (IsFractionRing.den A r : A) * X - C (IsFractionRing.num A r)) ^
      rootMultiplicity r (p.map (algebraMap A K)) ∣ p := by
  simpa [IsFractionRing.mk'_num_den'] using
    pow_rootMultiplicity_dvd_of_isRelPrime (K := K) p
      (nonZeroDivisors.coe_ne_zero _) (IsFractionRing.num_den_reduced A r)

/-- (3) The project statement as a corollary of (1). -/
example {R : Polynomial ℤ} {h : ℤ} {q : ℕ} (hq : 0 < q)
    (hcop : IsCoprime h (q : ℤ)) : ∃ Q : Polynomial ℤ, R =
      (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h) ^
      Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) * Q := by
  have := pow_rootMultiplicity_dvd_of_isRelPrime (K := ℚ) R (q := (q : ℤ))
    (by exact_mod_cast hq.ne') hcop.isRelPrime
  simp only [algebraMap_int_eq, eq_intCast, Int.cast_natCast] at this
  exact this

end Evidence
