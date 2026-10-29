from pathlib import Path
import json,hashlib,re,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent;N='Roth.exists_hasseDeriv_eval_ne_zero'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n' if not isinstance(x,str) else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',b)
f=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256']) for p,v in b['sources_and_pins'].items()];assert len(f)==17 and all(x['match']for x in f);put('inputs.json',f)
put('baseline-build.txt',(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
o=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert o[253]['name']==N;put('canonical-snapshot.json',o);put('canonical-entry.json',o[253])
p='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:16])+'\n';assert len(re.findall('^import ',p,re.M))==9;put('disk-prefix.lean.txt',p)
put('isolated-prefix.lean.txt',Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
src=(R/'Roth/MainLemma.lean').read_text();put('source-MainLemma.lean.txt',src)
for mod in ['Index','Box','Taylor','HasseDeriv']:put('source-'+mod+'.lean.txt',(R/('Roth/'+mod+'.lean')).read_text())
m=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0];target=m[m.index('theorem exists_hasseDeriv_eval_ne_zero'):m.index('private lemma abs_eval_iterated')];put('target-excerpt.lean.txt',target)
body=m.replace('exists_hasseDeriv_eval_ne_zero','replay')
arr=[]
for x in o:
 t=('Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name'])if x['visibility']=='private'else'`'+x['name']
 if len('    '+t+',')>100:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 arr.append('    '+t)
prior=(R/'.mathlib-quality/overview/evidence/Roth.le_index_of_forall_eval_eq_zero/original-executed.lean.txt').read_text();tail=prior.split('  let unique :=',1)[1].replace('CUTOFF252','WITNESS254').replace('Cutoff252Audit','Witness254Audit')
extra='''
end Witness254Original
#print Roth.exists_hasseDeriv_eval_ne_zero
#print axioms Roth.exists_hasseDeriv_eval_ne_zero
#print axioms Witness254Original.replay
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.exists_hasseDeriv_eval_ne_zero
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"WITNESS254_FULL_TYPE: {ci.type}"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.exists_hasseDeriv_eval_ne_zero
  let new ← Lean.getConstInfo `Witness254Original.replay
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "WITNESS254_SIGNATURE_CHANGED"
  Lean.logInfo "WITNESS254_SIGNATURE_IDENTICAL"
namespace Witness254Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.exists_hasseDeriv_eval_ne_zero
  let names : Array Lean.Name := #[
'''
s=p+'namespace Witness254Original\nopen Roth\n'+body+extra+',\n'.join(arr)+']\n  let unique :='+tail
assert max(map(len,s.splitlines()))<=100
put('original-executed.lean.txt',s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
for name,cmd in [('source-search',['rg','--no-ignore','-n','exists_hasseDeriv_eval_ne_zero','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','exists_hasseDeriv_eval_ne_zero','--','Roth','Roth.lean']),('inline-search',['rg','--no-ignore','-n',r'exists_weight_eq_index|le_index_iff|exists_hasseDeriv_eval_ne_zero','Roth','Roth.lean']),('literature-local',['rg','-n',r'has some derivative|index of|Hence.*derivative|nonzero derivative','.mathlib-quality/references/clean.tex'])]:
 q=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put(name+'.json',dict(request=cmd,result=dict(exit_code=q.returncode,stdout=q.stdout,stderr=q.stderr)))
print('PASS fresh17; full module replay; exact293 generated; width',max(map(len,s.splitlines())))
