from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).resolve().parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.index_rename'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cp(p,n=None):shutil.copyfile(p,D/(n or Path(p).name))
def run(n,cmd):
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);x=dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr);put(n,x);return x
base=ROOT/'.mathlib-quality/overview/evidence/shared'
for n in ['input-manifest.json','baseline-build.txt']:cp(base/n)
m=json.loads((base/'input-manifest.json').read_text());inputs=[]
for p,e in m['sources_and_pins'].items():
 f=ROOT/p;inputs.append(dict(path=p,sha256=sha(f),expected_sha256=e['sha256'],bytes=f.stat().st_size,match=sha(f)==e['sha256']))
assert len(inputs)==17 and all(x['match'] for x in inputs);put('inputs.json',inputs)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[148]);assert order[148]['name']==N
cp(ROOT/'.mathlib-quality/overview/progress.json','progress-snapshot.json')
links={}
for p in ['Roth/Index.lean','Roth/Theta.lean','Roth/Taylor.lean','Roth/Box.lean']:
 n=p.replace('/','-')+'.txt';cp(ROOT/p,n);links[p]=n
put('source-links.json',links)
mi=[]
for p in ['Mathlib/Algebra/MonoidAlgebra/Degree.lean','Mathlib/Data/Finset/Lattice/Fold.lean','Mathlib/Algebra/MvPolynomial/Rename.lean','Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean','Mathlib/Data/Finsupp/Weight.lean','Mathlib/Order/ConditionallyCompleteLattice/Finset.lean']:
 f=ROOT/'.lake/packages/mathlib'/p;mi.append(dict(path=str(f.relative_to(ROOT)),sha256=sha(f),bytes=f.stat().st_size));cp(f,p.replace('/','-')+'.txt')
put('mathlib-inputs.json',mi)
for n,pat in [('current',r'index_rename|support_rename_of_injective|taylor_rename'),('literature',r'weightedOrder.*rename|weightedTotalDegree.*rename|linearCombination_mapDomain|weight.*mapDomain'),('abstract',r'inf_image|infDegree|mapDomain_support_of_injective')]:
 run('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('rg-inline.json',['rg','--no-ignore','-n',r'index_rename|support_rename_of_injective|taylor_rename|weight_mapDomain','Roth','Roth.lean'])
searches=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_rename\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','index_rename','--','Roth','Roth.lean'])]
inv=sorted({x['file'] for x in order});put('complete-caller-search.json',dict(canonical_source_inventory=inv,searches=searches))
files=[]
for p in inv:
 f=ROOT/p;occ=[dict(line=i,kind='declaration' if p=='Roth/Index.lean' else 'body',text=t) for i,t in enumerate(f.read_text().splitlines(),1) if re.search(r'\bindex_rename\b',t)];files.append(dict(path=p,sha256=sha(f),occurrences=occ))
put('lexical-enumeration.json',dict(files=files,applications=3,proof_body_applications=3,source_reference_lines=2,statement_applications=0))

put('callers.json', [dict(name='Roth.indexSet_comp_subset',visibility='private',file='Roth/Theta.lean',line=154,applications=1,kind='body',plan='Full replay replaces index_rename e.injective in simp with IndexRenameBridge149.replacement e.injective. With re-aimed index use finite-support image law after coefficient map and translation naturality.'),dict(name='Roth.index_separated_mul_le_aux',visibility='private',file='Roth/Theta.lean',line=442,applications=2,kind='body',plan='Full replay replaces both index_rename applications inside rw with independently verified bridge, keeping Option.some injection and Unit-to-none injection. After parent migration use Finset.inf_image on the two translated supports.')])
put('direct-consumers.json',dict(consumers=['Roth.indexSet_comp_subset','Roth.index_separated_mul_le_aux'],scope='293 canonical kernel values; two direct target consumers, three explicit source applications'))
run('local-literature-search.json',['rg','-n',r'embed|renam|ind\(|Index|index|Lemma 4-2','.mathlib-quality/references/clean.tex'])
lines=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-index-excerpt.tex.txt').write_text('\n'.join(lines[529:642])+'\n')
for p in Path('/private/tmp/roth-overview').glob('index-rename-*'):
 if p.is_file() and p.suffix in ['.txt','.json']:cp(p)
put('literature-summary.json',dict(chatgpt_math='n/a: ask_chatgpt_math unavailable',concept='Weighted order of vanishing invariant under injective variable relabeling or adjoining unused variables.',standard='Minimum additive weight of Taylor support. Under injective variable map, support is image of exponent map and weights pull back. Valid over arbitrary coefficient commutative semiring in expanded finite-support representation; current parent index fixes real coefficients and finite variable types.',limits='nCatLab query returned only nLab out-of-namespace pages; no exact namespace hit. Acta1996 and Princeton PDF direct fetches timed out400; their search snippets are marked as such. Recent Salami2026 section8 concerns a distinct auxiliary-polynomial construction counterexample. Search limitations do not prove absence.'))
