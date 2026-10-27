import Roth.Separation
import Mathlib.RingTheory.MvPolynomial.Localization
import Mathlib.RingTheory.Localization.Integral

open MvPolynomial

-- (0) signature
#check @Roth.exists_nat_smul_eq_map

-- (1) univariate mathlib analogue
#check @IsLocalization.integerNormalization_spec

-- (2) General localization form (MvPolynomial analogue of `integerNormalization_spec`),
-- composed from `exist_integer_multiples` + `mem_range_map_iff_coeffs_subset`.
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

-- (3) Alternative: direct `IsLocalization.surj` on the instance `MvPolynomial.isLocalization`.
attribute [local instance] MvPolynomial.algebraMvPolynomial in
example {σ R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] (M : Submonoid R) [IsLocalization M S] (G : MvPolynomial σ S) :
    ∃ b ∈ M, ∃ U : MvPolynomial σ R, map (algebraMap R S) U = (b : R) • G := by
  obtain ⟨⟨U, ⟨_, b, hb, rfl⟩⟩, h⟩ := IsLocalization.surj (M.map (C (σ := σ))) G
  refine ⟨b, hb, U, ?_⟩
  change _ = map (algebraMap R S) U at h
  rw [← h]
  ext d
  simp [Algebra.smul_def, mul_comm]

-- (4) Project statement recovered from (2) at ℤ → ℚ, fixing the sign of `b`.
example {σ : Type*} (G : MvPolynomial σ ℚ) :
    ∃ (N : ℕ) (U : MvPolynomial σ ℤ), 0 < N ∧ map (Int.castRingHom ℚ) U = (N : ℚ) • G := by
  obtain ⟨b, hb, U, hU⟩ := exists_smul_eq_map_of_isLocalization (nonZeroDivisors ℤ) G
  have hb0 : b ≠ 0 := nonZeroDivisors.ne_zero hb
  refine ⟨b.natAbs, C b.sign * U, Int.natAbs_pos.2 hb0, ?_⟩
  have hU' : map (Int.castRingHom ℚ) U = (b : ℚ) • G := by
    rw [Int.cast_smul_eq_zsmul]; exact hU
  rw [map_mul, map_C, hU', smul_eq_C_mul, smul_eq_C_mul, ← mul_assoc, ← C_mul]
  congr 2
  rw [eq_intCast, ← Int.cast_mul, Int.sign_mul_self_eq_abs, Nat.cast_natAbs]

-- (5) Call-site refactor: `exists_primitive_smul_eq` reproved from (2), using `b : ℤ`, `b ≠ 0`.
open Roth in
theorem exists_primitive_smul_eq' {σ : Type*} {G : MvPolynomial σ ℚ} (hG : G ≠ 0) :
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧
      U.support.gcd (fun d ↦ U.coeff d) = 1 := by
  classical
  obtain ⟨N, hNM, U0, hU0⟩ := exists_smul_eq_map_of_isLocalization (nonZeroDivisors ℤ) G
  have hN : (N : ℚ) ≠ 0 := by exact_mod_cast nonZeroDivisors.ne_zero hNM
  replace hU0 : map (Int.castRingHom ℚ) U0 = (N : ℚ) • G := by
    rw [Int.cast_smul_eq_zsmul]; exact hU0
  have hne : U0.support.Nonempty := support_nonempty.mpr fun h ↦ by
    simpa [h, smul_eq_zero, hN, hG] using hU0.symm
  obtain ⟨g', hg', hg1⟩ := Finset.extract_gcd (fun d ↦ U0.coeff d) hne
  set g0 := U0.support.gcd (fun d ↦ U0.coeff d) with hg0def
  have hg0 : g0 ≠ 0 := by
    obtain ⟨d, hd⟩ := hne
    rw [hg0def, Ne, Finset.gcd_eq_zero_iff]
    exact fun h ↦ mem_support_iff.1 hd (h d hd)
  set U := ∑ d ∈ U0.support, monomial d (g' d) with hUdef
  have hUcoeff : ∀ d, U.coeff d = if d ∈ U0.support then g' d else 0 := by
    simp [hUdef, coeff_monomial, Finset.sum_ite_eq']
  have hU0coeff : ∀ d, U0.coeff d = g0 * U.coeff d := by
    intro d
    by_cases hd : d ∈ U0.support
    · simpa [hUcoeff, hd] using hg' d hd
    · simp [hUcoeff, hd, notMem_support_iff.1 hd]
  refine ⟨N / g0, U, div_ne_zero (by exact_mod_cast hN) (by exact_mod_cast hg0), ?_, ?_⟩
  · ext d
    have h1 := congrArg (fun P ↦ P.coeff d) hU0
    simp only [coeff_map, coeff_smul, smul_eq_mul, eq_intCast] at h1 ⊢
    rw [hU0coeff] at h1
    push_cast at h1
    rwa [div_mul_eq_mul_div, eq_div_iff (by exact_mod_cast hg0), mul_comm]
  · have hsupp : U.support = U0.support := by
      ext d
      simp [mem_support_iff, hU0coeff d, hg0]
    rw [hsupp, ← hg1]
    exact Finset.gcd_congr rfl fun d hd ↦ by rw [hUcoeff, ite_eq_left hd]
