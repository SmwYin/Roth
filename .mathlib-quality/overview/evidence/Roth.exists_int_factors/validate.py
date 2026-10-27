#!/usr/bin/env python3
"""Read-only portable176 assessment validator: scratch or integrated evidence directory."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_int_factors'
def rd(n): return json.loads((D/n).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==176 and a['completed']
assert a['verdict']=='YES-but-generalise-first' and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']
for t in ['{τ : Type','{U\' : MvPolynomial τ ℚ}','{V\' : Polynomial ℚ}',
          '∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ)','U ≠ 0','V ≠ 0',
          '(∀ (j : τ), degreeOf j U = degreeOf j U\')','V.natDegree = V\'.natDegree']:
 assert t in o['type'],t
assert not any(t in o['type'] for t in ['Fintype','DecidableEq'])
m=rd('copy-manifest.json');assert m['declaration']==N
seen=set()
for x in m['files']:
 if '/mathlibable/' in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed

def native(e):
 r=rd(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] and not z.get('timed_out')
 src=D/e['source'];s=src.read_text();assert sha(src)==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s or e['label']=='semantic-both-zero-factor-guards'
  ds=z['diagnostics']
 else:
  assert z['partial'] is False and not z.get('still_elaborating_lines') and not z.get('failed_dependencies')
  ds=z['items']
 assert not [x for x in ds if x.get('severity')in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message'] for x in ds)):
  assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
 info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 return ds
assert len(v['accepted'])==9
for e in v['accepted']:native(e)
for e in v['rejected']:
 z=rd(e['receipt'])['result']['structuredContent'];z=z.get('result',z)
 assert any(x.get('severity')in ['error','warning'] for x in z.get('items',z.get('diagnostics',[])))
 assert e['source'] not in {x['source'] for x in v['accepted']}
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('baseline-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path'] for x in fresh}
for x in fresh:assert x['matches'] and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'] and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Separation.lean')==sha(D/'source-context.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name'] for x in order})==293 and order[175]==rd('canonical-target.json')
assert order[175]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private'
          else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());h=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',h[1],h[2]) if h else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/v['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[v['audit']['start_line']-1:])==s.rstrip('\n')
ds=native(v['accepted'][0])
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=535 and
      x['message'].startswith('FACTORS176_DIRECT_CONSUMER:')]
assert cons==o['caller_summary']['direct_kernel_value_consumers']==['Roth.exists_det_eq_mul']
lex=rd('lexical-enumeration.json');assert {x['path'] for x in lex}=={x['file'] for x in order}
for f in lex:
 assert sha(R/f['path'])==f['sha256']
 occ=[{'line':i,'text':l} for i,l in enumerate((R/f['path']).read_text().splitlines(),1)
      if 'exists_int_factors' in l]
 assert occ==f['occurrences']
assert sum(len(f['occurrences'])for f in lex)==3 and o['caller_summary']['explicit_use_count']==1
full=(D/'factors176-gcd-full-executed.lean.txt').read_text()
assert len(re.findall(r'^import ',full,re.M))==15 and 'open MvPolynomial Roth'not in full
assert 'namespace Factors176Coeff' in full and 'namespace Primitive172FullGeneric' in full
assert 'IsLocalization.surj_of_gcd_domain' in full
assert 'IsBezout' not in full and 'UniqueFactorizationMonoid'not in full
assert 'theorem exists_int_factors' in full and '(∀ j, degreeOf j U = degreeOf j U\')' in full
assert 'V.natDegree = V\'.natDegree' in full
comp=(D/'factors176-gcd-composition-specialization-executed.lean.txt').read_text()
assert 'fail_if_success exact hF' in comp and 'fail_if_success simpa only using hF' in comp
assert 'Factors176GCD.exists_int_factors (R := ℤ) (K := ℚ) hU hV hF' in comp
caller=(D/'factors176-gcd-caller-executed.lean.txt').read_text()
assert 'namespace Factors176GCDCaller' in caller and 'Factors176GCD.exists_int_factors (R := ℤ) (K := ℚ) hU\' hV\' hFmap' in caller
assert 'Lean.mkPrivateNameCore `Roth.Separation `Roth.exists_rat_factors_det_hasseDeriv_aux' in caller
original=(D/'source-context.lean.txt').read_text().split('theorem exists_det_eq_mul',1)[1].split('\nend Roth')[0].strip()
replay=caller.split('namespace Factors176GCDCaller',1)[1].split('theorem exists_det_eq_mul',1)[1].split('#print axioms exists_det_eq_mul')[0].strip()
# Exact body comparison up to root's harmless wrapping of the original obtain line.
norm=lambda x:' '.join(x.split())
expected=original.replace('exists_rat_factors_det_hasseDeriv_aux','gcd_rat_factors').replace('exists_int_factors hU\' hV\' hFmap','Factors176GCD.exists_int_factors (R := ℤ) (K := ℚ) hU\' hV\' hFmap')
assert norm(replay)==norm(expected)
guards=(D/'factors176-guards-executed.lean.txt').read_text()
assert all('theorem '+x in guards for x in ['zero_product_impossible','left_zero_input','right_zero_input'])
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','local_search']:
  r=rd(form+'-'+method+'.json');assert r['method']==method and r['request']['query']
  assert not r['result'].get('isError',False)
 r=rd(form+'-rg.json');assert r['command'][0]=='rg' and r['exit_code']in [0,1]
for f in ['callers-rg.json','callers-git-grep.json']:
 r=rd(f);assert r['exit_code']==0 and len(r['stdout'].splitlines())==3
queries=[]
for i in range(5):
 w=rd(f'literature-{i}.json');assert len(w['response_digest']['sha256'])==64
 assert w['response_digest']['bytes']>0 and w['status'] and w['locators'] and w['summary']
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
          'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
g=rd('accepted-grouping.json');assert {x['declaration'] for x in g}==set(o['action']['grouping'])
assert all(x['verdict'].startswith('YES')and x['acceptance']=='PASS'for x in g)
assert rd('reviewers-focused.json')['exit_code']==0
assert all(t in rd('reviewers-focused.json')['stdout'] for t in ['e4c37418a1','Justus Springer','2f35248703'])
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
assert 'GENERIC_SIGNATURE'not in s and 'FULL_NATIVE_TYPE'not in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:176 full phases; fresh17; exact ordered293;9 clean native checks; full GCD factors/degrees; exact specialization/fullcaller/semantic guards;15search cells; literature; current manifest/links.')
