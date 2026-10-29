"""Validate one current-frontier worker request for the ROOT's native executor.
No native tool runs here; writes only the existing untracked scratch file for disk checks.
"""
from pathlib import Path
import json,hashlib,sys,re,shutil,subprocess
R=Path('/Users/ramin/LEAN/Roth');B=Path('/private/tmp/roth-overview');O=R/'.mathlib-quality/overview';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
assert len(sys.argv)==2
owner=load(B/'native-owner.json');assert owner['owner']=='root'and owner['exclusive']
p=load(O/'progress.json');N=p['next_declaration'];assert len(p['completed_declarations'])>=269
D=B/'assess'/N;f=Path(sys.argv[1]).resolve();assert f.parent==D/'root-requests'and f.suffix=='.json'
q=load(f);assert re.fullmatch('[A-Za-z0-9_-]+',q['id']);op=q['operation'];assert op in ['diagnostics','run_code','local_search']
receipt=D/q['receipt'];assert receipt.parent==D and receipt.suffix=='.json'and not receipt.exists(),receipt
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='ramin-cleanup'
for path,v in load(O/'evidence/shared/input-manifest.json')['sources_and_pins'].items():assert H(R/path)==v['sha256']
args=q['arguments'];source=None;audit=None
if op in ['diagnostics','run_code']:
 source=D/q['source'];assert source.parent==D and source.name.endswith('.lean.txt')and H(source)==q['source_sha256']
 s=source.read_text();assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 if op=='diagnostics':
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert H(D/'disk-prefix.lean.txt')=='363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593'
  assert len(re.findall('^import ',s,re.M))==9
  assert args['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
  assert set(args)<={'file_path','timeout_s','start_line'}and 0<args.get('timeout_s',45)<=60 and 0<args.get('start_line',1)<=16
  if q.get('original_audit'):
   command=['python3',str(B/'check_audit_source.py'),str(source)];z=subprocess.run(command,text=True,capture_output=True)
   assert z.returncode==0,z.stdout+z.stderr
   audit=dict(command=command,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr)
  shutil.copyfile(source,R/args['file_path']);assert H(R/args['file_path'])==H(source)
 else:
  assert args=={}
  prefix='\n'.join(x for x in s.splitlines()if x.startswith('import '))+'\n'
  if q.get('context')=='project_endpoint293':
   assert N=='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth'
   disk=D/'disk-prefix.lean.txt';assert H(disk)=='363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593'
   expected='\n'.join(x for x in disk.read_text().splitlines()if x.startswith('import '))+'\nimport Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
   assert prefix==expected and len(re.findall('^import ',s,re.M))==10
   approved=load(B/'native-prefix-authorizations.json')[N]['project_context_exception']
   assert approved['context']==q['context'] and approved['operation']==op and approved['prefix_sha256']==hashlib.sha256(prefix.encode()).hexdigest()
   audit=dict(scope='Explicit root-approved final293 project-context endpoint experiment; not mathlib-only composition evidence; persistent disk9 and isolated18 unchanged',prefix_sha256=hashlib.sha256(prefix.encode()).hexdigest())
  else:
   assert not q.get('context') and not re.search(r'^import (?!Mathlib\.)',s,re.M)
   base=(B/'current-isolated-prefix.lean.txt').read_text();assert s.startswith(base)
   if prefix!=base:
    a=load(B/'native-prefix-authorizations.json')[N]
    assert hashlib.sha256(prefix.encode()).hexdigest()in a['prefix_sha256']
  args={'code':s}
else:
 assert args.get('project_root')==str(R)and set(args)<={'query','project_root','limit'}
 assert isinstance(args['query'],str)and 0<args.get('limit',20)<=100
print(json.dumps(dict(id=q['id'],operation=op,arguments=args,receipt=str(receipt),worker_request=q,preexecution_audit=audit,source=str(source)if source else None),ensure_ascii=True))
