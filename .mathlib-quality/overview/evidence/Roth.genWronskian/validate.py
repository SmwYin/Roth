#!/usr/bin/env python3
"""Read-only validator for scratch or integrated current assessment artifacts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
N='Roth.genWronskian'
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
assert a['declaration']==N and a['canonical_index']==101 and a['completed']
assert a['allphases']=='PASS' and a['verdict']=='YES-but-generalise-first'
assert a['unresolved']==[] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' for v in a['phases'].values())
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
inputs=load('inputs.json');assert len(inputs)==17
assert all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('source-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert load('canonical-snapshot.json')==order and len(order)==293 and len({x['name'] for x in order})==293
assert load('canonical-entry.json')==order[100] and order[100]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert len(v['accepted'])==5 and len(v['rejected'])==1
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
 text='\n'.join(d.get('message','') for d in ds)
 assert not any(t in text for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',text):
  assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 fresh=ds if x['label']=='raw' else [d for d in ds if d.get('line',0)>=x['native_region_start_line']]
 msg='\n'.join(d.get('message','') for d in fresh)
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  for token in ['#check_failure Roth.genWronskian','#check_failure MvPolynomial.hasseDeriv','#check @Matrix.det','#check @Matrix.detRowAlternating','#check @Polynomial.wronskian','#check_failure (inferInstance : CommRing ℕ)']:assert token in s
 elif x['label']=='generic':
  for t in ['#print Roth.genWronskian','[CommRing R]','theorem original_eq','theorem abstract_eq','σ := ℕ']:assert t in s
 elif x['label']=='consumers':
  assert len(x['expected_axiom_declarations'])==5
  for n in x['expected_axiom_declarations']:assert n.split('.')[-1] in s
 elif x['label']=='bridge':
  for t in ['theorem expanded_eq','theorem raw_eq','hasseDeriv_apply','ULift.{v} ℤ','ULift.{w} (Fin 2)','#synth CommRing']:assert t in s,t
 else:
  found=re.search(r'let names : Array Lean.Name := #\[.*?\]',s,re.S);assert found and norm(found.group())==norm(array)
  assert 'GEN_WRONSKIAN_AUDIT: requested=293; unique=293' in msg
  assert 'GEN_WRONSKIAN_AUDIT_PRESENT: present=293; values=293' in msg
  consumers=[d['message'].split(': ',1)[1] for d in fresh if d.get('message','').startswith('GEN_WRONSKIAN_DIRECT_CONSUMER: ')]
  actual=[]
  for c in load('callers.json')['callers']:
   o=next(z for z in order if z['name']==c['name'])
   actual.append('_private.'+o['file'][:-5].replace('/','.')+'.0.'+o['name'] if o['visibility']=='private' else o['name'])
  assert consumers==actual
for x in v['rejected']:
 assert not x['accepted'] and (D/x['source']).is_file() and (D/x['receipt']).is_file()
f=load('formal-search.json');assert len(f)==12
for method in ['Finder','Loogle','LeanSearch','Local']:
 rows=[z for z in f if z['method']==method];assert {z['form'] for z in rows}=={'current','literature','abstract'}
 for z in rows:
  r=load(z['receipt']);assert r['request']==z['request'] and not r['response'].get('isError',False)
for form in ['current','standard','abstract','callers','inline','local-literature']:
 assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for n in ['web-0.json','web-3.json','web-6.json','web-direct.json','web-follow.json']:
 w=load(n);assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['summary']
 assert 'response' not in w and 'result' not in w
 queries.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(queries[:3]))==3
for domain in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(domain in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json');assert c['named_count']==5 and c['occurrence_count_excluding_def']==7
assert len(c['callers'])==5 and c['external_to_declaring_file']==2
assert load('overview-entry.json')['type'].startswith('∀')
assert load('reviewer-git.json')['result']['exit_code']==0
assert any(z['declaration']=='MvPolynomial.hasseDeriv' and z['verdict']=='YES-add-as-is' for z in load('accepted-yes-snapshot.json'))
s=report().read_text()
for t in ['## Phase 8','ONE-LINER WITH-EXEMPTION','RESTATE-BEFORE-SHIP','YES-but-generalise-first','Rao Xiaojia','NOT-COMPOSABLE','CommRing','LOW']:assert t in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
r=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
print('PASS: full phases, current manifest, exact native checks,17 inputs, canonical293 order,5 callers and evidence guard')
