from pathlib import Path
import json,hashlib,subprocess,sys,shutil
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.boxFamily_finite'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def manifest():
 fs=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  fs.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,layout='portable scratch/integrated',files=fs))
def validate(layout):
 if layout=='scratch':path=D/'validate.py'
 else:
  sim=D/'simulation';shutil.rmtree(sim,ignore_errors=True)
  E=sim/'.mathlib-quality/overview/evidence'/N;M=sim/'.mathlib-quality/overview/mathlibable';E.mkdir(parents=True);M.mkdir(parents=True)
  for p in D.iterdir():
   if p.is_file():shutil.copy2(p,M/(N+'.md')if p.name=='report.md'else E/p.name)
  path=E/'validate.py'
 cmd=[sys.executable,str(path),str(R)];z=subprocess.run(cmd,text=True,capture_output=True)
 out=dict(layout=layout,command=cmd,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,validator_sha256=sha(D/'validate.py'))
 if layout!='scratch':shutil.rmtree(D/'simulation')
 if z.returncode:print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(z.returncode)
 return out
instruction_paths=[Path('/private/tmp/roth-overview/next-worker245-prompt.txt'),Path('/private/tmp/roth-overview/WORKER_CONTRACT.md'),Path('/private/tmp/roth-overview/EXCLUSIVE_NATIVE_WORKER_ADDENDUM.md'),Path('/Users/ramin/.codex/skills/lean4/SKILL.md'),Path('/Users/ramin/.codex/skills/mathlib-quality/SKILL.md'),Path('/Users/ramin/.local/share/roth-mathlib-quality/commands/overview.md'),Path('/Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md')]
for n in['mathlib-search.md','mathlibable-verdicts.md','generalisation-patterns.md','mathlib-review-stages.md']:instruction_paths.append(Path('/Users/ramin/.codex/skills/mathlib-quality/references')/n)
put('instruction-inputs.json',[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)for p in instruction_paths])
manifest();checks=[validate('scratch'),validate('simulated-integrated')]
put('final-validation.json',dict(status='PASS',checks=checks,current_manifest_policy='Checks cover current manifest and validator at each invocation; final frozen manifest is rerun after this receipt is written. No historical manifest substituted.',all_required_evidence_complete=True))
put('frozen.json',dict(declaration=N,completed=True,frozen=True,root_acceptance='pending',native_ownership='released after final frozen currentmanifest validation; no further native/build scheduled',unresolved=[],production_unchanged=True))
manifest()
for layout in['scratch','simulated-integrated']:
 out=validate(layout);print(out['stdout'].strip())
print('FROZEN245: complete current manifest; both layouts PASS; secret guard PASS; native/build ownership released.')
