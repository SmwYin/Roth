#!/usr/bin/env python3
"""Portable read-only validation for completed canonical229; current manifest authoritative."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.lam'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==229 and a['completed']
assert a['allphases']=='PASS' and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='BORDERLINE-needs-human' and a['root_acceptance']in['pending','PASS']
assert not a['unresolved'] and not v['unresolved'] and 1<=len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']=='ℝ → ℕ → ℕ → ℝ'
assert not o['project_dependencies'] and not rd('native-type.json')['printer_elision']
# Current manifest is always checked; worker/root historical acceptance snapshots are not substitutes.
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==4
assert {x['label']for x in v['accepted']}=={'original','isolated','inline','project'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(r);assert not r['result'].get('isError',False)
 assert z['success'] and not z.get('timed_out');src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256'] and r['request']==e['original_execution_request']
 assert isinstance(r['elapsed_ms'],int) and r['elapsed_ms']>=0
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
  prefix=(D/'isolated-prefix.lean.txt').read_text();assert s.startswith(prefix)
  assert len(re.findall(r'^import ',s,re.M))==18
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())
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
rej=v['rejected'][0];assert (D/rej['source']).is_file()
z=result(rd(rej['receipt']));assert z['success']
assert any('expected type contains metavariables'in d['message']for d in z['diagnostics'])
assert result(rd(v['warming'][0]['receipt']))['partial']is True
iso=(D/'isolated-executed.lean.txt').read_text();zi=result(rd('isolated-receipt.json'))
assert 'inferInstance : CoeFun ℝ (fun _ : ℝ ↦ ℝ → ℝ)'in iso
assert any('failed to synthesize instance of type class\n  CoeFun ℝ'in d['message']for d in zi['diagnostics'])
assert not any('expected type contains metavariables'in d['message']for d in zi['diagnostics'])
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17 and set(base)=={x['path']for x in fresh}
for x in fresh:
 assert x['match'] and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in ['MainLemma','Main','Lattice']:
 assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
loc=rd('literature-source.json');assert sha(R/loc['path'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0 and'2467 jobs'in(D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name']for x in order})==293 and order[228]==rd('canonical-entry.json')
assert order[228]['name']==N and order[228]['line']==60
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
 else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('LAM229_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
 ('LAM229_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['Roth.gam','Roth.exists_delta']
assert not v['canonical_direct_type_consumers']
# Exact full original module replay, target renaming confined to the module before the audit.
source=(D/'source-MainLemma.lean.txt').read_text();body=source[source.index('namespace Roth'):]
body=body.replace('namespace Roth','namespace Lam229Original\nopen Roth',1).replace('end Roth','end Lam229Original')
body=re.sub(r'\blam\b','replay',body)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+body)
# Full caller modules, exact recorded inlining; original-signature checks cannot be skipped.
body=source[source.index('namespace Roth'):].replace('namespace Roth','namespace Lam229Inline\nopen Roth',1).replace('end Roth','end Lam229Inline')
body=body.replace('noncomputable def lam (δ : ℝ) (n m : ℕ) : ℝ := 4 * (1 + 3 * δ) * n * √(m : ℝ)','')
body=body.replace('lam δ n m','(4 * (1 + 3 * δ) * n * √(m : ℝ))').replace('[gam, lam]','[gam]')
body=body.replace('/-- The parameter `λ = 4(1 + 3δ) n m^{1/2}`. Source: §6, eq. (34). -/\n','')
main=(D/'source-Main.lean.txt').read_text();mb=main[main.index('namespace Roth'):]
mb=mb.replace('namespace Roth','namespace Lam229MainInline\nopen Roth',1).replace('end Roth','end Lam229MainInline')
mb=mb.replace('[gam, lam, eta,','[gam, eta,');mb=re.sub(r'\bgam\b','Lam229Inline.gam',mb)
mb=re.sub(r'\beta_lt_gam_iff\b','Lam229Inline.eta_lt_gam_iff',mb)
inl=(D/'inline-executed.lean.txt').read_text()
assert inl.startswith((D/'disk-prefix.lean.txt').read_text()+body+'\n'+mb+'\n')
assert not re.search(r'\blam\b',inl)
for t in ['example : Roth.gam = Lam229Inline.gam := rfl',
 'example : @Roth.eta_lt_gam_iff = @Lam229Inline.eta_lt_gam_iff := rfl',
 'example : @Roth.exists_delta = @Lam229MainInline.exists_delta := rfl',
 'Lean.mkPrivateNameCore `Roth.MainLemma','Lean.Meta.isDefEq old.type new.type']:
 assert t in inl
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  f=rd('search-'+form+'-'+method+'.json');assert f['form']==form and f['method']==method
  assert f['request']['query'] and not f['result'].get('isError',False)
  assert 'items'in f['result']['structuredContent']
 f=rd('search-'+form+'-rg.json');assert f['exit_code']in[0,1] and not f['stderr']
rg=rd('source-search.json');gg=rd('tracked-source-search.json')
assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
cs=rd('callers.json');assert cs['executable_occurrences']==cs['distinct_declarations']==4
assert len(cs['callers'])==4 and cs['external_to_file_declarations']==cs['external_to_file_files']==1
assert {x['name']for x in cs['callers']}=={'Roth.gam','Roth.eta_lt_gam_iff','Roth.exists_delta','Roth.exists_mem_RSet_le_index_of_log_bound_aux'}
for c in cs['callers']:
 lines=(R/c['file']).read_text().splitlines();assert c['source'].strip()=='\n'.join(lines[c['line']-1:c['end_line']]).strip()
inv=rd('source-inventory.json');assert inv['exit_code']==0
assert {x['file']for x in order}<=(set(inv['stdout'].splitlines())|{'Roth.lean'})
queries=[]
webnames=['web-general','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-locators','web-api-book']
for name in webnames:
 w=rd(name+'.json');assert len(w['raw_response_sha256'])==64 and w['raw_response_bytes']>0
 assert w['status']=='returned' and w['locators'] and w['summary'] and w['full_web_body_archived']is False
 for url in w['locators']+[x['url']for x in w['titles']]:
  assert url.startswith('https://') and '\\'not in url and not re.search(r'-{5,}',url),url
  assert not re.search(r'[?&](?:X-Amz[^=]*|token|signature|credential|sig)=',url,re.I),url
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
 'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-28 before:2026-10-29'in q for q in queries)
assert all('locator_note'in rd(n+'.json')for n in['web-general','mathoverflow'])
assert all(x['exit_code']==0 for x in rd('preparation-checks.json')['commands'])
c=v['composition'];assert not c['strict_three_existing_call_term_verified']
assert c['direct_arithmetic_construction_verified'] and c['actual_caller_replays']==4
assert not c['new_generic_scaled_definition_is_existing_mathlib']
assert c['original_signatures_retained_by_defeq'] and not c['imported_transitive_target_freedom_claimed']
p=D/'report.md'
if not p.exists():p=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=p.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and(D/link[len(prefix):]).is_file(),link
assert len(re.findall(r'^\| [1-9] \|',s.split('## Phase 4c')[1].split('## Phase 4.5')[0],re.M))==9
assert len(re.findall(r'^\| [1-5] \|',s.split('## Phase 4.6')[1].split('## Phase 5 ')[0],re.M))==5
assert len(re.findall(r'^\| (?:Typeclass|Reducibility|Noncanonical|Instance priority|Universe|Coercion)',s.split('## Phase 4.5')[1].split('## Phase 4.6')[0],re.M))==6
assert all(x in s for x in['NOT-COMPOSABLE','no printer-elision marker','all four original signatures','positive-a cancellation branch'])
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS229: complete phases; fresh17; exact canonical293; 2value/0type; four clean native sets; full fourcaller inlining; formal15; web URL guards; currentmanifest/links/secrets.')
