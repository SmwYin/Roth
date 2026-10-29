from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
prefix=(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
old=Path('/private/tmp/roth-overview/assess/Roth.roth/modern2-executed.lean.txt').read_text()
helpers=old[old.index('def pairSet'):old.index('lemma algebraic_modern_of_classical')]
# Parameterize only the theorem's exponent cutoff, leaving the literal half operation intact.
a,b=helpers.split('lemma exponent_iff',1)
b=b.replace('{α : ℝ}', '{α t : ℝ}').replace('κ ≤ 2','κ ≤ t').replace('p ≤ 2','p ≤ t').replace('(p + 2)','(p + t)')
code=prefix+'''
#check_failure LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
#check_failure Roth.approxSet
#check @LiouvilleWith.exists_pos
#check @LiouvilleWith.mono
#check @LiouvilleWith.frequently_lt_rpow_neg
#check @LiouvilleWith.irrational
#check @LiouvilleWith.add_rat_iff
#check @LiouvilleWith.mul_rat_iff
namespace Diophantine290Modern
open Real Filter
open scoped Filter
-- Scratch parameterized semantic property, with 2 recovered by specialization.
def UniformBound (t x : ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
    ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ (t + ε) < |x - (p : ℝ) / q|
example (x : ℝ) : True := by
  fail_if_success
    have : UniformBound 2 x ↔ (Irrational x ∧ ∀ {p}, LiouvilleWith p x → p ≤ 2) := by exact?
  trivial
'''+a+'lemma exponent_iff'+b+'''
lemma uniform_irrational {t x : ℝ} (h : UniformBound t x) : Irrational x := by
  rintro ⟨r, rfl⟩
  obtain ⟨C, hC, hb⟩ := h 1 zero_lt_one
  have hp := hb r.num r.den (by exact_mod_cast r.den_pos)
  have heq : (r.num : ℝ) / r.den = (r : ℝ) := (Rat.cast_def r).symm
  rw [heq, sub_self, abs_zero] at hp
  exact (div_pos hC (rpow_pos_of_pos (by positivity) _)).not_gt hp
lemma finite_uniform {x κ : ℝ} (hx : Irrational x) (hs : (pairSet x κ).Finite) :
    ∃ C : ℝ, 0 < C ∧ ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ κ < |x - (p : ℝ) / q| := by
  let f : ℤ × ℕ → ℝ := fun a ↦ |x - (a.1 : ℝ) / a.2| * (a.2 : ℝ) ^ κ
  obtain ⟨a, ha, hmin⟩ := Set.exists_min_image _ f (hs.insert (0, 1))
    (Set.insert_nonempty (0, 1) _)
  have haq : 0 < a.2 := by
    rcases ha with rfl | ha <;> first | exact ha.1 | norm_num
  have hfa : 0 < f a := mul_pos
    (abs_pos.mpr (sub_ne_zero.mpr (by simpa using hx.ne_rational a.1 a.2)))
    (rpow_pos_of_pos (by positivity) _)
  refine ⟨min (1 / 2) (f a / 2), by positivity, fun p q hq ↦ ?_⟩
  lift q to ℕ using hq.le
  have hq' : 0 < (q : ℝ) ^ κ := rpow_pos_of_pos (by exact_mod_cast hq) _
  rw [Int.cast_natCast, div_lt_iff₀ hq']
  by_cases hmem : (p, q) ∈ pairSet x κ
  · exact (min_le_right _ _).trans_lt
      ((half_lt_self hfa).trans_le (hmin (p, q) (Set.mem_insert_of_mem _ hmem)))
  · apply ((min_le_left _ _).trans_lt (by norm_num : (1 : ℝ) / 2 < 1)).trans_le
    exact le_of_not_gt fun h ↦ hmem ⟨by exact_mod_cast hq, (lt_div_iff₀ hq').mpr h⟩
lemma gap {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by
  obtain ⟨N, hN⟩ := Filter.eventually_atTop.1
    (((tendsto_rpow_atTop (sub_pos.2 hκ)).comp tendsto_natCast_atTop_atTop).eventually_gt_atTop M)
  refine ⟨N, fun q hq ↦ ?_⟩
  have hq0 : (0 : ℝ) < q := by exact_mod_cast (Nat.zero_le N).trans_lt hq
  rw [div_lt_iff₀ (Real.rpow_pos_of_pos hq0 κ), one_div_mul_eq_div, ← Real.rpow_sub hq0]
  exact hN q hq.le
lemma uniform_pair_iff {t x : ℝ} (hx : Irrational x) :
    UniformBound t x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t := by
  refine ⟨fun h κ hinf ↦ le_of_not_gt fun hκ ↦ ?_, fun h ε hε ↦ ?_⟩
  · obtain ⟨C, hC, hbound⟩ := h ((κ - t) / 2) (by linarith)
    obtain ⟨Q, hQ⟩ := gap (M := 1 / C) (by linarith : t + (κ - t) / 2 < κ)
    obtain ⟨⟨p, q⟩, hpq, hq⟩ :=
      (hinf.sdiff (pairSet_den_le_finite x κ Q)).nonempty
    have hgap : 1 / (q : ℝ) ^ κ < C / (q : ℝ) ^ (t + (κ - t) / 2) := by
      simpa [div_eq_mul_inv, ← mul_assoc, hC.ne'] using
        mul_lt_mul_of_pos_left (hQ q (lt_of_not_ge fun h ↦ hq ⟨hpq, h⟩)) hC
    exact (hpq.2.trans hgap).not_gt (by simpa using hbound p q (by exact_mod_cast hpq.1))
  · apply finite_uniform hx
    exact Set.not_infinite.mp fun hinf ↦ (by linarith : ¬ (t + ε ≤ t)) (h hinf)
lemma uniform_iff {t x : ℝ} :
    UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t := by
  constructor
  · intro h
    exact ⟨uniform_irrational h, (exponent_iff (uniform_irrational h)).mp
      ((uniform_pair_iff (uniform_irrational h)).mp h)⟩
  · rintro ⟨hx, h⟩
    exact (uniform_pair_iff hx).mpr ((exponent_iff hx).mpr h)
lemma cutoff_mono {s t x : ℝ} (h : UniformBound s x) (hst : s ≤ t) : UniformBound t x := by
  rw [uniform_iff] at h ⊢
  exact ⟨h.1, fun hp ↦ (h.2 hp).trans hst⟩
lemma rational_cutoff (r : ℚ) : ∀ {p : ℝ}, LiouvilleWith p (r : ℝ) → p ≤ 2 := by
  intro p hp
  by_contra! h
  exact (hp.irrational (by linarith)).ne_rat r rfl
example : ¬ UniformBound 2 0 := by
  intro h
  exact (uniform_irrational h).ne_rat 0 (by norm_num)
example : LiouvilleWith 1 (0 : ℝ) := liouvilleWith_one 0
example {p : ℝ} (hp : p ≤ 1) : LiouvilleWith p (0 : ℝ) := (liouvilleWith_one 0).mono hp
#print axioms Diophantine290Modern.uniform_iff
#print axioms Diophantine290Modern.cutoff_mono
#print axioms Diophantine290Modern.rational_cutoff
end Diophantine290Modern
'''
assert max(map(len,code.splitlines()))<=100,max(map(len,code.splitlines()))
(D/'modern-executed.lean.txt').write_text(code)
(D/'root-requests/modern01.json').write_text(json.dumps(dict(id='modern01',operation='run_code',source='modern-executed.lean.txt',source_sha256=hashlib.sha256(code.encode()).hexdigest(),receipt='modern01-receipt.json',arguments={}),indent=2)+'\n')
print('Prepared modern01 parameterized iff incl irrationality, recovery and cutoff monotonicity')
