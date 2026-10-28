from pathlib import Path
import json,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd()
iso=(D/'det207-isolated-executed.lean.txt').read_text().split('namespace Det207\n')[1]
iso='namespace Det207\n'+iso
helper='''
namespace Det207Project
open Roth MvPolynomial
variable {σ : Type*} [Fintype σ]

theorem indexDet {n : Type*} [Fintype n] [DecidableEq n]
    (M : Matrix n n (MvPolynomial σ ℝ)) (α : σ → ℝ) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (row col : n → ℝ) (hdet : M.det ≠ 0)
    (he : ∀ i j, M i j ≠ 0 → col j - row i ≤ index (M i j) α r) :
    ∑ j, col j - ∑ i, row i ≤ index M.det α r := by
  classical
  apply Det207.lowerDet (fun P ↦ index P α r) ?_ ?_ ?_ M row col hdet he
  · intro ι _ f c hn hf
    exact le_index_sum hn fun i _ ↦ hf i
  · intro ι _ f hf
    exact index_prod Finset.univ (fun i _ ↦ hf i) α hr
  · intro u x
    simpa only [map_intCast] using index_C_mul (Int.cast_ne_zero.2 (Units.ne_zero u)) x α r

variable {τ : Type*} [Fintype τ]
'''
theta=(R/'Roth/Theta.lean').read_text();target=theta.split('theorem sum_max_sub_le_index_det',1)[1].split('\nomit [DecidableEq τ] in\nprivate lemma index_separated',1)[0]
weak='theorem weak'+target
weak=weak.replace('    (hD : ∀ μ, (D μ).degree ≤ μ) (hdet :','    (hdet :')
weak=weak.replace('(hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ)', '(hδ : ∀ μ, weight (r ∘ some) (D μ) ≤ δ)')
weak=weak.replace('have h2 := hδ (D μ) ((hD μ).trans (Nat.le_sub_one_of_lt μ.isLt))','have h2 := hδ μ')
head=weak.split('  rw [Matrix.det_apply\'] at hdet ⊢')[0]
weak=head+'''  have h := indexDet (Matrix.of E) α hr (fun _ ↦ δ)
    (fun ν ↦ max 0 (index R α r - ν / r none)) hdet hterm
  rw [← Fin.sum_univ_eq_sum_range (fun ν : ℕ ↦ max 0 (index R α r - ν / r none)) l]
  simpa only [Fin.sum_const, nsmul_eq_mul] using h

#print axioms indexDet
#print axioms weak
end Det207Project
'''
# Full declaring module replay, retaining its imports through the unchanged nine-import disk context.
body=theta[theta.index('namespace Roth'):].replace('namespace Roth\n','namespace Det207Replay\nopen Roth\n',1)
body=body.rsplit('end Roth',1)[0]+'end Det207Replay\n'
start=body.index('theorem sum_max_sub_le_index_det');pstart=body.index(' := by\n',start)
pend=body.index('\nomit [DecidableEq τ] in\nprivate lemma index_separated',pstart)
body=body[:pstart]+''' := by
  exact Det207Project.weak D hdet α hr
    (fun μ ↦ hδ (D μ) ((hD μ).trans (Nat.le_sub_one_of_lt μ.isLt)))
'''+body[pend:]
# A separate replay of the complete actual caller consumes the weakened signature directly.
cstart=body.index('theorem index_le_lem6');cend=body.index('\nomit [DecidableEq τ] in',cstart+1)
caller='omit [DecidableEq τ] in\n'+body[cstart:cend].replace('theorem index_le_lem6','theorem directWeakCaller',1)
caller=caller.replace('sum_max_sub_le_index_det D hD','Det207Project.weak D')
caller=caller.replace('(fun d hd ↦ weight_le_delta_aux hδ0 hratio (hd.trans (Nat.sub_le_iff_le_add.2 hl\')))','(fun μ ↦ weight_le_delta_aux hδ0 hratio\n      (((hD μ).trans (Nat.le_sub_one_of_lt μ.isLt)).trans (Nat.sub_le_iff_le_add.2 hl\')))')
body=body.replace('end Lemma6\n',caller+'\n#print axioms index_le_lem6\n#print axioms directWeakCaller\nend Lemma6\n')
orig=(D/'det207-original-executed.lean.txt').read_text();prefix=orig.split('#check @Roth.')[0];audit=orig[orig.index('namespace Det207Audit'):]
guards="""
namespace Det207Guards
open Roth MvPolynomial

theorem indexX : index (X () : MvPolynomial Unit ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 1 := by
  simp [index, support_X, weight]

theorem indexZero : index (0 : MvPolynomial Unit ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 0 := by
  simp [index]

theorem zeroDetGuard : ¬ ((2 : ℝ) ≤
    index (Matrix.of fun _ _ : Fin 2 ↦ (X () : MvPolynomial Unit ℝ)).det
      (fun _ ↦ 0) (fun _ ↦ 1)) := by
  simp [Matrix.det_fin_two, indexZero]


theorem actualNonzeroGuard :
    let D : Fin 2 → (Empty →₀ ℕ) := fun _ ↦ 0
    let R : MvPolynomial (Option Empty) ℝ := X none
    let α : Option Empty → ℝ := fun _ ↦ 0
    let r : Option Empty → ℕ := fun _ ↦ 1
    (∀ μ, (D μ).degree ≤ μ) ∧
    (∀ d : Empty →₀ ℕ, d.degree ≤ 2 - 1 → weight (r ∘ some) d ≤ 0) ∧
    ¬ (∑ ν ∈ Finset.range 2, max 0 (index R α r - ν / r none) - 2 * 0 ≤
      index (Matrix.of fun μ ν : Fin 2 ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r) := by
  dsimp only
  refine ⟨?_, ?_, ?_⟩
  · intro μ
    simp
  · intro d _
    have hd : d = 0 := Subsingleton.elim _ _
    simp [hd]
  · have hi : index (X none : MvPolynomial (Option Empty) ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 1 := by
      have hn : (default : Option Empty) = none := Subsingleton.elim _ _
      simp [index, support_X, weight, hn]
    have hz : (Matrix.of fun _ ν : Fin 2 ↦ hasseDeriv
        ((0 : Empty →₀ ℕ).mapDomain some + Finsupp.single none (ν : ℕ))
          (X none : MvPolynomial (Option Empty) ℝ)).det = 0 := by
      simp [Matrix.det_fin_two, mul_comm]
    rw [hz]
    have iz : index (0 : MvPolynomial (Option Empty) ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 0 := by
      simp [index]
    rw [iz]
    simp [hi, Finset.sum_range_succ]

#print axioms actualNonzeroGuard

#print axioms indexX
#print axioms indexZero
#print axioms zeroDetGuard
end Det207Guards
#print axioms Det207Replay.Θ_lt
"""
s=prefix+iso+'\n'+helper+weak+'\n'+body+'\n'+guards+'\n'+audit
p=D/'det207-fullmodule-executed.lean.txt';p.write_text(s)
assert max(map(len,s.splitlines()))<=100,[(i+1,len(l)) for i,l in enumerate(s.splitlines()) if len(l)>100]
z=subprocess.run(['python3','/private/tmp/roth-overview/check_audit_source.py',str(p)],text=True,capture_output=True)
(D/'gate-fullmodule.json').write_text(json.dumps(dict(request=z.args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr),indent=2)+'\n');assert z.returncode==0
(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('Prepared',len(s.splitlines()),'lines; gate:',z.stdout)
