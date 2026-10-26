import Roth.Wronskian
import Mathlib.RingTheory.Polynomial.Wronskian

open Polynomial

/-! Evidence for `Roth.wronskianMatrix`. -/

-- (1) Weakening: the definition elaborates over any semiring, with an arbitrary column index type.
noncomputable def wronskianMatrix' {R ι : Type*} [Semiring R] (l : ℕ) (φ : ι → R[X]) :
    Matrix (Fin l) ι R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)

-- the project def is the specialisation
example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) :
    Roth.wronskianMatrix φ = wronskianMatrix' l φ := rfl

-- (2) Relation to mathlib's two-polynomial `Polynomial.wronskian`: for `l = 2` the determinant
-- of the project's matrix is exactly `Polynomial.wronskian a b` (`hasseDeriv 1 = derivative`).
example {R : Type*} [CommRing R] (a b : R[X]) :
    (wronskianMatrix' 2 ![a, b]).det = Polynomial.wronskian a b := by
  simp [wronskianMatrix', Matrix.det_fin_two, Polynomial.wronskian, hasseDeriv_one, mul_comm]

example {K : Type*} [Field K] (a b : K[X]) :
    Roth.wronskian ![a, b] = Polynomial.wronskian a b := by
  simp [Roth.wronskian, Roth.wronskianMatrix, Matrix.det_fin_two, Polynomial.wronskian,
    hasseDeriv_one, mul_comm]

-- (3) Probes: plain semireducible def, unfolds by rfl; universe-polymorphic.
example {K : Type*} [Field K] {l : ℕ} (φ : Fin l → K[X]) (μ ν : Fin l) :
    Roth.wronskianMatrix φ μ ν = hasseDeriv μ (φ ν) := rfl
example {K : Type 1} [Field K] {l : ℕ} (φ : Fin l → K[X]) (μ ν : Fin l) :
    Roth.wronskianMatrix φ μ ν = hasseDeriv μ (φ ν) := rfl
