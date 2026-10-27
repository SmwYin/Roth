#!/usr/bin/env python3
"""Read-only, portable validation: current integration manifest is authoritative."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.kronecker_monomial'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
def report():return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==107 and a['verdict']=='NO-mathlib-has-it'
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS'] and a['production_unchanged']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
assert a['parent_reaim']['analogous_law']=='MvPolynomial.aeval_monomial'
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
xs=load('inputs.json');assert len(xs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in xs)
baseline=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
assert set(x['path'] for x in xs)==set(baseline['sources_and_pins'])
for x in xs+load('source-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==load('canonical-snapshot.json') and len(order)==293 and len({x['name'] for x in order})==293
assert load('canonical-entry.json')==order[106] and order[106]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert {x['label'] for x in v['accepted']}=={'original','probes','raw','consumer','audit','bridge'}
assert set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'}
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
 if x['label']=='original':
  assert '@Roth.kronecker_monomial' in msg and 'Field K' in msg and 'Fintype σ' in msg
  assert 'theorem Roth.kronecker_monomial' in msg
 if x['label']=='probes':
  assert not re.search(r'\bkronecker_monomial\b',s)
  assert 'theorem target' in s and 'aeval_monomial' in s and '← Finset.prod_pow_eq_pow_sum' in s
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure Roth.kronecker_monomial' in s and '[CommSemiring R]' in s
  assert 'theorem abstract_monomial' in s and 'theorem weighted_monomial' in s
  assert 'aeval_monomial g d a' in s and 'Finsupp.weight w d' in s
  assert '[Fintype σ]' not in s
 if x['label']=='consumer':
  assert not re.search(r'\bkronecker_monomial\b',s)
  assert 'theorem replay' in s and 'have hmon' in s
  assert 'simp_rw [hmon, Polynomial.coeff_C_mul_X_pow]' in s
  assert 'kroneckerExp_injOn hk' in s
 if x['label']=='bridge':
  assert 'theorem exp_eq' in s and 'Finsupp.weight_eq_sum' in s
  assert 'theorem map_eq' in s and ':= rfl' in s
 if x['label']=='audit':
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert len(arrays)==1 and norm(arrays[0])==norm(array),'Exact executed canonical293 order'
  assert 'KRONECKER_MONOMIAL_AUDIT: requested=293; unique=293' in msg
  assert 'KRONECKER_MONOMIAL_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[z['message'].split(': ',1)[1] for z in fresh if z.get('message','').startswith('KRONECKER_MONOMIAL_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['Roth.coeff_kronecker']
assert len(v['rejected'])==1
for x in v['rejected']:
 assert (D/x['source']).exists() and (D/x['receipt']).exists() and x['reason']
 rr=load(x['receipt']);assert any(z.get('severity')=='error' for z in nodes(rr) if isinstance(z,dict))
f=load('formal-search.json');assert len(f)==12
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 rows=[x for x in f if x['method']==method];assert {x['form'] for x in rows}=={'current','standard','abstract'}
 assert all('result' in x or 'error' in x for x in rows)
for form in ['current','standard','abstract','callers','inline','local-literature']:
 assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for name in ['web-0.json','web-1.json','web-2.json','web-direct.json','web-supplement.json']:
 w=load(name);assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary'] and w['status']
 assert 'response' not in w and 'result' not in w
 assert all(len(z['title'])<=200 and '\n' not in z['title'] for z in w['locators'])
 queries += [z['q'] for z in w['request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for domain in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(domain in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json');assert c['named_count']==1 and c['callers']==['Roth.coeff_kronecker'] and c['external_to_declaring_file']==0
assert c['occurrence_count_excluding_def_doc']==1
assert load('overview-entry.json')['type'].startswith('∀') and 'Field K' in load('overview-entry.json')['type']
s=report().read_text()
for t in ['## Phase 8','NO-mathlib-has-it','BORDERLINE','SMALL','RESTATE-BEFORE-SHIP','293','MathOverflow','nCatLab','arXiv']:
 assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
r=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
print('PASS: completed phases,17 fresh inputs,6 accepted native proofs/audit, exact canonical293, sole caller, all search methods/channels, current manifest and secret guard')
