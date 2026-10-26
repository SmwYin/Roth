import Roth.Wronskian
import Mathlib.RingTheory.Localization.Module
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.CharP.Algebra

/-! Evidence for `Roth.wronskian_ne_zero_of_linearIndependent`. -/

open Polynomial

namespace Evidence

-- CommRing Wronskian (copied from the `Roth.wronskian` evidence file).
noncomputable def wronskian {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X]) : R[X] :=
  (Matrix.of fun μ ν : Fin l ↦ hasseDeriv μ (φ ν)).det

example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) : Roth.wronskian φ = wronskian φ := rfl

theorem map_wronskian {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S) {l : ℕ}
    (φ : Fin l → R[X]) : (wronskian φ).map f = wronskian fun ν ↦ (φ ν).map f := by
  rw [wronskian, ← Polynomial.coe_mapRingHom, RingHom.map_det]
  congr 1
  ext μ ν
  simp [hasseDeriv_map]

-- (1) Weakening `[Field K]` to `[CommRing R] [IsDomain R] [CharZero R]`: pass to the fraction
-- field (linear independence transfers by `LinearIndependent.iff_fractionRing`, the Wronskian
-- commutes with `map`, and `map` along an injective hom is injective) and apply the project
-- field statement.
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

-- (1') it applies over `ℤ` directly
example {l : ℕ} {φ : Fin l → ℤ[X]} (h : LinearIndependent ℤ φ) : wronskian φ ≠ 0 :=
  wronskian_ne_zero_of_linearIndependent h

-- (2) The project statement is the field specialisation.
example {K : Type*} [Field K] [CharZero K] {l : ℕ} {φ : Fin l → K[X]}
    (h : LinearIndependent K φ) : Roth.wronskian φ ≠ 0 :=
  wronskian_ne_zero_of_linearIndependent h

-- (3) `CharZero` cannot be dropped: `1, X ^ 2` are linearly independent over `ZMod 2`
-- but their Hasse Wronskian vanishes (`hasseDeriv 1 (X ^ 2) = 2 X = 0`).
example : LinearIndependent (ZMod 2) ![(1 : (ZMod 2)[X]), X ^ 2] := by
  rw [LinearIndependent.pair_iff]
  intro s t hst
  have h0 := congrArg (coeff · 0) hst
  have h2 := congrArg (coeff · 2) hst
  simp only [coeff_add, coeff_smul, coeff_one, coeff_X_pow, smul_eq_mul, coeff_zero] at h0 h2
  simpa using And.intro h0 h2

example : Roth.wronskian (K := ZMod 2) ![1, X ^ 2] = 0 := by
  simp [Roth.wronskian, Roth.wronskianMatrix, Matrix.det_fin_two, hasseDeriv_one]
  exact CharTwo.add_self_eq_zero 1

end Evidence
