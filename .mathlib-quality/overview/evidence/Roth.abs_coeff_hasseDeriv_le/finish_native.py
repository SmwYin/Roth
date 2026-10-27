from pathlib import Path
import shutil,json,hashlib,re
D=Path(__file__).parent;T=Path('/private/tmp/roth-overview')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
sets=[
 ('original','abs-hasse-original',['Roth.abs_coeff_hasseDeriv_le','MvPolynomial.AbsHasseAssessment.replay']),
 ('generic','abs-hasse-generic-clean',['MvPolynomial.AbsHasseGeneric.scalarBound','MvPolynomial.AbsHasseGeneric.bound','MvPolynomial.AbsHasseGeneric.specialization']),
 ('raw','abs-hasse-raw',['AbsHasseRaw.scalarBound','AbsHasseRaw.binomialBound']),
 ('consumers','abs-hasse-consumers',['MvPolynomial.AbsHasseConsumers.abs_eval_iterated_hasseDeriv_lt_aux_replay','MvPolynomial.AbsHasseConsumers.abs_coeff_diag_hasseDeriv_modByMonic_le_aux_replay'])]
a=[]
for label,stem,expected in sets:
 p=T/(stem+'-executed.lean.txt');r=T/(stem+'-receipt.json')
 sn=f'native-{label}-executed.lean.txt';rn=f'native-{label}-success.json'
 shutil.copyfile(p,D/sn);shutil.copyfile(r,D/rn);j=json.loads(r.read_text())
 a.append(dict(label=label,source=sn,receipt=rn,source_sha256=sha(D/sn),execution_path=j['request'].get('file_path','virtual lean_run_code'),original_source_path=str(p),original_receipt_path=str(r),expected_axiom_declarations=expected))
s=(D/'native-consumers-executed.lean.txt').read_text()
# Last generated array belongs to this declaration; earlier arrays in the persistent document remain untouched.
arrays=re.findall(r'  let names : Array Lean.Name := #\[.*?\]\n',s,re.S)
assert re.sub(r'\s','',arrays[-1])==re.sub(r'\s','',(D/'canonical-audit-array.lean.txt').read_text())
sn='rejected-generic-executed.lean.txt';rn='rejected-generic-receipt.json'
shutil.copyfile(T/'abs-hasse-generic-executed.lean.txt',D/sn)
shutil.copyfile(T/'abs-hasse-generic-receipt.json',D/rn)
rejected=[dict(label='generic-initial',accepted=False,source=sn,receipt=rn,source_sha256=sha(D/sn),reason='Initial add_le_add_right produced wrong term order and recovered sorryAx. Corrected to add_le_add ih le_rfl; only clean receipt accepted.',original_source_path=str(T/'abs-hasse-generic-executed.lean.txt'),original_receipt_path=str(T/'abs-hasse-generic-receipt.json'))]
out('verification.json',dict(declaration='Roth.abs_coeff_hasseDeriv_le',unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=a,rejected=rejected,production_unchanged=True))
shutil.copyfile(T/'abs-hasse-reviewer-git.json',D/'reviewer-git.json')
print('Copied 4 successful native sets and 1 rejected attempt; reviewer receipt')
