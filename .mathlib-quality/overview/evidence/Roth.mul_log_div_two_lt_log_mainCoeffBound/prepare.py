from pathlib import Path
import json,hashlib,re,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.mul_log_div_two_lt_log_mainCoeffBound');N='Roth.mul_log_div_two_lt_log_mainCoeffBound'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',base)
fresh=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==x['sha256'])for p,x in base['sources_and_pins'].items()];assert len(fresh)==17 and all(x['match']for x in fresh);put('inputs.json',fresh)
put('baseline-build.txt',(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-snapshot.json',order);put('canonical-entry.json',order[238]);assert order[238]['name']==N
put('source-MainLemma.lean.txt',(R/'Roth/MainLemma.lean').read_text())
prefix='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:16])+'\n';assert len(re.findall('^import ',prefix,re.M))==9;put('disk-prefix.lean.txt',prefix)
put('isolated-prefix.lean.txt',Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
mod=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
body=mod.replace('mul_log_div_two_lt_log_mainCoeffBound','replay')
array=[]
for x in order:
 if x['visibility']=='private':
  term='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name']
  if len('    '+term+',')>100:term=term.replace(' `'+x['name'],'\n      `'+x['name'])
 else:term='`'+x['name']
 array.append('    '+term)
prior=Path('/private/tmp/roth-overview/assess/Roth.four_lt_rpow/original-executed.lean.txt').read_text()
tail=prior.split('  let unique :=',1)[1].replace('FOUR238','LOG239').replace('end Four238Audit','end Log239Audit')
audit='namespace Log239Audit\nrun_cmd do\n  let env ← Lean.getEnv\n  let target := `'+N+'\n  let names : Array Lean.Name := #[\n'+',\n'.join(array)+']\n  let unique :='+tail
extra='''\nend Log239Original
#print Roth.mul_log_div_two_lt_log_mainCoeffBound
#print axioms Roth.mul_log_div_two_lt_log_mainCoeffBound
#print axioms Log239Original.replay
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.mul_log_div_two_lt_log_mainCoeffBound
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"LOG239_FULL_TYPE: {ci.type}"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.mul_log_div_two_lt_log_mainCoeffBound
  let new ← Lean.getConstInfo `Log239Original.replay
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "LOG239_SIGNATURE_CHANGED"
  Lean.logInfo "LOG239_SIGNATURE_IDENTICAL"
'''
s=prefix+'namespace Log239Original\nopen Roth\n'+body+extra+audit
assert max(map(len,s.splitlines()))<=100
put('original-executed.lean.txt',s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
put('target-excerpt.lean.txt',mod[mod.index('theorem mul_log_div_two'):mod.index('private lemma two_lt_rpow_aux')])
for n,args in [('source-search',['rg','--no-ignore','-n','mul_log_div_two_lt_log_mainCoeffBound','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','mul_log_div_two_lt_log_mainCoeffBound','--','Roth','Roth.lean']),('inline-search',['rg','--no-ignore','-n',r'log_sqrt|log.*floor|floor.*log|sqrt_lt_floor|log_mainCoeffBound','Roth','Roth.lean']),('literature-local',['rg','-n',r'X>4|whence|log B_1|sqrt X',' .mathlib-quality/references/clean.tex'.strip()])]:
 p=subprocess.run(args,cwd=R,capture_output=True,text=True);put(n+'.json',dict(request=args,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)))
print('Preparation PASS; fresh17 hashes; exact source written; maximum width',max(map(len,s.splitlines())))
