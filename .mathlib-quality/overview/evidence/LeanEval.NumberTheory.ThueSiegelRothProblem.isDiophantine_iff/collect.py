from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth')
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def command(n,args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);dump(n,dict(request=args,status=p.returncode,stdout=p.stdout,stderr=p.stderr));return p
command('source-search.json',['rg','--no-ignore','-n','isDiophantine_iff','Roth','Roth.lean'])
command('inline-search.json',['rg','--no-ignore','-n','IsDiophantine|approxSet.*Infinite|exists_pos_div_rpow','Roth','Roth.lean'])
command('full-name-search.json',['rg','-n','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff|theorem isDiophantine_iff|lemma isDiophantine_iff','.lake/packages/mathlib/Mathlib'])
for f,q in [('current','IsDiophantine|isDiophantine|Diophantine.*iff'),('standard','irrationality|irrationality_exponent|irrationalityMeasure'),('abstract','LiouvilleWith|frequently_lt_rpow_neg|exists_pos_div_rpow')]:
 command('formal-'+f+'-rg.json',['rg','-n',q,'.lake/packages/mathlib/Mathlib/NumberTheory'])
command('literature-local.json',['rg','-n','Roth|\\\\kappa|irrational|approximation','.mathlib-quality/references/clean.tex'])
(D/'local-source-section6.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[1138:1194])+'\n')
files=['Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean','Mathlib/NumberTheory/DiophantineApproximation/Basic.lean','Mathlib/NumberTheory/Real/Irrational.lean','Mathlib/Order/ConditionallyCompleteLattice/Finset.lean']
rows=[]
for i,f in enumerate(files):
 p=R/'.lake/packages/mathlib'/f;(D/f'mathlib-source-{i}.lean.txt').write_bytes(p.read_bytes());rows.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,archive=f'mathlib-source-{i}.lean.txt'))
dump('mathlib-inputs.json',rows)
dump('additional-inputs.json',[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size)for p in ['.mathlib-quality/references/clean.tex','.mathlib-quality/overview/declaration-order.json','.mathlib-quality/overview/progress.json']])
(D/'progress-snapshot.json').write_bytes((R/'.mathlib-quality/overview/progress.json').read_bytes())
N='LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff'
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
callers=[x for x in meta if x['name']!=N and 'isDiophantine_iff' in x['source']]
dump('callers.json',dict(canonical_source_callers=callers,lexical_scope='rg --no-ignore Roth/ and Roth.lean; canonical inventory crosscheck',internal_use_count=1,external_to_file=0,inline_rederivations='none in tracked production inventory',source_kernel_simp_distinction='Lexical caller1; direct kernel body1 confirmed exact293; direct type0; no simp attribute on target; transitive dependency closure not claimed'))
dump('prefix-controls.json',dict(shared18_sha256=sha(D/'isolated-prefix.lean.txt'),disk9_sha256=sha(D/'disk-prefix.lean.txt'),authorized19_sha256=hashlib.sha256(('\n'.join((D/'modern-executed.lean.txt').read_text().splitlines()[:19])+'\n').encode()).hexdigest(),authorization='Root fresh292 header read and message approving exact stable18 + LiouvilleWith; no inherited exception'))
dump('project-dependencies.json',dict(statement=['LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine','Roth.approxSet'],body=['LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine','Roth.approxSet','Roth.eventually_div_rpow_lt','Roth.approxSet_den_le_finite','LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux'],private_helper_visibility='last helper is private in Roth.LeanEval; shown using canonical source name, not raw kernel private name',new_proof_credit='Generic uniform/cutoff/Liouville theorem is authored proof, replayed from accepted290modern3 and extended here; none is asserted to be an existing mathlib theorem'))
# Raw receipts stay complete. Record concise matrix without pretending external index matches pin.
mat=[]
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local']:
  f=f'formal-{form}-{method}.json';a=json.loads((D/f).read_text());status='executed'
  if method=='local':
   rr=a['result'];ss=rr.get('structuredContent') or json.loads(rr['content'][0]['text']);status='executed; index='+ss.get('index','unknown')+'; no absence inference'
  mat.append(dict(form=form,method=method,receipt=f,status=status))
assert len(mat)==15;dump('formal-search-matrix.json',mat)
print('Collected sources, callers,17control record, exact15matrix and mathlib inputs')
