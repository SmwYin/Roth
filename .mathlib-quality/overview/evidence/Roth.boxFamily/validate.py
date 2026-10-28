#!/usr/bin/env python3
"""Read-only canonical233 validator for scratch and integrated current manifests."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.boxFamily'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['raw']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==233 and a['completed']
assert a['allphases']=='PASS'and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='BORDERLINE-needs-human'and a['root_acceptance']in['pending','PASS']
assert not a['unresolved']and not v['unresolved']and 1<=len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']=='{σ : Type u_1} → (σ → ℕ) → ℕ → Set (MvPolynomial σ ℤ)'
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
 r=rd(e['receipt']);z=result(r);assert not r['raw'].get('isError',False)
 assert z['success']and not z.get('timed_out');src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256']and r['request']==e['original_execution_request']
 assert isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s
  ds=z['diagnostics'];assert s.startswith((D/'isolated-prefix21.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==21
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
assert len(v['rejected'])==9 and len(v['warming'])==1
assert result(rd(v['warming'][0]['receipt']))['partial']is True
for e in v['rejected']:
 r=rd(e['receipt']);z=result(r)
 if 'code'in r['request']:assert r['request']['code']==(D/e['source']).read_text()
 assert any(d['severity']in['error','warning']for d in z.get('diagnostics',z.get('items',[])))
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path']for x in fresh}
for x in fresh:
 assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
assert sha(R/'Roth/MainLemma.lean')==sha(D/'source-MainLemma.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0 and'2467 jobs'in(D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[232]==rd('canonical-entry.json')
assert order[232]['name']==N and order[232]['line']==275
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('BOX233_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),('BOX233_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert len(v['canonical_direct_consumers'])==7 and len(v['canonical_direct_type_consumers'])==6
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Box233Original\nopen Roth',1).replace('end Roth','end Box233Original');body=re.sub(r'\bboxFamily\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
body=source[source.index('namespace Roth'):].replace('namespace Roth','namespace Box233Inline\nopen Roth',1).replace('end Roth','end Box233Inline')
start=body.index('/-- Integer polynomials with coordinate degrees');end=body.index('/- The polynomial with coefficient',start);body=body[:start]+body[end:]
body=re.sub(r'\bboxFamily r B\b','({W : MvPolynomial _ ℤ | (∀ j, degreeOf j W ≤ r j) ∧\n      ∀ d, 0 ≤ W.coeff d ∧ W.coeff d ≤ (B : ℤ)})',body)
prefix=(D/'disk-prefix.lean.txt').read_text()+body;lines=[]
for l in prefix.splitlines():
 while len(l)>100:
  pos=l.rfind(' ',0,99);lines.append(l[:pos]);l='      '+l[pos+1:]
 lines.append(l)
inl=(D/'inline-executed.lean.txt').read_text();assert inl.startswith('\n'.join(lines)+'\n')
assert not re.search(r'\bboxFamily\b',inl)
assert inl.count('Lean.Meta.isDefEq old.type new.type')==7
assert '#print axioms main_lemma'in inl and inl.count('#print axioms ')==37
iso=(D/'isolated-executed.lean.txt').read_text();pj=(D/'project-executed.lean.txt').read_text()
for t in['family_eq_image','family_finite','family_ncard','zero_mem','zero_bound','degree_support','restrict_support','infinite_family']:
 assert '#print axioms '+t in iso
assert 'fail_if_success rfl'in iso and 'theorem not_add_closed'in pj
assert 'Finset.coe_Icc, Finsupp.ofSupportFinite_coe'in pj
auth=rd('root-prefix-scope-authorization.json');pp=rd('prefix-provenance.json')
base18=(D/'isolated-prefix.lean.txt').read_text();p21=(D/'isolated-prefix21.lean.txt').read_text()
assert sha(D/'isolated-prefix.lean.txt')==auth['base_prefix_sha256']==pp['base18_sha256']
assert pp['base_shared_unchanged']and len(re.findall(r'^import ',base18,re.M))==18
assert p21==base18+''.join('import '+i+'\n'for i in auth['extra_imports'])
assert sha(D/'isolated-prefix21.lean.txt')==pp['accepted21_sha256']
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['form']==form and f['method']==method
  assert f['request']['query']and not f['raw'].get('isError',False)
  assert 'items'in f['raw']['structuredContent']
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1]and not f['stderr']
rg=rd('source-search.json');gg=rd('tracked-source-search.json');assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['distinct_declarations']==len(cs['callers'])==7
assert cs['external_to_file_files']==cs['external_to_file_declarations']==0
for c in cs['callers']:
 lines=(R/c['file']).read_text().splitlines();assert c['source'].strip()=='\n'.join(lines[c['line']-1:c['end_line']]).strip()
 assert len(re.findall(r'\bboxFamily\b',c['source']))==c['occurrences']
 assert hashlib.sha256(c['source'].encode()).hexdigest()==c['sha256']
for k in['web-general','nlab','ncatlab','stacks','mathoverflow','arxiv','web-api']:
 x=rd(k+'.json');assert x['request']and x['response']['status']=='returned'
 assert re.fullmatch('[a-f0-9]{64}',x['response']['sha256'])and x['response']['bytes']>0
 assert x['summary']and all(l['title'].strip()and l['url'].startswith('https://')for l in x['sources'])
 assert not any('...'in l['url']or re.search(r'(?i)(signature|token|credential)=',l['url'])for l in x['sources'])
assert len({q['q']for q in rd('web-general.json')['request']['search_query']})>=3
api=rd('web-api.json');assert len(api['request']['search_query'])>=1
assert any('mathlib4'in q['q']and 'coefficient'in q['q']for q in api['request']['search_query'])
assert any('mathlib4_docs'in x['url']for x in api['locators'])
assert (D/'root-primary-crosscheck.json').is_file()
assert 'site:ncatlab.org/ncatlab'in rd('ncatlab.json')['request']['search_query'][0]['q']
aq=rd('arxiv.json')['request']['search_query'][0]['q'];assert 'after:2021-10-28'in aq and'before:2026-10-29'in aq
report=D/'report.md'
if not report.exists():report=R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
text=report.read_text();assert all(l==l.rstrip()for l in text.splitlines())
for target in re.findall(r'\]\((\.\./evidence/[^)]+)\)',text):
 suffix=target.split('/'+N+'/',1)[1];assert(D/suffix).is_file(),target
for t in['## Phase 4a —','## Phase 4b —','overview4a web API search','BORDERLINE-needs-human','sufficient, not minimal','all nine rows','all five rows','all15','seven original signatures']:
 assert t in text,t
p=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert p.returncode==0,(p.stdout,p.stderr)
print(json.dumps(dict(status='PASS',declaration=N,current_manifest_files=len(m['files']),fresh_source_pins=17,canonical_exact_order=293,formal_cells=15,actual_callers=7,accepted_native_runs=4,secret_guard='PASS')))
