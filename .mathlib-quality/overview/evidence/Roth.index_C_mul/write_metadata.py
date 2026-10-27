from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).resolve().parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.index_C_mul'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for stem in ['explicit-composition','caller','bridge']:
 for suf in ['executed.lean.txt','receipt.json']:
  n='index-c-mul-'+stem+'-'+suf;shutil.copyfile(Path('/private/tmp/roth-overview')/n,D/n)
for n in ['index-c-mul-target-region.txt','index-c-mul-caller-region.txt']:
 p=Path('/private/tmp/roth-overview')/n
 if p.exists():shutil.copyfile(p,D/n)
p=ROOT/'.lake/packages/mathlib/Mathlib/Data/Finsupp/Defs.lean';n='Mathlib-Data-Finsupp-Defs.lean.txt';shutil.copyfile(p,D/n)
x=json.loads((D/'mathlib-inputs.json').read_text());x.append(dict(path=str(p.relative_to(ROOT)),sha256=sha(p),bytes=p.stat().st_size));put('mathlib-inputs.json',x)
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
put('assessment.json',dict(declaration=N,canonical_index=147,verdict='NO-composable-from-mathlib',completed=True,allphases='PASS',phases={p:'PASS' for p in phases},unresolved=[],root_acceptance='pending'))
type_='Roth.index_C_mul.{u_1} {σ : Type u_1} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (MvPolynomial.C c * P) α r = Roth.index P α r'
put('overview-entry.json',dict(declaration=N,kind='theorem',type=type_,what='Nonzero constant multiplication preserves the weighted Taylor index, including zero polynomials and zero weights.',how='Taylor multiplication and constant compatibility reduce to support_smul_eq.',hypotheses='Fintype fixed by parent; c≠0 essential uniformly by P=X guard; P, α and r arbitrary.',project_dependencies=['Roth.index','Roth.weight','MvPolynomial.taylor','MvPolynomial.taylor_C'],caller_summary='1 explicit body use at Theta405 in sum_max_sub_le_index_det; same sole direct consumer among exact canonical293; full caller replay passes.',mathlib_api_audit='Reaimed infDegree scalar law is core congrArg applied to existing Finsupp.support_smul_eq; independently compiled explicit existing-call term and canonical133 bridge transport.',moral_duplications='Scalar support invariance; related weightedOrder inequality/multiplication and negation API.',generalization='Verified arbitrary exponent/degree semilatticeinf/top and coefficient semiring acted on by scalar domain with torsion-free module. This library interface is not logical minimum; zero-preserving injective coefficient maps have existing support_mapRange_of_injective; unit/regular scalar extension not claimed compiled.',missing_api='No essential mathematical gap. Named degree_smul convenience not identified; explicit congruence composition sufficient.',junk='Used compatibility adapter; not dead code. No proof holes or infrastructure changes.',action='NO-composable-from-mathlib on generic parent reaim. Do not upstream concrete specialization. At sole Theta405 caller, inline verified original-form support proof if removing wrapper; retain map_intCast and Taylor/parent bridge normalization. Alternative local home Roth/Index.lean during parent migration.'))
accepted=[]
def add(label,stem,region,required,fmt='disk',source=None):
 src=source or 'index-c-mul-'+stem+'-executed.lean.txt';rec='index-c-mul-'+stem+'-receipt.json'
 if stem=='original':rec='index-c-mul-original-audit-receipt.json'
 accepted.append(dict(label=label,source=src,source_sha256=sha(D/src),receipt=rec,format=fmt,native_region_start_line=region,required_info=required,**({'guard':N} if fmt=='raw' else {})))
add('original','original',3599,[N+"' depends on axioms:",N+'.{u_1}'])
add('canonical-audit','original',3603,['INDEX_C_MUL147_AUDIT: requested=293; unique=293','INDEX_C_MUL147_AUDIT_PRESENT: present=293; values=293','INDEX_C_MUL147_DIRECT_CONSUMER: Roth.sum_max_sub_le_index_det'])
add('mathlib-generic','mathlib',1,["'IndexCMulMathlib147.modern' depends on axioms:","'IndexCMulMathlib147.supportGeneral' depends on axioms:"],fmt='raw')
add('explicit-composition','explicit-composition',1,["'IndexCMulMathlib147.modern' depends on axioms:"],fmt='raw')
add('target','target-clean',3921,["'IndexCMul147.replacement' depends on axioms:","'IndexCMul147.zero' depends on axioms:","'IndexCMul147.zeroScalarGuard' depends on axioms:"])
add('caller','caller',3937,["'IndexCMulCaller147.callerReplay' depends on axioms:"])
add('bridge','bridge',3980,["'IndexCMulBridge147.replacement' depends on axioms:"])
put('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=[dict(source='index-c-mul-target-initial-executed.lean.txt',receipt='index-c-mul-target-initial-receipt.json',reason='Initial zero-scalar guard omitted support_X and left a goal; not accepted proof evidence. All accepted replacements/guards rerun clean.')],audit=dict(source='index-c-mul-audit-executed.lean.txt',target=N,canonical_count=293,region_start_line=3603),target_source='index-c-mul-target-clean-executed.lean.txt',caller_source='index-c-mul-caller-executed.lean.txt',bridge_source='index-c-mul-bridge-executed.lean.txt'))
