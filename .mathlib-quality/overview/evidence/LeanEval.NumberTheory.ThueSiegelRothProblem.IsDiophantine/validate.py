#!/usr/bin/env python3
"""Read-only canonical290 current-manifest validator; scratch/integrated layouts."""
from pathlib import Path
import sys,json,hashlib,re
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine';draft='--draft'in sys.argv
rd=lambda n:json.loads((D/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 r=rd(n)['result'];r=r.get('structuredContent')or json.loads(r['content'][0]['text']);return r.get('result',r)
def diags(n):
 r=result(n);return r.get('items',r.get('diagnostics',[]))
def msgs(n):return '\n'.join(d['message']for d in diags(n))
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==290
assert a['verdict']=='BORDERLINE-needs-human'and not a['parent_verdict_inherited']and not a['cost_based_verdict']
assert a['unresolved']==v['unresolved']==[]and a['root_acceptance']in['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases and all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['full_type']=='ℝ → Prop'and o['project_dependencies']==[]
assert o['generalization']['verified']and 'Irrational x ∧'in o['generalization']['modern_type']
base=rd('input-manifest.json');assert base==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=rd('inputs.json');assert len(inputs)==len(base['sources_and_pins'])==17
for x in inputs:assert x['match']and sha(R/x['path'])==x['sha256']==base['sources_and_pins'][x['path']]['sha256']and(R/x['path']).stat().st_size==x['bytes']
assert rd('fresh-final-inputs.json')==dict(inputs=inputs,unchanged=True)
for f in ['Main','LeanEval']:assert sha(D/('source-'+f+'.lean.txt'))==sha(R/('Roth/'+f+'.lean'))
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==sha(D/x['archive'])==x['sha256']
for x in rd('additional-inputs.json'):assert sha(Path(x['path']))==x['sha256']and Path(x['path']).stat().st_size==x['bytes']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[289]==rd('canonical-entry.json')and order[289]['name']==N
s=(D/'original-executed.lean.txt').read_text();arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arr)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arr[0])
actual=[('private',m,n)if m else('public',p)for m,n,p in terms]
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
assert actual==expected and len(set(actual))==293
assert rd('target-metadata.json')['source']in s and 'Diophantine290Original.IsDiophantine := rfl'in s
m=msgs('original01-receipt.json')
for marker in ['D290_FULL_TYPE: ℝ → Prop','D290_AUDIT: requested=293; unique=293','D290_AUDIT_PRESENT: present=293; values=293']:assert marker in m
for kind in ['TYPE','BODY']:
 consumers=re.findall('D290_DIRECT_'+kind+'_CONSUMER: ([^\n]+)',m)
 assert consumers==[N.rsplit('.',1)[0]+'.isDiophantine_iff',N.rsplit('.',1)[0]+'.thueSiegelRoth']
assert 'characters elided'not in m and rd('native-type.json')['full_kernel_printer_body']
prefix={}
for k,count,h in [('isolated',18,'21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217'),('disk',9,'363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593')]:
 p=D/(k+'-prefix.lean.txt');assert sha(p)==rd('prefix-controls.json')[k+'_sha256']==h
 prefix[k]=p.read_text();assert len(re.findall(r'^import ',prefix[k],re.M))==count
extra=prefix['isolated']+'import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
assert hashlib.sha256(extra.encode()).hexdigest()==rd('prefix-authorization.json')['authorized_isolated_prefix_sha256']=='effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc'
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {e['id']for e in v['accepted']}=={'original01','callers01','shape02','modern03'}and len(v['rejected'])==3
for e in v['accepted']+v['rejected']:
 p=D/e['source'];j=rd(e['receipt']);assert sha(p)==e['source_sha256']==j['executor']['worker_request']['source_sha256']
 assert j['executor']['owner']=='root'and j['request']==e['original_execution_request']and j['elapsed_ms']==e['elapsed_ms']
for e in v['accepted']:
 z=result(e['receipt']);j=rd(e['receipt']);s=(D/e['source']).read_text()
 assert z['success']and not z.get('timed_out')and not z.get('partial')and not j['result'].get('isError')
 assert not[d for d in diags(e['receipt'])if d['severity']in['error','warning']or d.get('category')=='sorry']
 if e['format']=='disk':assert z['partial']is False and not z['failed_dependencies']and s.startswith(prefix['disk'])
 else:assert j['request']['code']==s and s.startswith(extra)and '#check_failure '+N in s and 'import Roth'not in s
 assert re.findall(r'^import (.+)$',s,re.M)==re.findall(r'^import (.+)$',prefix['disk']if e['format']=='disk'else extra,re.M)
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 t=msgs(e['receipt']);assert 'sorryAx'not in t and 'PANIC'not in t
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',t);assert axs
 for xs in axs:assert{x.strip()for x in xs.split(',')if x.strip()}<=allowed
for e in v['rejected']:assert not result(e['receipt'])['success']and 'sorryAx'in msgs(e['receipt'])
assert v['attempt_accounting']==dict(native_executions=7,accepted=4,rejected=3)
original=(D/'source-LeanEval.lean.txt').read_text();body=original[original.index('namespace LeanEval.'):].replace('LeanEval.NumberTheory.ThueSiegelRothProblem','Diophantine290Callers')
assert body in(D/'callers-executed.lean.txt').read_text()
for n in ['isDiophantine_iff','thueSiegelRoth']:assert'D290_CALLER_TARGET_FREE: Diophantine290Callers.'+n in msgs('callers01-receipt.json')
assert len(rd('callers.json')['explicit_callers'])==2
modern=(D/'modern3-executed.lean.txt').read_text()
for token in ['UniformBound t x ↔ Irrational x ∧','lemma cutoff_mono','lemma add_rat_iff','lemma mul_rat_iff','lemma rational_cutoff','lemma liouville_not_uniform','¬ UniformBound 2 0','liouvilleWith_one 0','example (x : ℝ) : UniformBound 2 x ↔']:assert token in modern
ph=rd('phase-checks.json');assert len(ph['modern9'])==9 and len(ph['proofstrategy5'])==5 and len(ph['statement_shape3'])==3 and len(ph['infrastructure_risks'])==6
fm=rd('formal-search-matrix.json')['cells'];assert len(fm)==15
assert{(x['form'],x['method'])for x in fm}=={(f,m)for f in ['current','standard','abstract']for m in ['leanfinder','leansearch','loogle','rg','local']}
for e in fm:assert(D/e['receipt']).is_file()
for f in ['current','standard','abstract']:
 for method in ['leanfinder','leansearch','loogle']:
  name='formal-'+f+'-'+method+('-retry'if f=='current'and method=='loogle'else'')+'.json';assert not rd(name)['result'].get('isError')
 assert result('formal-'+f+'-local.json')['index']==('warming'if f=='abstract'else'error')
lit=rd('literature.json');assert len(set(lit['general_queries']))>=3 and lit['explicit_mathlib_web_queries']
assert{x['channel']for x in lit['channels']}=={'web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'}
assert not lit['third_party_bodies_persisted']and lit['optional_channel']['status'].startswith('unavailable')
assert any('site:ncatlab.org/ncatlab'in x['query']for x in lit['channels'])and any('after:2021-10-29 before:2026-10-30'in x['query']for x in lit['channels'])
for p in D.glob('web-batch*.json'):
 x=json.loads(p.read_text());assert re.fullmatch('[0-9a-f]{64}',x['response_sha256'])and x['response_bytes']>0 and x['request']
 assert all('?'not in u and '...'not in u for u in x['links'])and not x['third_party_body_persisted']
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
print('PASS canonical290 currentmanifest/fresh17/exact293/native4/rejected3/formal15/fullcallers/semanticguard/links')
