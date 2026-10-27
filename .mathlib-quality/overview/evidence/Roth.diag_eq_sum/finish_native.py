from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).parent;B=Path('/private/tmp/roth-overview');N='Roth.diag_eq_sum'
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected={'original':[N],'raw':['DiagSumRaw.generic','DiagSumRaw.existingExpansion'],'consumers':['MvPolynomial.DiagSumConsumers.abs_coeff_diag_le_replay','MvPolynomial.DiagSumConsumers.natDegree_diag_le_replay']};a=[]
for label in expected:
 tag='raw-accepted' if label=='raw' else label
 src=B/f'diag-sum-{tag}-executed.lean.txt';rec=B/f'diag-sum-{tag}-receipt.json'
 ds=f'native-{label}-executed.lean.txt';dr=f'native-{label}-success.json';shutil.copyfile(src,D/ds);shutil.copyfile(rec,D/dr)
 a.append(dict(label=label,source=ds,receipt=dr,source_sha256=sha(src),execution_path='virtual lean_run_code' if label=='raw' else '.lake/roth-overview-session/NextHasseChecks.lean',original_source_path=str(src),original_receipt_path=str(rec),expected_axiom_declarations=expected[label]))
rejected=[]
for tag,reason in [('raw','Missing explicit MvPolynomial.aeval_def bridge: existingExpansion using eval₂_eq had type mismatch; not accepted.'),('raw-clean','Proof corrected with aeval_def but longLine warning; not accepted as final clean evidence.')]:
 src=B/f'diag-sum-{tag}-executed.lean.txt';rec=B/f'diag-sum-{tag}-receipt.json';ds=f'rejected-{tag}-executed.lean.txt';dr=f'rejected-{tag}-receipt.json';shutil.copyfile(src,D/ds);shutil.copyfile(rec,D/dr)
 rejected.append(dict(accepted=False,source=ds,receipt=dr,source_sha256=sha(src),original_source_path=str(src),original_receipt_path=str(rec),reason=reason))
out('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=a,rejected=rejected,production_unchanged=True))
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
r=json.loads((D/'native-original-success.json').read_text())['result']['structuredContent'];t=next(x['message'] for x in nodes(r) if isinstance(x,dict) and x.get('message','').startswith('@Roth.diag_eq_sum :'))
out('native-type.json',dict(type=t.split(' : ',1)[1],source='native-original-success.json'))
out('callers.json',dict(declaration=N,named_count=2,explicit_occurrences=2,external_to_file_count=0,internal_use_count_excluding_declaring_file=0,source_definition=1,named_callers=[dict(name='Roth.abs_coeff_diag_le',file='Roth/CoeffNorm.lean',line=176,refactor='Replace first rw by show diag P = _ from generic evaluation expansion; full caller replay passed.'),dict(name='Roth.natDegree_diag_le',file='Roth/CoeffNorm.lean',line=185,refactor='Replace rw expansion by generic evaluation expansion; full caller replay passed.')],native_audit=dict(status='PASS',requested=293,present=293,values=293,unique=293,order='generated directly from tracked declaration-order.json; portable exact equality required',direct_consumers=['Roth.abs_coeff_diag_le','Roth.natDegree_diag_le']),inline_audit='No equivalent diagonal expansion re-derived elsewhere; eval₂ expansions elsewhere concern different evaluations. Source refs/direct proof consumers are not opaque kernel/simp transitive dependency closure.'))
print(t)
