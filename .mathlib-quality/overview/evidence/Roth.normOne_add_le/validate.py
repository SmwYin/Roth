#!/usr/bin/env python3
"""Portable read-only validator of the current declaration 82 evidence inventory."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.normOne_add_le'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==82 and a['completed'] and a['allphases']=='PASS'
assert a['verdict']=='BORDERLINE-needs-human' and a['unresolved']==[] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases and all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N and m['files']
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['unresolved']==[] and {x['label'] for x in v['accepted']}=={'original','target','raw','consumers-generality','metric'}
assert len(v['rejected'])==1
expected={'original':['Roth.normOne_add_le','MvPolynomial.NormTriangleAssessment.replay'],'target':['MvPolynomial.NormAddAssessment.direct','MvPolynomial.NormAddAssessment.generic'],'raw':['NormAddRaw.generic','NormAddRaw.direct','NormAddRaw.finiteTriangle'],'consumers-generality':['MvPolynomial.NormAddGenerality.genericNonnegativeAtZero','MvPolynomial.NormAddGenerality.supportCard','MvPolynomial.NormAddConsumers.sumBound'],'metric':['MvPolynomial.NormAddMetric.zeroDistance','MvPolynomial.NormAddMetric.addDistance','MvPolynomial.NormAddMetric.triangle']}
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 successes=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True];assert successes
 messages=[]
 for z in successes:
  assert z.get('partial',False) is False and not z.get('timed_out',False) and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [q for q in ds if q.get('severity') in ['error','warning'] or q.get('category')=='sorry']
  msg='\n'.join(q.get('message','') for q in ds);messages.append(msg)
  assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axs
  for ax in axs:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 msg='\n'.join(messages)
 for name in expected[x['label']]:assert name in msg,name
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
  assert len(re.findall(r'^import ',s,re.M))==13
  for t in ['[AddZeroClass M]','[Preorder N]','Finsupp.sum_of_support_subset','theorem finiteTriangle','P.coeff Q.coeff']:assert t in s,t
 elif x['label']=='target':
  for t in ['#print '+N,'Finsupp.sum_of_support_subset','P.coeff + Q.coeff','[Preorder N]','abs_add_le']:assert t in s,t
 elif x['label']=='consumers-generality':
  assert 'NormAddAssessment.direct s f' in s and 'normOne_add_le s f' not in s
  assert 'genericNonnegativeAtZero' in s and 'ite_eq_left' in s and '(hzero : ∀ i, 0 ≤ size i 0)' in s
  assert 'ADD_AUDIT_CANONICAL: requested=293; present=293; values=293' in msg
  consumers=re.findall(r'ADD_DIRECT_PROOF_CONSUMER: ([^\n]+)',msg);assert consumers==['Roth.normOne_sum_le'],consumers
  assert 'ADD_AUDIT_NOT_LOADED:' not in msg
 elif x['label']=='metric':
  for t in ['#synth MetricSpace','Finsupp.sum_mapRange_index','theorem zeroDistance','theorem addDistance','dist_triangle','#check_failure (inferInstance : SeminormedAddCommGroup']:assert t in s,t
  assert 'Finsupp.instMetricSpaceWithLpOfNNReal' in msg and 'failed to synthesize instance of type class\n  SeminormedAddCommGroup' in msg
for x in v['rejected']:
 assert (D/x['source']).is_file() and (D/x['receipt']).is_file() and x['reason']
 r=load(x['receipt']);ds=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('severity')=='warning'];assert ds
 assert any('deprecated' in z.get('message','').lower() for z in ds)
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert load('input-hash-check.json')['all_pass'] and '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');p=R/l['path'];assert sha(p)==l['sha256'] and p.stat().st_size==l['bytes']
f=load('formal-search.json');assert len(f)==14
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  matches=[x for x in f if x['method']==method and (x['form']==form or (form=='current' and x['form']=='current-retry2'))]
  assert any(not x['result'].get('isError',False) for x in matches),(method,form)
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg'
assert len(load('rg-callers.json')['stdout'].splitlines())==2
qs=[]
for i in range(8):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes_utf8']>0
 assert w['summaries'] and w['urls'] and not w['full_bodies_archived'] and 'response' not in w
 assert all('?' not in u for u in w['urls']);qs.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in qs)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==1 and c['occurrence_count']==1 and c['external_to_declaring_file']==0
assert c['native_audit']['direct_consumers']==['Roth.normOne_sum_le'] and c['native_audit']['values']==293
g=load('generality.json');assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5 and len(g['infrastructure_rows'])==6
assert len(g['future_questions'])==3 and all(x['verified'] for x in g['expanded_forms'])
assert load('canonical-entry.json')['name']==N
o=load('canonical-order.json');assert o['index']==82 and o['total']==293 and o['entry']['name']==N
e=load('overview-entry.json');assert e['type'].startswith('∀') and N==e['declaration']
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for phase in phases:assert 'Phase '+phase in s
for t in ['**SMALL**','BORDERLINE-needs-human','MAXIMALLY GENERAL','False-generalization','nonnegative-at-zero','no Mode B parent re-aim override','not definitional','293','new bridge','one explicit']:assert t.lower() in s.lower(),t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/validate_canonical_audit.py'),str(D)],check=True)
print('PASS: complete declaration 82, current manifest,17 inputs,5 native sets,14 formal calls,all literature channels,sole caller293-value audit,links,secrets')
