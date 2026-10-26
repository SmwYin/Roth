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

namespace HasseZeroDirectAudit
variable {σ : Type*}
-- Short simp composition, using prod_eq_zero_iff from the default simp set.
theorem short (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simp [Nat.choose_eq_zero_iff, Finsupp.le_iff, not_forall]
-- Nonvanishing generic route avoids existential witness reasoning.
theorem via_nonzero (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simpa only [Nat.choose_ne_zero_iff, ← Finsupp.le_iff, not_not] using
    not_congr (Finsupp.prod_ne_zero_iff (f := d) (g := fun j ↦ (k j).choose))
end HasseZeroDirectAudit
#print axioms HasseZeroDirectAudit.short
#print axioms HasseZeroDirectAudit.via_nonzero

namespace HasseZeroUpperFnAudit
variable {σ : Type*}
theorem upper_function (d : σ →₀ ℕ) (k : σ → ℕ) :
    d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬ ∀ j, d j ≤ k j := by
  rw [Finsupp.prod_eq_zero_iff]
  simp only [Nat.choose_eq_zero_iff, not_forall, not_le]
  constructor
  · rintro ⟨i, _, h⟩
    exact ⟨i, h⟩
  · rintro ⟨i, h⟩
    exact ⟨i, Finsupp.mem_support_iff.mpr
      (Nat.ne_of_gt (lt_of_le_of_lt (Nat.zero_le _) h)), h⟩
example (d k : σ →₀ ℕ) : d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k :=
  upper_function d (fun j ↦ k j)
#print axioms upper_function
end HasseZeroUpperFnAudit

