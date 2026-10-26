"""Portable read-only validator. Pass repository root if cwd differs."""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
target='MvPolynomial.hasseDeriv_hasseDeriv'
report=b/'report.md'
if not report.is_file(): report=r/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
a=json.loads((b/'assessment.json').read_text())
assert a['declaration']==target and a['completed'] and a['root_acceptance'] in ['pending','PASS'] and a['unresolved']==[]
assert a['verdict']=='YES-add-as-is'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS' or x.startswith('N/A:') for x in a['phases'].values())
for path,e in json.loads((b/'input-manifest.json').read_text())['sources_and_pins'].items():
 assert hashlib.sha256((r/path).read_bytes()).hexdigest()==e['sha256'],path
for e in json.loads((b/'reference-hashes.json').read_text()):
 raw=(r/e['path']).read_bytes();assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256']
for e in json.loads((b/'copy-manifest.json').read_text())['files']:
 f=report if e['source']=='report.md' else b/e['source']; raw=f.read_bytes()
 assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256'],e['source']
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('https:','http:')):continue
 assert (b/link).is_file(),link
v=json.loads((b/'verification.json').read_text());assert v['unresolved']==[]
axioms=0
for e in v['accepted']:
 code=(b/e['source']).read_text(); assert hashlib.sha256(code.encode()).hexdigest()==e['source_sha256']
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 d=json.loads((b/e['receipt']).read_text());native=d['result'];assert not native.get('isError',False)
 sc=native.get('structuredContent',native);out=sc.get('result',sc)
 assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
 ds=out.get('items',out.get('diagnostics',[]));assert not any(x.get('severity') in ['error','warning'] for x in ds)
 if 'code' in d['request']:assert d['request']['code']==code
 else:
  c=json.loads((b/e['source_check']).read_text());assert c['matched_at_freeze'] and c['retained_sha256']==e['source_sha256']==c['disk_sha256']
 for item in ds:
  msg=item.get('message','');assert 'sorryAx' not in msg
  if 'depends on axioms:' in msg:
   names=re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',')
   assert {x.strip() for x in names if x.strip()}<={'propext','Classical.choice','Quot.sound'};axioms+=1
assert axioms>=5
raw=(b/'raw-executed.lean.txt').read_text()
assert 'import Roth' not in raw and "induction P using MvPolynomial.induction_on'" in raw and 'Nat.choose_mul' in raw and 'theorem iterativity' in raw
assert '#check_failure MvPolynomial.hasseDeriv_hasseDeriv' in raw and '#check_failure MvPolynomial.hasseDeriv' in raw
extra=(b/'extra-executed.lean.txt').read_text();assert 'theorem weighted' in extra and 'Finsupp.single () 2' in extra
for f in ['finder-current.json','Finder-literature.json','Finder-abstract.json','Loogle-current.json','loogle-literature.json','Loogle-abstract.json','search-current.json','search-literature.json','Search-abstract.json','Local-current.json','local-literature.json','Local-abstract.json']:
 d=json.loads((b/f).read_text());assert d['request']; res=d.get('response',d.get('result'));assert not res.get('isError',False)
rs=json.loads((b/'source-search.json').read_text());assert len(rs)>=4 and rs[2]['exit_code']==1
web=json.loads((b/'web-receipts.json').read_text())['requests']+[json.loads((b/'web5-receipt.json').read_text())]
assert len({q['q'] for x in web for q in x['request'].get('search_query',[])})>=3
for x in web:assert re.fullmatch('[a-f0-9]{64}',x['response']['sha256']) and x['response']['bytes']>0 and x['status'] and x['summary']
assert len(json.loads((b/'web-sources.json').read_text()))>=5
assert a['upstream']['group_with'] and a['upstream']['reviewer_candidates'] and a['missing_api']
print('PASS: all phases, source/pin/reference/current copy hashes, complete native successes, standard axioms, exact sources, five methods and full literature metadata')
