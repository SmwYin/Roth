from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.normOne_mul_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
shutil.copyfile(R/'Roth/CoeffNorm.lean',D/'source-module.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[84]['name']==N
out('canonical-order.json',dict(index=85,total=len(order),entry=order[84],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths={'mathlib-finset-order.lean.txt':'Algebra/Order/BigOperators/Group/Finset.lean','mathlib-finsupp-basic.lean.txt':'Algebra/BigOperators/Finsupp/Basic.lean','mathlib-lp-finsupp.lean.txt':'Analysis/Normed/Lp/Finsupp.lean','mathlib-norm.lean.txt':'Analysis/Polynomial/Norm.lean','mathlib-norm-ring.lean.txt':'Analysis/Normed/Ring/Basic.lean','mathlib-monoid-algebra.lean.txt':'Algebra/MonoidAlgebra/Defs.lean','mathlib-mvpolynomial.lean.txt':'Algebra/MvPolynomial/Basic.lean'}
m=[]
for dest,p in paths.items():
 f=R/'.lake/packages/mathlib/Mathlib'/p;shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'normOne_mul_le|norm_one_mul',['.lake/packages/mathlib/Mathlib']),('literature',r'norm_mul|convol|sum.*norm|norm.*sum',['.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','.lake/packages/mathlib/Mathlib/Analysis/Normed/Lp/Finsupp.lean','.lake/packages/mathlib/Mathlib/Analysis/Normed/Ring/Basic.lean']),('abstract',r'le_prod.*submultiplicative|mul_def|sum.*mul|mul.*sum',['.lake/packages/mathlib/Mathlib/Algebra/Order/BigOperators/Group/Finset.lean','.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Defs.lean']),('full-name',r'\bnormOne_mul_le\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_mul_le\b',['Roth','Roth.lean']),('inline',r'normOne.*\*|\*.*normOne|submultiplicative',['Roth','Roth.lean']),('local-literature',r'submultiplicativity|triangle inequality|\\ell|norm',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,497))+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,lines=[437,497]))
out('formal-search.json',[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))])
accepted=[]
for label,tag in [('original','original'),('raw','raw-clean'),('consumers','consumers')]:
 p=Path('/private/tmp/roth-overview/norm-mul-'+tag+'-executed.lean.txt');r=Path('/private/tmp/roth-overview/norm-mul-'+tag+'-receipt.json')
 sn='native-'+label+'-executed.lean.txt';rn='native-'+label+'-success.json';shutil.copyfile(p,D/sn);shutil.copyfile(r,D/rn)
 j=json.loads(r.read_text());accepted.append(dict(label=label,source=sn,source_sha256=sha(D/sn),receipt=rn,execution_path=j['request'].get('file_path','virtual lean_run_code'),original_source_path=str(p),original_receipt_path=str(r)))
rejected=[]
for label in ['raw']:
 p=Path('/private/tmp/roth-overview/norm-mul-'+label+'-executed.lean.txt');r=Path('/private/tmp/roth-overview/norm-mul-'+label+'-receipt.json');sn='rejected-'+label+'-executed.lean.txt';rn='rejected-'+label+'-receipt.json';shutil.copyfile(p,D/sn);shutil.copyfile(r,D/rn);rejected.append(dict(source=sn,receipt=rn,reason='Triangle rw did not match polynomial coefficient addition after unfold; rejected recovered sorryAx. Accepted clean source explicitly changes to P.coeff+Q.coeff.'))
out('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,production_unchanged=True))
s=(D/'native-consumers-executed.lean.txt').read_text();a=s[s.index('  let names : Array Lean.Name := #['):];a=a[:a.index(']\n')+2];(D/'canonical-audit-array.lean.txt').write_text(a)
# Retain initial requests as preparation, wrap only the unexecuted long lines.
p=D/'requested-consumers.lean.txt';s=p.read_text().replace('Lean.mkPrivateNameCore `Roth.Arithmetic.PrimaryOnSecondary `specializePrimary_fiberCardSumFactorBound_privateAux,','Lean.mkPrivateNameCore `Roth.Arithmetic.PrimaryOnSecondary\n      `specializePrimary_fiberCardSumFactorBound_privateAux,');s=s.replace('  Lean.logInfo m!"MUL_AUDIT_CANONICAL: requested={names.size}; present={present}; values={withValue}"','  Lean.logInfo m!"MUL_AUDIT_CANONICAL: requested={names.size}; present={present}; values={withValue}"');p.write_text(s)
out('callers.json',dict(named_count=1,occurrence_count=1,external_to_declaring_file=0,callers=[dict(name='Roth.normOne_prod_le',file='Roth/CoeffNorm.lean',lines=[108],replacement='Full multiplication expansion proof substituted for binary hypothesis; see accepted caller replay.')],inline_audit='Read all CoeffNorm and fresh rg across Roth: no separate source binary rederivation. Module doc and declaration are not callers.',native_audit=dict(requested=293,unique=293,present=293,values=293,direct_consumers=['Roth.normOne_prod_le'],status='PASS')))
print('Prepared fresh baseline, sources, searches and native evidence.')
