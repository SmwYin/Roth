#!/usr/bin/env python3
"""Read-only scratch/integrated validation, including current manifest and native gates."""
from pathlib import Path
import json,hashlib,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve();N='MvPolynomial.eval_eq_sum_box'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==74 and a['completed'] and a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged']
assert a['verdict']=='YES-but-generalise-first' and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and all(v=='PASS' for v in a['phases'].values())
assert set(a['justified_na'])=={'2b','4.5'}
for x in load('copy-manifest.json')['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
v=load('verification.json');assert len(v['rejected'])==1 and v['unresolved']==[]
assert {x['label'] for x in v['accepted']}=={'target','consumers','algebra','raw','fullcenter'}
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 found=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True];assert found
 for z in found:
  assert z.get('partial',False) is False and z.get('timed_out',False) is False and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msg='\n'.join(d.get('message','') for d in ds);assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axs
  for ax in axs:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and 'theorem supportEvaluated' in s
  assert 'Polynomial.sum_taylor_eq P a' in s and 'eval₂Hom f x' in s
  body=s[s.index('theorem supportEvaluated'):s.index('example (P : Polynomial A)',s.index('theorem supportEvaluated'))]
  assert not any(t in body for t in ['Fintype','hasseDeriv','Roth.box'])
 elif x['label']=='target':
  assert 'theorem replay' in s and 'open Classical in' in s and 'theorem withoutDecidableEq [Fintype σ]' in s
  weak=s[s.index('theorem withoutDecidableEq'):s.index('theorem recovery')];assert '[DecidableEq σ]' not in weak
  assert 'Subsingleton.elim' in s and 'cases hi' in s
 elif x['label']=='consumers':
  assert 'lemma powerBound' in s and 'theorem estimate' in s and 'TaylorEvaluatedAssessment.recovery' in s
  assert 'Real.rpow_le_rpow_of_nonpos' in s and 'Finset.sum_lt_sum_of_nonempty' in s
 elif x['label']=='algebra':
  assert '[CommRing B] [Algebra A B]' in s and 'aeval x P' in s and 'algebraMap A B (eval α (hasseDeriv d P))' in s
  assert 'theorem originalRecovery' in s and 'Subsingleton.elim' in s and 'cases hi' in s
  assert 'theorem estimateFromAlgebraTarget' in s and 'TaylorEvaluatedAlgebra.originalRecovery' in s
  assert 'Finset.sum_lt_sum_of_nonempty' in s
 else:
  assert '[CommSemiring A] [CommRing B] [Algebra A B]' in s and '(α x : σ → B)' in s
  assert 'aeval α (hasseDeriv d P)' in s and 'support_map_subset' in s and 'monomial_le_degreeOf' in s
  assert 'hasseDeriv_map' in s and 'eval₂_eq_eval_map' in s
  assert 'theorem originalRecovery' in s and 'Subsingleton.elim' in s and 'cases hi' in s
  assert 'theorem estimateFromFullCenter' in s and 'TaylorEvaluatedFullCenter.originalRecovery' in s
  assert 'Finset.sum_lt_sum_of_nonempty' in s
for x in v['rejected']:assert (D/x['source']).is_file() and (D/x['receipt']).is_file()
for n in load('prerequisites.json')['files']:assert (D/n).is_file()
b=load('file-completion-build.json');log=D/'file-completion-build.log';assert b['exit_code']==0 and b['command']==['/Users/ramin/.elan/bin/lake','build']
assert sha(log)==b['log_sha256'] and log.stat().st_size==b['log_bytes'] and '2467 jobs' in log.read_text()
assert not re.search(r'(?im)\b(error|warning)\b',log.read_text())
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert load('input-hash-check.json')['all_pass']
f=load('formal-search.json');assert len(f)==12
for method in ['Finder','Loogle','LeanSearch','Local']:
 rows=[x for x in f if x['method']==method];assert {x['form'] for x in rows}=={'current','literature','abstract'} and len(rows)==3
 assert all(not x['result'].get('isError',False) for x in rows)
for form in ['current','literature','abstract','full-name','callers','inline','local-literature']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for i in range(5):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w and w['urls']
 queries.extend(x['q'] for x in w['request'].get('search_query',[]))
assert len(set(queries[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in queries)
g=load('generality.json');assert g['dropped']=='Explicit DecidableEq σ binder' and g['same_mathematical_conclusion']
assert all(g[k] for k in ['original_caller_validated','weaker_caller_validated','algebra_target_validated','algebra_recovery_caller_validated','full_center_validated','coefficient_semiring_validated','full_center_recovery_caller_validated'])
c=load('callers.json');assert c['named_count']==1 and c['external_to_declaring_file']==1 and c['callers'][0]['line']==390
group=load('proposed-pr-group.json');assert len(group)==4 and all(x['verdict'].startswith('YES') for x in group)
assert load('reviewer-history.json')['exit_code']==0 and not load('reviewer-history.json')['contacted']
assert load('canonical-entry.json')['name']==N and load('overview-entry.json')['type'].startswith('∀')
s=report().read_text();assert '## Phase 8' in s and 'YES-but-generalise-first' in s and '_PENDING' not in s
assert 'propositionally, not definitionally' in s and 'RESTATE-BEFORE-SHIP' in s and '**BIG**' in s and '6.669' in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS74: all phases; fresh17; five clean nonpartial native sets; no-DecEq/coefficient-semiring/full B-center-point target; original recovery and full Main caller three times; raw support eval boundary; fresh full build2467; formal5x3; literature; standardaxioms/currentmanifest/links/secretguard')
