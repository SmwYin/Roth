from pathlib import Path
import json,subprocess,sys,shutil
D=Path(__file__).resolve().parent;R='/Users/ramin/LEAN/Roth';N='Roth.exists_reduced_approx'
draft=['--draft']if '--draft'in sys.argv else[]
if 'integrated'in sys.argv:
 T=D/'_validation-layout';shutil.rmtree(T,ignore_errors=True)
 E=T/'.mathlib-quality/overview/evidence'/N;M=T/'.mathlib-quality/overview/mathlibable';E.mkdir(parents=True);M.mkdir(parents=True)
 for p in D.rglob('*'):
  if not p.is_file()or '_validation-layout'in p.parts:continue
  rel=p.relative_to(D)
  if str(rel)=='report.md':dest=M/(N+'.md')
  else:dest=E/rel
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 cmd=['python3',str(E/'validate.py'),R]+draft
else:cmd=['python3',str(D/'validate.py'),R]+draft
z=subprocess.run(cmd,text=True,capture_output=True)
print(json.dumps({'request':{'argv':cmd},'result':{'exit_code':z.returncode,'output':z.stdout,'stderr':z.stderr}},indent=2))
sys.exit(z.returncode)
