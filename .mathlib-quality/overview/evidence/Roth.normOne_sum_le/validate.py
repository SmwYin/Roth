#!/usr/bin/env python3
"""Portable read-only declaration84 validator; current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.normOne_sum_le'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==84 and a['completed'] and a['allphases']=='PASS'
assert a['verdict']=='BORDERLINE-needs-human' and a['unresolved']==[] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases and all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N and m['files']
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['unresolved']==[] and {x['label'] for x in v['accepted']}=={'original','raw','consumers'} and v['rejected']==[]
expected={'original':['Roth.normOne_sum_le','MvPolynomial.NormSumAssessment.replay'],'raw':['NormSumRaw.generic','NormSumRaw.direct','NormSumRaw.finiteTriangle','NormSumRaw.genericFinite'],'consumers':['MvPolynomial.NormSumConsumers.normOne_mul_le_inline','MvPolynomial.NormSumConsumers.normOne_det_le_inline','MvPolynomial.NormSumConsumers.normOne_hasseDeriv_le_inline']}
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert len(order)==293 and len({x['name'] for x in order})==293
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
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
 for name in expected[x['label']]:
  assert re.search("'"+re.escape(name)+r"' depends on axioms:",msg),name
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
  assert len(re.findall(r'^import ',s,re.M))==13
  for t in ['[AddZeroClass M]','[Preorder N]','Finsupp.sum_of_support_subset','theorem finiteTriangle','P.coeff Q.coeff','theorem genericFinite']:assert t in s,t
 elif x['label']=='original':
  for t in ['#print '+N,'Roth.normOne_add_le s f','@Finset.le_sum_of_subadditive']:assert t in s,t
  assert 'theorem Roth.normOne_sum_le.' in msg and '[inst_2 : Preorder N]' in msg
 elif x['label']=='consumers':
  arr=re.search(r'let names : Array Lean.Name := #\[.*?\]\n',s,re.S);assert arr and norm(arr.group())==norm(array)
  assert 'names.toList.eraseDups.length' in s and 'unless unique == 293' in s
  assert 'SUM_AUDIT_UNIQUE: 293' in msg and 'SUM_AUDIT_CANONICAL: requested=293; present=293; values=293' in msg
  cs=re.findall(r'SUM_DIRECT_PROOF_CONSUMER: ([^\n]+)',msg);assert cs==['Roth.normOne_mul_le','Roth.normOne_det_le','Roth.normOne_hasseDeriv_le'],cs
  assert 'SUM_AUDIT_NOT_LOADED:' not in msg
  body=s[:s.index('run_cmd do')];assert 'normOne_sum_le' not in body and body.count('Finset.le_sum_of_subadditive normOne')==4
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert load('input-hash-check.json')['all_pass'] and '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');p=R/l['path'];assert sha(p)==l['sha256'] and p.stat().st_size==l['bytes']
f=load('formal-search.json');assert len(f)==14
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  matches=[x for x in f if x['method']==method and (x['form']==form or (form=='abstract' and x['form']=='abstract-retry2'))]
  assert any(not x['result'].get('isError',False) for x in matches),(method,form)
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg'
assert len(load('rg-callers.json')['stdout'].splitlines())==5
qs=[]
for i in range(8):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes_utf8']>0
 assert w['summaries'] and w['urls'] and not w['full_bodies_archived'] and 'response' not in w and 'result' not in w
 assert all('?' not in u for u in w['urls']);qs.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in qs)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==3 and c['occurrence_count']==4 and c['external_to_declaring_file']==0
assert c['native_audit']['unique']==293 and c['native_audit']['values']==293 and c['native_audit']['status']=='PASS'
g=load('generality.json');assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5 and len(g['infrastructure_rows'])==6
assert len(g['future_questions'])==2 and all(x['verified'] and x['status'].startswith('PASS') for x in g['expanded_forms'])
assert load('canonical-entry.json')['name']==N
o=load('canonical-order.json');assert o['index']==84 and o['total']==293 and o['entry']==order[83] and o['source_sha256']==sha(R/'.mathlib-quality/overview/declaration-order.json')
e=load('overview-entry.json');assert e['type'].startswith('∀') and N==e['declaration']
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for phase in phases:assert 'Phase '+phase in s
for t in ['**SMALL**','BORDERLINE-needs-human','MAXIMALLY GENERAL','False-generalization','no Mode B parent re-aim override','293','newly proved','4 occurrences','NOT-COMPOSABLE']:assert t.lower() in s.lower(),t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: declaration84 all phases,current manifest,17 inputs,3 clean native sets,exact293 unique canonical order,14 formal calls,all literature,links,secrets')
