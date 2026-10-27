from pathlib import Path
import hashlib,json
D=Path(__file__).parent;NAME='Roth.index_nonneg';files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dest='.mathlib-quality/overview/mathlibable/'+NAME+'.md' if p.name=='report.md' else '.mathlib-quality/overview/evidence/'+NAME+'/'+p.name
 files.append({'source':str(p),'destination':dest,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(D/'copy-manifest.json').write_text(json.dumps({'declaration':NAME,'files':files},indent=2)+'\n')
