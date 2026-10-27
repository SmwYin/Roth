from pathlib import Path
import json
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
s='''namespace MvPolynomial.DetCoeffConsumers
open Roth MvPolynomial
variable {τ : Type*} [Fintype τ]
open Lean Elab Term in
elab "detCoeffPrivateIndexSeparated" : term => do
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.Theta `Roth.index_separated_mul_le_aux)
'''
t=(R/'Roth/Theta.lean').read_text();a=t.index('theorem index_det_le');b=t.index('\nomit [DecidableEq τ]',a)
t=t[a:b].replace('theorem index_det_le','theorem caller').replace('abs_coeff_det_hasseDeriv_le _ R','DetCoeffGeneric.specialization _ R').replace('        ((abs_nonneg ((R.coeff 0 : ℤ) : ℝ)).trans (hR.2.2 0)) hR.2.2 d','        hR.2.2 d').replace('index_separated_mul_le_aux','detCoeffPrivateIndexSeparated')
s+=t+'\n#print axioms caller\n'
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']';(D/'canonical-audit-array.lean.txt').write_text(array+'\n')
s+='''run_cmd do
  let env ← Lean.getEnv
  '''+array+'''
  let unique : Nat := (names.toList.eraseDups).length
  unless names.size == 293 && unique == 293 do
    throwError "DET_COEFF_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "DET_COEFF_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.abs_coeff_det_hasseDeriv_le) then
          Lean.logInfo m!"DET_COEFF_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"DET_COEFF_AUDIT: requested={names.size}; unique={unique}"
  Lean.logInfo m!"DET_COEFF_AUDIT_PRESENT: present={present}; values={values}"
end MvPolynomial.DetCoeffConsumers
'''
s=s.replace(array,'\n    '.join([array[:array.index('#[')+2]]+[(n+(',' if k<len(names)-1 else ' ]')) for k,n in enumerate(names)]))
s=s.replace('Lean.mkPrivateNameCore `Roth.LeanEval `Roth.ratAbsIntDivNat_le_iff', 'Lean.mkPrivateNameCore `Roth.LeanEval\n      `Roth.ratAbsIntDivNat_le_iff')
# wrap every long private LeanEval name generically, preserving literal order
lines=[]
for line in s.splitlines():
 if len(line)>100 and 'Lean.mkPrivateNameCore `Roth.LeanEval ' in line:
  line=line.replace('Lean.mkPrivateNameCore `Roth.LeanEval ', 'Lean.mkPrivateNameCore `Roth.LeanEval\n      ')
 lines.append(line)
(D/'probe-consumers.lean.txt').write_text('\n'.join(lines)+'\n')
