# coding: utf-8
from pathlib import Path
import hashlib,json,shutil,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='MvPolynomial.degreeOf_taylor_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def rg(label,pattern,paths):
 args=['rg','-n',pattern,*paths];r=subprocess.run(args,cwd=R,capture_output=True)
 out('rg-'+label+'.json',dict(args=args,exit_code=r.returncode,stdout=r.stdout.decode('utf-8'),stderr=r.stderr.decode('utf-8')))
for label,pattern,paths in [
 ('current',r'degreeOf_taylor|taylor.*degreeOf|degreeOf.*taylor',['.lake/packages/mathlib/Mathlib']),
 ('literature',r'natDegree_taylor|degree_taylor|degreeOf_eq_natDegree',['.lake/packages/mathlib/Mathlib/Algebra']),
 ('abstract',r'degreeOf_aeval|degreeOf_eval₂|degreeOf_bind|degrees_aeval|aeval_natDegree_le|degreeOf_(sum|prod|pow)_le',['.lake/packages/mathlib/Mathlib']),
 ('full-name',r'MvPolynomial\.degreeOf_taylor_le|\b(theorem|lemma)\s+degreeOf_taylor_le\b',['.lake/packages/mathlib/Mathlib']),
 ('callers',r'\bdegreeOf_taylor_le\b',['Roth.lean','Roth']),
 ('inline',r'degreeOf_le_iff|degreeOf_taylor|hasseDeriv_eq_zero_of_degreeOf_lt',['Roth.lean','Roth']),
 ('local-literature',r'Taylor|degree|i_j|r_j',['.mathlib-quality/references/clean.tex'])]:rg(label,pattern,paths)
manifest=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for p,x in manifest['sources_and_pins'].items():
 f=R/p;inputs.append(dict(path=p,sha256=sha(f),baseline_sha256=x['sha256'],bytes=f.stat().st_size,match=sha(f)==x['sha256']))
assert len(inputs)==17 and all(x['match'] for x in inputs)
out('inputs.json',inputs);out('input-hash-check.json',dict(all_pass=True,count=17))
shutil.copy(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
entries=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());out('canonical-entry.json',next(x for x in entries if x['name']==N))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
if isinstance(order,dict):order=order.get('declarations',order.get('order',[]))
out('order-entry.json',next(x for x in order if x['name']==N))
links={'Roth/Taylor.lean':'Taylor-module.lean.txt','Roth/Index.lean':'Index-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Degrees.lean':'MvPolynomial-Degrees-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean':'Polynomial-Taylor-module.lean.txt','.lake/packages/mathlib/Mathlib/RingTheory/Polynomial/Basic.lean':'Polynomial-Basic-module.lean.txt'}
mi=[]
for p,n in links.items():
 shutil.copy(R/p,D/n)
 if p.startswith('.lake'):mi.append(dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size))
out('mathlib-inputs.json',mi)
clean=R/'.mathlib-quality/references/clean.tex';out('local-literature.json',dict(path=str(clean.relative_to(R)),sha256=sha(clean),bytes=clean.stat().st_size,lines='501–548;650–667',role='Taylor expansion with coordinate box and index bound'))
s=clean.read_text(encoding='utf-8').splitlines();(D/'clean-excerpts.tex.txt').write_text('\n'.join(s[500:549]+s[649:668])+'\n',encoding='utf-8')
out('callers.json',dict(named_callers=[dict(declaration='Roth.index_le_card',file='Roth/Index.lean',line=229,role='transport support exponent bound through translated degree',verified='full caller native-extra')],explicit_count=1,source_occurrences=['Roth/Taylor.lean:170 declaration','Roth/Index.lean:229 caller'],inline_audit='Other degreeOf_le_iff uses bound derivatives, substitutions, or support boxes; no independent constant-translation degree rederivation found.',limitations='Named source references, not exhaustive kernel/simp closure. Target not simp-tagged.'))
out('proof-body-diagnostic.json',dict(concrete_identifier='taylor',body_occurrences=1,abstract='degreeOf bound from vanishing of coefficients above a coordinate threshold',existing=['degreeOf_le_iff','mem_support_iff'],essential_project=['coeff_taylor','hasseDeriv_eq_zero_of_degreeOf_lt'],warning='Abstract criterion needs the actual vanishing premise; it is not a replacement proof of translation degree.'))
q=['git','-C','.lake/packages/mathlib','log','-12','--format=%h %an %s','--','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/Polynomial/Taylor.lean'];r=subprocess.run(q,cwd=R,capture_output=True);out('reviewer-history.json',dict(args=q,exit_code=r.returncode,stdout=r.stdout.decode('utf-8'),stderr=r.stderr.decode('utf-8')))
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());out('accepted-yes-grouping.json',[x for x in progress['completed_declarations'] if x['declaration'] in ['MvPolynomial.coeff_taylor','MvPolynomial.degreeOf_hasseDeriv_le','MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt','MvPolynomial.hasseDeriv']])
accepted=[]
for label in ['target','raw','extra']:
 for ending in ['executed.lean.txt','success.json']:shutil.copy(Path('/private/tmp/roth-overview')/f'degree-taylor-{label}-{ending}',D/f'native-{label}-{ending}')
 accepted.append(dict(label=label,source=f'native-{label}-executed.lean.txt',source_sha256=sha(D/f'native-{label}-executed.lean.txt'),receipt=f'native-{label}-success.json',proof_check=True))
rejected=[]
for p in Path('/private/tmp/roth-overview').glob('degree-taylor-*-rejected*'):
 shutil.copy(p,D/p.name.replace('degree-taylor-','native-'));rejected.append(p.name.replace('degree-taylor-','native-'))
out('verification.json',dict(declaration=N,standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,inputs='inputs.json',mathlib_inputs='mathlib-inputs.json',source_links=links,composition=dict(result='NOT-COMPOSABLE from currently demonstrated mathlib facts',essential_new_content='coeff_taylor and Hasse vanishing above coordinate degree; raw coefficient criterion assumes rather than proves this premise'),unresolved=[]))
out('assessment.json',dict(declaration=N,canonical_index=69,source='Roth/Taylor.lean:170',kind='theorem',verdict='YES-add-as-is',completed=True,allphases='PASS',phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']},justified_na={'2b':'Theorem, not a data definition.','4.5':'Theorem introduces no data/instance; all six infrastructure risks n/a.'},unresolved=[],root_acceptance='pending',production_unchanged=True))
out('overview-entry.json',dict(declaration=N,kind='theorem',type='∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (j : σ) (P : MvPolynomial σ R), MvPolynomial.degreeOf j (MvPolynomial.taylor α P) ≤ MvPolynomial.degreeOf j P',what='Constant coordinate translation does not increase degree in any chosen variable.',how='An exponent above the original coordinate degree has zero Hasse derivative, hence zero translated coefficient; apply the support characterization of degree.',hypotheses='Arbitrary independent-universe σ,R; CommSemiring R; arbitrary shift, variable and polynomial. No finiteness, nonzero, domain or characteristic restriction.',project_dependencies=['MvPolynomial.taylor','MvPolynomial.coeff_taylor','MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt'],caller_summary='One explicit caller Roth.index_le_card Index229; full copied proof verified using fresh target replay.',mathlib_api_audit='Existing degreeOf_le_iff and degree bounds on sums/products do not prove the essential translated coefficient vanishing. Polynomial.natDegree_taylor is univariate; aeval_natDegree_le uses total degree and a univariate target.',moral_duplications='Univariate Taylor degree invariance is analogous but not direct replacement. Direct aeval spelling is definitionally equivalent.',generalization='Maximal within CommSemiring parent interface; CommRing equality via inverse is a separately verified stronger specialization, not assumption weakening.',missing_api='Coordinate-degree control under multivariate constant-shift substitution, with arbitrary variable type and commutative-semiring coefficients.',junk='Used by index/cardinality bound; not dead code. Short proof relies on genuine new Hasse/Taylor content.',action='Propose in Mathlib/Algebra/MvPolynomial/Taylor.lean with coefficient Taylor and Hasse degree/vanishing API; direct aeval statement if named translation is declined.',verdict='YES-add-as-is'))
