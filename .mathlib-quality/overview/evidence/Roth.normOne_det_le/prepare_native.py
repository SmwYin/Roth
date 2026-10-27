from pathlib import Path
import json,re
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
src=(R/'Roth/CoeffNorm.lean').read_text()
prefix='namespace MvPolynomial.NormDetConsumers\nopen Roth MvPolynomial\nvariable {σ : Type*}\n'
start=src.index('theorem normOne_det_le ');end=src.index('\n/-- Coefficient bound',start)
body=src[start:end].replace('theorem normOne_det_le {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ}', 'theorem generalIndex {n : Type*} [Fintype n] [DecidableEq n]\n    (M : Matrix n n (MvPolynomial σ ℤ)) {C : ℝ}')
body=body.replace(' : normOne M.det ≤', ' :\n    normOne M.det ≤')
body=body.replace('l.factorial','(Fintype.card n).factorial').replace('C ^ l','C ^ Fintype.card n').replace('Equiv.Perm (Fin l)','Equiv.Perm n')
caller=src[src.index('theorem abs_coeff_det_hasseDeriv_le '):src.index('\nend Roth')]
caller=caller.replace('theorem abs_coeff_det_hasseDeriv_le ','theorem determinant_inline ').replace('normOne_det_le _','generalIndex _')
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
  Lean.logInfo m!"DET_AUDIT_UNIQUE: {unique}"
  let mut present : Nat := 0
  let mut withValue : Nat := 0
  for n in names do
    match env.find? n with
    | none => Lean.logInfo m!"DET_AUDIT_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        withValue := withValue + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.normOne_det_le) then
          Lean.logInfo m!"DET_DIRECT_PROOF_CONSUMER: {n}"
  Lean.logInfo
    m!"DET_AUDIT_CANONICAL: requested={names.size}; present={present}; values={withValue}"
'''
code=prefix+body+'\n#print axioms generalIndex\n'+caller+'\n#print axioms determinant_inline\n'+audit+'end MvPolynomial.NormDetConsumers\n'
assert all(len(x)<=100 for x in code.splitlines()),[(i+1,len(x),x) for i,x in enumerate(code.splitlines()) if len(x)>100]
(D/'probe-consumers.lean.txt').write_text(code)
print('consumer and canonical293 probe prepared')
