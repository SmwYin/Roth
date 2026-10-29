#!/usr/bin/env python3
"""Portable, read-only canonical267 validator. Current manifest is authoritative."""
from pathlib import Path
import json,sys,re,hashlib
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.approxSet'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 q=rd(n)['result']['structuredContent'];return q.get('result',q)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==267
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']and a['verdict']=='BORDERLINE-needs-human'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']and a['future_upstream_questions']<=5
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']=='ℝ → ℝ → Set (ℤ × ℕ)'
nt=rd('native-type.json');assert all(nt[k]for k in['full_type','full_written_source_body','full_kernel_printer_body'])and not nt['printer_elision']
assert o['project_dependencies']==rd('dependencies.json')['canonical_body']==[]
assert rd('dependencies.json')['canonical_type']==rd('dependencies.json')['transitive_project_dependencies']==[]
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
assert {x['label']for x in v['accepted']}=={'original','project','isolated','inline','supplement'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']and q['request']==e['original_execution_request']
 assert isinstance(q['elapsed_ms'],int)and q['elapsed_ms']>=0 and not q['result'].get('isError',False)
 assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall('^import ',s,re.M))==9
  assert q['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
  assert z['partial']is False and not z.get('failed_dependencies');ds=z['items']
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix20.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==20 and not re.search('^import Roth',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info and'PANIC'not in info and'LEAN_MCP_MAX_OUTPUT_CHARS'not in info
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert ax
 for x in ax:assert{y.strip()for y in x.split(',')if y.strip()}<=allowed
 assert all(x in info for x in e['required_info'])
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
assert len(v['rejected'])==4
for e in v['rejected']:
 q=rd(e['receipt']);z=result(e['receipt']);s=(D/e['source']).read_text()
 assert any(x['severity']in['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 if'code'in q['request']:assert q['request']['code']==s
assert result('original-warming-receipt.json')['partial']is True
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
loc=(D/'local-excerpt.tex.txt').read_text();lines=(R/l['path']).read_text().splitlines()
assert '\n'.join(lines[1138:1197])in loc and'\n'.join(lines[1570:1610])in loc
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[266]==rd('canonical-entry.json')and order[266]['name']==N and order[266]['line']==55
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
assert actual==expected and len(actual)==len(set(actual))==293
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
ds=result('original-receipt.json')['items'];msgs=[x['message']for x in ds]
assert [x.split(': ',1)[1]for x in msgs if x.startswith('APPROX267_DIRECT_CONSUMER:')]==c['direct_value']and len(c['direct_value'])==12
assert [x.split(': ',1)[1]for x in msgs if x.startswith('APPROX267_DIRECT_TYPE_CONSUMER:')]==c['direct_type']and len(c['direct_type'])==10
assert all(x in msgs for x in ['APPROX267_AUDIT: requested=293; unique=293','APPROX267_AUDIT_PRESENT: present=293; values=293'])
orig=(R/'Roth/Main.lean').read_text();body=orig[orig.index('namespace Roth'):].replace('namespace Roth','namespace Approx267Original\nopen Roth',1).replace('end Roth','end Approx267Original');body=re.sub(r'\bapproxSet\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
meta=rd('target-metadata.json');assert meta['name']==N and meta['source']==rd('target-metadata.json')['source']
assert meta['source']in(R/'Roth/Main.lean').read_text()
callers=rd('callers.json');assert len(callers['source_explicit'])==10 and callers['source_explicit_count']==10
for x in callers['source_explicit']:
 source='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])+'\n'
 assert source==(D/x['archive']).read_text()and sha(D/x['archive'])==x['sha256']
 assert len(re.findall(r'\bapproxSet\b',source))==x['target_occurrences']
inline=(D/'inline-executed.lean.txt').read_text()
assert not re.search(r'\bapproxSet\b',inline)and inline.count('Subsingleton.elim _ _')==12
assert len(re.findall(r'^elab "originalPrivate267_',inline,re.M))==3
assert inline.count('#print axioms ')==12
assert 'Roth.Main'in inline and'Roth.LeanEval'in inline
# Independent token comparison of full original proof bodies, omitting comments and changing
# exactly the target spelling to its literal lambda, with namespace changes only.
def uncomment(x):return re.sub(r'/\-.*?\-/','',x,flags=re.S)
raw='''(fun (α κ : ℝ) ↦
      ({hq : ℤ × ℕ | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ} : Set (ℤ × ℕ)))'''
main=uncomment(orig[orig.index('namespace Roth'):].replace('namespace Roth','namespace Approx267Inline\nopen Roth',1).replace('end Roth','end Approx267Inline'))
main=re.sub(r'def approxSet \(α κ : ℝ\) : Set \(ℤ × ℕ\) :=\n  .*\n','',main);main=re.sub(r'\bapproxSet\b',raw,main)
lean=(R/'Roth/LeanEval.lean').read_text();lean=lean[lean.index('namespace LeanEval.NumberTheory.ThueSiegelRothProblem'):]
lean=uncomment(lean.replace('namespace LeanEval.NumberTheory.ThueSiegelRothProblem','namespace Approx267InlineLeanEval',1).replace('end LeanEval.NumberTheory.ThueSiegelRothProblem','end Approx267InlineLeanEval')).replace('Roth.approxSet ',raw+' ')
normalize=lambda x:re.sub(r'\s+','',x)
assert normalize(main)in normalize(inline)and normalize(lean)in normalize(inline)
p=(D/'project-executed.lean.txt').read_text()
for token in ['theorem recovery','theorem constants_differ','theorem quotient_image','theorem finite_fiber','theorem infinite_iff_rat','hκ : 0 ≤ κ','hκ : 0 < κ','hα : Irrational α','eventually_div_rpow_lt','approxSet_den_le_finite']:assert token in p
iso=(D/'isolated-executed.lean.txt').read_text()
for token in ['theorem bounded_den_finite','theorem infinite_iff_frequently','theorem liouvilleWith_iff','∃ C : ℝ, (approxC α κ C).Infinite','theorem dirichlet_endpoint','theorem zero_rat_endpoint']:assert token in iso
supp=(D/'supplement-executed.lean.txt').read_text();assert 'theorem rational_pair_infinite (x : ℚ) (κ : ℝ)'in supp and'theorem zero_exponent_fiber_infinite'in supp
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+meth+'.json');assert q['request']and q['result']
  if meth=='rg':assert q['result']['exit_code']in[0,1]
  else:assert not q['result'].get('isError',False)
web=[rd('web-'+x+'.json')for x in ['general','channels','recent-api','primary']]
for q in web:
 assert q['request']and q['summary']and q['locators']and q['response']['bytes']>0 and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])
 assert'result'not in q and'body'not in q['response']
 for x in q['locators']:assert x['title']and x['url'].startswith('https://')and'?'not in x['url']and'…'not in x['url']
assert len({x['q']for x in web[0]['request']['search_query']})==3
assert any('site:ncatlab.org/ncatlab 'in x['q']for q in web for x in q['request'].get('search_query',[]))
assert any(all(t in x['q']for t in ['after:2021-10-29','before:2026-10-30'])for q in web for x in q['request'].get('search_query',[]))
assert any('mathlib4 DiophantineApproximation'in x['q']for q in web for x in q['request'].get('search_query',[]))
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']
shared=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')
if shared.is_file():assert sha(shared)==v['controls']['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
assert (D/'isolated-prefix20.lean.txt').read_text()==(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.NumberTheory.DiophantineApproximation.Basic\n'+'import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
auth=rd('root-prefix-scope-authorization.json');assert auth['authorized_by']=='root'and auth['prefix_sha256']==sha(D/'isolated-prefix20.lean.txt')==v['controls']['isolated20_sha256']
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
for s in ['Phase4.5','Phase4.6','Phase5.5','Phase6.0','NOT-COMPOSABLE','BORDERLINE-needs-human','LiouvilleWith κ α ↔ ∃ C : ℝ','full kernel body without elision','future upstream questions']:
 # prose formatting permits space between Phase and its number
 assert s in report or s.replace('Phase','Phase ')in report,s
assert rd('secret-guard.json')['exit_code']==0
assert rd('preparation-checks.json')['original_preexecution']['source_sha256']==sha(D/'original-executed.lean.txt')
assert all(not x['native_queried_after_failure']for x in rd('preparation-checks.json')['width_preparation_failures'])
assert v['no_file_end_build_due']and v['next_file_end_canonical_index']==289
print('PASS canonical267: currentmanifest; fresh17; exact293; five clean native sources; all12caller signatures; semantic C/ψ and exact rational/filter bridges/guards;20 authorized imports;15formal/all named literature+definitionAPIweb; portable links')
