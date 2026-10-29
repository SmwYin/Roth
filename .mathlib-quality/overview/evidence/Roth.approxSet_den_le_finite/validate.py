#!/usr/bin/env python3
"""Read-only canonical269 validator; current manifest is authoritative in both layouts."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.approxSet_den_le_finite'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def res(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==269
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']and a['verdict']=='BORDERLINE-needs-human'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']and a['future_upstream_questions']==3
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']=='∀ (α κ : ℝ) (Q₀ : ℕ), {hq : ℤ × ℕ | hq ∈ Roth.approxSet α κ ∧ hq.2 ≤ Q₀}.Finite'
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
assert {e['label']for e in v['accepted']}=={'original','isolated','inline','supplement','supplement2','scope'}
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
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==18 and not re.search('^import Roth',s,re.M)
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
 assert not z['success']and any(x['severity']in['error','warning']for x in z['diagnostics'])
 assert q['request']['code']==s
assert len(v['rejected'])==3 and v['attempt_accounting']==dict(native_executions=9,accepted_sources=6,rejected_sources=3,all_raw_responses_archived=True)
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
ls=(R/l['path']).read_text().splitlines();assert(D/'local-excerpt.tex.txt').read_text()=='\n'.join(ls[1174:1187]+['']+ls[1576:1587])+'\n'
assert 'fixed upper bound' in (D/'local-excerpt.tex.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[268]==rd('canonical-entry.json')and order[268]['name']==N and order[268]['line']==73
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
assert actual==expected and len(actual)==len(set(actual))==293
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
consumers=['Roth.reduction','Roth.exists_reduced_approx','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff']
assert c['direct_value']==consumers and c['direct_type']==[]
msgs=[x['message']for x in res('original-receipt.json')['items']]
assert [x.split(': ',1)[1]for x in msgs if x.startswith('BOUND269_DIRECT_CONSUMER:')]==c['direct_value']
assert not[x for x in msgs if x.startswith('BOUND269_DIRECT_TYPE_CONSUMER:')]
assert all(x in msgs for x in ['BOUND269_AUDIT: requested=293; unique=293','BOUND269_AUDIT_PRESENT: present=293; values=293'])
orig=(R/'Roth/Main.lean').read_text();meta=rd('target-metadata.json');assert meta['source']in orig
replay='namespace Bounded269Original\nopen Roth\n'+meta['source'].replace('theorem approxSet_den_le_finite','theorem replay',1)+'\nend Bounded269Original\n'
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+replay)
assert 'example : @Roth.approxSet_den_le_finite = @Bounded269Original.replay := Subsingleton.elim _ _'in s
assert 'Exact target only' in v['original_replay_scope']
callers=rd('callers.json');assert callers['source_explicit_count']==len(callers['source_explicit'])==3 and callers['source_call_count']==4
inline=(D/'inline-executed.lean.txt').read_text();proof=meta['source'].split(' := by\n',1)[1]
literalbinder='  have bound (α κ : ℝ) (Q₀ : ℕ) : {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite := by\n'+'\n'.join('  '+line for line in proof.splitlines())+'\n'
genericbinder='  have bound (α κ : ℝ) (Q₀ : ℕ) : {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite := by\n    exact bounded_den_finite α (fun q ↦ 1 / (q : ℝ) ^ κ) Q₀\n'
assert inline.count(literalbinder)==3 and inline.count(genericbinder)==3
for x in callers['source_explicit']:
 raw='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])+'\n'
 assert raw==(D/x['archive']).read_text()and sha(D/x['archive'])==x['sha256']
 assert raw.count('approxSet_den_le_finite')==x['target_occurrences']
 for binder in [literalbinder,genericbinder]:
  modified=raw.strip().replace('IsDiophantine x','LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x')if x['name'].startswith('LeanEval.')else raw.strip()
  modified=modified.replace('IsDiophantine x ↔ ∀ {κ : ℝ},','IsDiophantine x ↔\n      ∀ {κ : ℝ},')
  modified=modified.replace(' := by\n',' := by\n'+binder,1).replace('Roth.approxSet_den_le_finite','bound').replace('approxSet_den_le_finite','bound')
  assert modified in inline,x['name']
 assert 'example : @'+x['name']+' =\n    @'+x['name'].split('.')[-1]+' := Subsingleton.elim _ _'in inline
assert (D/'scope-executed.lean.txt').read_text().startswith(inline)
scope='\n'.join(x['message']for x in res('scope-receipt.json')['items'])
for route in ['Literal','Generic']:
 for n in ['reduction','exists_reduced_approx','isDiophantine_iff']:
  assert 'BOUND269_INLINE_CLOSURE_NO_TARGET: Bounded269'+route+'.'+n in scope
assert 'BOUND269_DIRECT_PROJECT_TYPE: [Roth.approxSet]'in scope
assert 'BOUND269_PROJECT_VALUE_CLOSURE: [Roth.approxSet_den_le_finite._simp_1_2,\n Roth.approxSet_den_le_finite._simp_1_1,\n Roth.approxSet,\n Roth.approxSet_den_le_finite]'in scope
assert o['project_dependencies']==rd('dependencies.json')['canonical_body']==rd('dependencies.json')['transitive_project_dependencies']==['Roth.approxSet']
iso=(D/'isolated-executed.lean.txt').read_text()
for t in ['theorem bounded_den_finite','theorem finite_radius','theorem old_form','theorem zero_bound','theorem negative_exponent','theorem rational_center','theorem closed_endpoint','theorem negative_radius_empty','theorem zero_pairs_infinite']:assert t in iso
supp=(D/'supplement2-executed.lean.txt').read_text()
for t in ['[Ring K] [LinearOrder K]','[IsStrictOrderedRing K] [FloorRing K]','fail_if_success solve | exact?','theorem zero_denominator_unrestricted']:assert t in supp
credit=rd('prior-proof-credit.json');assert not credit['existing_mathlib']and not credit['inherited_verdict']and sha(R/credit['source'])==credit['sha256']
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+method+'.json');assert q['request']and q['result']
  if method=='rg':assert q['result']['exit_code']in[0,1]
  else:assert not q['result'].get('isError',False)
 assert rd('search-'+f+'-rg-rejected-path.json')['result']['exit_code']==2
assert rd('full-name-search.json')['exit_code']==1 and rd('full-name-search.json')['stdout']==''
web=[rd('web-'+x+'.json')for x in ['general','channels','recent','primary']]
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
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
for t in ['BORDERLINE-needs-human','NOT-COMPOSABLE','Phase4.5','Phase4.6','Phase5.5','Phase6.0','not a complete kernel body dump','future upstream questions','no user decision']:
 assert t.lower()in report.lower(),t
assert len(re.findall(r'^\|[1-9]\|',report,re.M))==14
assert len(re.findall(r'^\d\. ',report,re.M))==3
assert rd('preparation-checks.json')['original_preexecution']['source_sha256']==sha(D/'original-executed.lean.txt')
assert rd('preparation-checks.json')['native_queried_after_preparation_failure']is False
assert v['no_file_end_build_due']and v['next_file_end_canonical_index']==289
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical269: current manifest; fresh17; exact293 ordered/private/value audit; six clean sources; six fullcaller/type/noncircular checks; arbitrarypsi credit+Ring/FloorRing/guards;15formal;all named channels;stable18/disk9;portable links;standard axioms')
