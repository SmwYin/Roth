from pathlib import Path
import json,hashlib
b=Path(__file__).resolve().parent;name='MvPolynomial.hasseDeriv_rename'
files=[]
for p in sorted(b.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','validation-receipt.json','worker-copy-manifest.json','root-review.json'] :continue
 files.append(dict(source=p.name,destination=f'.mathlib-quality/overview/mathlibable/{name}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{name}/{p.name}',sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(b/'copy-manifest.json').write_text(json.dumps(dict(files=files,exclusions=['copy-manifest.json self-reference','validation-receipt.json generated validation output','worker-copy-manifest.json historical integration record','root-review.json root acceptance record']),indent=2)+'\n')
