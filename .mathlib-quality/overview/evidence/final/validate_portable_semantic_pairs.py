#!/usr/bin/env python3
"""Validate preserved semantic comparison evidence without private scratch registries.

Usage: python3 validate_portable_semantic_pairs.py REPOSITORY PARTITIONS INVENTORY
       [--require-complete]
This checks evidence integrity and coverage, not a machine proof of the human judgments.
"""
from pathlib import Path
import hashlib,itertools,json,sys
R=Path(sys.argv[1]).resolve();D=Path(sys.argv[2]).resolve();I=Path(sys.argv[3]).resolve()
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
i=load(I);index=load(D/'index.json');rows=i['rows'];names=[x['declaration']for x in rows];n=len(rows)
order=load(R/'.mathlib-quality/overview/declaration-order.json')
assert n==i['completed_count']==index['accepted_declaration_count']
assert names==[x['name']for x in order[:n]] and len(names)==len(set(names))
assert index['inventory_sha256']==H(I)
if '--require-complete'in sys.argv:assert n==len(order)==293 and index['complete_project_pair_coverage']
else:assert index['complete_project_pair_coverage']==(n==293)
expected={tuple(sorted(p))for p in itertools.combinations(names,2)};seen=set();byname={x['declaration']:x for x in rows}
source_lines={x['file']:(R/x['file']).read_text().splitlines()for x in rows}
source_hash={f:H(R/f)for f in source_lines};report_hash={x['report']:H(R/x['report'])for x in rows}
for x in rows:
 assert x['report_sha256']==report_hash[x['report']]
 assert x['source_sha256']==hashlib.sha256('\n'.join(source_lines[x['file']][x['start_line']-1:x['end_line']]).encode()).hexdigest()
count=0
for a in index['artifacts']:
 p=D/a['path'];assert p.is_file()and H(p)==a['sha256']and p.stat().st_size==a['bytes']
 assert p.stat().st_size<50_000_000
 z=load(p);assert z['files']==a['files'] and z['accepted_declaration_count']==n and len(z['rows'])==z['pair_count']==a['pair_count']
 for pair in z['rows']:
  key=tuple(sorted((pair['a'],pair['b'])));assert key in expected and key not in seen;seen.add(key)
  assert isinstance(pair['same_statement'],(bool,str))and pair['same_proof']and pair.get('action',pair.get('verdict'))
  assert len(pair['evidence'])==2 and {e['declaration']for e in pair['evidence']}==set(key)
  for e in pair['evidence']:
   x=byname[e['declaration']]
   for k in ['canonical_index','file','start_line','end_line','report','report_sha256']:assert e[k]==x[k]
   assert e['source_excerpt_sha256']==x['source_sha256']and e['source_file_sha256']==source_hash[x['file']]
  assert sorted(e['file']for e in pair['evidence'])==sorted(a['files'])
 count+=len(z['rows'])
for s in index['specifications']:
 p=D/s['path'];assert p.is_file()and H(p)==s['sha256']
if 'markdown_artifacts'in index:
 assert len(index['markdown_artifacts'])==len(index['artifacts'])
 json_byname={a['path']:a for a in index['artifacts']}
 for a in index['markdown_artifacts']:
  p=D/a['path'];j=json_byname[a['json_source']]
  assert H(p)==a['sha256']and p.stat().st_size==a['bytes']<50_000_000
  assert a['json_source_sha256']==j['sha256']and a['pair_count']==j['pair_count']
  assert sum(line.startswith('| `')for line in p.read_text().splitlines())==a['pair_count']
 md=index['markdown_index'];assert H(D/md['path'])==md['sha256']and (D/md['path']).stat().st_size==md['bytes']
assert seen==expected and count==index['pair_count']==index['expected_pairs']==n*(n-1)//2
print(f'PASS portable semantic evidence: {n} canonical accepted declarations, {count} unique complete-prefix pairs, all source/report/specification hashes, bounded files; human judgments retained verbatim.')
