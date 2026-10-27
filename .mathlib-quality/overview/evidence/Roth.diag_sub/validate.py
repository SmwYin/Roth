#!/usr/bin/env python3
"""Read-only portable validator; checks current manifest in scratch or integrated layout."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.diag_sub'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==95
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['verdict']=='NO-mathlib-has-it' and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS']
ph={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==ph
assert all(v=='PASS' or k=='4.5' and v.startswith('n/a: theorem') for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[]
assert v['production_unchanged'] and len(v['rejected'])==1
assert {x['label'] for x in v['accepted']}=={'original','raw','consumers'}
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
 assert all(len(z)<=100 for z in s.splitlines())
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
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s and '#check_failure Roth.diag' in s
  assert not re.search(r'^import Roth\b',s,re.M)
  assert '[CommRing R]' in s and '[Algebra R A]' in s and '[AddGroup A]' in s
  assert 'SubtractionMonoid H]' in msg and '[AddMonoidHomClass F G H]' in msg
 if x['label']=='original':assert '#print '+N in s and 'theorem Roth.diag_sub.' in msg
 if x['label']=='consumers':
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]\n',s,re.S)
  assert arrays and norm(arrays[-1])==norm(array)
  assert 'unique == 293' in s and 'DIAG_SUB_AUDIT_UNIQUE: 293' in msg
  assert 'DIAG_SUB_AUDIT: requested=293; present=293; values=293' in msg
  assert re.findall(r'DIAG_SUB_DIRECT_PROOF_CONSUMER: ([^\n]+)',msg)==['Roth.eval_hasseDeriv_sub_eq_zero']
  assert 'DIAG_SUB_AUDIT_NOT_LOADED:' not in msg
  start=s.index('namespace MvPolynomial.DiagSubConsumers');end=s.index('run_cmd do',start)
  assert not re.search(r'\bdiag_sub\b',s[start:end]) and 'have hdiag :' in s[start:end]
  assert 'map_sub (MvPolynomial.aeval fun _ ↦ Polynomial.X) P Q' in s
  assert 'simp [map_sub, diag, Polynomial.sub_modByMonic, hdiag]' in s
for x in v['rejected']:
 assert not x['accepted'] and (D/x['source']).is_file() and (D/x['receipt']).is_file()
 r=load(x['receipt']);ns=list(nodes(r['result'].get('structuredContent',r['result'])))
 assert any(isinstance(z,dict) and (z.get('success') is False or z.get('severity')=='error') for z in ns)
for x in load('inputs.json')+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if 'baseline_sha256' in x:assert x['match'] and x['sha256']==x['baseline_sha256']
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert len(load('inputs.json'))==17 and load('input-hash-check.json')['all_pass']
for p,n in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/MainLemma.lean','source-caller.lean.txt')]:assert sha(R/p)==sha(D/n)
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');assert sha(R/l['path'])==l['sha256']
f=load('formal-search.json');assert len(f)==12
for i,x in enumerate(f,1):assert x==load(f'search-{i:02}.json')
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  ms=[x for x in f if x['tool'].endswith('__'+method) and x['form']==form]
  assert ms and any(not x['response'].get('isError',False) for x in ms)
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg' and not x['stderr']
qs=[]
for i in range(5):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['summary'] and w['response_status'] and 'response' not in w and 'result' not in w
 qs.extend(x['q'] for x in w['request'].get('search_query',[]))
 for z in w['locators']:assert '?' not in z['url'] and len(z['title'])<=180
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in qs)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==1 and c['external_to_file_count']==1
assert c['native_audit']['unique']==293 and c['native_audit']['direct_proof_consumers']==['Roth.eval_hasseDeriv_sub_eq_zero']
assert re.findall(r'^[^:]+:\d+:',load('rg-callers.json')['stdout'],re.M)==['Roth/CoeffNorm.lean:199:','Roth/MainLemma.lean:408:']
g=load('generality.json');assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5 and len(g['infrastructure_rows'])==6
assert all(x['verified'] and x['status']=='PASS' for x in g['expanded_forms'])
c=load('canonical-order.json');assert c['index']==95 and c['entry']==order[94]
assert c['source_sha256']==sha(R/'.mathlib-quality/overview/declaration-order.json')
assert load('canonical-entry.json')['name']==N
p=load('accepted-yes-grouping.json');assert p['completed_count']==94
assert all(x['verdict'].startswith('YES') and x['acceptance']=='PASS' for x in p['accepted_yes'])
assert p['parent_diag'][0]['verdict']=='NO-composable-from-mathlib'
e=load('overview-entry.json');assert e['type'].startswith('∀') and e['declaration']==N
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for p in ph:assert 'Phase '+p in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS declaration95: current manifest;17 inputs;3 accepted native sets;1 rejected preserved;exact293 unique order;all phases/searches/links/secrets')
