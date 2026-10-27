#!/usr/bin/env python3
"""Portable read-only validation of current manifest, raw receipts and canonical order."""
from pathlib import Path
import json,hashlib,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.normOne_le_card_mul'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==87 and a['completed']
assert a['allphases']=='PASS' and a['verdict']=='NO-mathlib-has-it'
assert not a['unresolved'] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['unresolved']==[] and v['production_unchanged'] and not v['rejected']
assert {x['label'] for x in v['accepted']}=={'original','raw','consumers'}
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert len(order)==293 and len({x['name'] for x in order})==293
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
expected={'original':['Roth.normOne_le_card_mul','MvPolynomial.NormCardAssessment.replay'],'raw':['NormCardRaw.polynomialSupport','NormCardRaw.abstractBound'],'consumers':['MvPolynomial.NormCardConsumers.supportWeakening','MvPolynomial.NormCardConsumers.determinant_inline']}
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256'] and all(len(z)<=100 for z in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 success=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True];assert success
 messages=[]
 for z in success:
  assert not z.get('partial',False) and not z.get('timed_out',False) and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [t for t in ds if t.get('severity') in ['error','warning'] or t.get('category')=='sorry']
  msg='\n'.join(t.get('message','') for t in ds);messages.append(msg)
  assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 msg='\n'.join(messages)
 for name in expected[x['label']]:assert "'"+name+"' depends on axioms:" in msg,name
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s
  assert not re.search(r'^import Roth\b',s,re.M) and len(re.findall(r'^import ',s,re.M))==13
  assert '[Preorder A] [AddLeftMono A]' in s and '∀ d ∈ P.support' in s
 elif x['label']=='original':assert '#print '+N in s and 'theorem Roth.normOne_le_card_mul.' in msg
 else:
  arr=re.search(r'let names : Array Lean.Name := #\[.*?\]\n',s,re.S);assert arr and norm(arr.group())==norm(array)
  assert 'unique == 293' in s and 'CARD_AUDIT_UNIQUE: 293' in msg
  assert 'CARD_AUDIT_CANONICAL: requested=293; present=293; values=293' in msg
  assert re.findall(r'CARD_DIRECT_PROOF_CONSUMER: ([^\n]+)',msg)==['Roth.abs_coeff_det_hasseDeriv_le']
  assert 'CARD_AUDIT_NOT_LOADED:' not in msg and 'normOne_le_card_mul' not in s[:s.index('run_cmd do')]
for x in load('inputs.json')+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if 'baseline_sha256' in x:assert x['match'] and x['sha256']==x['baseline_sha256']
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert len(load('inputs.json'))==17 and load('input-hash-check.json')['all_pass']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');assert sha(R/l['path'])==l['sha256']
f=load('formal-search.json');assert len(f)==12
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  ms=[x for x in f if x['method']==method and x['form']==form];assert len(ms)==1
  assert not ms[0]['response'].get('isError',False) and ms[0]==load(method+'-'+form+'.json')
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg' and not x['stderr']
assert len(load('rg-callers.json')['stdout'].splitlines())==2
qs=[]
for i in range(7):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['summary'] and w['urls'] and 'response' not in w and 'result' not in w
 qs.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in qs),site
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==1 and c['native_audit']['unique']==293 and c['native_audit']['status']=='PASS'
g=load('generality.json');assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5 and len(g['infrastructure_rows'])==6
assert all(x['verified'] and x['status']=='PASS' for x in g['expanded_forms'])
c=load('canonical-order.json');assert c['index']==87 and c['entry']==order[86] and c['source_sha256']==sha(R/'.mathlib-quality/overview/declaration-order.json')
assert load('canonical-entry.json')['name']==N
e=load('overview-entry.json');assert e['type'].startswith('∀') and e['declaration']==N
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for phase in phases:assert 'Phase '+phase in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS declaration87: current manifest,17 fresh inputs,3 clean native sets,exact293 unique order,12 formal calls,all literature,links,secrets')
