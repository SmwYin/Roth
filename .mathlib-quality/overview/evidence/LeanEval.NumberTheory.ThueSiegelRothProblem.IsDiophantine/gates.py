from pathlib import Path
import subprocess,json,sys
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');draft='--draft'in sys.argv
commands=[('validation-draft-scratch.json'if draft else'validation-scratch.json',['python3',str(D/'validate.py'),str(R)]+(['--draft']if draft else[])),('validation-draft-integrated.json'if draft else'validation-integrated.json',['python3',str(D/'check_layout.py')]+(['--draft']if draft else[])),('secret-scan-draft.json'if draft else'secret-scan.json',['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)])]
for name,args in commands:
 p=subprocess.run(args,cwd=R,text=True,capture_output=True)
 (D/name).write_text(json.dumps(dict(request=args,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)),indent=2)+'\n')
 print(name,p.returncode,p.stdout,p.stderr)
 assert p.returncode==0
 subprocess.run(['python3',str(D/'manifest.py')],check=True)
