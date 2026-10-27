#!/usr/bin/env python3
"""Portable read-only validation of current artifacts, native receipts and exact canonical order."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.degreeOf_det_hasseDeriv_le'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==99 and a['completed']
assert a['verdict']=='YES-but-generalise-first' and a['allphases']=='PASS'
assert a['unresolved']==[] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases
assert all(v=='PASS' or k=='4.5' and v.startswith('n/a: theorem') for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[]
assert v['production_unchanged'] and len(v['rejected'])==1
assert {x['label'] for x in v['accepted']}=={'original','raw','consumers','candidates'}
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert len(order)==293 and len({x['name'] for x in order})==293
assert load('canonical-snapshot.json')==order
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256']
 assert all(len(z)<=100 for z in s.splitlines()),x['source']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 ss=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and 'success' in z]
 assert ss and all(z['success'] is True for z in ss)
 messages=[]
 for z in ss:
  assert not z.get('partial',False) and not z.get('timed_out',False) and not z.get('failed_dependencies')
  if x['label'] in ['original','consumers']:assert z.get('partial') is False
  ds=z.get('diagnostics',z.get('items',[]))
  assert not [t for t in ds if t.get('severity') in ['error','warning'] or t.get('category')=='sorry']
  msg='\n'.join(t.get('message','') for t in ds);messages.append(msg)
  assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):
   assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 msg='\n'.join(messages)
 if x['label'] in ['original','consumers']:
  start=x['native_region_start_line']
  assert start==({'original':11738,'consumers':11742}[x['label']])
  fresh=[d for z in ss for d in z.get('items',z.get('diagnostics',[])) if d.get('line',0)>=start]
  msg='\n'.join(d.get('message','') for d in fresh)
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if x['label'] in ['raw','candidates']:
  assert r['request']['code']==s and '#check_failure '+N in s
  assert not re.search(r'^import Roth\b',s,re.M)
 if x['label']=='raw':
  assert '[CommRing R]' in s and '[Fintype ι]' in s
  assert 'theorem entry_bound' in s and 'theorem row_bound' in s
 if x['label']=='original':assert '#print '+N in s and 'theorem '+N+'.' in msg
 if x['label']=='candidates':assert '#check @Polynomial.natDegree_det_X_add_C_le' in s
 if x['label']=='consumers':
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]\n',s,re.S)
  assert arrays and norm(arrays[-1])==norm(array)
  assert 'unique == 293' in s and 'DET_DEGREE_AUDIT: requested=293; unique=293' in msg
  assert 'DET_DEGREE_AUDIT_PRESENT: present=293; values=293' in msg
  assert re.findall(r'DET_DEGREE_DIRECT_CONSUMER: ([^\n]+)',msg)==['Roth.exists_det_eq_mul']
  assert 'DET_DEGREE_NOT_LOADED:' not in msg
  code=s[:s.index('run_cmd do')]
  assert not re.search(r'\bdegreeOf_det_hasseDeriv_le\b',code)
  assert '[CommRing R]' in code and 'theorem hasse_generic' in code and 'theorem caller' in code
  assert code.count('exact specialization')==2
for x in v['rejected']:
 assert not x['accepted'] and (D/x['source']).is_file() and (D/x['receipt']).is_file()
 r=load(x['receipt']);ns=list(nodes(r['result'].get('structuredContent',r['result'])))
 assert any(isinstance(z,dict) and (z.get('success') is False or z.get('severity')=='error') for z in ns)
for x in load('inputs.json')+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if 'baseline_sha256' in x:assert x['match'] and x['sha256']==x['baseline_sha256']
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert len(load('inputs.json'))==17 and load('input-hash-check.json')['all_pass']
for p,s in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/Separation.lean','source-callers.lean.txt'),('Roth/HasseDeriv.lean','source-hasse.lean.txt')]:assert sha(R/p)==sha(D/s)
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');assert sha(R/l['path'])==l['sha256']
assert '435:' in (D/'local-literature-excerpt.txt').read_text()
f=load('formal-search.json');assert len(f)==12
for i,x in enumerate(f,1):assert x==load(f'search-{i:02}.json')
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  ms=[x for x in f if x['tool'].endswith('__'+method) and x['form']==form]
  assert ms and any(not x['response'].get('isError',False) for x in ms)
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg' and not x['stderr']
qs=[]
for i in range(6):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['summary'] and w['response_status'] and 'response' not in w and 'result' not in w
 qs.extend(x['q'] for x in w['request'].get('search_query',[]))
 for z in w['locators']:assert '?' not in z['url'] and len(z['title'])<=180
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(site in q for q in qs)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==1 and c['explicit_occurrences']==2
assert c['external_to_file_count']==1 and c['native_audit']['unique']==293
assert c['native_audit']['status']=='PASS'
assert c['native_audit']['direct_proof_consumers']==['Roth.exists_det_eq_mul']
assert re.findall(r'^[^:]+:\d+:',load('rg-callers.json')['stdout'],re.M)==['Roth/Separation.lean:555:','Roth/Separation.lean:558:','Roth/CoeffNorm.lean:245:']
g=load('generality.json');assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5
assert len(g['infrastructure_rows'])==6 and len(g['parameter_rows'])==8
assert all(x['verified'] and x['status']=='PASS' for x in g['expanded_forms'])
c=load('canonical-order.json');assert c['index']==99 and c['entry']==order[98]
assert c['source_sha256']==sha(R/'.mathlib-quality/overview/declaration-order.json')
assert load('canonical-entry.json')['name']==N
p=load('accepted-yes-grouping.json');assert p['completed_count']==98
assert all(x['verdict'].startswith('YES') and x['acceptance']=='PASS' for x in p['accepted_yes'])
e=load('overview-entry.json');assert e['type'].startswith('∀') and e['declaration']==N
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for p in phases:assert 'Phase '+p in s
for term in ['NOT-COMPOSABLE','RESTATE-BEFORE-SHIP','Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean','/generalise','/cleanup']:assert term in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS declaration99: current manifest;17 inputs;4 accepted native sets;1 rejected;293 unique exact order;all phases/searches/links/secrets')
