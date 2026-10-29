"""Append one explicitly root-reviewed endpoint to an existing reviewed YES group.
No verdict inference, native execution, Git or accepted report changes.
"""
from pathlib import Path
import json,hashlib,sys
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth')
read=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert len(sys.argv)==2
spec=Path(sys.argv[1]).resolve();assert spec.parent==B
s=read(spec);assert s['root_reviewed']is True
i=read(B/'final-completed-inventory-preparation.json');y=i['rows'][-1]
assert y['declaration']==s['declaration']and y['canonical_index']==s['canonical_index']
source=Path(y['report_source']);assert source.is_relative_to(R)or source.is_relative_to(B/'assess')
assert y['report_sha256']==s['accepted_report_sha256']==H(source)
assert y['verdict']==s['verdict']and y['verdict'].startswith('YES')
p=B/'final-completed-yes-mathematical-groups-preparation.json';g=read(p)
assert not any(a['declaration']==y['declaration']for q in g['groups']for a in q['assessments'])
matches=[q for q in g['groups']if q['mathematical_group']==s['append_to_existing_yes_group']]
assert len(matches)==1
matches[0]['assessments'].append({k:y[k]for k in ['canonical_index','declaration','what','verdict','report','report_sha256','native_direct_body_dependencies']})
p.write_text(json.dumps(g,indent=2,ensure_ascii=False)+'\n')
print('PASS explicit root grouping',y['declaration'],'in',s['append_to_existing_yes_group'])
