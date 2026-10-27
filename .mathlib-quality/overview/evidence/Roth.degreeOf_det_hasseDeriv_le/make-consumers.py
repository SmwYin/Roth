from pathlib import Path
import json
D=Path(__file__).resolve().parent; R=Path('/Users/ramin/LEAN/Roth')
s='''namespace MvPolynomial.DetDegreeConsumers
open Roth
variable {σ R ι : Type*} [CommRing R] [Fintype ι] [DecidableEq ι]
theorem hasse_generic (E : ι → ι → (σ →₀ ℕ)) (P : MvPolynomial σ R) (j : σ)
    {b : ℕ} (hP : degreeOf j P ≤ b) :
    degreeOf j (Matrix.of fun μ ν ↦ hasseDeriv (E μ ν) P).det ≤ Fintype.card ι * b := by
  classical
  rw [Matrix.det_apply']
  refine (degreeOf_sum_le _ _ _).trans (Finset.sup_le fun τ _ ↦ ?_)
  refine (degreeOf_C_mul_le _ j (Equiv.Perm.sign τ : R)).trans ?_
  refine (degreeOf_prod_le _ _ _).trans ?_
  simpa using Finset.sum_le_sum (s := Finset.univ)
    (fun i _ ↦ (degreeOf_hasseDeriv_le j (E (τ i) i) P).trans hP)
theorem specialization {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ))
    (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) (j : σ) :
    degreeOf j (Matrix.of fun μ ν ↦ hasseDeriv (E μ ν) P).det ≤ l * r j := by
  simpa using hasse_generic E P j (hP j)
'''
# Entire caller, independent of assessed target.
t=(R/'Roth/Separation.lean').read_text();t=t[t.index('theorem exists_det_eq_mul [Finite τ]'):t.index('\nend Roth',t.index('theorem exists_det_eq_mul [Finite τ]'))]
t=t.replace('theorem exists_det_eq_mul','theorem caller').replace('exact degreeOf_det_hasseDeriv_le','exact specialization').replace('exists_rat_factors_det_hasseDeriv_aux','_private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux')
s+='variable {τ : Type*}\n'+t+'\n#print axioms hasse_generic\n#print axioms specialization\n#print axioms caller\n'
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
(D/'canonical-audit-array.lean.txt').write_text(array+'\n')
s+='''run_cmd do
  let env ← Lean.getEnv
  '''+array+'''
  let unique := (names.toList.eraseDups).length
  unless names.size == 293 && unique == 293 do
    throwError "DET_DEGREE_BAD_CANONICAL_ARRAY"
  let mut present := 0
  let mut values := 0
  for n in names do
    match env.find? n with
    | none => throwError "DET_DEGREE_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.degreeOf_det_hasseDeriv_le) then
          Lean.logInfo m!"DET_DEGREE_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"DET_DEGREE_AUDIT: requested={names.size}; unique={unique}"
  Lean.logInfo m!"DET_DEGREE_AUDIT_PRESENT: present={present}; values={values}"
end MvPolynomial.DetDegreeConsumers
'''
# Wrap only the canonical literal's comma-separated tokens to satisfy line width.
s=s.replace(array,'\n    '.join([array[:array.index('#[')+2]]+[(n+(',' if k<len(names)-1 else ' ]')) for k,n in enumerate(names)]))
(D/'probe-consumers.lean.txt').write_text(s)
