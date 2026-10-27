import Roth.Separation

/-! Evidence for `Roth.det_hasseDeriv_separated`. -/

open MvPolynomial

-- (0) current signature
#check @Roth.det_hasseDeriv_separated

namespace Evidence

noncomputable def genWronskian {R σ : Type*} [CommRing R] {l : ℕ} (D : Fin l → σ →₀ ℕ)
    (φ : Fin l → MvPolynomial σ R) : MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det

noncomputable def wronskianMatrix {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → Polynomial R) :
    Matrix (Fin l) (Fin l) (Polynomial R) :=
  Matrix.of fun μ ν ↦ Polynomial.hasseDeriv μ (φ ν)

noncomputable def wronskian {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → Polynomial R) :
    Polynomial R := (wronskianMatrix φ).det

-- (1) `[Field K]` weakens to `[CommRing R]` (given CommRing versions of the parent defs);
-- the project proof goes through verbatim.
theorem det_hasseDeriv_separated {τ R : Type*} [CommRing R] {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (φ : Fin l → Polynomial R) (ψ : Fin l → MvPolynomial τ R) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ))
        (∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R) (φ ρ) *
          rename some (ψ ρ))).det = rename some (genWronskian D ψ) *
      Polynomial.aeval (X none : MvPolynomial (Option τ) R) (wronskian φ) := by
  rw [genWronskian, wronskian, AlgHom.map_det, AlgHom.map_det,
    ← Matrix.det_transpose ((Polynomial.aeval (X none)).mapMatrix (wronskianMatrix φ)),
    ← Matrix.det_mul]
  congr 1
  refine Matrix.ext fun μ ν ↦ ?_
  rw [Matrix.of_apply, map_sum, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun ρ _ ↦ ?_
  rw [mul_comm (Polynomial.aeval (X none : MvPolynomial (Option τ) R) (φ ρ)),
    Roth.hasseDeriv_rename_mul_aeval]
  rfl

-- the project statement is the `Field` specialisation
example {τ K : Type*} [Field K] {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K) :
    Roth.genWronskian D ψ = genWronskian D ψ ∧ Roth.wronskian φ = wronskian φ := ⟨rfl, rfl⟩

-- (2) over `ℤ` it now applies directly (no detour through `ℚ` needed for this step)
example {τ : Type*} {l : ℕ} (D : Fin l → (τ →₀ ℕ)) (φ : Fin l → Polynomial ℤ)
    (ψ : Fin l → MvPolynomial τ ℤ) := det_hasseDeriv_separated D φ ψ

end Evidence
