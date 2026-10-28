from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).resolve().parent
R=Path('/Users/ramin/LEAN/Roth')
N='Roth.Θ_le_of_forall_index_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def wr(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def rd(n):return json.loads((D/n).read_text())
def command(n,args):
 z=subprocess.run(args,cwd=R,text=True,capture_output=True);wr(n,dict(request=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));return z
for f in Path('/private/tmp/roth-overview').glob('theta-upper190-*'):
 if f.is_file():shutil.copy2(f,D/f.name)
for f in ['input-manifest.json','baseline-build.txt']:shutil.copy2(R/'.mathlib-quality/overview/evidence/shared'/f,D/f)
base=rd('input-manifest.json')['sources_and_pins'];wr('source-hashes.json',[dict(source=n,sha256=sha(R/n),matches_baseline=sha(R/n)==v['sha256'])for n,v in base.items()])
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());wr('canonical-snapshot.json',order);wr('canonical-target.json',order[189])
shutil.copy2(R/'Roth/Theta.lean',D/'Theta.lean.txt')
command('callers-rg.json',['rg','--no-ignore','-n','Θ_le_of_forall_index_le','Roth','Roth.lean'])
command('callers-git.json',['git','grep','-n','Θ_le_of_forall_index_le','--','Roth/','Roth.lean'])
command('inline-audit.json',['rg','--no-ignore','-n','csSup_le|Real.sSup_le|Θ_le_of_forall_index_le','Roth','Roth.lean'])
for form,pat in [('current','Roth\\.Θ_le_of_forall_index_le|forall_index_le'),('literature','theorem csSup_le|theorem sSup_le|lemma sSup_le'),('abstract','forall_mem_image2|sSup_image2')]:command('rg-'+form+'.json',['rg','--no-ignore','-n',pat,'.lake/packages/mathlib/Mathlib'])
command('local-literature.json',['rg','-n','Taking the supremum|supremum|Theta|Theta_m|\\\\Theta','.mathlib-quality/references/clean.tex'])
f=R/'.mathlib-quality/references/clean.tex';wr('local-literature-input.json',dict(source=str(f.relative_to(R)),sha256=sha(f)))
s=f.read_text();start=s.index('Index across sets of polynomials') if 'Index across sets of polynomials'in s else s.index('supremum');(D/'clean-section5-excerpt.tex.txt').write_text(s[max(0,start-100):start+18000])
files=['Mathlib/Order/ConditionallyCompleteLattice/Basic.lean','Mathlib/Order/ConditionallyCompleteLattice/Defs.lean','Mathlib/Data/Set/NAry.lean','Mathlib/Data/Real/Archimedean.lean','Mathlib/Algebra/Order/Archimedean/Real/Basic.lean']
mi=[]
for name in files:
 f=R/'.lake/packages/mathlib'/name;a='mathlib-'+name.replace('/','-')+'.txt';shutil.copy2(f,D/a);mi.append(dict(path=name,archive=a,sha256=sha(f),bytes=f.stat().st_size))
wr('mathlib-inputs.json',mi)
r=rd('theta-upper190-original-receipt.json')['result']['structuredContent'];r=r.get('result',r)
wr('native-type.json',dict(type=next(x['message'].split('THETAUPPER190_FULL_TYPE: ',1)[1] for x in r['items']if x['message'].startswith('THETAUPPER190_FULL_TYPE: '))))
wr('callers.json',dict(call_occurrences=2,distinct_declarations=2,external_to_file=0,statement_occurrences=0,callers=[dict(name='Roth.Θ_unique_le',file='Roth/Theta.lean',line=258,reference='Θ_le_of_forall_index_le hB fun _ hR _ hh ↦',refactor='csSup_le (indexSet_nonempty hB q r), destruct indexSet witnesses, preserve index_unique_le_log_div continuation'),dict(name='Roth.Θ_option_le',file='Roth/Theta.lean',line=599,reference='refine Θ_le_of_forall_index_le hB fun R hR h hh ↦ ?_',refactor='refine csSup_le (indexSet_nonempty hB q r) ?_; rintro _ ⟨R,hR,h,hh,rfl⟩; preserve index_le_lem6/Finset.le_sup continuation')]))
wr('preparation-not-executed.json',dict(description='Initial draft tried removing Fintype from fixed-parent signatures; root pre-execution review rejected it because Θ and index require the instance. Revised before any native execution. No rejected native receipts.'))
