#!/usr/bin/env python3
"""Read-only validator for scratch and integrated current artifacts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;N='MvPolynomial.taylor_injective'
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==71
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS'] and a['verdict']=='BORDERLINE-needs-human'
assert 1<=len(a['questions'])<=5
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' for v in a['phases'].values()) and set(a['justified_na'])=={'2b','4.5'}
for x in load('copy-manifest.json')['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
v=load('verification.json');assert len(v['rejected'])==2 and v['unresolved']==[]
assert {x['label'] for x in v['accepted']}=={'target','raw','extra'}
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 found=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True];assert found
 for z in found:
  assert z.get('partial',False) is False and z.get('timed_out',False) is False and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msg='\n'.join(d.get('message','') for d in ds);assert 'sorryAx' not in msg and 'PANIC' not in msg
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axs
  for ax in axs:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
  if x['label']=='target':
   used=re.search(r'INJECTIVE_REPLAY_CONSTANTS: (\[[^]]*\])',msg);assert used
   assert 'MvPolynomial.taylor_injective' not in used.group(1)
   assert 'MvPolynomial.taylor_neg_taylor' in used.group(1)
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and 'theorem conditionalInjective' in s and 'β j + α j = 0' in s
  assert 'Polynomial.taylor_injective a' in s and 'theorem generic' in s
  assert 'theorem topCollision' in s and 'theorem topNotInjective' in s
  assert 'WithTop ℕ' in s and 'theorem directInverse' in s
 elif x['label']=='extra':
  assert 'theorem expanded' in s and 'fail_if_success let _ := (MvPolynomial.taylor_injective' in s
 else:assert 'theorem independent' in s and 'theorem bundled' in s and 'theorem zeroCaller' in s
for n in v['prerequisites']:
 s=(D/n).read_text();assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert load('input-hash-check.json')['all_pass']
f=load('formal-search.json');assert {x['form'] for x in f}=={'current','literature','abstract'}
for form in f:
 assert {x['method'] for x in form['methods']}=={'Finder','LeanSearch','Loogle','local'}
 for m in form['methods']:assert m['status']=='fulfilled' and not m['value'].get('isError',False)
for form in ['current','literature','abstract','full-name','callers','inline','independent']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for tag in ['web-specific','web-channels','web-primary','web-locators']:
 w=load(tag+'.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
 assert w['safe_locators'];queries += [x['q'] for x in w['request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for domain in ['site:nlab.org','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(domain in q for q in queries)
assert load('callers.json')['explicit_count']==1 and load('callers.json')['external_to_declaring_file']==0
assert [x['line'] for x in load('callers.json')['named_callers']]==[193]
assert load('canonical-entry.json')['name']==N and load('overview-entry.json')['type'].startswith('∀')
s=report().read_text();assert '## Phase 8' in s and '**BORDERLINE-needs-human**' in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS71: full phases; fresh17 hashes; currentmanifest; native3 clean standardaxioms; actualfullzeroiffcaller; raw inverse/generic/conditional/univariate and semiring counterexample; formal5×3; namedlit; links/secretguard')
