from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.normOne_sum_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
shutil.copyfile(R/'Roth/CoeffNorm.lean',D/'source-module.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[83]['name']==N
out('canonical-order.json',dict(index=84,total=len(order),entry=order[83],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
# Stable thirteen-import prefix, fresh target-specific Roth-free proof.
old=Path('/private/tmp/roth-overview/norm-triangle-raw-executed.lean.txt').read_text()
raw=old.split('namespace MvPolynomial.NormAddGenerality')[0].replace('#check_failure Roth.normOne_add_le','#check_failure Roth.normOne_sum_le').replace('NormAddRaw','NormSumRaw')
raw+='''namespace NormSumRaw
 theorem genericFinite {κ ι M N : Type*} [AddCommMonoid M] [AddCommMonoid N]
    [Preorder N] [IsOrderedAddMonoid N] (size : κ → M → N)
    (hzero : ∀ i, size i 0 = 0)
    (hadd : ∀ i a b, size i (a + b) ≤ size i a + size i b)
    (s : Finset ι) (f : ι → κ →₀ M) :
    (∑ i ∈ s, f i).sum size ≤ ∑ i ∈ s, (f i).sum size :=
  Finset.le_sum_of_subadditive (fun p : κ →₀ M ↦ p.sum size)
    (by simp) (generic size hzero hadd) s f
#check @Finset.le_sum_of_subadditive
#check @norm_sum_le
#print axioms genericFinite
end NormSumRaw
'''
(D/'requested-raw.lean.txt').write_text(raw)
# Exact persistent project form, plus every explicit consumer with only sum wrapper inlined.
src=(R/'Roth/CoeffNorm.lean').read_text();parts=[]
for name,nxt in [('normOne_mul_le','normOne_prod_le'),('normOne_det_le','abs_coeff_hasseDeriv_le'),('normOne_hasseDeriv_le','diag')]:
 start=src.index('theorem '+name); end=src.index('/--',start)
 part=src[start:end].replace('theorem '+name,'theorem '+name+'_inline')
 part=part.replace('normOne_sum_le _ _','Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le _ _')
 parts.append(part+'#print axioms '+name+'_inline\n')
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='  let names : Array Lean.Name := #[\n    '+',\n    '.join(names)+']\n'
(D/'canonical-audit-array.lean.txt').write_text(array)
audit='run_cmd do\n  let env ← Lean.getEnv\n'+array+'  let unique := names.toList.eraseDups.length\n  unless unique == 293 do\n    throwError "Canonical audit must contain 293 unique names"\n  Lean.logInfo m!"SUM_AUDIT_UNIQUE: {unique}"\n  let mut present : Nat := 0\n  let mut withValue : Nat := 0\n  for n in names do\n    match env.find? n with\n    | none => Lean.logInfo m!"SUM_AUDIT_NOT_LOADED: {n}"\n    | some ci =>\n      present := present + 1\n      match ci.value? (allowOpaque := true) with\n      | none => pure ()\n      | some val =>\n        withValue := withValue + 1\n        if val.getUsedConstants.any (fun c ↦ c == `Roth.normOne_sum_le) then\n          Lean.logInfo m!"SUM_DIRECT_PROOF_CONSUMER: {n}"\n  Lean.logInfo m!"SUM_AUDIT_CANONICAL: requested={names.size}; present={present}; values={withValue}"\n'
consumer='''namespace MvPolynomial.NormSumConsumers
open Roth
variable {σ : Type*}
'''+''.join(parts)+audit+'end MvPolynomial.NormSumConsumers\n'
(D/'requested-consumers.lean.txt').write_text(consumer)
print('Prepared fresh raw and full explicit consumers plus canonical audit; 17 hashes match.')
