#!/usr/bin/env python3
"""Read-only verification of current scratch or integrated package; no native tool invocation."""
import argparse,hashlib,json,re
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path);args=parser.parse_args()
base=Path(__file__).resolve().parent
repo=args.repo or next((p for p in [Path.cwd(),*base.parents] if (p/'lakefile.toml').exists()),None)
assert repo is not None,'Pass --repo';repo=repo.resolve()
load=lambda f:json.loads((base/f).read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
a=load('assessment.json');name='Roth.det_choose_eq'
assert a['declaration']==name and a['canonical']==43
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases and set(a['phases'].values())=={'PASS'}
v=load('verification.json');assert v['unresolved']==[]
assert {'target','factorial','ring'} <= {x['label'] for x in v['accepted']}
for e in v['accepted']:
 source=base/e['source'];code=source.read_text();assert sha(source.read_bytes())==e['source_sha256']
 r=load(e['receipt']);assert not r['result'].get('isError',False)
 d=r['result']['structuredContent']
 while 'result' in d:d=d['result']
 assert d.get('success') is True and not d.get('partial',False) and not d.get('timed_out',False)
 assert not d.get('failed_dependencies',[])
 ds=d.get('items',d.get('diagnostics',[]));assert not [x for x in ds if x.get('severity') in ['warning','error']]
 ax=[x['message'] for x in ds if 'depends on axioms:' in x.get('message','')];assert ax
 for m in ax:
  hit=re.search(r'depends on axioms: \[([^\]]*)\]',m);assert hit
  assert {x.strip() for x in hit[1].split(',') if x.strip()}<=set(v['standard_axioms'])
 assert not re.search(r'\b(sorry|unsafe|native_decide|axiom)\b',code)
 assert not re.search(r'set_option\s+(maxHeartbeats|maxRecDepth)',code)
 if 'code' in r['request']:
  assert code==r['request']['code']
  assert '#check_failure Roth.det_choose_eq' in code
  assert not re.search(r'^import Roth',code,re.M)
inputs=load(v['inputs']);assert len(inputs)==17
for x in inputs:
 b=(repo/x['path']).read_bytes();assert x['match'] and sha(b)==x['sha256']==x['baseline_sha256'] and len(b)==x['bytes']
for x in load(v['mathlib_inputs']):
 b=(repo/x['path']).read_bytes();assert sha(b)==x['sha256'] and len(b)==x['bytes']
for src,arch in v['source_links'].items():assert (repo/src).read_bytes()==(base/arch).read_bytes()
for form in ['current','literature','abstract']:
 f=load(f'formal-{form}.json');assert len(f['requests'])==4 and len(f['results'])==4
 for x in f['results']:assert x['status']=='fulfilled' and not x['value'].get('isError',False)
 r=load(f'rg-{form}.json');assert r['exit_code'] in [0,1] and not r['stderr']
lit=load('literature.json');assert len(lit)>=10
assert len(load('webgeneral-metadata.json')['queries'])>=3
for file in v['web_metadata']:
 d=load(file);assert re.fullmatch('[0-9a-f]{64}',d['response_sha256']) and d['response_bytes']>0 and d['body_persisted'] is False
manifest=load('copy-manifest.json');assert manifest['declaration']==name
seen=set()
for x in manifest['files']:
 f=base/Path(x['source']).name
 if not f.exists() and x['destination'].endswith(f'mathlibable/{name}.md'):f=repo/x['destination']
 assert f.exists(),str(f)
 b=f.read_bytes();assert sha(b)==x['sha256'] and len(b)==x['bytes'],f.name
 seen.add(f.resolve())
expected={f.resolve() for f in base.iterdir() if f.is_file() and f.name not in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']}
assert expected<=seen,'Artifacts omitted from current manifest'
report=base/'report.md'
if not report.exists():report=repo/f'.mathlib-quality/overview/mathlibable/{name}.md'
s=report.read_text();prefix=f'../evidence/{name}/'
for target in re.findall(r'\]\(([^)]+)\)',s):
 if target.startswith('https://'):continue
 assert target.startswith(prefix),target
 assert (base/target[len(prefix):]).is_file(),target
assert 'Build completed successfully (2467 jobs)' in (base/'baseline-build.txt').read_text()
assert load('overview-entry.json')['type'].startswith('∀')
print(json.dumps(dict(declaration=name,status='PASS',native_accepted=len(v['accepted']),phase_count=len(phases),manifest_files=len(manifest['files']),unresolved=[]),indent=2))
