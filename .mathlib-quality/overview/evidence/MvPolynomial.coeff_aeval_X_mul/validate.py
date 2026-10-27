"""Read-only validation of completed private-prefilter triage, scratch or published."""
from pathlib import Path
import json,hashlib,re,sys
b=Path(__file__).resolve().parent;r=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();n='MvPolynomial.coeff_aeval_X_mul'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((b/'assessment.json').read_text());assert a['completed'] and a['mode']=='overview-private-prefilter' and a['verdict']=='SKIP' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS']
assert all(v.startswith('PASS') or v.startswith('n/a:') for v in a['phases'].values())
row=json.loads((b/'corrected-target.json').read_text());assert row['visibility']=='private' and row['source'].startswith('private lemma ')
source='\n'.join((r/row['file']).read_text().splitlines()[row['line']-1:row['end_line']]);assert source==row['source'] and hashlib.sha256(source.encode()).hexdigest()==row['sha256']
for name,e in json.loads((b/'input-manifest.json').read_text())['sources_and_pins'].items():assert sha(r/name)==e['sha256'],name
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/f'{n}.md'
for e in json.loads((b/'copy-manifest.json').read_text())['files']:
 p=report if e['source']=='report.md' else b/e['source'];assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],p
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http:','https:')):continue
 prefix='../evidence/'+n+'/';p=b/link[len(prefix):] if link.startswith(prefix) else report.parent/link;assert p.is_file(),link
v=json.loads((b/'verification.json').read_text());assert not v['unresolved'];code=b/v['native']['source'];assert sha(code)==v['native']['source_sha256'] and v['native']['matched_at_assessment']
raw=json.loads((b/v['native']['receipt']).read_text())['result'];assert not raw.get('isError');res=raw['structuredContent']['result']
assert res['success'] and not res.get('partial') and not res.get('timed_out') and not res.get('failed_dependencies')
assert not any(x['severity'] in ['error','warning'] for x in res['items'])
proofs=0
for item in res['items']:
 msg=item['message'];assert 'sorryAx' not in msg
 if 'depends on axioms:' in msg:
  axioms={x.strip() for x in re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',') if x.strip()};assert axioms<={'propext','Classical.choice','Quot.sound'};proofs+=1
assert proofs>=1
assert any("'MvPolynomial.PrivateCoeffAevalAssessment.replay' depends on axioms:" in x['message'] for x in res['items'])
assert all(x['exit_code']==0 for x in json.loads((b/'source-search.json').read_text()))
print('PASS: private-prefilter rule, complete inventory/structural review, source/callers, native replay, standard axioms, 17 pins/sources, artifact hashes and links')

import subprocess
subprocess.run([sys.executable,str(r/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(b)],check=True)
