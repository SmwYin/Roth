import Roth.GenWronskian

/-! Evidence for `Roth.genWronskian`. -/

open MvPolynomial

namespace Evidence

-- (1) Weakening `[Field K]` to `[CommRing R]` (determinant needs `CommRing`, `hasseDeriv` only
-- `CommSemiring`); no `Fintype σ` needed.
noncomputable def genWronskian {R σ : Type*} [CommRing R] {l : ℕ} (D : Fin l → σ →₀ ℕ)
    (φ : Fin l → MvPolynomial σ R) : MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det

-- the project def is the specialisation (definitional)
example {K σ : Type*} [Field K] {l : ℕ} (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ K) :
    Roth.genWronskian D φ = genWronskian D φ := rfl

-- elaborates over `ℤ` with an infinite variable type
noncomputable example (D : Fin 3 → ℕ →₀ ℕ) (φ : Fin 3 → MvPolynomial ℕ ℤ) :
    MvPolynomial ℕ ℤ := genWronskian D φ

-- (2) base change along a ring hom
theorem map_genWronskian {R S σ : Type*} [CommRing R] [CommRing S] (f : R →+* S) {l : ℕ}
    (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R) :
    map f (genWronskian D φ) = genWronskian D fun ν ↦ map f (φ ν) := by
  rw [genWronskian, genWronskian, RingHom.map_det]
  congr 1
  ext μ ν
  simp [MvPolynomial.hasseDeriv_map]

-- (3) univariate case: with one variable and `D μ = μ • e`, it is the Hasse Wronskian
theorem genWronskian_unique {K σ : Type*} [Field K] [Unique σ] {l : ℕ}
    (φ : Fin l → MvPolynomial σ K) :
    uniqueAlgEquiv K σ (genWronskian (fun μ ↦ Finsupp.single default (μ : ℕ)) φ) =
      Roth.wronskian fun ν ↦ uniqueAlgEquiv K σ (φ ν) := by
  rw [genWronskian, Roth.wronskian, AlgEquiv.map_det]
  refine congrArg Matrix.det (Matrix.ext fun μ ν ↦ ?_)
  exact MvPolynomial.uniqueAlgEquiv_hasseDeriv _ _

-- (4) degenerate sizes
example {R σ : Type*} [CommRing R] (D : Fin 0 → σ →₀ ℕ) (φ : Fin 0 → MvPolynomial σ R) :
    genWronskian D φ = 1 := by simp [genWronskian]

example {R σ : Type*} [CommRing R] (D : Fin 1 → σ →₀ ℕ) (φ : Fin 1 → MvPolynomial σ R) :
    genWronskian D φ = hasseDeriv (D 0) (φ 0) := by simp [genWronskian]

end Evidence
