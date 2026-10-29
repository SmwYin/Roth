from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth')
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def command(n,args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);dump(n,dict(request=args,status=p.returncode,stdout=p.stdout,stderr=p.stderr));return p
command('source-search.json',['rg','--no-ignore','-n','thueSiegelRoth','Roth','Roth.lean'])
command('source-search-git.json',['git','grep','-n','thueSiegelRoth','--','Roth/*.lean','Roth.lean'])
command('inline-search.json',['rg','--no-ignore','-n','IsDiophantine|roth_rat|theorem roth|approxSet.*Infinite','Roth','Roth.lean'])
command('full-name-search.json',['rg','-n','LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth|theorem thueSiegelRoth|lemma thueSiegelRoth|theorem thue_siegel_roth','.lake/packages/mathlib/Mathlib'])
for f,q in [('current','IsDiophantine|isDiophantine|thueSiegelRoth|thue_siegel_roth'),('standard','Roth|irrationality|irrationality_exponent|irrationalityMeasure'),('abstract','LiouvilleWith|frequently_lt_rpow_neg|exists_pos_real_of_irrational_root')]:
 command('formal-'+f+'-rg.json',['rg','-n',q,'.lake/packages/mathlib/Mathlib/NumberTheory'])
command('literature-local.json',['rg','-n','Roth|\\\\kappa|irrational|approximation','.mathlib-quality/references/clean.tex'])
(D/'local-source-section6.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[1138:1194])+'\n')
files=['Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean','Mathlib/NumberTheory/DiophantineApproximation/Basic.lean','Mathlib/NumberTheory/Transcendental/Liouville/Basic.lean','Mathlib/RingTheory/Algebraic/Basic.lean','Mathlib/RingTheory/Localization/FractionRing.lean']
rows=[]
for i,f in enumerate(files):
 p=R/'.lake/packages/mathlib'/f;(D/f'mathlib-source-{i}.lean.txt').write_bytes(p.read_bytes());rows.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,archive=f'mathlib-source-{i}.lean.txt'))
dump('mathlib-inputs.json',rows)
dump('additional-inputs.json',[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size)for p in ['.mathlib-quality/references/clean.tex','.mathlib-quality/overview/declaration-order.json','.mathlib-quality/overview/progress.json']])
(D/'progress-snapshot.json').write_bytes((R/'.mathlib-quality/overview/progress.json').read_bytes())
N='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth'
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
callers=[x for x in meta if x['name']!=N and 'thueSiegelRoth' in x['source']]
assert not callers
dump('callers.json',dict(canonical_source_callers=callers,lexical_scope='rg --no-ignore Roth/ and Roth.lean and git grep tracked production; canonical inventory crosscheck',internal_use_count=0,external_to_file=0,inline_rederivations='No separate benchmark uniform statement rederived; Roth.roth and Roth.roth_rat are intentional equivalent main endpoints, read fully',source_kernel_simp_distinction='Lexical0; fresh native exact293 direct kernel body0/type0; target no simp tag; transitive dependencies not counted; final benchmark endpoint not dead code'))
dump('prefix-controls.json',dict(shared18_sha256=sha(D/'isolated-prefix.lean.txt'),disk9_sha256=sha(D/'disk-prefix.lean.txt'),authorized19_sha256=hashlib.sha256(('\n'.join((D/'modern-executed.lean.txt').read_text().splitlines()[:19])+'\n').encode()).hexdigest(),project10_sha256=hashlib.sha256(('\n'.join((D/'project-modern-executed.lean.txt').read_text().splitlines()[:10])+'\n').encode()).hexdigest(),authorization='Root fresh293 header review authorized exact19 isolated; separately authorized exact disk9+LiouvilleWith10 PROJECT context only. No persistent prefix mutation.'))
dump('project-dependencies.json',dict(statement=['LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'],lexical_body=['LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff','Roth.roth'],kernel_body=['LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff','Roth.roth','Roth.approxSet'],private_helper_visibility='No direct private helper in final target; equivalence transitive closure includes its private positive-minimum helper.',new_proof_credit='Generic UniformBound/all-real pair/Liouville bridge replay adapted from accepted292 modern proof (itself credits accepted290 and288). Not existing mathlib. Final endpoint proof uses actual Roth.roth, project content.'))
mat=[]
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local']:
  f=f'formal-{form}-{method}.json';a=json.loads((D/f).read_text());status='executed'
  if method=='local':
   rr=a['result'];ss=rr.get('structuredContent') or json.loads(rr['content'][0]['text']);status='executed; index='+ss.get('index','unknown')+'; no absence inference'
  mat.append(dict(form=form,method=method,receipt=f,status=status))
assert len(mat)==15;dump('formal-search-matrix.json',mat)
command('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-8','--format=%H %ad %an %s','--date=short','--','Mathlib/NumberTheory/Transcendental/Liouville','Mathlib/NumberTheory/DiophantineApproximation'])
command('reviewer-mathematical-commits.json',['git','-C','.lake/packages/mathlib','log','--all','-8','--grep=Diophantine\\|Liouville','--format=%H %ad %an %s','--date=short','--','Mathlib/NumberTheory'])
print('Collected exact15formal matrix, fresh sources/hashes, zero callers, reviewer evidence')
