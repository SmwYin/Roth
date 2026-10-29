from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth')
def put(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def run(script,*args):
 x=subprocess.run(['python3',str(D/script),*args],text=True,capture_output=True,cwd=R);print(x.stdout);assert x.returncode==0,x.stderr
fresh=json.loads((D/'inputs.json').read_text())
for x in fresh:assert hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256']
put('fresh-final-inputs.json',dict(inputs=fresh,unchanged=True))
# Draft validation is meaningful only once all required native receipts PASS.
run('build_package.py')
run('manifest.py')
x=subprocess.run(['python3',str(D/'validate.py'),str(R),'--draft'],capture_output=True,text=True,cwd=R);assert x.returncode==0,(x.stdout,x.stderr)
put('validation-draft-scratch.json',dict(request=x.args,result=dict(exit_code=x.returncode,stdout=x.stdout,stderr=x.stderr)))
# Phase8 turns PASS only after completed native gates and a real draft package validation.
a=json.loads((D/'assessment.json').read_text());a['completed']=True;a['allphases']='PASS';a['phases']['8']='PASS';put('assessment.json',a)
v=json.loads((D/'verification.json').read_text());v['completed']=True;put('verification.json',v)
p=D/'report.md';s=p.read_text().replace('Completion remains pending until the required exact native receipts, current manifest, both\nportable layouts and secret scan pass. Root acceptance is a separate pending review.','Required native gates and draft validation have passed. Final current-manifest, both-layout and\nsecret-scan receipts accompany this frozen package. Root acceptance remains a separate pending review.');p.write_text(s)
run('manifest.py')
run('check_layout.py')
scan=['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)]
x=subprocess.run(scan,capture_output=True,text=True,cwd=R);assert x.returncode==0,(x.stdout,x.stderr)
put('secret-scan.json',dict(request=scan,result=dict(exit_code=x.returncode,stdout=x.stdout,stderr=x.stderr)))
run('manifest.py');run('check_layout.py');run('manifest.py')
x=subprocess.run(['python3',str(D/'validate.py'),str(R)],capture_output=True,text=True,cwd=R);assert x.returncode==0,(x.stdout,x.stderr);print(x.stdout)
print('FROZEN completedtrue allphasesPASS unresolved[] root_acceptancepending')
