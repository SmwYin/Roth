#!/usr/bin/env python3
"""Portable read-only validator: current manifest, scratch and integrated layouts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.sum_max_sub_le_index_det'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');f=rd('phase-evidence.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==207 and a['source']=='Roth/Theta.lean:376'
assert a['verdict']=='BORDERLINE-needs-human' and a['completed'] and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS'] and not a['production_edits']
assert a['assessment_date']=='2026-10-28' and f['mandatory_phases']==ph
assert (f['modern_idiom_rows'],f['proof_strategy_rows'],f['infrastructure_rows'])==(9,5,6)
assert len(f['statement_shape_checks'])==3 and f['verdict_questions']==3
assert f['full_declaring_module_read'] and f['full_declaring_module_lines']==985
assert f['callers_complete'] and f['full_module_native_replay'] and f['parent_reaim_checked']
assert not f['cost_used_as_verdict_factor'] and not f['maximality_claim']
assert f['all_named_literature_channels_attempted'] and f['web_general_queries']>=3
assert f['recent_arxiv_window']==['2021-10-28','2026-10-29']
keys={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert keys<=set(o) and o['type']==rd('native-type.json')['type']
for lemma in ['index_sub_weight_le_index_hasseDeriv',"Matrix.det_apply'",'index_prod','index_C_mul','le_index_sum']:
 assert lemma in o['how']
assert o['type'].startswith('∀ {τ : Type') and 'Fintype τ' in o['type']
assert 'Finsupp.degree (D μ) ≤ ↑μ' in o['type'] and 'max 0' in o['type']
assert not rd('native-type.json')['field_elision']
assert rd('completion.json')['status']=='COMPLETE/FROZEN'
# Always validate current copy-manifest, never substitute historical worker-copy-manifest.
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
assert not list(D.glob('*.lean'))
assert {'assessment.json','verification.json','overview-entry.json','validate.py','completion.json'}<=seen
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==5
prefix=(D/'det207-isolated-executed.lean.txt').read_text().splitlines()[:18]
assert len(prefix)==18 and prefix[-1]=='import Mathlib.Algebra.Order.Archimedean.Real.Basic'
disk=['import Mathlib.Algebra.Polynomial.Derivation','import Roth.LeanEval',
 'import Mathlib.LinearAlgebra.FreeModule.PID','import Mathlib.Algebra.Field.ULift',
 'import Mathlib.Data.Finsupp.Weight','import Mathlib.RingTheory.MvPolynomial.Localization',
 'import Mathlib.RingTheory.Localization.Integer','import Mathlib.RingTheory.Localization.FractionRing',
 'import Mathlib.Algebra.GCDMonoid.IntegrallyClosed']
for e in v['accepted']:
 rr=rd(e['receipt']);z=result(rr);s=(D/e['source']).read_text()
 assert not rr['result'].get('isError',False) and z['success'] and not z.get('timed_out')
 assert rr['request']==e['original_execution_request'] and isinstance(rr['elapsed_ms'],int)
 assert rr['elapsed_ms']>=0 and sha(D/e['source'])==e['source_sha256']
 assert max(map(len,s.splitlines()))<=100
 if e['format']=='raw':
  assert rr['request']['code']==s and s.splitlines()[:18]==prefix
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
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 assert e['required_info']
 for txt in e['required_info']:assert txt in info,(e['label'],txt)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
assert len(v['rejected'])==6 and len(v['historical'])==3
for e in v['rejected']+v['historical']:
 assert e['accepted'] is False and sha(D/e['source'])==e['source_sha256'] and e['reason']
 rr=rd(e['receipt']);z=result(rr);s=(D/e['source']).read_text()
 if e['format']=='raw':assert rr['request']['code']==s
 if e in v['rejected']:
  ds=z.get('diagnostics',z.get('items',[]))
  assert any(x['severity'] in ['error','warning'] for x in ds)
# Fresh source/pin baseline and exact source archives.
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source'] for x in fresh}
for x in fresh:
 assert x['matches_baseline'] and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for mod in ['Theta','Index']:assert sha(R/f'Roth/{mod}.lean')==sha(D/f'source-{mod}.lean.txt')
assert len((D/'source-Theta.lean.txt').read_text().splitlines())==985
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'] and sha(D/x['archive'])==sha(p)
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
assert rd('local-literature-search.json')['exit_code']==0
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
# Exact canonical order, including private modules, in every executed canonical source.
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name']for x in order})==293 and order[206]==rd('canonical-target.json')
assert order[206]['name']==N and order[206]['line']==376
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name'])for x in order]
for p in D.glob('*-executed.lean.txt'):
 s=p.read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S)
 if not arrays:continue
 assert len(arrays)==1
 items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
 actual=[('private',mod,nm) if mod else ('public',pub)for mod,nm,pub in items]
 assert actual==expected and len(actual)==len(set(actual))==293,p
for label in ['original','fullmodule']:
 z=result(rd('det207-'+label+'-receipt.json'));msgs=[x['message']for x in z['items']]
 assert 'DET207_AUDIT: requested=293; unique=293' in msgs
 assert 'DET207_AUDIT_PRESENT: present=293; values=293' in msgs
 assert [x.split(': ',1)[1]for x in msgs if x.startswith('DET207_DIRECT_CONSUMER:')]==['Roth.index_le_lem6']
 assert not [x for x in msgs if x.startswith('DET207_DIRECT_TYPE_CONSUMER:')]
for e in rd('canonical-gates.json')['checks']:
 z=rd(e['receipt']);assert z['exit_code']==0 and 'PASS exact293 unique source order:' in z['stdout']
 assert sha(D/e['source'])==e['source_sha256']
assert v['canonical_direct_consumers']==['Roth.index_le_lem6'] and not v['canonical_direct_type_consumers']
deps=o['project_dependencies'];assert isinstance(deps,list) and len(deps)==12
assert len(deps)==len(set(deps)) and set(deps)<={x['name']for x in order}
# Formal-search receipts are complete; index warming/error never establishes absence.
formal=[rd('search-'+str(i)+'.json')for i in range(12)]
assert {(x['form'],x['method'])for x in formal}=={(a,b)for a in ['current','standard','abstract']for b in ['Finder','Loogle','LeanSearch','local']}
for x in formal+[rd('reaim-'+str(i)+'.json')for i in range(4)]:
 assert x['request'] and x['status']=='fulfilled' and x['value']['response']['content']
for form in ['current','standard','abstract','reaim']:
 z=rd('rg-'+form+'.json');assert z['request'][0]=='rg' and z['exit_code'] in [0,1]
assert rd('rg-full-name.json')['exit_code']==1 and not rd('rg-full-name.json')['stdout']
for n in ['callers.json','inventory-callers.json','tracked-callers.json']:
 z=rd(n);assert z['exit_code']==0
 assert [int(x.split(':')[1])for x in z['stdout'].splitlines()]==[376,576]
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293
assert lex['occurrences']==[{'file':'Roth/Theta.lean','source_occurrence_lines':[376,576]}]
assert lex['callers']==[{'name':'Roth.index_le_lem6','file':'Roth/Theta.lean','line':576}]
inl=rd('inline-audit.json');assert inl['explicit_calls']==1 and not inl['simp_attribute']
assert not inl['same_full_statement_rederived_inline']
for x in inl['related_proof_bodies']:
 src=(R/x['file']).read_text().splitlines()
 assert (D/x['artifact']).read_text()=='\n'.join(src[x['start_line']-1:x['end_line']])+'\n'
assert rd('proof-body-audit.json')['diagnostic_fires']
c=v['composition'];assert not c['strict_three_existing_call_term_verified']
assert not c['parent_project_helpers_counted_as_mathlib_blocks'] and not c['new_helpers_counted_as_existing']
assert c['actual_caller_replays']==c['actual_call_occurrences']==c['direct_weakened_caller_replays']==1
assert c['full_module_replay'] and c['no_global_absence_claim']
s=(D/'det207-isolated-executed.lean.txt').read_text()
for tac in ['exact?','simp','positivity']:assert 'fail_if_success solve | '+tac in s
assert s.index('fail_if_success')<s.index("  rw [Matrix.det_apply'] at hdet ⊢")
s=(D/'det207-group-executed.lean.txt').read_text()
for t in ['[AddCommGroup Γ]','[PartialOrder Γ]','[IsOrderedAddMonoid Γ]']:assert t in s
s=(D/'det207-fullmodule-executed.lean.txt').read_text()
for t in ['theorem indexDet','theorem weak','theorem directWeakCaller','theorem actualNonzeroGuard','theorem Θ_lt','let D : Fin 2 → (Empty →₀ ℕ)','simp [hd]']:assert t in s
assert '(hδ : ∀ μ, weight (r ∘ some) (D μ) ≤ δ)' in s
assert 'exact Det207Project.weak D hdet α hr' in s
# Web archives contain only exact requests/digests/locators and original summaries.
qs=[]
for i in range(4):
 w=rd('web-'+str(i)+'.json');assert w['status']=='returned' and w['assessment_date']=='2026-10-28'
 assert len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 assert 'result' not in w and 'response' not in w and w['locators'] and w['sources'] and w['summary']
 for x in w['sources']:assert x['title'] and x['url'].startswith('https://') and x['locator']
 qs.extend(x['q']for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in qs)
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
for t in ['not closure tests for the complete old','IsDomain is a sufficient','actual target guard','not a cost-based downgrade']:assert t in s
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS207: allphases; fresh17; ordered293;1value/0type;5clean native;15searchcells+5reaim; fullmodule/actualcaller/weakcaller; orderedgroup/perrow/actualHasseguard; currentmanifest/links/secrets.')
