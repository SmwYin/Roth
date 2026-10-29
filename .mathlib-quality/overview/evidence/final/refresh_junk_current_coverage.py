"""Refresh completed-prefix usage review; new zero-consumer entries need explicit root disposition."""
from pathlib import Path
import json,hashlib
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
I=json.loads((B/'final-completed-inventory-preparation.json').read_text());idx={x['declaration']:x for x in I['rows']};U=json.loads((B/'final-completed-api-usage-preparation.json').read_text());assert U['completed_count']==I['completed_count']
basepath=B/'final-completed-junk-usage-reviewed-synthesis-preparation.json';base=json.loads(basepath.read_text());assert all(H(R/f)==h for f,h in base['source_hashes'].items())
p=B/'final-completed-junk-usage-current-coverage-preparation.json';old=json.loads(p.read_text())if p.exists()else{};prior=old.get('reviewed_zero_consumer_rows',old.get('unchanged_dispositions',base['zero_consumer_rows']));prior={x['declaration']:x for x in prior}
zeros={x['declaration']for x in U['rows']if x['has_no_source_or_direct_body_or_type_consumers']};rows=[]
for name in [x['declaration']for x in I['rows']if x['declaration']in zeros]:
 x=idx[name];assert H(Path(x.get('report_source',str(R/x['report']))))==x['report_sha256']
 if name in prior:
  y=prior[name];assert y['report_sha256']==x['report_sha256']
  if y.get('root_disposition_source'):assert H(B/y['root_disposition_source'])==y['root_disposition_sha256']
 else:
  options=[]
  for f in B.glob('*reviewed-synthesis-preparation.json'):
   d=json.loads(f.read_text());a=d.get('accepted_assessment',{})
   if a.get('declaration')==name and a.get('report_sha256')==x['report_sha256']and d.get('root_junk_disposition'):options.append((f,d))
  assert len(options)==1,('Need explicit root-reviewed new zero-consumer disposition',name)
  f,d=options[0];y={k:x[k]for k in ['declaration','verdict','report','report_sha256']};y.update(interpretation=d['root_junk_disposition'],root_disposition_source=f.name,root_disposition_sha256=H(f))
 rows.append(y)
out={'status':'ROOT-REVIEWED completed-prefix junk/usage reconciliation; final293 acceptance separate','completed_count':I['completed_count'],'base_review':{'source':basepath.name,'sha256':H(basepath)},'usage_provenance':{'source':'final-completed-api-usage-preparation.json','sha256':H(B/'final-completed-api-usage-preparation.json')},'zero_consumer_count':len(rows),'reviewed_zero_consumer_rows':rows,'production_scan_reuse':'Original successful source scans remain applicable: all14 original source hashes freshly equal the unchanged source snapshot. No new code and no repeated scan needed.','source_hashes':base['source_hashes'],'limitations':['These are zero lexical and canonical direct-kernel consumers, not external/simp/generated/transitive deadness.','No automatic deletion from NO, private-prefilter, or absent direct consumers.','Every new zero-consumer name requires an explicit root-authored disposition tied to its accepted report hash.']};p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('PASS current junk/usage coverage:',I['completed_count'],'assessed;',len(rows),'explicitly reviewed zero-consumer declarations; unchanged-source scan reuse verified')
