from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;N='Roth.indexSet_bddAbove'
rows=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md' if p.name=='report.md' else 'evidence/'+N+'/'+p.name)
 rows.append({'source':str(p),'destination':dest,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(D/'copy-manifest.json').write_text(json.dumps({'declaration':N,'files':rows},indent=2)+'\n')
