#!/usr/bin/env python3
"""Read-only portable canonical238 validator; current manifest is authoritative."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.four_lt_rpow'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==238 and a['completed']
assert a['allphases']=='PASS' and set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(x=='PASS'for x in a['phases'].values())
assert a['root_acceptance']in['pending','PASS'] and not a['unresolved'] and not v['unresolved']
assert a['verdict']=='BORDERLINE-needs-human' and 0<len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type'] and o['project_dependencies']==[]
assert rd('native-type.json')['printer_elision'] is True
m=rd('copy-manifest.json');assert m['declaration']==N
seen=set()
for x in m['files']:
 name='report.md'if'/mathlibable/'in x['destination']else Path(x['destination']).name
 p=D/name
 if not p.exists():p=R/x['destination']
 assert p.is_file() and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 seen.add(name)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed
assert {x['label']for x in v['accepted']}=={'original','isolated','inline','boundary'}
for e in v['accepted']:
 r=rd(e['receipt']);s=(D/e['source']).read_text()
 assert sha(D/e['source'])==e['source_sha256']
 assert r['request']==e['original_execution_request']and isinstance(r['elapsed_ms'],int)
 assert not r['result'].get('isError',False)
 z=result(r);assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert z['partial']is False and not z.get('failed_dependencies')
  assert r['request']=={'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean'}
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==9
  ds=z['items']
 else:
  assert r['request']['code']==s
  assert s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==18
  assert not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s
  ds=z['diagnostics']
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info
 if e['label']=='original':assert 'characters elided'in info
 else:assert 'characters elided'not in info
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',info):
  assert{x.strip()for x in ax.split(',')if x.strip()}<=allowed
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
assert len(v['rejected'])==3
for e in v['rejected']:
 r=rd(e['receipt']);s=(D/e['source']).read_text();assert r['request']['code']==s
 if r['result'].get('isError'):
  assert 'timed out'in str(r['result'])and 'timeout'in e['reason'].lower()
 else:
  z=result(r);assert not z['success']and any(x['severity']=='error'for x in z['diagnostics'])
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and{x['path']for x in fresh}==set(base)
for x in fresh:
 assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in['MainLemma','Main']:
 assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 assert sha(R/'.lake/packages/mathlib'/x['path'])==x['sha256']==sha(D/x['archive'])
local=rd('literature-local-input.json');assert sha(R/local['path'])==local['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[237]==rd('canonical-entry.json')
assert order[237]['name']==N and order[237]['line']==122
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
z=result(rd('original-receipt.json'));ds=z['items'];info='\n'.join(x['message']for x in ds)
assert 'FOUR238_AUDIT: requested=293; unique=293'in info
assert 'FOUR238_AUDIT_PRESENT: present=293; values=293'in info
assert 'FOUR238_SIGNATURE_IDENTICAL'in info
cs=rd('canonical-consumers.json');assert all(cs[k]==293 for k in['requested','unique','present','values'])
for marker,key in[('FOUR238_DIRECT_CONSUMER: ','direct_value'),('FOUR238_DIRECT_TYPE_CONSUMER: ','direct_type')]:
 assert[x['message'][len(marker):]for x in ds if x['message'].startswith(marker)]==cs[key]
assert len(cs['direct_value'])==2 and not cs['direct_type']
assert rd('preparation-checks.json')['freeze_time_canonical_recheck']['exit_code']==0
inline=(D/'inline-executed.lean.txt').read_text()
assert 'theorem four_lt_rpow'not in inline and inline.count('have numericalBound')==2
assert len([x for x in result(rd('inline-receipt.json'))['items']if x['message'].startswith('FOUR238_INLINE_SIGNATURE_IDENTICAL: ')])==6
for f in['source-search.json','tracked-source-search.json']:
 x=rd(f)['result'];assert x['exit_code']==0
 assert len([ln for ln in x['stdout'].splitlines()if'theorem four_lt_rpow'not in ln])==2
cells=rd('formal-search-matrix.json');assert len(cells)==15
assert{(x['form'],x['method'])for x in cells}=={(f,m)for f in['current','standard','abstract']for m in['leanfinder','loogle','leansearch','rg','local_search']}
for x in cells:
 z=rd(x['receipt']);assert z['request']and z['result']
 if x['method']=='rg':assert z['result']['exit_code']in[0,1]
 else:assert not z['result'].get('isError',False)
for f in['general','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','diophantine']:
 z=rd('web-'+f+'.json');assert z['request']and z['status']and z['summary']
 assert re.fullmatch('[0-9a-f]{64}',z['response_sha256'])and z['response_bytes']>0
 for h in z['hits']:assert h['title']and h['url'].startswith('http')and'?'not in h['url']and'...'not in h['url']
assert len(rd('web-general.json')['request']['search_query'])>=3
assert 'site:ncatlab.org/ncatlab'in rd('web-ncatlab.json')['request']['search_query'][0]['q']
for q in rd('web-diophantine.json')['request']['search_query']:
 assert'after:2021-10-28'in q['q']and'before:2026-10-29'in q['q']
report_path=D/'report.md'
if not report_path.exists():report_path=R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
report=report_path.read_text()
for dest in re.findall(r'\]\(([^)]+)\)',report):
 if dest.startswith('http'):continue
 prefix='../evidence/'+N+'/'
 assert dest.startswith(prefix),dest
 name=dest[len(prefix):];assert (D/name).is_file(),name
assert rd('secret-guard.json')['result']['exit_code']==0
print('PASS canonical238: phases, exact293, four clean native batches, 15 searches, current manifest, links, inputs, secrets')
