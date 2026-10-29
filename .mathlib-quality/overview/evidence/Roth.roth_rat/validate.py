#!/usr/bin/env python3
"""Portable read-only canonical289 validator, always checks current manifest."""
from pathlib import Path
import sys,json,hashlib,re
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.roth_rat';draft='--draft'in sys.argv
rd=lambda n:json.loads((D/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 q=rd(n)['result'];q=q.get('structuredContent')or json.loads(q['content'][0]['text']);return q.get('result',q)
def diags(n):
 q=result(n);return q.get('items',q.get('diagnostics',[]))
def msgs(n):return '\n'.join(x['message']for x in diags(n))
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==289
assert a['verdict']=='YES-but-generalise-first'and a['reason']=='LITERATURE-WEAKENING'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
if not draft:
 assert a['completed']and v['completed']and a['allphases']=='PASS'
 for n in ['validation-draft-scratch.json','validation-draft-integrated.json','secret-scan-draft.json']:
  assert rd(n)['result']['exit_code']==0
 assert rd('freeze-status.json')['completed']and rd('freeze-status.json')['native_release']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['full_type']and o['type'].startswith('∀ {α : ℝ}')
assert o['generalization']['proposed_type']=='∀ {α : ℝ}, IsAlgebraic ℚ α → ∀ {κ : ℝ}, {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite → κ ≤ 2'
assert o['generalization']['verified']and o['generalization']['drop']=='Irrational α'
base=rd('input-manifest.json');assert base==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=rd('inputs.json');assert len(inputs)==len(base['sources_and_pins'])==17
for x in inputs:
 assert x['match']and sha(R/x['path'])==x['sha256']==base['sources_and_pins'][x['path']]['sha256']
 assert x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')==dict(inputs=inputs,unchanged=True)
for mod,num in [('Main',588),('LeanEval',66)]:
 p=D/('source-'+mod+'.lean.txt');assert sha(p)==sha(R/('Roth/'+mod+'.lean'))and len(p.read_text().splitlines())==num
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==sha(D/x['archive'])==x['sha256']
for x in rd('additional-inputs.json'):
 p=Path(x['path']);p=p if p.is_absolute()else R/p;assert sha(p)==x['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[288]==rd('canonical-entry.json')and order[288]['name']==N
assert o['project_dependencies']==['Roth.approxSet','Roth.roth']
s=(D/'original-executed.lean.txt').read_text();arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arr)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arr[0])
actual=[('private',m,n)if m else('public',p)for m,n,p in terms]
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
assert actual==expected and len(actual)==len(set(actual))==293
assert rd('target-metadata.json')['source'].replace('theorem roth_rat','theorem replay')in s
assert 'example : @Roth.roth_rat = @Roth289Original.replay := Subsingleton.elim _ _'in s
m=msgs('original-receipt.json')
for t in ['ROTH289_FULL_TYPE:','ROTH289_AUDIT: requested=293; unique=293','ROTH289_AUDIT_PRESENT: present=293; values=293']:assert t in m
assert 'ROTH289_DIRECT_CONSUMER:'not in m and 'ROTH289_DIRECT_TYPE_CONSUMER:'not in m
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
assert c['direct_kernel_value_consumers']==c['direct_kernel_type_consumers']==[]
assert rd('native-type.json')['elided_characters']==[18826]and not rd('native-type.json')['full_kernel_printer_body']
assert '18826 characters elided'in m
assert 'characters elided'not in next(x['message']for x in diags('original-receipt.json')if x['message'].startswith('ROTH289_BODY_CONSTANTS:'))
prefix={}
for k,n,h in [('isolated',18,'21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217'),('disk',9,'363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593')]:
 p=D/(k+'-prefix.lean.txt');assert sha(p)==rd('prefix-controls.json')[k+'_sha256']==h
 prefix[k]=p.read_text();assert len(re.findall(r'^import ',prefix[k],re.M))==n
extra=prefix['isolated']+'import Mathlib.NumberTheory.DiophantineApproximation.Basic\n'
assert hashlib.sha256(extra.encode()).hexdigest()==rd('prefix-authorization.json')['authorized_isolated_prefix_sha256']=='9b1bd511ef007f620a7163c38b76aaf650486373cce45b2a4b108b5c1d83583e'
assert rd('prefix-authorization.json')['root_authorized']and not rd('prefix-authorization.json')['LiouvilleWith_import_authorized']
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==5 and len(v['rejected'])==2
for e in v['accepted']+v['rejected']:
 p=D/e['source'];q=rd(e['receipt']);assert sha(p)==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 assert q['executor']['owner']=='root'
for e in v['accepted']:
 q=rd(e['receipt']);z=result(e['receipt']);s=(D/e['source']).read_text()
 assert z['success']and not z.get('timed_out',False)and not q['result'].get('isError',False)
 assert q['request']==e['original_execution_request']and q['elapsed_ms']==e['elapsed_ms']
 assert not[x for x in diags(e['receipt'])if x['severity']in['error','warning']or x.get('category')=='sorry']
 if e['format']=='disk':assert z['partial']is False and not z['failed_dependencies']and s.startswith(prefix['disk'])
 else:assert q['request']['code']==s and s.startswith(extra)and '#check_failure '+N in s and 'import Roth'not in s
 assert re.findall(r'^import (.+)$',s,re.M)==re.findall(r'^import (.+)$',prefix['disk']if e['format']=='disk'else extra,re.M)
 assert max(map(len,s.splitlines()))<=100 and all(x==x.rstrip()for x in s.splitlines())and s.endswith('\n')and not s.endswith('\n\n')
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 t=msgs(e['receipt']);assert 'sorryAx'not in t and 'PANIC'not in t
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',t);assert axs
 for xs in axs:assert{x.strip()for x in xs.split(',')if x.strip()}<=allowed
assert not result('general01-receipt.json')['success']and 'sorryAx'in msgs('general01-receipt.json')
assert result('shape01-receipt.json')['success']and 'PANIC'in msgs('shape01-receipt.json')
assert v['attempt_accounting']==dict(native_executions=7,accepted=5,rejected=2)
shape=(D/'shape2-executed.lean.txt').read_text();assert 'ci.value? (allowOpaque := true)'in shape
assert 'ROTH289_INLINE_TARGET_FREE'in msgs('shape02-receipt.json')
assert len(rd('callers.json')['explicit_proof_callers'])==len(rd('callers.json')['explicit_type_callers'])==0
assert 'example : @Roth.roth_rat = @inline_endpoint := Subsingleton.elim _ _'in shape
assert 'Roth.roth hα halg (rational_to_pairs hinf)'in shape
modern=(D/'modern-executed.lean.txt').read_text();general=(D/'general2-executed.lean.txt').read_text();edges=(D/'edges-executed.lean.txt').read_text()
for t in ['lemma cofinite_iff_finite','lemma exponent_iff_cofinite','lemma cofinite_consequence','lemma recover','eventually_cofinite, not_le']:assert t in modern
for t in ['lemma inferred_irrational','Real.rpow_le_rpow_of_exponent_le','lemma generalize','lemma recover','hR (inferred_irrational hκ.le hinf) halg hinf','by exact?','by aesop']:assert t in general
for t in ['lemma rational_finite','lemma sharp','lemma coefficient_le_one','lemma zero_pairs_infinite']:assert t in edges
ph=rd('phase-checks.json');assert len(ph['modern9'])==9 and len(ph['proofstrategy5'])==5 and len(ph['statement_shape3'])==3 and len(ph['infrastructure_risks'])==6 and all(x['status']=='n/a'for x in ph['infrastructure_risks'])
fm=rd('formal-search-matrix.json')['cells'];assert len(fm)==15
assert{(x['form'],x['method'])for x in fm}=={(f,m)for f in ['current','standard','abstract']for m in ['leanfinder','leansearch','loogle','rg','local']}
for e in fm:assert(D/e['receipt']).is_file()
for f in ['current','standard','abstract']:
 for method in ['leanfinder','leansearch','loogle']:assert not rd(f'formal-{f}-{method}.json')['result'].get('isError',False)
 assert result(f'formal-{f}-local.json')['index']=='error'
assert rd('full-name-search.json')['status']==1 and not rd('full-name-search.json')['stdout']
lit=rd('literature.json');assert len(set(lit['general_queries']))>=3
assert{x['channel']for x in lit['channels']}=={'web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'}
assert not lit['third_party_bodies_persisted']and lit['optional_channel']['status'].startswith('unavailable')
assert any('site:ncatlab.org/ncatlab'in x['query']for x in lit['channels'])
assert any('after:2021-10-29 before:2026-10-30'in x['query']for x in lit['channels'])
assert len(list(D.glob('web-batch*.json')))==5
for p in D.glob('web-batch*.json'):
 x=json.loads(p.read_text());assert re.fullmatch('[0-9a-f]{64}',x['response_sha256'])and x['response_bytes']>0 and x['request']
 for item in x['links']:assert '?'not in item['url']and '...'not in item['url']
b=rd('file-end-build.json');assert b['command']==['lake','build']and b['exit_code']==b['warning_count']==0 and b['executor']=='root'
assert b['elapsed_ms']==6833.895 and sha(D/b['log'])==b['log_sha256']=='b7f96a04d807f93a54c01314b6f59b969256b6222dffa7ae4b62832d3a174e65'
for x in inputs:assert b['sources_and_pins'][x['path']]['sha256']==x['sha256']and b['sources_and_pins'][x['path']]['matches_baseline']
report=D/'report.md'
if not report.is_file():report=D.parent.parent/'mathlibable'/(N+'.md')
r=report.read_text();assert r.endswith('\n')and not r.endswith('\n\n')and all(l==l.rstrip()for l in r.splitlines())
for link in re.findall(r'\]\(([^)]+)\)',r):
 if link.startswith('https://'):continue
 pref='../evidence/'+N+'/';assert link.startswith(pref)and(D/link[len(pref):]).is_file(),link
manifest=rd('copy-manifest.json');assert manifest['declaration']==N;covered=set()
for e in manifest['files']:
 pref='.mathlib-quality/overview/evidence/'+N+'/'
 if e['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=report;rel='report.md'
 else:assert e['destination'].startswith(pref);rel=e['destination'][len(pref):];p=D/rel
 assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],str(p)
 assert rel not in covered;covered.add(rel)
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in exclude and '_validation-layout'not in p.relative_to(D).parts}
if not(D/'report.md').exists():files.add('report.md')
assert files==covered,(files-covered,covered-files)
for p in D.glob('*.py'):
 t=p.read_text();assert all(x==x.rstrip()for x in t.splitlines())and t.endswith('\n')and not t.endswith('\n\n'),p
assert not list(p for p in D.rglob('*.lean')if '_validation-layout'not in p.relative_to(D).parts)
print('PASS canonical289 currentmanifest/fresh17/exact293/native5/rejected2/formal15/zeroactualcallers/generality/cofinite/build/links')
