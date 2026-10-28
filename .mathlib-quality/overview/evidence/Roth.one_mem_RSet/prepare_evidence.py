from pathlib import Path
import hashlib,json,subprocess,shutil
D=Path(__file__).resolve().parent; R=Path('/Users/ramin/LEAN/Roth');N='Roth.one_mem_RSet'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def run(n,args):
 z=subprocess.run(args,cwd=R,capture_output=True,text=True)
 put(n,{'command':args,'cwd':str(R),'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr})
for f in ['input-manifest.json','baseline-build.txt']:
 shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared'/f,D/f)
base=json.loads((D/'input-manifest.json').read_text())['sources_and_pins']
put('source-hashes.json',[{'source':f,'sha256':sha(R/f),'bytes':(R/f).stat().st_size,'matches_baseline':sha(R/f)==v['sha256']}for f,v in base.items()])
shutil.copyfile(R/'Roth/Theta.lean',D/'source-Theta.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
put('canonical-snapshot.json',order);put('canonical-target.json',order[183])
run('callers.json',['rg','--no-ignore','-n','-w','one_mem_RSet','Roth','Roth.lean'])
run('inline-audit.json',['rg','--no-ignore','-n','one_mem_RSet|coeff_one|RSet|indexSet_nonempty','Roth','Roth.lean'])
put('callers-structured.json',[{'declaration':'Roth.indexSet_nonempty','file':'Roth/Theta.lean','line':81,'excerpt':(R/'Roth/Theta.lean').read_text().splitlines()[80],'role':'supremum-family nonemptiness, unit witness; sole explicit caller'}])
put('direct-consumers.json',['Roth.indexSet_nonempty']);put('direct-type-consumers.json',[])
for form,pat in [('current','one_mem_RSet|one_mem.*(height|degree|coeff)|bounded.*polynomial'),('standard','supNorm_one|gaussNorm_one|height_one|degreeOf_one|degrees_one'),('abstract','coeff_one|norm_one|norm_zero|one_ne_zero')]:
 run('rg-'+form+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
tex=R/'.mathlib-quality/references/clean.tex'
(D/'clean-section5-excerpt.tex.txt').write_text('\n'.join(tex.read_text().splitlines()[641:670])+'\n')
put('local-literature.json',{'source':str(tex.relative_to(R)),'sha256':sha(tex),'lines':[642,670],'summary':'Full family has integral nonzero polynomials, all coordinate degree bounds and all coefficient bounds. Constant1 is explicitly admitted to prove nonemptiness; local source assumes finite positive degrees but this law needs no such assumptions.','ask_chatgpt_math':'unavailable'})
paths=['Mathlib/Algebra/MvPolynomial/Basic.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/MonoidAlgebra/Defs.lean','Mathlib/Analysis/Polynomial/Norm.lean','Mathlib/RingTheory/Polynomial/GaussNorm.lean','Mathlib/Analysis/Normed/Ring/Basic.lean']
mi=[]
for path in paths:
 p=R/'.lake/packages/mathlib'/path;a='mathlib-'+path.replace('/','-')+'.txt';shutil.copyfile(p,D/a);mi.append({'path':path,'archive':a,'sha256':sha(p),'bytes':p.stat().st_size})
put('mathlib-inputs.json',mi)
for label in ['original','project','isolated']:
 for suffix in ['executed.lean.txt','receipt.json','region.txt']:
  p=Path('/private/tmp/roth-overview')/f'one-mem184-{label}-{suffix}'
  if p.exists():shutil.copyfile(p,D/p.name)
p=Path('/private/tmp/roth-overview/one-mem184-audit-executed.lean.txt');shutil.copyfile(p,D/p.name)
print('evidence prepared')
