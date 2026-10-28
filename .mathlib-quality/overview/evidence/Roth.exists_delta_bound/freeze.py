from pathlib import Path
import json,hashlib,subprocess,time
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.exists_delta_bound'
def write_manifest():
 xs=[]
 excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in excluded:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  xs.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
 (D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=xs),ensure_ascii=False,indent=2)+'\n')
f=D/'final-validation.json'
if not f.exists():f.write_text('{}\n')
write_manifest();args=['python3',str(D/'validate.py'),str(R)];t=time.monotonic();r=subprocess.run(args,capture_output=True,text=True)
print(r.stdout,end='');print(r.stderr,end='');assert r.returncode==0
f.write_text(json.dumps(dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,elapsed_ms=int((time.monotonic()-t)*1000)),indent=2)+'\n')
write_manifest();r2=subprocess.run(args,capture_output=True,text=True);print(r2.stdout,end='');print(r2.stderr,end='');assert r2.returncode==0 and r2.stdout==r.stdout
print('FREEZE READY: all current artifacts hashed and final validator PASS; no native work remains.')
