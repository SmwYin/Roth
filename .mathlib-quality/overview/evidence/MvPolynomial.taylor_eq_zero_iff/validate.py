#!/usr/bin/env python3
"""Read-only current-manifest validator in scratch or integrated layout."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;N='MvPolynomial.taylor_eq_zero_iff';R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==72 and a['completed'] and a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS'] and a['verdict']=='YES-but-generalise-first'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and all(x=='PASS' for x in a['phases'].values())
assert set(a['justified_na'])=={'2b','4.5'}
for x in load('copy-manifest.json')['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
v=load('verification.json');assert len(v['rejected'])==1 and v['unresolved']==[]
assert {x['label'] for x in v['accepted']}=={'target','raw','semiring','consumers','calleraudit','extra'}
messages={}
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 found=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True];assert found
 for z in found:
  assert z.get('partial',False) is False and z.get('timed_out',False) is False and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msg='\n'.join(d.get('message','') for d in ds);assert 'sorryAx' not in msg and 'PANIC' not in msg and '_inhabitedExprDummy' not in msg
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg)
  if x['label']!='calleraudit':assert axs
  for ax in axs:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
  messages[x['label']]=msg
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and 'theorem generic' in s and 'Function.Injective (shift α' in s
  assert 'Polynomial.taylor_eq_zero a P' in s and 'theorem conditional' in s and 'theorem ring' in s
  assert 'theorem topNotInjective' in s
 elif x['label']=='semiring':
  assert '[CommSemiring R]' in s and 'support.exists_maximal' in s and 'rw [coeff_hasseDeriv]' in s
  assert 'coeff_taylor, hderiv, eval_C' in s
  assert not any(t in s for t in ['taylor_injective','taylor_neg_taylor','taylor_eq_zero_iff'])
 elif x['label']=='consumers':
  assert 'attribute [-simp] '+N in s and 'attribute [local simp] MvPolynomial.TaylorZeroSemiringExperiment.reflected' in s
  for t in ['exists_weight_eq_index','le_index_iff','index_eq_weightedOrder_div','index_mul']:assert 'theorem '+t in s
 elif x['label']=='calleraudit':
  assert 'startsWith "MvPolynomial.taylor_eq_zero_iff"' in s and 'allowOpaque := true' in s
 elif x['label']=='extra':assert 'theorem expanded' in s and '[CommSemiring R]' in s and '[CommRing A]' in s
 else:assert 'theorem replay' in s and 'theorem independent' in s
used=re.search(r'SEMIRING_ZERO_REFLECTION_CONSTANTS: (\[[^]]*\])',messages['extra']);assert used
assert all(t not in used.group(1) for t in ['MvPolynomial.taylor_eq_zero_iff','MvPolynomial.taylor_injective','MvPolynomial.taylor_neg_taylor'])
for t in ['Roth.exists_weight_eq_index','Roth.le_index_iff','Roth.index_eq_weightedOrder_div','Roth.index_mul']:assert 'ZERO_IFF_DIRECT_PROOF_CONSUMER: '+t in messages['calleraudit']
for n in v['prerequisites']:assert (D/n).is_file()
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert load('input-hash-check.json')['all_pass']
f=load('formal-search.json');assert {x['label'] for x in f['forms']}=={'current','literature','abstract'}
for form in f['forms']:
 assert len(form['responses'])==3
 for response in form['responses']:assert response['status']=='fulfilled' and not response['value'].get('isError',False)
assert len(f['loogle'])==3 and all(not x['response'].get('isError',False) for x in f['loogle'])
for form in ['current','literature','abstract','full-name','callers','inline','independent','kernel']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for i in range(6):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
 assert w['locators'];queries += [x['q'] for x in w['request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for d in ['site:nlab.org','site:ncatlab.org','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(d in q for q in queries)
assert load('callers.json')['explicit_count']==0 and len(load('callers.json')['kernel_simp_consumers'])==4
g=load('generality.json');assert g['verified']=='CommSemiring R' and g['same_parent'] and g['same_conclusion'] and not g['proof_body_unchanged']
assert all(x['verdict'].startswith('YES') for x in load('proposed-pr-group.json')) and len(load('proposed-pr-group.json'))==4
assert load('reviewer-history.json')['exit_code']==0 and not load('reviewer-history.json')['contacted']
assert load('canonical-entry.json')['name']==N and load('overview-entry.json')['type'].startswith('∀')
s=report().read_text();assert '## Phase 8' in s and '**YES-but-generalise-first**' in s and 'GENERALITY_' not in s
assert 'not an unchanged-body hypothesis deletion' in s and 'RESTATE-BEFORE-SHIP' in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS72: fullphases; fresh17 hashes; six clean native sets; actual CommSemiring same-statement replacement and4implicitconsumers; formal5x3/namedlit; standardaxioms; currentmanifest/links/secretguard')
