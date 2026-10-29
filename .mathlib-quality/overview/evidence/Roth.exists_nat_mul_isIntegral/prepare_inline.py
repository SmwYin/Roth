from pathlib import Path
import json,re,hashlib
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.exists_nat_mul_isIntegral'
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());c=next(x for x in meta if x['name']=='Roth.reduction');raw=c['source']+'\n';(D/'caller-Roth.reduction.lean.txt').write_text(raw)
(D/'callers.json').write_text(json.dumps(dict(source_explicit=[dict(name=c['name'],file=c['file'],line=c['line'],end_line=c['end_line'],archive='caller-Roth.reduction.lean.txt',sha256=hashlib.sha256(raw.encode()).hexdigest(),occurrences=1)],source_explicit_count=1,external_to_declaring_file=0,internal_excluding_declaring_file=0,inline_rederivations_elsewhere=[]),indent=2))
needle='  obtain ⟨M, hM0, hMint⟩ := exists_nat_mul_isIntegral halg'
manual='''  obtain ⟨y, hy, hint⟩ :=
    ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 halg).exists_integral_multiple
  let M := y.natAbs
  have hM0 : 0 < M := Int.natAbs_pos.2 hy
  have hMint : IsIntegral ℤ ((M : ℝ) * α) := by
    simpa [M, zsmul_eq_mul, ← mul_assoc, ← Int.cast_mul, Int.sign_mul_self]
      using hint.zsmul y.sign'''
closure='''  obtain ⟨M, s, hM, hs⟩ :=
    ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 halg).exists_nsmul_eq (integralClosure ℤ ℝ)
  have hM0 : 0 < M := Nat.pos_of_ne_zero hM
  have hMint : IsIntegral ℤ ((M : ℝ) * α) := by
    have hi : IsIntegral ℤ (M • α) := by
      rw [hs]
      exact s.property
    simpa only [nsmul_eq_mul] using hi'''
body='namespace NatIntegral268Inline\nopen Roth\n'+raw.replace('theorem reduction ','theorem manual_reduction ',1).replace(needle,manual)+raw.replace('theorem reduction ','theorem closure_reduction ',1).replace(needle,closure)+'''example : @Roth.reduction = @manual_reduction := Subsingleton.elim _ _
example : @Roth.reduction = @closure_reduction := Subsingleton.elim _ _
end NatIntegral268Inline
#print axioms NatIntegral268Inline.manual_reduction
#print axioms NatIntegral268Inline.closure_reduction
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.exists_nat_mul_isIntegral
  let some val := ci.value? (allowOpaque := true) | throwError "NAT268_NO_BODY"
  Lean.logInfo m!"NAT268_BODY_CONSTANTS_OPAQUE: {val.getUsedConstants.toList}"
  let env ← Lean.getEnv
  let names := #[`Roth.exists_nat_mul_isIntegral, `NatIntegral268Inline.manual_reduction,
    `NatIntegral268Inline.closure_reduction]
  for n in names do
    let ci ← Lean.getConstInfo n
    let some val := ci.value? (allowOpaque := true) | throwError "NAT268_NO_VALUE: {n}"
    unless (ci.type.getUsedConstants.all fun c ↦
        !c.toString.startsWith "NatIntegral268Original.") do
      throwError "NAT268_BAD_CONTEXT"
    Lean.logInfo m!"NAT268_INLINE_BODY: {n}: {val.getUsedConstants.toList}"
    let info ← Lean.Meta.ppExpr ci.type
    Lean.logInfo m!"NAT268_INLINE_TYPE: {n}: {info}"
  let mut todo : List Lean.Name := val.getUsedConstants.toList.filter fun n ↦
    n.toString.startsWith "Roth."
  let mut seen : List Lean.Name := []
  while !todo.isEmpty do
    let n := todo.head!
    todo := todo.tail!
    if !seen.contains n then
      seen := n :: seen
      if let some ci := env.find? n then
        let deps := ci.type.getUsedConstants.toList ++
          ((ci.value? (allowOpaque := true)).map (·.getUsedConstants.toList)).getD []
        todo := deps ++ todo
  for n in seen do
    if n.toString.startsWith "Roth." then
      Lean.logInfo m!"NAT268_TRANSITIVE_PROJECT: {n}"
'''
# Dependency traversal is bounded by environment acyclicity, no resource changes.
full=(D/'disk-prefix.lean.txt').read_text()+body
assert max(map(len,full.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(full);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(full)
print('Prepared actual caller manual + closure',len(full.splitlines()),'lines')
