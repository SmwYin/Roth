#!/usr/bin/env python3
"""Read-only validator for scratch or integrated declaration78 package."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.normOne_eq_sum_of_support_subset'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==78 and a['completed'] and a['allphases']=='PASS'
assert a['verdict']=='NO-mathlib-has-it' and a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
manifest=load('copy-manifest.json')
assert manifest['declaration']==N and manifest['files']
for x in manifest['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']} <= {Path(x['destination']).name for x in manifest['files']}|{'report.md'}
v=load('verification.json')
assert v['unresolved']==[] and {x['label'] for x in v['accepted']}=={'target','consumers','raw','extra'}
assert len(v['rejected'])==2 and {x['label'] for x in v['rejected']}=={'target','raw'}
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 successes=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True]
 assert successes
 messages=[]
 for z in successes:
  assert z.get('partial',False) is False and not z.get('timed_out',False) and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [q for q in ds if q.get('severity') in ['error','warning'] or q.get('category')=='sorry']
  msg='\n'.join(q.get('message','') for q in ds);messages.append(msg)
  assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axs
  for ax in axs:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 msg='\n'.join(messages)
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
  for t in ['theorem current','theorem supportLocal','theorem addedOnly','theorem zeroSizeNecessary','theorem containmentNecessary','Int.cast_zero','abs_zero','Finsupp.sum_of_support_subset','∀ i ∈ s, size i 0 = 0','∀ i ∈ s, i ∉ f.support → size i 0 = 0']:assert t in s,t
  for t in ['NormSupportRaw.current','NormSupportRaw.supportLocal','NormSupportRaw.addedOnly','NormSupportRaw.zeroSizeNecessary','NormSupportRaw.containmentNecessary']:assert t in msg
 elif x['label']=='target':
  for t in ['#print '+N,'theorem replay','theorem viaFinsupp','theorem genericPadding','fun _ z ↦ |(z : ℝ)|']:assert t in s,t
  for t in [N,'NormSupportAssessment.viaFinsupp','@Finsupp.sum_of_support_subset']:assert t in msg,t
 elif x['label']=='consumers':
  for t in ['theorem monomialValue','theorem addition','NormSupportAssessment.viaFinsupp']:assert t in s
  assert N not in s and s.count('NormSupportAssessment.viaFinsupp')==4
  for t in ['NormSupportConsumers.monomialValue','NormSupportConsumers.addition']:assert t in msg
 else:
  assert 'theorem normCoefficients' in s and '[SeminormedCommRing R]' in s
  assert 'NormSupportExtra.normCoefficients' in msg
for x in v['rejected']:
 assert (D/x['source']).is_file() and (D/x['receipt']).is_file() and x['reason']
inputs=load('inputs.json')
assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert load('input-hash-check.json')['all_pass'] and '2467 jobs' in (D/'baseline-build.txt').read_text()
local=load('local-literature-source.json');p=R/local['path'];assert sha(p)==local['sha256'] and p.stat().st_size==local['bytes']
f=load('formal-search.json');assert len(f)==13
for m in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 assert {x['form'] for x in f if x['method']==m}>={'current','standard','abstract'}
assert load('lean_loogle-current.json')['result']['isError']
assert not load('lean_loogle-current-retry.json')['result'].get('isError',False)
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json');assert x['exit_code'] in [0,1] and x['command'][0]=='rg'
assert len(load('rg-callers.json')['stdout'].splitlines())==5
qs=[]
for i in range(7):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes_utf8']>0
 assert w['summaries'] and w['urls'] and not w['full_bodies_archived'] and 'response' not in w
 assert all('?' not in u for u in w['urls'])
 qs.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in qs)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==2 and c['occurrence_count']==4 and c['external_to_declaring_file']==0
assert len(c['callers'])==2
assert load('canonical-entry.json')['name']==N
o=load('canonical-order.json');assert o['index']==78 and o['total']==293 and o['entry']['name']==N
e=load('overview-entry.json');assert e['type'].startswith('∀') and N==e['declaration']
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for phase in phases:assert 'Phase '+phase in s
for t in ['**SMALL**','NO-mathlib-has-it','MAXIMALLY GENERAL','supportLocal','addedOnly','False-generalization','Int.cast_zero','abs_zero','Both **entire proof bodies**','no Mode B parent re-aim override','NO-composable']:assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS78: full phases; exhaustive named literature channels; formal5methods/3forms+queryretry; existing exact generic padding specialization; explicit3facts;4clean native sets;2full consumers/4uses; generalizations/2guards; hashes/currentmanifest/links/credentials.')

