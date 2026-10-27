from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='MvPolynomial.eq_sum_box_hasseDeriv'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for label,pat,paths in [
 ('current',r'eq_sum_box_hasseDeriv|sum.*taylor|taylor.*sum',['.lake/packages/mathlib/Mathlib/Algebra']),
 ('literature',r'Hasse|hasseDeriv|sum_taylor_eq|coeff.*taylor',['.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
 ('abstract',r'eval₂_eq|sum_monomial_eq|sum_monomial|comp_aeval|aeval_X_left',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
 ('full-name',r'MvPolynomial\.eq_sum_box_hasseDeriv|\b(theorem|lemma)\s+eq_sum_box_hasseDeriv\b',['.lake/packages/mathlib/Mathlib']),
 ('callers',r'\beq_sum_box_hasseDeriv\b',['Roth.lean','Roth']),
 ('inline',r'eval_eq_sum_box|sum.*hasseDeriv|hasseDeriv.*sum|Roth.box|\bbox r\b',['Roth.lean','Roth']),
 ('local-literature',r'Taylor|Hasse|expansion',['.mathlib-quality/references/clean.tex'])]:
 args=['rg','-n',pat,*paths];r=subprocess.run(args,cwd=R,capture_output=True);out('rg-'+label+'.json',dict(args=args,exit_code=r.returncode,stdout=r.stdout.decode(),stderr=r.stderr.decode()))
m=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());items=[]
for p,x in m['sources_and_pins'].items():
 f=R/p;items.append(dict(path=p,sha256=sha(f),baseline_sha256=x['sha256'],bytes=f.stat().st_size,match=sha(f)==x['sha256']))
assert len(items)==17 and all(x['match'] for x in items)
out('inputs.json',items);out('input-hash-check.json',dict(all_pass=True,count=17))
shutil.copy(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
entries=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());out('canonical-entry.json',next(x for x in entries if x['name']==N))
entries=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());entries=entries.get('declarations',entries.get('order',[])) if isinstance(entries,dict) else entries
out('order-entry.json',next(x for x in entries if x['name']==N))
sources={'Roth/Taylor.lean':'Taylor-module.lean.txt','Roth/Box.lean':'Box-module.lean.txt','Roth/HasseDeriv.lean':'HasseDeriv-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean':'MvPolynomial-Eval-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean':'MvPolynomial-Basic-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean':'Polynomial-Taylor-module.lean.txt','.lake/packages/mathlib/Mathlib/Data/Finsupp/Interval.lean':'Finsupp-Interval-module.lean.txt'}
mi=[]
for p,n in sources.items():
 shutil.copy(R/p,D/n)
 if p.startswith('.lake'):mi.append(dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size))
out('mathlib-inputs.json',mi)
clean=R/'.mathlib-quality/references/clean.tex';out('local-literature.json',dict(path=str(clean.relative_to(R)),sha256=sha(clean),locator='Section4 Index, lines500–529',summary='Real-coefficient coordinatewise bounded Taylor expansion; proof by linearity and one-variable binomial expansion. Ring/Hasse formulation removes field/characteristic/factorial restrictions.'))
(D/'clean-excerpts.tex.txt').write_text('\n'.join(clean.read_text().splitlines()[499:529])+'\n')
out('callers.json',dict(named_count=1,external_to_declaring_file=0,callers=[dict(declaration='MvPolynomial.eval_eq_sum_box',file='Roth/Taylor.lean',line=220,proof='simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)',migration='Use verified weaker scoped-Classical theorem, recovering arbitrary old DecidableEq formulation as necessary; full caller replay required.')],inline_audit='Search all production sources; evaluated expansion is direct corollary, downstream eval_eq_sum_box consumers are transitive rather than additional direct named callers. Coefficient formula and monomial reconstruction are related lemmas, not duplicate full bounded expansion.'))
out('proof-body-diagnostic.json',dict(named_objects=['taylor','hasseDeriv','Roth.box'],occurrences={'taylor':3,'hasseDeriv':1,'Roth.box':1},diagnostic='The proof first reconstructs translated coefficients on an arbitrary finite box and then uses inverse translation. An abstract reconstruction principle captures the transport step, but identifying coefficients as Hasse derivatives and showing all off-box coefficients vanish are substantive project facts. Generic aeval/eval₂ reconstruction does not supply these facts.',false_generalization='Replacing natural exponents by arbitrary monoid changes polynomial/Hasse meaning; dropping Fintype while retaining full product/box is not well-formed. Support-indexed representation would be a different API, not an unchanged same-statement weakening.'))
args=['git','-C','.lake/packages/mathlib','log','-6','--format=%h %an %s','--','Mathlib/Algebra/MvPolynomial/Eval.lean','Mathlib/Algebra/MvPolynomial/Basic.lean','Mathlib/Algebra/Polynomial/Taylor.lean'];r=subprocess.run(args,cwd=R,capture_output=True);out('reviewer-history.json',dict(args=args,exit_code=r.returncode,stdout=r.stdout.decode(),stderr=r.stderr.decode(),contacted=False))
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());names=['MvPolynomial.hasseDeriv','MvPolynomial.coeff_hasseDeriv','MvPolynomial.coeff_taylor','MvPolynomial.degreeOf_taylor_le']
group=[x for x in progress['completed_declarations'] if x['declaration'] in names];assert len(group)==4 and all(x['verdict'].startswith('YES') for x in group);out('proposed-pr-group.json',group)
