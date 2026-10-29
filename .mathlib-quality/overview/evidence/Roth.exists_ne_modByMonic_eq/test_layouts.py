from pathlib import Path
import json,subprocess,tempfile,shutil,sys
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_ne_modByMonic_eq'
def run(cmd):
 p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);return dict(request=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
def test():
 a=run(['python3',str(D/'validate.py'),str(R)])
 with tempfile.TemporaryDirectory(prefix='integrated-layout-',dir=D)as t:
  O=Path(t)/'overview';E=O/'evidence'/N;E.mkdir(parents=True);M=O/'mathlibable';M.mkdir()
  for p in D.iterdir():
   if p.is_file():shutil.copy2(p,E/p.name)
  (E/'report.md').unlink();shutil.copy2(D/'report.md',M/(N+'.md'))
  b=run(['python3',str(E/'validate.py'),str(R)])
 return dict(scratch=a,integrated_report_outside_evidence=b)
if __name__=='__main__':
 x=test();print(json.dumps(x,indent=2));assert all(v['exit_code']==0 for v in x.values())
 if '--no-write'not in sys.argv:(D/'validation-result.json').write_text(json.dumps(x,indent=2)+'\n')
