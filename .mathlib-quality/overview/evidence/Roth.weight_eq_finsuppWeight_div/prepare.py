from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).parent; R=Path('/Users/ramin/LEAN/Roth'); N='Roth.weight_eq_finsuppWeight_div'
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=R/'.mathlib-quality/overview/evidence/shared'
for n in ['input-manifest.json','baseline-build.txt']:shutil.copy(base/n,D/n)
inputs=[]
for p,x in json.loads((base/'input-manifest.json').read_text())['sources_and_pins'].items():
 f=R/p;inputs.append(dict(path=p,sha256=sha(f),expected_sha256=x['sha256'],match=sha(f)==x['sha256'],bytes=f.stat().st_size))
assert len(inputs)==17 and all(x['match'] for x in inputs)
dump('inputs.json',inputs)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-order.json',order)
dump('canonical-target.json',order[141]);shutil.copy('/private/tmp/roth-overview/review/corrected-manifest.json',D/'corrected-manifest.json')
links={}
for p in ['Roth/Index.lean','Roth/Box.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean','.lake/packages/mathlib/Mathlib/Data/Nat/Cast/Field.lean']:
 n=p.split('/')[-1]+'.txt';shutil.copy(R/p,D/n);links[p]=n
dump('source-links.json',links)
dump('mathlib-inputs.json',[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size) for p in links if p.startswith('.lake')])
for form,pat in [('current','weight_eq_finsuppWeight_div|cast_div_charZero|sum_div'),('literature','weightedTotalDegree|isWeightedHomogeneous_monomial|weight_eq_sum'),('abstract','apply_linearCombination|map_finsupp_linearCombination|linearCombination_linear_comp')]:
 cmd=['rg','--no-ignore','-n',pat,'.lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean','.lake/packages/mathlib/Mathlib/Data/Nat/Cast/Field.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPolynomial/WeightedHomogeneous.lean'];r=subprocess.run(cmd,cwd=R,text=True,capture_output=True);dump('rg-'+form+'.json',dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
searches=[]
for cmd in [['rg','--no-ignore','-n','weight_eq_finsuppWeight_div','Roth','Roth.lean'],['git','grep','-n','weight_eq_finsuppWeight_div','--','Roth','Roth.lean']]:
 r=subprocess.run(cmd,cwd=R,text=True,capture_output=True);searches.append(dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
inventory=sorted({x['file'] for x in order});dump('complete-caller-search.json',dict(searches=searches,canonical_source_inventory=inventory))
source=(R/'Roth/Index.lean').read_text();fragment='\n'.join(source.splitlines()[142:159]);dump('callers.json',[dict(name='Roth.index_eq_weightedOrder_div',file='Roth/Index.lean',line=143,reference_lines=[152,155],identifier_occurrences=2,source_sha256=sha(R/'Roth/Index.lean'),source_fragment=fragment,plan='Keep the weighted-order proof and replace both rewrites at 152 and 155 by the checked denominator-clearing bridge for the Finsupp reciprocal-weight representation. At 152 reverse the equality after ENat.toNat_natCast; at 155 use it forwards. Preserve hP, hr and the natural-to-real casts.')])
lex=[]
for p in inventory:
 s=(R/p).read_text();clean=re.sub(r'/\-.*?\-/|--[^\n]*',lambda m:'\n'*m[0].count('\n'),s,flags=re.S)
 occ=[dict(line=clean[:m.start()].count('\n')+1,kind='declaration' if 'theorem ' in clean[clean.rfind('\n',0,m.start())+1:m.start()] else 'proof-body application') for m in re.finditer(r'\bweight_eq_finsuppWeight_div\b',clean)]
 lex.append(dict(path=p,sha256=sha(R/p),occurrences=occ))
dump('lexical-enumeration.json',dict(files=lex,applications=2,proof_body_applications=2,statement_applications=0))
cmd=['rg','--no-ignore','-n','Nat.cast_div_charZero|∏ i, r i|finsuppWeight','Roth','Roth.lean'];r=subprocess.run(cmd,cwd=R,text=True,capture_output=True);dump('rg-inline.json',dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
(D/'clean-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:558])+'\n')
cmd=['rg','-n','natural weights|integral|D=|D =|weightedOrder|index',' .mathlib-quality/references/clean.tex'.strip()];r=subprocess.run(cmd,cwd=R,text=True,capture_output=True);dump('local-literature-search.json',dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
for n in ['Roth.weight','Roth.weight_mul_left','Roth.index']:
 shutil.copy(R/'.mathlib-quality/overview/mathlibable'/f'{n}.md',D/f'prior-{n}.md.txt')
