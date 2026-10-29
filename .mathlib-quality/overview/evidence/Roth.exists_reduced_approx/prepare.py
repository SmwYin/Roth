from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx');N='Roth.exists_reduced_approx'
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-entry.json',order[273])
src=(R/'Roth/Main.lean').read_text();(D/'source-Main.lean.txt').write_text(src)
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']==N);dump('target-metadata.json',target)
helper=next(x for x in meta if x['name']=='Roth.approxSet_num_den_mem_aux');(D/'target-excerpt.lean.txt').write_text(target['source']+'\n');(D/'helper-excerpt.lean.txt').write_text(helper['source']+'\n')
prefix=Path('/private/tmp/roth-overview/assess/Roth.exists_monic_aeval_eq_zero/disk-prefix.lean.txt').read_text();(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_text(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
terms=[]
for x in order:
 if x['visibility']=='private':
  t='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name']
  if len(t)>96:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 else:t='`'+x['name']
 terms.append('    '+t)
code=prefix+'\nnamespace Reduced274Original\nopen Roth\n'+helper['source'].replace('private theorem','theorem')+'\n\n'+target['source'].replace('theorem exists_reduced_approx','theorem replay')+'\nend Reduced274Original\n\n'
code+='''#check @Roth.exists_reduced_approx
set_option pp.all true in
#print Roth.exists_reduced_approx
#print axioms Roth.exists_reduced_approx
#print axioms Reduced274Original.replay
example : @Roth.exists_reduced_approx = @Reduced274Original.replay := Subsingleton.elim _ _
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.exists_reduced_approx
  let val := ci.value? (allowOpaque := true)
  Lean.logInfo m!"REDUCED274_BODY_CONSTANTS: {val.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"REDUCED274_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"REDUCED274_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
namespace Reduced274Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.exists_reduced_approx
  let names : Array Lean.Name := #[
'''+',\n'.join(terms)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "REDUCED274_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "REDUCED274_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"REDUCED274_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"REDUCED274_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"REDUCED274_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"REDUCED274_AUDIT_PRESENT: present={present}; values={values}"
end Reduced274Audit
'''
(D/'original-executed.lean.txt').write_text(code)
dump('root-requests/original01.json',{'id':'original01','operation':'diagnostics','source':'original-executed.lean.txt','source_sha256':sha(D/'original-executed.lean.txt'),'receipt':'original-receipt.json','original_audit':True,'arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}})
for form,q in [('current','exists_reduced_approx'),('standard','infinite_rat_abs_sub'),('abstract','of_finite_fibers')]:dump('root-requests/local-'+form+'.json',{'id':'local-'+form,'operation':'local_search','receipt':'formal-'+form+'-local.json','arguments':{'query':q,'project_root':str(R),'limit':30}})
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());dump('input-manifest.json',base)
inputs=[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size,'match':sha(R/p)==v['sha256']}for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);dump('inputs.json',inputs)
(D/'baseline-build.txt').write_text(Path('/private/tmp/roth-overview/baseline-build.txt').read_text())
assert max(map(len,code.splitlines()))<=100
print('Prepared exact original focused replay, canonical293, hashes17, local searches3')
