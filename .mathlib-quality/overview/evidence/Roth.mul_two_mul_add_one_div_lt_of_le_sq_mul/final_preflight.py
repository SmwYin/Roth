from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');s=D/'original-executed.lean.txt'
(D/'original-first-receipt.json').write_bytes((D/'original-receipt.json').read_bytes())
(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_bytes(s.read_bytes())
cmd=['python3','/private/tmp/roth-overview/check_audit_source.py',str(s)];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
r=dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr),source_sha256=hashlib.sha256(s.read_bytes()).hexdigest());(D/'preparation-checks.json').write_text(json.dumps(r,indent=2)+'\n');assert p.returncode==0
print(p.stdout,end='')
