#!/usr/bin/env python3
"""Read-only validator; authoritative current manifest, portable scratch/integrated layout."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.diag_eq_sum'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==91 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human' and a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases and all(v=='PASS' or k=='4.5' and v.startswith('n/a: theorem') for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert {x['label'] for x in v['accepted']}=={'original','raw','consumers'} and len(v['rejected'])==2
for x in v['rejected']:
 assert x['accepted'] is False and sha(D/x['source'])==x['source_sha256']
 assert (D/x['receipt']).is_file() and x['reason']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert len(order)==293 and len({x['name'] for x in order})==293
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']';norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256']
 assert all(len(z)<=100 for z in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 success=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True]
 assert success
 messages=[]
 for z in success:
  assert not z.get('partial',False) and not z.get('timed_out',False) and not z.get('failed_dependencies')
  if x['label']!='raw':assert z.get('partial') is False
  ds=z.get('diagnostics',z.get('items',[]));assert not [t for t in ds if t.get('severity') in ['error','warning'] or t.get('category')=='sorry']
  msg='\n'.join(t.get('message','') for t in ds);messages.append(msg)
  assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 msg='\n'.join(messages)
 for name in x['expected_axiom_declarations']:assert "'"+name+"' depends on axioms:" in msg,name
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
  assert 'theorem existingExpansion' in s and '[MvPolynomial.aeval_def, Finset.prod_pow_eq_pow_sum,' in s
  assert '@eval₂_eq' in msg and '@Polynomial.C_mul_X_pow_eq_monomial' in msg
 elif x['label']=='original':assert '#print '+N in s and 'theorem Roth.diag_eq_sum.' in msg
 else:
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]\n',s,re.S);assert arrays and norm(arrays[-1])==norm(array)
  assert 'unique == 293' in s and 'DIAG_SUM_AUDIT_UNIQUE: 293' in msg
  assert 'DIAG_SUM_AUDIT: requested=293; present=293; values=293' in msg
  assert re.findall(r'DIAG_SUM_DIRECT_PROOF_CONSUMER: ([^\n]+)',msg)==['Roth.abs_coeff_diag_le','Roth.natDegree_diag_le']
  assert 'DIAG_SUM_AUDIT_NOT_LOADED:' not in msg
for x in load('inputs.json')+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if 'baseline_sha256'in x:assert x['match'] and x['sha256']==x['baseline_sha256']
 if 'archive'in x:assert sha(D/x['archive'])==x['sha256']
assert len(load('inputs.json'))==17 and load('input-hash-check.json')['all_pass']
assert sha(R/'Roth/CoeffNorm.lean')==sha(D/'source-module.lean.txt') and '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');assert sha(R/l['path'])==l['sha256'] and 1449 in l['line_numbers']
f=load('formal-search.json');assert len(f)==12
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  ms=[x for x in f if x['method']==method and x['form']==form];assert len(ms)==1 and not ms[0]['response'].get('isError',False)
  assert ms[0]==load(method+'-'+form+'.json')
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg' and not x['stderr']
qs=[]
for i in range(19):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w
 qs.extend(z['q'] for z in w['request'].get('search_query',[]))
 for z in w['locators']:assert '?' not in z['url'] and len(z['title'])<=180
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert sum(site in q for q in qs)>=3
assert sum('site:ncatlab.org ' in q or 'site:ncatlab.org/ncatlab ' in q for q in qs)>=3
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==2 and c['explicit_occurrences']==2 and c['external_to_file_count']==0
assert c['native_audit']['unique']==293 and c['native_audit']['status']=='PASS'
g=load('generality.json');assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5 and len(g['infrastructure_rows'])==6
assert all(x['verified'] and x['status']=='PASS' for x in g['expanded_forms'])
c=load('canonical-order.json');assert c['index']==91 and c['entry']==order[90] and c['source_sha256']==sha(R/'.mathlib-quality/overview/declaration-order.json')
assert load('canonical-entry.json')['name']==N
assert load('accepted-yes-grouping.json')['completed_count']==90
assert all(x['verdict'].startswith('YES') and x['acceptance']=='PASS' for x in load('accepted-yes-grouping.json')['accepted_yes'])
e=load('overview-entry.json');assert e['type'].startswith('∀') and e['declaration']==N
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for phase in phases:assert 'Phase '+phase in s
assert 'trivial simp composition' in s and all(f'{i}. ' in s for i in [1,2,3])
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS declaration91: current manifest;17 inputs;3 native sets;2 rejected;exact293 unique order;all phases/searches/links/secrets')
