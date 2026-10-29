from pathlib import Path
import json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
N='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def req(id,src,original=False):
 dump('root-requests/'+id+'.json',dict(id=id,operation='diagnostics',source=src,source_sha256=sha(D/src),receipt=id+'-receipt.json',original_audit=original,arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-entry.json',order[289])
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']==N);dump('target-metadata.json',target)
for f in ['Main','LeanEval']:(D/('source-'+f+'.lean.txt')).write_bytes((R/('Roth/'+f+'.lean')).read_bytes())
(D/'target-excerpt.lean.txt').write_text(target['source']+'\n')
prefix=Path('/private/tmp/roth-overview/assess/Roth.roth/disk-prefix.lean.txt').read_bytes();(D/'disk-prefix.lean.txt').write_bytes(prefix);prefix=prefix.decode()
(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
terms=[]
for x in order:
 t=('Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name'])if x['visibility']=='private'else'`'+x['name']
 if len(t)>96:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 terms.append('    '+t)
code=prefix+'\nnamespace Diophantine290Original\nopen Real\n'+target['source']+'\nend Diophantine290Original\n\n'
code+='''example : LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine =
    Diophantine290Original.IsDiophantine := rfl
set_option pp.all true in
#print LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
#print axioms LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
#print axioms Diophantine290Original.IsDiophantine
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
  let some val := ci.value? (allowOpaque := true) | throwError "D290_MISSING_TARGET_VALUE"
  Lean.logInfo m!"D290_BODY_CONSTANTS: {val.getUsedConstants.toList}"
  Lean.logInfo m!"D290_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"D290_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
namespace Diophantine290Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
  let names : Array Lean.Name := #[
'''+',\n'.join(terms)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "D290_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    let some ci := env.find? n | throwError "D290_NOT_LOADED: {n}"
    present := present + 1
    if ci.type.getUsedConstants.contains target then
      Lean.logInfo m!"D290_DIRECT_TYPE_CONSUMER: {n}"
    let some val := ci.value? (allowOpaque := true) | throwError "D290_MISSING_VALUE: {n}"
    values := values + 1
    if val.getUsedConstants.contains target then
      Lean.logInfo m!"D290_DIRECT_BODY_CONSUMER: {n}"
  Lean.logInfo m!"D290_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"D290_AUDIT_PRESENT: present={present}; values={values}"
end Diophantine290Audit
'''
assert max(map(len,code.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(code);req('original01','original-executed.lean.txt',True)
lean=(R/'Roth/LeanEval.lean').read_text();lean=lean[lean.index('namespace LeanEval.'):].replace('LeanEval.NumberTheory.ThueSiegelRothProblem','Diophantine290Callers')
code=prefix+'\n'+lean+'''
example : LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine =
    Diophantine290Callers.IsDiophantine := rfl
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff =
    @Diophantine290Callers.isDiophantine_iff := Subsingleton.elim _ _
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Diophantine290Callers.thueSiegelRoth := Subsingleton.elim _ _
#print axioms Diophantine290Callers.isDiophantine_iff
#print axioms Diophantine290Callers.thueSiegelRoth
run_cmd Lean.Elab.Command.liftTermElabM do
  for n in [`Diophantine290Callers.isDiophantine_iff, `Diophantine290Callers.thueSiegelRoth] do
    let ci ← Lean.getConstInfo n
    let some val := ci.value? (allowOpaque := true) | throwError "D290_CALLER_MISSING_VALUE"
    let target := `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
    if ci.type.getUsedConstants.contains target || val.getUsedConstants.contains target then
      throwError "D290_CALLER_RETAINED_TARGET: {n}"
    Lean.logInfo m!"D290_CALLER_TARGET_FREE: {n}"
'''
assert max(map(len,code.splitlines()))<=100
(D/'callers-executed.lean.txt').write_text(code);req('callers01','callers-executed.lean.txt')
for f,q in [('current','IsDiophantine'),('standard','irrationality'),('abstract','LiouvilleWith')]:dump('root-requests/local-'+f+'.json',dict(id='local-'+f,operation='local_search',receipt='formal-'+f+'-local.json',arguments=dict(query=q,project_root=str(R),limit=40)))
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());dump('input-manifest.json',base)
inputs=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256'])for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);dump('inputs.json',inputs)
(D/'baseline-build.txt').write_bytes((R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_bytes())
dump('preparation-checks.json',dict(original_scope='exact target definition, no helpers',caller_scope='complete LeanEval module with namespace substitution only',all17_match=True))
print('Prepared original01, callers01, local-current, local-standard, local-abstract')
