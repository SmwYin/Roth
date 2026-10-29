from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def manifest():
 files=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  files.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=files))
cmd=['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(D)]
p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('secret-guard.json',dict(request=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,p.stdout+p.stderr
manifest();cmd=['python3',str(D/'validate.py'),str(R)];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
put('final-validation.json',dict(request=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr));manifest()
assert p.returncode==0,p.stdout+p.stderr
p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);assert p.returncode==0,p.stdout+p.stderr
print(p.stdout,end='');print('FROZEN: native ownership may be explicitly released to root')
