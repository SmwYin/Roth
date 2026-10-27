#!/usr/bin/env python3
"""Read-only validation of scratch or integrated current evidence (not historical manifests)."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
N='Roth.genWronskian_eq_zero_of_not_linearIndependent'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
def report():
 return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==106 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human' and a['allphases']=='PASS'
assert a['unresolved']==[] and a['root_acceptance'] in ['pending','PASS'] and a['production_unchanged']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS' for x in a['phases'].values())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
inputs=load('inputs.json');assert len(inputs)==17
shared=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
assert set(x['path'] for x in inputs)==set(shared['sources_and_pins'])
for x in inputs:
 assert x['match'] and x['sha256']==x['baseline_sha256']==shared['sources_and_pins'][x['path']]['sha256']
for x in inputs+load('source-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 if 'copy' in x:assert sha(D/x['copy'])==x['sha256']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert load('canonical-snapshot.json')==order and len(order)==293 and len({x['name'] for x in order})==293
assert load('canonical-entry.json')==order[105] and order[105]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
v=load('verification.json')
assert v['declaration']==N and v['production_unchanged'] and v['unresolved']==[]
assert len(v['accepted'])==5 and len(v['rejected'])==4
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert all(len(l)<=100 for l in s.splitlines()),x['source']
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 rs=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and 'success' in z]
 assert rs and all(z['success'] is True for z in rs)
 ds=[]
 for z in rs:
  assert not z.get('partial',False) and not z.get('timed_out',False) and not z.get('failed_dependencies')
  if x['label']!='raw':assert z.get('partial') is False
  ds.extend(z.get('items',z.get('diagnostics',[])))
 assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
 alltext='\n'.join(d.get('message','') for d in ds)
 assert not any(t in alltext for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',alltext):
  assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 fresh=ds if x['label']=='raw' else [d for d in ds if d.get('line',0)>=x['native_region_start_line']]
 msg='\n'.join(d.get('message','') for d in fresh)
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  for t in ['#check_failure Roth.genWronskian_eq_zero_of_not_linearIndependent',
            '#check_failure MvPolynomial.hasseDeriv','[CommSemiring R]',
            '[AddCommMonoid M]','theorem bundled_zero','#check @LinearMap.pi']:
   assert t in s,t
 elif x['label']=='probes':
  for t in ['theorem zero_divisor_guard','theorem inline_original','(A := MvPolynomial σ R)',
            'GenWronskianAssessment.generalized','LinearMap.pi','(ℤ × ℤ)']:
   assert t in s,t
 elif x['label']=='floor-audit':
  for t in ['[NoZeroDivisors R]','nontriviality R','let : IsDomain R := NoZeroDivisors.to_isDomain R']:
   assert t in s,t
  found=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert len(found)==1 and norm(found[0])==norm(array)
  assert 'GEN_WRONSKIAN_ZERO_AUDIT: requested=293; unique=293' in msg
  assert 'GEN_WRONSKIAN_ZERO_AUDIT_PRESENT: present=293; values=293' in msg
  assert not any(d.get('message','').startswith('GEN_WRONSKIAN_ZERO_DIRECT_CONSUMER: ') for d in fresh)
 elif x['label']=='original':
  assert '#print Roth.genWronskian_eq_zero_of_not_linearIndependent' in s
  assert '@Roth.genWronskian_eq_zero_of_not_linearIndependent :' in msg
 else:
  for t in ['[CommRing R]','noncomputable def generalized','theorem original_eq','theorem abstract_eq']:
   assert t in s,t
for x in v['rejected']:
 assert not x['accepted'] and (D/x['source']).is_file() and (D/x['receipt']).is_file()
 r=load(x['receipt']);assert isinstance(r,dict) and 'result' in r
 assert x['source'] not in [z['source'] for z in v['accepted']]
f=load('formal-search.json');assert len(f)==12
for method in ['Finder','Loogle','LeanSearch','Local']:
 rows=[z for z in f if z['method']==method]
 assert {z['form'] for z in rows}=={'current','literature','abstract'}
 for z in rows:
  r=load(z['receipt']);assert r['request']==z['request']
  if method=='Loogle' and z['form']=='current':
   assert r['response'].get('isError') is True
   assert not load('loogle-current-retry.json')['response'].get('isError',False)
  else:assert not r['response'].get('isError',False)
for form in ['current','standard','abstract','callers','inline','local-literature']:
 assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for file in ['web-0.json','web-1.json','web-2.json','web-direct.json']:
 w=load(file);assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w
 queries.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(queries[:3]))==3
for domain in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu',
               'site:mathoverflow.net','site:arxiv.org']:
 assert any(domain in q for q in queries),domain
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json')
assert c['named_count']==c['occurrence_count_excluding_def']==0 and c['callers']==[]
s=report().read_text()
for t in ['Phase 8','BORDERLINE-needs-human','NOT-COMPOSABLE','four named existing calls',
          'RESTATE-BEFORE-SHIP','STRICTLY NARROWER','n/a — theorem','ask_chatgpt_math unavailable',
          '1. Should','2. Should','3. If a separate','reconstructed exactly']:
 assert t in s,t
assert load('overview-entry.json')['type'].startswith('∀')
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
r=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
print('PASS: full phases, current manifest, native5clean/4rejected,17inputs, canonical293 exact order, zero callers, evidence guard')
