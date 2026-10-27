from pathlib import Path
import hashlib,json,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.diag';T=Path('/private/tmp/roth-overview')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
accepted=[]
for label in ['target','naturality','consumer','raw','infrastructure']:
 src=T/f'diag-{label}-executed.lean.txt';rec=T/f'diag-{label}-success.json'
 for p,n in [(src,f'native-{label}-executed.lean.txt'),(rec,f'native-{label}-success.json')]:shutil.copyfile(p,D/n)
 accepted.append(dict(label=label,source=f'native-{label}-executed.lean.txt',source_sha256=sha(src),receipt=f'native-{label}-success.json'))
rejected=[]
for label,amount in [('consumer',1),('raw',1),('infrastructure',2)]:
 for i in range(1,amount+1):
  stem=f'diag-{label}-rejected-{i}'
  for ext in ['.lean.txt','.json']:shutil.copyfile(T/(stem+ext),D/(stem+ext))
  rejected.append(dict(source=stem+'.lean.txt',receipt=stem+'.json',accepted=False))
out('verification.json',dict(declaration=N,accepted=accepted,rejected=rejected,standard_axioms=['propext','Classical.choice','Quot.sound'],unresolved=[],policy='Only clean full native success accepted, not partial/warming. Exact newly appended source chunks archived for persistent requests; raw request code archived exactly. No production change, new axioms, unsafe proof or raised limits.'))
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']}
out('assessment.json',dict(declaration=N,canonical_index=76,source='Roth/CoeffNorm.lean:161',kind='def',verdict='NO-composable-from-mathlib',reason='Exact one-call aeval-to-Polynomial.X construction and verified CommSemiring generality, with real semantic local API exemption and full def-specific/literature/formal/caller/native evidence.',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True))
out('overview-entry.json',dict(declaration=N,kind='def',type='∀ {σ : Type u_1}, MvPolynomial σ ℤ → Polynomial ℤ',what='Diagonal specialization: replace all variables by a common polynomial indeterminate, adding coefficients when total exponents collide.',how='One existing MvPolynomial.aeval application to constant Polynomial.X, exact rfl recovery. Alternative rename-to-PUnit then uniqueAlgEquiv is proved equal, not claimed defeq.',hypotheses='Arbitrary variable type σ and integer polynomial; no finiteness, DecidableEq, nonzero or degree assumptions.',project_dependencies=[],caller_summary='11 distinct direct declaration consumers: 5 CoeffNorm and 6 MainLemma in one external file. Full vanishing/subtraction replays and mathlib-only generalized expansion verified; all 11 caller plans explicit. Arbitrary predicate-context rfl transport checked, not a claim all callers were separately rebuilt.',mathlib_api_audit='MvPolynomial.aeval (Eval569) gives exact construction; comp_aeval_apply and Polynomial.aeval_X give arbitrary algebra-target evaluation. Existing rename and uniqueAlgEquiv supply alternate bundle. pUnitAlgEquiv deprecated in pinned source, avoided in probes.',moral_duplications='No second arbitrary-variable diagonal implementation found; HasseDeriv unique-variable transport is different. Not generating-series coefficient diagonal extraction. Bounds need independent assessments.',generalization='Verified CommSemiring R, independent arbitrary variable universe, exact ℤ specialization, empty/lifted variables and arbitrary commutative R-algebra evaluation. Bool/ℤ noninjectivity proved; no degree equality or equivalence claimed.',missing_api='No missing scalar construction, hom bundle or evaluation-composition API established. Specialized coefficient/degree bounds remain separate assessment candidates.',junk='Useful one-line semantic local API with eleven consumers; retain in CoeffNorm under production freeze. No claim downstream estimates are junk.',action='NO-composable-from-mathlib upstream wrapper. Reuse existing aeval; if later deleting, apply all eleven explicit caller plans and full dependent validation. Production sources unchanged.'))
c=json.loads((D/'callers.json').read_text())
for x in c['callers']:
 if x['name']=='Roth.exists_ne_modByMonic_eq':x['end_line']=379
 if x['name']=='Roth.eval_hasseDeriv_sub_eq_zero':x['end_line']=411
 if x['name']=='Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux':x['end_line']=548
 if x['name']=='Roth.exists_mem_RSet_le_index_aux':x.update(line=550,end_line=567)
 if x['name']=='Roth.exists_mem_RSet_le_index_of_rpow_bound_aux':x['line']=581
out('callers.json',c)
s=(D/'report.md').read_text().replace('one raw attempt\'s simp unfolding left an AlgEquiv projection goal, fixed by typed change.','one raw attempt\'s simp unfolding left an AlgEquiv projection goal, fixed by typed change.\nTwo infrastructure preparations failed on unqualified eval ambiguity and then an unnecessary\nsimpa style warning, corrected with qualified evaluation and simp at the hypothesis.').replace('both rejected preparations','all four rejected preparations')
(D/'report.md').write_text(s)
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','root-review.json']:continue
 dest='.mathlib-quality/overview/'+('mathlibable/'+N+'.md' if p.name=='report.md' else 'evidence/'+N+'/'+p.name)
 files.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
out('copy-manifest.json',dict(declaration=N,files=files))
print('Finalized candidate; validator must pass before freeze.')
