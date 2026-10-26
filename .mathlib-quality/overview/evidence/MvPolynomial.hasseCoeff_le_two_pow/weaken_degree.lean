import Roth.HasseDeriv

namespace MvPolynomial
variable {σ : Type*}

/-- Generalised form: no `Fintype σ`, no auxiliary box `r`; bound by `2 ^ |k|`. -/
theorem hasseCoeff_le_two_pow_degree (d k : σ →₀ ℕ) :
    hasseCoeff d k ≤ 2 ^ k.degree := by
  classical
  calc hasseCoeff d k = ∏ j ∈ d.support, (k j).choose (d j) := rfl
    _ ≤ ∏ j ∈ d.support, 2 ^ k j := Finset.prod_le_prod fun j _ ↦ Nat.choose_le_two_pow _ _
    _ = 2 ^ ∑ j ∈ d.support, k j := Finset.prod_pow_eq_pow_sum _ _ _
    _ ≤ 2 ^ k.degree := Nat.pow_le_pow_right two_pos <|
        Finset.sum_le_sum_of_ne_zero fun j _ hj ↦ Finsupp.mem_support_iff.2 hj

/-- The project statement recovered as a corollary. -/
example [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ} (hk : ∀ j, k j ≤ r j) :
    hasseCoeff d k ≤ 2 ^ (∑ j, r j) :=
  (hasseCoeff_le_two_pow_degree d k).trans <| Nat.pow_le_pow_right two_pos <| by
    rw [Finsupp.degree_eq_sum]; exact Finset.sum_le_sum fun j _ ↦ hk j

/-- Composition check: the current proof from mathlib + `hasseCoeff_eq_prod`. -/
example [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ} (hk : ∀ j, k j ≤ r j) :
    hasseCoeff d k ≤ 2 ^ (∑ j, r j) := by
  rw [hasseCoeff_eq_prod, ← Finset.prod_pow_eq_pow_sum]
  exact Finset.prod_le_prod fun j _ ↦
    (Nat.choose_le_two_pow _ _).trans (Nat.pow_le_pow_right two_pos (hk j))

end MvPolynomial
