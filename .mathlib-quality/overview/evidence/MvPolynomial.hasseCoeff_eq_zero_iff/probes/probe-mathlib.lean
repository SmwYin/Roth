import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv

#check @Finsupp.prod_eq_zero_iff
#check @Finsupp.prod_ne_zero_iff
#check @Finsupp.le_iff
#check @Nat.choose_eq_zero_iff
#check @Nat.choose_ne_zero_iff
#check @Finset.prod_eq_zero_iff
#check @Finset.prod_ne_zero_iff

namespace HasseZeroAudit
variable {σ : Type*}
-- Exact source form expanded, no target or project definitions in scope.
theorem expanded (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simp [Finsupp.prod, Finset.prod_eq_zero_iff, Nat.choose_eq_zero_iff,
    Finsupp.le_iff, not_forall]
-- Generic Finsupp product route: direct generic-product theorem plus scalar vanishing and order.
theorem generic (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simp [Finsupp.prod_eq_zero_iff, Nat.choose_eq_zero_iff, Finsupp.le_iff, not_forall]
-- Equivalent nonvanishing and positivity shapes; arbitrary type, no Fintype/DecidableEq/R.
theorem nonzero (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) ≠ 0 ↔ d ≤ k := by
  simpa using not_congr (generic d k)
theorem positive (d k : σ →₀ ℕ) :
    0 < d.prod (fun j ↦ (k j).choose) ↔ d ≤ k := by
  simpa only [Nat.pos_iff_ne_zero] using nonzero d k
-- Existing scalar finite-support generic API, not a new mathematical abstraction.
theorem product_route {α β ι : Type*} [Zero α] [CommMonoidWithZero β]
    [Nontrivial β] [NoZeroDivisors β] (f : ι →₀ α) (g : ι → α → β) :
    f.prod g = 0 ↔ ∃ i ∈ f.support, g i (f i) = 0 := by
  exact Finsupp.prod_eq_zero_iff
#print axioms expanded
#print axioms generic
#print axioms nonzero
#print axioms positive
#print axioms product_route
end HasseZeroAudit
