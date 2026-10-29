"""Actually execute portable validator in scratch and freshly simulated integrated layout."""
from pathlib import Path
import json,tempfile,subprocess,sys,shutil,time
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.ncard_boxFamily';runs=[]
def run(label,path):
 args=[sys.executable,str(path),str(R)];t=time.monotonic();z=subprocess.run(args,text=True,capture_output=True)
 runs.append(dict(layout=label,command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,elapsed_ms=int(1000*(time.monotonic()-t))))
 assert z.returncode==0,(label,z.stdout,z.stderr)
run('scratch',D/'validate.py')
with tempfile.TemporaryDirectory(prefix='layout-',dir=D)as tmp:
 O=Path(tmp)/'.mathlib-quality/overview';E=O/'evidence'/N;M=O/'mathlibable';E.mkdir(parents=True);M.mkdir()
 for p in D.iterdir():
  if p.is_file()and p.name!='report.md':shutil.copy2(p,E/p.name)
 shutil.copy2(D/'report.md',M/(N+'.md'));run('simulated-integrated',E/'validate.py')
(D/'final-validation.json').write_text(json.dumps(dict(status='PASS',actual_executions=True,executions=runs,simulated_layout_removed=True),ensure_ascii=False,indent=2)+'\n')
print('Both actual layout executions PASS.')
