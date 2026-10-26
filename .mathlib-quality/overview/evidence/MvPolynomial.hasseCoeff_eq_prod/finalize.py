"""Recompute frozen copy manifest after all complete gates; excludes manifest itself."""
import pathlib,json,hashlib
base=pathlib.Path(__file__).resolve().parent
target='MvPolynomial.hasseCoeff_eq_prod'
root=pathlib.Path('/Users/ramin/LEAN/Roth')
a=json.loads((base/'assessment.json').read_text());assert a['completed'] and not a['unresolved']
files=[]
for p in sorted(base.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','validation-receipt.json']:continue
 if p.name=='report.md':dest='.mathlib-quality/overview/mathlibable/'+target+'.md'
 else:dest='.mathlib-quality/overview/evidence/'+target+'/'+p.name
 b=p.read_bytes();files.append({'source':p.name,'destination':dest,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(base/'copy-manifest.json').write_text(json.dumps({'declaration':target,'files':files},indent=2)+'\n')
