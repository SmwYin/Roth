from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;N='Roth.four_lt_rpow'
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file()or p.name in exclude:continue
 dst='.mathlib-quality/overview/mathlibable/'+N+'.md'if p.name=='report.md'else'.mathlib-quality/overview/evidence/'+N+'/'+p.name
 files.append(dict(source=str(p),destination=dst,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=files),indent=2)+'\n')
