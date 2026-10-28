from pathlib import Path
import hashlib,json,subprocess,re,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.pow_rootMultiplicity_le'
def save(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,args):
 r=subprocess.run(args,cwd=R,text=True,capture_output=True);save(n,dict(request=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));return r.stdout
for p in Path('/private/tmp/roth-overview').glob('root-bound197-*'):
 if p.is_file():shutil.copy2(p,D/p.name)
shutil.copy2(R/'Roth/Theta.lean',D/'source-Theta.lean.txt')
base=R/'.mathlib-quality/overview/evidence/shared'
for n in ['input-manifest.json','baseline-build.txt']:shutil.copy2(base/n,D/n)
b=json.loads((D/'input-manifest.json').read_text())['sources_and_pins']
save('source-hashes.json',[dict(source=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,matches_baseline=sha(R/p)==b[p]['sha256']) for p in b])
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());save('canonical-snapshot.json',order);save('canonical-target.json',order[196])
run('callers.json',['rg','--no-ignore','-n','pow_rootMultiplicity_le','Roth','Roth.lean'])
run('git-callers.json',['git','grep','-n','pow_rootMultiplicity_le','--','Roth','Roth.lean'])
lex=[]
for item in order:
 p=R/item['file'];lines=p.read_text().splitlines();start=item['line']-1
 nexts=[x['line']-1 for x in order if x['file']==item['file'] and x['line']>item['line']]
 stop=min(nexts) if nexts else len(lines)
 if item['name']!=N and any('pow_rootMultiplicity_le' in s for s in lines[start:stop]):lex.append(item)
save('lexical-enumeration.json',dict(canonical_entries=len(order),callers=lex))
save('callers-structured.json',[dict(declaration=lex[0]['name'],file='Roth/Theta.lean',line=245,excerpt=(R/'Roth/Theta.lean').read_text().splitlines()[244])])
for form,pat in [('current','rootMultiplicity.*(leadingCoeff|≤)|pow_rootMultiplicity|pow_rootMultiplicity_le'),('standard','den_dvd_of_is_root|rational.root|den.*rootMultiplicity|rootMultiplicity.*den'),('abstract','leadingCoeff_dvd_leadingCoeff|dvd_of_fraction_map_dvd_fraction_map|IsRelPrime.*rootMultiplicity|rootMultiplicity.*IsRelPrime')]:
 run('rg-'+form+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('inline-audit.json',['rg','--no-ignore','-n','leadingCoeff|rootMultiplicity|Int.one_le_abs','Roth','Roth.lean'])
paths=['Mathlib/Algebra/Polynomial/Div.lean','Mathlib/Algebra/Polynomial/Degree/Operations.lean','Mathlib/Algebra/Polynomial/Degree/SmallDegree.lean','Mathlib/Algebra/Polynomial/DenomsClearable.lean','Mathlib/RingTheory/Polynomial/GaussLemma.lean','Mathlib/RingTheory/Polynomial/RationalRoot.lean','Mathlib/Data/Int/Basic.lean','Mathlib/Algebra/Order/Ring/Abs.lean']
mi=[]
for p in paths:
 src=R/'.lake/packages/mathlib'/p;n='mathlib-'+p.replace('/','-')+'.txt';shutil.copy2(src,D/n);mi.append(dict(path=p,sha256=sha(src),bytes=src.stat().st_size,archive=n))
save('mathlib-inputs.json',mi)
p=R/'.mathlib-quality/references/clean.tex';ls=p.read_text().splitlines();(D/'clean-lemma5-excerpt.tex.txt').write_text('\n'.join(ls[675:699])+'\n');save('local-literature.json',dict(source=str(p.relative_to(R)),sha256=sha(p),locator='§5 Lemma5 proof, lines676–699',summary='Gauss factor descent followed by comparison of nonzero integer leading coefficients yields q^t ≤ B.'))
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text())
records=progress['completed_declarations'];save('accepted-grouping.json',dict(records=[x for x in records if x['declaration']=='Roth.exists_eq_pow_mul_of_rootMultiplicity' and x['verdict'].startswith('YES')]))
body='\n'.join((R/'Roth/Theta.lean').read_text().splitlines()[209:222]);save('concrete-abstract-diagnostic.json',dict(body=body,counts={t:sum(t in line for line in body.splitlines()) for t in ['ℤ','ℚ','ℝ','Int.','Nat.']},conclusion='Integer coefficient discreteness is essential to bound; algebraic GCD-domain divisibility can be separated. Generic ordered codomain does not require real analysis.'))
print('prepared')
