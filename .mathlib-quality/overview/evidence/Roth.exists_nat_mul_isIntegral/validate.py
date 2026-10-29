#!/usr/bin/env python3
"""Read-only canonical268 validator; current manifest authoritative in both layouts."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_nat_mul_isIntegral'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def res(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==268
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']and a['verdict']=='NO-mathlib-has-it'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']=='∀ {α : ℝ}, IsAlgebraic ℚ α → ∃ (M : ℕ), 0 < M ∧ IsIntegral ℤ (↑M * α)'
nt=rd('native-type.json');assert nt['full_type']and nt['full_written_source_body']and nt['printer_elision']and not nt['full_kernel_printer_body']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 n='report.md'if'/mathlibable/'in x['destination']else Path(x['destination']).name
 p=report_path()if n=='report.md'else D/n
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 assert x['destination']=='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if n=='report.md'else'evidence/'+N+'/'+n)
 assert n not in seen,n
 seen.add(n)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {e['label']for e in v['accepted']}=={'original','isolated-firstclean','isolated','inline','supplement','scope'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=res(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']and q['request']==e['original_execution_request']
 assert isinstance(q['elapsed_ms'],int)and q['elapsed_ms']>=0 and not q['result'].get('isError',False)
 assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall('^import ',s,re.M))==9
  assert q['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
  assert z['partial']is False and not z.get('failed_dependencies');ds=z['items']
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix19.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==19 and not re.search('^import Roth',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info and'PANIC'not in info
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert ax
 for x in ax:assert{y.strip()for y in x.split(',')if y.strip()}<=allowed
 assert all(x in info for x in e['required_info']),e['label']
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['rejected']:
 q=rd(e['receipt']);z=res(e['receipt']);s=(D/e['source']).read_text()
 assert any(x['severity']in['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 if'code'in q['request']:assert q['request']['code']==s
assert len(v['rejected'])==3 and rd('receipt-capture-failure.json')['accepted']is False
acc=v['attempt_accounting'];assert acc['native_executions']==10 and acc['distinct_sources']==9 and acc['archived_actual_raw_responses']==9 and acc['missing_original_failed_response']==1
assert 'replay' in rd('isolated-rejected2-receipt.json')['provenance']
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
assert sha(R/'Roth/Main.lean')==sha(D/'source-Main.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
assert (D/'local-excerpt.tex.txt').read_text()=='\n'.join((R/l['path']).read_text().splitlines()[1147:1189])+'\n'
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[267]==rd('canonical-entry.json')and order[267]['name']==N and order[267]['line']==62
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
assert actual==expected and len(actual)==len(set(actual))==293
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
assert c['direct_value']==['Roth.reduction']and c['direct_type']==[]
msgs=[x['message']for x in res('original-receipt.json')['items']]
assert [x.split(': ',1)[1]for x in msgs if x.startswith('NAT268_DIRECT_CONSUMER:')]==c['direct_value']
assert not[x for x in msgs if x.startswith('NAT268_DIRECT_TYPE_CONSUMER:')]
assert all(x in msgs for x in ['NAT268_AUDIT: requested=293; unique=293','NAT268_AUDIT_PRESENT: present=293; values=293'])
orig=(R/'Roth/Main.lean').read_text();body=orig[orig.index('namespace Roth'):].replace('namespace Roth','namespace NatIntegral268Original\nopen Roth',1).replace('end Roth','end NatIntegral268Original');body=re.sub(r'\bexists_nat_mul_isIntegral\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
assert rd('target-metadata.json')['source']in orig
callers=rd('callers.json');assert callers['source_explicit_count']==len(callers['source_explicit'])==1
for x in callers['source_explicit']:
 raw='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])+'\n'
 assert raw==(D/x['archive']).read_text()and sha(D/x['archive'])==x['sha256']
 assert len(re.findall(r'\bexists_nat_mul_isIntegral\b',raw))==1
# Check whole original caller suffix token-for-token: only obtaining M changed.
suffix=raw[raw.index('  obtain ⟨Q₀, hQ₀⟩'):];compact=lambda x:re.sub(r'\s+','',x)
for fname in ['inline-executed.lean.txt','scope-executed.lean.txt']:
 src=(D/fname).read_text();assert compact(src).count(compact(suffix))==2
 assert 'example : @Roth.reduction = @manual_reduction := Subsingleton.elim _ _'in src
 assert 'example : @Roth.reduction = @closure_reduction := Subsingleton.elim _ _'in src
 assert 'exists_nat_mul_isIntegral halg'not in src
scope='\n'.join(x['message']for x in res('scope-receipt.json')['items'])
for t in ['NAT268_INLINE_NO_TARGET: NatIntegral268Inline.manual_reduction','NAT268_INLINE_NO_TARGET: NatIntegral268Inline.closure_reduction','NAT268_DIRECT_PROJECT_TYPE: []','Roth.exists_nat_mul_isIntegral._simp_1_1','Roth.exists_nat_mul_isIntegral._simp_1_2']:assert t in scope
assert o['project_dependencies']==rd('dependencies.json')['canonical_body']==rd('dependencies.json')['canonical_type']==rd('dependencies.json')['transitive_project_dependencies']==[]
iso=(D/'isolated-executed.lean.txt').read_text()
for t in ['theorem generic_ring','theorem fraction_ring','theorem nat_noncomm','theorem nat_rat_algebra','theorem old_direct','theorem closure_route','theorem converse','theorem nat_iff','theorem original_noncomm_specialization','nat_noncomm ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα)','theorem zero_endpoint','theorem rational_endpoint','theorem zero_multiplier_vacuous','[Ring A]','s.property']:assert t in iso
assert 'theorem no_unconditional_nat'in(D/'supplement-executed.lean.txt').read_text()
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+method+'.json');assert q['request']and q['result']
  if method=='rg':assert q['result']['exit_code']in[0,1]
  else:assert not q['result'].get('isError',False)
assert rd('full-name-search.json')['exit_code']==1 and rd('full-name-search.json')['stdout']==''
web=[rd('web-'+x+'.json')for x in ['general','channels','recent','primary','supplement']]
for q in web:
 assert q['request']and q['summary']and q['locators']and q['response']['bytes']>0 and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])
 assert'result'not in q and'body'not in q['response']
 for x in q['locators']:assert x['title']and x['url'].startswith('https://')and'?'not in x['url']and'…'not in x['url']
assert len({x['q']for x in web[0]['request']['search_query']})==3
assert any('site:ncatlab.org/ncatlab 'in x['q']for q in web for x in q['request'].get('search_query',[]))
assert any(all(t in x['q']for t in ['after:2021-10-29','before:2026-10-30'])for q in web for x in q['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(t in x['q']for q in web for x in q['request'].get('search_query',[]))
assert rd('optional-math-opinion.json')['status']=='n/a'
controls=v['controls'];assert sha(D/'isolated-prefix.lean.txt')==controls['shared_prefix_sha256']
shared=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')
if shared.is_file():assert sha(shared)==controls['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==controls['disk_prefix_sha256']
assert (D/'isolated-prefix19.lean.txt').read_text()==(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.RingTheory.Algebraic.Denominator\n'
assert sha(D/'isolated-prefix19.lean.txt')==controls['isolated19_sha256']==rd('root-prefix-scope-authorization.json')['prefix_sha256']
assert rd('root-prefix-scope-authorization.json')['authorized_by']=='root'
assert rd('composition.json')['canonical_denominator_route']['total_explicit_theorem_applications']==5
assert not rd('composition.json')['canonical_denominator_route']['new_helper_used']
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
for t in ['NO-mathlib-has-it','NOT-COMPOSABLE','Phase4.5','Phase4.6','Phase5.5','Phase6.0','five explicit theorem applications','not a complete kernel body dump','not a recovered original response','future upstream questions']:
 assert t in report,t
assert rd('preparation-checks.json')['original_preexecution']['source_sha256']==sha(D/'original-executed.lean.txt')
assert rd('preparation-checks.json')['native_queried_after_preparation_failure']is False
assert v['no_file_end_build_due']and v['next_file_end_canonical_index']==289
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical268: currentmanifest; fresh17; exact293 ordered/private/value audit; 6clean sources; fullcaller 2routes/noncircular; generic RingA+exact specialization; canonical denominator5calls; 15formal/all named literature; stable18/disk9+authorized19; portable links; no accepted proof gaps')
