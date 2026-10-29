#!/usr/bin/env python3
"""Read-only canonical275 current-manifest validator, scratch and integrated layouts."""
from pathlib import Path
import sys,json,re,hashlib
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();draft='--draft'in sys.argv;N='Roth.exists_m'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def ds(n):
 z=result(n);return z.get('items',z.get('diagnostics',[]))
def messages(n):return '\n'.join(x['message']for x in ds(n))
def report():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');nt=rd('native-type.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==275
assert a['verdict']=='BORDERLINE-needs-human'and a['root_acceptance']in ['pending','PASS']
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
assert not a['unresolved']and not v['unresolved']and not a['parent_verdict_inherited']and not a['cost_based_verdict']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
assert 1<=len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==nt['type']and o['type'].startswith('∀ {n : ℕ} {κ : ℝ}')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[274]==rd('canonical-entry.json')and order[274]['name']==N
cn={x['name']for x in order}
normalize=lambda s:re.sub(r'^_private\.[\w.]+\.0\.','',s)
assert all(x in cn for x in o['project_dependencies'])
assert o['project_dependencies']==[normalize(x)for x in nt['original_project_dependencies']]
assert not any(x.startswith('_private.')for x in o['project_dependencies'])
assert o['project_dependencies']==[]
assert o['generalization']['verified']and 'a b κ : ℝ'in o['generalization']['proposed_type']
assert nt['elided_characters']==[80194]and not nt['full_kernel_printer_body']
m=rd('copy-manifest.json');assert m['declaration']==N and m['recursive'];covered=set()
for e in m['files']:
 pref='.mathlib-quality/overview/evidence/'+N+'/'
 if e['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=report();rel='report.md'
 else:
  assert e['destination'].startswith(pref);rel=e['destination'][len(pref):];p=D/rel
 assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],str(p)
 assert rel not in covered;covered.add(rel)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in excluded and '_validation-layout'not in p.relative_to(D).parts}
if not(D/'report.md').exists():files.add('report.md')
assert files==covered,(files-covered,covered-files)
assert not list(p for p in D.rglob('*.lean')if '_validation-layout'not in p.relative_to(D).parts)
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label']for x in v['accepted']}=={'original','callers','consumers','generic','signed','composition','shape','replacementcaller'}
base=(D/'isolated-prefix.lean.txt').read_text();bi=re.findall(r'^import (.+)$',base,re.M);assert len(bi)==18
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 assert q['executor']['owner']=='root'and q['request']==e['original_execution_request']and q['elapsed_ms']==e['elapsed_ms']
 assert not q['result'].get('isError',False)and z['success']and not z.get('timed_out',False)
 imports=re.findall(r'^import (.+)$',s,re.M)
 if e['format']=='disk':
  assert z['partial']is False and not z['failed_dependencies']
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(imports)==9
 else:
  assert q['request']['code']==s and '#check_failure '+N in s and imports==bi
  assert not any(x.startswith('Roth')for x in imports)
 assert not [x for x in ds(e['receipt'])if x['severity']in ['error','warning']or x.get('category')=='sorry']
 t='\n'.join(x['message']for x in ds(e['receipt'])if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in t and 'PANIC'not in t
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',t)
 if e['axiom_print_required']:assert axs
 for xs in axs:assert {x.strip()for x in xs.split(',')if x.strip()}<=allowed
 assert all(x in t for x in e['required_info']),e['label']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 if 'code'in q['request']:assert q['request']['code']==(D/e['source']).read_text()
 assert not result(e['receipt'])['success']and e['status']=='rejected'
assert len(v['accepted'])==8 and len(v['other_executions'])==2 and v['attempt_accounting']['native_executions']==10
assert 'sorryAx'in messages('composition-receipt.json')
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json');assert len(b)==len(fresh)==17
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']==sha(D/x['archive'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for name in ['original-executed.lean.txt','consumer-scope-executed.lean.txt','consumer-scope2-executed.lean.txt']:
 s=(D/name).read_text();ars=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(ars)==1
 ts=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",ars[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in ts]
 assert actual==expected and len(actual)==len(set(actual))==293
for name in ['original-receipt.json','consumers2-receipt.json']:
 t=messages(name);assert 'DIM275_AUDIT: requested=293; unique=293'in t and 'DIMENSION275_AUDIT_PRESENT: present=293; values=293'in t
c=rd('canonical-consumers.json');assert c['direct_type_consumers']==[]and c['direct_value_consumers']==['Roth.exists_roth_parameters_aux']and len(c['transitive_project_consumers'])==5
assert rd('callers.json')['explicit_caller_count']==1 and rd('callers.json')['external_to_file_count']==0
assert rd('target-metadata.json')['source'].replace('theorem exists_m','theorem replay')in(D/'original-executed.lean.txt').read_text()
fm=rd('formal-search-matrix.json');assert len(fm['cells'])==15 and {(x['form'],x['method'])for x in fm['cells']}=={(f,t)for f in ['current','standard','abstract']for t in ['finder','search','loogle','rg','local']}
for x in fm['cells']:assert(D/x['receipt']).is_file()
for f in ['current','standard','abstract']:
 assert result('formal-'+f+'-local.json')['index']=='error'
 assert not rd('formal-'+f+'-loogle-retry.json')['result']['isError']
p=rd('phase-checks.json');assert len(p['modern9'])==9 and len(p['proofstrategy5'])==5 and len(p['statement_shape3'])==3 and len(p['infrastructure_risks'])==6
lit=rd('literature.json');assert len(lit['general_queries'])>=3 and len({x['q']for x in lit['general_queries']})>=3
assert {'nLab','nCatLab','Stacks','MathOverflow','recent arXiv','local','ask_chatgpt_math'}<={x['channel']for x in lit['channels']}and not lit['third_party_bodies_persisted']
for i in range(1,7):
 z=rd(f'web{i}-receipt.json');assert re.fullmatch('[0-9a-f]{64}',z['response_sha256'])and z['response_bytes']>0 and z['request']and z['response_status']=='returned'
assert any('site:ncatlab.org/ncatlab'in x['q']for x in rd('web5-receipt.json')['request']['search_query'])
assert 'after:2021-10-29 before:2026-10-30'in rd('web6-receipt.json')['request']['search_query'][0]['q']
for link in re.findall(r'\]\(([^)]+)\)',report().read_text()):
 if link.startswith('https://'):continue
 pref='../evidence/'+N+'/';assert link.startswith(pref),link
 assert(D/link[len(pref):]).is_file()or(draft and link[len(pref):]in ['validation-scratch.json','validation-integrated.json','secret-scan.json']),link
for n in ['validation-scratch.json','validation-integrated.json']:
 if(D/n).exists():
  x=rd(n);assert x['result']['exit_code']==0 and 'PASS canonical275'in x['result']['output']
 else:assert draft
if(D/'secret-scan.json').exists():assert rd('secret-scan.json')['result']['exit_code']==0
else:assert draft
print('PASS canonical275 current manifest, all phases, sources17, canonical293, native8, rejected2, links')
