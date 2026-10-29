from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;P=D.parent/'LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'
s=(P/'modern3-executed.lean.txt').read_text().replace('Diophantine290Modern','Equivalence292Modern')
s=s.replace('end Equivalence292Modern','''lemma rational_pair_infinite (r : ℚ) (κ : ℝ) : (pairSet (r : ℝ) κ).Infinite := by
  intro hs
  obtain ⟨N, hN⟩ := (hs.image Prod.snd).bddAbove
  let q : ℕ := r.den * (N + 1)
  let p : ℤ := r.num * (N + 1)
  have hq : 0 < q := Nat.mul_pos r.den_pos (Nat.succ_pos N)
  have heq : (p : ℝ) / q = (r : ℝ) := by
    dsimp [p, q]
    push_cast
    rw [mul_div_mul_right _ _ (by positivity : (N : ℝ) + 1 ≠ 0)]
    exact (Rat.cast_def r).symm
  have hm : (p, q) ∈ pairSet (r : ℝ) κ := by
    refine ⟨hq, ?_⟩
    rw [heq, sub_self, abs_zero]
    exact div_pos zero_lt_one (rpow_pos_of_pos (by exact_mod_cast hq) κ)
  have hle : q ≤ N := hN (Set.mem_image_of_mem Prod.snd hm)
  have hd := r.den_pos
  dsimp [q] at hle
  nlinarith
lemma pair_bound_irrational {t x : ℝ}
    (h : ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t) : Irrational x := by
  rintro ⟨r, rfl⟩
  have hh := h (rational_pair_infinite r (t + 1))
  linarith
lemma uniform_pair_iff_all_real {t x : ℝ} :
    UniformBound t x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t := by
  constructor
  · intro h
    exact (uniform_pair_iff (uniform_irrational h)).mp h
  · intro h
    exact (uniform_pair_iff (pair_bound_irrational h)).mpr h
lemma pair_liouville_iff_all_real {t x : ℝ} :
    (∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t) ↔
      Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t := by
  exact uniform_pair_iff_all_real.symm.trans uniform_iff
lemma rational_not_pair_bound (r : ℚ) (t : ℝ) :
    ¬ (∀ {κ : ℝ}, (pairSet (r : ℝ) κ).Infinite → κ ≤ t) := by
  intro h
  exact (pair_bound_irrational h).ne_rat r rfl
lemma weak_uniform_iff {t x : ℝ} : UniformBound t x ↔
    ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
      ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ (t + ε) ≤ |x - (p : ℝ) / q| := by
  constructor
  · intro h ε hε
    obtain ⟨C, hC, hb⟩ := h ε hε
    exact ⟨C, hC, fun p q hq ↦ (hb p q hq).le⟩
  · intro h ε hε
    obtain ⟨C, hC, hb⟩ := h ε hε
    refine ⟨C / 2, by positivity, fun p q hq ↦ ?_⟩
    exact (div_lt_div_of_pos_right (half_lt_self hC)
      (rpow_pos_of_pos (by exact_mod_cast hq) _)).trans_le (hb p q hq)
#print axioms Equivalence292Modern.uniform_pair_iff_all_real
#print axioms Equivalence292Modern.pair_liouville_iff_all_real
#print axioms Equivalence292Modern.weak_uniform_iff
end Equivalence292Modern''')
assert max(map(len,s.splitlines()))<=100
(D/'modern-executed.lean.txt').write_text(s.rstrip()+'\n')
req=dict(id='modern01',operation='run_code',source='modern-executed.lean.txt',source_sha256=hashlib.sha256((D/'modern-executed.lean.txt').read_bytes()).hexdigest(),receipt='modern01-receipt.json',arguments={})
(D/'root-requests/modern01.json').write_text(json.dumps(req,indent=2)+'\n')
print('Prepared modern01 exact19, generic all-real cutoff iff with rational countercases and weak strict bridge')
