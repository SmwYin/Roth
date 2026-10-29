"""Final postintegration formatting repair only; no assessment, proof or Git mutations."""
from pathlib import Path
import json,hashlib,shutil
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');F=R/'.mathlib-quality/overview/evidence/final'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
p=load(R/'.mathlib-quality/overview/progress.json');assert p['status']=='complete' and len(p['completed_declarations'])==293
ready=load(B/'final-readiness.json');root=load(B/'root-final-review.json');candidate=B/'FINAL_PROJECT_OVERVIEW_CANDIDATE.md';target=R/'PROJECT_OVERVIEW.md'
old=H(candidate);assert old==H(target)==ready['final_overview_sha256']==root['overview_sha256']
assert H(B/'root-final-review.json')==H(F/'root-final-review.json')
s=candidate.read_text();lines=s.splitlines(keepends=True);bad=[i for i,line in enumerate(lines)if line.rstrip('\n')!=line.rstrip('\n').rstrip(' \t')]
assert bad and all(lines[i]=='- **Notes**: \n'for i in bad)
new=s.replace('- **Notes**: \n','- **Notes**:\n');assert new.count('\n')==s.count('\n')
assert all(a==b or(a=='- **Notes**: 'and b=='- **Notes**:')for a,b in zip(s.splitlines(),new.splitlines()))
candidate.write_text(new);target.write_text(new);newhash=H(candidate)
note=dict(status='PASS',old_overview_sha256=old,new_overview_sha256=newhash,changed_line_count=len(bad),change='Remove trailing space only from empty generated Notes fields; no mathematical text or raw evidence changed.',script_sha256=H(Path(__file__)))
record=B/'final-overview-whitespace-repair.json';dump(record,note)
root['overview_sha256']=newhash;root['formatting_repair']=note;dump(B/'root-final-review.json',root)
ready['final_overview_sha256']=newhash
for x in ready['artifacts']:
 if x['source']==str(B/'root-final-review.json'):x['sha256']=H(B/'root-final-review.json')
for source in [Path(__file__).resolve(),record]:
 assert not any(x['source']==str(source)for x in ready['artifacts'])
 ready['artifacts'].append(dict(source=str(source),sha256=H(source)))
ready['postintegration_formatting_repair']=note;dump(B/'final-readiness.json',ready)
manifest=load(F/'copy-manifest.json')
for name in ['root-final-review.json','final-readiness.json',Path(__file__).name,record.name]:shutil.copyfile(B/name,F/name)
extra=manifest['readiness_support_artifacts']
for x in extra:
 if x['source']==str(B/'root-final-review.json'):x.update(sha256=H(F/'root-final-review.json'),bytes=(F/'root-final-review.json').stat().st_size)
for source in [Path(__file__).resolve(),record]:extra.append(dict(source=str(source),destination=str((F/source.name).relative_to(R)),sha256=H(source),bytes=source.stat().st_size))
manifest['postintegration_formatting_repair']=note;dump(F/'copy-manifest.json',manifest)
assert H(target)==ready['final_overview_sha256'] and H(F/'root-final-review.json')==H(B/'root-final-review.json')
for x in ready['artifacts']:assert H(Path(x['source']))==x['sha256']
for x in manifest['files']+manifest['readiness_support_artifacts']:assert H(R/x['destination'])==x['sha256']
print('PASS exact empty-Notes whitespace-only repair:',len(bad),'lines; overview/rootreview/readiness/copied manifest hashes synchronized; proofs/raw evidence unchanged')
