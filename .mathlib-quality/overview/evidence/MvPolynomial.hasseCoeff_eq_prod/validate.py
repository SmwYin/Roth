"""Read-only portable acceptance checks; run from project root or pass root path."""
import pathlib,sys,json,hashlib,re
base=pathlib.Path(__file__).resolve().parent
target='MvPolynomial.hasseCoeff_eq_prod'
root=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
assert (root/'lakefile.toml').is_file(),'Run from project root or pass it explicitly'
report=base/'report.md'
if not report.is_file():report=root/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
a=json.loads((base/'assessment.json').read_text())
assert a['completed'] and not a['unresolved'] and a['root_acceptance'] in ['pending','PASS']
assert all(v=='PASS' or v.startswith('N/A:') for v in a['phases'].values())
for name,d in json.loads((base/'input-manifest.json').read_text())['sources_and_pins'].items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==d['sha256'],name
for entry in json.loads((base/'copy-manifest.json').read_text())['files']:
 p=report if entry['source']=='report.md' else base/entry['source']
 data=p.read_bytes();assert len(data)==entry['bytes'] and hashlib.sha256(data).hexdigest()==entry['sha256'],str(p)
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('https:','http:')):continue
 prefix='../evidence/'+target+'/'
 p=base/link[len(prefix):] if link.startswith(prefix) else report.parent/link
 assert p.is_file(),link
v=json.loads((base/'verification.json').read_text())
for item in v['accepted']:
 raw=json.loads((base/item['receipt']).read_text())
 native=raw.get('result',raw);assert not native.get('isError',False)
 sc=native.get('structuredContent',native);res=sc.get('result',sc)
 assert res['success'] and not res.get('partial') and not res.get('timed_out') and not res.get('failed_dependencies')
 assert not [x for x in res.get('items',res.get('diagnostics',[])) if x.get('severity')=='error']
 code=(base/item['source']).read_text()
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code),item['source']
for name in ['finder-current','finder-abstract','loogle-current','loogle-abstract','search-current','search-abstract','local-current','local-abstract']:
 assert (base/(name+'.json')).is_file()
assert len(json.loads((base/'web-requests.json').read_text()))>=5
print('PASS: all phases, accepted native receipts, source/pin hashes, report links, copy hashes/bytes, search artifacts')
