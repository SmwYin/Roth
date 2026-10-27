#!/usr/bin/env python3
"""Portable read-only validator for declaration81 scratch/integrated assessment."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.abs_coeff_le_normOne'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def walk(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==81 and a['completed'] and a['allphases']=='PASS'
assert a['unresolved']==[] and a['root_acceptance'] in ['pending','PASS'] and a['production_unchanged']
assert a['verdict']=='NO-mathlib-has-it'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a:')) for k,v in a['phases'].items())
m=load('copy-manifest.json');names=set()
for x in m['files']:
 q=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert q.is_file() and sha(q)==x['sha256'] and q.stat().st_size==x['bytes'],q
 names.add(q.name)
assert {q.name for q in D.iterdir() if q.is_file()}-names<={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
v=load('verification.json')
assert v['unresolved']==[] and v['rejected']==[] and {x['label'] for x in v['accepted']}=={'target','raw','consumers','general'}
for x in v['accepted']:
 q=D/x['source'];s=q.read_text();assert sha(q)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 z=load(x['receipt']);result=z['result'];assert not result.get('isError',False)
 successes=[n for n in walk(result.get('structuredContent',result)) if isinstance(n,dict) and n.get('success') is True]
 assert successes,x['label']
 for n in successes:
  assert n.get('partial',False) is False and not n.get('timed_out',False) and not n.get('failed_dependencies')
  ds=n.get('diagnostics',n.get('items',[]))
  assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  messages='\n'.join(d.get('message','') for d in ds)
  assert not any(t in messages for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axioms=re.findall(r'depends on axioms: \[([^]]*)\]',messages);assert axioms
  for ax in axioms:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 if x['label'] in ['raw','general']:
  assert z['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s
 if x['label']=='raw':
  for t in ['theorem raw','theorem generic','theorem orderedAbs','[PartialOrder N]','[Lattice G]','theorem preorderGeneric','[Preorder N]']:assert t in s
 elif x['label']=='general':
  for t in ['theorem supportLocal','[Preorder N]','[AddLeftMono N]','∀ i ∈ f.support','Finset.single_le_sum h ha','Finset.sum_nonneg h']:assert t in s
 elif x['label']=='consumers':
  for t in ['theorem determinant','Finsupp.single_eval_le_sum _','normOne_det_le','normOne_hasseDeriv_le','by ring']:assert t in s
  assert 'abs_coeff_le_normOne' not in s
 else:
  for t in ['#print '+N,'theorem direct','Finsupp.single_eval_le_sum P.coeff']:assert t in s
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 q=R/x['path'];assert q.is_file() and sha(q)==x['sha256'] and q.stat().st_size==x['bytes'],q
assert load('input-hash-check.json')['all_pass'] and '2467 jobs' in (D/'baseline-build.txt').read_text()
lit=load('local-literature-source.json');q=R/lit['path'];assert sha(q)==lit['sha256'] and q.stat().st_size==lit['bytes']
f=load('formal-search.json');assert len(f)==14
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 assert {x['form'] for x in f if x['method']==method}>={'current','standard','abstract'}
 for form in ['current','standard','abstract']:assert (D/(method+'-'+form+'.json')).is_file()
assert not load('lean_loogle-current-corrected.json')['result'].get('isError',False)
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 assert load('rg-'+tag+'.json')['exit_code'] in [0,1]
assert 'single_eval_le_sum' in load('rg-literature.json')['stdout']
queries=[]
for i in range(5):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes_utf8']>0
 assert w['urls'] and w['summaries'] and not w['full_bodies_archived'] and 'response' not in w and 'raw' not in w
 queries.extend(q['q'] for q in w['request'].get('search_query',[]))
assert len(set(queries[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(site in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json');assert c['named_count']==1 and len(c['callers'])==1 and c['external_to_declaring_file']==0
assert load('canonical-entry.json')['name']==N
assert load('overview-entry.json')['type'].startswith('∀')
s=report().read_text()
for phase in a['phases']:assert 'Phase '+phase in s
for token in ['**SMALL**','NO-mathlib-has-it','MAXIMALLY GENERAL','STRICTLY NARROWER','False-generalization','supportLocal','entire sole determinant','new proof witness','PartialOrder','AddLeftMono','ask_chatgpt_math']:
 assert token in s,token
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS81: all phases; five methods/three forms; named literature channels and access limits; four fresh native sets; exact existing-law specialization, full sole consumer, separate new broader helper; source/pin/current manifest hashes; portable links; credential guard.')
