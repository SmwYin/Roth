from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
meta=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
def source(n):return next(x['source'] for x in meta if x['name']==n)
prefix=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_text()
s=prefix+'''import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith

#check_failure Roth.reduction
#check_failure Roth.approxSet
namespace Reduction271Generic
'''
s+=source('Roth.approxSet')+'\n\n'
for n in ['Roth.exists_nat_mul_isIntegral','Roth.approxSet_den_le_finite','Roth.eventually_div_rpow_lt']:
 s+=source(n)+'\n\n'
s+='''theorem scaling {α κ κ' : ℝ} (M : ℕ) (hM0 : 0 < M) (hκ : κ' < κ)
    (hinf : (approxSet α κ).Infinite) : (approxSet (M * α) κ').Infinite := by
  obtain ⟨Q₀, hQ₀⟩ := eventually_div_rpow_lt (M := M) hκ
  refine ((hinf.sdiff (approxSet_den_le_finite α κ Q₀)).image
    ((mul_right_injective₀ (by exact_mod_cast hM0.ne' : (M : ℤ) ≠ 0)).prodMap
      Function.injective_id).injOn).mono ?_
  rintro _ ⟨⟨h, q⟩, ⟨⟨hq0, happ⟩, hnot⟩, rfl⟩
  refine ⟨hq0, ?_⟩
  dsimp only [Prod.map, id]
  push_cast
  rw [mul_div_assoc, ← mul_sub, abs_mul, Nat.abs_cast]
  calc (M : ℝ) * |α - h / q| < M / (q : ℝ) ^ κ := by
        simpa only [mul_one_div] using mul_lt_mul_of_pos_left happ (by positivity : (0 : ℝ) < M)
    _ < 1 / (q : ℝ) ^ κ' := hQ₀ q (not_le.1 fun hc ↦ hnot ⟨⟨hq0, happ⟩, hc⟩)

theorem threshold {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α)
    {t κ : ℝ} (hκ : t < κ) (hinf : (approxSet α κ).Infinite) :
    ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ t < κ' ∧ κ' < κ ∧
      (approxSet α' κ').Infinite := by
  obtain ⟨M, hM0, hMint⟩ := exists_nat_mul_isIntegral halg
  refine ⟨M * α, (κ + t) / 2, hα.natCast_mul hM0.ne', hMint,
    by linarith, by linarith, scaling M hM0 (by linarith) hinf⟩

theorem recovery {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α)
    {κ : ℝ} (hκ : 2 < κ) (hinf : (approxSet α κ).Infinite) :
    ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧
      (approxSet α' κ').Infinite := by
  obtain ⟨a, k, ha, hi, ht, -, hs⟩ := threshold hα halg hκ hinf
  exact ⟨a, k, ha, hi, ht, hs⟩

theorem liouville_threshold {α κ : ℝ} (hα : Irrational α)
    (halg : IsAlgebraic ℚ α) (h : LiouvilleWith κ α) :
    ∃ α' : ℝ, Irrational α' ∧ IsIntegral ℤ α' ∧ LiouvilleWith κ α' := by
  obtain ⟨M, hM, hi⟩ := exists_nat_mul_isIntegral halg
  exact ⟨M * α, hα.natCast_mul hM.ne', hi, h.nat_mul hM.ne'⟩

#check @LiouvilleWith.nat_mul
#check @LiouvilleWith.frequently_lt_rpow_neg
#check @LiouvilleWith.exists_pos
#check @LiouvilleWith.mono
#print axioms scaling
#print axioms threshold
#print axioms recovery
#print axioms liouville_threshold
end Reduction271Generic
'''
p=D/'isolated-executed.lean.txt';p.write_text(s)
r=dict(id='isolated01',operation='run_code',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='isolated-receipt.json',arguments={})
(D/'root-requests/isolated01.json').write_text(json.dumps(r,indent=2))
print(max(map(len,s.splitlines())),len(s.splitlines()))
