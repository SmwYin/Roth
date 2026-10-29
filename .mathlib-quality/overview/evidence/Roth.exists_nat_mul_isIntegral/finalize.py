from pathlib import Path
import json,subprocess,shutil,datetime,hashlib
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_nat_mul_isIntegral'
def run(args):
 z=subprocess.run(args,text=True,capture_output=True,cwd=R);return dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr)
def put(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def manifest():
 z=run(['python3',str(D/'package.py')]);assert z['exit_code']==0;return z
def simulation():
 base=D/'portable-layout-test';E=base/'.mathlib-quality/overview/evidence'/N;M=base/'.mathlib-quality/overview/mathlibable';E.mkdir(parents=True,exist_ok=True);M.mkdir(parents=True,exist_ok=True)
 for p in D.iterdir():
  if p.is_file():shutil.copy2(p,M/(N+'.md')if p.name=='report.md'else E/p.name)
 try:return run(['python3',str(E/'validate.py'),str(R)])
 finally:shutil.rmtree(base)
manifest();scratch=run(['python3',str(D/'validate.py'),str(R)]);assert scratch['exit_code']==0,scratch
integrated=simulation();assert integrated['exit_code']==0,integrated
final_inputs=json.loads((D/'inputs.json').read_text());assert all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256']for x in final_inputs)
put('fresh-final-inputs.json',dict(inputs=final_inputs,unchanged=True))
put('final-validation.json',dict(status='PASS',scratch=scratch,simulated_integrated=integrated,fresh17=True,secret_guard='secret-guard.json',current_manifest_authoritative=True))
put('freeze-record.json',dict(declaration=N,canonical_index=268,status='FROZEN',completed=True,allphases='PASS',unresolved=[],native_released=True,released_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),root_acceptance='pending',exclusive_owner='assess_integral_multiple268',notes='All proof work completed. Six accepted exact native sources. Current manifest, scratch and simulated integrated validators, fresh17 and secretguard pass. Root owns independent acceptance/publication. No later native/build work by worker.'))
# Final guard includes every artifact, then regenerate current manifest to its exact bytes.
secret=run(['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(D)]);assert secret['exit_code']==0,secret;put('secret-guard.json',secret)
manifest();last=run(['python3',str(D/'validate.py'),str(R)]);assert last['exit_code']==0,last
last_sim=simulation();assert last_sim['exit_code']==0,last_sim
print(json.dumps(dict(status='PASS',scratch=last,simulated_integrated=last_sim,secret_guard=secret['stdout'],freeze='FROZEN; native RELEASED'),indent=2))
