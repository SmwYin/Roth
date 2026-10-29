from pathlib import Path
import sys,json,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.roth'
draft='--draft'in sys.argv
layout=D/'_validation-layout';e=layout/'.mathlib-quality/overview/evidence'/N
if layout.exists():shutil.rmtree(layout)
e.mkdir(parents=True)
manifest=json.loads((D/'copy-manifest.json').read_text())
for x in manifest['files']:
 dest=layout/x['destination'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(x['source'],dest)
shutil.copyfile(D/'copy-manifest.json',e/'copy-manifest.json')
args=['python3',str(e/'validate.py'),str(R)]+(['--draft']if draft else[])
p=subprocess.run(args,text=True,capture_output=True)
if '--record'in sys.argv:
 name='validation-draft-integrated.json'if draft else'validation-integrated.json'
 (D/name).write_text(json.dumps(dict(request=args,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)),indent=2)+'\n')
print(p.stdout,p.stderr,end='');sys.exit(p.returncode)
