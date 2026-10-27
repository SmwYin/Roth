#!/usr/bin/env python3
"""Portable, read-only current-manifest validator for scratch and integrated layouts."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
NAME='MvPolynomial.taylor'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=read('assessment.json');assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['declaration']==NAME and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(v=='PASS' for v in a['phases'].values())
seen=set()
for x in read('copy-manifest.json')['files']:
 dst=x['destination']; p=(D/'report.md' if (D/'report.md').exists() else ROOT/dst) if '/mathlibable/' in dst else D/Path(dst).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add(p.name)
assert {'assessment.json','overview-entry.json','verification.json','validate.py'}<=seen
v=read('verification.json');assert v['unresolved']==[]
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label'] for x in v['accepted']}=={'target','raw','callers'}
for x in v['accepted']:
 p=D/x['source'];assert sha(p)==x['source_sha256'];t=p.read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',t)
 r=read(x['receipt']);assert not r['result'].get('isError',False)
 good=[n for n in nodes(r['result']) if isinstance(n,dict) and n.get('success') is True];assert good
 for n in good:
  assert n.get('partial',False) is False and n.get('timed_out',False) is False and not n.get('failed_dependencies')
  di=n.get('diagnostics',n.get('items',[]));assert not [d for d in di if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  axs=re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(d.get('message','') for d in di));assert axs
  for ax in axs:assert {s.strip() for s in ax.split(',') if s.strip()}<=allowed
 if x['label']=='raw':
  assert r['request']['code']==t and '#check_failure '+NAME in t and not re.search(r'^import Roth\b',t,re.M)
 else: assert r['request']['file_path'].endswith('.lean')
for f in v['rejected']:assert (D/f).is_file()
assert read('native-target-rejected.json')['result']
inputs=read(v['inputs']);assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+read(v['mathlib_inputs']):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
for src,archive in v['source_links'].items():assert sha(ROOT/src)==sha(D/archive)
assert read('input-hash-check.json')['all_pass']
for r in read('formal-search.json'):
 assert r['status']=='fulfilled' and not r['value']['response'].get('isError',False)
for method in ['Finder','Loogle','LeanSearch','local']:
 assert {x['value']['form'] for x in read('formal-search.json') if x['value']['method']==method}=={'current','literature','abstract'}
for form in ['current','literature','abstract']:assert read('rg-'+form+'.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web-*-metadata.json')]
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for term in ['site:ncatlab.org/nlab','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(term in q for q in queries),term
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
cs=read('callers.json');assert len(cs)==24 and sum(x['identifier_occurrences'] for x in cs)==41
assert sum(x['file']=='Roth/Taylor.lean' for x in cs)==17
for c in cs:assert sha(ROOT/c['file'])==c['source_sha256'] and c['reference_lines'] and c['plan']
e=read('overview-entry.json');assert e['type'].startswith('{σ : Type') and e['caller_summary']['all_explicit_callers']==24
report=D/'report.md'
if not report.exists():report=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
t=report.read_text();assert '## Phase 8' in t and '**BORDERLINE-needs-human**' in t
for link in re.findall(r'\]\(([^)]+)\)',t):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert link.startswith(prefix),link;assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: all phases, current manifest hashes/bytes, exact complete native checks and axioms, 17 inputs, three-form searches, all 24 callers, links, credential guard')
