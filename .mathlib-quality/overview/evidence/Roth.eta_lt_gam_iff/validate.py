#!/usr/bin/env python3
"""Portable, read-only canonical235 evidence validator; current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.eta_lt_gam_iff'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==235 and a['completed']
assert a['allphases']=='PASS'and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='BORDERLINE-needs-human'and a['root_acceptance']in['pending','PASS']
assert not a['unresolved']and not v['unresolved']and 1<=len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and o['type'].startswith('∀ (δ : ℝ) (n m : ℕ),')
assert o['project_dependencies']==['Roth.gam','Roth.lam']and not rd('native-type.json')['printer_elision']
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
  assert all('#check_failure '+n in s for n in[N,'Roth.eta','Roth.gam','Roth.lam'])
  ds=z['diagnostics'];assert s.startswith((D/'isolated-prefix.lean.txt').read_text())
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
assert len(v['rejected'])==2 and len(v['warming'])==1
assert result(rd(v['warming'][0]['receipt']))['partial']is True
for i,e in enumerate(v['rejected']):
 r=rd(e['receipt']);assert r['request']['code']==(D/e['source']).read_text();z=result(r)
 if i==0:assert not z['success']and any('sorryAx'in d['message']for d in z['diagnostics'])
 else:assert z['success']and any(d['severity']=='warning'for d in z['diagnostics'])
iso=(D/'isolated-executed.lean.txt').read_text();zi=result(rd('isolated-receipt.json'))
for t in ['three_term','three_calls','additive','generic','expanded','weak','false_coefficient','negative_d']:
 assert any("'Gap235Isolated."+t+"' depends on axioms:"in d['message']for d in zi['diagnostics'])
term=iso.split('theorem three_term',1)[1].split('-- Removing',1)[0]
assert all(term.count(n)==1 for n in['lt_sub_iff_add_lt','mul_div_cancel_left₀','div_sub_div_same'])
assert 'grind'not in term and 'simp'not in term and 'ring'not in term
assert iso.count('fail_if_success')==2 and 'exact three_calls _ _ _ (2 : ℝ) two_ne_zero'in iso
assert '[Field K] [LinearOrder K] [IsStrictOrderedRing K]'in iso
pj=(D/'project-executed.lean.txt').read_text();assert 'theorem arbitrary_eta (e δ : ℝ)'in pj and '  ring\n'in pj
assert 'theorem explicit_existing_translation'in pj and 'lt_sub_iff_add_lt.symm'in pj
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path']for x in fresh}
for x in fresh:
 assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in ['MainLemma','Main','LeanEval']:
 assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0 and'2467 jobs'in(D/'baseline-build.txt').read_text()
assert 'roth:eq38'in(D/'local-excerpt.tex.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[234]==rd('canonical-entry.json')
assert order[234]['name']==N and order[234]['line']==100
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('GAP235_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),('GAP235_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['Roth.exists_delta','Roth.roth_of_isIntegral']and not v['canonical_direct_type_consumers']
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Gap235Original\nopen Roth',1).replace('end Roth','end Gap235Original');body=re.sub(r'\beta_lt_gam_iff\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
inl=(D/'inline-executed.lean.txt').read_text();assert 'eta_lt_gam_iff'not in inl.split('end Gap235Inline')[0]
for n in ['exists_delta','roth_of_isIntegral']:
 assert 'example : @Roth.'+n+' = @Gap235Inline.'+n+' := rfl'in inl
 assert '#print axioms Gap235Inline.'+n in inl
assert inl.count('linarith only [h]')==1 and inl.count('linarith only [h30]')==1
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['form']==form and f['method']==method
  assert f['request']['query']and not f['result'].get('isError',False)
  assert 'items'in f['result']['structuredContent']
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1]and not f['stderr']
rg=rd('source-search.json');gg=rd('tracked-source-search.json');assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['executable_occurrences']==cs['distinct_declarations']==2 and cs['external_to_file_files']==1
for c in cs['callers']:
 lines=(R/c['file']).read_text().splitlines();assert c['source'].strip()=='\n'.join(lines[c['line']-1:c['end_line']]).strip()
 assert len(re.findall(r'\beta_lt_gam_iff\b',c['body']))==1
 assert 'eta_lt_gam_iff'not in c['signature']
 assert hashlib.sha256(c['source'].encode()).hexdigest()==c['sha256']
inv=rd('source-inventory.json');assert inv['exit_code']==0
assert {x['file']for x in order}<=(set(inv['stdout'].splitlines())|{'Roth.lean'})
def url_ok(url):
 return url.startswith('https://')and'\\'not in url and not re.search(r'[.,;:!?)}\]]$|[-_=]{3,}',url)and'?'not in url
queries=[]
for name in ['web-general','nlab','ncatlab','stacks','mathoverflow','arxiv','primary']:
 w=rd(name+'.json');assert re.fullmatch('[0-9a-f]{64}',w['raw_response_sha256'])and w['raw_response_bytes']>0
 assert w['status'].startswith('returned')and w['summary']and w['full_web_body_archived']is False
 for url in w['locators']+[x['url']for x in w['titles']]:assert url_ok(url),url
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-28 before:2026-10-29'in q for q in queries)
assert all(x['exit_code']==0 for x in rd('preparation-checks.json')['commands'])
assert all(x['exit_code']==0 and x['source_read_before_native']for x in rd('preparation-checks.json')['observed_pre_execution'])
c=v['composition'];assert c['strict_three_existing_call_term_normalized_verified']and not c['strict_three_existing_call_term_original_verified']
assert not c['new_generic_is_existing_mathlib']and c['normalization_bridge_new_proof']and c['actual_caller_replays']==2
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
assert len(re.findall(r'^\| (current|standard|abstract) \|',s,re.M))==15
assert all(t in s for t in['NOT-COMPOSABLE','no printer-elision marker','three-existing-theorem term','recovered sorryAx','Pairwise duplication audit'])
assert (D/'isolated-prefix.lean.txt').read_bytes()==(R/'.mathlib-quality/overview/evidence/Roth.eta/isolated-prefix.lean.txt').read_bytes()
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS235: all phases; fresh17; exact293; two direct body/zero type consumers; four clean native sets; two actual caller signatures; formal15; currentmanifest/links/URLs/secrets; rejected separation.')
