from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.Θ_lt'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'));row=next(x for x in rows if x['name']==N);put('target-metadata.json',row);put('callers.json',[x for x in rows if x['name']in[c['name']for c in row['project_callers']]])
order=json.load(open(O/'declaration-order.json'));assert order[227]['name']==N;put('canonical-snapshot.json',order);put('canonical-entry.json',order[227])
b=json.load(open(O/'evidence/shared/input-manifest.json'));put('input-manifest.json',b);xs=[]
for p,v in b['sources_and_pins'].items():
 h=sha(R/p);assert h==v['sha256'];xs.append(dict(path=p,sha256=h,baseline_sha256=h,match=True,bytes=(R/p).stat().st_size))
put('inputs.json',xs);(D/'baseline-build.txt').write_bytes((O/'evidence/shared/baseline-build.txt').read_bytes())
s=(R/'Roth/Theta.lean').read_text();(D/'source-module.lean.txt').write_text(s);(D/'target-excerpt.lean.txt').write_text(row['source']+'\n');(D/'caller-module.lean.txt').write_bytes((R/'Roth/MainLemma.lean').read_bytes())
prefix='\n'.join((R/'.lake/roth-overview-session/GenWronskianChecks.lean').read_text().splitlines()[:15])+'\n';(D/'disk-prefix.lean.txt').write_text('\n'.join(prefix.splitlines()[:9])+'\n');(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Theta228\nopen Roth',1).replace('end Roth','end Theta228');body=re.sub(r'\bΘ_lt\b','replay',body)
checks='\n'.join('#print axioms Theta228.'+n for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))
old=Path('/private/tmp/roth-overview/assess/Roth.theta_lt_of_large_delta_aux/executed.lean.txt').read_text();audit=old[old.index('namespace ThetaPrivate227Audit'):];before,array=audit.split('  let names : Array Lean.Name := #[',1);before=before.replace('ThetaPrivate227Audit','Theta228Audit').replace('Lean.mkPrivateNameCore `Roth.Theta\n    `Roth.theta_lt_of_large_delta_aux','`Roth.Θ_lt');audit=before+'  let names : Array Lean.Name := #['+array;audit=audit.replace('THETA_PRIVATE227','THETA228').replace('end ThetaPrivate227Audit','end Theta228Audit')
full='''\n#check @Roth.Θ_lt
#print Roth.Θ_lt
#print axioms Roth.Θ_lt
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.Θ_lt
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"THETA228_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
'''
whole=prefix+body+'\n'+checks+'\n'+full+audit
assert all(len(l)<=100 for l in whole.splitlines());(D/'original-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
for name,cmd in [('source-search',['rg','--no-ignore','-n','Θ_lt','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','Θ_lt','--','Roth','Roth.lean'])]:
 z=subprocess.run(cmd,text=True,capture_output=True);put(name+'.json',dict(command=cmd,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));assert z.returncode==0
print('Prepared exact original',len(whole.splitlines()),'lines;',len(xs),'inputs match; callers',[(x['name'],x['line'])for x in json.load(open(D/'callers.json'))])
