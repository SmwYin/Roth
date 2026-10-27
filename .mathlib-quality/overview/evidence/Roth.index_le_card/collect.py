from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).resolve().parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.index_le_card'
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
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[149]);assert order[149]['name']==N
cp(ROOT/'.mathlib-quality/overview/progress.json','progress-snapshot.json')
links={}
for p in ['Roth/Index.lean','Roth/Theta.lean','Roth/Taylor.lean','Roth/Box.lean']:
 n=p.replace('/','-')+'.txt';cp(ROOT/p,n);links[p]=n
put('source-links.json',links)
mi=[]
for p in ['Mathlib/Algebra/MonoidAlgebra/Degree.lean','Mathlib/Data/Finset/Lattice/Fold.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Data/Finsupp/Weight.lean','Mathlib/Order/ConditionallyCompleteLattice/Finset.lean']:
 f=ROOT/'.lake/packages/mathlib'/p;mi.append(dict(path=str(f.relative_to(ROOT)),sha256=sha(f),bytes=f.stat().st_size));cp(f,p.replace('/','-')+'.txt')
put('mathlib-inputs.json',mi)
for n,pat in [('current',r'index_le_card|degreeOf.*taylor|taylor.*degreeOf'),('literature',r'weightedOrder.*le|le_weightedTotalDegree|weightedTotalDegree.*le'),('abstract',r'infDegree|theorem inf_le|theorem inf._le')]:
 run('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('rg-inline.json',['rg','--no-ignore','-n',r'index_le_card|weight_le_card|degreeOf_taylor_le|Fintype.card.*index|index.*Fintype.card','Roth','Roth.lean'])
searches=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_le_card\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','index_le_card','--','Roth','Roth.lean'])]
inv=sorted({x['file'] for x in order});put('complete-caller-search.json',dict(canonical_source_inventory=inv,searches=searches));files=[]
for p in inv:
 f=ROOT/p;occ=[dict(line=i,kind='declaration' if p=='Roth/Index.lean' else 'body',text=t) for i,t in enumerate(f.read_text().splitlines(),1) if re.search(r'\bindex_le_card\b',t)];files.append(dict(path=p,sha256=sha(f),occurrences=occ))
put('lexical-enumeration.json',dict(files=files,applications=2,proof_body_applications=2,source_reference_lines=2,statement_applications=0))
put('callers.json',[dict(name='Roth.indexSet_bddAbove',visibility='public',file='Roth/Theta.lean',line=91,applications=1,kind='body',plan='Full replay calls IndexCardBridge150.noNonzero with mapped degree bound; nonzero map proof discarded.'),dict(name='Roth.Θ_le_card',visibility='public',file='Roth/Theta.lean',line=117,applications=1,kind='body',plan='Full replay calls IndexCardBridge150.noNonzero inside Real.sSup_le with original mapped degree bound; nonzero map proof discarded.')])
put('direct-consumers.json',dict(consumers=['Roth.indexSet_bddAbove','Roth.Θ_le_card'],scope='293 canonical kernel values; two direct target consumers and two source proof applications'))
run('local-literature-search.json',['rg','-n',r'ind\(|Index|index|Taylor|weight at most|at most.*m','.mathlib-quality/references/clean.tex'])
lines=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-index-excerpt.tex.txt').write_text('\n'.join(lines[529:680])+'\n')
for p in Path('/private/tmp/roth-overview').glob('index-card-*'):
 if p.is_file() and p.suffix in ['.txt','.json']:cp(p)
put('literature-summary.json',dict(chatgpt_math='n/a: ask_chatgpt_math unavailable',concept='A weighted order of vanishing of a nonzero polynomial is at most its coordinate degree box normalized width, hence at most number of variables when each degree bound equals the denominator.',standard='Taylor support has a nonzero coefficient whose exponent in coordinate j is at most degree_j(P). For positive weights each quotient is at most1. Literature uses +infinity at zero; project instead uses real0 at zero, enabling its noNonzero weakening.',limits='nCatLab explicit namespace search had no exact hit; nLab direct XHTML unsupported400. Recent arXiv query contained false Roth-name and additive-combinatorics matches, rejected. No negative search is an absence proof.'))
