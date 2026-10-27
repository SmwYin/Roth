from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).resolve().parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.index_mul_left_weights'
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
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[147]);assert order[147]['name']==N
cp(ROOT/'.mathlib-quality/overview/progress.json','progress-snapshot.json')
links={}
for p in ['Roth/Index.lean','Roth/Theta.lean','Roth/Taylor.lean','Roth/Box.lean']:
 n=p.replace('/','-')+'.txt';cp(ROOT/p,n);links[p]=n
put('source-links.json',links)
mi=[]
for p in ['Mathlib/Algebra/MonoidAlgebra/Degree.lean','Mathlib/Data/Finset/Lattice/Fold.lean','Mathlib/Basic/Real/Pointwise.lean','Mathlib/Order/WithBot.lean','Mathlib/Order/ConditionallyCompleteLattice/Finset.lean']:
 f=ROOT/'.lake/packages/mathlib'/p;mi.append(dict(path=str(f.relative_to(ROOT)),sha256=sha(f),bytes=f.stat().st_size));cp(f,p.replace('/','-')+'.txt')
put('mathlib-inputs.json',mi)
for n,pat in [('current',r'index_mul_left_weights|sInf_smul_of_nonneg|image_smul'),('literature',r'weightedOrder.*(smul|mul)|weight.*(smul|mul)|sInf_smul_of_nonneg'),('abstract',r'map_finset_inf|apply_inf.*eq_inf.*comp|infDegree|monotone_map_iff|untopD.*map')]:
 run('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('rg-inline.json',['rg','--no-ignore','-n',r'index_mul_left_weights|sInf_smul|index.*fun j.*l|weight_mul_left','Roth','Roth.lean'])
searches=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_mul_left_weights\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','index_mul_left_weights','--','Roth','Roth.lean'])]
inv=sorted({x['file'] for x in order});put('complete-caller-search.json',dict(canonical_source_inventory=inv,searches=searches))
files=[]
for p in inv:
 f=ROOT/p;occ=[dict(line=i,kind='declaration' if p=='Roth/Index.lean' else 'body',text=t) for i,t in enumerate(f.read_text().splitlines(),1) if re.search(r'\bindex_mul_left_weights\b',t)];files.append(dict(path=p,sha256=sha(f),occurrences=occ))
put('lexical-enumeration.json',dict(files=files,applications=2,proof_body_applications=2,source_reference_lines=1,statement_applications=0))
put('callers.json',[dict(name='Roth.index_separated_mul_le_aux',visibility='private',file='Roth/Theta.lean',line=447,kind='body',applications=2,plan='Full replay uses IndexScale148.replacement in rw at hUΘ hVΘ. After infDegree re-aim use independently verified IndexScaleBridge148.replacement (same type). Keep hl>0 only for subsequent div_le_iff; scaling itself needs no positivity. If deleting wrapper, inline the verified local normalization proof at both hypotheses, not a false direct map_finset_inf rewrite.')]);put('direct-consumers.json',dict(consumers=['Roth.index_separated_mul_le_aux'],scope='293 canonical kernel values; sole direct target consumer; two source applications on one rw line'))
run('local-literature-search.json',['rg','-n',r'ind\(P.*|scal|index|l r|ell r','.mathlib-quality/references/clean.tex'])
lines=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-index-excerpt.tex.txt').write_text('\n'.join(lines[529:642])+'\n')
(D/'theta-scaling-excerpt.lean.txt').write_text('\n'.join((ROOT/'Roth/Theta.lean').read_text().splitlines()[414:453])+'\n')
for p in Path('/private/tmp/roth-overview').glob('index-scale-*'):
 if p.is_file() and p.suffix in ['.txt','.json']:cp(p)
put('literature-summary.json',dict(chatgpt_math='n/a: ask_chatgpt_math unavailable',concept='Weighted order of vanishing; homogeneous scaling of weighted support minima.',standard='For fixed polynomial/support, multiplying direct weights by c>=0 multiplies the minimum by c. Denominator parameters lr induce direct factor1/l. Classical r,l positive; source extends to zero via Lean total division and default-zero minimum.',limits='Salami2026 section8 disproves a different auxiliary-polynomial existence statement after anisotropic degree-box flooring; its weighted index definition agrees. nCatLab namespace returned only nLab out-of-namespace pages; nLab direct fetch400 unsupported XHTML. Search failures are not absence evidence.'))
