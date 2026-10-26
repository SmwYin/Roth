import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv

/-! Persistent mathlib-only assessment session control. -/
#check_failure MvPolynomial.hasseDeriv
#check Finsupp.lsum_apply
#check Finsupp.lsum_single

#check_failure MvPolynomial.hasseCoeff_eq_prod
open scoped BigOperators
namespace HasseProdAssessment
variable {σ : Type*}
#check @Finsupp.prod_fintype
#check @Finsupp.prod_of_support_subset
#check @Nat.choose_zero_right
-- Exact unfolded target; no Roth declaration is imported.
theorem exactTarget [Fintype σ] (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _
-- Upper function need not have finite support.
theorem upperFunction [Fintype σ] (d : σ →₀ ℕ) (k : σ → ℕ) :
    d.prod (fun j ↦ (k j).choose) = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _
-- Truly abstract form, already mathlib's prod_fintype.
theorem generic {M N : Type*} [Zero M] [CommMonoid N] [Fintype σ]
    (d : σ →₀ M) (g : σ → M → N) (h : ∀ j, g j 0 = 1) :
    d.prod g = ∏ j, g j (d j) := d.prod_fintype g h
-- Arbitrary index, finite ambient set alternative.
theorem ambientFinset (d k : σ →₀ ℕ) (s : Finset σ) (h : d.support ⊆ s) :
    d.prod (fun j ↦ (k j).choose) = ∏ j ∈ s, (k j).choose (d j) :=
  d.prod_of_support_subset h _ fun _ _ ↦ Nat.choose_zero_right _
-- Verify exact call-site shape after eliminating wrapper: only mathlib involved.
theorem caller [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ} (hk : ∀ j, k j ≤ r j) :
    d.prod (fun j ↦ (k j).choose) ≤ 2 ^ (∑ j, r j) := by
  rw [d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _), ← Finset.prod_pow_eq_pow_sum]
  exact Finset.prod_le_prod fun j _ ↦
    (Nat.choose_le_two_pow _ _).trans (Nat.pow_le_pow_right two_pos (hk j))
#print axioms exactTarget
#print axioms upperFunction
#print axioms generic
#print axioms ambientFinset
#print axioms caller
end HasseProdAssessment
