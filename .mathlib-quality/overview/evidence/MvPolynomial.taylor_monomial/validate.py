#!/usr/bin/env python3
"""Read-only scratch/integrated validator. Current copy-manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
NAME='MvPolynomial.taylor_monomial'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for y in x.values():yield from nodes(y)
 elif isinstance(x,list):
  for y in x:yield from nodes(y)
a=read('assessment.json')
assert a['declaration']==NAME and a['canonical_index']==57 and a['completed'] and a['allphases']=='PASS'
assert a['root_acceptance'] in ['pending','PASS'] and a['unresolved']==[] and a['production_unchanged']
assert a['verdict']=='NO-mathlib-has-it'
assert set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(x=='PASS' for x in a['phases'].values()) and set(a['justified_na'])=={'2b','4.5'}
seen=set()
for x in read('copy-manifest.json')['files']:
 dst=x['destination']; report='/mathlibable/' in dst
 p=(D/'report.md' if (D/'report.md').is_file() else ROOT/dst) if report else D/Path(dst).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add('report.md' if report else p.name)
assert {'report.md','assessment.json','overview-entry.json','verification.json','validate.py','formal-search.json'}<=seen
v=read('verification.json');assert v['unresolved']==[] and len(v['rejected'])==1
assert {x['label'] for x in v['accepted']}=={'target','raw','caller'}
allowed={'propext','Classical.choice','Quot.sound'}; assert set(v['standard_axioms'])==allowed
for x in v['accepted']:
 p=D/x['source'];t=p.read_text();assert sha(p)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',t)
 r=read(x['receipt']);assert not r['result'].get('isError',False)
 content=r['result'].get('structuredContent',r['result'])
 good=[n for n in nodes(content) if isinstance(n,dict) and n.get('success') is True]; assert good,x
 for n in good:
  assert n.get('partial',False) is False and n.get('timed_out',False) is False and not n.get('failed_dependencies')
  ds=n.get('diagnostics',n.get('items',[]))
  assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msgs='\n'.join(d.get('message','') for d in ds); assert 'sorryAx' not in msgs
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msgs);assert axs
  for ax in axs:assert {s.strip() for s in ax.split(',') if s.strip()}<=allowed
 if x['label']=='raw':
  assert r['request']['code']==t and not re.search(r'^import Roth\b',t,re.M)
  assert '#check_failure '+NAME in t and 'theorem universal' in t and '[CommSemiring A]' in t
  assert 'theorem inline' in t and 'aeval_monomial _ _ _' in t
 else:
  assert r['request']['file_path'].endswith('.lean') and 'namespace MvPolynomial.TaylorMonomialAssessment' in t
  if x['label']=='caller':
   frag=t[t.index('namespace MvPolynomial.TaylorMonomialCallerReplay'):]
   assert 'theorem replay' in frag and 'have h1 : taylor α P' in frag
   assert 'from aeval_monomial _ _ _' in frag and 'rw [taylor_monomial' not in frag
   assert 'taylor_neg_taylor' in frag and 'Finsupp.prod_fintype' in frag
inputs=read(v['inputs']); assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+read(v['mathlib_inputs']):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
for src,archive in v['source_links'].items():assert sha(ROOT/src)==sha(D/archive)
assert read('input-hash-check.json')['all_pass']
f=read('formal-search.json'); assert len(f)==12
for x in f:assert not x['response'].get('isError',False)
for method in ['Finder','Loogle','LeanSearch','local']:assert {x['form'] for x in f if x['method']==method}=={'current','literature','abstract'}
for form in ['current','literature','abstract']:assert read('rg-'+form+'.json')['exit_code']==0
web=[read('web-'+str(i)+'-metadata.json') for i in range(8)]
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for term in ['site:ncatlab.org/nlab','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(term in q for q in queries),term
for w in web+[read('web-primary-metadata.json'),read('web-stacks-followup-metadata.json')]:
 assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
assert read('local-literature.json')['locator']
c=read('callers.json');assert c['all_explicit_callers']==1 and c['external']==0 and c['within_declaring_file']==1 and c['callers'][0]['line']==212
assert read('overview-entry.json')['type'].startswith('∀ {σ : Type') and read('canonical-entry.json')['name']==NAME
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
t=p.read_text();assert '## Phase 8' in t and '**NO-mathlib-has-it**' in t
for link in re.findall(r'\]\(([^)]+)\)',t):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/'; assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: complete phases; current manifest; complete clean native target/raw/caller checks; standard axioms; 17 fresh inputs; five methods × three forms; all literature channels; one full named caller using direct generic law; links; credential guard')
