#!/usr/bin/env python3
# coding: utf-8
"""Portable read-only validation of completed declaration evidence."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='MvPolynomial.degreeOf_taylor_le'
def read(n):return json.loads((D/n).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=read('assessment.json')
assert a['declaration']==N and a['canonical_index']==69 and a['completed']
assert a['allphases']=='PASS' and a['verdict']=='YES-add-as-is' and a['unresolved']==[]
assert a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' for v in a['phases'].values())
seen=set()
for x in read('copy-manifest.json')['files']:
 report='/mathlibable/' in x['destination']
 p=(D/'report.md' if (D/'report.md').exists() else ROOT/x['destination']) if report else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add('report.md' if report else p.name)
assert {'report.md','assessment.json','overview-entry.json','verification.json','validate.py','formal-search.json'}<=seen
v=read('verification.json');assert v['unresolved']==[]
assert {x['label'] for x in v['accepted']}=={'target','raw','extra'}
allowed={'propext','Classical.choice','Quot.sound'}
for x in v['accepted']:
 p=D/x['source'];s=p.read_text(encoding='utf-8');assert sha(p)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=read(x['receipt']);assert not r['result'].get('isError',False)
 good=[n for n in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(n,dict) and n.get('success') is True]
 assert good
 for n in good:
  assert not n.get('partial',False) and not n.get('timed_out',False) and not n.get('failed_dependencies')
  ds=n.get('diagnostics',n.get('items',[]))
  assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msg='\n'.join(d.get('message','') for d in ds)
  assert all(y not in msg for y in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axs
  for ax in axs:assert {t.strip() for t in ax.split(',') if t.strip()}<=allowed
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s
  assert not re.search(r'^import Roth\b',s,re.M)
  assert all(t in s for t in ['coefficientCriterion','shiftCriterion','aeval_natDegree_le','Polynomial.natDegree_taylor Q r'])
 else:assert r['request']['file_path'].endswith('.lean')
 if x['label']=='extra':
  assert all(t in s for t in ['taylor_neg_taylor','DegreeTaylorAssessment.replay','supportBridge','weight_le_card','fail_if_success'])
inputs=read('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for src,dst in v['source_links'].items():assert sha(ROOT/src)==sha(D/dst)
assert read('input-hash-check.json')['all_pass']
f=read('formal-search.json');assert len(f)==12
for m in ['Finder','Loogle','LeanSearch','local']:
 assert {x['form'] for x in f if x['method']==m}=={'current','literature','abstract'}
assert all(not x['response'].get('isError',False) for x in f)
for form in ['current','literature','abstract']:assert read('rg-'+form+'.json')['exit_code'] in [0,1]
assert read('rg-full-name.json')['exit_code']==1 and read('callers.json')['explicit_count']==1
ws=[read('web'+str(i)+'-metadata.json') for i in range(4)]
qs=[q['q'] for w in ws for q in w['request'].get('search_query',[])]
assert len(set(qs[:3]))==3
for domain in ['ncatlab.org','stacks.math.columbia.edu','mathoverflow.net','arxiv.org']:
 assert any('site:'+domain in q for q in qs)
for w in ws:
 assert len(w['response_sha256'])==64 and w['response_bytes']>0
 for u in w['urls']:assert '?' not in u and '#' not in u
group=read('accepted-yes-grouping.json');assert len(group)==4
assert all(x['verdict']=='YES-add-as-is' for x in group)
p=D/'report.md' if (D/'report.md').exists() else ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text(encoding='utf-8')
for t in ['Phase 0','Phase 1','Phase 2','Phase 3','4a','4c','4.5','4.6','Phase 5','5.5','6.0','Phases 7','YES-add-as-is','Mathlib/Algebra/MvPolynomial/Taylor.lean']:
 assert t in s,t
for target in re.findall(r'\]\((\.\./evidence/[^)]+)\)',s):assert (D/Path(target).name).is_file(),target
assert len(read('overview-entry.json')['type'])>150
print(json.dumps(dict(status='PASS',declaration=N,manifest_artifacts=len(seen),native_accepted=3,production_inputs=17)))
