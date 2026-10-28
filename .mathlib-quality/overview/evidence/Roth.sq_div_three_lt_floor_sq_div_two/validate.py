#!/usr/bin/env python3
"""Portable read-only validation; use current copy manifest in either layout."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.sq_div_three_lt_floor_sq_div_two';ST='floorcompare202-'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');f=rd('phase-evidence.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==202 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human'and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS')and not a['unresolved']and not v['unresolved']
assert a['assessment_date']=='2026-10-28'and a['root_acceptance']in ['pending','PASS']
assert f['mandatory_phases']==ph and f['modern_idiom_rows']==9 and f['proof_strategy_rows']==5
assert f['infrastructure_rows']==6 and len(f['statement_shape_checks'])==3
assert f['verdict_questions']==3 and not f['cost_used_as_verdict_factor']
assert f['full_declaring_module_read']and f['full_declaring_module_lines']==985
assert f['full_module_native_replay']and f['callers_complete']and f['all_named_literature_channels_attempted']
assert f['recent_arxiv_window']==['2021-10-28','2026-10-29']
assert not f['maximality_claim']and not f['optimal_cutoff_claim']
keys={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert keys<=set(o)and o['type']==rd('native-type.json')['type']
assert o['type']=='∀ {a : ℝ}, 10 < a → a ^ 2 / 3 < ↑⌊a⌋₊ ^ 2 / 2'
assert o['project_dependencies']==[]and rd('native-type.json')['field_elision']is False
assert rd('completion.json')['status']=='COMPLETE/FROZEN'
pb=rd('proof-body-audit.json');assert pb['diagnostic_fires']and pb['real_named_object_occurrences']==0 and pb['abstract_rounding_call_occurrences']==1 and pb['substantive_lines']==1
m=rd('copy-manifest.json');seen=set();assert m['declaration']==N
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py','completion.json'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==4 and v['rejected']==[]
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success']and not z.get('timed_out')and isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 assert r['request']==e['original_execution_request']
 p=D/e['source'];s=p.read_text();assert sha(p)==e['source_sha256']
 assert max(map(len,s.splitlines()))<=100
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s
  ds=z['diagnostics']
  prefix=(D/(ST+'isolated-executed.lean.txt')).read_text().splitlines()[:18]
  assert s.splitlines()[:18]==prefix and len(prefix)==18
  assert prefix[-1]=='import Mathlib.Algebra.Order.Archimedean.Real.Basic'
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')and not z.get('failed_dependencies')
  ds=z['items'];assert s.splitlines()[:9]==[
   'import Mathlib.Algebra.Polynomial.Derivation','import Roth.LeanEval',
   'import Mathlib.LinearAlgebra.FreeModule.PID','import Mathlib.Algebra.Field.ULift',
   'import Mathlib.Data.Finsupp.Weight','import Mathlib.RingTheory.MvPolynomial.Localization',
   'import Mathlib.RingTheory.Localization.Integer','import Mathlib.RingTheory.Localization.FractionRing',
   'import Mathlib.Algebra.GCDMonoid.IntegrallyClosed']
 assert not [x for x in ds if x.get('severity')in ['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 assert e['required_info']
 for txt in e['required_info']:assert txt in info,(e['label'],txt)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline']and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
assert len((D/'source-Theta.lean.txt').read_text().splitlines())==985
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
assert rd('local-literature.json')['exit_code']==0
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and len({x['name']for x in order})==293
assert order[201]==rd('canonical-target.json')and order[201]['name']==N and order[201]['line']==300
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for label in ['original','fullmodule']:
 s=(D/(ST+label+'-executed.lean.txt')).read_text()
 arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
 items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
 actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
 assert actual==expected and len(actual)==len(set(actual))==293
 z=result(rd(ST+label+'-receipt.json'))
 for msg in ['FLOORCOMPARE202_AUDIT: requested=293; unique=293','FLOORCOMPARE202_AUDIT_PRESENT: present=293; values=293']:
  assert any(x['message']==msg for x in z['items'])
 assert not [x for x in z['items']if x['message'].startswith(('FLOORCOMPARE202_DIRECT_CONSUMER:','FLOORCOMPARE202_DIRECT_TYPE_CONSUMER:'))]
assert len(rd('canonical-gates.json')['checks'])==2
for e in rd('canonical-gates.json')['checks']:
 assert e['exit_code']==0 and 'PASS exact293 unique source order:'in e['stdout']
 assert e['source_sha256']==sha(D/Path(e['request'][-1]).name)
assert v['canonical_direct_consumers']==v['canonical_direct_type_consumers']==[]
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
formal=[rd('search-'+str(i)+'.json')for i in range(12)]
assert {(x['form'],x['method'])for x in formal}=={(a,b)for a in ['current','standard','abstract']for b in ['Finder','Loogle','LeanSearch','local']}
for x in formal:assert x['request']and x['status']=='fulfilled'and not x['value']['response'].get('isError',False)
for form in ['current','standard','abstract']:
 x=rd('rg-'+form+'.json');assert x['request'][0]=='rg'and x['exit_code']in [0,1]
full=rd('rg-full-name.json');assert full['request']==['rg','-n',r'\bsq_div_three_lt_floor_sq_div_two\b','.lake/packages/mathlib/Mathlib']
assert full['exit_code']==1 and full['stdout']==''
assert rd('callers.json')['stdout']==rd('inventory-callers.json')['stdout']==rd('tracked-callers.json')['stdout']
assert rd('callers.json')['stdout'].splitlines()==['Roth/Theta.lean:300:theorem sq_div_three_lt_floor_sq_div_two {a : ℝ} (ha : 10 < a) :']
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293 and lex['callers']==[]
assert len(lex['occurrences'])==1 and lex['occurrences'][0]['source_occurrence_lines']==[300]
inline=rd('inline-audit.json');assert inline['explicit_calls']==0 and not inline['simp_attribute']
assert len(inline['related_proof_bodies'])==4 and not inline['same_full_statement_rederived_inline']
for x in inline['related_proof_bodies']:
 src=(R/x['file']).read_text().splitlines()
 assert (D/x['artifact']).read_text()=='\n'.join(src[x['start_line']-1:x['end_line']])+'\n'
src=(D/'source-Theta.lean.txt').read_text();body=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
assert body in(D/(ST+'fullmodule-executed.lean.txt')).read_text()
s=(D/(ST+'isolated-executed.lean.txt')).read_text()
assert s.index('fail_if_success solve | exact?')<s.index('theorem genericOriginal')
for nm in ['closureGuards','genericOriginal','floorFree','genericFive','realFive','thresholdFourFails','noLowerBoundFails','realSpecialization']:assert 'theorem '+nm in s
assert '[FloorSemiring K]'in s and '(ha : 5 ≤ a)'in s
assert '(ha : 0 ≤ a) (hn : 5 ≤ n) (hlt : a < n + 1)'in s
assert 'Nat.le_floor ha'in s and '(99 / 20 : ℝ)'in s and ' = 4 :='in s
s=(D/(ST+'composition-executed.lean.txt')).read_text()
for nm in ['viaSubOne','viaSquareMonotonicity','negativeInputFails','sqrtComparison']:assert 'theorem '+nm in s
assert 'sq_lt_sq₀'in s and 'Nat.sub_one_lt_floor a'in s and 'Real.sqrt_lt\''in s
qs=[]
for i in range(4):
 w=rd(f'web-{i}.json');assert w['status']=='returned'and isinstance(w['summary'],str)and w['assessment_date']=='2026-10-28'
 assert len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 assert 'result'not in w and 'response'not in w and w['locators']and w['sources']
 for src in w['sources']:assert src['title']and src['url'].startswith('https://')and src['locator']
 qs.extend(x['q']for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-28'in q and 'before:2026-10-29'in q for q in qs)
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
assert all(str(i)+'. 'in s for i in range(1,4))
assert '71913'in s and 'not a complete pretty-printed kernel-body dump'in s
assert 'does **not** prove the strict intermediate'in s and 'consider removing this unused public endpoint'in s
c=v['composition'];assert not c['strict_three_existing_call_term_verified']and not c['parent_project_helpers_counted_as_mathlib_blocks']and not c['new_helpers_counted_as_existing']
assert c['actual_caller_replays']==c['actual_call_occurrences']==0 and c['full_module_replay']and c['no_global_absence_claim']
assert c['all_actual_floor_premises_discharged']and c['exact_search_before_new_helpers']
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS202: allphases; fresh17; exactordered293;0value/0type;4clean native;15searchcells; fullmodule; generic/cutoff5/necessity/compositions; currentmanifest/links/secrets.')
