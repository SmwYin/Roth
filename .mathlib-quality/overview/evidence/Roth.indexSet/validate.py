#!/usr/bin/env python3
"""Read-only canonical180 validator, supporting scratch and integrated layouts."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.indexSet'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==180 and a['completed']
assert a['verdict']=='NO-mathlib-has-it'and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS')and not a['unresolved']and not v['unresolved']
assert a['root_acceptance']in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and 'Fintype'in o['type']
assert 'DecidableEq'not in o['type']and o['project_dependencies']==['Roth.RSet','Roth.index']
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
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success']and not z.get('timed_out')
 src=D/e['source'];s=src.read_text();assert sha(src)==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not [x for x in ds if x.get('severity')in ['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
assert len(v['accepted'])==6 and len(v['rejected'])==3
for e in v['rejected']:
 assert sha(D/e['source'])==e['source_sha256']
 z=rd(e['receipt'])['result']['structuredContent'];z=z.get('result',z)
 assert any(x.get('severity')in ['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 assert e['source']not in {x['source']for x in v['accepted']}
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline']and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
for n in ['Theta','Index','Box']:assert sha(R/'Roth'/(n+'.lean'))==sha(D/('source-'+n+'.lean.txt'))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[179]==rd('canonical-target.json')
assert order[179]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
          else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert len(v['canonical_direct_consumers'])==10 and len(v['canonical_direct_type_consumers'])==3
assert v['canonical_direct_consumers']==rd('direct-consumers.json')
assert v['canonical_direct_type_consumers']==rd('direct-type-consumers.json')
z=rd('indexset180-original-receipt.json')['result']['structuredContent']['result']
for marker,expected_names in [('INDEXSET180_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
                              ('INDEXSET180_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 actual=[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]
 assert actual==expected_names
b=rd('separation-file-completion-2026-10-27.json')
assert b['exit_code']==0 and '2467 jobs'in b['stdout']and not b['stderr']
assert sha(D/'separation-file-completion-2026-10-27.log')==b['log_sha256']
assert len(b['sources_and_pins'])==17
for x in b['sources_and_pins']:assert sha(R/x['path'])==x['sha256']
for form in ['current','standard','abstract']:
 for method in ['finder','loogle','leansearch','local']:
  n=f'search-{form}-{method}.json'
  if (form,method)==('standard','loogle'):n='search-standard-loogle-retry.json'
  q=rd(n);assert q['request']and not q['response'].get('isError',False)
 assert rd('rg-'+form+'.json')['exit_code']in[0,1]
assert rd('search-standard-loogle.json')['response']['isError']
assert rd('rg-current.json')['exit_code']==1 and not rd('rg-current.json')['stdout']
# rg and git differ only by line separator style after filename.
rg=rd('callers.json')['stdout'];gg=rd('git-callers.json')['stdout'];assert sorted(rg.splitlines())==sorted(gg.splitlines())
cs=rd('callers-structured.json');assert len(cs)==4
assert sum(h['occurrences']for c in cs for h in c['hits'])==5
ls=(R/'Roth/Theta.lean').read_text().splitlines()
for c in cs:
 assert c['file']=='Roth/Theta.lean'and c['refactor']
 for h in c['hits']:assert h['code']==ls[h['line']-1].strip()
queries=[]
for fn in ['web-0.json','web-1.json','web-2.json','web-primary.json','web-recent.json']:
 w=rd(fn);assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['status']and w['returned_locators']and w['summary']
 queries.extend(x['q']for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
          'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-27'in q and 'before:2026-10-28'in q for q in queries)
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
s=(D/'indexset180-expanded-executed.lean.txt').read_text();assert 'Set.image2_congr\''in s
s=(D/'indexset180-generality-executed.lean.txt').read_text()
assert 'def arbitrary_variable_image {σ : Type u} (B : ℝ)'in s
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:180 all phases; fresh17; ordered293;10value/3type consumers;6 clean native records; exact image2/full restrictions;15 search cells; currentmanifest/links/secrets.')
