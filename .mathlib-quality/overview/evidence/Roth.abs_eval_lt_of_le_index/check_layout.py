from pathlib import Path
import json,subprocess,shutil,sys
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.abs_eval_lt_of_le_index'
def run(args):
 r=subprocess.run(args,cwd=R,text=True,capture_output=True);return dict(request=args,result=dict(exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
# Layout checks use a disposable package-local directory excluded from artifact manifests.
root=D/'_validation-layout';shutil.rmtree(root,ignore_errors=True)
e=root/'.mathlib-quality/overview/evidence'/N;m=root/'.mathlib-quality/overview/mathlibable';e.mkdir(parents=True);m.mkdir(parents=True)
for p in D.rglob('*'):
 if not p.is_file()or '_validation-layout'in p.relative_to(D).parts:continue
 rel=p.relative_to(D)
 if str(rel)=='report.md':shutil.copy2(p,m/(N+'.md'))
 else:(e/rel).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,e/rel)
for kind,args in [('scratch',['python3',str(D/'validate.py'),str(R)]),('integrated',['python3',str(e/'validate.py'),str(R)])]:
 args+=['--draft']if'--draft'in sys.argv else[]
 x=run(args);assert x['result']['exit_code']==0,x
 (D/('validation-'+kind+'.json')).write_text(json.dumps(x,indent=2)+'\n')
shutil.rmtree(root)
print('Both portable layouts PASS')
