from pathlib import Path
import hashlib,json,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_hasseDeriv_eval_ne_zero'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest():
 excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
 files=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in excluded:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  files.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=files))
def run(cmd):
 q=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
 return dict(request=cmd,exit_code=q.returncode,stdout=q.stdout,stderr=q.stderr)
q=run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)]);put('secret-guard.json',q);assert q['exit_code']==0,q
q=run(['python3','/private/tmp/roth-overview/check_audit_source.py',str(D/'original-executed.lean.txt')]);assert q['exit_code']==0,q
p=rd('preparation-checks.json');p['freeze_time_canonical_recheck']=q;put('preparation-checks.json',p)
put('validation-receipts.json',dict(status='preparing actual scratch/integrated results'))
put('freeze.json',dict(declaration=N,canonical_index=254,status='frozen',root_acceptance='pending',native_ownership='released at completed-package handoff',production_changes=False))
manifest()
scratch=run(['python3',str(D/'validate.py'),str(R)]);assert scratch['exit_code']==0,scratch
S=D/'simulated-integrated';E=S/'.mathlib-quality/overview/evidence'/N;M=S/'.mathlib-quality/overview/mathlibable';E.mkdir(parents=True,exist_ok=True);M.mkdir(parents=True,exist_ok=True)
def copy_current():
 for f in rd('copy-manifest.json')['files']:
  p=Path(f['source']);dest=S/f['destination'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 shutil.copyfile(D/'copy-manifest.json',E/'copy-manifest.json')
copy_current()
integrated=run(['python3',str(E/'validate.py'),str(R)]);assert integrated['exit_code']==0,integrated
# Historical manifest must not mask tampering of a current manifest-covered artifact.
shutil.copyfile(E/'copy-manifest.json',E/'worker-copy-manifest.json')
f=E/'overview-entry.json';original=f.read_bytes();f.write_bytes(original+b'\n')
negative=run(['python3',str(E/'validate.py'),str(R)]);assert negative['exit_code']!=0,negative
f.write_bytes(original)
restored=run(['python3',str(E/'validate.py'),str(R)]);assert restored['exit_code']==0,restored
put('validation-receipts.json',dict(status='PASS',scratch=scratch,simulated_integrated=integrated,current_manifest_tamper_canary=negative,restored_integrated=restored,note='Actual validator subprocesses; current artifact tamper rejected despite matching historical worker-copy-manifest; then restored and passed. Final manifest resealed after adding these raw results.'))
manifest();copy_current()
final_scratch=run(['python3',str(D/'validate.py'),str(R)]);final_integrated=run(['python3',str(E/'validate.py'),str(R)])
assert final_scratch['exit_code']==final_integrated['exit_code']==0,(final_scratch,final_integrated)
shutil.rmtree(S)
print(final_scratch['stdout'].strip());print(final_integrated['stdout'].strip());print('PASS secret guard + actual negative current-manifest canary; package frozen')
