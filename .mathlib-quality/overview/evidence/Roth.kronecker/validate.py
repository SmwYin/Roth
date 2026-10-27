#!/usr/bin/env python3
"""Portable read-only validation of the current assessment and actual native evidence."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent; R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.kronecker'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
def report():return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==102
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
assert load('canonical-entry.json')==order[101] and order[101]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']';norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert {x['label'] for x in v['accepted']}=={'original','generic','consumers','audit-infrastructure','raw'}
assert len(v['rejected'])==2
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
 if x['label']=='original':assert 'def Roth.kronecker' in msg and 'Field K' in msg
 if x['label']=='generic':
  for t in ['[CommSemiring R]','theorem direct_eq','theorem general_eq','theorem weighted_eq','σ := ℕ']:assert t in s,t
 if x['label']=='consumers':
  region=s
  assert 'namespace KroneckerConsumers' in s and 'end KroneckerConsumers' in region
  assert not re.search(r'\b(?:def|abbrev) kronecker\b|\bRoth.kronecker\b',region)
  assert region.count('MvPolynomial.aeval')>=10
  for c in load('callers.json')['callers']:assert c['name'].split('.')[-1] in region
  assert 'exists_genWronskian_ne_zero' in region
  assert len(next(z for z in v['accepted'] if z['label']=='audit-infrastructure')['expected_axiom_declarations'])==12
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure Roth.kronecker' in s and '#check @MvPolynomial.aeval' in s
 if x['label']=='audit-infrastructure':
  found=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert found and norm(found[-1])==norm(array),'Executed canonical array must match tracked exact order'
  assert 'KRONECKER_AUDIT: requested=293; unique=293' in msg
  assert 'KRONECKER_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[z['message'].split(': ',1)[1] for z in fresh if z.get('message','').startswith('KRONECKER_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']
  expected_source={c['name'] for c in load('callers.json')['callers']}
  expected_source.remove('Roth.derivative_kronHasse_aux')
  expected_source.add('Roth.exists_genWronskian_ne_zero')
  expected_kernel=[]
  for o in order:
   if o['name'] in expected_source:
    expected_kernel.append('_private.'+o['file'][:-5].replace('/','.')+'.0.'+o['name'] if o['visibility']=='private' else o['name'])
  assert actual==expected_kernel and len(actual)==9
  for t in ['#synth CommSemiring (Polynomial ℕ)','#synth Algebra ℕ (Polynomial ℕ)','#synth CoeFun','ULift.{u} ℚ','ULift.{v} (Fin 2)']:assert t in s,t
for x in v['rejected']:assert not x['accepted'] and (D/x['source']).exists() and (D/x['receipt']).exists()
f=load('formal-search.json');assert len(f)==12
for method in ['Finder','Loogle','LeanSearch','Local']:
 rows=[x for x in f if x['method']==method];assert {x['form'] for x in rows}=={'current','literature','abstract'}
 assert all(not x['response'].get('isError',False) for x in rows)
for form in ['current','standard','abstract','callers','inline','local-literature']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for i in range(3):
 w=load('web-'+str(i)+'.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w;queries += [x['q'] for x in w['request']['search_query']]
for n in ['web-direct.json','web-full.json']:
 w=load(n);assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w
assert len(set(queries[:3]))==3
for d in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(d in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json');assert c['named_count']==9 and len(c['callers'])==9 and c['occurrence_count_excluding_def']==17 and c['occurrence_line_count_excluding_def']==15 and c['external_to_declaring_file']==0
assert load('overview-entry.json')['type'].startswith('∀')
s=report().read_text()
for t in ['## Phase 8','ONE-LINER WITH-EXEMPTION','RESTATE-BEFORE-SHIP','NO-mathlib-has-it','COMPOSABLE','LOW']:assert t in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
r=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
print('PASS: full phases, current manifest, exact native sources,17 inputs, canonical293 exact order,9 source callers, secret guard')
