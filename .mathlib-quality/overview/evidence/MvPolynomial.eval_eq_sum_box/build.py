from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='MvPolynomial.eval_eq_sum_box'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for label,pat,paths in [
 ('current',r'eval_eq_sum_box|eval.*taylor|taylor.*eval',['.lake/packages/mathlib/Mathlib/Algebra']),
 ('literature',r'Hasse|hasseDeriv|sum_taylor_eq|coeff.*taylor',['.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
 ('abstract',r'eval₂_eq|eval_eq|aeval_sum|aeval_prod|aeval_C|aeval_X',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean']),
 ('full-name',r'MvPolynomial\.eval_eq_sum_box|\b(theorem|lemma)\s+eval_eq_sum_box\b',['.lake/packages/mathlib/Mathlib']),
 ('callers',r'\beval_eq_sum_box\b',['Roth.lean','Roth']),
 ('inline',r'eval_eq_sum_box|sum.*hasseDeriv|hasseDeriv.*sum|\bbox r\b',['Roth.lean','Roth']),
 ('local-literature',r'Taylor|Hasse|expansion|Q\(h_1/q_1',['.mathlib-quality/references/clean.tex'])]:
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
sources={'Roth/Taylor.lean':'Taylor-module.lean.txt','Roth/Box.lean':'Box-module.lean.txt','Roth/HasseDeriv.lean':'HasseDeriv-module.lean.txt','Roth/Main.lean':'Main-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean':'MvPolynomial-Eval-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean':'MvPolynomial-Basic-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean':'Polynomial-Taylor-module.lean.txt'}
mi=[]
for p,n in sources.items():
 shutil.copy(R/p,D/n)
 if p.startswith('.lake'):mi.append(dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size))
out('mathlib-inputs.json',mi)
clean=R/'.mathlib-quality/references/clean.tex';out('local-literature.json',dict(path=str(clean.relative_to(R)),sha256=sha(clean),locators=['Section4 Index, lines500–529','Section7 Taylor upper bound, lines1655–1673'],summary='Exact real multivariate Taylor expansion; substitution at rational approximants feeds strict upper estimate. Ring/Hasse formulation avoids factorial invertibility.'))
ss=clean.read_text().splitlines();(D/'clean-excerpts.tex.txt').write_text('\n'.join(ss[499:529]+ss[1654:1673])+'\n')
out('callers.json',dict(named_count=1,external_to_declaring_file=1,distinct_files=1,callers=[dict(declaration='Roth.abs_eval_lt_of_le_index',file='Roth/Main.lean',line=390,proof='rw [eval_eq_sum_box (fun _ ↦ α) (fun j ↦ (h j : ℝ) / q j) r Q hd]',migration='Use fresh verified evaluation theorem/recovery; full strict upper-bound proof and its private product-weight helper validated.')],inline_audit='All production sources searched; no independent rederivation of complete evaluated Hasse box identity. Generic coefficient evaluation sums and analytic term bounds are different statements. Explicit named callers only, not opaque kernel/simp closure.'))
out('proof-body-diagnostic.json',dict(named_objects=['eval','eq_sum_box_hasseDeriv'],proof_lines=1,occurrences={'eval':1,'eq_sum_box_hasseDeriv':1},diagnostic='Concrete-via-abstract fires: apply evaluation homomorphism to project polynomial expansion, then distribute through sums/products/constants. Generic finite-expansion transport is abstract, but the premise polynomial Hasse expansion is a substantive project theorem absent from pinned mathlib, not an existing building block. Arbitrary algebra target tested for real modernisation.',false_generalization='A hypothesis asserting the desired polynomial expansion is not a replacement proof of Taylor. Divided power algebras change multiplication. Noncommutative targets require commuting images/central coefficients, not unrestricted aeval. Natural exponents and finite box retain their meaning.'))
args=['git','-C','.lake/packages/mathlib','log','-6','--format=%h %an %s','--','Mathlib/Algebra/MvPolynomial/Eval.lean','Mathlib/Algebra/MvPolynomial/Basic.lean','Mathlib/Algebra/Polynomial/Taylor.lean'];r=subprocess.run(args,cwd=R,capture_output=True);out('reviewer-history.json',dict(args=args,exit_code=r.returncode,stdout=r.stdout.decode(),stderr=r.stderr.decode(),contacted=False))
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());names=['MvPolynomial.hasseDeriv','MvPolynomial.coeff_hasseDeriv','MvPolynomial.coeff_taylor','MvPolynomial.eq_sum_box_hasseDeriv']
group=[x for x in progress['completed_declarations'] if x['declaration'] in names];assert len(group)==4 and all(x['verdict'].startswith('YES') for x in group);out('proposed-pr-group.json',group)
