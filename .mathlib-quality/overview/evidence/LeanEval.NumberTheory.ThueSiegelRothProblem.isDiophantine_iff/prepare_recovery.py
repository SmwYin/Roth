from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent
s=(D/'modern-executed.lean.txt').read_text()
def block(a,b):return s[s.index(a):s.index(b)]
c=(D/'disk-prefix.lean.txt').read_text()+'\nnamespace Equivalence292Recovery\nopen Real\n'
c+=block('def UniformBound','example (_x')
c+=block('def pairSet','theorem pairSet_den')
c+=block('lemma uniform_irrational','lemma finite_uniform')
c+=block('lemma finite_uniform','lemma gap')
c+=block('lemma gap','lemma uniform_iff')
c+=block('lemma rational_pair_infinite','lemma pair_liouville')
c+='''theorem all_real {x : ℝ} :
    LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x ↔
      ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2 :=
  uniform_pair_iff_all_real
example {x : ℝ} (hx : Irrational x) :
    LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff hx =
      (all_real : LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x ↔
        ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2) := Subsingleton.elim _ _
open LeanEval.NumberTheory.ThueSiegelRothProblem
-- Complete actual caller with its original signature; only the equivalence invocation changes.
theorem thueSiegelRoth (x : ℝ) (_h_irr : Irrational x) (_h_alg : IsAlgebraic ℤ x) :
    IsDiophantine x :=
  all_real.mpr
    (Roth.roth _h_irr (_h_alg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)))
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Equivalence292Recovery.thueSiegelRoth := Subsingleton.elim _ _
example (r : ℚ) : ¬ IsDiophantine (r : ℝ) := by
  intro h
  exact (uniform_irrational (t := 2) h).ne_rat r rfl
example (r : ℚ) (κ : ℝ) : (Roth.approxSet (r : ℝ) κ).Infinite :=
  rational_pair_infinite r κ
#print axioms Equivalence292Recovery.all_real
#print axioms Equivalence292Recovery.thueSiegelRoth
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Equivalence292Recovery.thueSiegelRoth
  let some val := ci.value? (allowOpaque := true) | throwError "D292_RECOVERY_MISSING_VALUE"
  if val.getUsedConstants.contains
      `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff then
    throwError "D292_RECOVERY_RETAINED_TARGET"
  Lean.logInfo "D292_RECOVERY_CALLER_TARGET_FREE"
end Equivalence292Recovery
'''
# Generic bounded denominator helper is represented by its exact project operation.
c=c.replace('pairSet_den_le_finite','Roth.approxSet_den_le_finite')
assert max(map(len,c.splitlines()))<=100
(D/'recovery-executed.lean.txt').write_text(c.rstrip()+'\n')
r=dict(id='recovery01',operation='diagnostics',source='recovery-executed.lean.txt',source_sha256=hashlib.sha256((D/'recovery-executed.lean.txt').read_bytes()).hexdigest(),receipt='recovery01-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
(D/'root-requests/recovery01.json').write_text(json.dumps(r,indent=2)+'\n')
print('Prepared recovery01 exact disk9; all-real fixed2 equivalence and original-signature caller')
