#!/usr/bin/env python3
"""Read-only portable assessment validation; current manifest is authoritative."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.kroneckerExp'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
def report():return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==103
assert a['completed'] and a['allphases']=='PASS' and a['verdict']=='NO-mathlib-has-it'
assert a['unresolved']==[] and a['root_acceptance'] in ['pending','PASS'] and a['production_unchanged']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS' for x in a['phases'].values())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
xs=load('inputs.json');assert len(xs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in xs)
for x in xs+load('source-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==load('canonical-snapshot.json') and len(order)==293 and len({x['name'] for x in order})==293
assert load('canonical-entry.json')==order[102] and order[102]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']';norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert {x['label'] for x in v['accepted']}=={'original','generic','consumers','raw','audit-final'} and v['rejected']==[]
for x in v['accepted']:
 s=(D/x['source']).read_text();assert sha(D/x['source'])==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 rs=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and 'success' in z]
 assert rs and all(z['success'] for z in rs)
 ds=[]
 for z in rs:
  assert not z.get('partial',False) and not z.get('timed_out',False) and not z.get('failed_dependencies')
  if x['label']!='raw':assert z.get('partial') is False
  ds.extend(z.get('items',z.get('diagnostics',[])))
 assert not [z for z in ds if z.get('severity') in ['error','warning'] or z.get('category')=='sorry']
 txt='\n'.join(z.get('message','') for z in ds)
 assert not any(t in txt for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',txt):
  assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 fresh=ds if x['label']=='raw' else [z for z in ds if z.get('line',0)>=x['native_region_start_line']]
 msg='\n'.join(z.get('message','') for z in fresh)
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if x['label']=='original':assert 'def Roth.kroneckerExp' in msg and 'Field K' not in msg
 if x['label']=='generic':
  for t in ['Finsupp.weight_eq_sum','theorem target_eq','theorem function_eq','theorem linearCombination_eq','theorem additive']:assert t in s,t
  assert len(x['expected_axiom_declarations'])==6
 if x['label']=='consumers':
  assert 'namespace Roth.KroneckerExpConsumers' in s
  assert not re.search(r'\b(?:def|abbrev) kroneckerExp\b|\bRoth.kroneckerExp\b|\bkroneckerExp\b',s)
  assert s.count('Finsupp.weight')>=5 and 'Finsupp.weight_eq_sum' in s
  for c in load('callers.json')['callers']:assert c.split('.')[-1] in s
  assert 'exists_genWronskian_ne_zero' in s and len(x['expected_axiom_declarations'])==12
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure Roth.kroneckerExp' in s and 'theorem finite_sum_eq' in s and 'Finsupp.weight_eq_sum' in s
 if x['label']=='audit-final':
  found=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert len(found)==1 and norm(found[0])==norm(array),'Exactly one executed canonical array, tracked order'
  assert 'KRONECKER_EXP_AUDIT: requested=293; unique=293' in msg
  assert 'KRONECKER_EXP_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[z['message'].split(': ',1)[1] for z in fresh if z.get('message','').startswith('KRONECKER_EXP_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['Roth.kronecker_monomial','Roth.kroneckerExp_injOn','Roth.coeff_kronecker','Roth.kronecker_eq_zero_iff']
  for t in ['#synth AddCommMonoid ℕ','#synth Module ℕ ℕ','#synth CoeFun','ULift.{v} (Fin 2)','Finsupp.weight (R := ℕ)','theorem reducible']:assert t in s,t
for x in v['superseded']:assert (D/x['source']).exists() and (D/x['receipt']).exists()
for x in v['preparation_rejected']:assert (D/x['source']).exists() and x['reason']
f=load('formal-search.json');assert len(f)==12
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 rows=[x for x in f if x['method']==method];assert {x['form'] for x in rows}=={'current','standard','abstract'}
 assert all('result' in x or 'error' in x for x in rows)
assert not load('formal-search-retry.json')['result'].get('isError',False)
for form in ['current','standard','abstract','callers','inline','local-literature']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for i in range(3):
 w=load('web-'+str(i)+'.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w;queries += [x['q'] for x in w['request']['search_query']]
for n in ['web-direct.json','web-stacks.json','web-mo.json']:
 w=load(n);assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w
assert len(set(queries[:3]))==3
for d in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(d in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json');assert c['named_count']==3 and len(c['callers'])==3 and c['occurrence_count_excluding_def_doc']==6 and c['occurrence_line_count_excluding_def_doc']==6 and c['external_to_declaring_file']==0
assert load('overview-entry.json')['type'].startswith('∀')
s=report().read_text()
for t in ['## Phase 8','ONE-LINER WITH-EXEMPTION','RESTATE-BEFORE-SHIP','NO-mathlib-has-it','COMPOSABLE','LOW','Roth.weight']:assert t in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
r=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
print('PASS: all phases, current manifest, native exact sources,17 inputs, canonical293 exact order,3 source callers/4 value consumers, secret guard')
