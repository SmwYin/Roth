from pathlib import Path
import json,re,hashlib
base=Path(__file__).resolve().parent
report_path=base/'report.md'
if not report_path.exists():
 report_path=base.parent.parent/'mathlibable/MvPolynomial.hasseDeriv.md'
report=report_path.read_text()
prefix='../evidence/MvPolynomial.hasseDeriv/'
links=re.findall(r'\]\(([^)]+)\)',report)
checks=[]
for link in links:
 if link.startswith(prefix):
  rel=link[len(prefix):]
  checks.append(dict(link=link,exists=(base/rel).is_file()))
assert all(x['exists'] for x in checks),[x for x in checks if not x['exists']]
callers=json.load(open(base/'evidence/call-sites.json'))
assert len(callers['rows'])==92
assert len({r['caller'] for r in callers['rows']})==59
assert len([r for r in callers['rows'] if r['file']!='Roth/HasseDeriv.lean'])==72
assert all(r['caller'] for r in callers['rows'])
assert len(json.load(open(base/'evidence/literature-queries.json')))==16
baseline=json.load(open(base/'evidence/baseline-hash-verification.json'))
assert baseline['passed']==baseline['total']==17
probes=list((base/'probes').glob('*.lean'))
for p in probes:
 text=p.read_text()
 assert not re.search(r'\b(?:sorry|native_decide|unsafe)\b|^\s*axiom\s|set_option\s+(?:maxHeartbeats|maxRecDepth)',text,re.M),p
mathlib=(base/'probes/MathlibOnly.lean').read_text()
assert not re.search(r'^import\s+Roth',mathlib,re.M)
for name in ['target-risk-lsp.json','mathlib-only-lsp.json']:
 raw=json.load(open(base/'evidence'/name))['result']['structuredContent']['result']
 assert raw['success'] and not raw['partial'] and not raw['timed_out']
 assert not raw['failed_dependencies']
 assert not [x for x in raw['items'] if x['severity']=='error']
assert 'PENDING' not in report
result=dict(compiler_receipts_complete_and_error_free=True,local_links=len(checks),all_local_links_resolve=True,caller_counts_match=True,literature_query_count=16,baseline_hashes_match=17,scratch_no_new_axioms_sorry_native_or_limit_raises=True,mathlib_only_no_project_imports=True,completed_flag=json.load(open(base/'assessment.json'))['completed'])
json.dump(result,open(base/'validation.json','w'),indent=2)
print(json.dumps(result,indent=2))
