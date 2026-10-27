#!/usr/bin/env python3
"""Freeze only this scratch assessment; never edit production or Git."""
from pathlib import Path
import hashlib,json,re,shutil
D=Path(__file__).resolve().parent;T=D.parent.parent;R=Path.cwd()
N='Roth.exists_hasseDeriv_kronecker_eq_sum'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(D/n).write_text(json.dumps(v,indent=2)+'\n')
def native(rec):
 x=rec['result'];x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
for p in T.glob('exists-hasse-kronecker-*'):
 if p.is_file():shutil.copyfile(p,D/p.name)
P=T/'assess/Roth.derivative_aeval'
for n in ['derivative-aeval-no-tower-executed.lean.txt','derivative-aeval-no-tower-receipt.json']:
 shutil.copyfile(P/n,D/n)
starts={'original':7541,'audit':7545,'finite-gamma':7864,'consumer':7953,
 'rational-clean':7992,'semiring':8083,'semiring-consumer-clean':8174,'extraction':1}
starts['span-candidates']=8213
accepted=[]
for label,start in starts.items():
 source=f'exists-hasse-kronecker-{label}-executed.lean.txt';receipt=f'exists-hasse-kronecker-{label}-receipt.json'
 rec=json.loads((D/receipt).read_text());nr=native(rec)
 assert nr['success'] and not nr.get('partial',False),label
 ds=nr.get('items',nr.get('diagnostics',[]));assert not [x for x in ds if x.get('severity') in ['error','warning']],label
 names=[]
 for x in ds:
  if x.get('line',0)>=start:
   m=re.match(r"'([^']+)' depends on axioms:",x.get('message',''))
   if m:names.append(m[1])
 accepted.append(dict(label=label,source=source,source_sha256=sha(D/source),receipt=receipt,
  original_execution_request=rec['request'],execution_kind='persistent-disk' if 'file_path' in rec['request'] else 'run-code',
  native_region_start_line=start,expected_axiom_declarations=names))
s='derivative-aeval-no-tower-executed.lean.txt';r='derivative-aeval-no-tower-receipt.json'
rec=json.loads((D/r).read_text())
accepted.append(dict(label='semiring-first-order-prerequisite',source=s,source_sha256=sha(D/s),receipt=r,
 original_execution_request=rec['request'],execution_kind='run-code',native_region_start_line=1,
 expected_axiom_declarations=['DerivativeAEvalNoTower.semiring']))
rejected=[]
for label in ['gamma','rational','semiring-consumer']:
 s=f'exists-hasse-kronecker-{label}-executed.lean.txt';r=f'exists-hasse-kronecker-{label}-receipt.json'
 rec=json.loads((D/r).read_text());ds=native(rec).get('items',native(rec).get('diagnostics',[]))
 failures=[x['message'] for x in ds if x.get('severity') in ['warning','error']]
 assert failures,label
 rejected.append(dict(label=label,source=s,receipt=r,original_execution_request=rec['request'],reason='; '.join(failures)))
save('verification.json',dict(declaration=N,accepted=accepted,rejected=rejected,unresolved=[],production_unchanged=True,
 standard_axioms=['propext','Classical.choice','Quot.sound'],canonical_direct_consumers=['Roth.exists_genWronskian_ne_zero'],
 notes=['Full-file error/warning/axiom scans; fresh proof/audit assertions scoped to appended regions.',
 'Run-code uses diagnostics and has no partial field; persistent disk requires partial=false.',
 'Rejected initial consumer may contain recovery sorryAx and is excluded from accepted evidence.',
 'Characteristic-independent literature theorem is a future API design question, not a claimed native weakening.',
 'No repeated expensive exact? search is asserted as an absence proof.']))
s=(D/'exists-hasse-kronecker-audit-executed.lean.txt').read_text()
arr=re.search(r'let names : Array Lean.Name := #\[.*?\]',s,re.S).group(0)
(D/'canonical-audit-array.lean.txt').write_text(arr+'\n')
nr=native(json.loads((D/'exists-hasse-kronecker-original-receipt.json').read_text()))
typ=[x['message'] for x in nr['items'] if x.get('line',0)>=7541 and x['message'].startswith('Roth.exists_hasseDeriv_kronecker_eq_sum.')][0]
(D/'original-type.txt').write_text(typ+'\n')
fulltype='@'+N+' : ∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] [CharZero K] (k μ : ℕ), ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (Roth.kronecker k P) = ∑ d ∈ s, c d * Roth.kronecker k (MvPolynomial.hasseDeriv d P)'
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']}
phases['4.5']='n/a: theorem; all six infrastructure categories accounted for'
save('assessment.json',dict(declaration=N,canonical_index=116,source='Roth/GenWronskian.lean:214',verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,composition='NOT-COMPOSABLE',verified_weakening='arbitrary γ; CommSemiring R + Algebra ℚ R; Finite σ',future_api_questions=['Primary filtered-span membership API?','Primary characteristic-independent explicit Hasse–Taylor chain rule?','Public finite-coefficient corollary or project-local Wronskian helper?']))
save('overview-entry.json',dict(declaration=N,kind='theorem',type=fulltype,
 what='Uniform finite polynomial linear combination of substituted multivariate Hasse derivatives of order at most μ for a Kronecker pullback.',
 how='Extract supported Finsupp coefficients from private order-filtered span membership; membership uses derivative stability, induction and successor-scalar division.',
 hypotheses=['Field K and CharZero K in original','Fintype σ fixes concrete Kronecker enumeration','arbitrary natural k and μ; no k>1, degree bounds or l'],
 project_dependencies=['Roth.hasseDeriv_kronecker_mem (private)','Roth.kronSpan (private)','Roth.kronHasse (private)','Roth.kronecker','MvPolynomial.hasseDeriv'],
 caller_summary='One explicit same-file consumer Roth.exists_genWronskian_ne_zero at line260; canonical exact293 direct-consumer audit agrees. Full caller replays against strongest generalized theorem.',
 mathlib_api_audit='Polynomial.hasseDeriv_comp is operator composition, not substitution; Finsupp span/extraction API supplies coefficients only after substantive membership. Analytic Faà di Bruno and univariate Taylor API are partial matches.',
 moral_duplications='Final extraction is generic span linear algebra, but the private uniform higher chain-rule premise is new project content. No verified existing <=3-call replacement for the full law.',
 generalization='Verified arbitrary γ : σ → Polynomial R, CommSemiring R + Algebra ℚ R, Finite σ. Original specialization and actual sole caller compile. Characteristic-independent primary literature formula not claimed compiled.',
 missing_api='Higher polynomial-substitution law for multivariate Hasse derivatives, with choice of filtered-span, finitely supported coefficients or explicit Taylor formula.',
 junk='Live Wronskian helper; single explicit consumer does not make it dead or automatically composable.',
 action='BORDERLINE-needs-human: choose primary upstream representation and characteristic scope; original Kronecker corollary can remain project-local. All assessment verification complete.'))
sourcepairs=[('Roth/GenWronskian.lean','declaring-module.lean.txt'),('Roth/HasseDeriv.lean','project-hasse.lean.txt'),('.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','mathlib-hasse.lean.txt'),('.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean','mathlib-taylor.lean.txt'),('.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean','mathlib-linearCombination.lean.txt')]
save('source-inputs.json',[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size,archive=a) for p,a in sourcepairs])
refs=json.loads((D/'source-inputs.json').read_text())
refpath='.mathlib-quality/references/clean.tex'
refs.append(dict(path=refpath,sha256=sha(R/refpath),bytes=(R/refpath).stat().st_size))
save('source-inputs.json',refs)
save('optional-tool-availability.json',dict(ask_chatgpt_math='unavailable',local_index='unavailable; source-backed positive hits only',external_mathlib_index='Finder default v4.28.0 differs from pin; candidate checks native',first_order_prerequisite='Accepted112 DerivativeAEvalNoTower.semiring exact source and raw native receipt included'))
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dst,sha256=sha(p),bytes=p.stat().st_size))
save('copy-manifest.json',dict(declaration=N,files=files))
print(f'Frozen {len(files)} artifacts, {len(accepted)} accepted native experiments, {len(rejected)} rejected drafts')
