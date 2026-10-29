from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_m');N='Roth.exists_m'
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-entry.json',order[274])
src=(R/'Roth/Main.lean').read_text();(D/'source-Main.lean.txt').write_text(src)
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']==N);dump('target-metadata.json',target)
(D/'target-excerpt.lean.txt').write_text(target['source']+'\n')
prefix=Path('/private/tmp/roth-overview/assess/Roth.exists_monic_aeval_eq_zero/disk-prefix.lean.txt').read_text();(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_text(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
terms=[]
for x in order:
 if x['visibility']=='private':
  t='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name']
  if len(t)>96:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 else:t='`'+x['name']
 terms.append('    '+t)
code=prefix+'\nnamespace Dimension275Original\nopen Roth\n'+target['source'].replace('theorem exists_m','theorem replay')+'\nend Dimension275Original\n\n'
code+='''#check @Roth.exists_m
set_option pp.all true in
#print Roth.exists_m
#print axioms Roth.exists_m
#print axioms Dimension275Original.replay
example : @Roth.exists_m = @Dimension275Original.replay := Subsingleton.elim _ _
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.exists_m
  let val := ci.value? (allowOpaque := true)
  Lean.logInfo m!"DIMENSION275_BODY_CONSTANTS: {val.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"DIMENSION275_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"DIMENSION275_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
namespace Dimension275Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.exists_m
  let names : Array Lean.Name := #[
'''+',\n'.join(terms)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "DIMENSION275_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "DIMENSION275_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"DIMENSION275_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"DIMENSION275_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"DIM275_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"DIMENSION275_AUDIT_PRESENT: present={present}; values={values}"
end Dimension275Audit
'''
(D/'original-executed.lean.txt').write_text(code)
dump('root-requests/original01.json',{'id':'original01','operation':'diagnostics','source':'original-executed.lean.txt','source_sha256':sha(D/'original-executed.lean.txt'),'receipt':'original-receipt.json','original_audit':True,'arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}})
for form,q in [('current','exists_m'),('standard','sqrt'),('abstract','exists_nat_gt')]:dump('root-requests/local-'+form+'.json',{'id':'local-'+form,'operation':'local_search','receipt':'formal-'+form+'-local.json','arguments':{'query':q,'project_root':str(R),'limit':30}})
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());dump('input-manifest.json',base)
inputs=[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size,'match':sha(R/p)==v['sha256']}for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);dump('inputs.json',inputs)
(D/'baseline-build.txt').write_text(Path('/private/tmp/roth-overview/baseline-build.txt').read_text())
# Original target source is exact, including its pre-existing width.
assert max(map(len,[l for l in code.splitlines() if not l.startswith('theorem replay')]))<=100
print('Prepared exact original focused replay, canonical293, hashes17, local searches3')
