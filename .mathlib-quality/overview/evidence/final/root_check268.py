from pathlib import Path
import json,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_nat_mul_isIntegral');prefix=(D/'disk-prefix.lean.txt').read_text();s=(R/'Roth/Main.lean').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace NatIntegral268Original\nopen Roth',1).replace('end Roth','end NatIntegral268Original');body=re.sub(r'\bexists_nat_mul_isIntegral\b','replay',body)
assert(D/'original-executed.lean.txt').read_text().startswith(prefix+body)
c=json.loads((D/'callers.json').read_text())['source_explicit'];assert len(c)==1 and c[0]['name']=='Roth.reduction';x=c[0];raw='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])+'\n';assert raw==(D/x['archive']).read_text()
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
expected=prefix+'namespace NatIntegral268Inline\nopen Roth\n'+raw.replace('theorem reduction ','theorem manual_reduction ',1).replace(needle,manual)+raw.replace('theorem reduction ','theorem closure_reduction ',1).replace(needle,closure)
actual=(D/'inline-executed.lean.txt').read_text();assert actual.startswith(expected);assert actual.count('Subsingleton.elim _ _')==2
assert (D/'scope-executed.lean.txt').read_text().startswith(expected)
for label in ['original','isolated-firstclean','isolated','inline','supplement','scope']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);assert z['success']and not z.get('partial',False)and not z.get('timed_out',False)
 ds=z.get('items',z.get('diagnostics'));assert not[x for x in ds if x['severity']in['warning','error']];assert not any('sorryAx'in x['message']for x in ds)
 print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root exact full original Main replay and both full actual reduction caller replacements independently reconstructed; six native receipt groups clean. No final assessment acceptance here.')
