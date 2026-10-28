#!/usr/bin/env python3
"""Portable read-only canonical231 validation; current copy-manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.eta'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==231 and a['completed']
assert a['allphases']=='PASS'and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='BORDERLINE-needs-human'and a['root_acceptance']in['pending','PASS']
assert not a['unresolved']and not v['unresolved']and 1<=len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']=='ℝ → ℕ → ℝ'
assert o['project_dependencies']==rd('native-type.json')['project_body_dependencies']==[]
assert not rd('native-type.json')['printer_elision']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==4
assert {x['label']for x in v['accepted']}=={'original','isolated','inline','project'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(r);assert not r['result'].get('isError',False)
 assert z['success']and not z.get('timed_out');src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256']and r['request']==e['original_execution_request']
 assert isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and '#check_failure Roth.lam'in s;ds=z['diagnostics']
  assert s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==18
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')and not z.get('failed_dependencies')
  ds=z['items'];assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==9
 assert not[x for x in ds if x.get('severity')in['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']or'LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
assert len(v['rejected'])==len(v['warming'])==1
assert result(rd(v['warming'][0]['receipt']))['partial']is True
for e in v['rejected']:
 r=rd(e['receipt']);assert not result(r)['success']
 assert r['request']['code']==(D/e['source']).read_text()
 assert any('sorryAx'in d['message']for d in result(r)['diagnostics'])
iso=(D/'isolated-executed.lean.txt').read_text();zi=result(rd('isolated-receipt.json'))
assert 'inferInstance : CoeFun ℝ (fun _ : ℝ ↦ ℝ → ℝ)'in iso
assert '#check_failure Real.continuousAt_rpow_const'in iso
assert any('Unknown constant `Real.continuousAt_rpow_const`'in d['message']for d in zi['diagnostics'])
assert not any('expected type contains metavariables'in d['message']for d in zi['diagnostics'])
for t in ['formula','rootIter','direct','rootIter_eq','rootForm','atZero','dimensionZero','negativeGuard','positive','typedBridge']:
 assert any("'Eta231Isolated."+t+"' depends on axioms:"in d['message']for d in zi['diagnostics'])
assert '(hδ : 0 ≤ δ)'in iso and '(hb : 0 < b)'in iso
pj=(D/'project-executed.lean.txt').read_text()
assert 'Continuous (fun δ ↦ formula C b δ m)'in pj and '(hb : 0 ≤ b)'in pj
assert 'Real.rpow_def_of_neg hδ'in pj and 'Roth.eta (-1) 0 = -1'in pj
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path']for x in fresh}
for x in fresh:
 assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in ['MainLemma','Main','Theta']:
 assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0 and'2467 jobs'in(D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[230]==rd('canonical-entry.json')
assert order[230]['name']==N and order[230]['line']==66
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('ETA231_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),('ETA231_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
 assert len(ns)==8
assert 'Roth.roth_of_isIntegral'in v['canonical_direct_consumers']and'Roth.roth_of_isIntegral'not in v['canonical_direct_type_consumers']
assert 'Roth.eta_lt_gam_iff'in v['canonical_direct_type_consumers']and'Roth.eta_lt_gam_iff'not in v['canonical_direct_consumers']
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Eta231Original\nopen Roth',1).replace('end Roth','end Eta231Original');body=re.sub(r'\beta\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
def transform(s,ns):
 b=s[s.index('namespace Roth'):].replace('namespace Roth','namespace '+ns+'\nopen Roth',1).replace('end Roth','end '+ns)
 if ns=='Eta231Inline':
  b=b.replace('/-- The parameter `η = 10^m δ^{(1/2)^m}`. Source: §6, eq. (36). -/\n','')
  b=b.replace('noncomputable def eta (δ : ℝ) (m : ℕ) : ℝ := 10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)','')
 b=b.replace('eta δ m','(10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m))')
 b=b.replace('[eta, ','[').replace('[eta]','[]').replace(', eta,',',')
 if ns=='Eta231MainInline':
  for n in ['exists_delta_bound','eta_lt_gam_iff','main_lemma']:b=re.sub(r'\b'+n+r'\b','Eta231Inline.'+n,b)
 assert not re.search(r'\beta\b',b)
 return b
prefix=(D/'disk-prefix.lean.txt').read_text()+transform(source,'Eta231Inline')+'\n'+transform((D/'source-Main.lean.txt').read_text(),'Eta231MainInline')+'\n'
lines=[]
for l in prefix.splitlines():
 while len(l)>100:
  pos=l.rfind(' ',0,99);lines.append(l[:pos]);l='      '+l[pos+1:]
 lines.append(l)
inl=(D/'inline-executed.lean.txt').read_text();assert inl.startswith('\n'.join(lines)+'\n')
assert not re.search(r'\beta\b',inl)
assert inl.count('Lean.Meta.isDefEq old.type new.type')==4
for n in ['exists_delta_bound','eta_lt_gam_iff','main_lemma']:
 assert 'example : @Roth.'+n+' = @Eta231Inline.'+n+' := rfl'in inl
assert 'example : @Roth.exists_delta = @Eta231MainInline.exists_delta := rfl'in inl
assert '#print axioms roth_of_isIntegral'in inl
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['form']==form and f['method']==method
  assert f['request']['query']and not f['result'].get('isError',False)
  assert 'items'in f['result']['structuredContent']
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1]and not f['stderr']
rg=rd('source-search.json');gg=rd('tracked-source-search.json');assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['executable_occurrences']==18 and cs['distinct_declarations']==8
assert len(cs['callers'])==8 and cs['external_to_file_declarations']==3 and cs['external_to_file_files']==1
assert sum(c['signature_occurrences']for c in cs['callers'])==11
for c in cs['callers']:
 lines=(R/c['file']).read_text().splitlines();assert c['source'].strip()=='\n'.join(lines[c['line']-1:c['end_line']]).strip()
 assert len(re.findall(r'\beta\b',c['source']))==c['occurrences']
 assert hashlib.sha256(c['source'].encode()).hexdigest()==c['sha256']
inv=rd('source-inventory.json');assert inv['exit_code']==0
assert {x['file']for x in order}<=(set(inv['stdout'].splitlines())|{'Roth.lean'})
def url_ok(url):
 return bool(url.startswith('https://')and'\\'not in url and not re.search(r'[.,;:!?)}\]]$|[-_=]{3,}',url)and not re.search(r'[?&](?:X-Amz[^=]*|token|signature|credential|sig)=',url,re.I))
assert url_ok('https://arxiv.org/html/2502.00731v2')
for suffix in ['\\bad','.',',',';',':','!','?',')',']','}','-----','___','===']:
 assert not url_ok('https://example.org/path'+suffix)
queries=[]
for name in ['web-general','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-locators','web-api']:
 w=rd(name+'.json');assert re.fullmatch('[0-9a-f]{64}',w['raw_response_sha256'])and w['raw_response_bytes']>0
 assert w['status']=='returned'and w['summary']and w['full_web_body_archived']is False
 assert w['locators']
 for url in w['locators']+[x['url']for x in w['titles']]:assert url_ok(url),url
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-28 before:2026-10-29'in q for q in queries)
assert all(x['exit_code']==0 for x in rd('preparation-checks.json')['commands'])
c=v['composition'];assert not c['strict_three_existing_call_term_verified']
assert c['direct_arithmetic_construction_verified']and c['actual_caller_replays']==8 and c['actual_caller_occurrences']==18
assert not c['new_generic_profile_is_existing_mathlib']and not c['new_root_iteration_proof_is_existing_mathlib']
assert c['original_signatures_retained_by_defeq']and not c['imported_transitive_target_freedom_claimed']
p=D/'report.md'
if not p.exists():p=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=p.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
assert len(re.findall(r'^\| [1-9] \|',s.split('## Phase 4c')[1].split('## Phase 4.5')[0],re.M))==9
assert len(re.findall(r'^\| [1-5] \|',s.split('## Phase 4.6')[1].split('## Phase 5 ')[0],re.M))==5
assert len(re.findall(r'^\| (?:Typeclass|Reducibility|Noncanonical|Instance priority|Universe|Coercion)',s.split('## Phase 4.5')[1].split('## Phase 4.6')[0],re.M))==6
assert all(t in s for t in['NOT-COMPOSABLE','no printer-elision marker','All eight original signatures','negative-base','recovered sorryAx'])
assert 'REJECTED'in rd('import-preflight.json')['status']
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS231: all phases; fresh17; exact293;8type/8value; four clean native sets;18tokens/eightcaller signatures;formal15; currentmanifest/links/URLs/secrets; rejected separation.')
