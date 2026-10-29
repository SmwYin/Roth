from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'disk-prefix.lean.txt').read_text()+'''
namespace Box246Composition
open MvPolynomial Roth
elab "box246Representation" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.boxFamily_eq_image_finsupp_aux)

theorem image_count {σ R : Type*} [CommSemiring R] (s : Finset (σ →₀ ℕ))
    (t : (σ →₀ ℕ) → Finset R) :
    (AddMonoidAlgebra.ofCoeff '' (↑(s.finsupp t) : Set ((σ →₀ ℕ) →₀ R))).ncard =
      ∏ d ∈ s, (t d).card := by
  simp only [Set.ncard_image_of_injective _ AddMonoidAlgebra.ofCoeff_injective,
    Set.ncard_coe_finset, Finset.card_finsupp]

theorem simp_original {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1) := by
  classical
  have hp : (Finset.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))).card =
      ∏ᶠ j, (r j + 1) := by
    rw [Finsupp.card_Iic]
    simp only [Nat.card_Iic]
    exact (finprod_eq_prod_of_mulSupport_subset _ fun j hj ↦ by
      simpa [Finsupp.ofSupportFinite_support, Function.support, Function.mulSupport] using hj).symm
  have hc : ((B : ℤ) + 1).toNat = B + 1 := rfl
  simp only [box246Representation, Set.ncard_image_of_injective _
    AddMonoidAlgebra.ofCoeff_injective, Set.ncard_coe_finset, Finset.card_finsupp,
    Int.card_Icc, sub_zero, Finset.prod_const, hp, hc]

#print axioms image_count
#print axioms simp_original
end Box246Composition
'''
assert max(map(len,s.splitlines()))<=100
(D/'composition-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print(s)
