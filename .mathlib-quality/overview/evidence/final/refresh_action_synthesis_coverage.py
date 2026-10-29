"""Refresh coverage only from accepted declarations and already root-authored synthesis artifacts."""
from pathlib import Path
import json,hashlib
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();I=json.loads((B/'final-completed-inventory-preparation.json').read_text());p=B/'final-completed-action-synthesis-coverage-preparation.json';d=json.loads(p.read_text());rows=I['rows'];assert len(d['rows'])<=len(rows)
for a,b in zip(d['rows'],rows):assert a['declaration']==b['declaration']and a['report_sha256']==b['report_sha256']
for x in d['artifacts']:assert H(B/x['source'])==x['sha256'],x
supp={}
for f in B.glob('*reviewed-synthesis-preparation.json'):
 z=json.loads(f.read_text());a=z.get('accepted_assessment')
 if a:supp.setdefault(a['declaration'],[]).append((f,a))
for x in rows[len(d['rows']):]:
 assert H(Path(x.get('report_source',str(R/x['report']))))==x['report_sha256'];a={k:x[k]for k in['canonical_index','declaration','verdict','report','report_sha256']}
 if x['visibility']=='private':a['action_synthesis']='Private-prefilter disposition remains in completed detailed report; public contribution phases not run.'
 else:
  options=[(f,v)for f,v in supp.get(x['declaration'],[])if v['report_sha256']==x['report_sha256']];assert len(options)==1,('Missing/ambiguous root-reviewed synthesis',x['declaration']);f,v=options[0];assert v['verdict']==x['verdict'];a['action_synthesis']=f.name
  if not any(q['source']==f.name for q in d['artifacts']):d['artifacts'].append({'source':f.name,'sha256':H(f)})
 d['rows'].append(a)
assert [x['declaration']for x in d['rows']]==[x['declaration']for x in rows]
d.update(completed_count=len(rows),public_action_syntheses=sum(x['visibility']=='public'for x in rows),private_prefilter_dispositions=sum(x['visibility']=='private'for x in rows),remaining_unfinished=293-len(rows),unreconciled_completed=[]);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('PASS action synthesis coverage:',len(rows),'accepted,',d['public_action_syntheses'],'public +',d['private_prefilter_dispositions'],'private. Final global acceptance separate.')
