#!/usr/bin/env python3
"""Read-only validation in scratch or integrated evidence layouts."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.Θ_unique_le'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==199 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human' and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance']in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type'] and 'Fintype' in o['type'] and 'Unique' in o['type']
assert o['project_dependencies']==['Roth.Θ_le_of_forall_index_le','Roth.index_unique_le_log_div']
seen=set();m=rd('copy-manifest.json');assert m['declaration']==N
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
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==6 and not v['rejected']
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success']and not z.get('timed_out')
 p=D/e['source'];s=p.read_text();assert sha(p)==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  ds=z['diagnostics']
  if e['label']=='isolated':assert '#check_failure '+N in s
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')and not z.get('failed_dependencies');ds=z['items']
 assert not [x for x in ds if x.get('severity')in ['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 assert e['required_info']
 for x in e['required_info']:assert x in info,(e['label'],x)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline']and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and len({x['name']for x in order})==293
assert order[198]==rd('canonical-target.json')and order[198]['name']==N and order[198]['line']==256
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
cons=['_private.Roth.Theta.0.Roth.theta_scaled_unique_le_aux','_private.Roth.Theta.0.Roth.theta_lt_base_aux']
assert v['canonical_direct_consumers']==cons and v['canonical_direct_type_consumers']==[]
z=result(rd('theta-unique199-original-receipt.json'))
for marker,ns in [('THETAUNIQUE199_DIRECT_CONSUMER: ',cons),('THETAUNIQUE199_DIRECT_TYPE_CONSUMER: ',[])]:
 assert [x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
formal=[rd('search-'+str(i)+'.json')for i in range(12)]
assert {(x['form'],x['method'])for x in formal}=={(f,m)for f in ['current','standard','abstract']for m in ['Finder','Loogle','LeanSearch','local']}
for x in formal:assert x['request']and x['response']['status']=='fulfilled'
assert rd('search-current-loogle-retry2.json')['response']['isError']is False
for f in ['current','standard','abstract']:assert rd('rg-'+f+'.json')['exit_code']in [0,1]
assert sorted(rd('callers.json')['stdout'].splitlines())==sorted(rd('inventory-callers.json')['stdout'].splitlines())
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293
assert [x['name']for x in lex['callers']]==['Roth.theta_scaled_unique_le_aux','Roth.theta_lt_base_aux']
s=(D/'theta-unique199-fullcaller-executed.lean.txt').read_text()
assert 'theorem caller_scaled'in s and 'theorem caller_base'in s and s.count('RothThetaUnique199.fullUniqueOnly')>=2
s=(D/'theta-unique199-isolated-executed.lean.txt').read_text()
assert '(hpow : q ^ t ≤ B)'in s and 'theorem supremumOfLog'in s and '#check_failure '+N in s
assert 'coefficient_bound_necessary'in(D/'theta-unique199-guard-executed.lean.txt').read_text()
qs=[];web=rd('web-evidence.json')+[rd(n)for n in ['web-primary.json','web-supplementary.json','web-stacks.json','web-recent-window.json']]
for w in web:
 assert w['status']and w['summary']and len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 qs.extend(x['q']for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-27'in q and 'before:2026-10-28'in q for q in qs)
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
assert not v['composition']['strict_three_existing_call_term_verified']
assert not v['composition']['parent_project_helpers_counted_as_mathlib_blocks']and v['composition']['no_global_absence_claim']
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS199: full phases; fresh17; exactordered293;2value/0type;6clean native;15searchcells; fullcallers; Bhalfguard; currentmanifest/links/secrets.')
