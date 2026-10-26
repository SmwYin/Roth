import Roth.Wronskian

/-! Evidence for `Roth.wronskian_eq_zero_of_not_linearIndependent`. -/

open Polynomial

namespace Evidence

noncomputable def wronskianMatrix {R : Type*} [Semiring R] {l : ℕ} (φ : Fin l → R[X]) :
    Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)

noncomputable def wronskian {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X]) : R[X] :=
  (wronskianMatrix φ).det

-- (1) Weakening `[Field K]` to `[CommRing R] [IsDomain R]`: the project proof goes through
-- verbatim (`Matrix.exists_mulVec_eq_zero_iff` needs only a domain).
theorem wronskian_eq_zero_of_not_linearIndependent {R : Type*} [CommRing R] [IsDomain R]
    {l : ℕ} {φ : Fin l → R[X]} (h : ¬ LinearIndependent R φ) : wronskian φ = 0 := by
  obtain ⟨g, hg, ν₀, hν₀⟩ := Fintype.not_linearIndependent_iff.1 h
  refine Matrix.exists_mulVec_eq_zero_iff.1 ⟨fun ν ↦ C (g ν), fun h0 ↦ hν₀ ?_, ?_⟩
  · simpa using congrFun h0 ν₀
  · ext1 μ
    simpa [wronskianMatrix, Matrix.mulVec, dotProduct, ← smul_eq_C_mul, mul_comm]
      using congrArg (hasseDeriv μ) hg

-- the project theorem is the specialisation
example {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} (h : ¬ LinearIndependent K φ) :
    Roth.wronskian φ = 0 :=
  wronskian_eq_zero_of_not_linearIndependent h

-- (2) `[IsDomain R]` cannot be dropped: over `ZMod 4`, the one-element family `![C 2]` is
-- linearly dependent (`2 • C 2 = 0`) but its Wronskian is `C 2 ≠ 0`.
example : ¬ LinearIndependent (ZMod 4) ![(C 2 : (ZMod 4)[X])] := by
  refine Fintype.not_linearIndependent_iff.2 ⟨fun _ ↦ 2, ?_, 0, by decide⟩
  simp only [Finset.univ_unique, Finset.sum_singleton, Matrix.cons_val_fin_one, smul_eq_C_mul,
    ← C_mul]
  rw [show (2 : ZMod 4) * 2 = 0 by decide, C_0]

example : wronskian ![(C 2 : (ZMod 4)[X])] ≠ 0 := by
  simp only [wronskian, wronskianMatrix, Matrix.det_unique, Matrix.of_apply,
    Matrix.cons_val_fin_one, Fin.default_eq_zero, Fin.val_zero, hasseDeriv_zero,
    LinearMap.id_apply, ne_eq, C_eq_zero]
  decide

end Evidence
