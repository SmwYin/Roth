from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_m')
s=(D/'isolated-prefix.lean.txt').read_text()+'''
#check_failure Roth.exists_m
namespace Dimension275Shape
-- The middle quantitative requirement is implied by the first, not an independent input.
theorem middle {n m : ℕ} (hm : 16 * n ^ 2 < m) :
    4 * n * √(m : ℝ) < m := by
  have hmR0 : (16 : ℝ) * (n : ℝ) ^ 2 < m := by exact_mod_cast hm
  have hmR : (4 * (n : ℝ)) ^ 2 < m := by nlinarith only [hmR0]
  have hs : 4 * (n : ℝ) < √(m : ℝ) := (Real.lt_sqrt (by positivity)).2 hmR
  have hs0 : 0 < √(m : ℝ) := (by positivity : (0 : ℝ) ≤ 4 * n).trans_lt hs
  simpa only [← pow_two, Real.sq_sqrt (Nat.cast_nonneg m)] using
    mul_lt_mul_of_pos_right hs hs0

-- Abstract representation probe: arbitrary Archimedean ordered semiring bounds,
-- without claiming Real.sqrt itself is defined on that weaker hierarchy.
example {R : Type*} [Semiring R] [LinearOrder R] [IsStrictOrderedRing R] [Archimedean R]
    (a b : R) : ∃ n : ℕ, a < n ∧ b < n := by
  obtain ⟨n, hn⟩ := exists_nat_gt (max a b)
  exact ⟨n, (le_max_left _ _).trans_lt hn, (le_max_right _ _).trans_lt hn⟩

#check @Real.tendsto_sqrt_atTop
#check @tendsto_bdd_div_atTop_nhds_zero
#check @Real.lt_sqrt
#print axioms Dimension275Shape.middle
end Dimension275Shape
'''
(D/'shape-executed.lean.txt').write_text(s)
q={'id':'shape01','operation':'run_code','source':'shape-executed.lean.txt','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'shape-receipt.json','arguments':{}}
(D/'root-requests/shape01.json').write_text(json.dumps(q,indent=2)+'\n')
# Actual full caller replays with proposed new generic replacement, preserving its original type.
s=(D/'signed-executed.lean.txt').read_text().split('#check_failure Roth.exists_m\n',1)[1]
s=s[:s.index('-- No n>0')]+ 'end Dimension275Signed\n'
s=s.replace('  fail_if_success exact?\n','')
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());c=next(x for x in meta if x['name']=='Roth.exists_roth_parameters_aux')['source']
c=c.replace('private lemma exists_roth_parameters_aux','theorem replay').replace(':= exists_m (n := f.natDegree) hκ',':= Dimension275Signed.recovered (n := f.natDegree) hκ')
s=(D/'disk-prefix.lean.txt').read_text()+'\n'+s+'\nnamespace Dimension275ReplacementCaller\nopen Roth\n'+c+'\nend Dimension275ReplacementCaller\n#print axioms Dimension275ReplacementCaller.replay\n'
(D/'replacement-caller-executed.lean.txt').write_text(s)
q={'id':'replacementcaller01','operation':'diagnostics','source':'replacement-caller-executed.lean.txt','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'replacement-caller-receipt.json','arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}}
(D/'root-requests/replacementcaller01.json').write_text(json.dumps(q,indent=2)+'\n')
print('Prepared shape01 and replacementcaller01; no extra imports')
