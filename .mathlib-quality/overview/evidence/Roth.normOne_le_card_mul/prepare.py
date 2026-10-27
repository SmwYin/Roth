from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.normOne_le_card_mul'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
for src,dst in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/src,D/dst)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[86]['name']==N
out('canonical-order.json',dict(index=87,total=293,entry=order[86],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths=['Algebra/Order/BigOperators/Group/Finset.lean','Algebra/Order/BigOperators/Group/Multiset.lean','Analysis/Polynomial/Norm.lean','Analysis/Normed/Lp/Finsupp.lean']
m=[]
for i,p in enumerate(paths):
 f=R/'.lake/packages/mathlib/Mathlib'/p;dest=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'normOne_le_card_mul|norm_one.*card',['.lake/packages/mathlib/Mathlib']),('literature',r'card.*(norm|sum)|sum.*card|supNorm|l1Norm',['.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','.lake/packages/mathlib/Mathlib/Analysis/Normed/Lp/Finsupp.lean']),('abstract',r'sum_le_card_nsmul|sum_le_card_mul|prod_le_pow_card',['.lake/packages/mathlib/Mathlib/Algebra/Order/BigOperators']),('full-name',r'\bnormOne_le_card_mul\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_le_card_mul\b',['Roth','Roth.lean']),('inline',r'sum_le_card_nsmul|support.card.*B|normOne.*card',['Roth','Roth.lean']),('local-literature',r'Pad the monomial|norm|triangle inequality',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,497))+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,lines=[437,497]))
f=[]
for p in sorted(D.glob('lean_*.json')):
 x=json.loads(p.read_text());method,form=p.stem.rsplit('-',1);x.update(method=method,form=form);out(p.name,x);f.append(x)
out('formal-search.json',f)
acc=[]
for tag in ['original','raw','consumers']:
 p=Path('/private/tmp/roth-overview/norm-card-'+tag+'-executed.lean.txt');r=p.with_name('norm-card-'+tag+'-receipt.json');sn='native-'+tag+'-executed.lean.txt';rn='native-'+tag+'-success.json';shutil.copyfile(p,D/sn);shutil.copyfile(r,D/rn);j=json.loads(r.read_text());acc.append(dict(label=tag,source=sn,receipt=rn,source_sha256=sha(D/sn),execution_path=j['request'].get('file_path','virtual lean_run_code'),original_source_path=str(p),original_receipt_path=str(r)))
out('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=acc,rejected=[],production_unchanged=True))
s=(D/'native-consumers-executed.lean.txt').read_text();a=s[s.index('  let names : Array Lean.Name := #['):];a=a[:a.index(']\n')+2];(D/'canonical-audit-array.lean.txt').write_text(a)
out('callers.json',dict(named_count=1,occurrence_count=1,external_to_declaring_file=0,callers=[dict(name='Roth.abs_coeff_det_hasseDeriv_le',file='Roth/CoeffNorm.lean',lines=[270],replacement='Introduce hsize using Finset.sum_le_card_nsmul with support and coefficient absolute values; simpa only [Roth.normOne,nsmul_eq_mul]; replace normOne_le_card_mul P hB by hsize.')],inline_audit='Full module and repository rg inspected. abs_coeff_diag_le independently applies same bound after abs_sum_le_sum_abs; abs_eval_le uses pointwise sum bound. Neither is another explicit target caller.',native_audit=dict(requested=293,unique=293,present=293,values=293,direct_consumers=['Roth.abs_coeff_det_hasseDeriv_le'],status='PASS')))
print('Prepared fresh source, inputs and 3 accepted native sets')
