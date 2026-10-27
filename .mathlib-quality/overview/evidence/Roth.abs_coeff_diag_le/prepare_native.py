from pathlib import Path
import json
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
prefix='''namespace MvPolynomial.CoeffDiagConsumers
open Roth MvPolynomial
theorem specialization {σ : Type*} (P : MvPolynomial σ ℤ) {B : ℝ}
    (hB : ∀ k, |(P.coeff k : ℝ)| ≤ B) (n : ℕ) :
    |((diag P).coeff n : ℝ)| ≤ P.support.card * B := by
  classical
  have h0 : 0 ≤ B := (abs_nonneg _).trans (hB 0)
  refine (MvPolynomial.CoeffDiagGeneric.cardinal_fiber P n (fun z : ℤ ↦ |(z : ℝ)|)
    (by simp) (fun a b ↦ by simpa only [Int.cast_add] using abs_add_le (a : ℝ) (b : ℝ))
    (fun k _ ↦ hB k)).trans ?_
  exact mul_le_mul_of_nonneg_right (by exact_mod_cast Finset.card_filter_le _ _) h0
'''
s=(R/'Roth/MainLemma.lean').read_text();start=s.index('private lemma abs_coeff_diag_hasseDeriv_modByMonic_le_aux');end=s.index('private lemma abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux',start)
c=s[start:end].replace('private lemma abs_coeff_diag_hasseDeriv_modByMonic_le_aux','theorem abs_coeff_diag_hasseDeriv_modByMonic_le_aux_replay').replace('(abs_coeff_diag_le _','(specialization _')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 if len('    '+n+',')>100:
  m,d=n.rsplit(' ',1);n=m+'\n      '+d
 names.append('    '+n)
a='  let names : Array Lean.Name := #[\n'+',\n'.join(names)+']\n';(D/'canonical-audit-array.lean.txt').write_text(a)
audit='''run_cmd do
  let env ← Lean.getEnv
'''+a+'''  let unique := names.toList.eraseDups.length
  unless names.size == 293 && unique == 293 do
    throwError "Canonical audit must contain 293 unique names"
  Lean.logInfo m!"COEFF_DIAG_AUDIT_UNIQUE: {unique}"
  let mut present : Nat := 0
  let mut withValue : Nat := 0
  for n in names do
    match env.find? n with
    | none => Lean.logInfo m!"COEFF_DIAG_AUDIT_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        withValue := withValue + 1
        if val.getUsedConstants.any (fun c ↦ c == `Roth.abs_coeff_diag_le) then
          Lean.logInfo m!"COEFF_DIAG_DIRECT_PROOF_CONSUMER: {n}"
  Lean.logInfo
    m!"COEFF_DIAG_AUDIT: requested={names.size}; present={present}; values={withValue}"
'''
(D/'probe-consumers.lean.txt').write_text(prefix+c+'\n#print axioms specialization\n#print axioms abs_coeff_diag_hasseDeriv_modByMonic_le_aux_replay\n'+audit+'end MvPolynomial.CoeffDiagConsumers\n')
(D/'probe-seminorm.lean.txt').write_text('''namespace MvPolynomial.CoeffDiagSeminorm
variable {σ R : Type*} [CommRing R]
theorem seminorm_fiber (P : MvPolynomial σ R) (n : ℕ) (f : AddGroupSeminorm R) :
    f ((aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n) ≤
      ∑ k ∈ P.support.filter (fun k ↦ k.degree = n), f (P.coeff k) := by
  classical
  exact MvPolynomial.CoeffDiagGeneric.subadditive_fiber P n f (by simp) f.add_le
#check @AddGroupSeminorm.add_le
#print axioms seminorm_fiber
end MvPolynomial.CoeffDiagSeminorm
''')
