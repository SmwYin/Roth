from pathlib import Path
import json,hashlib,re,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.four_lt_rpow')
def put(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n' if not isinstance(x,str) else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',base)
fresh=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==x['sha256'])for p,x in base['sources_and_pins'].items()];assert all(x['match']for x in fresh);put('inputs.json',fresh)
put('baseline-build.txt',(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-snapshot.json',order);put('canonical-entry.json',order[237]);assert order[237]['name']=='Roth.four_lt_rpow'
for m in ['MainLemma','Main']:put('source-'+m+'.lean.txt',(R/('Roth/'+m+'.lean')).read_text())
prefix='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:16])+'\n';assert len(re.findall('^import ',prefix,re.M))==9;put('disk-prefix.lean.txt',prefix)
put('isolated-prefix.lean.txt',Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
mod=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
body=mod.replace('four_lt_rpow','replay')
array=[]
for x in order:
 if x['visibility']=='private':
  term='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name']
  if len('    '+term+',')>100:term=term.replace(' `'+x['name'],'\n      `'+x['name'])
 else:term='`'+x['name']
 array.append('    '+term)
prior=Path('/private/tmp/roth-overview/assess/Roth.sqrt_lt_floor/original-executed.lean.txt').read_text()
tail=prior.split('  let unique :=',1)[1].replace('SQRT237','FOUR238').replace('end Sqrt237Audit','end Four238Audit')
audit='namespace Four238Audit\nrun_cmd do\n  let env ← Lean.getEnv\n  let target := `Roth.four_lt_rpow\n  let names : Array Lean.Name := #[\n'+',\n'.join(array)+']\n  let unique :='+tail
extra='''\nend Four238Original
#print Roth.four_lt_rpow
#print axioms Roth.four_lt_rpow
#print axioms Four238Original.replay
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.four_lt_rpow
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"FOUR238_FULL_TYPE: {ci.type}"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.four_lt_rpow
  let new ← Lean.getConstInfo `Four238Original.replay
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "FOUR238_SIGNATURE_CHANGED"
  Lean.logInfo "FOUR238_SIGNATURE_IDENTICAL"
'''
s=prefix+'namespace Four238Original\nopen Roth\n'+body+extra+audit
assert max(map(len,s.splitlines()))<=100
put('original-executed.lean.txt',s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
put('target-excerpt.lean.txt',mod[mod.index('theorem four_lt_rpow'):mod.index('/-- If `2 ≤ q_1')])
for n,args in [('source-search',['rg','--no-ignore','-n','four_lt_rpow','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','four_lt_rpow','--','Roth','Roth.lean']),('inline-search',['rg','--no-ignore','-n',r'log 4|quadratic_le_exp|3 ≤ .*\^ 2 \* Real.log|two_lt_rpow','Roth','Roth.lean']),('literature-local',['rg','-n',r'X > 4|X>4|whence|m\(2m|delta r_1|delta.*log q_1',' .mathlib-quality/references/clean.tex'.strip()])]:
 p=subprocess.run(args,cwd=R,capture_output=True,text=True);put(n+'.json',dict(request=args,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)))
