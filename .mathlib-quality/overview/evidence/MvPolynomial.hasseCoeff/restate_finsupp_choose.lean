import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseCoeff`:
1. the proposed mathlib-idiomatic restatement `Finsupp.choose k d` (top index first, as in
   `Nat.choose`) agrees definitionally with `hasseCoeff d k` and the vanishing lemma ports;
2. the upper index can be weakened to an arbitrary function `σ → ℕ` (the product is over
   `d.support` only), and the vanishing lemma still compiles. -/

namespace Finsupp

variable {σ : Type*}

/-- Multi-index binomial coefficient `binom(k, d) = ∏ j, (k j).choose (d j)`. -/
def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose

example (d k : σ →₀ ℕ) : k.choose d = MvPolynomial.hasseCoeff d k := rfl

theorem choose_eq_zero_iff (k d : σ →₀ ℕ) : k.choose d = 0 ↔ ¬d ≤ k :=
  MvPolynomial.hasseCoeff_eq_zero_iff d k

end Finsupp

namespace Weaken

variable {σ : Type*}

/-- Upper index weakened to a plain function. -/
def hasseCoeff' (d : σ →₀ ℕ) (k : σ → ℕ) : ℕ := d.prod fun j ↦ (k j).choose

example (d k : σ →₀ ℕ) : hasseCoeff' d k = MvPolynomial.hasseCoeff d k := rfl

theorem hasseCoeff'_eq_zero_iff (d : σ →₀ ℕ) (k : σ → ℕ) :
    hasseCoeff' d k = 0 ↔ ∃ j, k j < d j := by
  simp only [hasseCoeff', Finsupp.prod, Finset.prod_eq_zero_iff, Nat.choose_eq_zero_iff,
    Finsupp.mem_support_iff]
  exact ⟨fun ⟨j, _, h⟩ ↦ ⟨j, h⟩, fun ⟨j, h⟩ ↦ ⟨j, by omega, h⟩⟩

end Weaken
