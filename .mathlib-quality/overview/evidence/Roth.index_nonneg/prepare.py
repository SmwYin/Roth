from pathlib import Path
import re,json,hashlib,subprocess,shutil
D=Path('/private/tmp/roth-overview/assess/Roth.index_nonneg'); R=Path('/Users/ramin/LEAN/Roth'); P=Path('/private/tmp/roth-overview/assess/Roth.le_index_iff')
def write(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=True)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['baseline-build.txt','input-manifest.json','canonical-order.json','clean.tex.txt','clean-excerpt.tex.txt','index-consumers-executed.lean.txt','index-consumers-receipt.json','index-expanded-bridge-executed.lean.txt','index-expanded-bridge-receipt.json','index-expanded-mathlib-executed.lean.txt','index-expanded-mathlib-receipt.json']:
 shutil.copy2(P/n,D/n)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());write('canonical-entry.json',next(x for x in order if x['name']=='Roth.index_nonneg'))
inputs=json.loads((P/'inputs.json').read_text())
for x in inputs:
 p=R/x['path'];x.update(sha256=sha(p),bytes=p.stat().st_size);x['match']=x['sha256']==x['expected_sha256']
write('inputs.json',inputs);write('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
links={}
for f in ['Roth/Index.lean','Roth/Theta.lean','Roth/Box.lean']:
 p=R/f;n=p.name+'.txt';shutil.copy2(p,D/n);links[f]=n
write('source-links.json',links)
def run(n,argv):
 z=subprocess.run(argv,cwd=R,text=True,capture_output=True);v={'argv':argv,'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr};write(n,v);return v
searches=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_nonneg\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','-w','index_nonneg','--','Roth/*.lean','Roth.lean'])]
write('complete-caller-search.json',{'canonical_source_inventory':sorted({x['file'] for x in order}|{'Roth.lean'}),'searches':searches})
for form,pattern in [('current',r'index_nonneg|Real.sInf_nonneg'),('literature',r'weightedOrder|weight_nonneg'),('abstract',r'le_inf_iff|sup_le_iff|le_untopD_iff|infDegree'),('inline',r'index_nonneg|sInf_nonneg|0 ≤ index|0 ≤ Roth.index')]:
 roots=['Roth','Roth.lean'] if form=='inline' else ['Roth','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean','.lake/packages/mathlib/Mathlib/Basic/Real/Basic.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean']
 run('rg-'+form+'.json',['rg','--no-ignore','-n',pattern,*roots])
run('local-literature-search.json',['rg','-n','index|nonnegative|ind\(P\)|non-negative','.mathlib-quality/references/clean.tex'])
paths=['.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean','.lake/packages/mathlib/Mathlib/Basic/Real/Basic.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean']
write('mathlib-inputs.json',[{'path':f,'sha256':sha(R/f),'bytes':(R/f).stat().st_size} for f in paths])
callers=[]
for file,name,lines,plan in [('Roth/Index.lean','Roth.index_eq_zero_iff',[100],'Replace the nonnegative argument to antisymm\u2032 by projectedLaw after shared parent bridge. Keep the minimum-attainment and evaluation implications.'),('Roth/Theta.lean','Roth.Θ_nonneg',[110],'After Real.sSup_nonneg and destructuring indexSet, apply the projected finite-inf nonnegative law to the Taylor polynomial with weight_nonneg.'),('Roth/Theta.lean','Roth.sum_max_sub_le_index_det',[395],'Replace the nonnegative index premise inside add_nonneg/max_le with projected finite-inf nonnegativity. Keep weight_nonneg, h2, derivative bounds and determinant sum/product argument.')]:
 s=(R/file).read_text();parts=s.splitlines();start=next(i for i,l in enumerate(parts) if re.search(r'^(theorem|lemma) '+re.escape(name.split('.')[-1])+r'\b',l));end=next((i for i in range(start+1,len(parts)) if re.match(r'^(theorem|lemma|end\b|/--) ',parts[i])),len(parts));fragment='\n'.join(parts[start:end])+'\n'
 callers.append({'file':file,'declaration':name,'reference_lines':lines,'identifier_occurrences':len(lines),'source_sha256':sha(R/file),'source_fragment':fragment,'plan':plan})
write('callers.json',callers);write('direct-consumers.json',{'count':3,'consumers':[x['declaration'] for x in callers]})
s=(R/'Roth/Index.lean').read_text();s=s[s.index('namespace Roth'):];s=s.replace('namespace Roth','namespace IndexReplay138',1).replace('end Roth','end IndexReplay138');s=s.replace('open MvPolynomial','open Roth MvPolynomial',1);s=s.replace('theorem index_nonneg','theorem replacement').replace('  Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)','  IndexNonneg138.originalReplacement P α r').replace('(index_nonneg P α r)','(replacement P α r)')
t=(R/'Roth/Theta.lean').read_text();t=t[t.index('namespace Roth'):];t=t.replace('namespace Roth','namespace ThetaReplay138',1).replace('end Roth','end ThetaReplay138');t=t.replace('open MvPolynomial','open Roth MvPolynomial',1).replace('index_nonneg','IndexNonneg138.originalReplacement')
# Entire two modules replay. Local replay index_eq_zero_iff consumes replacement; Theta uses imported index API.
out=s+'\n'+t+'\n#print axioms IndexReplay138.replacement\n#print axioms IndexReplay138.index_eq_zero_iff\n#print axioms ThetaReplay138.Θ_nonneg\n#print axioms ThetaReplay138.sum_max_sub_le_index_det\n'
(D/'index-nonneg-callers-prepared.lean.txt').write_text(out)
