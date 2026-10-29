from pathlib import Path
import json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
P=D.parent/'LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'
N='LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def req(id,src,original=False,op='diagnostics'):
 dump('root-requests/'+id+'.json',dict(id=id,operation=op,source=src,source_sha256=sha(D/src),receipt=id+'-receipt.json',original_audit=original,arguments={} if op=='run_code' else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-entry.json',order[291])
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']==N);dump('target-metadata.json',target)
for f in ['Main','LeanEval']:(D/('source-'+f+'.lean.txt')).write_bytes((R/('Roth/'+f+'.lean')).read_bytes())
(D/'target-excerpt.lean.txt').write_text(target['source']+'\n')
prefix=(P/'disk-prefix.lean.txt').read_text();(D/'disk-prefix.lean.txt').write_text(prefix)
(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
lean=(R/'Roth/LeanEval.lean').read_text();helper=lean[lean.index('private lemma exists_pos'):lean.index('/-- For irrational')]
code=prefix+'\nnamespace Equivalence292Original\nopen Real\nopen LeanEval.NumberTheory.ThueSiegelRothProblem\n'+helper+target['source']+'\nend Equivalence292Original\n\n'
code+='''example : @LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff =
    @Equivalence292Original.isDiophantine_iff := Subsingleton.elim _ _
set_option pp.all true in
#print LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff
#print axioms LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff
#print axioms Equivalence292Original.isDiophantine_iff
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff
  let some val := ci.value? (allowOpaque := true) | throwError "D292_MISSING_TARGET_VALUE"
  Lean.logInfo m!"D292_BODY_CONSTANTS: {val.getUsedConstants.toList}"
  Lean.logInfo m!"D292_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"D292_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
namespace Equivalence292Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff
  let names : Array Lean.Name := #[
'''
terms=[]
for x in order:
 t=('Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name'])if x['visibility']=='private'else'`'+x['name']
 if len(t)>96:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 terms.append('    '+t)
code+=',\n'.join(terms)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "D292_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    let some ci := env.find? n | throwError "D292_NOT_LOADED: {n}"
    present := present + 1
    if ci.type.getUsedConstants.contains target then
      Lean.logInfo m!"D292_DIRECT_TYPE_CONSUMER: {n}"
    let some val := ci.value? (allowOpaque := true) | throwError "D292_MISSING_VALUE: {n}"
    values := values + 1
    if val.getUsedConstants.contains target then
      Lean.logInfo m!"D292_DIRECT_BODY_CONSUMER: {n}"
  Lean.logInfo m!"D292_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"D292_AUDIT_PRESENT: present={present}; values={values}"
end Equivalence292Audit
'''
assert max(map(len,code.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(code);req('original01','original-executed.lean.txt',True)
# Full actual caller with the entire equivalence proof substituted at its use.
body=target['source'].split(':= by\n',1)[1]
caller=next(x for x in meta if x['name'].endswith('.thueSiegelRoth'))['source']
caller=caller.replace('(isDiophantine_iff _h_irr).mpr','''(show IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2 from by
      have hx := _h_irr
'''+''.join('    '+l+'\n' for l in body.splitlines())+''').mpr''')
code=prefix+'\nnamespace Equivalence292Inline\nopen Real\nopen LeanEval.NumberTheory.ThueSiegelRothProblem\n'+helper+caller+'''
end Equivalence292Inline
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Equivalence292Inline.thueSiegelRoth := Subsingleton.elim _ _
#print axioms Equivalence292Inline.thueSiegelRoth
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Equivalence292Inline.thueSiegelRoth
  let some val := ci.value? (allowOpaque := true) | throwError "D292_INLINE_MISSING_VALUE"
  unless !(val.getUsedConstants.contains
      `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff) do
    throwError "D292_INLINE_RETAINED_TARGET"
  Lean.logInfo "D292_INLINE_TARGET_FREE"
'''
assert max(map(len,code.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(code);req('inline01','inline-executed.lean.txt')
for f,q in [('current','isDiophantine'),('standard','irrationality'),('abstract','LiouvilleWith')]:dump('root-requests/local-'+f+'.json',dict(id='local-'+f,operation='local_search',receipt='formal-'+f+'-local.json',arguments=dict(query=q,project_root=str(R),limit=50)))
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());dump('input-manifest.json',base)
inputs=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256'])for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);dump('inputs.json',inputs)
(D/'baseline-build.txt').write_bytes((R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_bytes())
dump('preparation-checks.json',dict(original_scope='exact target plus exact private helper lines20-39, fresh namespace',caller_scope='full thueSiegelRoth body with original equivalence proof inlined; helper copied exactly',all17_match=True))
print('Prepared original01, inline01, local-current/standard/abstract')
