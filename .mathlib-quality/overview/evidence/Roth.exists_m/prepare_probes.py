from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_m')
def req(id,source,receipt,operation='run_code',audit=False):
 s=(D/source).read_bytes(); (D/'root-requests'/f'{id}.json').write_text(json.dumps({'id':id,'operation':operation,'source':source,'source_sha256':hashlib.sha256(s).hexdigest(),'receipt':receipt,'original_audit':audit,'arguments':{} if operation=='run_code' else {'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}},indent=2)+'\n')
prefix=(D/'isolated-prefix.lean.txt').read_text()
s=prefix+'''
#check_failure Roth.exists_m
namespace Dimension275
-- This is a NEW proof from existing mathlib building blocks, not an existing theorem.
theorem generic {a b κ : ℝ} (ha : 0 ≤ a) (hκ : b < κ) :
    ∃ m : ℕ, a ^ 2 < m ∧ a * √(m : ℝ) < m ∧
      b * m / (m - a * √(m : ℝ)) < κ := by
  obtain ⟨s, hs⟩ := exists_nat_gt (max a (κ * a / (κ - b)))
  have hsa : a < (s : ℝ) := (le_max_left _ _).trans_lt hs
  have hspos : (0 : ℝ) < s := ha.trans_lt hsa
  have hkey : κ * a < (s : ℝ) * (κ - b) :=
    (div_lt_iff₀ (sub_pos.mpr hκ)).mp ((le_max_right _ _).trans_lt hs)
  have hmul : a * (s : ℝ) < (s : ℝ) ^ 2 := by
    simpa only [pow_two] using mul_lt_mul_of_pos_right hsa hspos
  refine ⟨s ^ 2, ?_, ?_, ?_⟩
  · push_cast
    nlinarith only [sq_nonneg ((s : ℝ) - a), hsa, ha, hspos]
  · simpa only [Nat.cast_pow, Real.sqrt_sq (Nat.cast_nonneg s)] using hmul
  · push_cast
    rw [Real.sqrt_sq (Nat.cast_nonneg _), div_lt_iff₀ (sub_pos.mpr hmul)]
    nlinarith only [mul_lt_mul_of_pos_right hkey hspos]

theorem coefficient {t c b κ : ℝ} (ht : 0 ≤ t) (hc : 0 < c) (hκ : b < κ) :
    ∃ m : ℕ, (c * t) ^ 2 < m ∧ c * t * √(m : ℝ) < m ∧
      b * m / (m - c * t * √(m : ℝ)) < κ :=
  generic (mul_nonneg hc.le ht) hκ

theorem recovered {n : ℕ} {κ : ℝ} (hκ : 2 < κ) :
    ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧
      2 * m / (m - 4 * n * √(m : ℝ)) < κ := by
  obtain ⟨m, hm, hs, hq⟩ := generic (a := 4 * n) (by positivity) hκ
  refine ⟨m, ?_, hs, hq⟩
  have hm' : (16 : ℝ) * (n : ℝ) ^ 2 < m := by nlinarith only [hm]
  exact_mod_cast hm'

-- No n>0 is introduced: the generic theorem and recovery include the zero size.
example {κ : ℝ} (hκ : 2 < κ) : ∃ m : ℕ, 0 < m ∧
    4 * (0 : ℕ) * √(m : ℝ) < m ∧
    2 * m / (m - 4 * (0 : ℕ) * √(m : ℝ)) < κ := by
  simpa using (recovered (n := 0) hκ)

-- The strict exponent gap cannot simply be removed/weakened to 2≤κ.
theorem sharp_gap : ¬ ∃ m : ℕ, 16 * (0 : ℕ) ^ 2 < m ∧
    4 * (0 : ℕ) * √(m : ℝ) < m ∧
    2 * m / (m - 4 * (0 : ℕ) * √(m : ℝ)) < (2 : ℝ) := by
  rintro ⟨m, hm, _, hq⟩
  have hm0 : (m : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt (by simpa using hm) : m ≠ 0)
  norm_num [mul_div_cancel_right₀ _ hm0] at hq

#check @exists_nat_gt
#check @Nat.le_ceil
#check @Real.sqrt_sq
#check @mul_lt_mul_of_pos_right
#check @div_lt_iff₀
#print axioms Dimension275.generic
#print axioms Dimension275.coefficient
#print axioms Dimension275.recovered
#print axioms Dimension275.sharp_gap
end Dimension275
'''
(D/'generic-executed.lean.txt').write_text(s);req('generic01','generic-executed.lean.txt','generic-receipt.json')
# Full original actual caller, replacing precisely its one target application by the literal proof.
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()); caller=next(x for x in meta if x['name']=='Roth.exists_roth_parameters_aux')['source'];target=next(x for x in meta if x['name']=='Roth.exists_m')['source']
(D/'caller-excerpt.lean.txt').write_text(caller+'\n')
body=target.split(':= by\n',1)[1]; replacement='(by\n'+''.join('    '+l+'\n' for l in body.splitlines())+'    : ∃ m : ℕ, 16 * f.natDegree ^ 2 < m ∧\n      4 * f.natDegree * √(m : ℝ) < m ∧\n      2 * m / (m - 4 * f.natDegree * √(m : ℝ)) < κ)'
# Use a local exact-signature helper so original n/κ binders are retained, then inline that proof.
inline='  have dimension_choice {n : ℕ} {κ : ℝ} (hκ : 2 < κ) :\n      ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧\n        2 * m / (m - 4 * n * √(m : ℝ)) < κ := by\n'+''.join('  '+l+'\n' for l in body.splitlines())
caller=caller.replace('private lemma exists_roth_parameters_aux','theorem replay').replace(':= by\n',':= by\n'+inline,1).replace(':= exists_m (n := f.natDegree) hκ',':= dimension_choice (n := f.natDegree) hκ')
s=(D/'disk-prefix.lean.txt').read_text()+'\nnamespace Dimension275Caller\nopen Roth\n'+caller+'\nend Dimension275Caller\n#print axioms Dimension275Caller.replay\n'
(D/'callers-executed.lean.txt').write_text(s);req('callers01','callers-executed.lean.txt','callers-receipt.json','diagnostics')
# Negative automation composition is checked independently before any new theorem is declared.
s=prefix+'''
#check_failure Roth.exists_m
namespace Dimension275Composition
example {n : ℕ} {κ : ℝ} (hκ : 2 < κ) :
    ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧
      2 * m / (m - 4 * n * √(m : ℝ)) < κ := by
  fail_if_success exact?
  fail_if_success simp
  fail_if_success aesop
'''+''.join('  '+l+'\n' for l in body.splitlines())+'''
#print axioms Dimension275Composition._example
end Dimension275Composition
'''
s=s.replace('example {n : ℕ}', 'theorem checked {n : ℕ}').replace('Dimension275Composition._example','Dimension275Composition.checked')
(D/'composition-executed.lean.txt').write_text(s);req('composition01','composition-executed.lean.txt','composition-receipt.json')
print('Prepared generic, old recovery/zero/sharp-gap, actual full caller literal-proof inline, composition')
