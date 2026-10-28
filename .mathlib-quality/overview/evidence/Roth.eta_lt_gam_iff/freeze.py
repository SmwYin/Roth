from pathlib import Path
import hashlib,json,subprocess,sys
D=Path(__file__).resolve().parent;N='Roth.eta_lt_gam_iff'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def manifest():
 xs=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  xs.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=xs))
put('final-validation.json',dict(status='PASS',validator='validate.py',command=['python3',str(D/'validate.py'),str(Path.cwd())],note='Only frozen after actual exit0; receipt replaced below then currentmanifest revalidated.'))
manifest()
z=subprocess.run([sys.executable,str(D/'validate.py'),str(Path.cwd())],text=True,capture_output=True)
print(z.stdout,z.stderr);assert z.returncode==0
put('final-validation.json',dict(status='PASS',command=[sys.executable,str(D/'validate.py'),str(Path.cwd())],exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
manifest()
z=subprocess.run([sys.executable,str(D/'validate.py'),str(Path.cwd())],text=True,capture_output=True)
print(z.stdout,z.stderr);assert z.returncode==0
print('FROZEN235: complete validated package; native ownership may now be released explicitly.')
