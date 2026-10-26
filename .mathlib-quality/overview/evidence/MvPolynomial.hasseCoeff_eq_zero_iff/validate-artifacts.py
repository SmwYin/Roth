"""Validate scratch or integrated report links and hashed copy entries."""
from pathlib import Path
import hashlib,json,re
base=Path(__file__).resolve().parent
name='MvPolynomial.hasseCoeff_eq_zero_iff'
scratch=(base/'report.md').is_file()
report=base/'report.md' if scratch else base.parents[1]/'mathlibable'/f'{name}.md'
# Bootstrap only these two generated outputs before checking report self-links.
if scratch:
 for generated in ['evidence/report-links.json', 'copy-manifest.json']:
  if not (base/generated).is_file(): (base/generated).write_text('[]\n')
links=[]
for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',report.read_text()):
 if target.startswith(('http:','https:')):continue
 prefix='../evidence/'+name+'/'
 assert target.startswith(prefix),(label,target)
 local=base/target[len(prefix):]
 links.append(dict(label=label,target=target,exists=local.is_file()))
assert all(x['exists'] for x in links),links
if scratch:
 (base/'evidence/report-links.json').write_text(json.dumps(links,indent=2))
 copy=[]
 for file in sorted(base.rglob('*')):
  if not file.is_file() or file.name=='copy-manifest.json':continue
  rel=file.relative_to(base)
  destination=('.mathlib-quality/overview/mathlibable/'+name+'.md' if str(rel)=='report.md' else '.mathlib-quality/overview/evidence/'+name+'/'+str(rel))
  copy.append(dict(source=str(rel),destination=destination,sha256=hashlib.sha256(file.read_bytes()).hexdigest(),bytes=file.stat().st_size))
 (base/'copy-manifest.json').write_text(json.dumps(copy,indent=2))
else:
 copy=json.loads((base/'copy-manifest.json').read_text())
 repo=base.parents[3]
 for entry in copy:
  file=repo/entry['destination']
  assert file.is_file(),str(file)
  assert hashlib.sha256(file.read_bytes()).hexdigest()==entry['sha256'],str(file)
print(f'{len(links)} report links verified; {len(copy)} hashed copy entries.')
