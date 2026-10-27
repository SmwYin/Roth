from pathlib import Path
import shutil,json,hashlib,re
D=Path(__file__).parent;T=Path('/private/tmp/roth-overview')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
sets=[('original','norm-det-original',['Roth.normOne_det_le','MvPolynomial.NormDetAssessment.replay']),('raw','norm-det-raw',['NormDetRaw.genericDet']),('seminorm','norm-det-seminorm',['NormDetRaw.genericDet','NormDetRaw.seminormDet']),('consumers','norm-det-bundled-consumers-clean',['NormDetRaw.genericDet','NormDetRaw.seminormDet','MvPolynomial.NormDetPackaging.coeffSeminorm','MvPolynomial.NormDetPackaging.unitBound','MvPolynomial.NormDetRecovery.recover','MvPolynomial.NormDetConsumers.generalIndex','MvPolynomial.NormDetConsumers.finIndex','MvPolynomial.NormDetConsumers.determinant_inline'])]
a=[]
for label,stem,expected in sets:
 p=T/(stem+'-executed.lean.txt');r=T/(stem+'-receipt.json')
 sn=f'native-{label}-executed.lean.txt';rn=f'native-{label}-success.json'
 shutil.copyfile(p,D/sn);shutil.copyfile(r,D/rn);j=json.loads(r.read_text())
 a.append(dict(label=label,source=sn,receipt=rn,source_sha256=sha(D/sn),execution_path=j['request'].get('file_path','virtual lean_run_code'),original_source_path=str(p),original_receipt_path=str(r),expected_axiom_declarations=expected))
s=(D/'native-consumers-executed.lean.txt').read_text();arr=re.search(r'  let names : Array Lean.Name := #\[.*?\]\n',s,re.S).group();assert re.sub(r'\s','',arr)==re.sub(r'\s','',(D/'canonical-audit-array.lean.txt').read_text())
rej=[]
for label,src,receipt,why in [('warming','norm-det-bundled-consumers-executed.lean.txt','norm-det-bundled-consumers-receipt.json','Partial warming; not accepted validation.'),('failed','norm-det-bundled-consumers-executed.lean.txt','norm-det-bundled-consumers-complete-receipt.json','Original coefficient coercion and card_fin normalization failed; recovered sorryAx in rejected attempt. Corrected explicit coeffSeminorm_apply/card_fin simplifications and typed finIndex helper.')]:
 sn=f'rejected-{label}-executed.lean.txt';rn=f'rejected-{label}-receipt.json';shutil.copyfile(T/src,D/sn);shutil.copyfile(T/receipt,D/rn)
 rej.append(dict(label=label,source=sn,receipt=rn,source_sha256=sha(D/sn),reason=why,accepted=False,original_source_path=str(T/src),original_receipt_path=str(T/receipt)))
out('verification.json',dict(declaration='Roth.normOne_det_le',unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=a,rejected=rej,production_unchanged=True))
print('4 native accepted sets;warming and failed normalization retained separately')
