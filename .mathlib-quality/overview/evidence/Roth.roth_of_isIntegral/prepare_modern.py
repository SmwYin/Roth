from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.roth_of_isIntegral');R=Path('/Users/ramin/LEAN/Roth')
prefix=(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
assert hashlib.sha256(prefix.encode()).hexdigest()=='effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc'
main=(R/'Roth/Main.lean').read_text();bounded=main[main.index('theorem approxSet_den_le_finite'):main.index('/-- If `κ\' < κ`')].rstrip().replace('approxSet','pairSet')
s=prefix+'''
#check_failure Roth.roth_of_isIntegral
#check_failure Roth.approxSet
#check @Liouville.exists_pos_real_of_irrational_root
#check @LiouvilleWith.exists_pos
#check @LiouvilleWith.mono
#check @LiouvilleWith.frequently_lt_rpow_neg
#check @LiouvilleWith.irrational
#check @LiouvilleWith.mul_nat_iff
#check @LiouvilleWith.add_rat_iff
namespace Integral287Modern
open Filter
open scoped Filter
-- Scratch mathematical spelling of the pair predicate, using only mathlib operations.
def pairSet (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}
'''+bounded+'''
lemma infinite_of_frequent {α κ : ℝ}
    (hf : ∃ᶠ q : ℕ in atTop, 0 < q ∧ ∃ h : ℤ,
      |α - (h : ℝ) / q| < 1 / (q : ℝ) ^ κ) : (pairSet α κ).Infinite := by
  intro hs
  obtain ⟨N, hN⟩ := (hs.image Prod.snd).bddAbove
  obtain ⟨q, hqN, hq0, h, happ⟩ := ((eventually_gt_atTop N).and_frequently hf).exists
  exact (not_lt_of_ge (hN (Set.mem_image_of_mem Prod.snd ⟨hq0, happ⟩))) hqN
lemma liouville_of_infinite {α κ : ℝ} (hα : Irrational α)
    (hinf : (pairSet α κ).Infinite) : LiouvilleWith κ α := by
  refine ⟨1, frequently_atTop.2 fun N ↦ ?_⟩
  obtain ⟨⟨h, q⟩, hmem, hnot⟩ :=
    (hinf.sdiff (pairSet_den_le_finite α κ N)).nonempty
  have hNq : N < q := not_le.1 fun hq ↦ hnot ⟨hmem, hq⟩
  exact ⟨q, hNq.le, h, hα.ne_rational h q, hmem.2⟩
lemma exponent_iff {α : ℝ} (hα : Irrational α) :
    (∀ {κ : ℝ}, (pairSet α κ).Infinite → κ ≤ 2) ↔
      ∀ {p : ℝ}, LiouvilleWith p α → p ≤ 2 := by
  constructor
  · intro h p hp
    by_contra! h2
    have hqp : (p + 2) / 2 < p := by linarith
    have hf := hp.frequently_lt_rpow_neg hqp
    have hinf : (pairSet α ((p + 2) / 2)).Infinite := by
      apply infinite_of_frequent
      refine ((eventually_gt_atTop 0).and_frequently hf).mono ?_
      rintro q ⟨hq, m, _, hm⟩
      exact ⟨hq, m, by simpa [Real.rpow_neg, one_div] using hm⟩
    have := h hinf
    linarith
  · intro h κ hinf
    exact h (liouville_of_infinite hα hinf)
lemma integral_modern_of_classical
    (hR : ∀ {α : ℝ}, Irrational α → IsIntegral ℤ α →
      ∀ {κ : ℝ}, (pairSet α κ).Infinite → κ ≤ 2)
    {α p : ℝ} (hint : IsIntegral ℤ α) (hp : LiouvilleWith p α) : p ≤ 2 := by
  by_contra! h2
  have hα := hp.irrational (by linarith)
  exact ((exponent_iff hα).mp (hR hα hint) hp).not_gt h2
lemma recover_classical
    (hR : ∀ {α p : ℝ}, IsIntegral ℤ α → LiouvilleWith p α → p ≤ 2)
    {α κ : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α)
    (hinf : (pairSet α κ).Infinite) : κ ≤ 2 :=
  (exponent_iff hα).mpr (hR hint) hinf
-- Existing generic order automation and Liouville irrationality do not supply Roth's bound.
example {α κ : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α)
    (hinf : (pairSet α κ).Infinite) : True := by
  fail_if_success
    have : κ ≤ 2 := by exact?
  fail_if_success
    have : κ ≤ 2 := by aesop
  trivial
example : LiouvilleWith 1 (0 : ℝ) := liouvilleWith_one 0
#print axioms Integral287Modern.exponent_iff
#print axioms Integral287Modern.integral_modern_of_classical
#print axioms Integral287Modern.recover_classical
end Integral287Modern
'''
assert max(map(len,s.splitlines()))<=100
assert all(l==l.rstrip()for l in s.splitlines())
(D/'modern-executed.lean.txt').write_text(s)
(D/'root-requests/modern01.json').write_text(json.dumps(dict(id='modern01',operation='run_code',source='modern-executed.lean.txt',source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='modern01-receipt.json',arguments={},extra_import_authorization='root287 effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc'),indent=2)+'\n')
print('Prepared mathlib-only modern01; exact approved19 prefix; 100char gate PASS')
