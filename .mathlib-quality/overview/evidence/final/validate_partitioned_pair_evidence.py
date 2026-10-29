"""Validate bounded semantic-pair partitions against current accepted inventory and source."""
from pathlib import Path
import json,hashlib,itertools,sys
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');D=Path(sys.argv[1])if len(sys.argv)>1 else B/'final-pairwise-partitions';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
I=json.loads((B/'final-completed-inventory-preparation.json').read_text());idx={x['declaration']:x for x in I['rows']};m=json.loads((D/'index.json').read_text());assert m['accepted_declaration_count']==len(idx)==I['completed_count'];assert m['inventory_sha256']==H(B/'final-completed-inventory-preparation.json')
original={}
for fn in['final-completed-cross-module-pairwise-preparation.json','final-completed-theta-pairwise-preparation.json']:
 p=B/fn;assert any(x['historical_preparation_identifier']==fn and x['sha256']==H(p)for x in m['historical_inputs'])
 for x in json.loads(p.read_text())['rows']:
  key=tuple(sorted((x['a'],x['b'])));assert key not in original;original[key]=x
reports={n:H(Path(z.get('report_source',str(R/z['report']))))for n,z in idx.items()};assert all(reports[n]==z['report_sha256']for n,z in idx.items());sources={f:H(R/f)for f in{z['file']for z in idx.values()}}
seen=set();total=0
for artifact in m['artifacts']:
 p=D/artifact['path'];assert p.stat().st_size==artifact['bytes']<50_000_000 and H(p)==artifact['sha256'];d=json.loads(p.read_text());assert d['accepted_declaration_count']==len(idx) and d['files']==artifact['files']and len(d['rows'])==d['pair_count']==artifact['pair_count']
 for x in d['rows']:
  key=tuple(sorted((x['a'],x['b'])));assert key not in seen and key in original;seen.add(key);old=original[key]
  assert sorted([idx[n]['file']for n in key])==d['files']
  for field in ['a','b','same_statement','same_proof']:assert x[field]==old[field]
  for field in ['action','verdict','review_method']:assert x.get(field)==old.get(field) and (field in x)==(field in old)
  for v in x['evidence']:
   z=idx[v['declaration']];assert v['report_sha256']==reports[v['declaration']]and v['source_excerpt_sha256']==z['source_sha256']and v['source_file_sha256']==sources[z['file']]
   for k in['canonical_index','file','start_line','end_line','report']:assert v[k]==z[k]
  assert {v['declaration']for v in x['evidence']}==set(key)
  if x.get('review_specification'):assert H(D/x['review_specification'])==old['review_specification_sha256']
 total+=len(d['rows'])
expected={tuple(sorted(p))for p in itertools.combinations(idx,2)};assert seen==set(original)==expected and total==len(seen)==m['pair_count']==m['expected_pairs']==len(idx)*(len(idx)-1)//2
assert m['complete_project_pair_coverage']==(len(idx)==293)
for s in m['specifications']:assert H(D/s['path'])==s['sha256']
print('PASS exact semantic partition preservation:',len(idx),'accepted;',total,'unique pairs; all source/report hashes and comparison texts preserved. Final project acceptance separate.')
