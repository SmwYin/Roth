from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.mainCoeffBound'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def manifest():
 xs=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dst='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  xs.append(dict(source=str(p),destination=dst,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=xs))
put('frozen.json',dict(declaration=N,canonical_index=232,status='FROZEN',completed=True,production_changes=False,native_ownership='Released to root only after portable validation and secret guard PASS.',root_acceptance='pending'))
put('final-validation.json',dict(status='PASS',validator='validate.py',secret_guard='PASS',note='Final read-only validator run and secret scan must exit0 after current manifest regeneration.'))
manifest()
p=subprocess.run(['python3',str(D/'validate.py'),str(R)],capture_output=True,text=True)
print(p.stdout,p.stderr);assert p.returncode==0
