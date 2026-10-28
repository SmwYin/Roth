#!/usr/bin/env python3
"""Portable read-only validation of current evidence, not historical worker hashes."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.one_le_lem6M'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==200 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human'and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS')and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in ['pending','PASS']
f=rd('phase-evidence.json');assert f['mandatory_phases']==ph and f['modern_idiom_rows']==9 and f['proof_strategy_rows']==5 and f['infrastructure_rows']==6
assert len(f['statement_shape_checks'])==3 and f['verdict_questions']<=5 and not f['cost_used_as_verdict_factor']
assert f['full_declaring_module_read']and f['full_module_native_replay']and f['callers_complete']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']
assert o['type']=='∀ (p r₁ : ℕ) {B : ℝ}, 1 ≤ B → ∀ (l : ℕ), 1 ≤ Roth.lem6M p r₁ B l'
assert o['project_dependencies']==['Roth.lem6M']
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
assert len(v['accepted'])==5 and len(v['rejected'])==5
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success']and not z.get('timed_out')and isinstance(r['elapsed_ms'],int)
 assert r['elapsed_ms']>=0 and r['request']==e['original_execution_request']
 p=D/e['source'];s=p.read_text();assert sha(p)==e['source_sha256']
 assert max(map(len,s.splitlines()))<=100
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  ds=z['diagnostics'];assert '#check_failure '+N in s
  assert '#check_failure Roth.lem6M'in s
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
for e in v['rejected']:
 r=rd(e['receipt']);s=(D/e['source']).read_text();assert r['request']['code']==s
 assert result(r)['success']is False and e['reason']
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline']and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and len({x['name']for x in order})==293
assert order[199]==rd('canonical-target.json')and order[199]['name']==N and order[199]['line']==279
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for label in ['original','fullcaller','fullmodule']:
 s=(D/f'onelem6m200-{label}-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
 items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
 actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
 assert actual==expected and len(actual)==len(set(actual))==293
for e in rd('canonical-gates.json')['checks']:
 assert e['exit_code']==0 and 'PASS exact293 unique source order:'in e['stdout']
 assert e['source_sha256']==sha(D/Path(e['request'][-1]).name)
cons=['_private.Roth.Theta.0.Roth.theta_phi_lt_aux']
assert v['canonical_direct_consumers']==cons and v['canonical_direct_type_consumers']==[]
z=result(rd('onelem6m200-original-receipt.json'))
for marker,ns in [('ONELEM6M200_DIRECT_CONSUMER: ',cons),('ONELEM6M200_DIRECT_TYPE_CONSUMER: ',[])]:
 assert [x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
for msg in ['ONELEM6M200_AUDIT: requested=293; unique=293','ONELEM6M200_AUDIT_PRESENT: present=293; values=293']:
 assert any(x['message']==msg for x in z['items'])
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
formal=[rd('search-'+str(i)+'.json')for i in range(12)]
assert {(x['form'],x['method'])for x in formal}=={(f,m)for f in ['current','standard','abstract']for m in ['Finder','Loogle','LeanSearch','local']}
for x in formal:
 assert x['request']and x['status']=='fulfilled'
 assert not x['value']['response'].get('isError',False)
for f in ['current','standard','abstract']:assert rd('rg-'+f+'.json')['exit_code']in [0,1]
assert sorted(rd('callers.json')['stdout'].splitlines())==sorted(rd('inventory-callers.json')['stdout'].splitlines())
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293
assert [x['name']for x in lex['callers']]==['Roth.theta_phi_lt_aux']
assert lex['callers'][0]['source_occurrence_lines']==[866]
s=(D/'onelem6m200-fullcaller-executed.lean.txt').read_text()
assert 'theorem caller'in s and 'OneLem6M200Project.bound'in s
bound=s.split('namespace OneLem6M200Project',1)[1].split('end OneLem6M200Project',1)[0]
assert 'one_le_lem6M'not in bound and 'theorem bound'in bound and 'rw [lem6M]'in bound
src=(D/'source-Theta.lean.txt').read_text();body=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
assert body in(D/'onelem6m200-fullmodule-executed.lean.txt').read_text()
s=(D/'onelem6m200-isolated-executed.lean.txt').read_text()
for nm in ['directReal','genericScalar','listReal','abstractProduct','powerPremise','zeroExponent','baseAssumptionNecessary']:assert 'theorem '+nm in s
assert '(hBl : 1 ≤ B ^ l)'in s and 'List.one_le_prod hf'in s
s=(D/'onelem6m200-weak-executed.lean.txt').read_text();assert '[Semiring K] [PartialOrder K] [IsOrderedRing K]'in s and 'Nat.mono_cast'in s and 'theorem genericWeak'in s
qs=[]
for i in range(5):
 w=rd(f'web-{i}.json');assert w['status']and w['summary']and w['locators']
 assert len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 assert 'result'not in w
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
assert all(str(i)+'. 'in s for i in range(1,4))
c=v['composition'];assert not c['strict_three_existing_call_term_verified']and not c['parent_project_helpers_counted_as_mathlib_blocks']
assert c['actual_caller_replays']==1 and c['list_product_full_actual_factor_bindings']and c['full_module_replay']and c['no_global_absence_claim']
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS200: full phases; fresh17; exactordered293;1value/0type;5clean native;15searchcells; fullcaller/module; weak-order scalar; guards; currentmanifest/links/secrets.')
