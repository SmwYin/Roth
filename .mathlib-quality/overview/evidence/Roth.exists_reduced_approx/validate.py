#!/usr/bin/env python3
"""Read-only canonical274 validator, CURRENT recursive manifest, scratch or integrated layout."""
from pathlib import Path
import json,hashlib,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_reduced_approx';draft='--draft'in sys.argv
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def messages(n):
 z=result(n);return '\n'.join(x['message']for x in z.get('items',z.get('diagnostics',[])))
def report():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==274
assert a['verdict']=='YES-but-generalise-first'and a['root_acceptance']in ['pending','PASS']
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
assert not a['unresolved']and not v['unresolved']and not a['parent_verdict_inherited']
assert not a['cost_based_verdict']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and o['type'].startswith('∀ {α : ℝ}')
canonical_names={x['name']for x in rd('canonical-snapshot.json')}
assert all(x in canonical_names for x in o['project_dependencies'])
assert o['project_dependencies']==[x.replace('_private.Roth.Main.0.','')
 for x in rd('native-type.json')['original_project_dependencies']]
assert not any(x.startswith('_private.')for x in o['project_dependencies'])
assert o['generalization']['verified']and '0 < κ'in o['type']
assert '0 < κ'not in o['generalization']['proposed_type']
assert 'κ ≤ 2'in o['generalization']['subcritical_type']
assert rd('native-type.json')['elided_characters']==[86997]
assert not rd('native-type.json')['full_kernel_printer_body']
# Validate every artifact using the CURRENT manifest; historical worker manifest is not authoritative.
m=rd('copy-manifest.json');assert m['declaration']==N and m['recursive'];covered=set()
for e in m['files']:
 pref='.mathlib-quality/overview/evidence/'+N+'/'
 if e['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=report();rel='report.md'
 else:
  assert e['destination'].startswith(pref);rel=e['destination'][len(pref):];p=D/rel
 assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],p
 assert rel not in covered;covered.add(rel)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in excluded
 and '_validation-layout'not in p.relative_to(D).parts}
if not(D/'report.md').exists():files.add('report.md')
assert files==covered,(files-covered,covered-files)
assert not list(D.rglob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {e['label']for e in v['accepted']}=={
 'original','callers','consumers','isolated','generic','composition','counterexample'}
base=(D/'isolated-prefix.lean.txt').read_text();baseimports=re.findall(r'^import (.+)$',base,re.M)
assert len(baseimports)==18
auth=rd('native-prefix-authorization.json');assert auth['declaration']==N
assert auth['modules']==['Mathlib.NumberTheory.DiophantineApproximation.Basic']
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 assert q['executor']['owner']=='root'and q['request']==e['original_execution_request']
 assert q['elapsed_ms']==e['elapsed_ms']and isinstance(q['elapsed_ms'],int)
 assert not q['result'].get('isError',False)and z['success']and not z.get('timed_out',False)
 imports=re.findall(r'^import (.+)$',s,re.M)
 if e['format']=='disk':
  assert z['partial']is False and not z['failed_dependencies']
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(imports)==9
 else:
  assert q['request']['code']==s and '#check_failure '+N in s
  assert imports==baseimports or imports==baseimports+auth['modules']
  if len(imports)==19:
   assert hashlib.sha256(('\n'.join('import '+x for x in imports)+'\n').encode()).hexdigest()in auth['prefix_sha256']
  assert not any(x.startswith('Roth')for x in imports)
 ds=z.get('items',z.get('diagnostics',[]))
 assert not [x for x in ds if x['severity']in ['error','warning']or x.get('category')=='sorry']
 t='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in t and 'PANIC'not in t
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',t)
 if e['axiom_print_required']:assert axs
 for xs in axs:assert {x.strip()for x in xs.split(',')if x.strip()}<=allowed
 assert all(x in t for x in e['required_info']),e['label']
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']
 assert q['executor']['worker_request']['source_sha256']==e['source_sha256']
 if 'code'in q['request']:assert q['request']['code']==(D/e['source']).read_text()
 assert not result(e['receipt'])['success']and e['status']=='rejected'
assert len(v['accepted'])==7 and len(v['other_executions'])==3
assert 'sorryAx'in messages('isolated-receipt.json')and 'sorryAx'in messages('counterexample-receipt.json')
assert v['attempt_accounting']['native_executions']==10
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json');assert len(b)==len(fresh)==17
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:
 assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']==sha(D/x['archive'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[273]==rd('canonical-entry.json')and order[273]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for name in ['original-executed.lean.txt','consumer-scope-executed.lean.txt','consumer-scope2-executed.lean.txt']:
 s=(D/name).read_text();ars=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(ars)==1
 ts=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",ars[0])
 actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in ts]
 assert actual==expected and len(actual)==len(set(actual))==293
for name in ['original-receipt.json','consumers2-receipt.json']:
 t=messages(name);assert 'REDUCED274_AUDIT: requested=293; unique=293'in t
 assert 'REDUCED274_AUDIT_PRESENT: present=293; values=293'in t
c=rd('canonical-consumers.json');assert c['direct_type_consumers']==[]
assert c['direct_value_consumers']==['Roth.exists_approximants']
assert len(c['transitive_project_consumers'])==6
assert rd('callers.json')['explicit_caller_count']==1
assert rd('callers.json')['external_to_file_count']==0
src=(D/'original-executed.lean.txt').read_text()
assert rd('target-metadata.json')['source'].replace('theorem exists_reduced_approx','theorem replay')in src
assert(D/'helper-excerpt.lean.txt').read_text().strip().replace('private theorem','theorem')in src
fm=rd('formal-search-matrix.json');assert len(fm['cells'])==15
assert {(x['form'],x['method'])for x in fm['cells']}=={
 (f,t)for f in ['current','standard','abstract']for t in ['finder','search','loogle','rg','local']}
for x in fm['cells']:assert(D/x['receipt']).is_file()
for f in ['current','standard','abstract']:assert result('formal-'+f+'-local.json')['index']=='error'
p=rd('phase-checks.json');assert len(p['modern9'])==9 and len(p['proofstrategy5'])==5
assert len(p['statement_shape3'])==3 and len(p['infrastructure_risks'])==6
lit=rd('literature.json');assert len(lit['general_queries'])>=3
assert {'nLab','nCatLab','Stacks','MathOverflow','recent arXiv','local','ask_chatgpt_math'}<={x['channel']for x in lit['channels']}
assert not lit['third_party_bodies_persisted']
for i in range(1,6):
 z=rd(f'web{i}-receipt.json');assert re.fullmatch('[0-9a-f]{64}',z['response_sha256'])
 assert z['response_bytes']>0 and z['request']and z['status']=='returned'
for link in re.findall(r'\]\(([^)]+)\)',report().read_text()):
 if link.startswith('https://'):continue
 pref='../evidence/'+N+'/';assert link.startswith(pref),link
 assert(D/link[len(pref):]).is_file(),link
if(D/'validation-scratch.json').exists():
 for n in ['validation-scratch.json','validation-integrated.json']:
  if(D/n).exists():
   x=rd(n);assert x['result']['exit_code']==0 and 'PASS canonical274'in x['result']['output']
  else:assert draft
if(D/'secret-scan.json').exists():assert rd('secret-scan.json')['result']['exit_code']==0
print('PASS canonical274 current manifest, all phases, sources17, canonical293, native7, rejected3, links')
