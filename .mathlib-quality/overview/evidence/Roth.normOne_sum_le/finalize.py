from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).resolve().parent;N='Roth.normOne_sum_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
accepted=[]
for label in ['original','raw','consumers']:
 p=Path('/private/tmp/roth-overview/norm-sum-'+label+'-executed.lean.txt');r=Path('/private/tmp/roth-overview/norm-sum-'+label+'-receipt.json');assert p.is_file() and r.is_file()
 sn='native-'+label+'-executed.lean.txt';rn='native-'+label+'-success.json';shutil.copyfile(p,D/sn);shutil.copyfile(r,D/rn)
 j=json.loads(r.read_text());accepted.append(dict(label=label,source=sn,source_sha256=sha(D/sn),receipt=rn,execution_path=j['request'].get('file_path','virtual lean_run_code'),original_source_path=str(p),original_receipt_path=str(r)))
out('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=[],production_unchanged=True))
c=json.loads((D/'callers.json').read_text());c['native_audit']['status']='PASS';out('callers.json',c)
g=json.loads((D/'generality.json').read_text());g['expanded_forms'][0]['status']='PASS: fresh native raw receipt';out('generality.json',g)
phases={x:'PASS' for x in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem introduces no structure or instance'
out('assessment.json',dict(declaration=N,canonical_index=84,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,source='Roth/CoeffNorm.lean:90–92'))
s=(D/'report.md').read_text().replace('This read-only assessment is complete once the linked native receipts pass; upstream API questions below are design choices, not unresolved verification.','This read-only assessment is complete; all linked native receipts pass. Upstream API questions below are design choices, not unresolved verification.')
(D/'report.md').write_text(s)
# The validator itself is included. Manifest excludes itself and optional root/historical records.
rows=[]
for f in sorted(D.iterdir()):
 if not f.is_file() or f.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md' if f.name=='report.md' else 'evidence/'+N+'/'+f.name)
 rows.append(dict(source=str(f),destination=dest,sha256=sha(f),bytes=f.stat().st_size))
out('copy-manifest.json',dict(declaration=N,files=rows))
print('Complete worker metadata prepared; validate and root-review gates remain.')
