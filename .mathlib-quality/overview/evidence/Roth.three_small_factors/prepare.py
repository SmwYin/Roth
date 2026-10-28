from pathlib import Path
import json,hashlib,re,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent;N='Roth.three_small_factors'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',base)
fresh=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==x['sha256'])for p,x in base['sources_and_pins'].items()];assert len(fresh)==17 and all(x['match']for x in fresh);put('inputs.json',fresh)
put('baseline-build.txt',(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-snapshot.json',order);put('canonical-entry.json',order[240]);assert order[240]['name']==N
for m in ['MainLemma','Main']:put('source-'+m+'.lean.txt',(R/('Roth/'+m+'.lean')).read_text())
prefix='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:16])+'\n';assert len(re.findall('^import ',prefix,re.M))==9;put('disk-prefix.lean.txt',prefix)
put('isolated-prefix.lean.txt',Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
mod=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
body=mod.replace('three_small_factors','replay')
array=[]
for x in order:
 if x['visibility']=='private':
  term='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name']
  if len('    '+term+',')>100:term=term.replace(' `'+x['name'],'\n      `'+x['name'])
 else:term='`'+x['name']
 array.append('    '+term)
prior=Path('/private/tmp/roth-overview/assess/Roth.mul_log_div_two_lt_log_mainCoeffBound/original-executed.lean.txt').read_text()
tail=prior.split('  let unique :=',1)[1].replace('LOG239','FACT241').replace('end Log239Audit','end Fact241Audit')
audit='namespace Fact241Audit\nrun_cmd do\n  let env ← Lean.getEnv\n  let target := `'+N+'\n  let names : Array Lean.Name := #[\n'+',\n'.join(array)+']\n  let unique :='+tail
extra='''
end Fact241Original
#print Roth.three_small_factors
#print axioms Roth.three_small_factors
#print axioms Fact241Original.replay
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.three_small_factors
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"FACT241_FULL_TYPE: {ci.type}"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.three_small_factors
  let new ← Lean.getConstInfo `Fact241Original.replay
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "FACT241_SIGNATURE_CHANGED"
  Lean.logInfo "FACT241_SIGNATURE_IDENTICAL"
'''
s=prefix+'namespace Fact241Original\nopen Roth\n'+body+extra+audit
assert max(map(len,s.splitlines()))<=100
put('original-executed.lean.txt',s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
put('target-excerpt.lean.txt',mod[mod.index('theorem three_small_factors'):mod.index('private lemma exists_norm_coeff')])
for n,args in [('source-search',['rg','--no-ignore','-n','three_small_factors','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','three_small_factors','--','Roth','Roth.lean']),('inline-search',['rg','--no-ignore','-n',r'two_lt_rpow_aux|three_small_factors|2 \* m \* Real.log|log_mainCoeffBound','Roth','Roth.lean']),('literature-local',['rg','-n',r'three-small-factors|log B_1|roth:eq32','.mathlib-quality/references/clean.tex'])]:
 p=subprocess.run(args,cwd=R,capture_output=True,text=True);put(n+'.json',dict(request=args,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)))
print('Preparation PASS; fresh17 hashes; width',max(map(len,s.splitlines())))
