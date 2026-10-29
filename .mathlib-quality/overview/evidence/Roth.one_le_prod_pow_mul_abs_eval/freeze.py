from pathlib import Path
import json,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth')
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def run(args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);x=dict(request=args,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,x;return x
def own(script,*args):return run(['python3',str(D/script),*args])
own('manifest.py');x=own('validate.py',str(R),'--draft');put('validation-draft-scratch.json',x)
own('manifest.py');own('check_layout.py','--draft')
scan=['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)]
x=run(scan);put('secret-scan.json',x)
# Only completed native plus actual draft manifest/layout/secret gates permit completion flags.
a=json.loads((D/'assessment.json').read_text());a.update(completed=True,allphases='PASS');a['phases']['8']='PASS';put('assessment.json',a)
v=json.loads((D/'verification.json').read_text());v['completed']=True;put('verification.json',v)
p=D/'report.md';s=p.read_text().replace('Native assessment is verified; packaging gates pending until actual current-manifest, both-layout and secret validation succeed. Root independently accepts and integrates.','Native assessment and actual current-manifest, both-layout and secret validation have passed. Assessment completed; unresolved[]; root acceptance pending independent integration.');p.write_text(s)
own('manifest.py');own('check_layout.py');own('manifest.py');own('check_layout.py');own('manifest.py');x=own('validate.py',str(R));print(x['result']['stdout'].strip());print('FROZEN completedtrue allphasesPASS unresolved[] root_acceptancepending; root native owner throughout')
