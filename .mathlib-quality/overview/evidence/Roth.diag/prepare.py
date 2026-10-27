from pathlib import Path
import hashlib,json,subprocess,shutil
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
def out(n,x): (D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n,pat,paths in [
('current',r'\bdiag\b|diagonal.*substitut|substitut.*diagonal',['.lake/packages/mathlib/Mathlib']),
('literature',r'uniqueAlgEquiv|eval₂_const_uniqueAlgEquiv|rename_eq_aeval',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
('abstract',r'def aeval|theorem comp_aeval|lemma comp_aeval_apply|def eval₂Hom|theorem aeval_unique',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
('full-name',r'\bdiag\b',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/RingTheory/MvPolynomial']),
('callers',r'\bdiag\b',['Roth','Roth.lean']),
('inline',r'aeval.*fun.*Polynomial.X|eval₂.*fun.*Polynomial.X|rename.*PUnit|uniqueAlgEquiv',['Roth','Roth.lean']),
('local-literature',r'same variable|diagonal substitution|resulting polynomial',['.mathlib-quality/references/clean.tex'])]:
 args=['rg','-n',pat,*paths];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+n+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,x in base['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=x['sha256'],match=sha(f)==x['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=base['baseline_commit']))
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
sources={'source-module.lean.txt':'Roth/CoeffNorm.lean','source-callers.lean.txt':'Roth/MainLemma.lean','mathlib-eval.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean','mathlib-equiv.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Equiv.lean','mathlib-rename.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Rename.lean'}
mi=[]
for dest,path in sources.items():
 f=R/path;shutil.copyfile(f,D/dest);mi.append(dict(path=path,sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('source-inputs.json',mi)
f=R/'.mathlib-quality/references/clean.tex';ls=f.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {ls[i]}' for i in list(range(1442,1458))+list(range(1498,1513)))+'\n');out('local-literature-source.json',dict(path=str(f.relative_to(R)),sha256=sha(f),lines=[[1443,1458],[1499,1513]]))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']=='Roth.diag'))
formal=[]
for method,prefix in [('Finder','finder'),('Loogle','loogle'),('LeanSearch','search'),('Local','local')]:
 for form,tag in [('current','current'),('literature','standard'),('abstract','abstract')]:formal.append(dict(method=method,form=form,**json.loads((D/(prefix+'-'+tag+'.json')).read_text())))
out('formal-search.json',formal)
callers=[
('CoeffNorm','diag_eq_sum',164,168,'Replace diag P by aeval-to-X; remove rw[diag] and retain aeval_def/eval₂_eq and monomial collection. Full general semiring raw proof verified.'),
('CoeffNorm','abs_coeff_diag_le',174,179,'Substitute aeval-to-X in conclusion; use replayed expansion instead of diag_eq_sum; finite coefficient sum and absolute-value proof unchanged.'),
('CoeffNorm','natDegree_diag_le',183,189,'Substitute aeval-to-X in conclusion; use replayed expansion, natDegree_sum_le and monomial degree bound. Keep inequality; cancellation prevents general equality.'),
('CoeffNorm','eval_diag',193,196,'Replace diag P in statement and unfolding simp; existing comp_aeval_apply plus Polynomial.aeval_X supplies general algebra-target evaluation rather than polynomial induction.'),
('CoeffNorm','diag_sub',199,200,'Replace all three occurrences with aeval-to-X; map_sub _ _ _ is already exact. Full scratch subtraction proof verified.'),
('MainLemma','exists_ne_modByMonic_eq',359,383,'Replace every diag in remainder-bound hypothesis, conclusion, and finite encoding F by aeval-to-X; output polynomial is definitionally unchanged, finite pigeonhole/remainder reconstruction untouched.'),
('MainLemma','eval_hasseDeriv_sub_eq_zero',402,412,'Replace both remainder-hypothesis expressions and intermediate divisibility; use generic map_sub, unfold aeval-to-X, then comp_aeval_apply and aeval_X. Full actual proof replayed natively.'),
('MainLemma','abs_coeff_diag_hasseDeriv_modByMonic_le_aux',497,513,'Replace diag in conclusion and hcD coefficient bound. Invoke rewritten coefficient and degree bounds; remainder estimate/arithmetic unchanged.'),
('MainLemma','abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux',515,547,'Replace diag in conclusion, local bound, and hreal; use previous rewritten auxiliary, same monic/nonmonic/degree-zero cases and floor arithmetic.'),
('MainLemma','exists_mem_RSet_le_index_aux',549,570,'Replace diag in hC; invoke rewritten pigeonhole and vanishing statements; final index membership conclusion unchanged.'),
('MainLemma','exists_mem_RSet_le_index_of_rpow_bound_aux',583,619,'Replace diag in local hC; rewritten floor estimate gives same bound; final membership/index conclusion unchanged.')]
out('callers.json',dict(named_count=11,external_to_declaring_file=6,scope='Distinct production declarations with exact whole-word diag in signature/body; excludes definition/docstrings; not kernel/simp dependency closure.',callers=[dict(name='Roth.'+n,file='Roth/'+m+'.lean',line=a,end_line=b,refactor=p) for m,n,a,b,p in callers],inline_audit='No second aeval-to-Polynomial.X definition in production sources; univariate/uniqueAlgEquiv in HasseDeriv is single-variable coefficient/Hasse transport, not arbitrary variable collapse.'))
out('generality.json',dict(status='STRICTLY NARROWER THAN STANDARD',verified=['CommSemiring R coefficients with arbitrary independently universe-polymorphic σ','Exact original ℤ specialization by rfl','generic algebra target evaluation naturality','eval₂Hom Polynomial.C representation by rfl','rename to PUnit followed by uniqueAlgEquiv equals bundled aeval, proved not defeq'],not_claimed=['injectivity for arbitrary variable types','degree equality','noncommutative coefficient generality','completed new global instance or novel universal-property construction'],cost='CHEAP; same aeval body. Existing aeval already provides the more general construction.'))
print('Prepared source, 17-hash, formal-search and eleven-caller records.')
