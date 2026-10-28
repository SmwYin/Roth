from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
generic=(D/'isolated-executed.lean.txt').read_text().split('open MvPolynomial',1)[1]
generic=generic.replace('#check_failure Roth.boxFamily\n','')
body='''
namespace Box233Project
open MvPolynomial
theorem specialization {σ : Type*} (r : σ → ℕ) (B : ℕ) :
    Roth.boxFamily r B = Box233Generic.family r (fun _ ↦ Set.Icc (0 : ℤ) B) := rfl
theorem zero_bound {σ : Type*} (r : σ → ℕ) : Roth.boxFamily r 0 = {0} :=
  Box233Generic.zero_bound r
theorem infinite_family : (Roth.boxFamily (fun _ : ℕ ↦ 1) 1).Infinite :=
  Box233Generic.infinite_family
open Classical in
theorem generic_bridge {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    Roth.boxFamily r B = AddMonoidAlgebra.ofCoeff ''
      (↑((Finset.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))).finsupp
        fun _ ↦ Finset.Icc (0 : ℤ) B) : Set ((σ →₀ ℕ) →₀ ℤ)) := by
  rw [specialization]
  simpa only [Finset.coe_Icc, Finsupp.ofSupportFinite_coe] using
    Box233Generic.family_eq_image (Finsupp.ofSupportFinite r (Set.toFinite _))
    (fun _ ↦ Finset.Icc (0 : ℤ) B) (fun _ ↦ Finset.mem_Icc.2 ⟨le_rfl, by positivity⟩)
theorem interval_intersection {σ : Type*} (r : σ → ℕ) (B : ℕ) :
    Roth.boxFamily r B = {P | ∀ j, degreeOf j P ≤ r j} ∩
      ⋂ d, (fun P : MvPolynomial σ ℤ ↦ P.coeff d) ⁻¹' Set.Icc 0 (B : ℤ) := by
  ext P
  simp only [Roth.boxFamily, Set.mem_ofPred_eq, Set.mem_inter_iff, Set.mem_iInter,
    Set.mem_preimage, Set.mem_Icc]
theorem not_add_closed : ¬ ∀ P ∈ Roth.boxFamily (fun _ : Unit ↦ 0) 1,
    ∀ Q ∈ Roth.boxFamily (fun _ : Unit ↦ 0) 1, P + Q ∈ Roth.boxFamily (fun _ : Unit ↦ 0) 1 := by
  intro h
  have h1 : (1 : MvPolynomial Unit ℤ) ∈ Roth.boxFamily (fun _ ↦ 0) 1 := by
    constructor
    · simp
    · intro d
      simp only [MvPolynomial.coeff_one]
      split_ifs <;> norm_num
  have h2 := (h 1 h1 1 h1).2 0
  norm_num at h2
#check (Roth.boxFamily (σ := Type) (fun _ ↦ 1) 1)
#check (Roth.boxFamily (σ := Unit) (fun _ ↦ 1) 1)
#synth Membership (MvPolynomial Unit ℤ) (Set (MvPolynomial Unit ℤ))
#print axioms specialization
#print axioms zero_bound
#print axioms infinite_family
#print axioms generic_bridge
#print axioms interval_intersection
#print axioms not_add_closed
end Box233Project
'''
code=(D/'disk-prefix.lean.txt').read_text()+'open MvPolynomial'+generic+body
assert max(map(len,code.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print(code)
