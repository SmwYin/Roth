from pathlib import Path
import re,json
D=Path(__file__).resolve().parent;R=Path.cwd();s=(D/'source-MainLemma.lean.txt').read_text();b=s[s.index('namespace Roth'):]
a=b.index('/-- For polynomials over a seminormed ring');e=b.index('/-- Integer polynomials with coordinate',a)
t=b[b.index('theorem norm_coeff_modByMonic_le',a):e].strip();b=b[:a]+b[e:]
needle='''      (((∏ k, (r k + 1) : ℕ) : ℝ) * (2 ^ (∑ k, r k) * B)) := by
''';assert b.count(needle)==1
local=t.replace('theorem norm_coeff_modByMonic_le','have remainder_bound',1)
local=local.replace('(hs : P.natDegree ≤ s) (i : ℕ) : ‖', '(hs : P.natDegree ≤ s) (i : ℕ) :\n    ‖')
local='\n'.join('  '+x for x in local.splitlines())+'\n'
b=b.replace(needle,needle+local).replace('    norm_coeff_modByMonic_le (by simpa','    remainder_bound (by simpa')
assert 'norm_coeff_modByMonic_le'not in b
b=b.replace('namespace Roth','namespace Rem243Inline\nopen Roth',1).replace('end Roth','end Rem243Inline')
checks='''
elab "oldCaller243" : term => do
  Lean.Meta.mkConstWithFreshMVarLevels (Lean.mkPrivateNameCore `Roth.MainLemma
    `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux)
example : oldCaller243 = @Rem243Inline.abs_coeff_diag_hasseDeriv_modByMonic_le_aux := rfl
#print axioms Rem243Inline.abs_coeff_diag_hasseDeriv_modByMonic_le_aux
#print axioms Rem243Inline.main_lemma
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo ``Rem243Inline.abs_coeff_diag_hasseDeriv_modByMonic_le_aux
  let some v := ci.value? (allowOpaque := true) | throwError "REM243_MISSING_CALLER"
  if v.getUsedConstants.any (fun c ↦ c == `Roth.norm_coeff_modByMonic_le) then
    throwError "REM243_TARGET_NOT_INLINED"
  Lean.logInfo "REM243_INLINE: actual caller; original signature retained; body inlined"
'''
whole=(D/'disk-prefix.lean.txt').read_text()+b+'\n'+checks
for l in whole.splitlines():
 if len(l)>100:print(len(l),l)
assert max(map(len,whole.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
rows=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());cs=[x for x in rows if x['name']=='Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux'];assert len(cs)==1
(D/'callers.json').write_text(json.dumps(dict(executable_occurrences=1,distinct_declarations=1,external_to_file=0,callers=cs),ensure_ascii=False,indent=2)+'\n')
print('Prepared complete MainLemma with actual caller inlining and signature equality')
