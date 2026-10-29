from pathlib import Path
import hashlib,json,subprocess,shutil,datetime
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.approxSet'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest():
 xs=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dst='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  xs.append(dict(source=str(p),destination=dst,sha256=sha(p),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=xs))
def run(args):
 t=datetime.datetime.now();z=subprocess.run(args,text=True,capture_output=True);return dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,elapsed_ms=int((datetime.datetime.now()-t).total_seconds()*1000))
# Fresh final source/pin check before freeze.
fresh=json.load(open(D/'inputs.json'))
for x in fresh:assert sha(R/x['path'])==x['sha256']and(R/x['path']).stat().st_size==x['bytes']
put('fresh-final-inputs.json',dict(unchanged=True,inputs=fresh))
guard=run(['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(D)]);put('secret-guard.json',guard);assert guard['exit_code']==0,guard
put('freeze-record.json',dict(declaration=N,canonical_index=267,completed=True,frozen_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),native_ownership='exclusive worker, release at final completed handoff',accepted_native_sources=5,rejected_native_attempts=4,root_acceptance='pending',production_changed=False,shared18_changed=False,disk9_changed=False))
manifest()
a=run(['python3',str(D/'validate.py'),str(R)]);print(json.dumps(a,ensure_ascii=False));assert a['exit_code']==0
S=D/'simulated-integrated';E=S/'.mathlib-quality/overview/evidence'/N;M=S/'.mathlib-quality/overview/mathlibable';E.mkdir(parents=True,exist_ok=True);M.mkdir(parents=True,exist_ok=True)
for p in D.iterdir():
 if p.is_file():shutil.copy2(p,M/(N+'.md')if p.name=='report.md'else E/p.name)
b=run(['python3',str(E/'validate.py'),str(R)]);print(json.dumps(b,ensure_ascii=False));shutil.rmtree(S);assert b['exit_code']==0
put('final-validation.json',dict(declaration=N,scratch=a,simulated_integrated=b,both_PASS=True))
# New verification receipt is itself current-manifest covered.
guard=run(['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(D)]);put('secret-guard.json',guard);assert guard['exit_code']==0
manifest()
c=run(['python3',str(D/'validate.py'),str(R)]);print(json.dumps(c,ensure_ascii=False));assert c['exit_code']==0
print('FROZEN completed package; native ownership may be explicitly released to root')
