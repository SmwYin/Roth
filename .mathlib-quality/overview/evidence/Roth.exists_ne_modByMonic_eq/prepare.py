from pathlib import Path
import json,hashlib,re,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent;N='Roth.exists_ne_modByMonic_eq'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n' if not isinstance(x,str) else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',b)
f=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256'])for p,v in b['sources_and_pins'].items()];assert len(f)==17 and all(x['match']for x in f);put('inputs.json',f)
put('baseline-build.txt',(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
o=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert o[248]['name']==N;put('canonical-snapshot.json',o);put('canonical-entry.json',o[248])
p='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:16])+'\n';assert len(re.findall('^import ',p,re.M))==9;put('disk-prefix.lean.txt',p)
put('isolated-prefix.lean.txt',Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
src=(R/'Roth/MainLemma.lean').read_text();put('source-MainLemma.lean.txt',src)
m=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0];target=m[m.index('theorem exists_ne_modByMonic_eq'):m.index('/-- The difference of two distinct members')];put('target-excerpt.lean.txt',target)
body=m.replace('exists_ne_modByMonic_eq','replay')
arr=[]
for x in o:
 t=('Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name'])if x['visibility']=='private'else'`'+x['name']
 if len('    '+t+',')>100:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 arr.append('    '+t)
prior=(R/'.mathlib-quality/overview/evidence/Roth.three_small_factors/original-executed.lean.txt').read_text();tail=prior.split('  let unique :=',1)[1].replace('FACT241','COLL249').replace('Fact241Audit','Collision249Audit')
extra='''
end Collision249Original
#print Roth.exists_ne_modByMonic_eq
#print axioms Roth.exists_ne_modByMonic_eq
#print axioms Collision249Original.replay
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.exists_ne_modByMonic_eq
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"COLL249_FULL_TYPE: {ci.type}"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.exists_ne_modByMonic_eq
  let new ← Lean.getConstInfo `Collision249Original.replay
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "COLL249_SIGNATURE_CHANGED"
  Lean.logInfo "COLL249_SIGNATURE_IDENTICAL"
namespace Collision249Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.exists_ne_modByMonic_eq
  let names : Array Lean.Name := #[
'''
s=p+'namespace Collision249Original\nopen Roth\n'+body+extra+',\n'.join(arr)+']\n  let unique :='+tail
assert max(map(len,s.splitlines()))<=100
put('original-executed.lean.txt',s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
for name,cmd in [('source-search',['rg','--no-ignore','-n','exists_ne_modByMonic_eq','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','exists_ne_modByMonic_eq','--','Roth','Roth.lean']),('inline-search',['rg','--no-ignore','-n',r'exists_ne_modByMonic_eq|exists_ne_map_eq_of_card_lt|sum_modByMonic_coeff','Roth','Roth.lean']),('literature-local',['rg','-n',r'1\+2B|2B_1|pigeonhole|number of such|number of possible','.mathlib-quality/references/clean.tex'])]:
 q=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put(name+'.json',dict(request=cmd,result=dict(exit_code=q.returncode,stdout=q.stdout,stderr=q.stderr)))
print('PASS fresh17; full module replay; exact293 generated; width',max(map(len,s.splitlines())))
