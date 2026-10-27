import Roth.Separation
import Mathlib.RingTheory.MvPolynomial.Localization
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.RingTheory.Localization.Integral
import Mathlib.RingTheory.Localization.NumDen

open MvPolynomial

-- (0) signatures
#check @Roth.exists_int_factors

-- (1)-(3) copied from the Roth.exists_primitive_smul_eq evidence (general GCD-domain primitive multiple)
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


-- (5) integrality test over a GCD domain (generalises Roth.exists_int_eq_of_gcd_eq_one; no Bezout needed)
theorem isInteger_of_gcd_eq_one {ι R K : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    [UniqueFactorizationMonoid R]
    [Field K] [Algebra R K] [IsFractionRing R K] {s : Finset ι} {u : ι → R} (hu : s.gcd u = 1)
    {v : K} (hv : ∀ a ∈ s, IsLocalization.IsInteger R (algebraMap R K (u a) * v)) :
    IsLocalization.IsInteger R v := by
  apply IsFractionRing.isInteger_of_isUnit_den
  refine isUnit_of_dvd_one (hu ▸ Finset.dvd_gcd fun a ha ↦ ?_)
  obtain ⟨z, hz⟩ := hv a ha
  have hv' : v * algebraMap R K (IsFractionRing.den R v) =
      algebraMap R K (IsFractionRing.num R v) := by
    have h := IsLocalization.mk'_spec (M := nonZeroDivisors R) K (IsFractionRing.num R v)
      (IsFractionRing.den R v)
    rwa [IsFractionRing.mk'_num_den] at h
  have key : z * (IsFractionRing.den R v : R) = u a * IsFractionRing.num R v := by
    apply IsFractionRing.injective R K
    rw [map_mul, map_mul, hz, mul_assoc, hv']
  exact (IsFractionRing.num_den_reduced R v).symm.dvd_of_dvd_mul_right ⟨z, by rw [← key, mul_comm]⟩

-- (6) General form of Roth.exists_int_factors: GCD domain R, fraction field K.
theorem exists_factors_of_map_eq_rename_mul_aeval {τ R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [UniqueFactorizationMonoid R] [Field K] [Algebra R K]
    [IsFractionRing R K] {U' : MvPolynomial τ K} {V' : Polynomial K} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) R} (hF : map (algebraMap R K) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) K) V') :
    ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree := by
  have hinj : Function.Injective (algebraMap R K) := IsFractionRing.injective R K
  obtain ⟨g, U, hg, hUmap, hgcd⟩ := exists_primitive_smul_eq_map (R := R) hU
  set V'' := Polynomial.C g⁻¹ * V' with hV''
  have hF' : map (algebraMap R K) F = rename some (map (algebraMap R K) U) *
      Polynomial.aeval (X none : MvPolynomial (Option τ) K) V'' := by
    rw [hF, hUmap, hV'', map_mul, Polynomial.aeval_C, MvPolynomial.algebraMap_eq, smul_eq_C_mul,
      map_mul, rename_C, mul_mul_mul_comm, ← C_mul, mul_inv_cancel₀ hg, C_1, one_mul]
  have hlift : V'' ∈ (Polynomial.mapRingHom (algebraMap R K)).range := by
    refine (Polynomial.mem_map_range (algebraMap R K)).2 fun b ↦ ?_
    obtain ⟨z, hz⟩ := isInteger_of_gcd_eq_one hgcd (K := K) (v := V''.coeff b) fun a _ ↦
      ⟨F.coeff (a.mapDomain some + Finsupp.single none b), by
        have h := congrArg (fun P ↦ P.coeff (a.mapDomain some + Finsupp.single none b)) hF'
        simp only [Roth.coeff_rename_mul_aeval, coeff_map] at h
        exact h⟩
    exact ⟨z, hz⟩
  obtain ⟨V, hVmap⟩ := hlift
  rw [Polynomial.coe_mapRingHom] at hVmap
  refine ⟨U, V, ?_, ?_, ?_, fun j ↦ ?_, ?_⟩
  · exact fun h ↦ smul_ne_zero hg hU (by simpa [h] using hUmap.symm)
  · exact fun h ↦ mul_ne_zero (Polynomial.C_ne_zero.2 (inv_ne_zero hg)) hV
      (by simpa [h, hV''] using hVmap.symm)
  · apply MvPolynomial.map_injective (algebraMap R K) hinj
    rw [hF', map_mul (map (algebraMap R K)), map_rename,
      Polynomial.map_aeval_eq_aeval_map (φ := algebraMap R K) (by ext r; simp [MvPolynomial.algebraMap_eq]), map_X,
      hVmap]
  · rw [degreeOf, ← degrees_map_of_injective U hinj, hUmap, ← degreeOf, smul_eq_C_mul,
      degreeOf_C_mul j g (mem_nonZeroDivisors_of_ne_zero hg)]
  · rw [← Polynomial.natDegree_map_eq_of_injective hinj, hVmap,
      Polynomial.natDegree_C_mul (inv_ne_zero hg)]

-- (7) Project statement recovered as a specialisation of (6).
example {τ : Type*} {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) ℤ} (hF : map (Int.castRingHom ℚ) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :
    ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree :=
  exists_factors_of_map_eq_rename_mul_aeval hU hV hF
