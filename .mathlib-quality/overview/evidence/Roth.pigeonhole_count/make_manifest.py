from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;N='Roth.pigeonhole_count'
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
xs=[]
for p in sorted(D.iterdir()):
 if p.is_file()and p.name not in excluded:
  dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
  xs.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=xs),indent=2)+'\n')
print('Manifest',len(xs),'artifacts')
