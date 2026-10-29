#!/usr/bin/env python3
"""Read-only293 current manifest, exact native provenance and portable layout validation."""
from pathlib import Path
import json,hashlib,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth';draft='--draft'in sys.argv
rd=lambda n:json.loads((D/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 r=rd(n)['result'];r=r.get('structuredContent')or json.loads(r['content'][0]['text']);return r.get('result',r)
def ds(n):
 r=result(n);return r.get('items',r.get('diagnostics',[]))
def msgs(n):return '\n'.join(x['message']for x in ds(n))
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==293
assert a['verdict']=='YES-but-generalise-first'and a['reason']=='MODERN-IDIOM'and a['classification']=='BIG'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']and a['root_acceptance']in ['pending','PASS']
assert a['unresolved']==v['unresolved']==[]
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
required={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert required<=set(o)and o['type']==rd('native-type.json')['full_type']
assert 'Irrational x → IsAlgebraic ℤ x →'in o['type']and rd('native-type.json')['full_kernel_printer_body']
deps=['LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff','Roth.roth','Roth.approxSet']
assert o['project_dependencies']==deps
assert set(deps)<={x['name']for x in rd('canonical-snapshot.json')}
assert o['generalization']['verified']and 'Irrational x ∧'in o['generalization']['exact_uniform_bridge']
base=rd('input-manifest.json');assert base==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=rd('inputs.json');assert len(inputs)==len(base['sources_and_pins'])==17
for x in inputs:assert x['match']and sha(R/x['path'])==x['sha256']==base['sources_and_pins'][x['path']]['sha256']and(R/x['path']).stat().st_size==x['bytes']
assert rd('fresh-final-inputs.json')==dict(inputs=inputs,unchanged=True)
for f in ['Main','LeanEval']:assert sha(D/('source-'+f+'.lean.txt'))==sha(R/('Roth/'+f+'.lean'))
for x in rd('mathlib-inputs.json'):assert sha(Path(x['path']))==sha(D/x['archive'])==x['sha256']
for x in rd('additional-inputs.json'):
 if x['path'].endswith('progress.json'):continue
 assert sha(R/x['path'])==x['sha256']and(R/x['path']).stat().st_size==x['bytes']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[292]==rd('canonical-entry.json')and order[292]['name']==N
s=(D/'original-executed.lean.txt').read_text();arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arr)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arr[0])
actual=[('private',m,n)if m else('public',p)for m,n,p in terms]
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
assert actual==expected and len(set(actual))==293 and rd('target-metadata.json')['source']in s
assert 'ci.value? (allowOpaque := true)'in s and 'value!'not in s and 'D293_MISSING_VALUE'in s
m=msgs('original01-receipt.json')
for marker in ['D293_FULL_TYPE:','D293_AUDIT: requested=293; unique=293','D293_AUDIT_PRESENT: present=293; values=293']:assert marker in m
assert 'D293_DIRECT_TYPE_CONSUMER:'not in m and 'D293_DIRECT_BODY_CONSUMER:'not in m
assert rd('canonical-consumers.json')==dict(type=[],body=[],requested=293,unique=293,present=293,values=293)
prefix={}
for k,count,h,key in [('isolated',18,'21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217','shared18_sha256'),('disk',9,'363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593','disk9_sha256')]:
 p=D/(k+'-prefix.lean.txt');assert sha(p)==rd('prefix-controls.json')[key]==h
 prefix[k]=p.read_text();assert len(re.findall(r'^import ',prefix[k],re.M))==count
extra=prefix['isolated']+'import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
project='\n'.join(prefix['disk'].splitlines()[:9])+'\nimport Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
assert hashlib.sha256(extra.encode()).hexdigest()==rd('prefix-controls.json')['authorized19_sha256']=='effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc'
assert hashlib.sha256(project.encode()).hexdigest()==rd('prefix-controls.json')['project10_sha256']=='4761c6a729fe5e133a97cd57f46600bf09ea76d6e8bc21470618789bf86a9cac'
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert{e['id']for e in v['accepted']}=={'original01','generality02','modern01','composition01','projectmodern01'}
assert[e['id']for e in v['rejected']]==['generality01']and v['attempt_accounting']==dict(native_executions=6,accepted=5,rejected=1)
for e in v['accepted']+v['rejected']:
 p=D/e['source'];j=rd(e['receipt']);assert sha(p)==e['source_sha256']==j['executor']['worker_request']['source_sha256']
 assert j['executor']['owner']=='root'and j['request']==e['original_execution_request']and j['elapsed_ms']==e['elapsed_ms']
for e in v['accepted']:
 z=result(e['receipt']);j=rd(e['receipt']);s=(D/e['source']).read_text()
 assert z['success']and not z.get('timed_out')and not z.get('partial')and not j['result'].get('isError')
 assert not[x for x in ds(e['receipt'])if x['severity']in ['error','warning']or x.get('category')=='sorry']
 assert 'sorryAx'not in msgs(e['receipt'])and 'PANIC'not in msgs(e['receipt'])
 if e['format']=='disk':assert z['partial']is False and not z['failed_dependencies']and s.startswith(prefix['disk']);pfx=prefix['disk']
 else:
  assert j['request']['code']==s
  pfx=extra if e['format']=='isolated'else project
  assert s.startswith(pfx)
  if e['format']=='isolated':assert 'import Roth'not in s and '#check_failure '+N in s
  else:assert j['executor']['worker_request']['context']=='project_endpoint293'
 assert re.findall(r'^import (.+)$',s,re.M)==re.findall(r'^import (.+)$',pfx,re.M)
 assert max(map(len,s.splitlines()))<=100 and not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',msgs(e['receipt']));assert axs
 for xs in axs:assert{x.strip()for x in xs.split(',')if x.strip()}<=allowed
assert not result('generality01-receipt.json')['success']and 'sorryAx'in msgs('generality01-receipt.json')
assert rd('callers.json')['canonical_source_callers']==[]and rd('callers.json')['internal_use_count']==0
modern=(D/'modern-executed.lean.txt').read_text()
for token in ['UniformBound t x ↔ Irrational x ∧','lemma rational_cutoff','lemma rational_pair_infinite','lemma uniform_pair_iff_all_real','lemma pair_liouville_iff_all_real','lemma weak_uniform_iff','lemma cutoff_mono','lemma add_rat_iff','lemma mul_rat_iff']:assert token in modern
projectsource=(D/'project-modern-executed.lean.txt').read_text()
for token in ['lemma algebraic_not_liouville','lemma family_recovery','lemma liouville_counterexample','lemma no_irrational_free_uniform','(Roth.roth hx ha)']:assert token in projectsource
ph=rd('phase-checks.json');assert len(ph['modern9'])==9 and len(ph['proofstrategy5'])==5 and len(ph['statement_shape3'])==3 and len(ph['infrastructure_risks'])==6
fm=rd('formal-search-matrix.json');assert len(fm)==15
assert{(x['form'],x['method'])for x in fm}=={(f,m)for f in ['current','standard','abstract']for m in ['leanfinder','leansearch','loogle','rg','local']}
for e in fm:
 assert(D/e['receipt']).is_file()
 if e['method']in ['leanfinder','leansearch','loogle']:assert not rd(e['receipt'])['result'].get('isError')
assert rd('formal-current-loogle.json')['result']['isError']
for f in ['current','standard','abstract']:assert result('formal-'+f+'-local.json')['index']==('warming'if f=='abstract'else'error')
lit=rd('literature.json');assert len(set(lit['general_queries']))>=3 and not lit['third_party_bodies_persisted']and lit['optional_channel']['status'].startswith('unavailable')
assert{x['channel']for x in lit['channels']}=={'web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'}
assert any('site:ncatlab.org/ncatlab'in x['query']for x in lit['channels'])and any('after:2021-10-29 before:2026-10-30'in x['query']for x in lit['channels'])
for p in D.glob('web-batch*.json'):
 x=json.loads(p.read_text());assert re.fullmatch('[0-9a-f]{64}',x['response_sha256'])and x['response_bytes']>0 and x['request']and not x['full_response_archived']
progress=rd('progress-snapshot.json')['completed_declarations']
for n in ['Roth.roth_of_isIntegral','Roth.roth','Roth.roth_rat']:assert any(x['declaration']==n and x['acceptance']=='PASS'and x['verdict'].startswith('YES')for x in progress)
report=D/'report.md'
if not report.is_file():report=D.parent.parent/'mathlibable'/(N+'.md')
r=report.read_text();assert r.endswith('\n')and not r.endswith('\n\n')and all(l==l.rstrip()for l in r.splitlines())
for token in ['MODERN-IDIOM','PROJECT-CONTEXT','not dead code','DiophantineApproximation/Roth.lean','483ba09b','834e5169','No parent verdict is inherited']:assert token in r
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
assert not list(p for p in D.rglob('*.lean')if '_validation-layout'not in p.relative_to(D).parts)
print('PASS canonical293 currentmanifest/fresh17/exact293/native5/rejected1/formal15/zeroactualcallers/fulluniformrecovery/links')
