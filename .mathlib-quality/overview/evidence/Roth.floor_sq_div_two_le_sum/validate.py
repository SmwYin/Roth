#!/usr/bin/env python3
"""Portable, read-only current-manifest validation in scratch or integrated layouts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.floor_sq_div_two_le_sum'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');f=rd('phase-evidence.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==201 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human'and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS')and not a['unresolved']and not v['unresolved']
assert a['assessment_date']=='2026-10-28'and a['root_acceptance']in ['pending','PASS']
assert f['mandatory_phases']==ph and f['modern_idiom_rows']==9 and f['proof_strategy_rows']==5
assert f['infrastructure_rows']==6 and len(f['statement_shape_checks'])==3
assert f['verdict_questions']==3 and not f['cost_used_as_verdict_factor']
assert f['full_declaring_module_read']and f['full_declaring_module_lines']==985
assert f['full_module_native_replay']and f['callers_complete']and f['all_named_literature_channels_attempted']
assert f['recent_arxiv_window']==['2021-10-28','2026-10-29']
keys={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert keys<=set(o)and o['type']==rd('native-type.json')['type']
assert o['type']=='∀ {a : ℝ}, 0 ≤ a → ↑⌊a⌋₊ ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ↑ν)'
assert o['project_dependencies']==[]and rd('native-type.json')['field_elision']is False
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
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==4 and len(v['rejected'])==5
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
  prefix=(D/'floorsum201-isolated-executed.lean.txt').read_text().splitlines()[:18]
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
 for text in e['required_info']:assert text in info,(e['label'],text)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['rejected']:
 r=rd(e['receipt']);assert r['request']['code']==(D/e['source']).read_text()
 assert result(r)['success']is False and e['reason']
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
assert order[200]==rd('canonical-target.json')and order[200]['name']==N and order[200]['line']==289
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for label in ['original','fullmodule']:
 s=(D/f'floorsum201-{label}-executed.lean.txt').read_text()
 arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
 items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
 actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
 assert actual==expected and len(actual)==len(set(actual))==293
 z=result(rd(f'floorsum201-{label}-receipt.json'))
 for msg in ['FLOORSUM201_AUDIT: requested=293; unique=293','FLOORSUM201_AUDIT_PRESENT: present=293; values=293']:
  assert any(x['message']==msg for x in z['items'])
 assert not [x for x in z['items']if x['message'].startswith(('FLOORSUM201_DIRECT_CONSUMER:','FLOORSUM201_DIRECT_TYPE_CONSUMER:'))]
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
assert rd('callers.json')['stdout']==rd('inventory-callers.json')['stdout']==rd('tracked-callers.json')['stdout']
assert rd('callers.json')['stdout'].splitlines()==['Roth/Theta.lean:289:theorem floor_sq_div_two_le_sum {a : ℝ} (ha : 0 ≤ a) :']
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293 and lex['callers']==[]
assert len(lex['occurrences'])==1 and lex['occurrences'][0]['source_occurrence_lines']==[289]
inline=rd('inline-audit.json');assert inline['explicit_calls']==0 and not inline['simp_attribute']
assert len(inline['related_proof_bodies'])==2 and not inline['same_full_statement_rederived_inline']
src=(D/'source-Theta.lean.txt').read_text();body=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
assert body in(D/'floorsum201-fullmodule-executed.lean.txt').read_text()
s=(D/'floorsum201-isolated-executed.lean.txt').read_text()
for nm in ['genericFloor','cutoff','ringCutoff','exactSum','nonnegNecessary','closureGuards']:assert 'theorem '+nm in s
assert '[CommRing K] [PartialOrder K] [IsOrderedRing K]'in s and '[FloorSemiring K]'in s
s=(D/'floorsum201-composition-executed.lean.txt').read_text()
assert s.index('fail_if_success solve | exact?')<s.index('theorem genericFloor')
for nm in ['ringFloor','viaRingCutoff','viaExactSum','genericRouteGuard']:assert 'theorem '+nm in s
assert 'ringCutoff (K := ℝ) ⌊a⌋₊ (Nat.floor_le ha)'in s
assert 'Nat.cast_nonneg (α := ℝ) ⌊a⌋₊'in s
assert '[Ring K]'in(D/'floorsum201-ring-probe-executed.lean.txt').read_text()
assert any('CommSemiring K'in x['message']for x in result(rd('floorsum201-ring-probe-receipt.json'))['diagnostics'])
qs=[]
for i in range(5):
 w=rd(f'web-{i}.json');assert w['status']=='returned'and w['summary']and w['assessment_date']=='2026-10-28'
 assert len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 assert 'result'not in w and 'response'not in w
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
assert 'normalization infrastructure'in s and 'natural casts are central'in s
assert all(str(i)+'. 'in s for i in range(1,4))
c=v['composition'];assert not c['strict_three_existing_call_term_verified']and not c['parent_project_helpers_counted_as_mathlib_blocks']
assert c['actual_caller_replays']==c['actual_call_occurrences']==0 and c['full_module_replay']and c['no_global_absence_claim']
assert c['all_actual_floor_and_sum_premises_discharged']and c['exact_search_before_new_helpers']
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS201: full phases; fresh17; exactordered293;0value/0type;4clean native;15searchcells; fullmodule; verified generality/necessity/bridges; currentmanifest/links/secrets.')
