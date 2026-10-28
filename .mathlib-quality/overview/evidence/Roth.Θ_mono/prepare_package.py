from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent
R=Path('/Users/ramin/LEAN/Roth')
N='Roth.Θ_mono'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def wr(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def rd(n):return json.loads((D/n).read_text())
def command(n,args):
 z=subprocess.run(args,cwd=R,text=True,capture_output=True);wr(n,dict(request=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));return z
for f in Path('/private/tmp/roth-overview').glob('theta-mono191-*'):
 if f.is_file():shutil.copy2(f,D/f.name)
for f in ['input-manifest.json','baseline-build.txt']:shutil.copy2(R/'.mathlib-quality/overview/evidence/shared'/f,D/f)
base=rd('input-manifest.json')['sources_and_pins'];wr('source-hashes.json',[dict(source=n,sha256=sha(R/n),matches_baseline=sha(R/n)==v['sha256'])for n,v in base.items()])
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());wr('canonical-snapshot.json',order);wr('canonical-target.json',order[190])
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());wr('accepted-verdict-snapshot.json',progress['completed_declarations'])
shutil.copy2(R/'Roth/Theta.lean',D/'Theta.lean.txt')
command('callers-rg.json',['rg','--no-ignore','-n','Θ_mono','Roth','Roth.lean'])
command('callers-git.json',['git','grep','-n','Θ_mono','--','Roth/','Roth.lean'])
command('inline-audit.json',['rg','--no-ignore','-n','csSup_le_csSup|Real.sSup_le|Θ_mono|indexSet.*⊆|RSet.*⊆','Roth','Roth.lean'])
for form,pat in [('current','Roth\\.Θ_mono|theorem Θ_mono'),('literature','theorem csSup_le_csSup|theorem sSup_le_sSup|lemma sSup_le'),('abstract','csSup_le_csSup|IsLUB.mono|image2_subset')]:command('rg-'+form+'.json',['rg','--no-ignore','-n',pat,'.lake/packages/mathlib/Mathlib'])
command('local-literature.json',['rg','-n','nondecreasing|increasing.*B|supremum|\\\\Theta','.mathlib-quality/references/clean.tex'])
f=R/'.mathlib-quality/references/clean.tex';wr('local-literature-input.json',dict(source=str(f.relative_to(R)),sha256=sha(f)))
s=f.read_text();start=s.index('Index across sets of polynomials');(D/'clean-section5-excerpt.tex.txt').write_text(s[start:start+18000])
files=['Mathlib/Order/ConditionallyCompleteLattice/Basic.lean','Mathlib/Order/ConditionallyCompleteLattice/Defs.lean','Mathlib/Data/Set/NAry.lean','Mathlib/Algebra/Order/Archimedean/Real/Basic.lean']
mi=[]
for name in files:
 f=R/'.lake/packages/mathlib'/name;a='mathlib-'+name.replace('/','-')+'.txt';shutil.copy2(f,D/a);mi.append(dict(path=name,archive=a,sha256=sha(f),bytes=f.stat().st_size))
wr('mathlib-inputs.json',mi)
r=rd('theta-mono191-original-receipt.json')['result']['structuredContent'];r=r.get('result',r)
wr('native-type.json',dict(type=next(x['message'].split('THETAMONO191_FULL_TYPE: ',1)[1]for x in r['items']if x['message'].startswith('THETAMONO191_FULL_TYPE: '))))
wr('callers.json',dict(call_occurrences=2,distinct_declarations=2,external_to_file=0,statement_occurrences=0,documentation_occurrences=1,callers=[dict(name='Roth.theta_scaled_unique_le_aux',visibility='private',file='Roth/Theta.lean',line=758,reference='refine (Θ_mono hM1 hM _).trans',refactor='Inline csSup_le_csSup at s=indexSet M (fun _:Unit ↦ q₂) (fun _ ↦ l*r₂), t=indexSet (q₁^(δ*(l*r₁))) same q/r; retain indexSet_bddAbove, indexSet_nonempty hM1 and height inclusion using hM; preserve full Θ_unique_le/arithmetic continuation'),dict(name='Roth.theta_prefix_lt_aux',visibility='private',file='Roth/Theta.lean',line=790,reference='refine (Θ_mono hM1 hM _).trans_lt',refactor='Inline csSup_le_csSup at q=(fun j:Fin(n+1) ↦ q j.castSucc), r=(fun j ↦ l*r j.castSucc), heights M and q0^(ε*(l*r0)); retain project boundedness/nonempty and height inclusion using hM; preserve hCeq/ih/finite-index arithmetic continuation')]))
