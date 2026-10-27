from pathlib import Path
import json
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
g=(D/'probe-generic.lean.txt').read_text()
scalar=g[g.index('theorem scalarBound'):g.index('theorem bound')]
raw='''#check_failure Roth.abs_coeff_hasseDeriv_le
#check_failure MvPolynomial.hasseDeriv
namespace AbsHasseRaw
variable {σ R : Type*} [CommRing R]
'''+scalar+'''theorem binomialBound [Fintype σ] (p : AddGroupSeminorm R)
    (d k : σ →₀ ℕ) (r : σ → ℕ) (hk : ∀ j, k j ≤ r j)
    (a : R) {B : ℝ} (ha : p a ≤ B) :
    p (((∏ j, (k j).choose (d j) : ℕ) : R) * a) ≤ 2 ^ (∑ j, r j) * B := by
  have hc : (∏ j, (k j).choose (d j) : ℕ) ≤ 2 ^ (∑ j, r j) := by
    rw [← Finset.prod_pow_eq_pow_sum]
    exact Finset.prod_le_prod fun j _ ↦
      (Nat.choose_le_two_pow _ _).trans (Nat.pow_le_pow_right two_pos (hk j))
  have hc' : ((∏ j, (k j).choose (d j) : ℕ) : ℝ) ≤ 2 ^ (∑ j, r j) := by
    exact_mod_cast hc
  exact (scalarBound p _ _).trans
    (mul_le_mul hc' ha (apply_nonneg p a) (by positivity))
#check @Polynomial.hasseDeriv_coeff
#check @Nat.choose_le_two_pow
#check @Finset.prod_le_prod
#check @MvPolynomial.monomial_le_degreeOf
#check @norm_nsmul_le
#print axioms scalarBound
#print axioms binomialBound
end AbsHasseRaw
'''
(D/'probe-raw.lean.txt').write_text(raw)
s=(R/'Roth/MainLemma.lean').read_text()
callers=[]
for name in ['abs_eval_iterated_hasseDeriv_lt_aux','abs_coeff_diag_hasseDeriv_modByMonic_le_aux']:
 start=s.index('private lemma '+name);end=s.index('\nprivate lemma ',start+1)
 c=s[start:end].replace('private lemma '+name,'theorem '+name+'_replay\n')
 c=c.replace('abs_coeff_hasseDeriv_le','MvPolynomial.AbsHasseGeneric.specialization')
 c=c.replace('(MvPolynomial.AbsHasseGeneric.specialization i _ hdQ (MvPolynomial.AbsHasseGeneric.specialization k P hP hc))', '(MvPolynomial.AbsHasseGeneric.specialization i _ hdQ\n      (MvPolynomial.AbsHasseGeneric.specialization k P hP hc))')
 c=c.replace('    {P : MvPolynomial σ ℤ} {r : σ → ℕ} {A B : ℝ} (hA', '    {P : MvPolynomial σ ℤ} {r : σ → ℕ} {A B : ℝ}\n    (hA')
 callers.append(c)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 if len('    '+n+',')>100:
  module,decl=n.rsplit(' ',1);n=module+'\n      '+decl
 names.append('    '+n)
array='  let names : Array Lean.Name := #[\n'+',\n'.join(names)+']\n'
(D/'canonical-audit-array.lean.txt').write_text(array)
audit='''run_cmd do
  let env ← Lean.getEnv
'''+array+'''  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "Canonical audit must contain 293 unique names"
  Lean.logInfo m!"ABS_HASSE_AUDIT_UNIQUE: {unique}"
  let mut present : Nat := 0
  let mut withValue : Nat := 0
  for n in names do
    match env.find? n with
    | none => Lean.logInfo m!"ABS_HASSE_AUDIT_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        withValue := withValue + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.abs_coeff_hasseDeriv_le) then
          Lean.logInfo m!"ABS_HASSE_DIRECT_PROOF_CONSUMER: {n}"
  Lean.logInfo
    m!"ABS_HASSE_AUDIT: requested={names.size}; present={present}; values={withValue}"
'''
code='namespace MvPolynomial.AbsHasseConsumers\nopen Roth MvPolynomial\n'+\
 '\n'.join(callers)+'\n'+\
 '\n'.join('#print axioms '+n+'_replay' for n in [
 'abs_eval_iterated_hasseDeriv_lt_aux','abs_coeff_diag_hasseDeriv_modByMonic_le_aux'])+\
 '\n'+audit+'end MvPolynomial.AbsHasseConsumers\n'
for name,snippet in [('probe-consumers.lean.txt',code),('probe-raw.lean.txt',raw)]:
 assert all(len(x)<=100 for x in snippet.splitlines()),[(i+1,len(x)) for i,x in enumerate(snippet.splitlines()) if len(x)>100]
 (D/name).write_text(snippet)
