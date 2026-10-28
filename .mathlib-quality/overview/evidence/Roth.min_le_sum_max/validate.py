#!/usr/bin/env python3
"""Portable, read-only validation of current worker/integrated evidence."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.min_le_sum_max';ST='minsum206-'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
f=rd('phase-evidence.json');ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==206 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human' and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS'] and not a['production_edits']
assert a['assessment_date']=='2026-10-28' and f['mandatory_phases']==ph
assert (f['modern_idiom_rows'],f['proof_strategy_rows'],f['infrastructure_rows'])==(9,5,6)
assert len(f['statement_shape_checks'])==3 and f['verdict_questions']==3
assert not f['cost_used_as_verdict_factor'] and not f['maximality_claim']
assert not f['optimal_constant_claim'] and not f['source_positivity_size_premises']
assert f['full_declaring_module_read'] and f['full_declaring_module_lines']==985
assert f['full_module_native_replay'] and f['callers_complete']
assert f['all_named_literature_channels_attempted']
assert f['recent_arxiv_window']==['2021-10-28','2026-10-29']
assert f['pre_helper_gate_only_in']==ST+'composition-executed.lean.txt'
keys={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert keys<=set(o) and o['type']==rd('native-type.json')['type']
assert o['type'].startswith('∀ {θ : ℝ} {rp : ℕ} (l : ℕ),')
assert 'min (↑l * θ / 2) (↑rp * θ ^ 2 / 3)' in o['type']
assert not rd('native-type.json')['field_elision'] and len(o['project_dependencies'])==3
assert rd('completion.json')['status']=='COMPLETE/FROZEN'
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/' in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py','completion.json'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==8 and len(v['rejected'])==2
prefix=(D/(ST+'isolated-executed.lean.txt')).read_text().splitlines()[:18]
assert len(prefix)==18 and prefix[-1]=='import Mathlib.Algebra.Order.Archimedean.Real.Basic'
disk=['import Mathlib.Algebra.Polynomial.Derivation','import Roth.LeanEval',
 'import Mathlib.LinearAlgebra.FreeModule.PID','import Mathlib.Algebra.Field.ULift',
 'import Mathlib.Data.Finsupp.Weight','import Mathlib.RingTheory.MvPolynomial.Localization',
 'import Mathlib.RingTheory.Localization.Integer','import Mathlib.RingTheory.Localization.FractionRing',
 'import Mathlib.Algebra.GCDMonoid.IntegrallyClosed']
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success'] and not z.get('timed_out') and isinstance(r['elapsed_ms'],int)
 assert r['elapsed_ms']>=0 and r['request']==e['original_execution_request']
 p=D/e['source'];s=p.read_text();assert sha(p)==e['source_sha256']
 assert max(map(len,s.splitlines()))<=100
 if e['format']=='raw':
  assert r['request']['code']==s and s.splitlines()[:18]==prefix
  assert not re.search(r'^import Roth\b',s,re.M) and '#check_failure '+N in s
  ds=z['diagnostics']
 else:
  assert z['partial'] is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies') and s.splitlines()[:9]==disk
  ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message'] for x in ds)):
  assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
 info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 assert e['required_info']
 for txt in e['required_info']:assert txt in info,(e['label'],txt)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['rejected']:
 assert e['accepted'] is False and sha(D/e['source'])==e['source_sha256']
 r=rd(e['receipt']);assert r['request']['code']==(D/e['source']).read_text()
 assert result(r)['success'] is False
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source'] for x in fresh}
for x in fresh:assert x['matches_baseline'] and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'] and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
assert len((D/'source-Theta.lean.txt').read_text().splitlines())==985
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
assert rd('local-literature-search.json')['exit_code']==0
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name'] for x in order})==293 and order[205]==rd('canonical-target.json')
assert set(o['project_dependencies'])<={x['name'] for x in order}
assert len(o['project_dependencies'])==len(set(o['project_dependencies']))
assert order[205]['name']==N and order[205]['line']==362
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
for label in ['original','fullmodule-initial','fullmodule']:
 s=(D/(ST+label+'-executed.lean.txt')).read_text()
 arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
 items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
 actual=[('private',mod,nm) if mod else ('public',pub) for mod,nm,pub in items]
 assert actual==expected and len(actual)==len(set(actual))==293
 z=result(rd(ST+label+'-receipt.json'));msgs=[x['message'] for x in z['items']]
 assert 'MINSUM206_AUDIT: requested=293; unique=293' in msgs
 assert 'MINSUM206_AUDIT_PRESENT: present=293; values=293' in msgs
 assert [x.split(': ',1)[1] for x in msgs if x.startswith('MINSUM206_DIRECT_CONSUMER:')]==['Roth.index_le_lem6']
 assert not [x for x in msgs if x.startswith('MINSUM206_DIRECT_TYPE_CONSUMER:')]
for e in rd('canonical-gates.json')['checks']:
 z=rd(e['receipt']);assert z['exit_code']==0 and 'PASS exact293 unique source order:' in z['stdout']
 assert sha(D/e['source'])==e['source_sha256']
assert v['canonical_direct_consumers']==['Roth.index_le_lem6'] and v['canonical_direct_type_consumers']==[]
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
formal=[rd('search-'+str(i)+'.json') for i in range(14)]
assert {(x['form'],x['method']) for x in formal}=={(a,b) for a in ['current','standard','abstract'] for b in ['Finder','Loogle','LeanSearch','local']}
for i,x in enumerate(formal):
 assert x['request'] and x['status']=='fulfilled'
 assert x['value']['response'].get('isError',False)==(i in [1,5])
for form in ['current','standard','abstract']:
 z=rd('rg-'+form+'.json');assert z['request'][0]=='rg' and z['exit_code'] in [0,1]
assert rd('rg-full-name.json')['exit_code']==1 and rd('rg-full-name.json')['stdout']==''
assert rd('rg-finite-cutoff.json')['exit_code']==0
for n in ['callers.json','inventory-callers.json','tracked-callers.json']:
 z=rd(n);assert z['exit_code']==0
 assert [int(x.split(':')[1]) for x in z['stdout'].splitlines()]==[362,586]
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293
assert lex['occurrences']==[{'file':'Roth/Theta.lean','source_occurrence_lines':[362,586]}]
assert lex['callers']==[{'name':'Roth.index_le_lem6','file':'Roth/Theta.lean','line':586}]
inline=rd('inline-audit.json');assert inline['explicit_calls']==1 and not inline['simp_attribute']
assert not inline['same_full_statement_rederived_inline'] and len(inline['related_proof_bodies'])==5
for x in inline['related_proof_bodies']:
 src=(R/x['file']).read_text().splitlines()
 assert (D/x['artifact']).read_text()=='\n'.join(src[x['start_line']-1:x['end_line']])+'\n'
pb=rd('proof-body-audit.json');assert pb['diagnostic_fires'] and pb['real_named_object_occurrences']==0
c=v['composition'];assert not c['strict_three_existing_call_term_verified']
assert not c['parent_project_helpers_counted_as_mathlib_blocks'] and not c['new_helpers_counted_as_existing']
assert c['actual_caller_replays']==c['actual_call_occurrences']==c['inline_caller_replays']==1
assert c['full_module_replay'] and c['no_global_absence_claim']
s=(D/(ST+'composition-executed.lean.txt')).read_text()
assert s.index('fail_if_success solve | exact?')<s.index('  have mul_div_two_le_sum_max_aux')
assert 'exact (min_le_left' in s and 'exact (min_le_right' in s
s=(D/(ST+'finite-executed.lean.txt')).read_text()
assert '[FloorSemiring K]' not in s and 'Nat.findGreatest_spec' in s
assert 'Nat.findGreatest_is_greatest' in s and 'Nat.cast_succ' in s
assert 'hsum / 2 + sq_nonneg a / 6' not in s and 'rp * θ ^ 2 / 2' in s
assert 'Nat.cast_nonneg rp' in s and 'min_le_min_left' in s
s=(D/(ST+'isolated-executed.lean.txt')).read_text()
for nm in ['noMinLinearFails','noMinQuadraticFails','strictFails','noMaxFails','negativeScale']:
 assert 'theorem '+nm in s
s=(D/(ST+'fullmodule-executed.lean.txt')).read_text()
assert '  MinSum206Finite.originalViaStronger l' in s and 'theorem inlineConsumer' in s
assert s.count('theorem index_le_lem6')==1 and 'theorem Θ_lt' in s
qs=[]
for i in range(4):
 w=rd('web-'+str(i)+'.json');assert w['status']=='returned' and w['assessment_date']=='2026-10-28'
 assert len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 assert 'result' not in w and 'response' not in w and w['locators'] and w['sources'] and w['summary']
 for x in w['sources']:assert x['title'] and x['url'].startswith('https://') and x['locator']
 qs.extend(x['q'] for x in w['request']['search_query'])
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:
 assert any(q.startswith(t) for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-28' in q and 'before:2026-10-29' in q for q in qs)
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 pfx='../evidence/'+N+'/'
 assert link.startswith(pfx) and (D/link[len(pfx):]).is_file(),link
assert all(str(i)+'. ' in s for i in range(1,4))
assert 'before any new helper declarations' in s and 'not ordered the same way for negative rp' in s
assert 'Nat.cast_nonneg' in s and 'No sharp-constant or maximal-generality assertion' in s
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS206: allphases; fresh17; exactordered293;1value/0type;8clean native;15searchcells+retries; fullmodule/caller/inline; generic/noFloor/constant2/guards; currentmanifest/links/secrets.')
