import Roth.Wronskian
import Mathlib.RingTheory.Localization.Module
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.CharP.Algebra

/-! Evidence for `Roth.wronskian_eq_zero_iff`: the iff over a characteristic-zero domain,
obtained by combining the two (already verified) domain-generalised directions, plus
counterexamples showing `CharZero` and `IsDomain` are both needed for the iff. -/

open Polynomial

namespace Evidence

-- CommRing Wronskian (same as the parent evidence files).
noncomputable def wronskian {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X]) : R[X] :=
  (Matrix.of fun μ ν : Fin l ↦ hasseDeriv μ (φ ν)).det

example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) : Roth.wronskian φ = wronskian φ := rfl

theorem map_wronskian {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S) {l : ℕ}
    (φ : Fin l → R[X]) : (wronskian φ).map f = wronskian fun ν ↦ (φ ν).map f := by
  rw [wronskian, ← Polynomial.coe_mapRingHom, RingHom.map_det]
  congr 1
  ext μ ν
  simp [hasseDeriv_map]

-- easy direction over a domain (proof of the project lemma, verbatim)
theorem wronskian_eq_zero_of_not_linearIndependent {R : Type*} [CommRing R] [IsDomain R]
    {l : ℕ} {φ : Fin l → R[X]} (h : ¬ LinearIndependent R φ) : wronskian φ = 0 := by
  obtain ⟨g, hg, ν₀, hν₀⟩ := Fintype.not_linearIndependent_iff.1 h
  refine Matrix.exists_mulVec_eq_zero_iff.1 ⟨fun ν ↦ C (g ν), fun h0 ↦ hν₀ ?_, ?_⟩
  · simpa using congrFun h0 ν₀
  · ext1 μ
    simpa [Matrix.mulVec, dotProduct, ← smul_eq_C_mul, mul_comm]
      using congrArg (hasseDeriv μ) hg

-- hard direction over a char-0 domain (fraction-field transfer of the project lemma)
theorem wronskian_ne_zero_of_linearIndependent {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} (h : LinearIndependent R φ) : wronskian φ ≠ 0 := by
  have hinj : Function.Injective (algebraMap R (FractionRing R)) :=
    IsFractionRing.injective R (FractionRing R)
  have : CharZero (FractionRing R) := charZero_of_injective_algebraMap hinj
  have hli : LinearIndependent (FractionRing R)
      (fun ν ↦ (φ ν).map (algebraMap R (FractionRing R))) := by
    rw [← LinearIndependent.iff_fractionRing R (FractionRing R)]
    exact h.map' (Polynomial.mapAlg R (FractionRing R)).toLinearMap
      (LinearMap.ker_eq_bot.2 (Polynomial.map_injective _ hinj))
  intro h0
  apply Roth.wronskian_ne_zero_of_linearIndependent hli
  have := congrArg (Polynomial.map (algebraMap R (FractionRing R))) h0
  rwa [map_wronskian, Polynomial.map_zero] at this

-- (1) the iff over `[CommRing R] [IsDomain R] [CharZero R]`, in both orientations
theorem wronskian_eq_zero_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} : wronskian φ = 0 ↔ ¬ LinearIndependent R φ :=
  ⟨imp_not_comm.mp wronskian_ne_zero_of_linearIndependent,
    wronskian_eq_zero_of_not_linearIndependent⟩

theorem wronskian_ne_zero_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} : wronskian φ ≠ 0 ↔ LinearIndependent R φ := by
  rw [ne_eq, wronskian_eq_zero_iff, not_not]

-- (1') over `ℤ`
example {l : ℕ} {φ : Fin l → ℤ[X]} : wronskian φ = 0 ↔ ¬ LinearIndependent ℤ φ :=
  wronskian_eq_zero_iff

-- (2) the project statement is the field specialisation
example {K : Type*} [Field K] [CharZero K] {l : ℕ} {φ : Fin l → K[X]} :
    Roth.wronskian φ = 0 ↔ ¬ LinearIndependent K φ :=
  wronskian_eq_zero_iff

-- (3) `CharZero` is needed: over `ZMod 2`, `![1, X ^ 2]` is independent, Wronskian zero.
example : ¬ (Roth.wronskian (K := ZMod 2) ![1, X ^ 2] = 0 ↔
    ¬ LinearIndependent (ZMod 2) ![(1 : (ZMod 2)[X]), X ^ 2]) := by
  have hli : LinearIndependent (ZMod 2) ![(1 : (ZMod 2)[X]), X ^ 2] := by
    rw [LinearIndependent.pair_iff]
    intro s t hst
    have h0 := congrArg (coeff · 0) hst
    have h2 := congrArg (coeff · 2) hst
    simp only [coeff_add, coeff_smul, coeff_one, coeff_X_pow, smul_eq_mul, coeff_zero] at h0 h2
    simpa using And.intro h0 h2
  have hW : Roth.wronskian (K := ZMod 2) ![1, X ^ 2] = 0 := by
    simp [Roth.wronskian, Roth.wronskianMatrix, Matrix.det_fin_two, hasseDeriv_one]
    exact CharTwo.add_self_eq_zero 1
  simp [hW, hli]

-- (4) `IsDomain` is needed even with `CharZero`: over `ℚ × ℚ`, the one-element family
-- `![C (1, 0)]` is dependent (`(0, 1) • C (1, 0) = 0`) but its Wronskian is `C (1, 0) ≠ 0`.
example : ¬ LinearIndependent (ℚ × ℚ) ![(C (1, 0) : (ℚ × ℚ)[X])] := by
  refine Fintype.not_linearIndependent_iff.2 ⟨fun _ ↦ (0, 1), ?_, 0, by simp⟩
  simp [smul_eq_C_mul, ← C_mul]

example : wronskian ![(C (1, 0) : (ℚ × ℚ)[X])] ≠ 0 := by
  simp [wronskian, Matrix.det_unique]

end Evidence
