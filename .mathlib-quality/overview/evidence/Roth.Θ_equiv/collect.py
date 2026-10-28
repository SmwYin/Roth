# coding: utf-8
from pathlib import Path
import json,hashlib,subprocess,shutil
P=Path('/private/tmp/roth-overview/assess/Roth.\u0398_equiv');R=Path.cwd()
def dump(n,v): (P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def run(n,c):
 z=subprocess.run(c,shell=True,text=True,capture_output=True);dump(n,dict(command=c,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
def cp(s,n):shutil.copyfile(s,P/n)
cp('.mathlib-quality/overview/evidence/shared/input-manifest.json','input-manifest.json')
cp('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')
base=json.loads((P/'input-manifest.json').read_text())['sources_and_pins'];fresh=[]
for f,v in base.items():
 b=(R/f).read_bytes();h=hashlib.sha256(b).hexdigest();fresh.append(dict(source=f,sha256=h,bytes=len(b),matches_baseline=h==v['sha256']))
assert len(fresh)==17 and all(x['matches_baseline']for x in fresh);dump('source-hashes.json',fresh)
for f in ['Theta','Index','CoeffNorm','Taylor','Box']:
 cp('Roth/'+f+'.lean','source-'+f+'.lean.txt')
order=json.loads(Path('.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-snapshot.json',order);dump('canonical-target.json',order[192]);assert order[192]['name']=='Roth.\u0398_equiv'
progress=json.loads(Path('.mathlib-quality/overview/progress.json').read_text());dump('accepted-verdict-snapshot.json',progress)
run('callers-rg.json',"rg --no-ignore -n '\u0398_equiv' Roth Roth.lean")
run('callers-git.json',"git grep -n '\u0398_equiv' -- Roth Roth.lean")
run('source-inventory.json','rg --files --no-ignore Roth')
run('inline-audit.json',"rg --no-ignore -n 'indexSet_comp_subset|congrArg sSup|rename.*R|\u0398_equiv' Roth Roth.lean")
run('rg-current.json',"rg -n 'Roth[.]\u0398_equiv|indexSet_comp_subset|bounded.*coeff.*rename|rename.*bounded.*coeff' .lake/packages/mathlib/Mathlib")
run('rg-literature.json',"rg -n 'renameEquiv|coeff_rename_mapDomain|degreeOf_rename_of_injective|rename_eq_zero_iff_of_injective|support_rename_of_injective' .lake/packages/mathlib/Mathlib/Algebra/MvPolynomial")
run('rg-abstract.json',"rg -n 'theorem (Equiv.iSup_congr|Equiv.iSup_comp|iSup_congr|sSup_image|image2_image_left|image2_image_right|image2_congr)' .lake/packages/mathlib/Mathlib/Order/CompleteLattice/Basic.lean .lake/packages/mathlib/Mathlib/Data/Set/NAry.lean")
run('rg-transport.json',"rg -n '(rename|mapDomain|embDomain)' .lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/{Rename,Degrees,Supported}.lean .lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean")
run('local-literature.json',"rg -n 'renam|supremum|Theta_m' .mathlib-quality/references/clean.tex")
b=Path('.mathlib-quality/references/clean.tex').read_bytes();dump('local-literature-input.json',dict(source='.mathlib-quality/references/clean.tex',sha256=hashlib.sha256(b).hexdigest(),bytes=len(b)))
(P/'clean-excerpt.tex.txt').write_text('\n'.join(b.decode().splitlines()[620:703])+'\n')
paths=['Mathlib/Algebra/MvPolynomial/Rename.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/MvPolynomial/Supported.lean','Mathlib/Data/Set/NAry.lean','Mathlib/Order/CompleteLattice/Basic.lean']
mi=[]
for f in paths:
 b=Path('.lake/packages/mathlib',f).read_bytes();n='mathlib-'+f.replace('/','-')+'.txt';(P/n).write_bytes(b);mi.append(dict(path=f,archive=n,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b)))
dump('mathlib-inputs.json',mi)
dump('callers.json',dict(call_occurrences=1,distinct_declarations=1,outside_declaring_file=0,external_files=0,callers=[dict(name='Roth.theta_lt_succ_aux',visibility='private',file='Roth/Theta.lean',line=919,reference='rw [\u2190 \u0398_equiv e.symm ((q 0 : \u211d) ^ (\u03b4 * r 0)) q r]',plan='Retain local theorem until arithmetic-family transport API settled; replay complete caller with freshly proved replacement. If splitting, prove indexSet equality via inverse transports, apply congrArg sSup, then retain reverse rewrite.')]))
