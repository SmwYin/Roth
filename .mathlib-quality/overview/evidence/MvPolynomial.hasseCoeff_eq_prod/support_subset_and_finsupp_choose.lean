import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseCoeff_eq_prod`:
1. generalisation from `[Fintype σ]` to any finset `s ⊇ d.support` (mirrors mathlib's
   `Finsupp.multinomial_eq_of_support_subset`); the Fintype form is a one-line corollary;
2. the statement ports verbatim to the proposed `Finsupp.choose k d`;
3. composition check: the project lemma is exactly `Finsupp.prod_fintype` applied to
   `Nat.choose_zero_right`, and can be inlined at the single call site. -/

open Finset

namespace MvPolynomial

variable {σ : Type*}

theorem hasseCoeff_eq_prod_of_support_subset {d k : σ →₀ ℕ} {s : Finset σ}
    (h : d.support ⊆ s) : hasseCoeff d k = ∏ j ∈ s, (k j).choose (d j) :=
  d.prod_of_support_subset h _ fun _ _ ↦ Nat.choose_zero_right _

example [Fintype σ] (d k : σ →₀ ℕ) : hasseCoeff d k = ∏ j, (k j).choose (d j) :=
  hasseCoeff_eq_prod_of_support_subset (subset_univ _)

/-- Composition check: the project proof is a single mathlib call. -/
example [Fintype σ] (d k : σ →₀ ℕ) : hasseCoeff d k = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _

/-- Inlined at the single call site (`hasseCoeff_le_two_pow`) via `simp`. -/
example [Fintype σ] (d k : σ →₀ ℕ) : hasseCoeff d k = ∏ j, (k j).choose (d j) := by
  simp [hasseCoeff, Finsupp.prod_fintype]

end MvPolynomial

namespace Finsupp

variable {σ : Type*}

/-- Multi-index binomial coefficient (as proposed in the parent report). -/
def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose

theorem choose_eq_prod_of_support_subset {k d : σ →₀ ℕ} {s : Finset σ} (h : d.support ⊆ s) :
    k.choose d = ∏ j ∈ s, (k j).choose (d j) :=
  d.prod_of_support_subset h _ fun _ _ ↦ Nat.choose_zero_right _

theorem choose_eq_prod [Fintype σ] (k d : σ →₀ ℕ) : k.choose d = ∏ j, (k j).choose (d j) :=
  choose_eq_prod_of_support_subset (subset_univ _)

example [Fintype σ] (d k : σ →₀ ℕ) : MvPolynomial.hasseCoeff d k = k.choose d := rfl

end Finsupp
