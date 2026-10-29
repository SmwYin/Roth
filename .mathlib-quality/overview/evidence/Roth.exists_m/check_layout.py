from pathlib import Path
import subprocess,json,sys,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');draft='--draft'in sys.argv
E=D/'_validation-layout';shutil.rmtree(E,ignore_errors=True);I=E/'.mathlib-quality/overview/evidence/Roth.exists_m';I.mkdir(parents=True)
for x in json.loads((D/'copy-manifest.json').read_text())['files']:
 src=D/('report.md'if x['destination'].endswith('mathlibable/Roth.exists_m.md')else x['destination'].split('/evidence/Roth.exists_m/',1)[1]);dst=E/x['destination'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
shutil.copyfile(D/'copy-manifest.json',I/'copy-manifest.json')
cmd=[sys.executable,str(I/'validate.py'),str(R)]+(['--draft']if draft else[]);p=subprocess.run(cmd,text=True,capture_output=True);print(json.dumps({'command':cmd,'exit_code':p.returncode,'output':p.stdout,'stderr':p.stderr},indent=2));shutil.rmtree(E);sys.exit(p.returncode)
