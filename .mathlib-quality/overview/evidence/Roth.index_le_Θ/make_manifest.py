# coding: utf-8
from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;N='Roth.index_le_Θ'
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=files),indent=2,ensure_ascii=False)+'\n')
