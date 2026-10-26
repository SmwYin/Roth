import Roth.Wronskian
import Mathlib.RingTheory.Polynomial.Wronskian

/-! Evidence for `Roth.wronskian`. -/

open Polynomial

namespace Evidence

-- (1) Weakening: the matrix needs `[Semiring R]`, the determinant `[CommRing R]`.
noncomputable def wronskianMatrix {R : Type*} [Semiring R] {l : ℕ} (φ : Fin l → R[X]) :
    Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)

noncomputable def wronskian {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X]) : R[X] :=
  (wronskianMatrix φ).det

-- the project def is the specialisation (definitional)
example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) :
    Roth.wronskian φ = wronskian φ := rfl

-- the weakened def also elaborates over `ℤ` (integral Wronskians)
noncomputable example (φ : Fin 3 → ℤ[X]) : ℤ[X] := wronskian φ

-- (2) `l = 2` agrees with mathlib's two-argument `Polynomial.wronskian` over any `CommRing`.
theorem wronskian_fin_two {R : Type*} [CommRing R] (a b : R[X]) :
    wronskian ![a, b] = Polynomial.wronskian a b := by
  simp [wronskian, wronskianMatrix, Matrix.det_fin_two, Polynomial.wronskian, hasseDeriv_one,
    mul_comm]

-- (3) Small sanity values: `l = 0` gives `1`, `l = 1` gives the polynomial itself.
example {R : Type*} [CommRing R] (φ : Fin 0 → R[X]) : wronskian φ = 1 := by
  simp [wronskian]

example {R : Type*} [CommRing R] (φ : Fin 1 → R[X]) : wronskian φ = φ 0 := by
  simp [wronskian, wronskianMatrix]

-- (4) Base change: the Wronskian commutes with ring homomorphisms of coefficients
-- (`hasseDeriv_map`), the fact used in Roth/Separation.lean via `RingHom.map_det`.
theorem map_wronskian {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S) {l : ℕ}
    (φ : Fin l → R[X]) : (wronskian φ).map f = wronskian fun ν ↦ (φ ν).map f := by
  rw [wronskian, ← Polynomial.coe_mapRingHom, RingHom.map_det]
  congr 1
  ext μ ν
  simp [wronskianMatrix, hasseDeriv_map]

end Evidence
