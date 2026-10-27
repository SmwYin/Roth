#!/usr/bin/env python3
"""Portable read-only validator: current manifest, scratch or integrated layout."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd().resolve()
NAME='MvPolynomial.taylor_apply'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
a=read('assessment.json')
assert a['declaration']==NAME and a['completed'] and a['allphases']=='PASS'and a['unresolved']==[]
assert a['root_acceptance']in ['pending','PASS']and a['verdict']=='NO-composable-from-mathlib'
assert set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(x=='PASS'for x in a['phases'].values())
seen=set()
for x in read('copy-manifest.json')['files']:
 dst=x['destination']
 p=(D/'report.md'if(D/'report.md').is_file()else ROOT/dst)if'/mathlibable/'in dst else D/Path(dst).name
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 seen.add('report.md' if '/mathlibable/' in dst else p.name)
assert {'report.md','assessment.json','verification.json','overview-entry.json','validate.py','formal-search.json'}<=seen
v=read('verification.json');assert v['unresolved']==[]and {x['label']for x in v['accepted']}=={'target','raw'}
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
for x in v['accepted']:
 p=D/x['source'];t=p.read_text();assert sha(p)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',t)
 r=read(x['receipt']);assert not r['result'].get('isError',False)
 good=[n for n in nodes(r['result'].get('structuredContent',r['result']))if isinstance(n,dict)and n.get('success')is True];assert good
 for n in good:
  assert n.get('partial',False)is False and n.get('timed_out',False)is False and not n.get('failed_dependencies')
  di=n.get('diagnostics',n.get('items',[]));assert not[d for d in di if d.get('severity')in ['error','warning']or d.get('category')=='sorry']
  axs=re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(d.get('message','')for d in di));assert axs
  for ax in axs:assert {s.strip()for s in ax.split(',')if s.strip()}<=allowed
 if x['label']=='raw':assert r['request']['code']==t and '#check_failure '+NAME in t and not re.search(r'^import Roth\b',t,re.M)
 else:
  assert r['request']['file_path'].endswith('.lean')
  assert 'theorem replay' in t and 'namespace TaylorApplyAssessment' in t
inputs=read(v['inputs']);assert len(inputs)==17 and all(x['match']and x['sha256']==x['baseline_sha256']for x in inputs)
for x in inputs+read(v['mathlib_inputs']):
 p=ROOT/x['path'];assert sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
for src,archive in v['source_links'].items():assert sha(ROOT/src)==sha(D/archive)
assert read('input-hash-check.json')['all_pass']
f=read('formal-search.json');assert len(f)==12
for x in f:assert x['status']=='fulfilled'and not x['value']['response'].get('isError',False)
for method in ['Finder','Loogle','LeanSearch','local']:assert{x['value']['form']for x in f if x['value']['method']==method}=={'current','literature','abstract'}
for form in ['current','literature','abstract']:assert read('rg-'+form+'.json')['exit_code']==0
web=[read(p.name)for p in sorted(D.glob('web-*-metadata.json'))];assert len(web)==8
queries=[q['q']for w in web for q in w['request'].get('search_query',[])]
assert len(set(web[0]['request']['search_query'][i]['q']for i in range(3)))==3
for term in ['site:ncatlab.org/nlab','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(term in q for q in queries),term
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response'not in w
assert read('local-literature.json')['locator']
c=read('callers.json');assert c['all_explicit_callers']==0 and c['excluded'][0]['identifier']=='Polynomial.taylor_apply'
assert [x['line']for x in c['inline_rederivations']]==[143,148,153,159,166]
assert read('overview-entry.json')['type'].startswith('∀ {σ : Type')
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
t=p.read_text();assert '## Phase 8' in t and '**NO-composable-from-mathlib**'in t
for link in re.findall(r'\]\(([^)]+)\)',t):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert link.startswith(prefix),link;assert(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: phases; current manifest; clean complete native checks; standard axioms; 17 inputs; 5 methods × 3 forms; all named literature channels; zero named callers; links; credential guard')
