from pathlib import Path
import json,hashlib,subprocess,sys,shutil,datetime
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.main_lemma'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def manifest():
 xs=[]
 for p in sorted(D.iterdir()):
  if not p.is_file()or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  xs.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
 put('copy-manifest.json',dict(declaration=N,files=xs))
cmd=['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(D)]
z=subprocess.run(cmd,text=True,capture_output=True);put('secret-guard.json',dict(command=cmd,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));print(z.stdout,z.stderr);assert z.returncode==0
put('final-validation.json',dict(status='pending',commands=[]))
put('freeze-record.json',dict(declaration=N,status='pending',native_ownership='RELEASED; root retains ownership; documentary reseal only',production_and_pins_unchanged=True))
manifest()
cmd=[sys.executable,str(D/'validate.py'),str(R)];z=subprocess.run(cmd,text=True,capture_output=True);print(z.stdout,z.stderr);assert z.returncode==0
checks=[dict(layout='scratch',command=cmd,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr)]
# Simulated integrated layout uses a current manifest, a report outside the evidence directory,
# and excluded integration-only acceptance artifacts. It is written only under the candidate.
S=D/'.simulated-integration';E=S/'overview/evidence'/N;M=S/'overview/mathlibable';E.mkdir(parents=True,exist_ok=True);M.mkdir(parents=True,exist_ok=True)
for p in D.iterdir():
 if p.is_file()and p.name!='report.md':shutil.copy2(p,E/p.name)
shutil.copy2(D/'report.md',M/(N+'.md'))
(E/'root-acceptance.json').write_text('{"status":"simulated-only"}\n')
cmd=[sys.executable,str(E/'validate.py'),str(R)];z=subprocess.run(cmd,text=True,capture_output=True);print(z.stdout,z.stderr);checks.append(dict(layout='simulated-integrated',command=cmd,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));assert z.returncode==0
shutil.rmtree(S)
put('final-validation.json',dict(status='PASS',checks=checks,secret_guard='secret-guard.json',current_manifest_validated=True))
put('freeze-record.json',dict(declaration=N,status='FROZEN',frozen_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),native_ownership='RELEASED; root retains ownership; documentary reseal only',production_and_pins_unchanged=True,root_acceptance='pending',unresolved=[]))
manifest()
z=subprocess.run([sys.executable,str(D/'validate.py'),str(R)],text=True,capture_output=True);print(z.stdout,z.stderr);assert z.returncode==0
print('FROZEN266: documentary package resealed; native/build ownership remains RELEASED to root.')
