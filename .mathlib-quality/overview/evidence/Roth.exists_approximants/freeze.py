from pathlib import Path
import json,subprocess,hashlib
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_approximants'
def put(n,o):(D/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def run(args):
 z=subprocess.run(args,cwd=R,text=True,capture_output=True);o=dict(request=dict(command=args),result=dict(exit_code=z.returncode,output=z.stdout,stderr=z.stderr));assert z.returncode==0,o;return o
def manifest():run(['python3',str(D/'manifest.py')])
a=json.loads((D/'assessment.json').read_text());assert not a['completed']and a['phases']['8']=='pending'
base=json.loads((D/'input-manifest.json').read_text())['sources_and_pins'];fresh=[]
for p,v in base.items():
 q=R/p;h=hashlib.sha256(q.read_bytes()).hexdigest();assert h==v['sha256'];fresh.append(dict(path=p,sha256=h,bytes=q.stat().st_size,match=True))
assert fresh==json.loads((D/'inputs.json').read_text());put('fresh-final-inputs.json',dict(unchanged=True,inputs=fresh))
manifest()
put('validation-draft-scratch.json',run(['python3',str(D/'validate.py'),str(R),'--draft']));manifest()
put('validation-draft-integrated.json',run(['python3',str(D/'check_layout.py'),'--draft']));manifest()
put('secret-scan.json',run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)]));manifest()
# All actual required gates passed with completedfalse/phase8pending, before final status mutation.
a.update(completed=True,allphases='PASS');a['phases']['8']='PASS';put('assessment.json',a)
v=json.loads((D/'verification.json').read_text());v['completed']=True;put('verification.json',v)
manifest()
put('validation-scratch.json',run(['python3',str(D/'validate.py'),str(R)]));manifest()
put('validation-integrated.json',run(['python3',str(D/'check_layout.py')]));manifest()
s=(D/'report.md').read_text().replace('This is a completed mathematical\nassessment once the final package gates pass;','All final package gates passed; this is a completed mathematical\nassessment;')
s+='\nFinal gates: [scratch validation](../evidence/'+N+'/validation-scratch.json), [integrated validation](../evidence/'+N+'/validation-integrated.json), [secret scan](../evidence/'+N+'/secret-scan.json). All passed; completed=true, unresolved[], root acceptance pending.\n';(D/'report.md').write_text(s)
put('secret-scan.json',run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)]));manifest()
print(run(['python3',str(D/'validate.py'),str(R)])['result']['output'],end='')
print(run(['python3',str(D/'check_layout.py')])['result']['output'],end='')
print('FREEZE canonical277; all native requests resolved; preparation phase released to root')
