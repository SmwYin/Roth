from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).resolve().parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.index_C_mul'
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
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[146]);assert order[146]['name']==N
cp(ROOT/'.mathlib-quality/overview/progress.json','progress-snapshot.json')
links={}
for p in ['Roth/Index.lean','Roth/Theta.lean','Roth/Taylor.lean','Roth/Box.lean']:
 n=p.replace('/','-')+'.txt';cp(ROOT/p,n);links[p]=n
put('source-links.json',links)
mi=[]
for p in ['Mathlib/Algebra/MonoidAlgebra/Degree.lean','Mathlib/Algebra/MonoidAlgebra/Defs.lean','Mathlib/RingTheory/MvPowerSeries/Order.lean','Mathlib/Algebra/MvPolynomial/Basic.lean','Mathlib/Data/Finsupp/SMul.lean']:
 f=ROOT/'.lake/packages/mathlib'/p;mi.append(dict(path=str(f.relative_to(ROOT)),sha256=sha(f),bytes=f.stat().st_size));cp(f,p.replace('/','-')+'.txt')
put('mathlib-inputs.json',mi)
for n,pat in [('current',r'index_C_mul|Roth.index|support_smul_eq'),('literature',r'weightedOrder_smul|order_smul|weightedOrder_C|natTrailingDegree_smul'),('abstract',r'supDegree_smul|infDegree_smul|support_smul_eq|support_mapRange_of_injective')]:
 run('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('rg-inline.json',['rg','--no-ignore','-n',r'index_C_mul|support_smul_eq|index.*C |index.*sign|sign.*index','Roth','Roth.lean'])
searches=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_C_mul\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','index_C_mul','--','Roth','Roth.lean'])]
inv=sorted({x['file'] for x in order});put('complete-caller-search.json',dict(canonical_source_inventory=inv,searches=searches))
files=[]
for p in inv:
 f=ROOT/p;occ=[dict(line=i,kind='declaration' if p=='Roth/Index.lean' else 'body',text=t) for i,t in enumerate(f.read_text().splitlines(),1) if re.search(r'\bindex_C_mul\b',t)];files.append(dict(path=p,sha256=sha(f),occurrences=occ))
put('lexical-enumeration.json',dict(files=files,applications=1,proof_body_applications=1,statement_applications=0))
put('callers.json',[dict(name='Roth.sum_max_sub_le_index_det',file='Roth/Theta.lean',line=405,kind='body',plan='Retain local adapter while index retained; replay full caller using IndexCMul147.replacement. If inline desired, substitute its rw proof at local hidx using nonzero sign scalar and retain map_intCast normalization.')]);put('direct-consumers.json',dict(consumers=['Roth.sum_max_sub_le_index_det'],scope='293 canonical kernel values, direct target references only'))
run('local-literature-search.json',['rg','-n','ind\(cP|Multiplication by a sign|index|sign','.mathlib-quality/references/clean.tex'])
lines=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-index-excerpt.tex.txt').write_text('\n'.join(lines[529:642])+'\n');(D/'clean-sign-excerpt.tex.txt').write_text('\n'.join(lines[819:829])+'\n')
(D/'theta-sign-excerpt.lean.txt').write_text('\n'.join((ROOT/'Roth/Theta.lean').read_text().splitlines()[389:413])+'\n')
for n in ['index-c-mul-original-executed.lean.txt','index-c-mul-original-audit-receipt.json','index-c-mul-original-region.txt','index-c-mul-audit-executed.lean.txt','index-c-mul-audit-region.txt','index-c-mul-mathlib-executed.lean.txt','index-c-mul-mathlib-receipt.json','index-c-mul-target-clean-executed.lean.txt','index-c-mul-target-clean-receipt.json','index-c-mul-target-initial-executed.lean.txt','index-c-mul-target-initial-receipt.json']:
 p=Path('/private/tmp/roth-overview')/n
 if p.exists():cp(p)
put('literature-summary.json',dict(chatgpt_math='n/a: ask_chatgpt_math unavailable',concept='weighted order of vanishing; invariance under nonzero scalar / unit multiplication',standard='Nonzero scalar multiplication preserves every Taylor coefficient zero/nonzero status; weighted support minima are unchanged.',limits='Local text uses positive real r and infinity at zero; project uses natural r and zero index0. Neither affects scalar support equality. nLab fetch400 unsupported XHTML; distinct nCatLab query returned nLab results. Recent arXiv hits use different notions. No external search proves absence.'))
