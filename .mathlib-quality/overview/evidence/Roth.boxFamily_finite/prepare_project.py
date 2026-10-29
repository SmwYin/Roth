from pathlib import Path
import json,re
D=Path(__file__).resolve().parent;R=Path.cwd()
body=(D/'generic-body.lean.txt').read_text().replace('#check_failure Roth.boxFamily_finite\n','')
project='''
namespace Box245Project
open MvPolynomial
elab "box245Representation" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.boxFamily_eq_image_finsupp_aux)

theorem finite_generic {σ R : Type*} [CommSemiring R] (r : σ → ℕ)
    [Finite (Function.support r)] (t : (σ →₀ ℕ) → Set R) (ht : ∀ d, (t d).Finite) :
    (Box245Generic.family r t).Finite := by
  classical
  have hs : {d : σ →₀ ℕ | ∀ j, d j ≤ r j}.Finite := by
    change (Set.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))).Finite
    exact Set.finite_Iic _
  exact Box245Generic.finite_family_of_monomials r hs t ht

theorem finite_original {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (Roth.boxFamily r B).Finite := by
  simpa only [Roth.boxFamily, Box245Generic.family, Set.mem_Icc] using
    finite_generic r (fun _ ↦ Set.Icc (0 : ℤ) B) (fun _ ↦ Set.finite_Icc _ _)

theorem private_bridge_composition {σ : Type*} (r : σ → ℕ)
    [Finite (Function.support r)] (B : ℕ) : (Roth.boxFamily r B).Finite := by
  classical
  rw [box245Representation]
  exact (Finset.finite_toSet _).image _

theorem supplied_signature : @Roth.boxFamily_finite = @finite_original := rfl

theorem zero_coefficient_bound {σ : Type*} (r : σ → ℕ) : (Roth.boxFamily r 0).Finite := by
  change (Box245Generic.family r (fun _ ↦ Set.Icc (0 : ℤ) 0)).Finite
  rw [Box245Generic.zero_bound]
  exact Set.finite_singleton _

theorem zero_degree {σ : Type*} (B : ℕ) :
    (Roth.boxFamily (fun _ : σ ↦ 0) B).Finite := by
  let : Fintype (Function.support (fun _ : σ ↦ 0)) :=
    (show (Function.support (fun _ : σ ↦ 0)).Finite by simp).fintype
  exact finite_original _ B

theorem empty_variables (r : Empty → ℕ) (B : ℕ) : (Roth.boxFamily r B).Finite :=
  finite_original r B

theorem infinite_variables_finite_support (B : ℕ) :
    (Roth.boxFamily (fun i : ℕ ↦ if i = 0 then 2 else 0) B).Finite := by
  have hs : (Function.support (fun i : ℕ ↦ if i = 0 then 2 else 0)).Finite := by
    simp [Function.support]
  let : Fintype (Function.support (fun i : ℕ ↦ if i = 0 then 2 else 0)) := hs.fintype
  exact finite_original _ B

theorem support_needed : (Roth.boxFamily (fun _ : ℕ ↦ 1) 1).Infinite :=
  Box245Generic.infinite_family

theorem weaker_disjunction {σ : Type*} (r : σ → ℕ) (B : ℕ)
    (h : B = 0 ∨ (Function.support r).Finite) : (Roth.boxFamily r B).Finite := by
  rcases h with rfl | h
  · exact zero_coefficient_bound r
  · let : Fintype (Function.support r) := h.fintype
    exact finite_original r B

open Roth
'''
cs=json.load(open(D/'callers.json'))['callers'];assert len(cs)==1
caller=cs[0]['source']
old='(boxFamily_finite r B).fintype'
new='''(show (boxFamily r B).Finite from by
    rw [box245Representation]
    exact (Finset.finite_toSet _).image _).fintype'''
assert caller.count(old)==1
caller=caller.replace(old,new)
project+=caller+'''

theorem caller_signature :
    @Roth.exists_ne_modByMonic_eq = @Box245Project.exists_ne_modByMonic_eq := rfl

#print axioms finite_generic
#print axioms finite_original
#print axioms private_bridge_composition
#print axioms supplied_signature
#print axioms zero_coefficient_bound
#print axioms zero_degree
#print axioms empty_variables
#print axioms infinite_variables_finite_support
#print axioms support_needed
#print axioms weaker_disjunction
#print axioms exists_ne_modByMonic_eq
#print axioms caller_signature
#print Roth.boxFamily_finite
end Box245Project
'''
s=(D/'disk-prefix.lean.txt').read_text()+body+project
assert max(map(len,s.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print(s)
