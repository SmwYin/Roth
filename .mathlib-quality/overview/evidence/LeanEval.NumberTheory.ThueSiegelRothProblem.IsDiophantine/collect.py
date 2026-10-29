from pathlib import Path
import subprocess,json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
N='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def run(n,args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);dump(n,dict(request=args,status=p.returncode,stdout=p.stdout,stderr=p.stderr))
for form,pat in [('current',r'IsDiophantine|[Dd]iophantine|2 \+.*ε'),('standard',r'irrationality.*(measure|exponent)|approximation.*exponent|[Rr]oth'),('abstract',r'LiouvilleWith|liouvilleWith|irrational_add_ratCast_iff')]:run('formal-'+form+'-rg.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib/NumberTheory'])
run('source-search.json',['rg','--no-ignore','-n','IsDiophantine','Roth','Roth.lean'])
run('tracked-source-search.json',['git','grep','-n','IsDiophantine','--','Roth','Roth.lean'])
run('full-name-search.json',['rg','-n',N,'.lake/packages/mathlib/Mathlib'])
run('inline-search.json',['rg','--no-ignore','-n','∀ ε|2 \+ ε|IsDiophantine|LiouvilleWith','Roth','Roth.lean'])
run('literature-local.json',['rg','-n','irrationality|Roth|algebraic number|approximat','.mathlib-quality/references/clean.tex'])
run('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-10','--format=%H %ad %an %s','--date=short','--','Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean'])
mods=['NumberTheory/Transcendental/Liouville/LiouvilleWith.lean','NumberTheory/Transcendental/Liouville/Basic.lean','NumberTheory/Real/Irrational.lean','Topology/Instances/Irrational.lean']
inputs=[]
for i,m in enumerate(mods):
 p=R/'.lake/packages/mathlib/Mathlib'/m;a=f'mathlib-source-{i}.lean.txt';(D/a).write_bytes(p.read_bytes());inputs.append(dict(path=str(p.relative_to(R)),archive=a,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
dump('mathlib-inputs.json',inputs)
dump('progress-snapshot.json',json.loads((R/'.mathlib-quality/overview/progress.json').read_text()))
dump('prefix-controls.json',dict(isolated_import_count=18,disk_import_count=9,isolated_sha256='21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217',disk_sha256='363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593',root_exclusive_native=True))
dump('prefix-authorization.json',dict(authorized_by='root explicit message after fresh pinned header read',extra_import='Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith',authorized_isolated_prefix_sha256='effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc',shared18_unchanged=True,disk9_unchanged=True))
print('Collected full searches and pinned snapshots')
