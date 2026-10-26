import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv

/-! Persistent mathlib-only assessment session control. -/
#check_failure MvPolynomial.hasseDeriv
#check Finsupp.lsum_apply
#check Finsupp.lsum_single

#check_failure MvPolynomial.coeff_hasseDeriv
#check_failure HasseZeroAudit.expanded
example (P : Prop) (h : P) : P := by exact?

/-! Isolated coefficient-identity assessment: new witnesses, no project import. -/
open MvPolynomial
namespace CoeffAssessment
variable {σ R : Type*} [CommSemiring R]
noncomputable def delta (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
    (monomial (k - d)).comp (LinearMap.lsmul R R ((d.prod (fun j ↦ (k j).choose) : ℕ) : R))) ∘ₗ
      (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

-- Exact? must not find a pre-existing proof of the expanded proposed coefficient API.
theorem independent (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (delta d P).coeff e = ((d.prod (fun j ↦ ((e + d) j).choose) : ℕ) : R) * P.coeff (e + d) := by
  fail_if_success exact?
  classical
  have hz (k : σ →₀ ℕ) : d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
    simp [Finsupp.prod, Finset.prod_eq_zero_iff, Nat.choose_eq_zero_iff, Finsupp.le_iff,
      not_forall]
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    rw [show delta d (monomial k a) =
      monomial (k - d) (((d.prod (fun j ↦ (k j).choose) : ℕ) : R) * a) by simp [delta],
      coeff_monomial, coeff_monomial]
    by_cases hk : k = e + d
    · simp [hk]
    by_cases hdk : d ≤ k
    · simp [hk, tsub_eq_iff_eq_add_of_le hdk]
    · simp [hk, (hz k).2 hdk]
  | add p q hp hq => simp [hp, hq, mul_add]

-- Additive/linear-map characterization, an equivalent statement rather than an assumption weakening.
example (d e : σ →₀ ℕ) :
    (lcoeff R e).comp (delta d) =
      ((d.prod (fun j ↦ ((e + d) j).choose) : ℕ) : R) • lcoeff R (e + d) := by
  apply LinearMap.ext
  intro P
  exact independent d e P

-- Polynomial-coefficient commutativity is needed by the pinned domain itself.
section
variable {S : Type*} [Semiring S]
#check_failure MvPolynomial σ S
end

#print axioms independent
end CoeffAssessment


/-! New weighted-lowering witness used to test abstraction of the coefficient proof. -/
open MvPolynomial
namespace CoeffAbstractAssessment
variable {σ R : Type*} [CommSemiring R]
theorem coeff_lowering (d e : σ →₀ ℕ) (w : (σ →₀ ℕ) → R)
    (L : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (hL : ∀ k a, L (monomial k a) = monomial (k - d) (w k * a))
    (hz : ∀ k, ¬d ≤ k → w k = 0) (P : MvPolynomial σ R) :
    (L P).coeff e = w (e + d) * P.coeff (e + d) := by
  fail_if_success exact?
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    rw [hL, coeff_monomial, coeff_monomial]
    by_cases hk : k = e + d
    · simp [hk]
    by_cases hdk : d ≤ k
    · simp [hk, tsub_eq_iff_eq_add_of_le hdk]
    · simp [hk, hz k hdk]
  | add p q hp hq => simp [hp, hq, mul_add]
#print axioms coeff_lowering
end CoeffAbstractAssessment

