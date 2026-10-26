"""Read-only validation, from scratch or after integration. Run from the project root."""
import pathlib,json,hashlib,re
base=pathlib.Path(__file__).resolve().parent
target='MvPolynomial.coeff_hasseDeriv'
root=next((p for p in [pathlib.Path.cwd(),*base.parents] if (p/'lakefile.toml').is_file()),None)
assert root,'Run from project root'
report=base/'report.md'
if not report.is_file():report=root/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
a=json.loads((base/'assessment.json').read_text());assert a['completed'] and not a['unresolved']
for name,r in json.loads((base/'evidence/input-manifest.json').read_text())['sources_and_pins'].items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==r['sha256'],name
for r in json.loads((base/'copy-manifest.json').read_text())['files']:
 p=report if r['source']=='report.md' else base/r['source']
 assert p.is_file(),str(p)
 data=p.read_bytes();assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],str(p)
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('https:','http:')):continue
 prefix='../evidence/'+target+'/'
 p=base/link[len(prefix):] if link.startswith(prefix) else (report.parent/link).resolve()
 assert p.is_file(),link
for name in ['target','shape','mathlib','route']:
 raw=json.loads((base/'evidence'/(name+'-lsp.json')).read_text())['result']
 assert not raw.get('isError')
 sc=raw['structuredContent']; r=sc.get('result',sc); assert r['success'] and not r.get('partial') and not r.get('timed_out') and not r.get('failed_dependencies')
 assert not [i for i in r.get('items',r.get('diagnostics',[])) if i.get('severity')=='error']
print('PASS: completed assessment, source/pin hashes, all copy hashes/byte counts, report links, native gates')
