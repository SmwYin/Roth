#!/usr/bin/env python3
"""Portable, read-only scratch/integrated validator; current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
NAME='Roth.le_index_iff'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] is True and not z.get('timed_out')
 if e['format']=='raw':
  ds=z['diagnostics'];s=(D/e['source']).read_text();assert r['request']['code']==s
  assert '#check_failure '+e['guard'] in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies')
  assert not z.get('still_elaborating_lines');ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 return ds
assert D.is_dir()
a=read('assessment.json');assert a['declaration']==NAME and a['completed'] and a['allphases']=='PASS'
assert not a['unresolved'] and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])==set(['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'])
assert all(x=='PASS' for x in a['phases'].values())
seen=set()
for e in read('copy-manifest.json')['files']:
 if '/mathlibable/' in e['destination']:
  p=D/'report.md'
  if not p.exists():p=ROOT/e['destination']
 else:p=D/Path(e['destination']).name
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
actual={p.name for p in D.iterdir() if p.is_file()}
assert actual-{'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed
for e in v['accepted']:
 p=D/e['source'];assert sha(p)==e['source_sha256'];s=p.read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for m in e['required_info']:assert m in info,(e['label'],m)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert axs
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for e in v['rejected']:assert (D/e['source']).is_file() and (D/e['receipt']).is_file()
inputs=read('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['expected_sha256'] for x in inputs)
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
assert read('input-hash-check.json')=={'all_pass':True,'count':17}
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293
assert 'let target := `Roth.le_index_iff' in s
cs=read('callers.json');assert len(cs)==4 and sum(c['identifier_occurrences'] for c in cs)==5
assert sum(c['file']=='Roth/Index.lean' for c in cs)==3
for c in cs:
 assert sha(ROOT/c['file'])==c['source_sha256'] and c['source_fragment'] in (ROOT/c['file']).read_text() and c['plan']
 for line in c['reference_lines']:assert 'le_index_iff' in (ROOT/c['file']).read_text().splitlines()[line-1]
cons=read('direct-consumers.json');assert cons['count']==4 and set(cons['consumers'])=={c['declaration'] for c in cs}
search=read('complete-caller-search.json');assert len(search['searches'])==2
assert all(e['exit_code']==0 and len(e['stdout'].splitlines())==7 for e in search['searches'])
assert {x['file'] for x in order}<=set(search['canonical_source_inventory'])
orig=next(e for e in v['accepted'] if e['label']=='original-and-audit');ds=native(orig)
new=[x for x in ds if x.get('line',0)>=v['audit']['native_region_start_line']]
actualcons=[x['message'].split(': ',1)[1] for x in new if x['message'].startswith('LE_INDEX_IFF137_DIRECT_CONSUMER:')]
assert actualcons==cons['consumers']
s=(D/'le-index-iff-callers-executed.lean.txt').read_text();assert not re.search(r'\ble_index_iff\b',s)
assert s.count('LeIndexIff137.originalReplacement')==2 and 'IndexReplay137.replacement' in s
formal=read('formal-search.json');assert len(formal)==12 and all(e['status']=='fulfilled' for e in formal)
formal=[e['value'] for e in formal]
for e in formal:assert e['result'].get('isError') is False
for f in ['current','literature','abstract']:
 for m in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
  assert any(e['form']==f and e['method'].endswith('__'+m) for e in formal)
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code']==0
assert read('local-literature-search.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web*-metadata.json')]
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
assert len({q['q'] for q in read('web0-metadata.json')['request']['search_query']})>=3
for target in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org after:2021-10-27 ']:assert any(target in q for q in queries)
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w and w['locators']
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
s=(D/'clean-excerpt.tex.txt').read_text();assert s=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:556])+'\n'
e=read('overview-entry.json');assert all(t in e['type'] for t in ['Fintype','MvPolynomial','hasseDeriv','Roth.index','Roth.weight'])
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
s=p.read_text();assert '## Phase 8' in s and a['verdict'] in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: phases, current manifest, native success/axioms, canonical exact order293, source/pin hashes17, four callers/five applications, formal/literature channels, portable links and credential guard')
