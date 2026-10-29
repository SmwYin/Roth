from pathlib import Path
import json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
N='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def req(i,s,orig=False,op='diagnostics'):
 dump('root-requests/'+i+'.json',dict(id=i,operation=op,source=s,source_sha256=sha(D/s),receipt=i+'-receipt.json',original_audit=orig,arguments={} if op=='run_code' else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-entry.json',order[292])
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']==N);dump('target-metadata.json',target)
for f in ['Main','LeanEval']:(D/('source-'+f+'.lean.txt')).write_bytes((R/('Roth/'+f+'.lean')).read_bytes())
(D/'target-excerpt.lean.txt').write_text(target['source']+'\n')
prefix=(D.parent/'LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/disk-prefix.lean.txt').read_text();(D/'disk-prefix.lean.txt').write_text(prefix)
(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
code=prefix+'\nnamespace Endpoint293Original\nopen Real\nopen LeanEval.NumberTheory.ThueSiegelRothProblem\n'+target['source']+'\nend Endpoint293Original\n\n'
code+='''example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Endpoint293Original.thueSiegelRoth := Subsingleton.elim _ _
set_option pp.all true in
#print LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth
#print axioms LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth
#print axioms Endpoint293Original.thueSiegelRoth
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth
  let some val := ci.value? (allowOpaque := true) | throwError "D293_MISSING_TARGET_VALUE"
  Lean.logInfo m!"D293_BODY_CONSTANTS: {val.getUsedConstants.toList}"
  Lean.logInfo m!"D293_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"D293_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
namespace Endpoint293Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth
  let names : Array Lean.Name := #[
'''
terms=[]
for x in order:
 t=('Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name'])if x['visibility']=='private'else'`'+x['name']
 if len(t)>96:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 terms.append('    '+t)
code+=',\n'.join(terms)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "D293_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    let some ci := env.find? n | throwError "D293_NOT_LOADED: {n}"
    present := present + 1
    if ci.type.getUsedConstants.contains target then
      Lean.logInfo m!"D293_DIRECT_TYPE_CONSUMER: {n}"
    let some val := ci.value? (allowOpaque := true) | throwError "D293_MISSING_VALUE: {n}"
    values := values + 1
    if val.getUsedConstants.contains target then
      Lean.logInfo m!"D293_DIRECT_BODY_CONSUMER: {n}"
  Lean.logInfo m!"D293_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"D293_AUDIT_PRESENT: present={present}; values={values}"
end Endpoint293Audit
'''
assert max(map(len,code.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(code);req('original01','original-executed.lean.txt',True)
for f,q in [('current','thueSiegelRoth'),('standard','IsAlgebraic'),('abstract','LiouvilleWith')]:dump('root-requests/local-'+f+'.json',dict(id='local-'+f,operation='local_search',receipt='formal-'+f+'-local.json',arguments=dict(query=q,project_root=str(R),limit=50)))
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());dump('input-manifest.json',base)
inputs=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256'])for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);dump('inputs.json',inputs)
(D/'baseline-build.txt').write_bytes((R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_bytes())
dump('preparation-checks.json',dict(original_scope='exact target only, fresh namespace, imported public dependencies, no private helper closure needed',caller_scope='zero actual source callers; full293 audit requested',all17_match=True))
print('Prepared original01, local-current/standard/abstract')
