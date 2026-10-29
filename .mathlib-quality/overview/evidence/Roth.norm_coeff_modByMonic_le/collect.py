from pathlib import Path
import json,subprocess,hashlib
D=Path(__file__).resolve().parent;R=Path.cwd()
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
for form,pattern in [('current',r'norm_coeff_modByMonic_le|norm.*modByMonic|modByMonic.*norm'),('standard',r'coeff_modByMonic|div_wf_lemma|modByMonic_eq_self_iff'),('abstract',r'gaussNorm.*modByMonic|modByMonic.*gaussNorm|toSeminormedRing|supNorm')]:
 args=['rg','-n',pattern,'.lake/packages/mathlib/Mathlib'];r=subprocess.run(args,text=True,capture_output=True);put('search-'+form+'-rg.json',dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
args=['rg','--no-ignore','-n',r'norm_coeff_modByMonic|coeff.*modByMonic|div_wf_lemma|leadingCoeff.*X.*natDegree','Roth','Roth.lean'];r=subprocess.run(args,text=True,capture_output=True);put('inline-audit.json',dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
files=['Mathlib/Algebra/Polynomial/Div.lean','Mathlib/Algebra/Polynomial/CoeffMem.lean','Mathlib/Analysis/Normed/Unbundled/RingSeminorm.lean','Mathlib/RingTheory/Polynomial/GaussNorm.lean','Mathlib/Analysis/Polynomial/Norm.lean'];xs=[]
for f in files:
 p=R/'.lake/packages/mathlib'/f;n='mathlib-'+f.replace('/','-')+'.txt';(D/n).write_bytes(p.read_bytes());xs.append(dict(path=f,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,archive=n))
put('mathlib-inputs.json',xs)
p=R/'.mathlib-quality/references/clean.tex';(D/'local-excerpt.tex.txt').write_text('\n'.join(p.read_text().splitlines()[1430:1482])+'\n')
r=json.loads((D/'original-receipt.json').read_text())['result']['structuredContent']['result'];msgs=[x['message'] for x in r['items']];put('native-type.json',dict(type=next(x.split('REM243_FULL_TYPE: ')[1] for x in msgs if x.startswith('REM243_FULL_TYPE: ')),printer_elision=any('characters elided' in x for x in msgs)))
put('canonical-consumers.json',dict(body=[x.split('REM243_DIRECT_CONSUMER: ')[1]for x in msgs if x.startswith('REM243_DIRECT_CONSUMER: ')],type=[x.split('REM243_DIRECT_TYPE_CONSUMER: ')[1]for x in msgs if x.startswith('REM243_DIRECT_TYPE_CONSUMER: ')]))
print('collected searches, pinned sources, full type and consumers')
