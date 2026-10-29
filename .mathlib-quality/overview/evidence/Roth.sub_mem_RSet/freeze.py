from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.sub_mem_RSet';base='.mathlib-quality/overview/'
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file()or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dst=base+'mathlibable/'+N+'.md'if p.name=='report.md'else base+'evidence/'+N+'/'+p.name
 files.append(dict(source=str(p),destination=dst,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'copy-manifest.json').write_text(json.dumps(dict(declaration=N,files=files),ensure_ascii=False,indent=2)+'\n')
print('manifest',len(files),'files')
