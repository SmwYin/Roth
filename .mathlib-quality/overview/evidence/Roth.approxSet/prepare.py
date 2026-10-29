from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.approxSet';O=R/'.mathlib-quality/overview'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
order=json.load(open(O/'declaration-order.json'));assert order[266]['name']==N
put('canonical-snapshot.json',order);put('canonical-entry.json',order[266]);put('target-metadata.json',next(x for x in json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))if x['name']==N))
b=json.load(open(O/'evidence/shared/input-manifest.json'));put('input-manifest.json',b);xs=[]
for p,v in b['sources_and_pins'].items():
 h=sha(R/p);assert h==v['sha256'];xs.append(dict(path=p,sha256=h,bytes=(R/p).stat().st_size,match=True))
put('inputs.json',xs);(D/'baseline-build.txt').write_bytes((O/'evidence/shared/baseline-build.txt').read_bytes())
put('accepted-verdict-snapshot.json',json.load(open(O/'progress.json')))
for mod in ['Main','LeanEval']:(D/('source-'+mod+'.lean.txt')).write_bytes((R/('Roth/'+mod+'.lean')).read_bytes())
for n,args in [('source-search',['rg','--no-ignore','-n',r'\bapproxSet\b','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','-w','approxSet','--','Roth','Roth.lean']),('source-inventory',['rg','--files','--no-ignore','Roth']),('inline-search',['rg','--no-ignore','-n',r'approxSet|\|.*α.*-.*\|.*<.*1 /|\|.*x.*-.*\|.*<.*1 /','Roth','Roth.lean']),('local-literature',['rg','-n',r'\\section|reduced|q\^.*kappa|q.*>.*0',' .mathlib-quality/references/clean.tex'.strip()])]:
 z=subprocess.run(args,text=True,capture_output=True);put(n+'.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1730:1910])+'\n')
scratch=R/'.lake/roth-overview-session/GenWronskianChecks.lean';prefix='\n'.join(scratch.read_text().splitlines()[:15])+'\n';assert len(re.findall('^import ',prefix,re.M))==9
(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
s=(R/'Roth/Main.lean').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Approx267Original\nopen Roth',1).replace('end Roth','end Approx267Original');body=re.sub(r'\bapproxSet\b','replay',body)
full='''
#check @Roth.approxSet
set_option pp.all true in
#print Roth.approxSet
#print axioms Roth.approxSet
#print axioms Approx267Original.replay
example : @Roth.approxSet = @Approx267Original.replay := rfl
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.approxSet
  Lean.logInfo m!"APPROX267_BODY_CONSTANTS: {ci.value?.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"APPROX267_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"APPROX267_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
'''
names=[]
for d in order:
 if d['visibility']=='private':
  t='Lean.mkPrivateNameCore `'+d['file'][:-5].replace('/','.')+' `'+d['name']
  if len('    '+t+',')>100:t=t.replace(' `'+d['name'],'\n      `'+d['name'])
 else:t='`'+d['name']
 names.append('    '+t)
audit='''
namespace Approx267Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.approxSet
  let names : Array Lean.Name := #[
'''+',\n'.join(names)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "APPROX267_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "APPROX267_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"APPROX267_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"APPROX267_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"APPROX267_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"APPROX267_AUDIT_PRESENT: present={present}; values={values}"
end Approx267Audit
'''
whole=prefix+body+full+audit
assert max(map(len,whole.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(whole);scratch.write_text(whole)
print('Prepared original full Main replay',len(whole.splitlines()),'lines; fresh17; exact293; nine imports')
