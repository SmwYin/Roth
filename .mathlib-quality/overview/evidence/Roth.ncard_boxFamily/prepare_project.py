from pathlib import Path
import json,re
D=Path(__file__).resolve().parent;R=Path.cwd()
body=(D/'generic-body.lean.txt').read_text().replace('#check_failure Roth.ncard_boxFamily\n','')
p='''
namespace Box246Project
open MvPolynomial Roth
elab "box246Representation" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.boxFamily_eq_image_finsupp_aux)

theorem ncard_original {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1) := by
  classical
  have h := Box246Generic.constant_choices (Finsupp.ofSupportFinite r (Set.toFinite _))
    (Finset.Icc (0 : ℤ) B) (by simp)
  have hc : (Finset.Icc (0 : ℤ) B).card = B + 1 := by simp
  rw [hc] at h
  have he : (Box246Generic.family (Finsupp.ofSupportFinite r (Set.toFinite _))
      (fun _ ↦ Finset.Icc (0 : ℤ) B)) = boxFamily r B := by
    ext P
    simp only [Box246Generic.family, boxFamily, Set.mem_ofPred_eq, Finset.mem_Icc]
    rfl
  rw [he] at h
  rw [h]
  congr 1
  exact (finprod_eq_prod_of_mulSupport_subset _ fun j hj ↦ by
    simpa [Finsupp.ofSupportFinite_support, Function.support, Function.mulSupport] using hj).symm

theorem ncard_inline {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1) := by
  rw [box246Representation, Set.ncard_image_of_injective _
    AddMonoidAlgebra.ofCoeff_injective, Set.ncard_coe_finset, Finset.card_finsupp]
  simp only [Int.card_Icc, sub_zero, Finset.prod_const, Finsupp.card_Iic, Nat.card_Iic]
  congr 1
  exact (finprod_eq_prod_of_mulSupport_subset _ fun j hj ↦ by
    simpa [Finsupp.ofSupportFinite_support, Function.support, Function.mulSupport] using hj).symm

theorem supplied_signature : @Roth.ncard_boxFamily = @ncard_original := rfl

theorem zero_coefficient_bound {σ : Type*} (r : σ → ℕ) :
    (boxFamily r 0).ncard = (0 + 1) ^ ∏ᶠ j, (r j + 1) := by
  have hz : boxFamily r 0 = {0} := by
    ext P
    constructor
    · intro h
      apply Set.mem_singleton_iff.2
      apply MvPolynomial.ext
      intro d
      exact le_antisymm (h.2 d).2 (h.2 d).1
    · rintro rfl
      simp [boxFamily]
  simp [hz]

theorem zero_degree {σ : Type*} (B : ℕ) :
    (boxFamily (fun _ : σ ↦ 0) B).ncard = B + 1 := by
  let : Fintype (Function.support (fun _ : σ ↦ 0)) :=
    (show (Function.support (fun _ : σ ↦ 0)).Finite by simp).fintype
  simpa using ncard_original (fun _ : σ ↦ 0) B

theorem empty_variables (r : Empty → ℕ) (B : ℕ) : (boxFamily r B).ncard = B + 1 := by
  have he : r = fun _ ↦ 0 := funext fun x ↦ nomatch x
  subst r
  exact zero_degree B

theorem infinite_variables_finite_support (B : ℕ) :
    (boxFamily (Finsupp.single 0 2 : ℕ →₀ ℕ) B).ncard = (B + 1) ^ 3 := by
  classical
  have h := Box246Generic.constant_choices (Finsupp.single 0 2 : ℕ →₀ ℕ)
    (Finset.Icc (0 : ℤ) B) (by simp)
  simpa [Box246Generic.family, boxFamily] using h

theorem infinite_family : (boxFamily (fun _ : ℕ ↦ 1) 1).Infinite := by
  have hi : Function.Injective (fun i : ℕ ↦ (X i : MvPolynomial ℕ ℤ)) :=
    fun _ _ h ↦ MvPolynomial.X_injective h
  refine (Set.infinite_range_of_injective hi).mono (Set.range_subset_iff.2 ?_)
  intro i
  constructor
  · intro j
    by_cases h : i = j
    · subst j
      simp
    · simp [degreeOf_X_of_ne (Ne.symm h)]
  · intro d
    simp only [MvPolynomial.coeff_X]
    split_ifs <;> norm_num

theorem support_needed : (boxFamily (fun _ : ℕ ↦ 1) 1).ncard ≠
    (1 + 1) ^ ∏ᶠ _ : ℕ, (1 + 1) := by
  have hp : ∏ᶠ _ : ℕ, (1 + 1 : ℕ) = 1 := by
    apply finprod_of_infinite_mulSupport
    simpa [Function.mulSupport] using (Set.infinite_univ : (Set.univ : Set ℕ).Infinite)
  rw [infinite_family.ncard, hp]
  norm_num

theorem strict_no_direct {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ) :
    (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1) := by
  fail_if_success exact Finset.card_finsupp _ _
  fail_if_success exact Set.ncard_image_of_injective _ AddMonoidAlgebra.ofCoeff_injective
  fail_if_success solve | simp only [boxFamily]
  exact ncard_inline r B
'''
cs=json.load(open(D/'callers.json'))['callers'];assert len(cs)==1
caller=cs[0]['source'];old='ncard_boxFamily,'
new='''show (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1) from by
        rw [box246Representation, Set.ncard_image_of_injective _
          AddMonoidAlgebra.ofCoeff_injective, Set.ncard_coe_finset, Finset.card_finsupp]
        simp only [Int.card_Icc, sub_zero, Finset.prod_const, Finsupp.card_Iic, Nat.card_Iic]
        congr 1
        exact (finprod_eq_prod_of_mulSupport_subset _ fun j hj ↦ by
          simpa [Finsupp.ofSupportFinite_support, Function.support, Function.mulSupport]
            using hj).symm,'''
assert caller.count(old)==1;p+=caller.replace(old,new)+'''

theorem caller_signature :
    @Roth.exists_ne_modByMonic_eq = @Box246Project.exists_ne_modByMonic_eq := rfl

#check_failure Polynomial.card_eq_of_natDegree_le_of_coeff_le
'''
p+='\n'.join('#print axioms '+n for n in re.findall(r'^\s*theorem (\w+)',p,re.M))
p+='''
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.ncard_boxFamily
  for n in ci.type.getUsedConstants do
    if n.toString.startsWith "Roth." || n.toString.startsWith "_private.Roth." then
      Lean.logInfo m!"BOX246_TARGET_KERNEL_TYPE: {n}"
  let some v := ci.value? (allowOpaque := true) | throwError "BOX246_NO_TARGET_BODY"
  for n in v.getUsedConstants do
    if n.toString.startsWith "Roth." || n.toString.startsWith "_private.Roth." then
      Lean.logInfo m!"BOX246_TARGET_KERNEL_BODY: {n}"
  Lean.logInfo m!"BOX246_TARGET_COMPACT_BODY: {← Lean.Meta.ppExpr v}"
  let c ← Lean.getConstInfo `Box246Project.exists_ne_modByMonic_eq
  let some cv := c.value? (allowOpaque := true) | throwError "BOX246_NO_CALLER_BODY"
  unless !(cv.getUsedConstants.contains `Roth.ncard_boxFamily) do
    throwError "BOX246_INLINE_STILL_DIRECTLY_USES_TARGET"
  Lean.logInfo "BOX246_CALLER_INLINE_NO_DIRECT_TARGET: PASS"
end Box246Project
'''
s=(D/'disk-prefix.lean.txt').read_text()+body+p
assert max(map(len,s.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print(s)
