from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.boxFamily_finite'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'));row=next(x for x in rows if x['name']==N);put('target-metadata.json',row)
order=json.load(open(O/'declaration-order.json'));assert order[244]['name']==N;put('canonical-snapshot.json',order);put('canonical-entry.json',order[244]);put('accepted-verdict-snapshot.json',json.load(open(O/'progress.json')))
b=json.load(open(O/'evidence/shared/input-manifest.json'));put('input-manifest.json',b);xs=[]
for p,v in b['sources_and_pins'].items():
 h=sha(R/p);assert h==v['sha256'];xs.append(dict(path=p,sha256=h,baseline_sha256=h,match=True,bytes=(R/p).stat().st_size))
put('inputs.json',xs);(D/'baseline-build.txt').write_bytes((O/'evidence/shared/baseline-build.txt').read_bytes())
for mod in ['MainLemma']:(D/('source-'+mod+'.lean.txt')).write_bytes((R/('Roth/'+mod+'.lean')).read_bytes())
(D/'target-excerpt.lean.txt').write_text(row['source']+'\n')
for n,args in [('source-search',['rg','--no-ignore','-n',r'\bboxFamily_finite\b','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','-w','boxFamily_finite','--','Roth','Roth.lean']),('source-inventory',['rg','--files','--no-ignore','Roth']),('inline-audit',['rg','--no-ignore','-n',r'boxFamily|finite_toSet|\.Finite|\.fintype','Roth','Roth.lean']),('local-literature',['rg','-n',r'B_1|mathcal.W|polynomials',' .mathlib-quality/references/clean.tex'.strip()])]:
 z=subprocess.run(args,text=True,capture_output=True);put(n+'.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1390:1440])+'\n')
cs=[]
for c in row['source_callers']:
 x=next(x for x in rows if x['name']==c['name']and x['file']==c['file']);s=x['source'];cs.append({**c,'end_line':x['end_line'],'visibility':x['visibility'],'source':s,'sha256':hashlib.sha256(s.encode()).hexdigest(),'signature':x['signature'],'body':x['body'],'occurrences':len(re.findall(r'\bboxFamily_finite\b',s))})
put('callers.json',dict(callers=cs,distinct_declarations=len(cs),external_to_file=0,executable_occurrences=sum(x['occurrences']for x in cs)))
prefix='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:15])+'\n';assert len([l for l in prefix.splitlines()if l.startswith('import ')])==9
(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
s=(R/'Roth/MainLemma.lean').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Box245Original\nopen Roth',1).replace('end Roth','end Box245Original');body=re.sub(r'\bboxFamily_finite\b','replay',body)
checks='\n'.join('#print axioms Box245Original.'+n for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))
full='''\n#check @Roth.boxFamily_finite
set_option pp.all true in
#print Roth.boxFamily_finite
#print axioms Roth.boxFamily_finite
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.boxFamily_finite
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"BOX245_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
'''
names=[]
for d in order:
 if d['visibility']=='private':
  text='Lean.mkPrivateNameCore `'+d['file'][:-5].replace('/','.')+' `'+d['name']
  if len('    '+text+',')>100:text=text.replace(' `'+d['name'],'\n      `'+d['name'])
 else:text='`'+d['name']
 names.append('    '+text)
audit='''
namespace Box245Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.boxFamily_finite
  let names : Array Lean.Name := #[
'''+',\n'.join(names)+''']
  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "BOX245_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "BOX245_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"BOX245_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"BOX245_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"BOX245_AUDIT: requested={names.size}; unique={unique}"
  Lean.logInfo m!"BOX245_AUDIT_PRESENT: present={present}; values={values}"
end Box245Audit
'''
whole=prefix+body+'\n'+checks+'\n'+full+audit
assert max(map(len,whole.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
print('Prepared original',len(whole.splitlines()),'lines; fresh17; exact293; nine imports retained')
