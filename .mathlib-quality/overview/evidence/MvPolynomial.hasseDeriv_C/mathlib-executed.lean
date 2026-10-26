import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Nat.Choose.Bounds
#check_failure MvPolynomial.hasseDeriv_C
#check @Polynomial.hasseDeriv_C
#check @MvPolynomial.C
#check @MvPolynomial.monomial
#check @Finsupp.lsum_single
#check @MvPolynomial.C_apply
#check @MvPolynomial.pderiv_C
#check @Finsupp.lsum_apply
namespace HasseCProbe
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
def factor (d k : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
noncomputable def delta (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (factor d k : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
theorem factor_zero {d : σ →₀ ℕ} (hd : d ≠ 0) : factor d 0 = 0 := by
  obtain ⟨i, hi⟩ := Finsupp.ne_iff.mp hd
  change d i ≠ 0 at hi
  change d.prod (fun j ↦ (0 : ℕ).choose (d j)) = 0
  rw [Finsupp.prod_eq_zero_iff]
  exact ⟨i, Finsupp.mem_support_iff.mpr hi, Nat.choose_eq_zero_of_lt (Nat.pos_of_ne_zero hi)⟩
theorem factor_zero_short {d : σ →₀ ℕ} (hd : d ≠ 0) : factor d 0 = 0 := by
  simpa [factor, Finsupp.prod_eq_zero_iff, Nat.choose_eq_zero_iff,
    Finsupp.mem_support_iff, Nat.pos_iff_ne_zero] using (Finsupp.ne_iff.mp hd)
theorem delta_monomial (d k : σ →₀ ℕ) (a : R) :
    delta d (monomial k a) = monomial (k - d) ((factor d k : R) * a) :=
  Finsupp.lsum_single R (fun k : σ →₀ ℕ ↦
    (monomial (k - d)).comp (LinearMap.lsmul R R (factor d k : R))) k a
theorem constant {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : delta d (C a) = 0 := by
  rw [C_apply, delta_monomial, factor_zero hd]
  simp
theorem zero_constant (a : R) : delta (0 : σ →₀ ℕ) (C a) = C a := by
  rw [C_apply, delta_monomial]
  simp [factor]
theorem necessity : delta (0 : Unit →₀ ℕ) (C (1 : ℕ)) ≠ 0 := by
  rw [zero_constant]
  simp
theorem abstract_constant (L : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (hL : ∀ a, L (monomial 0 a) = 0) (a : R) : L (C a) = 0 :=
  hL a
theorem abstract_monomial (b : (σ →₀ ℕ) → R) (s : (σ →₀ ℕ) → (σ →₀ ℕ))
    (hb : b 0 = 0) (a : R) :
    (Finsupp.lsum R (fun k ↦ (monomial (s k)).comp (LinearMap.lsmul R R (b k)))
      ((AddMonoidAlgebra.coeffLinearEquiv R) (C a))) = 0 := by
  rw [C_apply]
  simp [hb]
#print axioms factor_zero_short
#print axioms factor_zero
#print axioms delta_monomial
#print axioms zero_constant
#print axioms abstract_constant
#print axioms constant
#print axioms necessity
#print axioms abstract_monomial
end HasseCProbe
