/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

import Mathlib.Algebra.EuclideanDomain.Int
import Mathlib.Algebra.GCDMonoid.Finset
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.RingTheory.Localization.Integer
import Mathlib.RingTheory.PrincipalIdealDomain

/-!
# Integral and primitive rescalings of rational polynomials

A polynomial over a localization has an integral multiple (`Roth.exists_map_eq_smul`); every
nonzero polynomial over `ℚ` therefore has a nonzero rational multiple with integer coefficients of
gcd `1` (`Roth.exists_primitive_smul_eq`), and a number whose products with a family of integers
of gcd `1` are all integers is itself an integer (`Roth.exists_int_eq_of_gcd_eq_one`). These are
the two ingredients of the integrality step in Lemma 2 of the source.

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §2, proof of Lemma 2
(`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open MvPolynomial

variable {σ : Type*}

/-- Clearing denominators: a polynomial over a localization `K` of `A` at `M` becomes the image of
a polynomial over `A` after multiplication by some element of `M`. -/
theorem exists_map_eq_smul {A K : Type*} [CommRing A] [CommRing K] [Algebra A K] (M : Submonoid A)
    [IsLocalization M K] (G : MvPolynomial σ K) :
    ∃ (N : M) (U : MvPolynomial σ A), map (algebraMap A K) U = algebraMap A K N • G := by
  classical
  obtain ⟨b, hb⟩ := IsLocalization.exist_integer_multiples M G.support G.coeff
  simp only [IsLocalization.IsInteger, RingHom.mem_rangeS] at hb
  choose! c hc using hb
  refine ⟨b, ∑ d ∈ G.support, monomial d (c d), ?_⟩
  ext e
  rw [coeff_map, coeff_sum, coeff_smul, smul_eq_mul]
  simp only [coeff_monomial, Finset.sum_ite_eq']
  split_ifs with he
  · simpa [Algebra.smul_def] using hc e he
  · simp [notMem_support_iff.1 he]

/-- A rational polynomial becomes integral after multiplication by a nonzero integer.
Source: §2, proof of Lemma 2 ("clearing denominators"). -/
theorem exists_map_eq_int_smul (G : MvPolynomial σ ℚ) :
    ∃ (N : ℤ) (U : MvPolynomial σ ℤ), N ≠ 0 ∧ map (Int.castRingHom ℚ) U = (N : ℚ) • G := by
  obtain ⟨N, U, hU⟩ := exists_map_eq_smul (nonZeroDivisors ℤ) G
  exact ⟨N, U, nonZeroDivisors.coe_ne_zero N, by simpa using hU⟩

/-- Every nonzero rational polynomial has a nonzero rational multiple that is an integral
polynomial with coprime coefficients.
Source: §2, proof of Lemma 2 ("Choose `g ∈ ℚ×` so that `U = gG` is an integral primitive
polynomial"). -/
theorem exists_primitive_smul_eq {G : MvPolynomial σ ℚ} (hG : G ≠ 0) :
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧
      U.support.gcd U.coeff = 1 := by
  classical
  -- clear denominators
  obtain ⟨N, U0, hN, hU0⟩ := exists_map_eq_int_smul G
  have hne : U0.support.Nonempty := support_nonempty.mpr fun h ↦ by
    simpa [h, smul_eq_zero, hN, hG] using hU0.symm
  -- divide by the gcd of the coefficients (`Finset.extract_gcd`)
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
  refine ⟨(N : ℚ) / g0, U, div_ne_zero (by exact_mod_cast hN) (by exact_mod_cast hg0), ?_, ?_⟩
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

/-- If integers `u_a` have gcd `1` and every `u_a v` is an integer, then `v` is an integer.
Source: §2, proof of Lemma 2 ("Primitivity gives a finite integral linear combination
`∑ z_a u_a = 1`"). -/
theorem exists_int_eq_of_gcd_eq_one {ι K : Type*} [Ring K] {s : Finset ι} {u : ι → ℤ}
    (hu : s.gcd u = 1) {v : K} (hv : ∀ a ∈ s, ∃ z : ℤ, (u a : K) * v = z) : ∃ z : ℤ, v = z := by
  -- Bézout: `∑ z_a u_a = 1`
  obtain ⟨z, hz⟩ := Finset.gcd_eq_sum_mul s u
  rw [hu] at hz
  choose! w hw using hv
  -- hence `v = ∑ z_a (u_a v)` is an integer
  refine ⟨∑ i ∈ s, w i * z i, ?_⟩
  calc v = ((∑ i ∈ s, u i * z i : ℤ) : K) * v := by simp [← hz]
    _ = ((∑ i ∈ s, w i * z i : ℤ) : K) := by
        push_cast
        rw [Finset.sum_mul]
        exact Finset.sum_congr rfl fun i hi ↦ by
          rw [Int.cast_comm (u i), mul_assoc, hw i hi, Int.cast_comm]

end Roth
