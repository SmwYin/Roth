from pathlib import Path
import json,subprocess,time,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.sub_mem_RSet'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def run(cmd):
 t=time.monotonic();z=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
 x=dict(command=[str(c)for c in cmd],exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,elapsed_ms=int((time.monotonic()-t)*1000))
 print(z.stdout,end='');print(z.stderr,end='');assert z.returncode==0,x;return x
def manifest():run(['python3',str(D/'freeze.py')])
def integrated():
 base=D/'.simulation';assert not base.exists();E=base/'.mathlib-quality/overview/evidence'/N;M=base/'.mathlib-quality/overview/mathlibable';E.mkdir(parents=True);M.mkdir(parents=True)
 try:
  for p in D.iterdir():
   if p.is_file():shutil.copyfile(p,(M/(N+'.md'))if p.name=='report.md'else E/p.name)
  return run(['python3',str(E/'validate.py'),str(R)])
 finally:shutil.rmtree(base)
if not(D/'final-validation.json').exists():put('final-validation.json',dict(status='pending actual validation'))
manifest()
scratch=run(['python3',str(D/'validate.py'),str(R)]);sim=integrated()
put('final-validation.json',dict(status='PASS',scratch=scratch,simulated_integrated=sim,simulation_removed=True,final_current_manifest_rechecks='Repeated after final record, guard and freeze-marker creation; exact output in finalization receipt.'))
guard=run(['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(D)]);put('secret-guard.json',guard)
put('frozen.json',dict(declaration=N,status='complete-frozen',root_acceptance='pending',native_ownership_release='Explicitly released to root after final current-manifest validators PASS.',completed=True,unresolved=[],frozen_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())))
manifest()
run(['python3',str(D/'validate.py'),str(R)]);integrated()
print('PASS FINAL: completed250 package frozen; both actual layouts checked against final current manifest')
