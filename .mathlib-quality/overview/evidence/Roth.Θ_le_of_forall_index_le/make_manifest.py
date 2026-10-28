from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
N='Roth.Θ_le_of_forall_index_le'
ex={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
a=[]
for p in sorted(D.iterdir()):
 if not p.is_file()or p.name in ex:continue
 dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if p.name=='report.md'else'evidence/'+N+'/'+p.name)
 a.append(dict(source=str(p),destination=dest,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=a),indent=2,ensure_ascii=False)+'\n')
