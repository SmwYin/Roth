from pathlib import Path
import json
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
s=(D/'probe-generic.lean.txt').read_text()
raw='''#check_failure Roth.normOne_hasseDeriv_le
#check_failure MvPolynomial.hasseDeriv
'''+s[:s.index('theorem bound')].replace('MvPolynomial.NormHasseGeneric','NormHasseRaw')+'''theorem finiteMonomialBound [Fintype σ] (p : AddGroupSeminorm R)
    (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) :
    size p (∑ k ∈ P.support,
      monomial (k - d) (((∏ j, (k j).choose (d j) : ℕ) : R) * P.coeff k)) ≤
      2 ^ (∑ j, r j) * size p P := by
  classical
  refine (size_sum p _ _).trans ?_
  rw [size, Finsupp.sum, Finset.mul_sum]
  refine Finset.sum_le_sum fun k hk ↦ ?_
  rw [size_monomial]
  have hc : (∏ j, (k j).choose (d j) : ℕ) ≤ 2 ^ (∑ j, r j) := by
    rw [← Finset.prod_pow_eq_pow_sum]
    exact Finset.prod_le_prod fun j _ ↦
      (Nat.choose_le_two_pow _ _).trans
        (Nat.pow_le_pow_right two_pos ((monomial_le_degreeOf j hk).trans (hP j)))
  have hc' : ((∏ j, (k j).choose (d j) : ℕ) : ℝ) ≤ 2 ^ (∑ j, r j) := by
    exact_mod_cast hc
  exact (scalarBound p _ _).trans (mul_le_mul_of_nonneg_right hc' (apply_nonneg p _))
#check @Polynomial.hasseDeriv_coeff
#check @Finsupp.sum_of_support_subset
#check @Finset.le_sum_of_subadditive
#check @Nat.choose_le_two_pow
#print axioms finiteMonomialBound
end NormHasseRaw
'''
(D/'probe-raw.lean.txt').write_text(raw)
s=(R/'Roth/CoeffNorm.lean').read_text();start=s.index('theorem abs_coeff_det_hasseDeriv_le');end=s.index('\nend Roth',start)
c=s[start:end].replace('theorem abs_coeff_det_hasseDeriv_le','theorem determinant_replay').replace('(normOne_hasseDeriv_le _ P hP)','(MvPolynomial.NormHasseGeneric.specialization _ P hP)')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 if len('    '+n+',')>100:
  module,decl=n.rsplit(' ',1);n=module+'\n      '+decl
 names.append('    '+n)
a='  let names : Array Lean.Name := #[\n'+',\n'.join(names)+']\n';(D/'canonical-audit-array.lean.txt').write_text(a)
audit='''run_cmd do
  let env ← Lean.getEnv
'''+a+'''  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "Canonical audit must contain 293 unique names"
  Lean.logInfo m!"NORM_HASSE_AUDIT_UNIQUE: {unique}"
  let mut present : Nat := 0
  let mut withValue : Nat := 0
  for n in names do
    match env.find? n with
    | none => Lean.logInfo m!"NORM_HASSE_AUDIT_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        withValue := withValue + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.normOne_hasseDeriv_le) then
          Lean.logInfo m!"NORM_HASSE_DIRECT_PROOF_CONSUMER: {n}"
  Lean.logInfo
    m!"NORM_HASSE_AUDIT: requested={names.size}; present={present}; values={withValue}"
'''
code='namespace MvPolynomial.NormHasseConsumers\nopen Roth MvPolynomial\n'+c+'\n#print axioms determinant_replay\n'+audit+'end MvPolynomial.NormHasseConsumers\n'
(D/'probe-consumers.lean.txt').write_text(code)
for f in ['probe-raw.lean.txt','probe-generic.lean.txt','probe-consumers.lean.txt']:
 assert all(len(x)<=100 for x in (D/f).read_text().splitlines()),f
