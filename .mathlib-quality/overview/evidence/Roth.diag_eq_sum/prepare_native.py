from pathlib import Path
import json
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
raw='''#check_failure Roth.diag_eq_sum
namespace DiagSumRaw
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
theorem generic (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
      ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) := by
  classical
  rw [aeval_def, eval₂_eq]
  simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial]
theorem existingExpansion (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
      ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) := by
  classical
  simpa only [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial] using
    (eval₂_eq (algebraMap R (Polynomial R)) (fun _ ↦ Polynomial.X) P)
#check @MvPolynomial.eval₂_eq
#check @MvPolynomial.aeval_def
#check @Finset.prod_pow_eq_pow_sum
#check @Finsupp.degree_apply
#check @Polynomial.algebraMap_eq
#check @Polynomial.C_mul_X_pow_eq_monomial
#print axioms generic
#print axioms existingExpansion
end DiagSumRaw
'''
(D/'probe-raw.lean.txt').write_text(raw)
s=(R/'Roth/CoeffNorm.lean').read_text();cs=[]
for name,nxt in [('abs_coeff_diag_le','/-- The degree'),('natDegree_diag_le','/-- Evaluating')]:
 start=s.index('theorem '+name);end=s.index(nxt,start)
 c=s[start:end].replace('theorem '+name,'theorem '+name+'_replay').replace('rw [diag_eq_sum','rw [show diag P = _ from DiagSumRaw.existingExpansion P')
 cs.append(c)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 if len('    '+n+',')>100:
  m,d=n.rsplit(' ',1);n=m+'\n      '+d
 names.append('    '+n)
a='  let names : Array Lean.Name := #[\n'+',\n'.join(names)+']\n';(D/'canonical-audit-array.lean.txt').write_text(a)
audit='''run_cmd do
  let env ← Lean.getEnv
'''+a+'''  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "Canonical audit must contain 293 unique names"
  Lean.logInfo m!"DIAG_SUM_AUDIT_UNIQUE: {unique}"
  let mut present : Nat := 0
  let mut withValue : Nat := 0
  for n in names do
    match env.find? n with
    | none => Lean.logInfo m!"DIAG_SUM_AUDIT_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        withValue := withValue + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.diag_eq_sum) then
          Lean.logInfo m!"DIAG_SUM_DIRECT_PROOF_CONSUMER: {n}"
  Lean.logInfo
    m!"DIAG_SUM_AUDIT: requested={names.size}; present={present}; values={withValue}"
'''
(D/'probe-consumers.lean.txt').write_text('namespace DiagSumConsumers\nopen Roth MvPolynomial\n'+''.join(cs)+'\n#print axioms abs_coeff_diag_le_replay\n#print axioms natDegree_diag_le_replay\n'+audit+'end DiagSumConsumers\n')
