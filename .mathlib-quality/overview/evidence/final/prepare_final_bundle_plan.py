"""Plan a self-contained bounded final evidence bundle; never touches Git.
--require-complete additionally requires all293 and real final build artifacts.
"""
from pathlib import Path
import json,hashlib,sys
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();complete='--require-complete'in sys.argv
I=json.loads((B/'final-completed-inventory-preparation.json').read_text());n=I['completed_count']
if complete:assert n==293
seeds=['final-completed-inventory-preparation.json','final-source-statistics-and-imports-preparation.json','final-canonical-direct-dependencies.json','final-kernel-graph.json','final-inventory-type-repair-plan.json','final-inventory-how-clarification-plan.json','final-inventory-editorial-clarification-plan.json','final-project-dependency-reviewed-resolutions.json','final-completed-action-synthesis-coverage-preparation.json','final-completed-junk-usage-current-coverage-preparation.json','final-completed-yes-mathematical-groups-preparation.json','final-file-summary-preparation.json','final-completed-api-usage-preparation.json','final-completed-definition-api-index-preparation.json','final-completed-action-buckets-preparation.json','final-main-endpoint-source-flow-preparation.json','final-readme-reconciliation-preparation.json','validate_portable_semantic_pairs.py','validate_portable_global_evidence.py','render_partitioned_pair_tables.py','render_whole_overview_preparation.py','FINAL_REPORT_ASSEMBLY_PLAN.md','review/corrected-manifest.json','prepare_completed_inventory.py','prepare_final_indexes.py','prepare_partitioned_pair_evidence.py','validate_partitioned_pair_evidence.py','refresh_action_synthesis_coverage.py','validate_action_synthesis_coverage.py','refresh_junk_current_coverage.py','render_final_inventory_preview.py','render_cross_file_preview.py','render_pairwise_preview.py','prepare_final_bundle_plan.py','refresh_global_preparation.py','GLOBAL_PREPARATION_VALIDATION.json']
if complete:
 audit=json.loads((B/'final-native-panic-audit.json').read_text());assert audit['status']=='PASS'and audit['completed_declaration_count']==293 and audit['accepted_panic_records']==0
 seeds+=['final-native-panic-audit.json']
 seeds+=['final-build-verification.json','prepare_root_native_request.py','execute_root_native_request.js','ROOT_NATIVE_EXECUTOR_ADDENDUM.md','MINIMAL_ORIGINAL_REPLAY_ADDENDUM.md','native-prefix-authorizations.json']
 # Root reconstruction scripts are supporting provenance; their historical local paths
 # are preserved without claiming the generators are portable validators.
 seeds+=[str(p.relative_to(B))for p in sorted(B.glob('root_check*.py'))]
 seeds+=['append_root_reviewed_pairs.py']+[str(p.relative_to(B))for p in sorted(B.glob('review_*_pair_spec.json'))]

# Monolithic whitespace/duplicate aggregate layout is replaced losslessly by bounded JSON+MD.
excluded={'final-completed-cross-module-pairwise-preparation.json','final-completed-theta-pairwise-preparation.json','final-completed-combined-pairwise-preparation.json','FINAL_PAIRWISE_PREVIEW.md'}
paths=set();pending=[B/s for s in seeds];historical=[]
def strings(x):
 if isinstance(x,str):yield x
 elif isinstance(x,list):
  for v in x:yield from strings(v)
 elif isinstance(x,dict):
  for v in x.values():yield from strings(v)
while pending:
 p=pending.pop().resolve()
 if p in paths:continue
 assert p.is_file(),p
 if p.name in excluded:
  historical.append({'source':str(p),'sha256':H(p),'replacement':'pairwise/index.json and bounded module-pair JSON/Markdown, preserving all semantic rows/provenance'});continue
 assert p.stat().st_size<50_000_000,p
 paths.add(p)
 if p.suffix!='.json':continue
 for s in strings(json.loads(p.read_text())):
  if len(s)>400 or '\n'in s or not s.endswith(('.json','.lean.txt','.md','.py','.log','.txt')):continue
  q=Path(s);q=q if q.is_absolute()else B/q
  try:q=q.resolve();q.relative_to(B)
  except ValueError:continue
  if q.is_file()and q not in paths:pending.append(q)
# Partition index and exact rows already preserve historical registry identifiers and hashes.
P=B/'final-pairwise-partitions';m=json.loads((P/'index.json').read_text());assert m['accepted_declaration_count']==n and m['pair_count']==n*(n-1)//2
if complete:assert m['complete_project_pair_coverage']
records=[];seen={}
for p in sorted(paths):
 dest='.mathlib-quality/overview/evidence/final/'+p.name
 assert dest not in seen,(p,seen.get(dest));seen[dest]=p
 records.append({'source':str(p),'destination':dest,'sha256':H(p),'bytes':p.stat().st_size})
for p in sorted(P.rglob('*')):
 if not p.is_file():continue
 assert p.stat().st_size<50_000_000
 dest='.mathlib-quality/overview/evidence/final/pairwise/'+str(p.relative_to(P));assert dest not in seen;seen[dest]=p
 records.append({'source':str(p),'destination':dest,'sha256':H(p),'bytes':p.stat().st_size})
out={'status':'FINAL-BUNDLE-PLAN'if complete else'PREVIEW-ONLY-NOT-FINAL','accepted_declaration_count':n,'copied_to_repository':False,'files':records,'historical_large_layout_replacements':historical,'total_bytes':sum(x['bytes']for x in records),'largest_bytes':max(x['bytes']for x in records),'interpretation':'Raw sources/receipts retain historical paths byte-for-byte. The manifest maps each input to its planned tracked copy. Per-declaration reports/evidence already live in their separately accepted tracked packages. Only explicit portable validators claim operation without private scratch registries.'}
(B/'FINAL_BUNDLE_PLAN.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('PASS scratch bundle plan:',n,'assessments;',len(records),'bounded artifacts;',out['total_bytes'],'bytes total;',out['largest_bytes'],'largest. No tracked files copied.')
