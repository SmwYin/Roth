"""Execute and archive actual validator checks in scratch and integrated layouts."""
from pathlib import Path
import json,subprocess,shutil,time,sys
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_monic_aeval_eq_zero'
draft='--draft' in sys.argv

def run(args):
 start=time.monotonic();z=subprocess.run(args,capture_output=True,text=True,cwd=R)
 rec=dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,
          elapsed_ms=int(1000*(time.monotonic()-start)))
 print(z.stdout,z.stderr);assert z.returncode==0,rec
 return rec
scratch=run(['python3',str(D/'validate.py'),str(R)]+(['--draft'] if draft else []))
T=D/'portable-check';E=T/'.mathlib-quality/overview/evidence'/N
try:
 E.mkdir(parents=True)
 for x in json.load(open(D/'copy-manifest.json'))['files']:
  p=T/x['destination'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(x['source'],p)
 shutil.copy2(D/'copy-manifest.json',E/'copy-manifest.json')
 integrated=run(['python3',str(E/'validate.py'),str(R)]+(['--draft'] if draft else []))
finally:
 if T.exists():shutil.rmtree(T)
out='draft-validation.json' if draft else 'final-validation.json'
if '--no-record' not in sys.argv:
 (D/out).write_text(json.dumps(dict(status='PASS',draft=draft,scratch_layout=scratch,
  integrated_layout=integrated,temporary_integrated_test_removed=True),indent=2)+'\n')
