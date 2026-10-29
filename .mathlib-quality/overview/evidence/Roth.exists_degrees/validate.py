#!/usr/bin/env python3
"""Read-only portable canonical278 assessment validator; default never accepts drafts."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
draft='--draft'in sys.argv;N='Roth.exists_degrees'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result'];z=z.get('structuredContent')or json.loads(z['content'][0]['text']);return z.get('result',z)
def ds(n):
 z=result(n);return z.get('items',z.get('diagnostics',[]))
def messages(n):return '\n'.join(x['message']for x in ds(n))
def report():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.exists():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==278
assert a['verdict']=='YES-but-generalise-first'and a['root_acceptance']in['pending','PASS']
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']and not a['unresolved']and not v['unresolved']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
nt=rd('native-type.json');assert o['type']==nt['type']and o['type'].startswith('∀ {m : ℕ}')
assert 'δ ≤ 1'in o['type']and '∃ (r : Fin m → ℕ)'in o['type']
assert o['project_dependencies']==nt['original_project_dependencies']==[]
assert not nt['full_kernel_printer_body']and nt['elided_characters']==[78277]
assert o['generalization']['verified']and '[FloorRing K]'in o['generalization']['proposed_type']
assert '[Finite ι]'in o['generalization']['proposed_type']and '(hc : 1 < c)'in o['generalization']['proposed_type']
assert '(hδ : 0 < δ)'not in o['generalization']['proposed_type']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[277]==rd('canonical-entry.json')and order[277]['name']==N
s=(D/'original-executed.lean.txt').read_text();ars=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(ars)==1
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
ts=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",ars[0]);actual=[('private',m,n)if m else('public',p)for m,n,p in ts]
assert actual==expected and len(actual)==len(set(actual))==293
assert rd('target-metadata.json')['source'].replace('theorem exists_degrees','theorem replay')in s
assert 'example : @Roth.exists_degrees = @Degrees278Original.replay := Subsingleton.elim _ _'in s
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json');assert len(base)==len(fresh)==17
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for m in ['Main','LeanEval']:assert sha(R/('Roth/'+m+'.lean'))==sha(D/('source-'+m+'.lean.txt'))
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']==sha(D/x['archive'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
pc=rd('prefix-controls.json');assert pc['declaration']==N
for k,n,known in [('isolated',18,'21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217'),('disk',9,None)]:
 c=pc[k];p=D/c['archive'];assert sha(p)==c['sha256']and(c['sha256']==known if known else True)
 assert len(c['imports'])==c['count']==n and re.findall(r'^import (.+)$',p.read_text(),re.M)==c['imports']
# Prefix authorization is self-contained; never read external mutable /tmp controls.
auth=rd('native-prefix-authorization.json');extra=pc['isolated']['imports']+['Mathlib.Algebra.Order.Floor.Semifield']
ps=(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.Algebra.Order.Floor.Semifield\n'
assert(D/'candidate-prefix.lean.txt').read_text()==ps
assert auth['declaration']==N and auth['modules']==['Mathlib.Algebra.Order.Floor.Semifield']and auth['root_review']
assert auth['prefix_sha256']==[hashlib.sha256(ps.encode()).hexdigest()]==['4a045eaa6d4f0fbe919e3bf25579e8ce8654472204255f7ab0898dd2d8de805d']
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label']for x in v['accepted']}=={'original','generic','recovery','callers','composition','edges','candidate'}
for e in v['accepted']:
 p=D/e['source'];s=p.read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(p)==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 assert q['executor']['owner']=='root'and q['request']==e['original_execution_request']and q['elapsed_ms']==e['elapsed_ms']
 assert not q['result'].get('isError',False)and z['success']and not z.get('timed_out',False)
 assert not[x for x in ds(e['receipt'])if x['severity']in['error','warning']or x.get('category')=='sorry']
 assert max(map(len,s.splitlines()))<=100
 imports=re.findall(r'^import (.+)$',s,re.M)
 if e['format']=='disk':
  assert z['partial']is False and not z['failed_dependencies']and s.startswith((D/'disk-prefix.lean.txt').read_text())and imports==pc['disk']['imports']
 else:
  assert q['request']['code']==s and '#check_failure '+N in s
  assert imports==(extra if e['label']=='candidate'else pc['isolated']['imports'])
  assert s.startswith(ps if e['label']=='candidate'else(D/'isolated-prefix.lean.txt').read_text())
 t='\n'.join(x['message']for x in ds(e['receipt'])if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in t and 'PANIC'not in t
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',t)
 if e['axiom_print_required']:assert ax
 for xs in ax:assert{x.strip()for x in xs.split(',')if x.strip()}<=allowed
 assert all(x in t for x in e['required_info']),e['label']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 if'code'in q['request']:assert q['request']['code']==(D/e['source']).read_text()
 assert any(x['severity']in['error','warning']for x in ds(e['receipt']))
assert v['attempt_accounting']['native_executions']==len(v['accepted'])+len(v['other_executions'])
assert 'DEG278_DIRECT_CONSUMER: _private.Roth.Main.0.Roth.exists_roth_approximants_aux'in messages('original-receipt.json')
assert 'DEG278_DIRECT_TYPE_CONSUMER:'not in messages('original-receipt.json')
assert len(re.findall('characters elided',messages('original-receipt.json')))==1
cc=(D/'callers5-executed.lean.txt').read_text();caller=(D/'caller-excerpt.lean.txt').read_text().strip()
assert caller.replace('private lemma exists_roth_approximants_aux','theorem replaced').replace('exists_degrees hδ0 hδ1 hq1','Degrees278Recovery.all_positive_delta hδ0 hq1')in cc
compact=lambda s:' '.join(s.split())
assert compact(rd('target-metadata.json')['body'].removeprefix('by\n'))in compact(cc)
rec=(D/'recovery5-executed.lean.txt').read_text()
assert 'theorem all_positive_delta'in rec and 'theorem recovered'in rec and '(_hδ1 : δ ≤ 1)'in rec
assert 'example : @Roth.exists_degrees = @Degrees278Recovery.recovered := Subsingleton.elim _ _'in rec
c=rd('callers.json');assert c['explicit_caller_count']==1 and c['external_to_file_count']==0 and c['callers'][0]['call_line']==440
p=rd('phase-checks.json');assert len(p['modern9'])==9 and len(p['proofstrategy5'])==5 and len(p['statement_shape3'])==3 and len(p['infrastructure_risks'])==6
fm=rd('formal-search-matrix.json');assert len(fm['cells'])==15 and{(x['form'],x['method'])for x in fm['cells']}=={(f,m)for f in['current','standard','abstract']for m in['leanfinder','loogle','leansearch','rg','local']}
for x in fm['cells']:assert(D/x['receipt']).is_file()
for f in['current','standard','abstract']:
 assert result('formal-'+f+'-local.json')['index']in['error','warming']
 for m in['leanfinder','leansearch','loogle']:assert not rd('formal-'+f+'-'+m+'.json')['result']['isError']
assert result('formal-abstract-local-retry.json')['index']=='error'
lit=rd('literature.json');assert len(lit['general_queries'])>=3 and len({x['q']for x in lit['general_queries']})>=3
assert{x['channel']for x in lit['channels']}=={'web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'}and not lit['third_party_bodies_persisted']
assert lit['optional_channel']['channel']=='ask_chatgpt_math'and lit['local_channel']['channel']=='local'
for name in['web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-locator']:
 z=rd(name+'.json');assert re.fullmatch('[0-9a-f]{64}',z['response_sha256'])and z['response_bytes']>0 and z['request']and z['status']=='returned'
assert 'site:ncatlab.org/ncatlab'in rd('ncatlab.json')['request']['search_query'][0]['q']
assert 'after:2021-10-29 before:2026-10-30'in rd('arxiv.json')['request']['search_query'][0]['q']
for link in re.findall(r'\]\(([^)]+)\)',report().read_text()):
 if link.startswith('https://'):continue
 pref='../evidence/'+N+'/';assert link.startswith(pref)and(D/link[len(pref):]).is_file(),link
m=rd('copy-manifest.json');assert m['declaration']==N and m['recursive'];covered=set()
for e in m['files']:
 pref='.mathlib-quality/overview/evidence/'+N+'/'
 if e['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=report();rel='report.md'
 else:assert e['destination'].startswith(pref);rel=e['destination'][len(pref):];p=D/rel
 assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],str(p)
 assert rel not in covered;covered.add(rel)
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in exclude and '_validation-layout'not in p.relative_to(D).parts}
if not(D/'report.md').exists():files.add('report.md')
assert files==covered,(files-covered,covered-files)
assert not list(p for p in D.rglob('*.lean')if '_validation-layout'not in p.relative_to(D).parts)
for n in['validation-scratch.json','validation-integrated.json','secret-scan.json']:
 if(D/n).exists():assert rd(n)['result']['exit_code']==0
print('PASS canonical278 current manifest, phases, sources17, exact293, native7, complete caller, formal15, prefixes, links')
