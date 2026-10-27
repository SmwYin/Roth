import Roth.GenWronskian

/-! Evidence for `Roth.genWronskian_eq_zero_of_not_linearIndependent`. -/

open MvPolynomial

namespace Evidence

noncomputable def genWronskian {R σ : Type*} [CommRing R] {l : ℕ} (D : Fin l → σ →₀ ℕ)
    (φ : Fin l → MvPolynomial σ R) : MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det

-- (1) Weakening `[Field K]` to `[CommRing R] [IsDomain R]`: the project proof goes through
-- verbatim (`Matrix.exists_mulVec_eq_zero_iff` needs only that `MvPolynomial σ R` is a domain).
theorem genWronskian_eq_zero_of_not_linearIndependent {R σ : Type*} [CommRing R] [IsDomain R]
    {l : ℕ} (D : Fin l → (σ →₀ ℕ)) {φ : Fin l → MvPolynomial σ R}
    (h : ¬ LinearIndependent R φ) : genWronskian D φ = 0 := by
  classical
  obtain ⟨g, hg, ν₀, hν₀⟩ := Fintype.not_linearIndependent_iff.1 h
  refine Matrix.exists_mulVec_eq_zero_iff.1 ⟨fun ν ↦ C (g ν), fun h0 ↦ hν₀ ?_, ?_⟩
  · simpa using congrFun h0 ν₀
  · ext1 μ
    simpa [Matrix.mulVec, dotProduct, map_smul, ← smul_eq_C_mul, mul_comm] using
      congrArg (hasseDeriv (D μ)) hg

-- the project theorem is the specialisation
example {K σ : Type*} [Field K] {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K}
    (h : ¬ LinearIndependent K φ) : Roth.genWronskian D φ = 0 :=
  genWronskian_eq_zero_of_not_linearIndependent D h

-- (2) `[IsDomain R]` cannot be dropped: over `ZMod 4`, `![C 2]` is dependent (`2 • C 2 = 0`)
-- but its generalized Wronskian with `D = ![0]` is `C 2 ≠ 0`.
example : ¬ LinearIndependent (ZMod 4) ![(C 2 : MvPolynomial (Fin 1) (ZMod 4))] := by
  refine Fintype.not_linearIndependent_iff.2 ⟨fun _ ↦ 2, ?_, 0, by decide⟩
  simp only [Finset.univ_unique, Finset.sum_singleton, Matrix.cons_val_fin_one, smul_eq_C_mul,
    ← C_mul]
  rw [show (2 : ZMod 4) * 2 = 0 by decide, C_0]

example : genWronskian ![(0 : Fin 1 →₀ ℕ)] ![(C 2 : MvPolynomial (Fin 1) (ZMod 4))] ≠ 0 := by
  simp only [genWronskian, Matrix.det_unique, Matrix.of_apply, Matrix.cons_val_fin_one,
    hasseDeriv_zero, LinearMap.id_apply, ne_eq, C_eq_zero]
  decide

-- (3) Abstract form (Phase 4c row 8): for `R`-linear maps `L μ : M →ₗ[R] A` into a domain `A`
-- that is a faithful `R`-algebra, `det (L μ (φ ν)) = 0` whenever `φ` is `R`-dependent.
theorem det_linearMap_eq_zero_of_not_linearIndependent {R M A : Type*} [CommRing R]
    [AddCommGroup M] [Module R M] [CommRing A] [IsDomain A] [Algebra R A] [FaithfulSMul R A]
    {l : ℕ} (L : Fin l → M →ₗ[R] A) {φ : Fin l → M} (h : ¬ LinearIndependent R φ) :
    (Matrix.of fun μ ν ↦ L μ (φ ν)).det = 0 := by
  classical
  obtain ⟨g, hg, ν₀, hν₀⟩ := Fintype.not_linearIndependent_iff.1 h
  refine Matrix.exists_mulVec_eq_zero_iff.1 ⟨fun ν ↦ algebraMap R A (g ν), fun h0 ↦ hν₀ ?_, ?_⟩
  · exact FaithfulSMul.algebraMap_injective R A (by simpa using congrFun h0 ν₀)
  · ext1 μ
    simpa [Matrix.mulVec, dotProduct, Algebra.smul_def, mul_comm] using congrArg (L μ) hg

-- both project lemmas are one-line corollaries of the abstract form
example {R σ : Type*} [CommRing R] [IsDomain R] {l : ℕ} (D : Fin l → σ →₀ ℕ)
    {φ : Fin l → MvPolynomial σ R} (h : ¬ LinearIndependent R φ) : genWronskian D φ = 0 :=
  det_linearMap_eq_zero_of_not_linearIndependent (A := MvPolynomial σ R)
    (fun μ ↦ hasseDeriv (D μ)) h

example {K : Type*} [Field K] {l : ℕ} {φ : Fin l → Polynomial K}
    (h : ¬ LinearIndependent K φ) : Roth.wronskian φ = 0 :=
  det_linearMap_eq_zero_of_not_linearIndependent (A := Polynomial K)
    (fun μ ↦ Polynomial.hasseDeriv (μ : ℕ)) h

end Evidence
