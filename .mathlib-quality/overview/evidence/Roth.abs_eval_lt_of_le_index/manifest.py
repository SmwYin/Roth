from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;N='Roth.abs_eval_lt_of_le_index'
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files=[]
for p in sorted(D.rglob('*')):
 if not p.is_file()or p.name in exclude or '_validation-layout'in p.relative_to(D).parts:continue
 rel=str(p.relative_to(D));dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if rel=='report.md'else'evidence/'+N+'/'+rel)
 files.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,recursive=True,files=files),indent=2)+'\n')
