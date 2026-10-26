import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv

/-! Persistent mathlib-only assessment session control. -/
#check_failure MvPolynomial.hasseDeriv
#check Finsupp.lsum_apply
#check Finsupp.lsum_single

#check_failure MvPolynomial.hasseCoeff_eq_zero_iff
#check_failure MvPolynomial.hasseCoeff
#check @Finsupp.prod_eq_zero_iff
#check @Finsupp.prod_ne_zero_iff
namespace HasseZeroSearchAudit
variable {σ : Type*}
example (d k : σ →₀ ℕ) : d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  first | exact? | simp [Nat.choose_eq_zero_iff, Finsupp.le_iff, not_forall]
example {α β ι : Type*} [Zero α] [CommMonoidWithZero β]
    [Nontrivial β] [NoZeroDivisors β] (f : ι →₀ α) (g : ι → α → β) :
    f.prod g = 0 ↔ ∃ i ∈ f.support, g i (f i) = 0 := by
  exact?
end HasseZeroSearchAudit

