from pathlib import Path
import json
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth')
s=Path('/private/tmp/roth-overview/norm-mul-raw-clean-executed.lean.txt').read_text()
prefix=s[:s.index('#check_failure')]
s=s[s.index('namespace NormMulRaw'):s.index('#check @MvPolynomial.mul_def')]
s=s.replace('NormMulRaw','NormProdRaw')
s+='''theorem genericProd (size : R → ℝ) (hzero : size 0 = 0)
    (hnonneg : ∀ a, 0 ≤ size a) (hone : size 1 ≤ 1)
    (hadd : ∀ a b, size (a + b) ≤ size a + size b)
    (hmul : ∀ a b, size (a * b) ≤ size a * size b)
    {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ R) :
    sizeSum size (∏ i ∈ s, f i) ≤ ∏ i ∈ s, sizeSum size (f i) := by
  apply Finset.le_prod_of_submultiplicative_of_nonneg (sizeSum size)
    (fun P ↦ Finset.sum_nonneg fun _ _ ↦ hnonneg _) _
    (genericMul size hzero hadd hmul) s f
  simpa only [← MvPolynomial.monomial_zero_one, monomialSize size hzero] using hone
theorem directProd {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    replacement (∏ i ∈ s, f i) ≤ ∏ i ∈ s, replacement (f i) := by
  exact genericProd (fun z : ℤ ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _)
    (by simp) (fun a b ↦ by simpa using abs_add_le (a : ℝ) (b : ℝ))
    (fun a b ↦ by simp [abs_mul]) s f
#check @Finset.le_prod_of_submultiplicative_of_nonneg
#print axioms triangle
#print axioms finiteTriangle
#print axioms monomialSize
#print axioms genericMul
#print axioms direct
#print axioms genericProd
#print axioms directProd
end NormProdRaw
'''
(D/'requested-raw.lean.txt').write_text(prefix+'#check_failure Roth.normOne_prod_le\n'+s)
module=(R/'Roth/CoeffNorm.lean').read_text()
start=module.index('theorem normOne_det_le');end=module.index('/-- Coefficient bound for a Hasse',start)
consumer=module[start:end].strip().replace('theorem normOne_det_le','theorem normOne_det_le_inline')
consumer=consumer.replace(':= normOne_sum_le _ _', ':=\n      normOne_sum_le _ _')
consumer=consumer.replace('(normOne_prod_le Finset.univ fun i ↦ M (τ i) i)', '''(Finset.le_prod_of_submultiplicative_of_nonneg normOne normOne_nonneg
      (by simpa using (normOne_monomial (0 : σ →₀ ℕ) 1).le)
      normOne_mul_le Finset.univ fun i ↦ M (τ i) i)''')
consumer=consumer.replace('using (Finset.', 'using\n      (Finset.').replace('((Finset.prod_le_prod₀', '( (Finset.prod_le_prod₀')
consumer=consumer.replace('fun i _ ↦ hM _ _).trans_eq', 'fun i _ ↦ hM _ _).trans_eq\n        ')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 if len(n)+4>100:n=n.replace(' `','\n      `')
 names.append(n)
array='  let names : Array Lean.Name := #[\n    '+',\n    '.join(names)+']\n'
audit='''run_cmd do
  let env ← Lean.getEnv
'''+array+'''  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "Canonical audit must contain 293 unique names"
  Lean.logInfo m!"PROD_AUDIT_UNIQUE: {unique}"
  let mut present : Nat := 0
  let mut withValue : Nat := 0
  for n in names do
    match env.find? n with
    | none => Lean.logInfo m!"PROD_AUDIT_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        withValue := withValue + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.normOne_prod_le) then
          Lean.logInfo m!"PROD_DIRECT_PROOF_CONSUMER: {n}"
  Lean.logInfo
    m!"PROD_AUDIT_CANONICAL: requested={names.size}; present={present}; values={withValue}"
'''
(D/'canonical-audit-array.lean.txt').write_text(array)
(D/'requested-consumers.lean.txt').write_text('''namespace MvPolynomial.NormProdConsumers
open Roth MvPolynomial
variable {σ : Type*}
'''+consumer+'\n#print axioms normOne_det_le_inline\n'+audit+'end MvPolynomial.NormProdConsumers\n')
for p in D.glob('requested-*.lean.txt'):
 assert all(len(l)<=100 for l in p.read_text().splitlines()),p
