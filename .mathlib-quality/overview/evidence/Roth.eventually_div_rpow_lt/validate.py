#!/usr/bin/env python3
"""Portable read-only canonical270 assessment validator; validate CURRENT manifest."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.eventually_div_rpow_lt'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def reportpath():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==270
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']and a['verdict']=='YES-but-generalise-first'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and o['type'].startswith('∀ {M κ κ\' : ℝ}')
assert o['generalization']['verified']and o['generalization']['proposed_type'].startswith('∀ {α : Type*}')
assert rd('native-type.json')['printer_elision']and not rd('native-type.json')['full_kernel_printer_body']
assert rd('native-type.json')['full_written_source_body']and rd('native-type.json')['full_type']
# Manifest destinations preserve supporting subdirectory paths. Root records are integration-only.
m=rd('copy-manifest.json');assert m['declaration']==N;covered=set()
for x in m['files']:
 prefix='.mathlib-quality/overview/evidence/'+N+'/'
 if x['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=reportpath();rel='report.md'
 else:
  assert x['destination'].startswith(prefix);rel=x['destination'][len(prefix):];p=D/rel
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 assert rel not in covered;covered.add(rel)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in excluded}
assert files<=covered,files-covered
assert not list(D.rglob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert{e['label']for e in v['accepted']}=={'original','isolated','inline','scope','supplement'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt']);ds=z.get('items',z.get('diagnostics'))
 assert sha(D/e['source'])==e['source_sha256']and q['request']==e['original_execution_request']
 assert q['executor']['owner']=='root'and q['executor']['worker_request']['source_sha256']==e['source_sha256']
 assert isinstance(q['elapsed_ms'],int)and q['elapsed_ms']>=0 and not q['result'].get('isError',False)
 assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall('^import ',s,re.M))==9
  assert z['partial']is False and not z['failed_dependencies']
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  imports=re.findall('^import (.+)$',s,re.M);assert len(imports)==20 and not any(x.startswith('Roth')for x in imports)
  assert imports[-2:]==v['controls']['isolated_extra_modules']and'#check_failure '+N in s
  prefix='\n'.join(s.splitlines()[:20])+'\n'
  assert hashlib.sha256(prefix.encode()).hexdigest()in rd('import-authorization.json')['prefix_sha256']
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info and 'PANIC'not in info
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert ax
 for x in ax:assert{y.strip()for y in x.split(',')if y.strip()}<=allowed
 assert all(x in info for x in e['required_info']),e['label']
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['rejected']:
 q=rd(e['receipt']);s=(D/e['source']).read_text();z=result(e['receipt']);ds=z.get('items',z.get('diagnostics'))
 assert sha(D/e['source'])==e['source_sha256']and any(x['severity']in['error','warning']for x in ds)
 if'code'in q['request']:assert q['request']['code']==s
 assert q['executor']['worker_request']['source_sha256']==e['source_sha256']
assert len(v['rejected'])==7 and v['attempt_accounting']['native_executions']==12
assert len(list(D.glob('*-receipt.json')))==12
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json');assert len(b)==len(fresh)==17
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):assert sha(R/'.lake/packages/mathlib'/x['path'])==x['sha256']==sha(D/x['archive'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
assert(D/'local-excerpt.tex.txt').read_text()=='\n'.join((R/l['path']).read_text().splitlines()[1166:1194])+'\n'
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[269]==rd('canonical-entry.json')and order[269]['name']==N and order[269]['line']==103
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for fname in ['original-executed.lean.txt','scope3-executed.lean.txt']:
 s=(D/fname).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
 terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
 assert actual==expected and len(actual)==len(set(actual))==293
s=(D/'original-executed.lean.txt').read_text();meta=rd('target-metadata.json');assert meta['source']in(R/'Roth/Main.lean').read_text()
replay='namespace Decay270Original\nopen Roth\n'+meta['source'].replace('theorem eventually_div_rpow_lt','theorem replay',1)+'\nend Decay270Original\n'
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+replay)
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
consumers=['Roth.reduction','Roth.exists_reduced_approx','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff']
assert c['direct_value']==consumers and c['direct_type']==[]and not c['simp_member']
assert len(c['transitive_project_type_and_value_consumers'])==9
callers=rd('callers.json');assert callers['source_explicit_count']==callers['source_call_count']==3
inline=(D/'inline2-executed.lean.txt').read_text();proof=meta['source'].split(' := by\n',1)[1]
binder="  have bound {M κ κ' : ℝ} (hκ : κ' < κ) :\n      ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by\n"
literal=binder+'\n'.join('  '+line for line in proof.splitlines())+'\n';generic=binder+'    exact recovery hκ\n'
assert inline.count(literal)==inline.count(generic)==3
for x in callers['source_explicit']:
 raw='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])+'\n'
 assert raw==(D/x['archive']).read_text()and sha(D/x['archive'])==x['sha256']and raw.count('eventually_div_rpow_lt')==1
 for bnd in [literal,generic]:
  z=raw.strip().replace('IsDiophantine x','LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x')if x['name'].startswith('LeanEval.')else raw.strip()
  z=z.replace('IsDiophantine x ↔ ∀ {κ : ℝ},','IsDiophantine x ↔\n      ∀ {κ : ℝ},').replace(' := by\n',' := by\n'+bnd,1).replace('Roth.eventually_div_rpow_lt','bound').replace('eventually_div_rpow_lt','bound')
  assert z in inline
 assert 'example : @'+x['name']+' =\n    @'+x['name'].split('.')[-1]+' := Subsingleton.elim _ _'in inline
assert rd('dependencies.json')['canonical_body']==o['project_dependencies']==[]
iso=(D/'isolated3-executed.lean.txt').read_text()
for t in ['theorem eventual_filter','theorem eventual_real','theorem threshold','theorem recovery','theorem nonpositive','theorem equal_guard','liouvilleWith_one 0']:assert t in iso
supp=(D/'supplement3-executed.lean.txt').read_text();assert supp.index('fail_if_success solve | exact?')<supp.index('theorem eventual_filter')and'fail_if_success solve | apply?'not in supp
assert '(∀ M : ℝ, ∃ Q : ℕ' in supp and '↔ κ\' < κ' in supp
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+method+'.json');assert q['request']and q['result']
  if method=='rg':assert q['result']['exit_code']in[0,1]
  else:assert not q['result'].get('isError',False)
 assert rd('search-'+f+'-local_search.json')['result']['structuredContent']['index']=='error'
assert rd('full-name-search.json')['exit_code']==1 and not rd('full-name-search.json')['stdout']
web=[rd('web-'+x+'.json')for x in ['batch0','batch3','batch6','primary']]
for q in web:
 assert q['request']and q['summary']and q['locators']and q['response']['bytes']>0 and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])
 assert'result'not in q and'body'not in q['response']
 for x in q['locators']:assert x['title']and x['url'].startswith('https://')and'?'not in x['url']and'…'not in x['url']
assert len({x['q']for x in web[0]['request']['search_query']})==3
for t in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(t in x['q']for q in web for x in q['request'].get('search_query',[]))
assert any(all(t in x['q']for t in ['after:2021-10-29','before:2026-10-30'])for q in web for x in q['request'].get('search_query',[]))
assert rd('optional-math-opinion.json')['status']=='n/a'
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']and sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
shared=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')
if shared.is_file():assert sha(shared)==v['controls']['shared_prefix_sha256']
report=reportpath().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file()
 elif not href.startswith('https://'):raise AssertionError(href)
for t in ['YES-but-generalise-first','NOT-COMPOSABLE','Phase4.5','Phase4.6','Phase5.5','Phase6.0','not a complete kernel body dump','teorth','standalone','Main:164','LeanEval:42']:assert t.lower()in report.lower(),t
assert len(re.findall(r'^\|[1-9]\|',report,re.M))==14
assert v['no_file_end_build_due']and v['next_file_end_canonical_index']==289
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical270: current recursive manifest; fresh17; exact293;5clean/7rejected;6fullcallers;standard axioms;15formal;all named literature channels;authorized20/stable18/disk9;portable links;YES restatement/reviewer/grouping')
