from pathlib import Path
import hashlib,json,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.indexSet_nonempty'
def put(n,v): (D/n).write_text(json.dumps(v,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=R/'.mathlib-quality/overview/evidence/shared'
for n in ['input-manifest.json','baseline-build.txt']:shutil.copy(base/n,D/n)
b=json.loads((D/'input-manifest.json').read_text())['sources_and_pins']
put('source-hashes.json',[{'source':n,'sha256':sha(R/n),'matches_baseline':sha(R/n)==v['sha256']}for n,v in b.items()])
shutil.copy(R/'Roth/Theta.lean',D/'source-Theta.lean.txt')
o=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-snapshot.json',o);put('canonical-target.json',o[184])
assert o[184]['name']==N
put('direct-consumers.json',['Roth.Θ_le_of_forall_index_le','Roth.Θ_mono']);put('direct-type-consumers.json',[])
def run(name,args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);put(name,{'command':args,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
run('callers.json',['rg','--no-ignore','-n',r'\bindexSet_nonempty\b','Roth','Roth.lean'])
put('callers-structured.json',[{'declaration':n,'file':'Roth/Theta.lean','line':l,'excerpt':(R/'Roth/Theta.lean').read_text().splitlines()[l-1]}for n,l in [('Roth.Θ_le_of_forall_index_le',127),('Roth.Θ_mono',136)]])
for form,pattern in [('current','indexSet_nonempty|RSet.*Nonempty|index.*[Nn]onempty'),('standard','image2_nonempty_iff|Nonempty.image2|image_nonempty'),('abstract','theorem Nonempty.image2|theorem image2_nonempty_iff|theorem Nonempty.prod|def image2')]:
 run('rg-'+form+'.json',['rg','--no-ignore','-n',pattern,'.lake/packages/mathlib/Mathlib'])
run('inline-audit.json',['rg','--no-ignore','-n','one_mem_RSet|isCoprime_one_left|indexSet.*Nonempty|csSup_le|csSup_le_csSup','Roth','Roth.lean'])
p=R/'.mathlib-quality/references/clean.tex';s=p.read_text();put('local-literature.json',{'path':str(p.relative_to(R)),'sha256':sha(p),'queries':['index across sets','constant polynomial','supremum is well-defined'],'locator':'section5 lines643–701','summary':'Nonemptiness explicitly witnessed by constant1 with numerators1, before boundedness/Taylor argument. Source assumes B≥1; no positive q or r needed for the existence witness.'});(D/'clean-section5-excerpt.tex.txt').write_text('\n'.join(s.splitlines()[642:701])+'\n')
inputs=[]
for n in ['Mathlib/Data/Set/NAry.lean','Mathlib/Data/Set/Operations.lean','Mathlib/Data/Set/Image.lean','Mathlib/Algebra/MvPolynomial/Basic.lean']:
 p=R/'.lake/packages/mathlib'/n;a='mathlib-'+n.replace('/','-')+'.txt';shutil.copy(p,D/a);inputs.append({'path':n,'archive':a,'sha256':sha(p),'bytes':p.stat().st_size})
put('mathlib-inputs.json',inputs)
