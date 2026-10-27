#!/usr/bin/env python3
"""Read-only validation in scratch or integrated layout; current manifest is authoritative."""
from pathlib import Path
import json,re,hashlib,sys,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
NAME='Roth.index'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=read('assessment.json');assert a['completed'] and a['allphases']=='PASS' and not a['unresolved']
assert a['declaration']==NAME and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(v=='PASS' for v in a['phases'].values())
seen=set()
for e in read('copy-manifest.json')['files']:
 p=(D/'report.md' if (D/'report.md').exists() else ROOT/e['destination']) if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','validate.py','overview-entry.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed
for e in v['accepted']:
 p=D/e['source'];assert sha(p)==e['source_sha256'];s=p.read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 results=[z for z in nodes(r['result']) if isinstance(z,dict) and z.get('success') is True]
 if e.get('format')=='raw':
  z=r['result']['structuredContent'];assert z['success'] and not z['timed_out'];ds=z['diagnostics'];assert r['request']['code']==s
  assert '#check_failure Roth.index' in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert results
  for z in results:assert z.get('partial') is False and not z.get('timed_out') and not z.get('failed_dependencies')
  ds=results[0].get('items',results[0].get('diagnostics',[]))
 assert not [z for z in ds if z.get('severity') in ['error','warning'] or z.get('category')=='sorry']
 new=[z for z in ds if z.get('line',0)>=e.get('native_region_start_line',0)]
 info='\n'.join(z.get('message','') for z in new)
 for m in e['required_info']:assert m in info,(e['label'],m)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert axs
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for p in v['rejected']:assert (D/p).is_file()
inputs=read('inputs.json');assert len(inputs)==17 and all(x['match'] for x in inputs)
for x in inputs+read('mathlib-inputs.json'):assert sha(ROOT/x['path'])==x['sha256'] and (ROOT/x['path']).stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
for e in read('source-excerpts.json'):
 expected='\n'.join((ROOT/e['source']).read_text().splitlines()[e['start_line']-1:e['end_line']])+'\n'
 assert (D/e['archive']).read_text()==expected
assert read('direct-consumers.json')['count']==39
assert read('input-hash-check.json')['all_pass']
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/'index-audit-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
actual=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 actual.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert actual==expected and len(set(actual))==293
calls=read('formal-search.json');assert len(calls)>=12 and all(not c['response'].get('isError',False) for c in calls)
for m in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:assert sum(c['method']==m for c in calls)>=3
for f in ['current','literature','abstract','inline']:assert read('rg-'+f+'.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web*-metadata.json')];qs=[q['q'] for w in web for q in w['request'].get('search_query',[])]
assert len({x['q'] for x in read('web0-metadata.json')['request']['search_query']})==3
for s in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(s in q for q in qs)
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
cs=read('callers.json');assert len(cs)==34 and sum(c['identifier_occurrences'] for c in cs)==60
assert sum(c['file']=='Roth/Index.lean' for c in cs)==16
for c in cs:assert sha(ROOT/c['file'])==c['source_sha256'] and c['source_fragment'] and c['plan']
e=read('overview-entry.json');assert 'Fintype' in e['type'] and 'MvPolynomial' in e['type']
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable/Roth.index.md'
s=p.read_text();assert '## Phase 8' in s and a['verdict'] in s and 'PENDING' not in s
for l in re.findall(r'\]\(([^)]+)\)',s):
 if l.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert l.startswith(prefix) and (D/l[len(prefix):]).is_file(),l
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: full phases, current artifacts, exact native checks, scoped axioms, canonical order293, hashes17, callers34, all searches, links, secret guard')
