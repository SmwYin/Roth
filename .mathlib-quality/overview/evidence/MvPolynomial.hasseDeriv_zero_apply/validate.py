"""Portable read-only package checks: scratch or integrated evidence directory."""
import pathlib,sys,json,hashlib,re
base=pathlib.Path(__file__).resolve().parent
target='MvPolynomial.hasseDeriv_zero_apply'
root=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
assert (root/'lakefile.toml').is_file(),'Run from project root or pass root'
report=base/'report.md'
if not report.is_file():report=root/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
a=json.loads((base/'assessment.json').read_text())
assert a['completed'] and not a['unresolved'] and a['root_acceptance'] in ['pending','PASS']
assert all(v=='PASS' or v.startswith('N/A:') for v in a['phases'].values())
assert a['category']=='BORDERLINE-needs-human' and 0<len(a['upstream_design_questions'])<=5
for name,d in json.loads((base/'input-manifest.json').read_text())['sources_and_pins'].items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==d['sha256'],name
for e in json.loads((base/'copy-manifest.json').read_text())['files']:
 p=report if e['source']=='report.md' else base/e['source']
 data=p.read_bytes();assert len(data)==e['bytes'] and hashlib.sha256(data).hexdigest()==e['sha256'],str(p)
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('https:','http:')):continue
 prefix='../evidence/'+target+'/'
 p=base/link[len(prefix):] if link.startswith(prefix) else report.parent/link
 assert p.is_file(),link
v=json.loads((base/'verification.json').read_text())
assert not v['unresolved']
for entry in v['accepted']:
 raw=json.loads((base/entry['receipt']).read_text());native=raw.get('result',raw)
 assert not native.get('isError',False)
 sc=native.get('structuredContent',native);r=sc.get('result',sc)
 assert r['success'] and not r.get('partial') and not r.get('timed_out') and not r.get('failed_dependencies')
 assert not [x for x in r.get('items',r.get('diagnostics',[])) if x.get('severity')=='error']
 code=(base/entry['source']).read_text()
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code),entry['source']
for name in ['finder-current','finder-abstract','loogle-current','loogle-abstract','search-current','search-abstract','local-current','local-abstract']:
 raw=json.loads((base/(name+'.json')).read_text());assert not raw['result'].get('isError',False),name
web=json.loads((base/'web-requests.json').read_text());assert len(web)>=5
queries=[x['q'] for r in web for x in r['request'].get('search_query',[])]
assert len(set(queries))>=3
for r in web:
 assert re.fullmatch('[0-9a-f]{64}',r['response_sha256']) and r['response_bytes']>0 and r['summary']
assert 'import Roth' not in (base/'mathlib-executed.lean').read_text()
assert '#check_failure MvPolynomial.hasseDeriv_zero_apply' in (base/'mathlib-executed.lean').read_text()
print('PASS: complete phases, no unresolved checks, accepted native receipts, source/pin hashes, copy hashes/bytes, report links, five search methods and web metadata')
