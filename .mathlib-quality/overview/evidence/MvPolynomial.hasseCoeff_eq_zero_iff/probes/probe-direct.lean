import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
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
