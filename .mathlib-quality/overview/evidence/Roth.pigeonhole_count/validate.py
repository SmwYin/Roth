#!/usr/bin/env python3
"""Read-only canonical248 validator for scratch or integrated layout. Current manifest governs."""
from pathlib import Path
import json,hashlib,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.pigeonhole_count'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
def report_path():
 for p in[D/'report.md',D.parent.parent/'mathlibable'/(N+'.md'),R/'.mathlib-quality/overview/mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Report unavailable in scratch or integrated layout')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==248
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(x=='PASS'for x in a['phases'].values())and a['root_acceptance']in['pending','PASS']
assert a['verdict']=='BORDERLINE-needs-human'and 0<len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and '∀ {B : ℝ}'in o['type']
assert o['project_dependencies']==['Roth.floor_rpow_count_lt_aux']
assert rd('native-type.json')['printer_elision']is True
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 n='report.md'if'/mathlibable/'in x['destination']else Path(x['destination']).name
 p=report_path()if n=='report.md'else D/n
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 assert x['destination']=='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if n=='report.md'else'evidence/'+N+'/'+n)
 seen.add(n)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and{x['label']for x in v['accepted']}=={'original','isolated','inline'}
def check_run(e,accepted=True):
 r=rd(e['receipt']);s=(D/e['source']).read_text();z=result(r)
 assert isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 assert not r['result'].get('isError',False)
 if e['format']=='disk':
  assert r['request']['file_path'].endswith('/.lake/roth-overview-session/GenWronskianChecks.lean')
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall(r'^import ',s,re.M))==9
  ds=z['items']
 else:
  assert r['request']['code']==s
  assert not re.search(r'^import Roth\b',s,re.M)and '#check_failure '+N in s
  if accepted:assert s.startswith((D/'isolated-prefix.lean.txt').read_text())and len(re.findall(r'^import ',s,re.M))==19
  ds=z['diagnostics']
 if accepted:
  assert z['success']and not z.get('timed_out',False)
  if e['format']=='disk':assert z['partial']is False and not z.get('failed_dependencies')
  assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
  info='\n'.join(x['message']for x in ds if x['line']>=e.get('native_region_start_line',17))
  assert 'sorryAx'not in info
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert axs
  for ax in axs:assert{x.strip()for x in ax.split(',')if x.strip()}<=allowed
  for t in e.get('required_info',[]):assert t in info,(e.get('label'),t)
  assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
  assert max(map(len,s.splitlines()))<=100
 return r,z,ds
for e in v['accepted']:
 assert sha(D/e['source'])==e['source_sha256']and rd(e['receipt'])['request']==e['original_execution_request']
 check_run(e)
for e in v['supplementary_successes']:check_run(e)
assert len(v['rejected'])==1
for e in v['rejected']:
 r,z,ds=check_run(e,False);assert not z['success']and any(x['severity']=='error'for x in ds)
 assert 'Unknown constant `Real.add_rpow_le_rpow_add`'in'\n'.join(x['message']for x in ds)
 assert len(re.findall(r'^import ',(D/e['source']).read_text(),re.M))==18
for e in v['warming']:
 r=rd(e['receipt']);z=result(r);assert z['partial']and not z['success']and z['timed_out']
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
for x in fresh:
 assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
assert sha(R/'Roth/MainLemma.lean')==sha(D/'source-MainLemma.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-local-input.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[247]==rd('canonical-entry.json')
assert order[247]['name']==N and order[247]['line']==334
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
z=result(rd('original-final-receipt.json'));ds=z['items'];info='\n'.join(x['message']for x in ds if x['line']>=17)
assert 'COUNT248_AUDIT: requested=293; unique=293'in info and 'COUNT248_AUDIT_PRESENT: present=293; values=293'in info
assert '26115 characters elided'in info
cs=rd('canonical-consumers.json');assert all(cs[k]==293 for k in['requested','unique','present','values'])
for marker,key in[('COUNT248_DIRECT_CONSUMER: ','direct_value'),('COUNT248_DIRECT_TYPE_CONSUMER: ','direct_type')]:
 assert[x['message'][len(marker):]for x in ds if x['message'].startswith(marker)]==cs[key]
assert cs['direct_value']==['_private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_of_rpow_bound_aux']and not cs['direct_type']
deps=rd('dependencies.json');assert not deps['canonical_type']and deps['canonical_body']==['_private.Roth.MainLemma.0.Roth.floor_rpow_count_lt_aux']
for k in['type','body']:
 raw=next(x['message'].split(': ',1)[1]for x in ds if x['message'].startswith('COUNT248_'+k.upper()+'_CONSTANTS: '))
 assert[x.strip()for x in raw.strip('[]').split(',')]==deps[k]
assert rd('preparation-checks.json')['freeze_time_canonical_recheck']['exit_code']==0
inline=(D/'inline-executed.lean.txt').read_text();assert 'theorem pigeonhole_count'not in inline and inline.count('have countBound')==1
assert v['full_actual_callers']['original_signatures_verified']==1
c=rd('callers.json');assert len(c['callers'])==1 and c['lexical_total_excluding_declaration']==1 and c['external_to_file_uses']==0
assert c['internal_use_count_excluding_declaring_file']==0 and c['total_actual_proof_uses']==1
assert len(rd('formal-search-matrix.json'))==15
for f in['current','standard','abstract']:
 for meth in['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+meth+'.json');assert q['request']and q['result']
for n in['source-search','tracked-source-search','inline-search','full-name-search','literature-local']:
 q=rd(n+'.json');assert q['request']and q['result']['exit_code']in[0,1]
web=[rd('web-'+x+'.json')for x in['general1','general2','general3','nlab','ncatlab','stacks','mathoverflow','arxiv','arxiv-refined','primary','primary-detail']]
for q in web:
 assert q['request']and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])and q['response']['bytes']>0 and q['summary']
 assert 'result'not in q and 'body'not in q['response']
 for x in q['locators']:assert x['title']and x['url'].startswith('https://')and'…'not in x['url']
assert len({web[i]['request']['search_query'][0]['q']for i in range(3)})==3
assert 'site:ncatlab.org/ncatlab 'in web[4]['request']['search_query'][0]['q']
assert all(t in web[7]['request']['search_query'][0]['q']for t in['after:2021-10-29','before:2026-10-30'])
prefix=(D/'isolated-prefix18.lean.txt').read_text();assert sha(D/'isolated-prefix18.lean.txt')==v['controls']['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
assert (D/'isolated-prefix.lean.txt').read_text()==prefix+'import Mathlib.Analysis.MeanInequalitiesPow\n'
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
assert all(x in report for x in['Phase4.5','Phase4.6','Phase5.5','Phase6.0','MAXIMALLY GENERAL','NOT-COMPOSABLE'])
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical248: current manifest, fresh17, exact293, native/callers/15formal/all literature/scratch-or-integrated links')
