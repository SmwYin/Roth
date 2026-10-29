#!/usr/bin/env python3
"""Portable read-only canonical266 validator; current manifest is authoritative."""
from pathlib import Path
import json,sys,re,hashlib
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.main_lemma'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 q=rd(n)['result']['structuredContent'];return q.get('result',q)
def report_path():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('Missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==266
assert a['completed']and v['completed']and a['allphases']=='PASS'and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in['pending','PASS']and a['verdict']=='YES-add-as-is'
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'for x in a['phases'].values())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and'∃ (Q : MvPolynomial (Fin m) ℤ)'in o['type']
assert rd('native-type.json')['full_type']and rd('native-type.json')['full_written_source_body']
assert rd('native-type.json')['printer_elision']and not rd('native-type.json')['full_kernel_printer_body']
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
assert {x['label']for x in v['accepted']}=={'original','project','inline','isolated','representation'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']and q['request']==e['original_execution_request']
 assert isinstance(q['elapsed_ms'],int)and q['elapsed_ms']>=0 and not q['result'].get('isError',False)
 assert z['success']and not z.get('timed_out',False)
 if e['format']=='disk':
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())and len(re.findall('^import ',s,re.M))==9
  assert q['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
  assert z['partial']is False and not z.get('failed_dependencies');ds=z['items']
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix19.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==19 and not re.search('^import Roth',s,re.M)
  assert '#check_failure '+N in s and '#check_failure MvPolynomial.taylor'in s
  ds=z['diagnostics']
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
 info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info and'PANIC'not in info
 if e['label']!='original':assert'LEAN_MCP_MAX_OUTPUT_CHARS'not in info
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert ax
 for x in ax:assert{y.strip()for y in x.split(',')if y.strip()}<=allowed
 assert all(x in info for x in e['required_info'])
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
assert len(v['rejected'])==5
for e in v['rejected']:
 q=rd(e['receipt']);z=result(e['receipt']);s=(D/e['source']).read_text()
 assert not z['success']or any(x['severity']=='warning'for x in z.get('items',z.get('diagnostics',[])))
 assert any(x['severity']in['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 if'code'in q['request']:assert q['request']['code']==s
assert result('original-warming-receipt.json')['partial']is True
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17 and{x['path']for x in fresh}==set(b)
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:assert x['match']and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['MainLemma','Main','LeanEval','Box','Index','Taylor','HasseDeriv']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])and p.stat().st_size==x['bytes']
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293
assert order[265]==rd('canonical-entry.json')and order[265]['name']==N and order[265]['line']==735

# Canonical dependency fields must contain canonical tracked names, including private names.
lookup={((('_private.'+x['file'][:-5].replace('/','.')+'.0.')if x['visibility']=='private'else'')+x['name']):x['name']for x in order}
canonical={x['name']for x in order};dep=rd('dependencies.json')
rawds=result('original-receipt.json')['items']
for k in ['body','type']:
 message=next(x['message']for x in rawds if x['message'].startswith('MAIN266_'+k.upper()+'_CONSTANTS:'))
 raw=[n for n in lookup if re.search(r'(?<![\w.])'+re.escape(n)+r'(?![\w.])',message)]
 assert dep['raw_kernel_'+k]==raw and dep['raw_kernel_'+k+'_constants_message']==message
 assert dep['canonical_'+k]==[lookup[n]for n in raw]
 assert len(dep['canonical_'+k])==len(set(dep['canonical_'+k]))
 assert set(dep['canonical_'+k])<=canonical
 assert not any(n.startswith('_private.')for n in dep['canonical_'+k])
assert set(o['project_dependencies'])<=canonical and o['project_dependencies']==dep['canonical_body']

# Independently cross-check the project subset against the nonelided filtered native row.
edge=next(x for x in dep['transitive_project_edges']if x.startswith('MAIN266_PROJECT_BODY_EDGE: Roth.main_lemma ->'))
assert 'LEAN_MCP_MAX_OUTPUT_CHARS'not in edge and 'elided'not in edge
edge_names=[n for n in lookup if re.search(r'(?<![\w.])'+re.escape(n)+r'(?![\w.])',edge.split(' -> ',1)[1])]
assert set(dep['raw_kernel_body'])==set(edge_names)|{'MvPolynomial.hasseDeriv'}
elision=dep['raw_kernel_body_constants_elision']
assert elision['present']and elision['elided_characters']==128
assert elision['nonelided_target_project_edge']==edge
assert'128 characters elided'in dep['raw_kernel_body_constants_message']

correction=rd('documentary-correction.json')
for n,h in correction['native_artifact_hashes'].items():assert sha(D/n)==h

expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
assert actual==expected and len(actual)==len(set(actual))==293
c=rd('canonical-consumers.json');assert all(c[k]==293 for k in ['requested','unique','present','values'])
assert c['direct_value']==['_private.Roth.Main.0.Roth.one_lt_roth_eval_bound_aux']and not c['direct_type']
ds=result('original-receipt.json')['items'];actual=[x['message'].split(': ',1)[1]for x in ds if x['message'].startswith('MAIN266_DIRECT_CONSUMER:')];assert actual==c['direct_value']
assert not[x for x in ds if x['message'].startswith('MAIN266_DIRECT_TYPE_CONSUMER:')]
for marker in ['MAIN266_AUDIT: requested=293; unique=293','MAIN266_AUDIT_PRESENT: present=293; values=293']:assert any(marker==x['message']for x in ds)
orig=(R/'Roth/MainLemma.lean').read_text();body=orig[orig.index('namespace Roth'):].replace('namespace Roth','namespace Main266Original\nopen Roth',1).replace('end Roth','end Main266Original');body=re.sub(r'\bmain_lemma\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
inline=(D/'inline-executed.lean.txt').read_text();assert' main_lemma hf'not in inline and'index_le_Θ hW hcop'in inline
assert v['full_actual_callers']['count']==1 and v['full_actual_callers']['original_signatures_verified']==2
assert rd('callers.json')['callers'][0]['call_line']==466
p=(D/'project-executed.lean.txt').read_text();assert'theorem numerical_envelope'in p and'theorem old_recovery'in p
assert'@Roth.main_lemma = @old_recovery'in p and'exact main_lemma'not in p
assert 'B : ℕ'in p and'hΘ : Θ X q r < E'in p and'(hpow : (B : ℝ) * β ^ 3 ≤ (B : ℝ) ^ c)'in p
iso=(D/'isolated-executed.lean.txt').read_text();assert'clear witness\n    exact?'in iso and'exact witness'in iso
rep=(D/'representation-executed.lean.txt').read_text();assert'theorem goal_eq'in rep and'MvPolynomial.coeff_taylor x i P'in rep
assert len(rd('formal-search-matrix.json'))==15
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd('search-'+f+'-'+meth+'.json');assert q['request']and q['result']
assert not rd('search-abstract-leanfinder-retry.json')['result'].get('isError',False)
for f in ['current','standard','abstract']:assert rd('search-'+f+'-rg.json')['result']['exit_code']in[0,1]
web=[rd('web-'+x+'.json')for x in ['general','channels','recent','more','primary']]
for q in web:
 assert q['request']and q['summary']and q['locators']and q['response']['bytes']>0 and re.fullmatch('[0-9a-f]{64}',q['response']['sha256'])
 assert'result'not in q and'body'not in q['response']
 for x in q['locators']:assert x['title']and x['url'].startswith('https://')and'?'not in x['url']and'…'not in x['url']
assert len({x['q']for x in web[0]['request']['search_query']})==3
assert any('site:ncatlab.org/ncatlab 'in x['q']for q in web for x in q['request'].get('search_query',[]))
assert any(all(t in x['q']for t in ['after:2021-10-29','before:2026-10-30'])for q in web for x in q['request'].get('search_query',[]))
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']
shared=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')
if shared.is_file():assert sha(shared)==v['controls']['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
assert (D/'isolated-prefix19.lean.txt').read_text()==(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.NumberTheory.SiegelsLemma\n'
assert rd('root-prefix-scope-authorization.json')['authorized_by']=='root'
progress=rd('accepted-verdict-snapshot.json');accepted={x['declaration']:x for x in progress['completed_declarations']}
for g in rd('accepted-grouping.json')['groups']:
 for n in g['declarations']:assert accepted[n]['verdict'].startswith('YES')and accepted[n]['acceptance']=='PASS'
assert'f9314f86ef3bdc9c59ce1ab0e5c014f69a834429'in rd('reviewer-commits.json')['result']['stdout']
build=rd('file-end-build.json');assert build['command']=='lake build'and build['argv']==['lake','build']and build['exit_code']==0
assert build['elapsed_ms']>0 and build['full_actual_log']and build['log_sha256']==sha(D/build['log'])and build['log_bytes']==(D/build['log']).stat().st_size
assert (D/build['log']).read_text()=='Build completed successfully (2467 jobs).\n'
report=report_path().read_text()
for href in re.findall(r'\]\(([^)]+)\)',report):
 if href.startswith('../evidence/'+N+'/'):assert(D/href.split('/')[-1]).is_file(),href
 elif not href.startswith('https://'):raise AssertionError(href)
for s in ['Phase4.5','Phase4.6','Phase5.5','Phase6.0','NOT-COMPOSABLE','YES-add-as-is','diagnostic witness pass-through','does **not** itself assert γ−η>0','not** a full kernel-body dump','private budget layer','Mathlib/NumberTheory/DiophantineApproximation/Roth.lean']:assert s in report,s
assert rd('secret-guard.json')['exit_code']==0
assert rd('preparation-checks.json')['original_preexecution']['source_sha256']==sha(D/'original-executed.lean.txt')
assert all(not x['native_queried_after_failure']for x in rd('preparation-checks.json')['width_preparation_failures'])
print('PASS canonical266: currentmanifest; fresh17; exact293; five clean native sources; full actual caller signatures; semantic envelope/exact recovery; equivalent isolated goal;19 authorized imports;15formal/all named literature; actual file-end lake build; portable links')
