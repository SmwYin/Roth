import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseCoeff_eq_zero_iff`:
1. composition from mathlib primitives (`Finsupp.prod_ne_zero_iff` (a simp lemma), `Nat.choose_ne_zero_iff`,
   `Finsupp.le_iff`);
2. the positive restatements `≠ 0 ↔ d ≤ k` and `0 < _ ↔ d ≤ k` (mirroring
   `Nat.choose_ne_zero_iff` / `Nat.choose_pos`);
3. the `Finsupp.choose k d` restatement proposed in the parent `hasseCoeff` report;
4. no typeclass is involved (the section `[CommSemiring R]` is not included). -/

namespace MvPolynomial

variable {σ : Type*}

/-- Composition: the nonzero form is a two-lemma `simp` chain. -/
theorem hasseCoeff_ne_zero_iff (d k : σ →₀ ℕ) : hasseCoeff d k ≠ 0 ↔ d ≤ k := by
  simp [hasseCoeff, Nat.choose_ne_zero_iff, Finsupp.le_iff]

theorem hasseCoeff_pos_iff (d k : σ →₀ ℕ) : 0 < hasseCoeff d k ↔ d ≤ k :=
  Nat.pos_iff_ne_zero.trans (hasseCoeff_ne_zero_iff d k)

/-- The project's form follows from the nonzero form in one line. -/
example (d k : σ →₀ ℕ) : hasseCoeff d k = 0 ↔ ¬d ≤ k := by
  rw [← hasseCoeff_ne_zero_iff, not_not]

end MvPolynomial

namespace Finsupp

variable {σ : Type*}

def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose

theorem choose_ne_zero_iff {k d : σ →₀ ℕ} : k.choose d ≠ 0 ↔ d ≤ k := by
  simp [choose, Nat.choose_ne_zero_iff, Finsupp.le_iff]

theorem choose_eq_zero_iff {k d : σ →₀ ℕ} : k.choose d = 0 ↔ ¬d ≤ k := by
  rw [← choose_ne_zero_iff, not_not]

theorem choose_pos_iff {k d : σ →₀ ℕ} : 0 < k.choose d ↔ d ≤ k :=
  Nat.pos_iff_ne_zero.trans choose_ne_zero_iff

end Finsupp
