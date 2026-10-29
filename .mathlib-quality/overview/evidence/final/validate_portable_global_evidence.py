#!/usr/bin/env python3
"""Validate copied review evidence using only repository and final evidence directory.
Usage: python3 validate_portable_global_evidence.py REPOSITORY EVIDENCE [--require-complete]
Hashes/coverage/actual native receipts are checked; human mathematical judgments remain review.
"""
from pathlib import Path
import collections,hashlib,json,re,sys
R=Path(sys.argv[1]).resolve();D=Path(sys.argv[2]).resolve();H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda n:json.loads((D/n).read_text())
I=load('final-completed-inventory-preparation.json');rows=I['rows'];n=len(rows);order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());names=[x['name']for x in order]
assert n==I['completed_count']and[x['declaration']for x in rows]==names[:n]
if '--require-complete'in sys.argv:assert n==293
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())['sources_and_pins'];assert len(base)==17
for p,x in base.items():assert H(R/p)==x['sha256']
for x in rows:
 source='\n'.join((R/x['file']).read_text().splitlines()[x['start_line']-1:x['end_line']]);assert hashlib.sha256(source.encode()).hexdigest()==x['source_sha256']
 assert all(x[k]for k in ['type','what','how','hypotheses'])and x['type']not in ['def','lemma','theorem']
 report=R/x['report'];assert H(report)==x['report_sha256']
 a=json.loads((R/x['acceptance']).read_text());assert a['status']=='PASS'and a['report_sha256']==x['report_sha256']
 for f,h in a['evidence_sha256'].items():assert H((R/x['acceptance']).parent/f)==h
G=load('final-kernel-graph.json');assert G['canonical_count']==G['canonical_unique']==G['kernel_values']==293
for p,x in G['sources_and_pins'].items():assert H(R/p)==x['sha256']
for key in ['receipt','source']:assert H(D/Path(G[key]).name)==G[key+'_sha256']
r=load(Path(G['receipt']).name);z=r['result']['structuredContent'];z=z.get('result',z)
assert z['success']and z['partial']is False and not z['timed_out']and not z['failed_dependencies']
assert not[x for x in z['items']if x['severity']in ['error','warning']]
messages=[x['message']for x in z['items']]
assert 'FINAL_GRAPH_COMPLETE: names=293; unique=293; values=293'in messages
for marker,key,count in [('FINAL_BODY_EDGE: ','body_edges',740),('FINAL_TYPE_EDGE: ','type_edges',291)]:
 parsed=[m[len(marker):].split(' <- ')for m in messages if m.startswith(marker)];assert parsed==G[key]and len(parsed)==count==G[key[:-1]+'_count']
def canonical(raw):
 if raw in names:return raw
 options=[x['name']for x in order if x['visibility']=='private'and raw.startswith('_private.'+x['file'][:-5].replace('/','.')+'.')and raw.endswith('.'+x['name'])]
 assert len(options)==1,(raw,options);return options[0]
C=load('final-canonical-direct-dependencies.json');assert C['provenance_sha256']==H(D/C['provenance']);assert[x['canonical_name']for x in C['declarations']]==names
for kind,key in [('body','body_edges'),('type','type_edges')]:
 edges={(canonical(a),canonical(b))for a,b in G[key]};got={(x['canonical_name'],b)for x in C['declarations']for b in x[kind+'_dependencies']};assert edges==got
S=load('final-source-statistics-and-imports-preparation.json');assert S['total_files']==14 and S['physical_lines']==4874 and S['canonical_written_declarations']==293
for x in S['rows']:
 p=R/x['file'];assert H(p)==x['sha256']
repair=load('final-inventory-type-repair-plan.json');assert len(repair['kind_only_inventory_entries'])==14
for x in repair['kind_only_inventory_entries']:
 a=x['accepted_full_binder_signature'];assert H(D/Path(a['receipt']).name)==a['receipt_sha256']
 receipt=load(Path(a['receipt']).name);z=receipt['result']['structuredContent'];z=z.get('result',z);assert z['success']and z['partial']is False
 assert a['type']in[m['message'].split(': ',1)[-1]for m in z['items']]
 assert next(y for y in rows if y['declaration']==x['declaration'])['type']==a['type']
A=load('final-completed-action-synthesis-coverage-preparation.json')
assert A['completed_count']==n and not A['unreconciled_completed']
assert [x['declaration']for x in A['rows']]==[x['declaration']for x in rows]
for x,y in zip(A['rows'],rows):
 for k in ['canonical_index','declaration','verdict','report','report_sha256']:assert x[k]==y[k]
for a in A['artifacts']:assert H(D/a['source'])==a['sha256']
assert A['public_action_syntheses']==sum(x['visibility']=='public'for x in rows)
assert A['private_prefilter_dispositions']==sum(x['visibility']=='private'for x in rows)
Y=load('final-completed-yes-mathematical-groups-preparation.json');assigned=[x['declaration']for g in Y['groups']for x in g['assessments']]
yes={x['declaration']for x in rows if x['verdict'].startswith('YES-')}
assert Y['completed_count']==n and not Y['unassigned_later_yes']and len(assigned)==len(set(assigned))and set(assigned)==yes
for g in Y['groups']:
 for a in g['assessments']:assert next(x['report_sha256']for x in rows if x['declaration']==a['declaration'])==a['report_sha256']
J=load('final-completed-junk-usage-current-coverage-preparation.json');assert J['completed_count']==n
U=load('final-completed-api-usage-preparation.json');assert H(D/J['usage_provenance']['source'])==J['usage_provenance']['sha256']
zero={x['declaration']for x in U['rows']if x['has_no_source_or_direct_body_or_type_consumers']}
assert J['zero_consumer_count']==len(J['reviewed_zero_consumer_rows'])==len(zero)and{x['declaration']for x in J['reviewed_zero_consumer_rows']}==zero
assert H(D/J['base_review']['source'])==J['base_review']['sha256']
for x in J['reviewed_zero_consumer_rows']:
 assert x['interpretation']and next(y['report_sha256']for y in rows if y['declaration']==x['declaration'])==x['report_sha256']
 if x.get('root_disposition_source'):assert H(D/x['root_disposition_source'])==x['root_disposition_sha256']
for p,h in J['source_hashes'].items():assert H(R/p)==h
if '--require-complete' in sys.argv:
 build=load('final-build-verification.json')
 for record,command in [(build,['lake','build']),(build['lean_eval'],['lake','build','Roth.LeanEval'])]:
  assert record['command']==command and record['exit_code']==0
  log=D/Path(record['log']).name
  assert log.is_file() and H(log)==record['log_sha256']
  assert 'Build completed successfully' in log.read_text(),log
 print('PASS portable final literal builds: lake build and lake build Roth.LeanEval; exact copied successful log hashes')
print(f'PASS portable global evidence: {n} accepted reports/all evidence hashes, fresh17, exact whole293 native graph/references,14 fullbinder repairs, action/YES groups and explicit junk/usage coverage. Semantic judgments remain independently reviewed, not machine-proved here.')
