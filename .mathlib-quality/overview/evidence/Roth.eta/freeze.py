from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;N='Roth.eta'
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file()or p.name in {'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}:continue
 dst='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
 files.append(dict(source=str(p),destination=dst,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=files),ensure_ascii=False,indent=2)+'\n')
print('Current231 manifest:',len(files),'artifacts')
