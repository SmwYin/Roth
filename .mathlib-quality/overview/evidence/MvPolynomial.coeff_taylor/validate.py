#!/usr/bin/env python3
"""Read-only validation of scratch or integrated coeff_taylor evidence."""
from pathlib import Path
import hashlib,json,re,sys
base=Path(__file__).resolve().parent
q='MvPolynomial.coeff_taylor'
def load(name):return json.loads((base/name).read_text())
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def report_path():
 if (base/'report.md').exists():return base/'report.md'
 return base.parent.parent/'mathlibable'/f'{q}.md'
def resolve(dest):
 prefix=f'.mathlib-quality/overview/evidence/{q}/'
 if dest.startswith(prefix):return base/dest[len(prefix):]
 assert dest==f'.mathlib-quality/overview/mathlibable/{q}.md',dest
 return report_path()
manifest=load('copy-manifest.json')
entries=manifest['files'] if isinstance(manifest,dict) else manifest
for item in entries:
 f=resolve(item['destination']);assert f.is_file(),str(f)
 assert f.stat().st_size==item['bytes'],f'byte mismatch {f}'
 assert digest(f)==item['sha256'],f'hash mismatch {f}'
a=load('assessment.json');assert a['declaration']==q and a['completed'] is True
assert a['verdict']=='YES-add-as-is' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS']
required=['0','1','2','3','4','4c','4.5','4.6','5','5.5','6','7','8']
assert set(a['phases'])==set(required)
for k,v in a['phases'].items():
 assert v['status']=='PASS' or (v['status']=='n/a' and v.get('reason')),(k,v)
# Unwrap native structured content without treating partial/warming responses as success.
def native(name):
 r=load(name)['result'];assert not r.get('isError',False),name
 d=r.get('structuredContent')
 if d is None:d=json.loads(next(x['text'] for x in r['content'] if x['type']=='text'))
 while isinstance(d,dict) and set(d)=={'result'}:d=d['result']
 return d
v=load('verification.json');allowed=set(v['axioms_allowlist'])
for record in v['accepted_native']:
 src=base/record['source'];assert digest(src)==record['source_sha256']
 d=native(record['receipt']);assert d.get('success') is True,record
 assert d.get('partial',False) is False and d.get('timed_out',False) is False
 assert not d.get('failed_dependencies',[])
 items=d.get('items',d.get('diagnostics',[]))
 assert all(x.get('severity') not in ['error','warning'] for x in items),record
 msgs='\n'.join(x.get('message','') for x in items)
 assert 'sorryAx' not in msgs
 for decl in record['declarations']:
  matches=[x.get('message','') for x in items if f"'{decl}' depends on axioms:" in x.get('message','')]
  assert matches,decl
  for msg in matches:
   axioms=msg.split('depends on axioms:',1)[1].strip().strip('[]')
   assert set(t.strip() for t in axioms.split(',') if t.strip())<=allowed,(decl,axioms)
  assert decl.rsplit('.',1)[-1] in src.read_text(),decl
 request=load(record['receipt'])['request']
 if 'code' in request:assert request['code']==src.read_text(),'exact executed virtual code mismatch'
 else:assert request['file_path']==record['original_execution_path']
# Successful independent proof must not directly call the original target.
d=native('native-target-success.json');messages=[x.get('message','') for x in d['items']]
constants=next(x for x in messages if x.startswith('COEFF_TAYLOR_CONSTANTS:'))
assert 'MvPolynomial.coeff_taylor,' not in constants
assert 'MvPolynomial.PrivateTaylorMonomialAssessment.replay' in constants
# Rejected final composition is intentionally not accepted theorem evidence.
d=native(v['composition_final']['receipt']);assert d['success'] is False and not d.get('timed_out',False)
errors=[x for x in d['diagnostics'] if x.get('severity')=='error'];assert len(errors)==2
assert any('unsolved goals' in x['message'] for x in errors)
assert any('exact?' in x['message'] and 'could not close' in x['message'] for x in errors)
assert load(v['composition_final']['receipt'])['request']['code']==(base/v['composition_final']['source']).read_text()
# Locate real project from cwd or integrated ancestry; scratch does not hard-code a workspace.
candidates=[Path.cwd(),*Path.cwd().parents,*base.parents]
project=next((x for x in candidates if (x/'Roth/Taylor.lean').is_file()),None)
assert project is not None,'run from the Roth project or integrated evidence directory'
m=load('inputs.json');assert len(m['sources_and_pins'])==17
for rel,expect in m['sources_and_pins'].items():assert digest(project/rel)==expect['sha256'],rel
for item in load('mathlib-inputs.json'):
 f=project/item['path'];assert digest(f)==item['sha256'] and f.stat().st_size==item['bytes']
assert load('input-hash-check.json')['all_match'] is True
progress=json.loads((project/'.mathlib-quality/overview/progress.json').read_text())
current={x['declaration']:x for x in progress['completed_declarations']}
for item in load('accepted-grouping.json'):
 assert item['declaration'] in current
 assert item['verdict'].startswith('YES') and current[item['declaration']]['verdict']==item['verdict']
 assert current[item['declaration']].get('acceptance')=='PASS'
# Every method must have actually attempted all three forms, with raw response preserved.
for meth in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','literature','abstract']:
  d=load(f'search-{meth}-{form}.json');assert d['method']==meth and d['form']==form
  assert d['request'].get('query') and 'response' in d
for form in ['current','literature','abstract','full-name']:
 d=load(f'rg-{form}.json');assert d['request'][0]=='rg' and d['exit_code'] in [0,1]
# Curated web evidence contains exact requests and hashes, never full article/search bodies.
for f in base.glob('web-*.json'):
 d=json.loads(f.read_text());assert d['request'] and re.fullmatch('[0-9a-f]{64}',d['response_sha256'])
 assert d['response_bytes']>0 and 'response' not in d
text=report_path().read_text()
for target in re.findall(r'\]\(([^)]+)\)',text):
 if target.startswith('http'):continue
 prefix=f'../evidence/{q}/';assert target.startswith(prefix),target
 assert (base/target[len(prefix):]).is_file(),target
assert 'Phase 8' in text
print('PASS: portable hashes, all phases, exact native success/standard axioms, rejected composition, sources/pins, accepted grouping, 5×3 searches, metadata and links')
