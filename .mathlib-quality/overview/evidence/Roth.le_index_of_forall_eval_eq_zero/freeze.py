from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.le_index_of_forall_eval_eq_zero'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest():
 files=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  files.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=files))
def run(cmd):
 r=subprocess.run(cmd,cwd=R,capture_output=True,text=True);return dict(request=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr)
def simulate():
 S=D/'simulated';out=S/'.mathlib-quality/overview/evidence'/N
 out.mkdir(parents=True,exist_ok=True)
 for f in json.loads((D/'copy-manifest.json').read_text())['files']:
  dest=S/f['destination'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f['source'],dest)
 shutil.copyfile(D/'copy-manifest.json',out/'copy-manifest.json')
 return out
secret=run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)])
assert secret['exit_code']==0,secret
put('secret-guard.json',secret)
manifest()
scratch=run(['python3',str(D/'validate.py'),str(R)]);assert scratch['exit_code']==0,scratch
out=simulate();integrated=run(['python3',str(out/'validate.py'),str(R)]);assert integrated['exit_code']==0,integrated
put('final-validation.json',dict(status='PASS',scratch=scratch,simulated_integrated=integrated,production_sources_and_pins='fresh17 match current tracked shared manifest',current_manifest_required=True,historical_manifest_not_used=True,root_acceptance='pending'))
manifest()
# Recheck current hashes including final-validation, without modifying any artifact afterwards.
scratch=run(['python3',str(D/'validate.py'),str(R)]);assert scratch['exit_code']==0,scratch
out=simulate();integrated=run(['python3',str(out/'validate.py'),str(R)]);assert integrated['exit_code']==0,integrated
print(scratch['stdout'].strip());print(integrated['stdout'].strip());print('FROZEN candidate; current manifest',sha(D/'copy-manifest.json'))
