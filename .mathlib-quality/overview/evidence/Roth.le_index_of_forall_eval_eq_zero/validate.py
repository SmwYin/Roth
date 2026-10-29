#!/usr/bin/env python3
"""Read-only canonical252 validator: scratch/integrated layouts, current manifest only."""
from pathlib import Path
import json,hashlib,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.le_index_of_forall_eval_eq_zero'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==252
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())and a['root_acceptance']in['pending','PASS']
assert a['verdict']=='BORDERLINE-needs-human'and 0<len(a['questions'])<=5
assert not a['cost_based_verdict']and not a['parent_verdict_inherited']
keys={'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}
assert keys<=set(o)and all(o[k]or o[k]==[]for k in keys)
assert o['type']==rd('native-type.json')['type']and '∀ {σ : Type'in o['type']and '[inst : Fintype σ]'in o['type']
assert o['project_dependencies']==rd('dependencies.json')['canonical_body']
assert rd('native-type.json')['printer_elision']is False and rd('native-type.json')['full_original_body']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 n='report.md'if'/mathlibable/'in x['destination']else Path(x['destination']).name
 p=report_path()if n=='report.md'else D/n
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 assert x['destination']=='.mathlib-quality/overview/'+('mathlibable/'+N+'.md'if n=='report.md'else'evidence/'+N+'/'+n)
 assert n not in seen,n
 seen.add(n)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label']for x in v['accepted']}=={'original','isolated','project','inline','controls','reaim','reaim-project','positive'}
def check_run(e,accepted=True):
 raw=rd(e['receipt']);s=(D/e['source']).read_text();z=result(e['receipt'])
 assert isinstance(raw['elapsed_ms'],int)and raw['elapsed_ms']>=0 and not raw['result'].get('isError',False)
 if e['format']=='disk':
  assert raw['request']['file_path'].endswith('/.lake/roth-overview-session/GenWronskianChecks.lean')
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall(r'^import ',s,re.M))==9
  ds=z['items']
 else:
  assert raw['request']['code']==s
  assert s.startswith((D/'isolated-prefix.lean.txt').read_text())and len(re.findall(r'^import ',s,re.M))==18
  assert not re.search(r'^import Roth\b',s,re.M)and '#check_failure '+N in s
  ds=z['diagnostics']
 if accepted:
  assert z['success']and not z.get('timed_out',False)
  if e['format']=='disk':assert z['partial']is False and not z.get('failed_dependencies')
  assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
  info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
  assert 'sorryAx'not in info and not re.search(r'characters elided|LEAN_MCP_MAX_OUTPUT_CHARS',info)
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert axs
  for ax in axs:assert{x.strip()for x in ax.split(',')if x.strip()}<=allowed
  for t in e.get('required_info',[]):assert t in info,(e['label'],t)
  assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
  assert max(map(len,s.splitlines()))<=100
 return raw,z,ds
for e in v['accepted']:
 assert sha(D/e['source'])==e['source_sha256']and rd(e['receipt'])['request']==e['original_execution_request']
 check_run(e)
for e in v['rejected']:
 raw,z,ds=check_run(e,False);assert not z['success']and any(x['severity']=='error'for x in ds)
assert len(v['rejected'])==1 and len(v['warming'])==1
warm=result(v['warming'][0]['receipt']);assert warm['partial']is True and not warm['success']
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
for x in fresh:
 assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in ['MainLemma','Index','Box','Taylor','HasseDeriv']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-local-input.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293 and order[251]==rd('canonical-entry.json')
assert order[251]['name']==N and order[251]['line']==419
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
z=result('original-receipt.json');ds=z['items'];info='\n'.join(x['message']for x in ds if x['line']>=17)
assert 'CUTOFF252_AUDIT: requested=293; unique=293'in info and 'CUTOFF252_AUDIT_PRESENT: present=293; values=293'in info
cs=rd('canonical-consumers.json');assert all(cs[k]==293 for k in ['requested','unique','present','values'])
for marker,key in [('CUTOFF252_DIRECT_CONSUMER: ','direct_value'),('CUTOFF252_DIRECT_TYPE_CONSUMER: ','direct_type')]:
 assert[x['message'][len(marker):]for x in ds if x['message'].startswith(marker)]==cs[key]
assert cs['direct_value']==['_private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_aux']and not cs['direct_type']
deps=rd('dependencies.json');assert deps['canonical_type']==['Roth.weight','MvPolynomial.hasseDeriv','Roth.index']
assert deps['canonical_body']==['Roth.weight','MvPolynomial.hasseDeriv','Roth.index','Roth.le_index_iff','MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt']
for k in ['type','body']:
 raw=next(x['message'].split(': ',1)[1]for x in result('project-receipt.json')['items']if x['message'].startswith('CUTOFF252_'+k.upper()+'_CONSTANTS: '))
 assert[x.strip()for x in raw.strip('[]').split(',')]==deps[k]
assert rd('preparation-checks.json')['freeze_time_canonical_recheck']['exit_code']==0
assert rd('preparation-checks.json')['original_preexecution']['source_sha256']==sha(D/'original-executed.lean.txt')
inline=(D/'inline-executed.lean.txt').read_text();assert N not in inline.split('end Cutoff252Inline')[0]and 'theorem le_index_of_forall_eval_eq_zero'not in inline
assert v['full_actual_callers']['original_signatures_verified']==1
c=rd('callers.json');assert len(c['callers'])==1 and c['lexical_total_excluding_declaration']==1 and c['external_to_file_uses']==0
assert c['internal_use_count_excluding_declaring_file']==0 and c['total_actual_proof_uses']==1 and c['callers'][0]['call_line']==562
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+meth+'.json');assert q['request']and q['result']
assert not rd('search-abstract-loogle-retry.json')['result']['isError']
for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
 q=rd('search-reaim-'+meth+'.json');assert q['request']and q['result']
for n in ['source-search','tracked-source-search','inline-search','full-name-search','literature-local']:
 q=rd(n+'.json');assert q['request']and q['result']['exit_code']in [0,1]
labels=['general1','general2','general3','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-detail'];web=[rd('web-'+x+'.json')for x in labels]
for q in web:
 assert q['request']and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])and q['response']['bytes']>0 and q['summary']
 assert 'result'not in q and 'body'not in q['response']and q['locators']
 for x in q['locators']:assert x['title']and len(x['title'])<160 and x['url'].startswith('https://')and '…'not in x['url']and '?'not in x['url']
assert len({web[i]['request']['search_query'][0]['q']for i in range(3)})==3
assert 'site:ncatlab.org/ncatlab 'in web[4]['request']['search_query'][0]['q']
assert all(t in web[7]['request']['search_query'][0]['q']for t in ['after:2021-10-29','before:2026-10-30'])
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
assert all(x in report for x in ['Phase4.5','Phase4.6','Phase5.5','Phase6.0','NOT-COMPOSABLE','BORDERLINE-needs-human','positive-cutoff','Finset.le_inf_iff'])
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical252: current manifest, fresh17, exact293, eight clean native sources, exact recoveries, positive/zero/degree guards, full caller, all15formal+reaim/all literature; portable links')
