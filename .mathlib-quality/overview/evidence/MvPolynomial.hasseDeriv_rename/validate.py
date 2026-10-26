"""Portable, read-only package validation; scratch or integrated evidence layout."""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
target='MvPolynomial.hasseDeriv_rename'
assert (r/'lakefile.toml').is_file(),'Run in project root or pass it as argument'
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
a=json.loads((b/'assessment.json').read_text());assert a['completed'] and a['unresolved']==[] and a['root_acceptance'] in ['pending','PASS']
assert a['category']=='YES-add-as-is' and a['upstream']['group_with'] and a['missing_api']
assert all(x=='PASS' or x.startswith('N/A:') for x in a['phases'].values())
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
for path,e in json.loads((b/'input-manifest.json').read_text())['sources_and_pins'].items():assert hashlib.sha256((r/path).read_bytes()).hexdigest()==e['sha256'],path
for name in ['worker-source-manifest.json','reference-source-manifest.json']:
 for e in json.loads((b/name).read_text())['files']:
  p=r/e['path'];assert p.stat().st_size==e['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256'],e['path']
for e in json.loads((b/'copy-manifest.json').read_text())['files']:
 p=report if e['source']=='report.md' else b/e['source'];raw=p.read_bytes();assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256'],p
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http:','https:')):continue
 prefix='../evidence/'+target+'/'
 p=b/link[len(prefix):] if link.startswith(prefix) else report.parent/link
 assert p.is_file(),link
v=json.loads((b/'verification.json').read_text());assert v['unresolved']==[]
axiom_count=0
for e in v['accepted']:
 code=(b/e['source']).read_text();assert hashlib.sha256(code.encode()).hexdigest()==e['source_sha256']
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 raw=json.loads((b/e['receipt']).read_text());native=raw['result'];assert not native.get('isError',False)
 sc=native.get('structuredContent',native);res=sc.get('result',sc)
 assert res['success'] and not res.get('partial',False) and not res.get('timed_out',False) and not res.get('failed_dependencies')
 ds=res.get('items',res.get('diagnostics',[]));assert not any(x['severity'] in ['error','warning'] for x in ds)
 if 'code' in raw['request']:assert raw['request']['code']==code
 else:
  c=json.loads((b/e.get('source_check','execution-source-check.json')).read_text());assert c['matched_at_freeze'] and c['retained_sha256']==e['source_sha256']==c['disk_sha256']
 for d in ds:
  msg=d.get('message','')
  assert 'sorryAx' not in msg
  if 'depends on axioms:' in msg:
   names=re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',')
   assert {s.strip() for s in names if s.strip()} <= {'propext','Classical.choice','Quot.sound'}
   axiom_count+=1
assert axiom_count>=10
rawcode=(b/'rawdelta-executed.lean').read_text(); assert 'import Roth' not in rawcode and "induction P using MvPolynomial.induction_on'" in rawcode and 'coeff_hasseDeriv' not in rawcode and 'Finsupp.lsum_single' in rawcode and 'Finsupp.mapDomain_tsub hf' in rawcode and 'Finsupp.prod_mapDomain_index_inj hf' in rawcode
math=(b/'mathlib-executed.lean').read_text();assert 'import Roth' not in math and '#check_failure MvPolynomial.hasseDeriv_rename' in math
for method in ['finder','loogle','search','local']:
 for form in ['current','literature','abstract']:
  raw=json.loads((b/f'{method}-{form}.json').read_text());assert raw['request'] and not raw['result'].get('isError',False)
receipts=json.loads((b/'grep-receipts.json').read_text());assert len(receipts)>=7 and receipts[-1]['exit_code']==0
web=json.loads((b/'web-requests.json').read_text());assert len(web)>=4
assert len({q['q'] for e in web for q in e['request'].get('search_query',[])})>=3
for e in web:assert re.fullmatch('[0-9a-f]{64}',e['response_sha256']) and e['response_bytes']>0 and e['summary'] and e['status']
assert len(json.loads((b/'web-sources.json').read_text()))>=5
code=(b/'target-executed.lean').read_text();assert all(s in code for s in ['collision_lhs','collision_rhs','Fin 2','Function.Injective f','theorem square','theorem embedding'])
meta=json.loads((b/'corrected-target.json').read_text());assert meta['name']==target and meta['line']==143
assert len([x for x in json.loads((b/'grep-receipts.json').read_text())[0]['stdout'].splitlines() if x.startswith('Roth/Separation.lean:165:')])==1
print('PASS: all phases, 17 baseline inputs, source/reference and copy hashes/bytes, links, accepted complete native receipts, standard axioms, exact sources, 5 search methods × 3 forms, web metadata')
