#!/usr/bin/env python3
"""Read-only current-manifest validator, scratch and integrated layouts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;N='MvPolynomial.taylor_neg_taylor'
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
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==70
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS'] and a['verdict']=='BORDERLINE-needs-human'
assert 1<=len(a['questions'])<=5
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' for v in a['phases'].values()) and set(a['justified_na'])=={'2b','4.5'}
for x in load('copy-manifest.json')['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
v=load('verification.json');assert v['rejected']==[] and v['unresolved']==[]
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
   used=re.search(r'INVERSE_REPLAY_CONSTANTS: (\[[^]]*\])',msg);assert used
   assert 'MvPolynomial.taylor_neg_taylor' not in used.group(1)
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and 'theorem conditional' in s and 'β j + α j = 0' in s
  assert '(Polynomial.taylorEquiv a).symm_apply_apply P' in s
  assert 'theorem directInverse' in s and 'simp [shift, comp_aeval_apply, add_assoc, aeval_X_left_apply]' in s
 elif x['label']=='extra':
  assert 'def equivalence' in s and 'theorem expansionCaller' in s
  assert '(TaylorInverseAssessment.replay α P).symm' in s
  assert 'fail_if_success let _ := (MvPolynomial.taylor_neg_taylor' in s
 else:assert 'theorem injective' in s and 'theorem zeroIff' in s
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert load('input-hash-check.json')['all_pass']
f=load('formal-search.json')
for m in ['Finder','LeanSearch','Loogle','local']:
 for form in ['current','literature','abstract']:assert any(x['method']==m and x['form']==form for x in f)
assert any(x['method']=='Loogle' and x['form']=='abstract-retry-success' and not x['result'].get('isError',False) for x in f)
for form in ['current','literature','abstract','full-name','callers','inline']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for tag in ['web0','web4','webprimary','webfollow','weblocator']:
 w=load(tag+'-metadata.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
 assert w['safe_locators'];queries += [x['q'] for x in w['actual_request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for domain in ['site:ncatlab.org/nlab','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(domain in q for q in queries)
assert load('callers.json')['explicit_count']==2 and load('callers.json')['external_to_declaring_file']==0
assert [x['line'] for x in load('callers.json')['named_callers']]==[188,208]
assert load('canonical-entry.json')['name']==N and load('overview-entry.json')['type'].startswith('∀')
s=report().read_text();assert '## Phase 8' in s and '**BORDERLINE-needs-human**' in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: complete70 phases, fresh17hashes, currentmanifest, native3clean, standardaxioms, explicit2fullcallers, conditional/bundle/univprobes, formal5methods×3forms with honest retry, named literature channels, links, credential guard')
