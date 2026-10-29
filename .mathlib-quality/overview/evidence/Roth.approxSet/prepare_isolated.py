from pathlib import Path
import re,json,hashlib
D=Path(__file__).resolve().parent;R=Path.cwd();prefix=(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.NumberTheory.DiophantineApproximation.Basic\n'+'import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n'
(D/'isolated-prefix20.lean.txt').write_text(prefix)
auth=dict(authorized_by='root',scope='canonical267 only',unchanged_shared18=True,unchanged_disk9=True,message='Authorized267 ONLY isolated20 = stable18 + DiophantineApproximation.Basic + Transcendental.Liouville.LiouvilleWith. Prior19 superseded within267 only.',prefix_sha256=hashlib.sha256(prefix.encode()).hexdigest())
(D/'root-prefix-scope-authorization.json').write_text(json.dumps(auth,indent=2)+'\n')
body='''
#check_failure Roth.approxSet
#check @Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational
#check @Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational
#check @Rat.finite_rat_abs_sub_lt_one_div_den_sq
#check @LiouvilleWith
#check @LiouvilleWith.exists_pos
#check @LiouvilleWith.frequently_lt_rpow_neg
#print LiouvilleWith
namespace Approx267Isolated
open Filter
open scoped Filter
noncomputable def approxWith (α : ℝ) (ψ : ℕ → ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < ψ hq.2}
noncomputable def approxC (α κ C : ℝ) : Set (ℤ × ℕ) :=
  approxWith α (fun q ↦ C / (q : ℝ) ^ κ)
theorem bounded_den_finite (α : ℝ) (ψ : ℕ → ℝ) (Q₀ : ℕ) :
    {hq ∈ approxWith α ψ | hq.2 ≤ Q₀}.Finite := by
  set S : ℝ := ∑ q ∈ Finset.Icc 1 Q₀, |ψ q|
  set K : ℤ := ⌈(Q₀ : ℝ) * (|α| + S)⌉
  refine (Finset.finite_toSet (Finset.Icc (-K) K ×ˢ Finset.Icc 1 Q₀)).subset ?_
  rintro ⟨h, q⟩ ⟨⟨hq0, happ⟩, hqQ⟩
  simp only at hq0 happ hqQ
  have hqR : (0 : ℝ) < q := by exact_mod_cast hq0
  have hdiv : |(h : ℝ) / q| ≤ |α| + S := by
    rw [abs_sub_comm] at happ
    linarith only [happ, le_abs_self (ψ q), abs_sub_abs_le_abs_sub ((h : ℝ) / q) α,
      Finset.single_le_sum (f := fun q : ℕ ↦ |ψ q|) (fun i _ ↦ abs_nonneg _)
        (Finset.mem_Icc.2 ⟨hq0, hqQ⟩)]
  have habs : |(h : ℝ)| ≤ Q₀ * (|α| + S) := by
    have hqQR : (q : ℝ) ≤ Q₀ := by exact_mod_cast hqQ
    have hh : |(h : ℝ)| / q ≤ |α| + S := by simpa [abs_div] using hdiv
    simpa [mul_comm] using ((div_le_iff₀ hqR).1 hh).trans
      (mul_le_mul_of_nonneg_left hqQR ((abs_nonneg _).trans hdiv))
  have hK' : |h| ≤ K := by
    have : ((|h| : ℤ) : ℝ) ≤ K := by
      rw [Int.cast_abs]
      exact habs.trans (Int.le_ceil _)
    exact_mod_cast this
  simp only [Finset.coe_product, Set.mem_prod, Finset.coe_Icc, Set.mem_Icc]
  exact ⟨abs_le.1 hK', hq0, hqQ⟩
theorem infinite_iff_frequently (α : ℝ) (ψ : ℕ → ℝ) :
    (approxWith α ψ).Infinite ↔
      ∃ᶠ q : ℕ in atTop, ∃ h : ℤ, (h, q) ∈ approxWith α ψ := by
  rw [Filter.frequently_atTop']
  constructor
  · intro hi Q
    obtain ⟨⟨h, q⟩, hmem, hn⟩ := (hi.sdiff (bounded_den_finite α ψ Q)).nonempty
    exact ⟨q, not_le.mp (fun hq ↦ hn ⟨hmem, hq⟩), h, hmem⟩
  · intro hf hfin
    obtain ⟨Q, hQ⟩ := (hfin.image Prod.snd).bddAbove
    obtain ⟨q, hq, h, hm⟩ := hf Q
    exact hq.not_ge (hQ ⟨(h, q), hm, rfl⟩)
theorem liouvilleWith_iff {α κ : ℝ} (hα : Irrational α) :
    LiouvilleWith κ α ↔ ∃ C : ℝ, (approxC α κ C).Infinite := by
  constructor
  · rintro ⟨C, hC⟩
    refine ⟨C, (infinite_iff_frequently _ _).2 ?_⟩
    refine ((Filter.eventually_gt_atTop 0).and_frequently hC).mono ?_
    rintro q ⟨hq, h, _, hh⟩
    exact ⟨h, hq, hh⟩
  · rintro ⟨C, hC⟩
    refine ⟨C, ((infinite_iff_frequently _ _).1 hC).mono ?_⟩
    rintro q ⟨h, _, hh⟩
    exact ⟨h, by simpa using hα.ne_rational h q, hh⟩
theorem dirichlet_endpoint {α : ℝ} (hα : Irrational α) :
    {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ (2 : ℝ)}.Infinite := by
  simpa only [Real.rpow_two] using
    Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational hα
theorem zero_rat_endpoint :
    {x : ℚ | |(0 : ℝ) - x| < 1 / (x.den : ℝ) ^ (2 : ℝ)}.Finite := by
  apply Set.not_infinite.mp
  intro hi
  apply (show ¬ Irrational (0 : ℝ) by simp)
  apply (Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational 0).mp
  simpa only [Real.rpow_two] using hi
-- A candidate named set is a diagnostic witness; automation reproducing its literal
-- comprehension is not evidence of an existing semantic Diophantine approximation API.
example (α κ : ℝ) (witness : Set (ℤ × ℕ))
    (hw : witness = {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}) :
    approxC α κ 1 = witness := by
  rw [hw]
  rfl
end Approx267Isolated
'''
checks='\n'.join('#print axioms Approx267Isolated.'+n for n in re.findall(r'^theorem (\w+)',body,re.M))
whole=prefix+body+checks+'\n'
assert max(map(len,whole.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(whole)
print('Prepared isolated20',len(whole.splitlines()),'lines')
