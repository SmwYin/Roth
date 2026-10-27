#!/usr/bin/env python3
"""Freeze the completed assessment's exact artifacts; does not edit repository files."""
from pathlib import Path
import hashlib,json,re,shutil
D=Path(__file__).resolve().parent;T=D.parent.parent
N='Roth.derivative_aeval'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(D/n).write_text(json.dumps(v,indent=2)+'\n')
def native(rec):
 x=rec['result'];x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
for p in T.glob('derivative-aeval-*'):
 if p.is_file():shutil.copyfile(p,D/p.name)
accepted=[];rejected=[]
labels=['original','audit','raw','finite-support','no-tower','specialization','consumer','kaehler']
for label in labels:
 s=f'derivative-aeval-{label}-executed.lean.txt';r=f'derivative-aeval-{label}-receipt.json'
 assert (D/s).exists() and (D/r).exists(),label
 rec=json.loads((D/r).read_text());nr=native(rec);assert nr['success'] and not nr.get('partial',False)
 start=5365 if label=='original' else 5369 if label=='audit' else 1
 if label=='consumer':start=5689
 ds=nr.get('items',nr.get('diagnostics',[]))
 expected=[]
 for z in ds:
  if z.get('line',0)>=start:
   hit=re.match(r"'([^']+)' depends on axioms:",z.get('message',''))
   if hit:expected.append(hit.group(1))
 if label=='audit':expected=[]
 accepted.append(dict(label=label,source=s,source_sha256=sha(D/s),receipt=r,original_execution_request=rec['request'],execution_kind='persistent-disk' if 'file_path' in rec['request'] else 'run-code',native_region_start_line=start,expected_axiom_declarations=expected))
for p in sorted(D.glob('derivative-aeval-*-rejected-receipt.json')):
 r=p.name;s=r.replace('-receipt.json','-executed.lean.txt');rec=json.loads(p.read_text());nr=native(rec)
 ds=nr.get('items',nr.get('diagnostics',[]));fail=[z['message'] for z in ds if z.get('severity') in ['error','warning']]
 assert fail
 rejected.append(dict(label=r.removeprefix('derivative-aeval-').removesuffix('-receipt.json'),source=s,receipt=r,original_execution_request=rec['request'],reason='; '.join(fail)))
# The optional generic absence probe is recorded as a search outcome, never accepted proof evidence.
for p in sorted(D.glob('derivative-aeval-*absence*-receipt.json')):
 if p.name in {x['receipt'] for x in rejected}:continue
 r=p.name;s=r.replace('-receipt.json','-executed.lean.txt');rec=json.loads(p.read_text());ds=native(rec).get('diagnostics',native(rec).get('items',[]));fail=[z['message'] for z in ds if z.get('severity') in ['error','warning']]
 if fail:rejected.append(dict(label='absence',source=s,receipt=r,original_execution_request=rec['request'],reason='; '.join(fail)))
s=(D/'derivative-aeval-audit-executed.lean.txt').read_text();arr=re.search(r'let names : Array Lean.Name := #\[.*?\]',s,re.S).group(0)
(D/'canonical-audit-array.lean.txt').write_text(arr+'\n')
save('verification.json',dict(declaration=N,accepted=accepted,rejected=rejected,unresolved=[],production_unchanged=True,standard_axioms=['propext','Classical.choice','Quot.sound'],canonical_direct_consumers=['_private.Roth.GenWronskian.0.Roth.derivative_kronHasse_aux'],incomplete_native=[dict(receipt='derivative-aeval-consumer-partial-receipt.json',reason='Import/header reload returned partial elaboration; not accepted as proof success.')],notes=['Original/audit disk diagnostics contain historical info; freshness scoped to target native region.','Raw run-code returns diagnostics rather than items and has no partial field.','New generalization helpers are accepted new proofs, not existing mathlib replacement theorems.','No raised limits, axioms, sorry, unsafe or native_decide in accepted snippets.']))
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dst,sha256=sha(p),bytes=p.stat().st_size))
save('copy-manifest.json',dict(declaration=N,files=files))
print(f'Packaged {len(files)} artifacts, {len(accepted)} accepted native sources, {len(rejected)} rejected native attempts')
