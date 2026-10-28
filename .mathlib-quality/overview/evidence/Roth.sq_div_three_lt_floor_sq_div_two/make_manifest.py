from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;N='Roth.sq_div_three_lt_floor_sq_div_two';files=[]
for p in sorted(D.iterdir()):
 if not p.is_file()or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dst='.mathlib-quality/overview/mathlibable/'+N+'.md'if p.name=='report.md'else'.mathlib-quality/overview/evidence/'+N+'/'+p.name
 files.append(dict(source=str(p),destination=dst,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=files),ensure_ascii=False,indent=2)+'\n')
print('Manifest files:',len(files))
