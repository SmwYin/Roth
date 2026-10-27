from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).parent;B=Path('/private/tmp/roth-overview');N='Roth.normOne_hasseDeriv_le'
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
expected={'original':[N,'MvPolynomial.NormHasseAssessment.replay'],'generic':['MvPolynomial.NormHasseGeneric.'+x for x in ['size_add','size_sum','size_monomial','scalarBound','bound','specialization']],'raw':['NormHasseRaw.finiteMonomialBound'],'consumers':['MvPolynomial.NormHasseConsumers.determinant_replay']}
a=[]
for label in expected:
 src=B/f'norm-hasse-{label}-executed.lean.txt';rec=B/f'norm-hasse-{label}-receipt.json'
 ds=f'native-{label}-executed.lean.txt';dr=f'native-{label}-success.json';shutil.copyfile(src,D/ds);shutil.copyfile(rec,D/dr)
 a.append(dict(label=label,source=ds,receipt=dr,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),execution_path='virtual lean_run_code' if label=='raw' else '.lake/roth-overview-session/NextHasseChecks.lean',original_source_path=str(src),original_receipt_path=str(rec),expected_axiom_declarations=expected[label]))
out('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=a,rejected=[],production_unchanged=True))
# Actual executed snippets are authoritative; preserve exact preparation separately.
s=(D/'native-generic-executed.lean.txt').read_text();start=s.rindex('namespace MvPolynomial.NormHasseGeneric');(D/'accepted-generic-snippet.lean.txt').write_text(s[start:])
r=json.loads((D/'native-original-success.json').read_text())['result']['structuredContent'];r=r.get('result',r);items=r['items'];t=next(x['message'] for x in items if x['message'].startswith('@normOne_hasseDeriv_le :'))
out('native-type.json',dict(type=t.split(' : ',1)[1],source='native-original-success.json'))
out('callers.json',dict(declaration=N,named_count=1,explicit_occurrences=1,documentation_occurrences=1,source_definition=1,named_callers=[dict(name='Roth.abs_coeff_det_hasseDeriv_le',file='Roth/CoeffNorm.lean',line=269,refactor='Replace with specialization of generic coefficient seminorm sum bound; full proof replay passed')],native_audit=dict(status='PASS',requested=293,present=293,values=293,unique=293,order='generated directly from tracked declaration-order.json; portable comparison required',direct_consumers=['Roth.abs_coeff_det_hasseDeriv_le']),inline_audit='No other direct uses; project has coefficient Hasse bounds which are different sup estimates; source occurrences are not opaque closure'))
print(t)
