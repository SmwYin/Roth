from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent
def req(id,src,op):
 s=(D/src).read_bytes();assert max(map(len,s.decode().splitlines()))<=100
 (D/'root-requests'/f'{id}.json').write_text(json.dumps(dict(id=id,operation=op,source=src,source_sha256=hashlib.sha256(s).hexdigest(),receipt=id+'-receipt.json',arguments={}if op=='run_code'else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
s=(D/'modern-executed.lean.txt').read_text().replace('example (x : ℝ) : True','example (_x : ℝ) : True').replace('UniformBound 2 x ↔ (Irrational x ∧ ∀ {p}, LiouvilleWith p x → p ≤ 2)','UniformBound 2 _x ↔ (Irrational _x ∧ ∀ {p}, LiouvilleWith p _x → p ≤ 2)')
s=s.replace('  rw [heq, sub_self, abs_zero] at hp','  simp only [Int.cast_natCast] at hp\n  rw [heq, sub_self, abs_zero] at hp')
s=s.replace('end Diophantine290Modern','''lemma add_rat_iff {t x : ℝ} (r : ℚ) :
    UniformBound t (x + r) ↔ UniformBound t x := by
  simp only [uniform_iff, irrational_add_ratCast_iff, LiouvilleWith.add_rat_iff]
lemma mul_rat_iff {t x : ℝ} {r : ℚ} (hr : r ≠ 0) :
    UniformBound t (x * r) ↔ UniformBound t x := by
  simp only [uniform_iff, irrational_mul_ratCast_iff, hr, true_and,
    LiouvilleWith.mul_rat_iff hr]
-- Complete recovery of the fixed2 integer-denominator formula, using no project imports.
example (x : ℝ) : UniformBound 2 x ↔
    ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
      ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ (2 + ε) < |x - (p : ℝ) / q| := Iff.rfl
#print axioms Diophantine290Modern.add_rat_iff
#print axioms Diophantine290Modern.mul_rat_iff
end Diophantine290Modern''')
(D/'modern2-executed.lean.txt').write_text(s);req('modern02','modern2-executed.lean.txt','run_code')
s=(D/'shape-executed.lean.txt').read_text().replace('example (x : ℝ) : True','example (_x : ℝ) : True').replace('inferInstanceAs (U x)','inferInstanceAs (U _x)')
s=s.replace('''      simpa only [Int.cast_neg, neg_div_neg_eq, abs_of_neg (by exact_mod_cast hneg)] using hh
    · simpa only [abs_of_pos (by exact_mod_cast hpos)] using hb p q hpos''','''      have hqR : (q : ℝ) < 0 := by exact_mod_cast hneg
      rw [abs_of_neg hqR]
      simpa only [Int.cast_neg, neg_div_neg_eq] using hh
    · have hqR : (0 : ℝ) < q := by exact_mod_cast hpos
      rw [abs_of_pos hqR]
      exact hb p q hpos''')
s=s.replace('''    exact ⟨C, hC, fun p q hq ↦ by
      simpa only [abs_of_pos (by exact_mod_cast hq)] using hb p q hq.ne'⟩''','''    refine ⟨C, hC, fun p q hq ↦ ?_⟩
    have hqR : (0 : ℝ) < q := by exact_mod_cast hq
    simpa only [abs_of_pos hqR] using hb p q hq.ne' ''').rstrip()+'\n'
(D/'shape2-executed.lean.txt').write_text(s);req('shape02','shape2-executed.lean.txt','diagnostics')
print('Prepared immutable modern02 and shape02; rejected originals unchanged')
