import Mathlib.Algebra.BigOperators.Finsupp.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Choose.Multinomial

-- This file deliberately imports no Roth modules. A composition, not an absence assertion.
universe u
variable {σ : Type u}
def composedCoefficient (d k : σ →₀ ℕ) : ℕ :=
  Finsupp.prod d (fun j n ↦ Nat.choose (k j) n)
#print axioms composedCoefficient
#check @Finsupp.prod
#check @Nat.choose
#check @Finsupp.multinomial
-- The direct definition is the complete original mathematical contract, with no target available.
example (d k : σ →₀ ℕ) : composedCoefficient d k =
    d.prod (fun j ↦ (k j).choose) := rfl
-- A stricter proposal is not needed to construct the value.
def upperFunctionCoefficient (d : σ →₀ ℕ) (k : σ → ℕ) : ℕ :=
  Finsupp.prod d (fun j n ↦ Nat.choose (k j) n)
example (d k : σ →₀ ℕ) : upperFunctionCoefficient d k = composedCoefficient d k := rfl
-- Generic-route probe for the claimed composition: automation must reconstruct it.
example (d k : σ →₀ ℕ) : composedCoefficient d k =
    d.prod (fun j ↦ (k j).choose) := by exact?
