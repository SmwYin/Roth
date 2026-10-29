"""Check all accepted declarations have their root-reviewed action disposition and intact evidence."""
from pathlib import Path
import json,hashlib
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();I=json.loads((B/'final-completed-inventory-preparation.json').read_text());d=json.loads((B/'final-completed-action-synthesis-coverage-preparation.json').read_text());rows=I['rows'];assert len(rows)==len(d['rows'])==d['completed_count']
artifacts={x['source']:x for x in d['artifacts']};assert len(artifacts)==len(d['artifacts'])
for f,v in artifacts.items():assert (B/f).is_file()and H(B/f)==v['sha256']
for x,z in zip(d['rows'],rows):
 for k in['canonical_index','declaration','verdict','report','report_sha256']:assert x[k]==z[k]
 assert H(Path(z.get('report_source',str(R/z['report']))))==x['report_sha256']
 if z['visibility']=='private':assert z['verdict']=='SKIP'and x['action_synthesis'].startswith('Private-prefilter disposition')
 else:assert x['action_synthesis']in artifacts
assert d['public_action_syntheses']==sum(x['visibility']=='public'for x in rows)
assert d['private_prefilter_dispositions']==sum(x['visibility']=='private'for x in rows)
assert d['remaining_unfinished']==293-len(rows)and not d['unreconciled_completed']and d['production_changes']is False
print('PASS complete accepted-prefix action coverage:',len(rows),'declarations; intact root synthesis and accepted report hashes; private/public workflow distinction preserved.')
