#!/usr/bin/env python3
"""Read-only canonical253 package validator, scratch or integrated; CURRENT manifest only."""
from pathlib import Path
import json,hashlib,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==253
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())and a['root_acceptance']in ['pending','PASS']
assert a['verdict']=='BORDERLINE-needs-human'and 0<len(a['questions'])<=5
assert not a['cost_based_verdict']and not a['parent_verdict_inherited']
keys={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert keys<=set(o)and all(o[k]or o[k]==[]for k in keys)
assert o['type']==rd('native-type.json')['type']and '∀ {K : Type'in o['type']and '[inst : Semifield K]'in o['type']
assert not o['project_dependencies']and not rd('dependencies.json')['canonical_type']and not rd('dependencies.json')['canonical_body']
assert rd('native-type.json')['printer_elision']and not rd('native-type.json')['full_kernel_body_dump']
seen=set();m=rd('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 n='report.md'if'/mathlibable/'in x['destination']else Path(x['destination']).name
 p=report_path()if n=='report.md'else D/n
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 expected='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if n=='report.md'else'evidence/'+N+'/'+n)
 assert x['destination']==expected and n not in seen;n and seen.add(n)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label']for x in v['accepted']}=={'original','isolated','controls','comparison'}
for e in v['accepted']:
 s=(D/e['source']).read_text();raw=rd(e['receipt']);z=result(e['receipt'])
 assert isinstance(raw['elapsed_ms'],int)and raw['elapsed_ms']>=0 and not raw['result'].get('isError',False)
 assert raw['request']==e['original_execution_request']and sha(D/e['source'])==e['source_sha256']
 assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert raw['request']['file_path'].endswith('/.lake/roth-overview-session/GenWronskianChecks.lean')
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall(r'^import ',s,re.M))==9
  assert z['partial']is False and not z.get('failed_dependencies');ds=z['items']
 else:
  assert raw['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==18 and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 assert not[x for x in ds if x['severity']in ['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info
 if e['label']!='original':assert not re.search('characters elided|LEAN_MCP_MAX_OUTPUT_CHARS',info)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert axs
 for ax in axs:assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 for marker in e['required_info']:assert marker in info,(e['label'],marker)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
assert len(v['rejected'])==1
for e in v['rejected']:
 z=result(e['receipt']);s=(D/e['source']).read_text();assert rd(e['receipt'])['request']['code']==s
 assert z['success']and any(x['severity']=='warning'and 'unused'in x['message']for x in z['diagnostics'])
 assert not any(x['severity']=='error'or x.get('category')=='sorry'for x in z['diagnostics'])
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and {x['path']for x in fresh}==set(b)
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert sha(R/'Roth/MainLemma.lean')==sha(D/'source-MainLemma.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-local-input.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[252]==rd('canonical-entry.json')and order[252]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
cs=rd('canonical-consumers.json');assert all(cs[k]==293 for k in ['requested','unique','present','values'])
ds=result('original-receipt.json')['items'];info='\n'.join(x['message']for x in ds if x['line']>=17)
assert 'BUDGET253_AUDIT: requested=293; unique=293'in info and 'BUDGET253_AUDIT_PRESENT: present=293; values=293'in info
for marker,key in [('BUDGET253_DIRECT_CONSUMER: ','direct_value'),('BUDGET253_DIRECT_TYPE_CONSUMER: ','direct_type')]:
 assert [x['message'][len(marker):]for x in ds if x['message'].startswith(marker)]==cs[key]==[]
assert rd('preparation-checks.json')['result']['exit_code']==0 and rd('preparation-checks.json')['source_sha256']==sha(D/'original-executed.lean.txt')
c=rd('callers.json');assert not c['callers']and all(c[k]==0 for k in ['lexical_total_excluding_declaration','external_to_file_uses','internal_use_count_excluding_declaring_file','total_actual_proof_uses'])
assert v['full_actual_callers']['count']==0 and rd('inline-audit.json')['not_claimed_actual_caller']
assert rd('inline-audit.json')['original_main_signature_identical']
for n in ['source-search','tracked-source-search']:
 q=rd(n+'.json');assert q['result']['exit_code']==0 and len(q['result']['stdout'].splitlines())==1 and ':433:'in q['result']['stdout']
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+meth+'.json');assert q['request']and q['result']
assert rd('full-name-search.json')['result']['exit_code']==1 and not rd('full-name-search.json')['result']['stdout']
for n in ['inline-search','literature-local']:assert rd(n+'.json')['request']and rd(n+'.json')['result']['exit_code']in [0,1]
labels=['general1','general2','general3','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-detail'];web=[rd('web-'+x+'.json')for x in labels]
for q in web:
 assert q['request']and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])and q['response']['bytes']>0 and q['summary']
 assert 'result'not in q and 'body'not in q['response']and q['locators']
 for x in q['locators']:assert x['title']and len(x['title'])<160 and x['url'].startswith('https://')and '…'not in x['url']and '?'not in x['url']
assert len({web[i]['request']['search_query'][0]['q']for i in range(3)})==3
assert 'site:ncatlab.org/ncatlab 'in web[4]['request']['search_query'][0]['q']
assert all(t in web[7]['request']['search_query'][0]['q']for t in ['after:2021-10-29','before:2026-10-30'])
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']and sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert (D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
assert all(x in report for x in ['Phase4.5','Phase4.6','Phase5.5','Phase6.0','NOT-COMPOSABLE','BORDERLINE-needs-human','weak','Callers table: **none**','elided'])
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical253: CURRENT manifest, fresh17, exact293, four clean native sources, exact recovery, boundary guards, no-caller scope, all15formal and named literature, portable links')
