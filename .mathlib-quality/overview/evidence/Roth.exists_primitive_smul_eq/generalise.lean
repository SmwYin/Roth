import Roth.Separation
import Mathlib.RingTheory.MvPolynomial.Localization
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.RingTheory.Localization.Integral
import Mathlib.RingTheory.Polynomial.Content

open MvPolynomial

-- (0) signature
#check @Roth.exists_primitive_smul_eq
-- univariate mathlib analogues
#check @Polynomial.eq_C_content_mul_primPart
#check @Polynomial.isPrimitive_primPart
#check @IsLocalization.integerNormalization_spec

-- (1) Clearing denominators for an arbitrary localization (from the
-- Roth.exists_nat_smul_eq_map assessment, evidence (2) there).
theorem exists_smul_eq_map_of_isLocalization {σ R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] (M : Submonoid R) [IsLocalization M S] (G : MvPolynomial σ S) :
    ∃ b ∈ M, ∃ U : MvPolynomial σ R, map (algebraMap R S) U = (b : R) • G := by
  classical
  obtain ⟨b, hb⟩ := IsLocalization.exist_integer_multiples M G.support G.coeff
  refine ⟨b, b.2, ?_⟩
  have hmem : (b : R) • G ∈ Set.range (map (algebraMap R S)) := by
    rw [mem_range_map_iff_coeffs_subset]
    intro q hq
    simp only [Finset.mem_coe, coeffs, Finset.mem_image] at hq
    obtain ⟨d, hd, rfl⟩ := hq
    rw [coeff_smul]
    exact hb d (support_smul hd)
  exact hmem

-- (2) Content / primitive-part decomposition for MvPolynomial over a GCD monoid
-- (MvPolynomial analogue of `Polynomial.eq_C_content_mul_primPart` + `isPrimitive_primPart`).
theorem exists_eq_C_gcd_mul {σ R : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    {P : MvPolynomial σ R} (hP : P ≠ 0) :
    ∃ U : MvPolynomial σ R, P = C (P.support.gcd P.coeff) * U ∧
      U.support.gcd U.coeff = 1 := by
  classical
  have hne : P.support.Nonempty := support_nonempty.mpr hP
  obtain ⟨g', hg', hg1⟩ := Finset.extract_gcd P.coeff hne
  have hg0 : P.support.gcd P.coeff ≠ 0 := by
    obtain ⟨d, hd⟩ := hne
    rw [Ne, Finset.gcd_eq_zero_iff]
    exact fun h ↦ mem_support_iff.1 hd (h d hd)
  set U := ∑ d ∈ P.support, monomial d (g' d) with hUdef
  have hUcoeff : ∀ d, U.coeff d = if d ∈ P.support then g' d else 0 := by
    simp [hUdef, coeff_monomial, Finset.sum_ite_eq']
  have hPcoeff : ∀ d, P.coeff d = P.support.gcd P.coeff * U.coeff d := by
    intro d
    by_cases hd : d ∈ P.support
    · simpa [hUcoeff, hd] using hg' d hd
    · simp [hUcoeff, hd, notMem_support_iff.1 hd]
  refine ⟨U, ?_, ?_⟩
  · ext d; rw [coeff_C_mul, hPcoeff]
  · have hsupp : U.support = P.support := by
      ext d
      simp [mem_support_iff, hPcoeff d, hg0]
    rw [hsupp, ← hg1]
    exact Finset.gcd_congr rfl fun d hd ↦ by rw [hUcoeff, ite_eq_left hd]

-- (3) General form: GCD domain R with fraction field K, arbitrary σ.
theorem exists_primitive_smul_eq_map {σ R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K]
    {G : MvPolynomial σ K} (hG : G ≠ 0) :
    ∃ (g : K) (U : MvPolynomial σ R), g ≠ 0 ∧ map (algebraMap R K) U = g • G ∧
      U.support.gcd U.coeff = 1 := by
  obtain ⟨b, hb, U0, hU0⟩ := exists_smul_eq_map_of_isLocalization (nonZeroDivisors R) G
  have hb0 : (algebraMap R K b) ≠ 0 :=
    (IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors hb)
  have hU00 : U0 ≠ 0 := by
    rintro rfl
    rw [map_zero, eq_comm, ← algebraMap_smul K, smul_eq_zero] at hU0
    exact hU0.elim hb0 hG
  obtain ⟨U, hU, hU1⟩ := exists_eq_C_gcd_mul hU00
  set c := U0.support.gcd U0.coeff
  have hc : algebraMap R K c ≠ 0 := by
    refine (IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors
      (mem_nonZeroDivisors_of_ne_zero ?_))
    intro h0; rw [h0, C_0, zero_mul] at hU; exact hU00 hU
  refine ⟨algebraMap R K b / algebraMap R K c, U, div_ne_zero hb0 hc, ?_, hU1⟩
  have h2 : C (algebraMap R K c) * map (algebraMap R K) U = algebraMap R K b • G := by
    rw [← map_C, ← map_mul, ← hU, hU0, algebraMap_smul]
  rw [smul_eq_C_mul] at h2 ⊢
  rw [div_eq_inv_mul, C_mul, mul_assoc, ← h2, ← mul_assoc, ← C_mul, inv_mul_cancel₀ hc, C_1,
    one_mul]

-- (4) Project statement recovered as a one-line specialisation of (3).
example {σ : Type*} {G : MvPolynomial σ ℚ} (hG : G ≠ 0) :
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧
      U.support.gcd (fun d ↦ U.coeff d) = 1 :=
  exists_primitive_smul_eq_map hG
