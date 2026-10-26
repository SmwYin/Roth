import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Nat.Choose.Bounds

#check_failure MvPolynomial.hasseDeriv_zero_apply
namespace ZeroApplyAssessment
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
noncomputable def delta (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R ((d.prod fun j ↦ (k j).choose : ℕ) : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

-- Underlying identity: local reconstruction, no project alias or project theorem.
example (P : MvPolynomial σ R) : delta 0 P = P := by
  simp [delta, Function.comp_def, LinearMap.lsmul_apply, sum_def]

-- Existing univariate analogue and linear-map pointwise routes are distinct.
#check @Polynomial.hasseDeriv_zero'
#check @Polynomial.hasseDeriv_zero
#check @Finsupp.lsum_single
#check @Finsupp.lsum_comp_lsingle
#check @MvPolynomial.sum_monomial_eq
#check @LinearMap.congr_fun
#check @LinearMap.ext
example (f : Polynomial R) : Polynomial.hasseDeriv 0 f = f := Polynomial.hasseDeriv_zero'

-- Abstract coefficient-preserving maps: content retained by an explicit normalization law.
example (T : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (h : ∀ e P, (T P).coeff e = P.coeff e) (P : MvPolynomial σ R) : T P = P := by
  ext e
  exact h e P
example : ¬ ∀ T : MvPolynomial Unit ℕ →ₗ[ℕ] MvPolynomial Unit ℕ,
    ∀ P, T P = P := by
  intro h
  have hh := h 0 1
  simpa using hh
end ZeroApplyAssessment
