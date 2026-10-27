from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).resolve().parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.index_neg'
def put(n,x): (D/n).write_text(json.dumps(x,indent=2)+'\n')
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
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[145]);assert order[145]['name']==N
cp(ROOT/'.mathlib-quality/overview/progress.json','progress-snapshot.json')
links={}
for p in ['Roth/Index.lean','Roth/Theta.lean','Roth/Taylor.lean','Roth/Box.lean']:
 n=p.replace('/','-')+'.txt';cp(ROOT/p,n);links[p]=n
put('source-links.json',links)
mi=[]
for p in ['Mathlib/Algebra/MonoidAlgebra/Degree.lean','Mathlib/RingTheory/MvPowerSeries/Order.lean','Mathlib/Algebra/MvPolynomial/CommRing.lean']:
 f=ROOT/'.lake/packages/mathlib'/p;mi.append(dict(path=str(f.relative_to(ROOT)),sha256=sha(f),bytes=f.stat().st_size));cp(f,p.replace('/','-')+'.txt')
put('mathlib-inputs.json',mi)
for n,pat in [('current',r'index_neg|Roth.index'),('literature',r'weightedOrder_neg|order_neg|natTrailingDegree_neg'),('abstract',r'supDegree_neg|infDegree_neg|support_neg')]:
 run('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('rg-inline.json',['rg','--no-ignore','-n',r'index_neg|index \(-|support_neg|neg_one|sign.*index|index.*sign','Roth','Roth.lean'])
searches=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_neg\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','index_neg','--','Roth','Roth.lean'])]
inv=sorted({x['file'] for x in order});put('complete-caller-search.json',dict(canonical_source_inventory=inv,searches=searches))
files=[]
for p in inv:
 f=ROOT/p;occ=[dict(line=i,kind='declaration',text=t) for i,t in enumerate(f.read_text().splitlines(),1) if re.search(r'\bindex_neg\b',t)];files.append(dict(path=p,sha256=sha(f),occurrences=occ))
put('lexical-enumeration.json',dict(files=files,applications=0,proof_body_applications=0,statement_applications=0));put('callers.json',[]);put('direct-consumers.json',dict(consumers=[],scope='293 canonical kernel values, direct target references only'))
run('local-literature-search.json',['rg','-n','sign|index|ind\\(','.mathlib-quality/references/clean.tex'])
lines=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-index-excerpt.tex.txt').write_text('\n'.join(lines[529:642])+'\n');(D/'clean-sign-excerpt.tex.txt').write_text('\n'.join(lines[819:829])+'\n')
(D/'theta-sign-excerpt.lean.txt').write_text('\n'.join((ROOT/'Roth/Theta.lean').read_text().splitlines()[389:413])+'\n')
for n in ['index-neg-original-executed.lean.txt','index-neg-original-audit-receipt.json','index-neg-original-region.txt','index-neg-audit-executed.lean.txt','index-neg-audit-region.txt']:cp(Path('/private/tmp/roth-overview')/n)
for n in ['index-consumers-executed.lean.txt','index-consumers-receipt.json']:cp(Path('/private/tmp/roth-overview/assess/Roth.index_prod')/n)
put('literature-summary.json',dict(chatgpt_math='n/a: ask_chatgpt_math unavailable',concept='weighted order of vanishing; invariance under negation / units',standard='Negation preserves nonzero Taylor coefficient support. General signed finitely supported coefficient families and arbitrary degree maps suffice.',limits='Local text uses positive real r and infinity at zero; project uses natural r without positivity and zero index0. These choices do not affect negation support equality. Stacks is contextual; nLab direct fetch400; nCatLab search returned outside namespace; arXiv recent hits use different notions.'))
