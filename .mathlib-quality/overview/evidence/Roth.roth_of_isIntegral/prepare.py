from pathlib import Path
import json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.roth_of_isIntegral');N='Roth.roth_of_isIntegral'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-entry.json',order[286])
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']==N);dump('target-metadata.json',target)
main=(R/'Roth/Main.lean').read_text();(D/'source-Main.lean.txt').write_text(main);(D/'source-LeanEval.lean.txt').write_text((R/'Roth/LeanEval.lean').read_text());(D/'target-excerpt.lean.txt').write_text(target['source']+'\n')
prefix=Path('/private/tmp/roth-overview/assess/Roth.exists_monic_aeval_eq_zero/disk-prefix.lean.txt').read_text();(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_text(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
terms=[]
for x in order:
 if x['visibility']=='private':
  t='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name']
  if len(t)>96:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 else:t='`'+x['name']
 terms.append('    '+t)
closure=main[main.index('-- Choose the polynomial, coefficient bound'):main.index('/-- Roth\'s theorem for irrational real algebraic integers')]
code=prefix+'\nnamespace Integral287Original\nopen Roth MvPolynomial\n'+closure+target['source'].replace('theorem roth_of_isIntegral','theorem replay')+'\nend Integral287Original\n\n'
code+='''#check @Roth.roth_of_isIntegral
set_option pp.all true in
#print Roth.roth_of_isIntegral
#print axioms Roth.roth_of_isIntegral
#print axioms Integral287Original.replay
example : @Roth.roth_of_isIntegral = @Integral287Original.replay := Subsingleton.elim _ _
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.roth_of_isIntegral
  let val := ci.value? (allowOpaque := true)
  Lean.logInfo m!"INT287_BODY_CONSTANTS: {val.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"INT287_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"INT287_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
namespace Integral287Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.roth_of_isIntegral
  let names : Array Lean.Name := #[
'''+',\n'.join(terms)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "INT287_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "INT287_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"INT287_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"INT287_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"INT287_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"INT287_AUDIT_PRESENT: present={present}; values={values}"
end Integral287Audit
'''
assert max(map(len,code.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(code)
dump('root-requests/original01.json',{'id':'original01','operation':'diagnostics','source':'original-executed.lean.txt','source_sha256':sha(D/'original-executed.lean.txt'),'receipt':'original-receipt.json','original_audit':True,'arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}})
for form,q in [('current','roth_of_isIntegral'),('standard','roth'),('abstract','LiouvilleWith')]:dump('root-requests/local-'+form+'.json',{'id':'local-'+form,'operation':'local_search','receipt':'formal-'+form+'-local.json','arguments':{'query':q,'project_root':str(R),'limit':40}})
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());dump('input-manifest.json',base)
inputs=[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size,'match':sha(R/p)==v['sha256']}for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);dump('inputs.json',inputs)
(D/'baseline-build.txt').write_text((R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
dump('preparation-checks.json',{'max_width':max(map(len,code.splitlines())),'all17_match':True,'native_scope':'exact target and five private helpers, imported public project ingredients','helpers':['exists_roth_parameters_aux','exists_roth_approximants_aux','one_lt_roth_eval_bound_aux','roth_product_bound_aux','roth_log_bound_aux']})
print('Prepared original01 + three local searches; exact width <=100; fresh17 pass')
