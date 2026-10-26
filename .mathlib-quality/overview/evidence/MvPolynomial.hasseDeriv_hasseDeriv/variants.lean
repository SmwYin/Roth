import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseDeriv_hasseDeriv` (overview / mathlibable). -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Operator-level form in the shape of mathlib's `Polynomial.hasseDeriv_comp`
(`∘ₗ`, `ℕ`-scalar on the right), derived from the project lemma. -/
example (d e : σ →₀ ℕ) :
    (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e =
      hasseCoeff d (d + e) • hasseDeriv (d + e) := by
  refine LinearMap.ext fun P ↦ ?_
  simp [hasseDeriv_hasseDeriv, Nat.cast_smul_eq_nsmul]

/-- (2) Conversely the project's pointwise `R`-cast form is a one-liner from the operator form,
so the operator form can be the primary statement and the pointwise one a corollary. -/
example (d e : σ →₀ ℕ) (P : MvPolynomial σ R)
    (hcomp : (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e =
      hasseCoeff d (d + e) • hasseDeriv (d + e)) :
    hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by
  simpa [Nat.cast_smul_eq_nsmul] using LinearMap.congr_fun hcomp P

/-- (3) `simp` with the coefficient API alone does NOT close the statement: it leaves the
multi-index binomial identity `binom(f+d,d) binom(f+d+e,e) = binom(d+e,d) binom(f+d+e,d+e)`
(the private `hasseCoeff_mul_hasseCoeff`), which is the real content. -/
example (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by
  ext f
  fail_if_success (simp [coeff_hasseDeriv, hasseCoeff]; done)
  rw [hasseDeriv_hasseDeriv]

end MvPolynomial
