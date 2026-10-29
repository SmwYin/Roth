from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent

def req(i,op,source=None,receipt=None,args={},**kw):
 r=dict(id=i,operation=op,receipt=receipt or i+'-receipt.json',arguments=args,**kw)
 if source:r.update(source=source,source_sha256=hashlib.sha256((D/source).read_bytes()).hexdigest())
 (D/'root-requests'/ (i+'.json')).write_text(json.dumps(r,indent=2)+'\n')
req('original01','diagnostics','original-executed.lean.txt','original-receipt.json',dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45),original_audit=True)
for form,q in [('current','exists_monic_aeval_eq_zero'),('standard','IsIntegral'),('abstract','natDegree_mul_X_pow')]:
 req('local-'+form,'local_search',receipt='search-'+form+'-local_search.json',args=dict(query=q,project_root='/Users/ramin/LEAN/Roth',limit=30))
s=(D/'isolated-prefix.lean.txt').read_text()+'''#check_failure Roth.exists_monic_aeval_eq_zero
#check IsIntegral
#check Polynomial.natDegree_mul_X_pow
#check Polynomial.Monic.mul
#check Polynomial.monic_X_pow
#check Polynomial.Monic.ne_zero
#check Polynomial.aeval_def
namespace Monic272Generic
open Polynomial
-- Pure padding needs no integral API and uses semirings, even a noncommutative target.
theorem pad {R A : Type*} [CommSemiring R] [Nontrivial R] [Semiring A] [Algebra R A]
    {a : A} {f : R[X]} (hf : f.Monic) (hfa : aeval a f = 0) (N : ℕ) :
    ∃ g : R[X], g.Monic ∧ aeval a g = 0 ∧ N ≤ g.natDegree := by
  refine ⟨f * X ^ N, hf.mul (monic_X_pow N), ?_, ?_⟩
  · rw [map_mul, hfa, zero_mul]
  · simp [hf.ne_zero]
-- Pinned IsIntegral is defined for rings, so the witness form is the semiring weakening.
theorem integral {R A : Type*} [CommRing R] [Nontrivial R] [Ring A] [Algebra R A]
    {a : A} (ha : IsIntegral R a) (N : ℕ) :
    ∃ g : R[X], g.Monic ∧ aeval a g = 0 ∧ N ≤ g.natDegree := by
  obtain ⟨f, hf, hfa⟩ := ha
  exact pad hf (by simpa only [aeval_def] using hfa) N
-- Original specialization, retaining all original assumptions and exact result.
theorem original {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree :=
  integral hint 2
-- A nontrivial target is not required: target PUnit admits the same witness padding.
example (N : ℕ) : ∃ g : ℕ[X], g.Monic ∧ aeval (0 : PUnit) g = 0 ∧ N ≤ g.natDegree := by
  exact pad (monic_X_pow 1) (by simp) N
-- Integral integer and rational values are included: no irrationality premise exists.
example (z : ℤ) (N : ℕ) : ∃ f : ℤ[X], f.Monic ∧ aeval (z : ℝ) f = 0 ∧ N ≤ f.natDegree :=
  integral (isIntegral_algebraMap (R := ℤ) (A := ℝ) z) N
example (N : ℕ) : ∃ f : ℤ[X], f.Monic ∧ aeval (0 : ℚ) f = 0 ∧ N ≤ f.natDegree :=
  integral (isIntegral_zero) N
-- A trivial coefficient ring invalidates all positive degree bounds.
example : ¬ ∃ f : PUnit[X], 1 ≤ f.natDegree := by simp
#print axioms pad
#print axioms integral
#print axioms original
end Monic272Generic
'''
(D/'isolated-executed.lean.txt').write_text(s)
req('isolated01','run_code','isolated-executed.lean.txt','isolated-receipt.json')
print('requests prepared; isolated width',max(map(len,s.splitlines())))
