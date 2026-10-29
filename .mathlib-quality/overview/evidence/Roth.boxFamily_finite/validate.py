#!/usr/bin/env python3
"""Portable read-only canonical245 validator. Validate current copy-manifest in either layout."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.boxFamily_finite'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
def report():
 p=D/'report.md';return p if p.is_file()else D.parent.parent/'mathlibable'/(N+'.md')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==245 and a['completed']
assert a['allphases']=='PASS'and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='BORDERLINE-needs-human'and a['root_acceptance']in['pending','PASS']
assert not a['unresolved']and not v['unresolved']and len(a['questions'])==3
required={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert required<=set(o)and o['type']==rd('native-type.json')['type']
assert 'Finite ↑(Function.support r)'in o['type']and'(Roth.boxFamily r B).Finite'in o['type']
assert o['project_dependencies']==['Roth.boxFamily','Roth.boxFamily_eq_image_finsupp_aux']
nt=rd('native-type.json');assert nt['printer_elision']and nt['elided_characters']==9641
assert nt['compact_body_complete']and not nt['full_kernel_body_available']
assert nt['kernel_type_project_constants']==['Roth.boxFamily']
assert nt['kernel_body_project_constants']==['Roth.boxFamily','_private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:p=report();seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {e['label']for e in v['accepted']}=={'original','availability','isolated','project','composition','dependencies'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(r);assert not r['result'].get('isError',False)
 assert z['success']and not z.get('timed_out');src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256']and r['request']==e['original_execution_request']
 assert isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s
  ds=z['diagnostics'];assert s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==18
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')and not z.get('failed_dependencies')
  ds=z['items'];assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==9
 assert not[x for x in ds if x.get('severity')in['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
 if e['label']=='original':assert '9641 characters elided'in info
 else:assert not any('characters elided'in x['message']for x in ds)
assert len(v['rejected'])==6 and len(v['warming'])==1
assert result(rd('original-warming-receipt.json'))['partial']is True
for e in v['rejected']:
 r=rd(e['receipt']);z=result(r);ds=z.get('items',z.get('diagnostics',[]))
 assert any(x['severity']in['error','warning']for x in ds)
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
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
assert '\\label{roth:eq43}'in(D/'local-excerpt.tex.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[244]==rd('canonical-entry.json')
assert order[244]['name']==N and order[244]['line']==301
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('BOX245_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),('BOX245_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['Roth.exists_ne_modByMonic_eq']and not v['canonical_direct_type_consumers']
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Box245Original\nopen Roth',1).replace('end Roth','end Box245Original');body=re.sub(r'\bboxFamily_finite\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['request']['query']
  assert not f['result'].get('isError',False)and'items'in f['result']['structuredContent']
  if method=='local_search':assert f['result']['structuredContent']['index']=='error'
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1]and not f['stderr']
assert rd('full-name-search.json')['exit_code']==0
rg=rd('source-search.json');gg=rd('tracked-source-search.json')
assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['executable_occurrences']==cs['distinct_declarations']==1 and cs['external_to_file']==0
for c in cs['callers']:
 assert c['source'].strip()=='\n'.join((R/c['file']).read_text().splitlines()[c['line']-1:c['end_line']]).strip()
 assert hashlib.sha256(c['source'].encode()).hexdigest()==c['sha256']
 assert len(re.findall(r'\bboxFamily_finite\b',c['body']))==1
pj=(D/'project-executed.lean.txt').read_text();c=cs['callers'][0]
old='(boxFamily_finite r B).fintype';new='''(show (boxFamily r B).Finite from by
    rw [box245Representation]
    exact (Finset.finite_toSet _).image _).fintype'''
assert c['source'].replace(old,new)in pj
assert '@Roth.exists_ne_modByMonic_eq = @Box245Project.exists_ne_modByMonic_eq := rfl'in pj
assert '@Roth.boxFamily_finite = @finite_original := rfl'in pj
iso=(D/'isolated-executed.lean.txt').read_text()
assert '[CommSemiring R]'in iso and '(ht : ∀ d ∈ s, (t d).Finite)'in iso
assert 'Set.Finite.pi\''in iso and 'Set.Finite.of_injOn'in iso and 'Finsupp.notMem_support_iff'in iso
for t in['zero_coefficient_bound','zero_degree','empty_variables','infinite_variables_finite_support','support_needed','weaker_disjunction']:
 assert "'Box245Project."+t+"' depends on axioms:"in str(result(rd('project-receipt.json')))
comp=(D/'composition-executed.lean.txt').read_text()
assert 'fail_if_success exact (Finset.finite_toSet _).image _'in comp
assert 'fail_if_success solve | simp only [Roth.boxFamily]'in comp
assert '(s.finsupp t).finite_toSet.image _'in comp
inv=rd('source-inventory.json');assert inv['exit_code']==0
assert {x['file']for x in order}<=(set(inv['stdout'].splitlines())|{'Roth.lean'})
queries=[]
for name in['web-general','web-channels','web-recent','web-primary']:
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
assert c['abstract_existing_image_law_verified']and c['generic_semiring_finite_coefficients_verified']
assert c['original_recovery_verified']and c['actual_caller_replays']==1 and c['full_body_inline_success']
assert c['inline_private_bridge_retained']and c['direct_target_independence_only']
assert not v['generality']['support_iff_claimed']and v['generality']['weaker_disjunction_compiled']
s=report().read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
assert len(re.findall(r'^\| [1-9] \|',s.split('## Phase 4c')[1].split('## Phase 4.5')[0],re.M))==9
assert len(re.findall(r'^\| [1-5] \|',s.split('## Phase 4.6')[1].split('## Phase 5 ')[0],re.M))==5
assert len(re.findall(r'^\| (current|standard|abstract) \|',s,re.M))==15
assert all(t in s for t in['NOT-COMPOSABLE','not a full kernel-body dump','pairwise duplication audit','9641','index:error','not user blockers'])
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS245: all phases; fresh17; exact293; formal15; six clean native sets; actual caller inline; edge cases; currentmanifest/links/secrets.')
