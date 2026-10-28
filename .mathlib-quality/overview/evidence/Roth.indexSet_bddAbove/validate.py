#!/usr/bin/env python3
"""Portable read-only validation of current scratch or integrated artifacts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.indexSet_bddAbove'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==186 and a['completed']
assert a['verdict']=='BORDERLINE-needs-human' and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']
assert '∀ {σ : Type u_1} [inst : Fintype σ] (B : ℝ) (q : σ → ℕ) {r : σ → ℕ}' in o['type']
assert 'BddAbove (Roth.indexSet B q r)' in o['type']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/' in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==3 and len(v['rejected'])==1
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success'] and not z.get('timed_out')
 src=D/e['source'];s=src.read_text();assert sha(src)==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 else:
  assert z['partial'] is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message'] for x in ds)):
  assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
 info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
rej=v['rejected'][0];assert (D/rej['source']).is_file();z=result(rd(rej['receipt']))
assert not z['success'] and any('sorryAx' in x['message'] for x in z['diagnostics'])
s=(D/'bddabove186-isolated-executed.lean.txt').read_text()
assert '[LE γ]' in s and '⟨c, Set.forall_mem_image2.mpr h⟩' in s
assert 'change (∃ c, ∀ z ∈ Set.image2 f s t, z ≤ c) ↔ _' in s
s=(D/'bddabove186-project-executed.lean.txt').read_text()
assert 'Roth.index_le_card' in s and 'theorem pointwise' in s
assert 'theorem caller_index_le' in s and 'theorem caller_mono' in s
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source'] for x in fresh}
for x in fresh:assert x['matches_baseline'] and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'] and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name'] for x in order})==293 and order[185]==rd('canonical-target.json')
assert order[185]['name']==N and order[185]['line']==87
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private'
 else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm) if mod else ('public',pub) for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert v['canonical_direct_consumers']==rd('direct-consumers.json')==['Roth.index_le_Θ','Roth.Θ_mono']
assert v['canonical_direct_type_consumers']==rd('direct-type-consumers.json')==[]
z=result(rd('bddabove186-original-receipt.json'))
for marker,ns in [('BDDABOVE186_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
 ('BDDABOVE186_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert [x['message'][len(marker):] for x in z['items'] if x['message'].startswith(marker)]==ns
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
f=rd('formal-search.json');assert len(f)==12
assert {(x['form'],x['method']) for x in f}=={(fm,m) for fm in ['current','standard','abstract']
 for m in ['finder','loogle','leansearch','local']}
for x in f:assert not x['response'].get('isError',False)
for fm in ['current','standard','abstract']:assert rd('rg-'+fm+'.json')['exit_code'] in [0,1]
assert len(rd('formal-positive.json'))==3
assert sorted(rd('callers.json')['stdout'].splitlines())==sorted(rd('git-callers.json')['stdout'].splitlines())
cs=rd('callers-structured.json');assert len(cs)==2
assert [x['declaration'] for x in cs]==v['canonical_direct_consumers']
for x in cs:assert x['excerpt']==(R/x['file']).read_text().splitlines()[x['line']-1]
qs=[]
for n in ['web-0.json','web-1.json','web-2.json','web-3.json','web-primary.json']:
 w=rd(n);assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['status'] and w['urls'] and w['summary'];qs.extend(x['q'] for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
 'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t) for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
assert len(rd('web-primary.json')['request']['open'])==3
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
assert 'BORDERLINE-needs-human' in s and 're-aim' in s
assert '1. Should' in s and '2. Should' in s and '3. Should' in s
assert v['composition']['complete_family_checked'] and not v['composition']['strict_three_existing_call_term_verified']
assert not v['composition']['parent_project_def_counted_as_mathlib_block']
assert v['composition']['no_global_absence_claim'] and v['composition']['bridge_definitional']
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:186; all phases; fresh17; ordered293;2value/0type;3clean native; rejected1 retained;15search cells;2callers; current manifest/links/secrets.')
