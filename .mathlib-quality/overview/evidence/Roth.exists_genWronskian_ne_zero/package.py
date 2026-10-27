#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,shutil
D=Path(__file__).resolve().parent;R=Path.cwd();T=D.parent.parent;N='Roth.exists_genWronskian_ne_zero'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(D/n).write_text(json.dumps(v,indent=2)+'\n')
def native(rec):
 x=rec['result'];x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
for p in T.glob('exists-gen-wronskian-*'):
 if p.is_file() and 'full-execution' not in p.name and 'execution-contexts' not in p.name:
  shutil.copyfile(p,D/p.name)
for suffix in ['json','log']:
 p=T/f'gen-wronskian-file-completion-2026-10-27.{suffix}';shutil.copyfile(p,D/p.name)
regions={'original':9153,'audit':9157,'support-clean':9476,'actual-consumer':9514,'candidates':1,'jacobian':1,'characteristic-final':1}
accepted=[]
for label,start in regions.items():
 sn=f'exists-gen-wronskian-{label}-executed.lean.txt';rn=f'exists-gen-wronskian-{label}-receipt.json';rec=json.loads((D/rn).read_text());nr=native(rec);assert nr['success'] and not nr.get('partial',False)
 ds=nr.get('items',nr.get('diagnostics',[]));assert not [x for x in ds if x.get('severity') in ['error','warning']]
 names=[]
 for x in ds:
  if x.get('line',0)>=start:
   m=re.match(r"'([^']+)' depends on axioms:",x.get('message',''))
   if m:names.append(m[1])
 accepted.append(dict(label=label,source=sn,source_sha256=sha(D/sn),receipt=rn,original_execution_request=rec['request'],execution_kind='persistent-disk' if 'file_path' in rec['request'] else 'run-code',archive_kind='exact-appended-snippet' if 'file_path' in rec['request'] else 'exact-run-code-source',source_start_line_in_native_file=start,native_region_start_line=start,expected_axiom_declarations=names))
rejected=[]
for label in ['support','drop-finite','drop-field','composition','characteristic','characteristic-clean']:
 sn=f'exists-gen-wronskian-{label}-executed.lean.txt';rn=f'exists-gen-wronskian-{label}-receipt.json';rec=json.loads((D/rn).read_text());nr=native(rec);ds=nr.get('items',nr.get('diagnostics',[]));errs=[x['message'] for x in ds if x.get('severity') in ['error','warning']];assert errs
 rejected.append(dict(label=label,source=sn,receipt=rn,reason='; '.join(errs),original_execution_request=rec['request']))
save('verification.json',dict(declaration=N,accepted=accepted,rejected=rejected,unresolved=[],production_unchanged=True,standard_axioms=['propext','Classical.choice','Quot.sound'],canonical_direct_consumers=['_private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux'],notes=['Original/audit persistent disk info assertions scoped to exact fresh region; all-file error/warning/axiom checks retained.','Accepted support-clean removes Finite σ by new finite-family support/rename proof; original finite-variable theorem is used as local prerequisite, not circularly as an arbitrary-variable theorem.','Failed Finite drop establishes old proof limitation; failed Field drop establishes parent genWronskian interface only, not mathematical falsehood.','Actual full Separation caller replay substitutes the stronger arbitrary-variable theorem and retains all public helpers.','Composition exact? failure is not evidence of absence; positive candidates have inspected signatures and do not supply bounded derivative-row selection.','Run-code receipts use diagnostics and no partial field; persistent disk requires partial=false.']))
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; six infrastructure categories considered'
save('assessment.json',dict(declaration=N,canonical_index=119,source='Roth/GenWronskian.lean:254',verdict='YES-but-generalise-first',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,classification='BIG',composition='NOT-COMPOSABLE',verified_weakening='Delete Finite σ; exact same Field/CharZero/Fin l/genWronskian conclusion, via finite union of variable supports and rename transport.',upstream_file='Mathlib/RingTheory/MvPolynomial/Wronskian.lean',pr_title='feat(MvPolynomial): nonvanishing generalized Hasse Wronskians',generalise_checklist='/generalise Roth.exists_genWronskian_ne_zero',cleanup_checklist='/cleanup Roth/GenWronskian.lean Roth.exists_genWronskian_ne_zero'))
msg=(D/'original-type.txt').read_text().strip()
save('overview-entry.json',dict(declaration=N,kind='theorem',type='@'+msg,what='A linearly independent finite family of multivariate polynomials has a nonzero Hasse Wronskian with total derivative order at most each row index.',how='Choose bounded injective Kronecker substitution, use univariate nonvanishing, expand higher substituted derivatives and determinant, contradict simultaneous vanishing.',hypotheses=['Field K','CharZero K: essential for bounded row-order theorem','Finite σ: removable by verified finite-support restriction/rename proof','φ : Fin l → MvPolynomial σ K; LinearIndependent K φ; no positive l or nonempty σ assumption'],project_dependencies=['Roth.genWronskian','Roth.exists_hasseDeriv_kronecker_eq_sum','Roth.wronskian_ne_zero_of_linearIndependent','Roth.linearIndependent_kronecker','private Roth.wronskian_kronecker_eq_sum_aux'],caller_summary='One explicit external-to-file caller: private Roth.exists_rat_factors_det_hasseDeriv_aux, Separation:524; exact293 canonical direct-consumer audit agrees; full caller replay with stronger theorem passes.',mathlib_api_audit='Pinned pairwise Polynomial.Wronskian TODO explicitly requests n-tuples. Generic matrix determinant nonvanishing and Jacobian criteria do not select bounded derivative rows from coefficient-field independence. All five search methods executed on three forms.',moral_duplications='Classical Bostan–Dumas Theorem3 polynomial specialization, with Hasse normalization; not duplicated by existing two-polynomial Wronskian API.',generalization='Verified deletion of Finite σ, using finite union of vars, LI.of_comp, derivative rename, degree_mapDomain and determinant rename. Direct one-edit replay fails at Fintype.ofFinite. Domain/fraction-field and formal-series extensions remain distinct unverified proposals.',missing_api='Bounded generalized Hasse-Wronskian nonvanishing criterion for independent finite polynomial families; finite-family univariate criterion and multivariate Hasse interface are prerequisite API.',junk='Live module main theorem, substantive classical result; not junk despite a single direct consumer.',action='YES-but-generalise-first: remove global variable finiteness with accepted support bridge, prepare new Mathlib/RingTheory/MvPolynomial/Wronskian.lean beside accepted parent proposal; retain CharZero/Field/row bounds; independently develop any domain or power-series extension.'))
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dst,sha256=sha(p),bytes=p.stat().st_size))
save('copy-manifest.json',dict(declaration=N,files=files));print('Packaged',len(files),'artifacts')
