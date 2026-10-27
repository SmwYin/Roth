from pathlib import Path
import subprocess,json,hashlib,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');O=R/'.mathlib-quality/overview'
def put(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def cp(a,n):shutil.copyfile(a,D/n)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((O/'evidence/shared/input-manifest.json').read_text());cp(O/'evidence/shared/input-manifest.json','input-manifest.json');cp(O/'evidence/shared/baseline-build.txt','baseline-build.txt')
rows=[]
for n,v in manifest['sources_and_pins'].items():
 p=R/n;rows.append({'path':n,'sha256':sha(p),'bytes':p.stat().st_size});assert sha(p)==v['sha256']
put('source-hashes.json',rows)
for n in ['Lattice','Box','MainLemma']:cp(R/f'Roth/{n}.lean',f'Roth-{n}.lean.txt')
order=json.loads((O/'declaration-order.json').read_text());put('canonical-snapshot.json',order);put('canonical-entry.json',order[131]);assert order[131]['name']=='Roth.card_filter_weight_le'
put('accepted-yes-history.json',[x for x in json.loads((O/'progress.json').read_text())['completed_declarations'] if x.get('verdict','').startswith('YES')])
queries={
 'full-name':['rg','-n',r'\bRoth\.card_filter_weight_le\b','.lake/packages/mathlib/Mathlib'],
 'current':['rg','-n',r'card_filter_weight|card_filter.*sqrt|sqrt.*card_filter','.lake/packages/mathlib/Mathlib'],
 'literature':['rg','-n',r'lattice.*(count|point)|sum_sq_le_of_mem_box|card_sphere_le_rothNumberNat','.lake/packages/mathlib/Mathlib/Combinatorics','.lake/packages/mathlib/Mathlib/NumberTheory','.lake/packages/mathlib/Mathlib/Algebra/Module/ZLattice'],
 'abstract':['rg','-n',r'meas_ge_le_variance_div_sq|variance_sum_pi|variance_le_sq_of_bounded|toMeasure_uniformOfFintype_apply','.lake/packages/mathlib/Mathlib'],
 'callers':['rg','-n',r'\bcard_filter_weight_le\b','Roth','Roth.lean'],
 'inline':['rg','-n',r'filter.*weight|sqrt.*card|card.*sqrt|2 \*.*√.*lam','Roth'],
 'local-literature':['rg','-n',r'roth:lem8|Lattice count estimate|lattice count|Hoeffding|Chebyshev','.mathlib-quality/references/clean.tex']}
for n,cmd in queries.items():
 z=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('rg-'+n+'.json',{'command':cmd,'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr,'untruncated':True})
text=(R/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {text[i]}'for i in range(1047,1154))+'\n')
files={'.lake/packages/mathlib/Mathlib/Probability/Moments/Variance.lean':[(380,509)],'.lake/packages/mathlib/Mathlib/Probability/Distributions/Uniform.lean':[(270,307)],'.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean':[(144,198),(493,495)],'.lake/packages/mathlib/Mathlib/Data/Finset/Card.lean':[(414,420)],'.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean':[(733,752)]}
parts=[]; hashes=[]
for n,ranges in files.items():
 p=R/n;lines=p.read_text().splitlines();hashes.append({'path':n,'sha256':sha(p),'bytes':p.stat().st_size});parts.append(n)
 for a,b in ranges:parts.extend(f'{i+1}: {lines[i]}'for i in range(a-1,b))
(D/'mathlib-candidates.txt').write_text('\n'.join(parts)+'\n');put('candidate-source-hashes.json',hashes)
put('explicit-callers.json',{'count':1,'external_files':['Roth/MainLemma.lean'],'callers':[{'file':'Roth/MainLemma.lean','line':574,'declaration':'_private.Roth.MainLemma.0.Roth.mul_card_filter_weight_le_aux','pattern':'(card_filter_weight_le m r hr (by positivity)) ha.le).trans_eq ?_','refactor':'Retain until accepted upstream representation chosen. If function-box law introduced, convert one filtered-box cardinality by proved bridge then keep mul_le_mul_of_nonneg_left and existing push_cast/field_simp/ring.'}],'inline_derivations':[],'scope':'Explicit source references only, not transitive kernel/simp closure.'})
put('optional-tools.json',{'ask_chatgpt_math':'unavailable','other_channels_reduced':False})
print('captured all17 matching sources/pins and exact searches')
