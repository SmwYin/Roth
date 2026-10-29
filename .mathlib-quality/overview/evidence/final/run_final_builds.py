"""Run the two final literal builds, only after root owns native and293 is reviewed."""
from pathlib import Path
import json,hashlib,subprocess,sys,time,datetime,shutil
R=Path('/Users/ramin/LEAN/Roth');B=Path('/private/tmp/roth-overview');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sys.argv[1:]==['--root-owns-native']
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());assert len(p['completed_declarations'])==292
N='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth';assert p['next_declaration']==N
D=B/'assess'/N;a=json.loads((D/'assessment.json').read_text());rr=json.loads((D/'root-review.json').read_text());assert a['completed']and not a['unresolved']and rr['status']=='PASS'and rr['report_sha256']==H(D/'report.md')
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())['sources_and_pins'];assert len(base)==17
for f,x in base.items():assert H(R/f)==x['sha256']
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='ramin-cleanup'
assert shutil.which('lake'),'lake executable unavailable'
def run(command,filename):
 log=B/filename;start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.perf_counter()
 with log.open('w')as out:q=subprocess.run(command,cwd=R,text=True,stdout=out,stderr=subprocess.STDOUT)
 rec={'command':command,'cwd':str(R),'resolved_lake':shutil.which('lake'),'started_utc':start,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_ms':round((time.perf_counter()-t)*1000,3),'exit_code':q.returncode,'log':str(log),'log_sha256':H(log),'warning_count':log.read_text().count('warning:')}
 print(json.dumps(rec),flush=True);return rec
first=run(['lake','build'],'final-lake-build.log')
out=dict(first,status='RUNNING',runner_source=str(Path(__file__).resolve()),runner_sha256=H(Path(__file__)),scope='Actual final literal builds after all declaration assessments/root review; no production edits')
pth=B/'final-build-verification.json';pth.write_text(json.dumps(out,indent=2)+'\n')
assert first['exit_code']==0,'Full lake build failed; do not publish'
second=run(['lake','build','Roth.LeanEval'],'final-lake-build-LeanEval.log');out['lean_eval']=second
out['status']='PASS'if second['exit_code']==0 else'FAIL';out['sources_and_pins']={f:{'sha256':H(R/f),'matches_baseline':H(R/f)==x['sha256']}for f,x in base.items()};pth.write_text(json.dumps(out,indent=2)+'\n')
assert second['exit_code']==0 and all(x['matches_baseline']for x in out['sources_and_pins'].values()),'Final LeanEval/source validation failed; do not publish'
for rec in[first,second]:assert 'Build completed successfully'in Path(rec['log']).read_text()
print('PASS actual final lake build AND lake build Roth.LeanEval, fresh17 unchanged',flush=True)
