import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.normOne_add_le`: the triangle inequality for the ℓ¹ coefficient norm
holds verbatim for `MvPolynomial.l1Norm` over any `[SeminormedCommRing R]` (parent verdict
target), and further for an ℓ¹ norm taken with respect to an `AbsoluteValue R ℝ` on a
`CommSemiring` (no negation needed). The project statement is recovered for `R = ℤ`. -/

open MvPolynomial

namespace Evidence81

section Seminormed

variable {σ R : Type*} [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

theorem l1Norm_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1Norm p = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

/-- The project proof, verbatim with `|·|` ↦ `‖·‖`. -/
theorem l1Norm_add_le (p q : MvPolynomial σ R) : l1Norm (p + q) ≤ l1Norm p + l1Norm q := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_add,
    l1Norm_eq_sum_of_support_subset (s := p.support ∪ q.support) Finset.subset_union_left,
    l1Norm_eq_sum_of_support_subset (s := p.support ∪ q.support) Finset.subset_union_right,
    ← Finset.sum_add_distrib]
  exact Finset.sum_le_sum fun d _ ↦ by simpa using norm_add_le (p.coeff d) (q.coeff d)

theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- Recovery of the exact project statement from the general one. -/
example (P Q : MvPolynomial σ ℤ) : Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q := by
  simpa only [l1Norm_int_eq_normOne] using l1Norm_add_le P Q

end Seminormed

section AbsoluteValue

-- Floor: an ℓ¹ norm w.r.t. an absolute value on a commutative semiring (e.g. `ℕ`).
variable {σ R : Type*} [CommSemiring R] (v : AbsoluteValue R ℝ)

noncomputable def l1NormAbv (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, v (p.coeff d)

theorem l1NormAbv_eq_sum_of_support_subset {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)}
    (hs : p.support ⊆ s) : l1NormAbv v p = ∑ d ∈ s, v (p.coeff d) :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

theorem l1NormAbv_add_le (p q : MvPolynomial σ R) :
    l1NormAbv v (p + q) ≤ l1NormAbv v p + l1NormAbv v q := by
  classical
  rw [l1NormAbv_eq_sum_of_support_subset v support_add,
    l1NormAbv_eq_sum_of_support_subset v (s := p.support ∪ q.support) Finset.subset_union_left,
    l1NormAbv_eq_sum_of_support_subset v (s := p.support ∪ q.support) Finset.subset_union_right,
    ← Finset.sum_add_distrib]
  exact Finset.sum_le_sum fun d _ ↦ by simpa using v.add_le (p.coeff d) (q.coeff d)

end AbsoluteValue

end Evidence81
