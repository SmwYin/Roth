import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Nat.Choose.Bounds
#check_failure MvPolynomial.hasseDeriv_map
namespace AssessHasseMapRaw
open MvPolynomial
variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]
def factor (d k : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
noncomputable def delta (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (factor d k : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
theorem delta_monomial (d k : σ →₀ ℕ) (a : R) :
    delta d (monomial k a) = monomial (k - d) ((factor d k : R) * a) :=
  Finsupp.lsum_single R (fun k : σ →₀ ℕ ↦
    (monomial (k - d)).comp (LinearMap.lsmul R R (factor d k : R))) k a
theorem natural (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    delta d (map f P) = map f (delta d P) := by
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    simp only [map_monomial, delta_monomial, map_mul, map_natCast]
  | add p q hp hq => simp only [map_add, hp, hq]
#print axioms delta_monomial
#print axioms natural
end AssessHasseMapRaw
