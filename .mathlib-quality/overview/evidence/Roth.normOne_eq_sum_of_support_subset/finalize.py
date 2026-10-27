from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;N='Roth.normOne_eq_sum_of_support_subset'
files=[]
for p in sorted(D.iterdir()):
 if p.is_file() and p.name not in ['copy-manifest.json','worker-copy-manifest.json','root-review.json']:
  files.append(dict(source=str(p),destination=('.mathlib-quality/overview/mathlibable/'+N+'.md' if p.name=='report.md' else '.mathlib-quality/overview/evidence/'+N+'/'+p.name),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=files),ensure_ascii=False,indent=2)+'\n')
print(len(files),'artifacts manifested')

