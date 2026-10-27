#!/usr/bin/env python3
"""Read-only178 validator, portable between scratch and integrated evidence directories."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_det_eq_mul'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==178 and a['completed']
assert a['verdict']=='YES-but-generalise-first' and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']
for t in ['{τ : Type','[Finite τ]','{P : MvPolynomial (Option τ) ℤ}',
          'P ≠ 0','1 ≤ l','l ≤ r none + 1','Finsupp.degree (D μ) ≤ ↑μ','U ≠ 0','V ≠ 0',
          'degreeOf j U ≤ l * r (some j)','V.natDegree ≤ l * r none']:
 assert t in o['type'],t
assert 'Fintype'not in o['type'] and 'DecidableEq'not in o['type']
m=rd('copy-manifest.json');assert m['declaration']==N
seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed

def native(e):
 r=rd(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success']and not z.get('timed_out')
 src=D/e['source'];s=src.read_text();assert sha(src)==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s
  ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not [x for x in ds if x.get('severity')in ['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 return ds
assert len(v['accepted'])==9
for e in v['accepted']:native(e)
assert len(v['rejected'])==2
for e in v['rejected']:
 assert sha(D/e['source'])==e['source_sha256']
 z=rd(e['receipt'])['result']['structuredContent'];z=z.get('result',z)
 assert any(x.get('severity')in ['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 assert e['source']not in {x['source']for x in v['accepted']}
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline']and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Separation.lean')==sha(D/'declaring-module.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[177]==rd('canonical-target.json')
assert order[177]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
          else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert v['canonical_direct_consumers']==['Roth.index_le_lem6']
# The exact generic theorem preserves every semantic conjunct and has no finite-variable binder.
s=(D/'det-factors178-isolated-executed.lean.txt').read_text()
assert '#check_failure MvPolynomial.hasseDeriv'in s
assert not re.search(r'^import Roth\b',s,re.M)
canon=s[s.index('namespace DetFactors178Canonical'):]
assert '[CharZero R]'in canon and '[NormalizedGCDMonoid R]'in canon
assert 'FractionRing R'in canon and '[Finite τ]'not in canon
for t in ['1 ≤ l','l ≤ r none + 1','(D μ).degree ≤ μ','U ≠ 0','V ≠ 0',
          'degreeOf j U ≤ l * r (some j)','V.natDegree ≤ l * r none']:
 assert t in canon,t
assert 'DetFactors178Arbitrary.exists_det_eq_mul'in canon
# Complete current source caller replay, without old target use in the new region.
e=next(x for x in v['accepted']if x['label']=='caller')
s=(D/e['source']).read_text().splitlines()[e['native_region_start_line']-1:];s='\n'.join(s)
assert 'theorem index_le_lem6_replay'in s
assert 'DetFactors178Canonical.exists_det_eq_mul_gcd_domain hR.1 hR.2.1'in s
assert 'Lean.mkPrivateNameCore `Roth.Theta'in s
assert not re.search(r'\bRoth\.exists_det_eq_mul\b',s)
b=rd('separation-file-completion-2026-10-27.json')
assert b['exit_code']==0 and '2467 jobs'in b['stdout']and not b['stderr']
assert sha(D/'separation-file-completion-2026-10-27.log')==b['log_sha256']
assert len(b['sources_and_pins'])==17
for x in b['sources_and_pins']:assert sha(R/x['path'])==x['sha256']
for form in ['current','standard','abstract']:
 for method in ['finder','loogle','leansearch','local']:
  q=rd(f'search-{form}-{method}.json');assert q['request']and not q['response'].get('isError',False)
 assert rd('rg-'+form+'.json')['exit_code']in[0,1]
assert rd('rg-current.json')['exit_code']==1 and not rd('rg-current.json')['stdout']
assert sorted(rd('callers.json')['stdout'].splitlines())==sorted(rd('git-callers.json')['stdout'].splitlines())
queries=[]
for i in range(1,6):
 w=rd(f'web-{i}.json');assert len(w['response_fingerprint']['sha256'])==64
 assert w['response_fingerprint']['bytes']>0 and w['status']and w['locators']and w['summary']
 assert not w['body_archived']
 queries.extend(x['q']for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
          'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-27'in q and 'before:2026-10-28'in q for q in queries)
g=rd('accepted-grouping.json');assert {x['declaration']for x in g}==set(o['action']['grouping'])
assert all(x['verdict'].startswith('YES')and x['acceptance']=='PASS'for x in g)
assert rd('reviewers-focused.json')['exit_code']==0
assert all(t in rd('reviewers-focused.json')['stdout']for t in ['e4c37418a1','Justus Springer','2f35248703'])
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:178 full phases; fresh17; exact ordered293;9 clean native records; arbitraryτ GCD-domain determinant/factors/allbounds; fullcaller; semantic guards;15search cells; full2467job completion build; currentmanifest/links.')
