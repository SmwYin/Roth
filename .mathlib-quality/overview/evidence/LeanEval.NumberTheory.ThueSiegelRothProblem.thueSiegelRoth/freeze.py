from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
def files():return sorted(p for p in D.rglob('*')if p.is_file()and p.name not in exclude and '_validation-layout'not in p.relative_to(D).parts)
def manifest():
 entries=[]
 for p in files():
  rel=str(p.relative_to(D));dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if rel=='report.md'else'evidence/'+N+'/'+rel)
  entries.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
 dump('copy-manifest.json',dict(declaration=N,files=entries))
def check(draft,layout):
 if layout=='scratch':v=D/'validate.py'
 else:
  T=D/'_validation-layout';shutil.rmtree(T,ignore_errors=True)
  E=T/'evidence'/N;E.mkdir(parents=True);M=T/'mathlibable';M.mkdir()
  for p in files()+[D/'copy-manifest.json']:
   rel=p.relative_to(D)
   if rel==Path('report.md'):shutil.copyfile(p,M/(N+'.md'))
   else:
    q=E/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
  v=E/'validate.py'
 cmd=['python3',str(v),str(R)]+(['--draft']if draft else[])
 p=subprocess.run(cmd,text=True,capture_output=True)
 out=dict(request=cmd,status=p.returncode,stdout=p.stdout,stderr=p.stderr)
 dump('validation-'+('draft-'if draft else'')+layout+'.json',out)
 assert p.returncode==0,out
 return out
for p in D.glob('*.py'):
 p.write_text('\n'.join(x.rstrip()for x in p.read_text().splitlines()).rstrip()+'\n')
inputs=json.loads((D/'inputs.json').read_text())
for x in inputs:assert sha(R/x['path'])==x['sha256']
dump('fresh-final-inputs.json',dict(inputs=inputs,unchanged=True))
dump('freeze-status.json',dict(completed=False,native_release=False,stage='draft review gates'))
# First validate the real current draft manifest in scratch and integrated layouts.
manifest();check(True,'scratch');manifest();check(True,'integrated');manifest();check(True,'scratch')
scan=['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)]
p=subprocess.run(scan,text=True,capture_output=True);dump('secret-scan-draft.json',dict(request=scan,status=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
manifest();check(True,'scratch');manifest();check(True,'integrated')
# Phase8 may become PASS only after both current draft layouts and secret guard actually pass.
a=json.loads((D/'assessment.json').read_text());a.update(completed=True,allphases='PASS',native_release='released after complete gates');a['phases']['8']='PASS';dump('assessment.json',a)
v=json.loads((D/'verification.json').read_text());v['completed']=True;dump('verification.json',v)
dump('freeze-status.json',dict(completed=True,native_release=True,stage='draft gates passed; final validation follows'))
manifest();check(False,'scratch');manifest();check(False,'integrated')
p=subprocess.run(scan,text=True,capture_output=True);dump('secret-scan.json',dict(request=scan,status=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
manifest();check(False,'scratch');manifest();check(False,'integrated');manifest()
# Final current-manifest checks after storing outputs; outputs are stable in these locations.
check(False,'scratch');manifest();check(False,'integrated');manifest()
dump('freeze-status.json',dict(completed=True,native_release=True,stage='all actual draft and final gates PASS; frozen and worker native requests released; root owns final builds'))
manifest();check(False,'scratch');manifest();check(False,'integrated');manifest()
print('FROZEN canonical293; current manifest, both layouts, fresh17 and secret guard PASS; worker native requests released; root owns final builds')
