import Roth.Wronskian

/-! Evidence for `Roth.wronskian_update_sub_smul`. -/

open Polynomial

namespace Evidence

noncomputable def wronskianMatrix {R : Type*} [Semiring R] {l : ℕ} (φ : Fin l → R[X]) :
    Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)

noncomputable def wronskian {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X]) : R[X] :=
  (wronskianMatrix φ).det

-- (1) `[Field K]` weakens to `[CommRing R]`, project proof verbatim.
theorem wronskian_update_sub_smul {R : Type*} [CommRing R] {l : ℕ} {φ : Fin l → R[X]}
    {ν ν' : Fin l} (h : ν ≠ ν') (c : R) :
    wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ := by
  refine (congrArg Matrix.det ?_).trans
    (Matrix.det_updateCol_add_smul_self (wronskianMatrix φ) h.symm (-C c))
  ext μ ρ
  simp [wronskianMatrix, Matrix.updateCol_apply, Function.update_apply, apply_ite,
    ← smul_eq_C_mul, sub_eq_add_neg]

-- (2) `smul` spelling (`c • φ ν`) and `add` variant, same proof shape.
theorem wronskian_update_add_smul {R : Type*} [CommRing R] {l : ℕ} {φ : Fin l → R[X]}
    {ν ν' : Fin l} (h : ν ≠ ν') (c : R) :
    wronskian (Function.update φ ν' (φ ν' + c • φ ν)) = wronskian φ := by
  refine (congrArg Matrix.det ?_).trans
    (Matrix.det_updateCol_add_smul_self (wronskianMatrix φ) h.symm (C c))
  ext μ ρ
  simp [wronskianMatrix, Matrix.updateCol_apply, Function.update_apply, apply_ite,
    ← smul_eq_C_mul]

-- (3) the project theorem is the specialisation
example {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) :
    Roth.wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = Roth.wronskian φ :=
  wronskian_update_sub_smul h c

-- (4) `ν ≠ ν'` is necessary: ν = ν', c = 1 sends φ ν to 0, killing a nonzero Wronskian.
example : wronskian (Function.update ![(1 : ℚ[X])] 0 (![(1 : ℚ[X])] 0 - C 1 * ![(1 : ℚ[X])] 0))
    ≠ wronskian ![(1 : ℚ[X])] := by
  simp [wronskian, wronskianMatrix, Matrix.det_unique]

-- (5) Most general standard form: a constant change of basis `A` multiplies the Wronskian by
-- `det A`; (1) is the special case of a transvection.
theorem wronskian_mul_matrix {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X])
    (A : Matrix (Fin l) (Fin l) R) :
    wronskian (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskian φ := by
  have : wronskianMatrix (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = wronskianMatrix φ * A.map C := by
    refine Matrix.ext fun μ ν ↦ ?_
    simp only [wronskianMatrix, Matrix.of_apply, Matrix.mul_apply, Matrix.map_apply, map_sum,
      map_smul]
    simp [smul_eq_C_mul, mul_comm]
  rw [wronskian, this, Matrix.det_mul,
    show (A.map C).det = C A.det from (RingHom.map_det C A).symm, wronskian, mul_comm]

end Evidence
