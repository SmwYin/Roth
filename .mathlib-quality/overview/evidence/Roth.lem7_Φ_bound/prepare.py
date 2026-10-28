from pathlib import Path
import json,hashlib,re,subprocess,shutil
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent;O=R/'.mathlib-quality/overview';N='Roth.lem7_Φ_bound'
def save(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((O/'evidence/shared/input-manifest.json').read_text());save('input-manifest.json',base)
inputs=[dict(path=p,sha256=sha(R/p),baseline_sha256=v['sha256'],bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256'])for p,v in base['sources_and_pins'].items()];assert len(inputs)==17 and all(x['match']for x in inputs);save('inputs.json',inputs)
shutil.copy(O/'evidence/shared/baseline-build.txt',D/'baseline-build.txt')
rows=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());row=next(x for x in rows if x['name']==N);save('target-metadata.json',row)
callers=[next(x for x in rows if x['name']==c['name'])for c in row['project_callers']];save('callers.json',callers)
order=json.loads((O/'declaration-order.json').read_text());assert order[217]['name']==N;save('canonical-snapshot.json',order);save('canonical-entry.json',order[217])
src=(R/'Roth/Theta.lean').read_text();(D/'source-module.lean.txt').write_text(src)
prior=Path('/private/tmp/roth-overview/assess/Roth.lem6M_lt/original-executed.lean.txt').read_text();prefix='\n'.join(prior.splitlines()[:9])+'\n';(D/'disk-prefix.lean.txt').write_text(prefix)
shutil.copy('/private/tmp/roth-overview/current-isolated-prefix.lean.txt',D/'isolated-prefix.lean.txt')
body=src[src.index('namespace Roth'):].replace('namespace Roth','namespace Phi218\nopen Roth',1).replace('end Roth','end Phi218');body=re.sub(r'\blem7_Φ_bound\b','replay',body)
axioms='\n'.join('#print axioms Phi218.'+m for m in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))
audit=prior[prior.index('namespace LemSixM217Audit'):];i=audit.index('let names : Array Lean.Name');j=audit.index('  let unique :=',i);audit=audit[:i].replace('LemSixM217','Phi218').replace('`Roth.lem6M_lt','`Roth.lem7_Φ_bound')+audit[i:j]+audit[j:].replace('LEMSIXM217','PHI218').replace('LemSixM217','Phi218');audit=audit.replace('LEMSIXM217','PHI218')
s=prefix+'\n/-! Read-only numeric Phi bound audit. -/\n\nopen MvPolynomial\n\n'+body+'\n#check @Roth.lem7_Φ_bound\n#print Roth.lem7_Φ_bound\n#print axioms Roth.lem7_Φ_bound\n'+axioms+'\n\n'+audit
assert all(len(l)<=100 for l in s.splitlines());(D/'original-executed.lean.txt').write_text(s)
res=subprocess.run(['python3','/private/tmp/roth-overview/check_audit_source.py',str(D/'original-executed.lean.txt')],capture_output=True,text=True);save('canonical-preflight.json',dict(command=res.args,exit_code=res.returncode,stdout=res.stdout,stderr=res.stderr));assert res.returncode==0
(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
for label,cmd in [('source-search',['rg','--no-ignore','-n','-w','lem7_Φ_bound','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','-w','lem7_Φ_bound','--','Roth/','Roth.lean']),('inline-audit',['rg','--no-ignore','-n','lem7_Φ_bound|hδe|have hmul|10 \^ \(p - 1\)','Roth','Roth.lean'])]:
 r=subprocess.run(cmd,cwd=R,capture_output=True,text=True);save(label+'.json',dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
tex=R/'.mathlib-quality/references/clean.tex';save('literature-source.json',dict(path=str(tex.relative_to(R)),sha256=sha(tex)));lines=tex.read_text().splitlines();hits=[i for i,l in enumerate(lines)if '\\delta_1' in l or 'delta_1' in l];keep=set();
for i in hits:
 keep.update(range(max(0,i-12),min(len(lines),i+20)))
(D/'clean-excerpt.tex.txt').write_text('\n'.join(str(i+1)+': '+lines[i]for i in sorted(keep))+'\n')
print('PASS fresh17 inputs; target218; entire-module replay prepared; exact293 preflight; source searches archived')
