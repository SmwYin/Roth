#!/usr/bin/env python3
"""Read-only canonical271 validator. Always validate CURRENT recursive manifest."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.reduction';draft='--draft' in sys.argv
# Draft mode is only for pre-completion gate preparation; final checks never pass --draft.
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 q=rd(n)['result']['structuredContent'];return q.get('result',q)
def rpt():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==271
assert a['root_acceptance'] in ['pending','PASS'] and a['verdict']=='BORDERLINE-needs-human'
assert not a['parent_verdict_inherited'] and not a['cost_based_verdict']
assert not a['unresolved'] and not v['unresolved']
if not draft:assert a['completed'] and v['completed'] and a['allphases']=='PASS'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS' or (draft and k=='8' and x=='pending') for k,x in a['phases'].items())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'} <= set(o)
assert o['type']==rd('native-type.json')['type'] and o['type'].startswith('∀ {α : ℝ}')
assert o['generalization']['verified'] and '{t κ : ℝ}' in o['generalization']['proposed_type']
assert rd('native-type.json')['elided_characters']==[137118,515]
assert not rd('native-type.json')['full_kernel_printer_body']
# Resolve destinations rather than historical absolute scratch sources.
m=rd('copy-manifest.json');assert m['declaration']==N;covered=set()
for x in m['files']:
 prefix='.mathlib-quality/overview/evidence/'+N+'/'
 if x['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=rpt();rel='report.md'
 else:
  assert x['destination'].startswith(prefix);rel=x['destination'][len(prefix):];p=D/rel
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 assert rel not in covered;covered.add(rel)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file() and p.name not in excluded}
assert files<=covered,files-covered
assert not list(D.rglob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label'] for x in v['accepted']}=={'original','isolated','callers','composition-guards','dependencies','consumers'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt'])
 ds=z.get('items',z.get('diagnostics',[]))
 assert sha(D/e['source'])==e['source_sha256'] and q['request']==e['original_execution_request']
 assert q['executor']['owner']=='root'
 assert q['executor']['worker_request']['source_sha256']==e['source_sha256']
 assert isinstance(q['elapsed_ms'],int) and not q['result'].get('isError',False)
 assert z['success'] and not z.get('timed_out',False)
 if e['format']=='disk':
  assert z['partial'] is False and not z['failed_dependencies']
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==9
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  imports=re.findall('^import (.+)$',s,re.M)
  assert len(imports)==20 and not any(x.startswith('Roth') for x in imports)
  assert imports[-2:]==v['controls']['isolated_extra_modules'] and '#check_failure '+N in s
  pfx='\n'.join(s.splitlines()[:20])+'\n'
  assert hashlib.sha256(pfx.encode()).hexdigest() in rd('import-authorization.json')['prefix_sha256']
 assert not [x for x in ds if x['severity'] in ['error','warning'] or x.get('category')=='sorry']
 info='\n'.join(x['message'] for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx' not in info and 'PANIC' not in info
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['axiom_print_required']:assert ax
 for x in ax:assert {y.strip() for y in x.split(',') if y.strip()} <= allowed
 assert all(x in info for x in e['required_info']),e['label']
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']
 assert q['executor']['worker_request']['source_sha256']==e['source_sha256']
 if 'code' in q['request']:assert q['request']['code']==(D/e['source']).read_text()
assert result('caller-receipt.json')['partial'] and result('caller-receipt.json')['timed_out']
assert result('caller2-receipt.json')['success'] and result('caller2-receipt.json')['partial'] is False
assert any(x['severity']=='warning' for x in result('scope-receipt.json')['diagnostics'])
assert len(list(D.glob('*-receipt.json')))==v['attempt_accounting']['native_executions']==9
# Production source and pin freshness, complete source reads, pinned candidate snapshots.
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:
 assert x['match'] and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 assert sha(R/x['path'])==x['sha256']==sha(D/x['artifact'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
assert (D/'local-excerpt.tex.txt').read_text()=='\n'.join((R/l['path']).read_text().splitlines()[1149:1198])+'\n'
# Ordered293 source arrays: count and private-name modules are not interchangeable.
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert order[270]==rd('canonical-entry.json') and order[270]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
for fname in ['original-executed.lean.txt','consumer-scope-executed.lean.txt']:
 s=(D/fname).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S)
 assert len(arrays)==1
 terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0])
 actual=[('private',mod,nm) if mod else ('public',pub) for mod,nm,pub in terms]
 assert actual==expected and len(actual)==len(set(actual))==293
meta=rd('target-metadata.json');assert meta['source'] in (R/'Roth/Main.lean').read_text()
replay='namespace Reduction271Original\nopen Roth\n'+meta['source'].replace('theorem reduction','theorem replay',1)+'\nend Reduction271Original\n'
assert (D/'original-executed.lean.txt').read_text().startswith((D/'disk-prefix.lean.txt').read_text()+replay)
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
assert c['direct_value']==['Roth.roth'] and c['direct_type']==[] and not c['simp_member']
assert c['transitive_project_type_and_value_consumers']==['Roth.roth','Roth.roth_rat','LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth']
assert rd('dependencies.json')['canonical_body']==o['project_dependencies']
caller=(D/'caller-Roth.roth.lean.txt').read_text();native=(D/'caller3-executed.lean.txt').read_text()
assert caller.strip() in (R/'Roth/Main.lean').read_text() and native.count(caller.strip())==2
assert native.count(meta['source'])==1
for token in ['example : @Roth.roth = @Reduction271Inline.roth','example : @Roth.roth = @Reduction271Replacement.roth','example : @Roth.reduction = @Reduction271Replacement.reduction']:
 assert token in native
iso=(D/'isolated-executed.lean.txt').read_text()
for token in ['theorem scaling','theorem threshold','theorem recovery','theorem liouville_threshold',"∧ t < κ' ∧ κ' < κ ∧",'hinf.sdiff','prodMap']:
 assert token in iso
scope=(D/'scope2-executed.lean.txt').read_text()
assert scope.index('fail_if_success solve | exact?')<scope.index('have exists_nat_mul_isIntegral')
assert 'fail_if_success solve | apply?' not in scope
assert 'liouvilleWith_one 0' in scope and 'approxSet (3 / 4) 0' in scope
assert len(rd('formal-search-matrix.json'))==15
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd(f'search-{form}-{method}.json')
  if method=='rg':assert q['command'] and q['exit_code'] in [0,1]
  else:
   assert q['request'] and q['result']
   if method=='local_search':assert q['result']['structuredContent']['index']=='error'
   else:assert not q['result'].get('isError',False)
web=[rd(f'web-batch{i}.json') for i in range(4)]
for q in web:
 assert q['request'] and q['summary'] and q['locators'] and q['response_bytes']>0
 assert re.fullmatch('[0-9a-f]{64}',q['response_sha256']) and 'result' not in q
 for x in q['locators']:assert x['title'] and x['url'].startswith('https://') and '?' not in x['url'] and '…' not in x['url']
assert len({x['q'] for x in web[0]['request']['search_query']})==3
for t in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(t in x['q'] for q in web for x in q['request'].get('search_query',[]))
assert any('after:2021-10-29' in x['q'] and 'before:2026-10-30' in x['q'] for q in web for x in q['request'].get('search_query',[]))
assert rd('optional-math-opinion.json')['status']=='justified n/a'
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
shared=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')
if shared.is_file():assert sha(shared)==v['controls']['shared_prefix_sha256']
report=rpt().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert (D/href[len('../evidence/'+N+'/'):]).is_file(),href
 else:assert href.startswith('https://'),href
for t in ['BORDERLINE-needs-human','NOT-COMPOSABLE','Phase4.5','Phase4.6','Phase5.5','Phase6.0','not a complete kernel body dump','same-exponent Infinite theorem','arbitrary real threshold']:
 assert t.lower() in report.lower(),t
assert len(re.findall(r'^\d+\. ',report,re.M))==3
assert v['no_file_end_build_due'] and v['next_file_end_canonical_index']==289
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical271'+(' DRAFT preparation' if draft else '')+': current recursive manifest, fresh17, exact293,6clean primary/9native receipts,2full callers,standard axioms,15formal,named literature,portable links,3future API questions')
