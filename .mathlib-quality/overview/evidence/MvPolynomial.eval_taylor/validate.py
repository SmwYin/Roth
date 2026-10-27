#!/usr/bin/env python3
"""Portable read-only scratch/integrated assessment validator; current manifest authoritative."""
from pathlib import Path
import hashlib,json,re
base=Path(__file__).resolve().parent
q='MvPolynomial.eval_taylor'
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
manifest=load('copy-manifest.json');entries=manifest['files'] if isinstance(manifest,dict) else manifest
for item in entries:
 f=resolve(item['destination']);assert f.is_file(),str(f)
 assert f.stat().st_size==item['bytes'],f'byte mismatch {f}'
 assert digest(f)==item['sha256'],f'hash mismatch {f}'
a=load('assessment.json');assert a['declaration']==q and a['completed'] is True
assert a['verdict']=='BORDERLINE-needs-human' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS']
assert 1<=len(a['questions'])<=5
required=['0','1','2','3','4','4c','4.5','4.6','5','5.5','6','7','8'];assert set(a['phases'])==set(required)
for k,v in a['phases'].items():
 if isinstance(v,str):assert v=='PASS' or v.startswith('n/a:'),(k,v)
 else:assert v['status']=='PASS' or (v['status']=='n/a' and v.get('reason')),(k,v)
def unwrap(r):
 assert not r.get('isError',False)
 d=r.get('structuredContent')
 if d is None:d=json.loads(next(x['text'] for x in r['content'] if x['type']=='text'))
 while isinstance(d,dict) and set(d)=={'result'}:d=d['result']
 return d
def native(name):return unwrap(load(name)['result'])
v=load('verification.json');allowed=set(v['axioms_allowlist'])
for record in v['accepted_native']:
 src=base/record['source'];assert digest(src)==record['source_sha256']
 d=native(record['receipt']);assert d.get('success') is True,record
 assert d.get('partial',False) is False and d.get('timed_out',False) is False
 assert not d.get('failed_dependencies',[])
 items=d.get('items',d.get('diagnostics',[]))
 assert all(x.get('severity') not in ['error','warning'] for x in items),record
 msgs='\n'.join(x.get('message','') for x in items);assert 'sorryAx' not in msgs
 for decl in record['declarations']:
  matches=[x.get('message','') for x in items if f"'{decl}' depends on axioms:" in x.get('message','')]
  assert matches,decl
  for msg in matches:
   axioms=msg.split('depends on axioms:',1)[1].strip().strip('[]')
   assert set(t.strip() for t in axioms.split(',') if t.strip())<=allowed,(decl,axioms)
  assert decl.rsplit('.',1)[-1] in src.read_text(),decl
 request=load(record['receipt'])['request']
 if 'code' in request:assert request['code']==src.read_text(),'exact executed code mismatch'
 else:assert request['file_path']==record['original_execution_path']
 if record['receipt']!='native-target-success.json':
  assert 'import Roth' not in src.read_text()
  assert '#check_failure MvPolynomial.eval_taylor' in src.read_text()
# Every rejected experiment is excluded from accepted_native.
for name in ['native-raw-rejected.json','native-raw-second-rejected.json']:
 d=native(name);assert d['success'] is False
 assert any(x.get('severity')=='error' for x in d.get('diagnostics',d.get('items',[])))
 assert load(name)['request']['code']==(base/name.replace('.json','.lean.txt')).read_text()
# Native target replay does not call itself or use a downstream Taylor law.
replay=(base/'native-target-executed.lean.txt').read_text().split('namespace MvPolynomial.EvalTaylorAssessment',1)[1]
body=replay.split('theorem replay',1)[1].split('#print axioms',1)[0]
assert 'eval_taylor' not in body and 'coeff_taylor' not in body
assert '← eval_assoc' in body
# Locate real project without a hard-coded workspace.
candidates=[Path.cwd(),*Path.cwd().parents,*base.parents]
project=next((x for x in candidates if (x/'Roth/Taylor.lean').is_file()),None)
assert project is not None,'run from the Roth project or an integrated evidence directory'
m=load('inputs.json');assert len(m['sources_and_pins'])==17
for rel,expect in m['sources_and_pins'].items():assert digest(project/rel)==expect['sha256'],rel
for item in load('mathlib-inputs.json'):
 f=project/item['path'];assert digest(f)==item['sha256'] and f.stat().st_size==item['bytes']
assert load('input-hash-check.json')['all_match'] is True
# Honest named source refs, separately filtered native reference locations.
refs=native('native-references.json');assert refs['total']==5
production=[x for x in refs['items'] if not x['file_path'].startswith('.lake/') and not (x['file_path']=='Roth/Taylor.lean' and x['line']==141)]
assert production==[]
assert load('callers.json')['named_occurrences_excluding_definition']==0
for meth in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','literature','abstract']:
  d=load(f'search-{meth}-{form}.json');assert d['method']==meth and d['form']==form
  assert d['request'].get('query') and 'response' in d
for form in ['current','literature','abstract','full-name','callers','inline']:
 d=load(f'rg-{form}.json');assert d['request'][0]=='rg' and d['exit_code'] in [0,1]
for f in base.glob('web-*.json'):
 d=json.loads(f.read_text());assert d['request'] and re.fullmatch('[0-9a-f]{64}',d['response_sha256'])
 assert d['response_bytes']>0 and 'response' not in d and d.get('summary')
assert len(load('web-0.json')['request']['search_query'])>=3
assert set(['N','C','S','O','A','P'])<=set(f.stem[4:] for f in base.glob('web-*.json'))
progress=json.loads((project/'.mathlib-quality/overview/progress.json').read_text())
current={x['declaration']:x for x in progress['completed_declarations']}
for item in load('accepted-grouping.json'):
 assert current[item['declaration']]['verdict']==item['verdict'] and item['verdict'].startswith('YES')
 assert current[item['declaration']].get('acceptance')=='PASS'
e=load('overview-entry.json');assert e['type'].startswith('∀') and e['kind']=='theorem'
text=report_path().read_text()
for target in re.findall(r'\]\(([^)]+)\)',text):
 if target.startswith('http'):continue
 prefix=f'../evidence/{q}/';assert target.startswith(prefix),target
 assert (base/target[len(prefix):]).is_file(),target
assert 'Phase 8' in text
print('PASS: current manifest, exact native success, standard axioms, all phases, source/pins, 5×3 methods, web metadata, zero production refs, portable links')
