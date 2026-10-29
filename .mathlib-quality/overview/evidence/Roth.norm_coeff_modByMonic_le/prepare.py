from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.norm_coeff_modByMonic_le'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'));row=next(x for x in rows if x['name']==N);put('target-metadata.json',row)
order=json.load(open(O/'declaration-order.json'));assert order[242]['name']==N;put('canonical-snapshot.json',order);put('canonical-entry.json',order[242]);put('accepted-verdict-snapshot.json',json.load(open(O/'progress.json')))
b=json.load(open(O/'evidence/shared/input-manifest.json'));put('input-manifest.json',b);xs=[]
for p,v in b['sources_and_pins'].items():
 h=sha(R/p);assert h==v['sha256'];xs.append(dict(path=p,sha256=h,baseline_sha256=h,match=True,bytes=(R/p).stat().st_size))
put('inputs.json',xs);(D/'baseline-build.txt').write_bytes((O/'evidence/shared/baseline-build.txt').read_bytes())
for mod in ['MainLemma','Main','LeanEval']:(D/('source-'+mod+'.lean.txt')).write_bytes((R/('Roth/'+mod+'.lean')).read_bytes())
(D/'target-excerpt.lean.txt').write_text(row['source']+'\n')
for n,args in [('source-search',['rg','--no-ignore','-n',r'\bnorm_coeff_modByMonic_le\b','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','-w','norm_coeff_modByMonic_le','--','Roth','Roth.lean']),('source-inventory',['rg','--files','--no-ignore','Roth']),('inline-audit',['rg','--no-ignore','-n',r'norm_coeff_modByMonic_le|16.*n.*\^ 2|eventually_nhds_iff','Roth','Roth.lean']),('local-literature',['rg','-n',r'leading.term|elimination|s-n|abc\(T\)',' .mathlib-quality/references/clean.tex'.strip()])]:
 z=subprocess.run(args,text=True,capture_output=True);put(n+'.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1360:1450])+'\n')
prefix='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:15])+'\n';assert len([l for l in prefix.splitlines()if l.startswith('import ')])==9
(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
s=(R/'Roth/MainLemma.lean').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Rem243Original\nopen Roth',1).replace('end Roth','end Rem243Original');body=re.sub(r'\bnorm_coeff_modByMonic_le\b','replay',body)
checks='\n'.join('#print axioms Rem243Original.'+n for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))
full='''\n#check @Roth.norm_coeff_modByMonic_le
set_option pp.all true in
#print Roth.norm_coeff_modByMonic_le
#print axioms Roth.norm_coeff_modByMonic_le
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.norm_coeff_modByMonic_le
  let val := ci.value? (allowOpaque := true)
  Lean.logInfo m!"REM243_BODY_CONSTANTS: {val.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"REM243_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"REM243_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
'''
names=[]
for d in order:
 if d['visibility']=='private':
  text='Lean.mkPrivateNameCore `'+d['file'][:-5].replace('/','.')+' `'+d['name']
  if len('    '+text+',')>100:text=text.replace(' `'+d['name'],'\n      `'+d['name'])
 else:text='`'+d['name']
 names.append('    '+text)
audit='''
namespace Rem243Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.norm_coeff_modByMonic_le
  let names : Array Lean.Name := #[
'''+',\n'.join(names)+''']
  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "REM243_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "REM243_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"REM243_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"REM243_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"REM243_AUDIT: requested={names.size}; unique={unique}"
  Lean.logInfo m!"REM243_AUDIT_PRESENT: present={present}; values={values}"
end Rem243Audit
'''
whole=prefix+body+'\n'+checks+'\n'+full+audit
assert max(map(len,whole.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
print('Prepared original',len(whole.splitlines()),'lines; fresh17; exact293; nine imports retained')
