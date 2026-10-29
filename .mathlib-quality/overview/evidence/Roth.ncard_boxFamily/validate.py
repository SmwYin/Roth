#!/usr/bin/env python3
"""Read-only canonical246 validation, scratch or integrated; current manifest is authoritative."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.ncard_boxFamily'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
p=D/'report.md';report=p if p.is_file()else D.parent.parent/'mathlibable'/(N+'.md')
scope=rd('root-prefix-scope-note.json');assert scope['active_prefix_imports']==19 and not scope['shared18_changed'] and not scope['persistent_disk9_changed'] and not scope['production_changed']
ledger=rd('final-validation.json');assert ledger['status']=='PASS'and ledger['actual_executions']
assert {x['layout']for x in ledger['executions']}=={'scratch','simulated-integrated'}
assert all(x['exit_code']==0 and 'PASS246:'in x['stdout']for x in ledger['executions'])
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');nt=rd('native-type.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==246 and a['completed']and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS')and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']and a['verdict']=='BORDERLINE-needs-human'
assert len(a['questions'])==3
required={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert required<=set(o)and o['type']==nt['type']
assert 'Finite ↑(Function.support r)'in o['type']and'(Roth.boxFamily r B).ncard'in o['type']
assert o['project_dependencies']==['Roth.boxFamily','Roth.boxFamily_eq_image_finsupp_aux']
assert nt['kernel_type_project_constants']==['Roth.boxFamily']
assert nt['kernel_body_project_constants']==['Roth.boxFamily','_private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux']
assert nt['printer_elision']and nt['elided_characters']==80823 and not nt['full_kernel_body_available']
assert nt['compact_body_complete']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 seen.add('report.md'if p==report else p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {e['label']for e in v['accepted']}=={'original','isolated','project','composition'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(r);assert not r['result'].get('isError',False)
 assert z['success']and not z['timed_out'];src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256']and r['request']==e['original_execution_request']
 assert isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and s.startswith((D/'isolated-active-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==19;ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')and not z.get('failed_dependencies')
  ds=z['items'];assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==9
 assert not[x for x in ds if x.get('severity')in['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for marker in e['required_info']:assert marker in info,(e['label'],marker)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
 if e['label']=='original':assert '80823 characters elided'in info
 else:assert not any('characters elided'in x['message']for x in ds)
assert len(v['rejected'])==6 and len(v['warming'])==1
assert result(rd('original-warming-receipt.json'))['partial']is True
for e in v['rejected']:
 r=rd(e['receipt']);z=result(r);assert any(x['severity']in['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 assert (D/e['source']).is_file()
 if 'code'in r['request']:assert r['request']['code']==(D/e['source']).read_text()
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path']for x in fresh}
for x in fresh:
 assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
assert sha(R/'Roth/MainLemma.lean')==sha(D/'source-MainLemma.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert '\\label{roth:eq43}'in(D/'local-excerpt.tex.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and len({x['name']for x in order})==293
assert order[245]==rd('canonical-entry.json')and order[245]['name']==N and order[245]['line']==311
progress=rd('accepted-verdict-snapshot.json');assert len(progress['completed_declarations'])==245
assert {x['declaration']for x in progress['completed_declarations']}=={x['name']for x in order[:245]}
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('BOX246_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),('BOX246_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['Roth.exists_ne_modByMonic_eq']and not v['canonical_direct_type_consumers']
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Box246Original\nopen Roth',1).replace('end Roth','end Box246Original');body=re.sub(r'\bncard_boxFamily\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
assert len(re.findall(r'^import ',(D/'isolated-prefix.lean.txt').read_text(),re.M))==18
assert (D/'isolated-active-prefix.lean.txt').read_text()==(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.Data.Finsupp.Interval\n'
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['request']['query']and not f['result'].get('isError',False)
  assert 'items'in f['result']['structuredContent']
  if method=='local_search':assert f['result']['structuredContent']['index']=='error'
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1]and not f['stderr']
assert rd('full-name-search.json')['exit_code']==1
rg=rd('source-search.json');gg=rd('tracked-source-search.json')
assert rg['exit_code']==gg['exit_code']==0 and sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['executable_occurrences']==cs['distinct_declarations']==1 and cs['external_to_file']==0
for c in cs['callers']:
 assert c['source'].strip()=='\n'.join((R/c['file']).read_text().splitlines()[c['line']-1:c['end_line']]).strip()
 assert hashlib.sha256(c['source'].encode()).hexdigest()==c['sha256']
 assert len(re.findall(r'\bncard_boxFamily\b',c['body']))==1
pj=(D/'project-executed.lean.txt').read_text()
# Independently extract the exact literal inline proof, without executing a mutating preparer.
tree=ast.parse((D/'prepare_project.py').read_text());new=next(ast.literal_eval(n.value)for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='new'for t in n.targets))
assert cs['callers'][0]['source'].replace('ncard_boxFamily,',new)in pj
assert '@Roth.exists_ne_modByMonic_eq = @Box246Project.exists_ne_modByMonic_eq := rfl'in pj
assert '@Roth.ncard_boxFamily = @ncard_original := rfl'in pj
assert 'exact_mod_cast hcount'in pj and 'Fintype.exists_ne_map_eq_of_card_lt F'in pj
iso=(D/'isolated-executed.lean.txt').read_text()
assert '[CommSemiring R]'in iso and '(ht : ∀ d ∉ Finset.Iic r, 0 ∈ t d)'in iso
assert 'theorem representation'in iso and 'theorem ncard_family'in iso and 'Finset.card_finsupp'in iso
for t in['zero_coefficient_bound','zero_degree','empty_variables','infinite_variables_finite_support','infinite_family','support_needed']:
 assert "'Box246Project."+t+"' depends on axioms:"in str(result(rd('project-receipt.json')))
assert 'fail_if_success exact Finset.card_finsupp _ _'in pj
assert 'fail_if_success solve | simp only [boxFamily]'in pj
comp=(D/'composition-executed.lean.txt').read_text()
assert 'theorem image_count'in comp and 'theorem simp_original'in comp
assert 'have hp : (Finset.Iic'in comp and 'simp only [box246Representation'in comp
inv=rd('source-inventory.json');assert inv['exit_code']==0
assert {x['file']for x in order}<=(set(inv['stdout'].splitlines())|{'Roth.lean'})
queries=[]
for name in['web-general','web-channels','web-recent','web-primary','web-correction']:
 w=rd(name+'.json');assert re.fullmatch('[0-9a-f]{64}',w['raw_response_sha256'])and w['raw_response_bytes']>0
 assert w['status'].startswith('returned')and w['summary']and w['full_web_body_archived']is False
 for x in w['titles']:assert x['url'].startswith('https://')and'?'not in x['url']and'\\'not in x['url']
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-29 before:2026-10-30'in q for q in queries)
p=rd('preparation-checks.json');assert p['canonical_gate']['exit_code']==0 and p['all_sources_inspected_before_execution']
assert all(x['exit_code']==0 and x['source_read_before_native']for x in p['observed_pre_execution'])
c=v['composition'];assert not c['strict_existing_mathlib_composition_verified']and not c['new_generic_is_existing_mathlib']
assert c['abstract_existing_image_law_verified']and c['generic_semiring_finite_coefficients_verified']and c['closing_simp_verified']
assert c['original_recovery_verified']and c['actual_caller_replays']==1 and c['full_body_inline_success']and c['inline_private_bridge_retained']
assert all(v['generality'][k] for k in ['off_box_zero_only','no_Fintype_sigma_restriction','support_wholesale_removal_refuted','B_zero_no_support'])
assert v['generality']['mechanical_Int_typeclass_weakening_claimed'] is False
s=report.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
assert len(re.findall(r'^\| [1-9] \|',s.split('## Phase 4c')[1].split('## Phase 4.5')[0],re.M))==9
assert len(re.findall(r'^\| [1-5] \|',s.split('## Phase 4.6')[1].split('## Phase 5 ')[0],re.M))==5
assert len(re.findall(r'^\| (current|standard|abstract) \|',s,re.M))==15
for name in['Typeclass diamond','Reducibility leak','Non-canonical unfolding','Instance priority collision','Universe-polymorphism issues','Coercion ambiguity']:assert name in s
assert all(t in s for t in['NOT-COMPOSABLE','not a full kernel-body dump','pairwise duplication audit','80823','index:error','not user blockers','**BIG**','Polynomial.ncard_boxPoly'])
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS246: all phases; fresh17; exact293; formal15; four clean native sets; full caller inline; edge cases; currentmanifest/links/secrets.')
