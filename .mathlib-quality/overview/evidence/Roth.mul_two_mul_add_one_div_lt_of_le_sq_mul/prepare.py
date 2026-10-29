from pathlib import Path
import json,hashlib,subprocess,re
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent;N='Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',b)
f=[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256'])for p,v in b['sources_and_pins'].items()];assert len(f)==17 and all(x['match']for x in f);put('inputs.json',f)
put('baseline-build.txt',(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_text())
o=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert o[252]['name']==N;put('canonical-snapshot.json',o);put('canonical-entry.json',o[252])
p='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:16])+'\n';assert len(re.findall('^import ',p,re.M))==9;put('disk-prefix.lean.txt',p)
put('isolated-prefix.lean.txt',Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text())
src=(R/'Roth/MainLemma.lean').read_text();put('source-MainLemma.lean.txt',src)
m=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0];target=m[m.index('theorem mul_two_mul_add_one_div_lt_of_le_sq_mul'):m.index('/-- If the index of `P')];put('target-excerpt.lean.txt',target)
body=m.replace('mul_two_mul_add_one_div_lt_of_le_sq_mul','replay')
arr=[]
for x in o:
 t=('Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' `'+x['name'])if x['visibility']=='private'else'`'+x['name']
 if len('    '+t+',')>100:t=t.replace(' `'+x['name'],'\n      `'+x['name'])
 arr.append('    '+t)
prior=(R/'.mathlib-quality/overview/evidence/Roth.le_index_of_forall_eval_eq_zero/original-executed.lean.txt').read_text();tail=prior.split('  let unique :=',1)[1].replace('CUTOFF252','BUDGET253').replace('Cutoff252Audit','Budget253Audit')
extra='''
end Budget253Original
#print Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
#print axioms Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
#print axioms Budget253Original.replay
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"BUDGET253_FULL_TYPE: {ci.type}"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
  let new ← Lean.getConstInfo `Budget253Original.replay
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "BUDGET253_SIGNATURE_CHANGED"
  Lean.logInfo "BUDGET253_SIGNATURE_IDENTICAL"
run_cmd do
  let ci ← Lean.getConstInfo `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
  Lean.logInfo m!"BUDGET253_TYPE_CONSTANTS: {ci.type.getUsedConstants}"
  let some v := ci.value? (allowOpaque := true) | throwError "BUDGET253_NO_VALUE"
  Lean.logInfo m!"BUDGET253_BODY_CONSTANTS: {v.getUsedConstants}"
namespace Budget253Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
  let names : Array Lean.Name := #[
'''
s=p+'namespace Budget253Original\nopen Roth\n'+body+extra+',\n'.join(arr)+']\n  let unique :='+tail
assert max(map(len,s.splitlines()))<=100
put('original-executed.lean.txt',s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
for name,cmd in [('source-search',['rg','--no-ignore','-n','mul_two_mul_add_one_div_lt_of_le_sq_mul','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','mul_two_mul_add_one_div_lt_of_le_sq_mul','--','Roth','Roth.lean']),('inline-search',['rg','--no-ignore','-n',r'mul_two_mul_add_one_div_lt_of_le_sq_mul|sq_pos_of_pos hδpos|have hq : M|hδm.*2 \* M','Roth','Roth.lean']),('literature-local',['rg','-n',r'lem7-satisfied|immediate from|delta.*log.*q_1|2m\+1','.mathlib-quality/references/clean.tex'])]:
 q=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put(name+'.json',dict(request=cmd,result=dict(exit_code=q.returncode,stdout=q.stdout,stderr=q.stderr)))
put('literature-local-input.json',dict(path='.mathlib-quality/references/clean.tex',sha256=sha(R/'.mathlib-quality/references/clean.tex')))
print('PASS fresh17; full module replay; exact293 generated; width',max(map(len,s.splitlines())))
