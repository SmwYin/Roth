#!/usr/bin/env python3
"""Portable read-only validator of the current manifest in scratch/integrated layout."""
from pathlib import Path
import argparse,json,hashlib,re
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path);args=ap.parse_args()
p=Path(__file__).resolve().parent
repo=args.repo or next((q for q in [Path.cwd(),*p.parents] if (q/'lakefile.toml').is_file()),None)
assert repo is not None,'Pass --repo';repo=repo.resolve();name='Roth.coeff_wronskian_of_natDegree_injective'
load=lambda f:json.loads((p/f).read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
a=load('assessment.json');assert a['declaration']==name and a['canonical']==46 and a['completed'] and a['allphases']=='PASS' and not a['unresolved']
assert a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and set(a['phases'].values())=={'PASS'}
v=load('verification.json');assert not v['unresolved'] and {x['label'] for x in v['accepted']}=={'target','ring','finite','caller'}
for e in v['accepted']:
 source=p/e['source'];code=source.read_text();assert sha(source.read_bytes())==e['source_sha256']
 r=load(e['receipt']);assert not r['result'].get('isError',False);d=r['result']['structuredContent']
 while 'result' in d:d=d['result']
 assert d.get('success') is True and not d.get('partial',False) and not d.get('timed_out',False) and not d.get('failed_dependencies',[])
 ds=d.get('diagnostics',d.get('items',[]));assert not [x for x in ds if x.get('severity') in ['error','warning']]
 ax=[x['message'] for x in ds if 'depends on axioms:' in x.get('message','')];assert ax
 for s in ax:
  m=re.search(r'depends on axioms: \[([^\]]*)\]',s);assert m
  assert {x.strip() for x in m[1].split(',') if x.strip()}<=set(v['standard_axioms'])
 assert not re.search(r'\b(sorry|unsafe|native_decide|axiom)\b',code)
 assert not re.search(r'set_option\s+(maxHeartbeats|maxRecDepth)',code)
 if 'code' in r['request']:
  assert code==r['request']['code'] and '#check_failure Roth.coeff_wronskian_of_natDegree_injective' in code
  assert not re.search(r'^import Roth',code,re.M)
for x in load(v['inputs']):
 b=(repo/x['path']).read_bytes();assert x['match'] and sha(b)==x['sha256']==x['baseline_sha256'] and len(b)==x['bytes']
assert len(load(v['inputs']))==17
for x in load(v['mathlib_inputs']):
 b=(repo/x['path']).read_bytes();assert sha(b)==x['sha256'] and len(b)==x['bytes']
for src,archive in v['source_links'].items():assert (repo/src).read_bytes()==(p/archive).read_bytes()
for form in ['current','literature','abstract']:
 f=load('formal-'+form+'.json');assert len(f['requests'])==4
 for method in ['Finder','Loogle','LeanSearch','local']:
  assert not f[method].get('isError',False) and 'content' in f[method]
 r=load('rg-'+form+'.json');assert r['exit_code'] in [0,1] and not r['stderr']
assert len(load('literature.json'))>=10
assert len(load('web-general-metadata.json')['request']['search_query'])>=3
for file in v['web_metadata']:
 d=load(file);assert re.fullmatch('[0-9a-f]{64}',d['response_sha256']) and d['response_bytes']>0 and d['body_persisted'] is False
manifest=load('copy-manifest.json');assert manifest['declaration']==name;seen=set()
for x in manifest['files']:
 f=p/Path(x['source']).name
 if not f.exists() and x['destination'].endswith('/'+name+'.md'):f=repo/x['destination']
 assert f.is_file(),str(f);b=f.read_bytes();assert sha(b)==x['sha256'] and len(b)==x['bytes'],f.name;seen.add(f.resolve())
expected={f.resolve() for f in p.iterdir() if f.is_file() and f.name not in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']}
assert expected<=seen,'Current manifest omits artifacts'
report=p/'report.md'
if not report.exists():report=repo/f'.mathlib-quality/overview/mathlibable/{name}.md'
text=report.read_text();prefix=f'../evidence/{name}/'
for link in re.findall(r'\]\(([^)]+)\)',text):
 if link.startswith('https://'):continue
 assert link.startswith(prefix),link;assert (p/link[len(prefix):]).is_file(),link
assert load('overview-entry.json')['type'].startswith('∀')
assert 'Build completed successfully (2467 jobs)' in (p/'baseline-build.txt').read_text()
assert load('secret-scan-receipt.json')['result']['exit_code']==0
print(json.dumps(dict(declaration=name,status='PASS',accepted_native=len(v['accepted']),manifest_files=len(manifest['files']),phases=len(a['phases']),unresolved=[]),indent=2))
