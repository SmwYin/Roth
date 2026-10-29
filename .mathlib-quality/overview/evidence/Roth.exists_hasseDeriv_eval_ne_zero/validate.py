#!/usr/bin/env python3
"""Portable read-only254 validator: current copy-manifest is authoritative."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.exists_hasseDeriv_eval_ne_zero'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def res(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==254
assert a['verdict']=='NO-mathlib-has-it'and a['completed']and v['completed']
assert a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}and all(x=='PASS'for x in a['phases'].values())
assert a['root_acceptance']in['pending','PASS']and not a['cost_based_verdict']and not a['parent_verdict_inherited']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and '∀ {σ : Type'in o['type']and '[inst : Fintype σ]'in o['type']
assert rd('native-type.json')['full_original_body']and not rd('native-type.json')['printer_elision']
assert o['project_dependencies']==rd('dependencies.json')['canonical_body']
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
assert {x['label']for x in v['accepted']}=={'original','isolated','project','inline'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=res(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']and q['request']==e['original_execution_request']
 assert isinstance(q['elapsed_ms'],int)and q['elapsed_ms']>=0 and not q['result'].get('isError',False)
 assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall('^import ',s,re.M))==9
  assert q['request']['file_path'].endswith('/.lake/roth-overview-session/GenWronskianChecks.lean')
  assert z['partial']is False and not z.get('failed_dependencies');ds=z['items']
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==18 and not re.search('^import Roth',s,re.M)
  assert '#check_failure '+N in s and '#check_failure MvPolynomial.taylor'in s
  ds=z['diagnostics']
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert not any(x in info for x in ['sorryAx','PANIC','characters elided','LEAN_MCP_MAX_OUTPUT_CHARS'])
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert ax
 for x in ax:assert{y.strip()for y in x.split(',')if y.strip()}<=allowed
 assert all(x in info for x in e['required_info'])
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
assert len(v['rejected'])==3
for e in v['rejected']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=res(e['receipt']);assert not z['success']
 assert any(x['severity']=='error'for x in z.get('items',z.get('diagnostics',[])))
 if 'code'in q['request']:assert q['request']['code']==s
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
for mod in ['MainLemma','Index','Box','Taylor','HasseDeriv']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-local-input.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[253]==rd('canonical-entry.json')and order[253]['name']==N and order[253]['line']==454
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
assert actual==expected and len(actual)==len(set(actual))==293
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
assert c['direct_value']==['_private.Roth.MainLemma.0.Roth.exists_hasseDeriv_index_eval_bound_aux']and not c['direct_type']
ds=res('original-receipt.json')['items'];actual=[x['message'].split(': ',1)[1]for x in ds if x['message'].startswith('WITNESS254_DIRECT_CONSUMER:')];assert actual==c['direct_value']
assert not[x for x in ds if x['message'].startswith('WITNESS254_DIRECT_TYPE_CONSUMER:')]
inline=(D/'inline-executed.lean.txt').read_text().split('end Witness254Inline')[0]
assert 'exists_hasseDeriv_eval_ne_zero'not in inline and 'theorem caller_inline'in inline and 'theorem main_lemma'in inline
assert v['full_actual_callers']['count']==1 and v['full_actual_callers']['original_signatures_verified']==2
c=rd('callers.json');assert len(c['callers'])==1 and c['total_actual_proof_uses']==1 and c['external_to_file_uses']==0 and c['callers'][0]['call_line']==486
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+meth+'.json');assert q['request']and q['result']
assert not rd('search-standard-leanfinder-retry.json')['result'].get('isError',False)
for n in ['source-search','tracked-source-search','inline-search','full-name-search','literature-local']:
 q=rd(n+'.json');assert q['request']and q['result']['exit_code']in[0,1]
labels=['general1','general2','general3','nlab','ncatlab','stacks','mathoverflow','arxiv','primary'];web=[rd('web-'+x+'.json')for x in labels]
for q in web:
 assert q['request']and q['summary']and q['locators']and q['response']['bytes']>0 and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])
 assert 'result'not in q and 'body'not in q['response']
 for x in q['locators']:assert x['title']and x['url'].startswith('https://')and '?'not in x['url']and '…'not in x['url']
assert len({q['request']['search_query'][0]['q']for q in web[:3]})==3
assert 'site:ncatlab.org/ncatlab 'in web[4]['request']['search_query'][0]['q']
assert all(t in web[7]['request']['search_query'][0]['q']for t in ['after:2021-10-29','before:2026-10-30'])
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']and sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
assert all(x in report for x in ['Phase4.5','Phase4.6','Phase5.5','Phase6.0','NOT-COMPOSABLE','NO-mathlib-has-it','Finset.inf_lt_iff','canonical252','all-r'])
assert rd('secret-guard.json')['exit_code']==0
assert rd('preparation-checks.json')['original_preexecution']['source_sha256']==sha(D/'original-executed.lean.txt')
print('PASS canonical254: current manifest; fresh17; exact293; four clean native sources; exact all-r recovery/generalization/boundary controls; full caller+main signatures; all15formal/all literature; portable links')
