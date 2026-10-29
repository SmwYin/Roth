from pathlib import Path
import json,re,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.reduction';O=R/'.mathlib-quality/overview'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
order=json.loads((O/'declaration-order.json').read_text());assert order[270]['name']==N
put('canonical-snapshot.json',order);put('canonical-entry.json',order[270])
meta=next(x for x in json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))if x['name']==N);put('target-metadata.json',meta)
b=json.load(open(O/'evidence/shared/input-manifest.json'));put('input-manifest.json',b);xs=[]
for p,v in b['sources_and_pins'].items():
 h=sha(R/p);assert h==v['sha256'];xs.append(dict(path=p,sha256=h,bytes=(R/p).stat().st_size,match=True))
put('inputs.json',xs);(D/'baseline-build.txt').write_bytes((O/'evidence/shared/baseline-build.txt').read_bytes());put('accepted-verdict-snapshot.json',json.load(open(O/'progress.json')))
for m in ['Main','LeanEval']:(D/('source-'+m+'.lean.txt')).write_bytes((R/('Roth/'+m+'.lean')).read_bytes())
for n,args in [('source-search',['rg','--no-ignore','-n',r'\breduction\b','Roth','Roth.lean']),('source-inventory',['rg','--files','--no-ignore','Roth']),('inline-search',['rg','--no-ignore','-n',r'of_finite_fibers|finite_toSet|Finset.Icc|den_le_finite','Roth','Roth.lean']),('local-literature',['rg','-n',r'large enough|kappa|absor|M/q|sufficiently','.mathlib-quality/references/clean.tex'])]:
 z=subprocess.run(args,text=True,capture_output=True);put(n+'.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1174:1187]+['']+loc.read_text().splitlines()[1576:1587])+'\n')
scratch=R/'.lake/roth-overview-session/GenWronskianChecks.lean';prefix='\n'.join(scratch.read_text().splitlines()[:15])+'\n';assert len(re.findall('^import ',prefix,re.M))==9
(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
target=meta['source'];assert target in(R/'Roth/Main.lean').read_text()
body='namespace Reduction271Original\nopen Roth\n'+target.replace('theorem reduction','theorem replay',1)+'\nend Reduction271Original\n'
full='''
#check @Roth.reduction
set_option pp.all true in
#print Roth.reduction
#print axioms Roth.reduction
#print axioms Reduction271Original.replay
example : @Roth.reduction = @Reduction271Original.replay := Subsingleton.elim _ _
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.reduction
  Lean.logInfo m!"REDUCTION271_BODY_CONSTANTS: {ci.value? (allowOpaque := true) |>.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"REDUCTION271_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"REDUCTION271_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
'''
full=full.replace('  Lean.logInfo m!"REDUCTION271_BODY_CONSTANTS: {ci.value? (allowOpaque := true) |>.map (·.getUsedConstants.toList)}"','  let val := ci.value? (allowOpaque := true)\n  Lean.logInfo m!"REDUCTION271_BODY_CONSTANTS: {val.map (·.getUsedConstants.toList)}"')
names=[]
for d in order:
 if d['visibility']=='private':
  t='Lean.mkPrivateNameCore `'+d['file'][:-5].replace('/','.')+' `'+d['name']
  if len('    '+t+',')>100:t=t.replace(' `'+d['name'],'\n      `'+d['name'])
 else:t='`'+d['name']
 names.append('    '+t)
audit='''
namespace Reduction271Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.reduction
  let names : Array Lean.Name := #[
'''+',\n'.join(names)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "REDUCTION271_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "REDUCTION271_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"REDUCTION271_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"REDUCTION271_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"REDUCTION271_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"REDUCTION271_AUDIT_PRESENT: present={present}; values={values}"
end Reduction271Audit
'''
whole=prefix+body+full+audit
for line in whole.splitlines():
 if len(line)>100: print(len(line),line)
(D/'original-executed.lean.txt').write_text(whole)
print('Prepared exact target replay only; no private helpers needed; fresh17; exact293; disk9')
