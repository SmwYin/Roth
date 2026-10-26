import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` (overview / mathlibable). -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Order-theoretic hypothesis `Disjoint d e` (mathlib idiom, via `Finsupp.disjoint_iff`). -/
example {d e : σ →₀ ℕ} (h : Disjoint d e) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P :=
  hasseDeriv_hasseDeriv_of_disjoint (Finsupp.disjoint_iff.1 h) P

/-- (2) Operator form, matching `Polynomial.hasseDeriv_comp`. -/
example {d e : σ →₀ ℕ} (h : Disjoint d.support e.support) :
    (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e = hasseDeriv (d + e) :=
  LinearMap.ext (hasseDeriv_hasseDeriv_of_disjoint h)

/-- (3) Sharpness over `ℕ`: the binomial factor is `1` only for disjoint supports, so the
hypothesis is exactly the characteristic-free condition. -/
example {d e : σ →₀ ℕ} (h1 : hasseCoeff d (d + e) = 1) : Disjoint d.support e.support := by
  classical
  refine Finset.disjoint_left.2 fun j hd he ↦ ?_
  have hpos : ∀ i ∈ d.support, 1 ≤ ((d + e) i).choose (d i) := fun i _ ↦
    Nat.choose_pos (by simp)
  have := (Finset.prod_eq_one_iff_of_one_le hpos).1 h1 j hd
  rw [Finsupp.mem_support_iff] at hd he
  simp only [Finsupp.coe_add, Pi.add_apply, Nat.choose_eq_one_iff] at this
  omega

/-- (4) Weakening in positive characteristic: only `(hasseCoeff d (d + e) : R) = 1` is needed. -/
example {d e : σ →₀ ℕ} (h : (hasseCoeff d (d + e) : R) = 1) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := by
  rw [hasseDeriv_hasseDeriv, h, one_smul]

/-- (5) Composition from `hasseDeriv_hasseDeriv` by `simp` alone does not close it. -/
example {d e : σ →₀ ℕ} (h : Disjoint d.support e.support) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := by
  fail_if_success (simp [hasseDeriv_hasseDeriv, hasseCoeff]; done)
  exact hasseDeriv_hasseDeriv_of_disjoint h P

end MvPolynomial
