#!/usr/bin/env python3
"""Portable read-only current-manifest validator; accepts scratch or integrated evidence."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.Θ_nonneg'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==188 and a['completed']
assert a['allphases']=='PASS' and a['verdict']=='NO-mathlib-has-it'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type'] and 'Fintype σ' in o['type']
assert '0 ≤ Roth.Θ B q r' in o['type'] and 'DecidableEq' not in o['type']
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
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==5 and not v['rejected']
assert {x['label']for x in v['accepted']}=={'original','project','isolated','callers','bridge'}
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success'] and not z.get('timed_out')
 src=D/e['source'];s=src.read_text();assert sha(src)==e['source_sha256']
 assert r['request']==e['original_execution_request']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 else:
  assert z['partial'] is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline'] and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for f in ['Theta','Index','Box']:assert sha(R/'Roth'/f'{f}.lean')==sha(D/f'{f}.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']
 assert p.stat().st_size==x['bytes'] and sha(D/x['archive'])==sha(p)
loc=rd('local-literature-input.json');assert sha(R/loc['source'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert set(o['project_dependencies']) <= {x['name'] for x in order}
assert len({x['name']for x in order})==293 and order[187]==rd('canonical-target.json')
assert order[187]['name']==N and order[187]['line']==107
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
 else ('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert v['canonical_direct_consumers']==['Roth.index_le_lem6']
assert v['canonical_direct_type_consumers']==[]
z=result(rd('theta-nonneg188-original-receipt.json'))
for marker,ns in [('THETANONNEG188_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
 ('THETANONNEG188_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert [x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
f=rd('formal-search.json');assert len(f)==12
assert {(x['form'],x['method'])for x in f}=={(fm,m)for fm in ['current','literature','abstract']
 for m in ['Finder','Loogle','LeanSearch','local']}
for x in f:assert not x['response'].get('isError',False)
for fm in ['current','literature','abstract']:assert rd('rg-'+fm+'.json')['exit_code'] in [0,1]
rg=rd('callers-rg.json');gg=rd('callers-git.json')
assert rg['exit_code']==gg['exit_code']==0 and sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
lines=rg['stdout'].splitlines();assert len(lines)==3
assert ':583:' in lines[2] and lines[2].count('Θ_nonneg')==2
cs=rd('callers.json');assert cs['distinct_declarations']==1 and cs['call_occurrences']==2
assert cs['reference'] in (R/cs['file']).read_text().splitlines()[cs['line']-1]
qs=[]
for n in ['web0-metadata.json','web4-metadata.json','web-direct-metadata.json']:
 w=rd(n);assert len(w['response_digest']['sha256'])==64 and w['response_digest']['bytes']>0
 assert w['status'] and w['locators'] and w['summary'];qs.extend(x['q']for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
 'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-27' in q for q in qs)
assert len(rd('web-direct-metadata.json')['request']['open'])==4
project=(D/'theta-nonneg188-project-executed.lean.txt').read_text().splitlines()[342:]
p='\n'.join(project)
assert 'Roth.index_nonneg' not in p and 'Roth.Θ_nonneg' not in p
assert 'Finset.sum_nonneg' in p and 'div_nonneg' in p and 'Nat.cast_nonneg' in p
assert 'Real.sSup_nonneg' in p and 'Real.sInf_nonneg' in p
caller=(D/'theta-nonneg188-callers-executed.lean.txt').read_text()
caller=caller[caller.index('elab "mapped188"'):]
assert caller.count('ThetaNonneg188.replacement _')==2 and 'Θ_nonneg' not in caller
assert caller.count('Lean.mkPrivateNameCore `Roth.Theta')==3
orig=(R/'Roth/Theta.lean').read_text();orig=orig[orig.index('theorem index_le_lem6 '):]
orig=orig[:orig.index('\nomit [DecidableEq τ] in')].strip()
new=orig.replace('theorem index_le_lem6 ','theorem caller ').replace('Θ_nonneg _','ThetaNonneg188.replacement _')
for a,b in [('mapped_det_ne_zero_aux','mapped188'),('weight_le_delta_aux','weight188'),
 ('index_numeric_bound_aux','numeric188')]:new=new.replace(a,b)
assert new in caller
bridge=(D/'theta-nonneg188-bridge-executed.lean.txt').read_text()
assert 'Roth.Θ B q r = SupSet.sSup (Roth.indexSet B q r) := rfl' in bridge
c=v['composition'];assert c['parent_reaim'] and c['bridge_definitional'] and c['pointwise_independent']
assert not c['strict_three_existing_call_term_verified'] and not c['parent_project_def_counted_as_mathlib_block']
assert c['actual_caller_replays']==1 and c['actual_call_occurrences']==2
assert c['no_circular_later_zero_member_extension'] and c['no_global_absence_claim']
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
assert 'NO-mathlib-has-it' in s and 're-aim' in s and 'all five accepted native sets' in s.lower()
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:188; all phases; fresh17; ordered293;1value/0type;5clean native;15formal cells;1full caller/2occurrences;current manifest/links/secrets.')
