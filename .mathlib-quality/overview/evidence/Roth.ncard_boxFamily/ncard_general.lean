import Roth.MainLemma

/-! Evidence for the `/overview` assessment of `Roth.ncard_boxFamily`.

1. General multivariate count (any `CommSemiring R`, finite monomial set `S`, per-monomial
   finite coefficient sets `U d`): the count is `∏ d ∈ S, #(U d)`. No order, no `ℤ`.
2. Interval specialisation over `ℤ` (per-monomial bounds `a d ≤ coeff ≤ b d`): multivariate
   analogue of `Polynomial.ncard_boxPoly`.
3. `Roth.ncard_boxFamily` re-derived from (2). -/

open MvPolynomial Finset

theorem MvPolynomial.ncard_setOf_support_subset_coeff_mem {σ R : Type*} [CommSemiring R]
    (S : Finset (σ →₀ ℕ)) (U : (σ →₀ ℕ) → Finset R) :
    {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d ∈ S, p.coeff d ∈ U d}.ncard =
      ∏ d ∈ S, #(U d) := by
  classical
  have : {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d ∈ S, p.coeff d ∈ U d} =
      AddMonoidAlgebra.ofCoeff '' (S.finsupp U : Set ((σ →₀ ℕ) →₀ R)) := by
    ext p
    constructor
    · rintro ⟨hp, hc⟩
      exact ⟨p.coeff, Finset.mem_finsupp_iff.2 ⟨fun d hd ↦ hp hd, hc⟩, rfl⟩
    · rintro ⟨c, hc, rfl⟩
      exact Finset.mem_finsupp_iff.1 hc
  rw [this, Set.ncard_image_of_injective _ AddMonoidAlgebra.ofCoeff_injective,
    Set.ncard_coe_finset, Finset.card_finsupp]

/-- Multivariate `ncard_boxPoly`: integer bounds per monomial. -/
theorem MvPolynomial.ncard_setOf_support_subset_coeff_mem_Icc {σ : Type*}
    (S : Finset (σ →₀ ℕ)) (a b : (σ →₀ ℕ) → ℤ) :
    {p : MvPolynomial σ ℤ | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧
      ∀ d ∈ S, a d ≤ p.coeff d ∧ p.coeff d ≤ b d}.ncard = ∏ d ∈ S, (b d + 1 - a d).toNat := by
  simpa [Finset.mem_Icc] using ncard_setOf_support_subset_coeff_mem S fun d ↦ Icc (a d) (b d)

/-- `Roth.ncard_boxFamily` as a corollary. -/
example {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (Roth.boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1) := by
  classical
  set R := Finsupp.ofSupportFinite r (Set.toFinite _)
  have hset : Roth.boxFamily r B = {p : MvPolynomial σ ℤ |
      (p.support : Set (σ →₀ ℕ)) ⊆ Iic R ∧ ∀ d ∈ Iic R, 0 ≤ p.coeff d ∧ p.coeff d ≤ B} := by
    ext W
    refine ⟨fun hW ↦ ⟨fun d hd ↦ mem_Iic.2 fun j ↦ (monomial_le_degreeOf j hd).trans (hW.1 j),
      fun d _ ↦ hW.2 d⟩, fun ⟨hs, hc⟩ ↦ ⟨fun j ↦ degreeOf_le_iff.2 fun d hd ↦
      (mem_Iic.1 (hs hd)) j, fun d ↦ ?_⟩⟩
    by_cases hd : d ∈ Iic R
    · exact hc d hd
    · simp [Finsupp.notMem_support_iff.1 (fun h ↦ hd (hs h))]
  rw [hset, ncard_setOf_support_subset_coeff_mem_Icc]
  simp only [sub_zero, prod_const, Finsupp.card_Iic, Nat.card_Iic]
  rw [show ((B : ℤ) + 1).toNat = B + 1 by omega]
  congr 1
  exact (finprod_eq_prod_of_mulSupport_subset _ fun j hj ↦ by
    simpa [R, Finsupp.ofSupportFinite_support, Function.support, Function.mulSupport]
      using hj).symm
