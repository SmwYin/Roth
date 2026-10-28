#!/usr/bin/env python3
"""Portable read-only234 assessment gate: validate current, not historical, manifest."""
from pathlib import Path
import json,hashlib,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.exists_delta_bound'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['raw']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==234 and a['completed']and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS')and a['root_acceptance']in['pending','PASS']
assert a['verdict']=='BORDERLINE-needs-human'and 1<=len(a['questions'])<=5
assert a['unresolved']==v['unresolved']==[]and not a['production_changed']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
nt=rd('native-type.json');assert o['type']==nt['type']and nt['type'].startswith('∀ {n m : ℕ},')
assert '∀ (δ : ℝ), 0 ≤ δ → δ ≤ δ₀ →'in nt['type']and nt['printer_elision']
assert o['project_dependencies']==['Roth.eta']and not nt['full_kernel_body_dump']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.is_file():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==4
assert {e['label']for e in v['accepted']}=={'original','isolated','inline','project'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(e['receipt']);src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256']and r['request']==e['original_execution_request']
 assert isinstance(r['elapsed_ms'],int)and r['elapsed_ms']>=0
 assert not r['raw'].get('isError',False)and z['success']and not z.get('timed_out')
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert s.startswith((D/'isolated-prefix19.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==19 and '#check_failure '+N in s
  ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')and not z.get('failed_dependencies')
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==9;ds=z['items']
 assert not[d for d in ds if d.get('severity')in['error','warning']or d.get('category')=='sorry']
 assert not any('sorryAx'in d['message']for d in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(d['message']for d in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(d['message']for d in ds if d.get('line',0)>=e['native_region_start_line'])
 assert all(marker in info for marker in e['required_info'])
 if e['label']=='original':assert 'characters elided'in info
 else:assert 'characters elided'not in info
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
assert len(v['rejected'])==5
for e in v['rejected']:
 r=rd(e['receipt']);z=result(e['receipt']);s=(D/e['source']).read_text()
 if 'code'in r['request']:assert r['request']['code']==s
 ds=z.get('diagnostics',z.get('items',[]));assert any(d['severity']in['error','warning']for d in ds)
assert len(v['warming'])==1 and result(v['warming'][0]['receipt'])['partial']is True
assert result('original-printer-receipt.json')['success']
assert 'DELTA234_BODY_CONSTANTS: none'in'\n'.join(d['message']for d in result('original-printer-receipt.json')['items'])
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path']for x in fresh}
for x in fresh:
 assert x['match']and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in['MainLemma','Main','LeanEval']:
 assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0 and'2467 jobs'in(D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[233]==rd('canonical-entry.json')
assert order[233]['name']==N and order[233]['line']==77
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(v['audit']['receipt'])
for marker,ns in[('DELTA234_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),('DELTA234_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[d['message'][len(marker):]for d in z['items']if d['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['Roth.exists_delta']and not v['canonical_direct_type_consumers']
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Delta234Original\nopen Roth',1).replace('end Roth','end Delta234Original');body=re.sub(r'\bexists_delta_bound\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
# Reconstruct the actual complete caller replay; only target invocation is replaced.
source=(D/'source-Main.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Delta234Inline\nopen Roth',1).replace('end Roth','end Delta234Inline')
target=rd('target-metadata.json')['source'];sig,proof=target.split(' := by\n',1)
local=sig.replace('theorem exists_delta_bound {n m : ℕ} (hm : 16 * n ^ 2 < m)','have local_bound')+' := by\n'+proof
local='\n'.join('  '+l if i==0 else '    '+l for i,l in enumerate(local.splitlines()))
body=body.replace("  obtain ⟨δ₀, hδ₀, hδ₀'⟩ := exists_delta_bound hm",local+"\n  obtain ⟨δ₀, hδ₀, hδ₀'⟩ := local_bound")
lines=[]
for l in ((D/'disk-prefix.lean.txt').read_text()+body).splitlines():
 while len(l)>100:
  pos=l.rfind(' ',0,99);lines.append(l[:pos]);l='      '+l[pos+1:]
 lines.append(l)
inl=(D/'inline-executed.lean.txt').read_text();assert inl.startswith('\n'.join(lines)+'\n')
assert 'exists_delta_bound'not in body and 'Lean.Meta.isDefEq old.type new.type'in inl
assert '#print axioms Delta234Inline.roth'in inl and '#print axioms Delta234Inline.roth_rat'in inl
iso=(D/'isolated-executed.lean.txt').read_text();pj=(D/'project-executed.lean.txt').read_text()
for name in['transport','small_continuous','small_power_perturbation','gap_iff','original_expanded','no_m_zero','equality_boundary','exponent_zero_fails']:
 assert '#print axioms Delta234Generic.'+name in iso
for name in['sharp_iff','closed_endpoints','n_zero','generic_specializes','interval_shape','transport_full_event']:
 assert '#print axioms Delta234Project.'+name in pj
assert "Real.zero_rpow hp.ne'"in iso and'0 < p'in iso
assert '(h 0 le_rfl hδ₀.le).2'in pj and'h δ₀ hδ₀.le le_rfl'in pj
assert 'mem_nhdsGE_iff_exists_Icc_subset.mp (nhdsWithin_le_nhds he)'in pj
assert "Roth.eta._proof_1, Roth.gam._proof_1"in'\n'.join(d['message']for d in result('project-receipt.json')['items'])
auth=rd('root-prefix-scope-authorization.json');pp=rd('prefix-provenance.json')
b18=(D/'isolated-prefix.lean.txt').read_text();p19=(D/'isolated-prefix19.lean.txt').read_text()
assert sha(D/'isolated-prefix.lean.txt')==auth['base_prefix_sha256']==pp['base18_sha256']
assert pp['base_shared_unchanged']and len(re.findall('^import ',b18,re.M))==18
assert p19==b18+''.join('import '+i+'\n'for i in auth['extra_imports'])
assert sha(D/'isolated-prefix19.lean.txt')==pp['accepted19_sha256']
for form in['current','standard','abstract','power']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['form']==form and f['method']==method
  assert f['request']['query']and not f['raw'].get('isError',False)
  assert 'items'in f['raw']['structuredContent']
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1]and not f['stderr']
rg=rd('source-search.json');gg=rd('tracked-source-search.json');assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['distinct_declarations']==len(cs['callers'])==1 and cs['bound_applications']==2
for c in cs['callers']:
 lines=(R/c['file']).read_text().splitlines();assert c['source'].strip()=='\n'.join(lines[c['line']-1:c['end_line']]).strip()
 assert hashlib.sha256(c['source'].encode()).hexdigest()==c['source_sha256']
 assert len(re.findall(r'\bexists_delta_bound\b',c['source']))==1
for k in['web-general','nlab','ncatlab','stacks','stacks-refine','mathoverflow','arxiv','arxiv-retry','web-api','primary-crosscheck']:
 x=rd(k+'.json');assert x['request']and x['response']['status'].startswith('returned')
 assert re.fullmatch('[a-f0-9]{64}',x['response']['sha256'])and x['response']['bytes']>0
 assert x['summary']and all(l['title'].strip()and l['url'].startswith('https://')for l in x['sources'])
 assert not any('...'in l['url']or re.search(r'(?i)(signature|token|credential)=',l['url'])for l in x['sources'])
assert len({q['q']for q in rd('web-general.json')['request']['search_query']})>=3
assert 'site:ncatlab.org/ncatlab'in rd('ncatlab.json')['request']['search_query'][0]['q']
aq=rd('arxiv.json')['request']['search_query'][0]['q'];assert 'after:2021-10-28'in aq and'before:2026-10-29'in aq
assert 'mathlib4'in rd('web-api.json')['request']['search_query'][0]['q']
prep=rd('preparation-checks.json');assert prep['final_exact_source_gate']['exit_code']==0 and not prep['stale_source_execution']
report=D/'report.md'
if not report.is_file():report=R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
text=report.read_text();assert all(l==l.rstrip()for l in text.splitlines())
for target in re.findall(r'\]\((\.\./evidence/[^)]+)\)',text):
 assert(D/target.split('/'+N+'/',1)[1]).is_file(),target
for t in['## Phase 4a —','## Phase 4b —','all nine rows','all five rows','All15','NOT-COMPOSABLE','sufficient, not claimed minimal','two bound applications, not two callers','BORDERLINE-needs-human','original exists_delta signature retained']:
 assert t in text,t
p=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert p.returncode==0,(p.stdout,p.stderr)
print(json.dumps(dict(status='PASS',declaration=N,current_manifest_files=len(m['files']),fresh_source_pins=17,canonical_exact_order=293,formal_cells=20,actual_callers=1,returned_bound_applications=2,accepted_native_runs=4,secret_guard='PASS')))
