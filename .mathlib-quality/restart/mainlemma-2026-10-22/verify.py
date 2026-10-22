from pathlib import Path
import json,gzip,hashlib
p=Path(__file__).resolve().parent;m=json.loads((p/'manifest.json').read_text());seen=set()
for r in m['rows']:
 f=p/r['saved'];b=f.read_bytes();assert len(b)==r['stored_bytes'] and hashlib.sha256(b).hexdigest()==r['stored_sha256']
 if r['saved'] not in seen:
  raw=gzip.decompress(b)if r['encoding']=='gzip'else b;assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];seen.add(r['saved'])
print('PASS',len(m['rows']),'indexed files;',len(seen),'unique immutable blobs. Evidence integrity only, no proof acceptance.')
