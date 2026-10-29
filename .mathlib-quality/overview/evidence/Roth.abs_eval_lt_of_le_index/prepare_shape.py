from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index');R=Path('/Users/ramin/LEAN/Roth')
s=(D/'project2-executed.lean.txt').read_text()
shape='''
namespace Taylor281Shape
open Roth MvPolynomial
lemma coefficient_bound_pos {σ : Type*} [Fintype σ] [DecidableEq σ]
    (Q : MvPolynomial σ ℝ) (a : σ → ℝ) (r : σ → ℕ) {C : ℝ}
    (hC : ∀ d ∈ box r, |eval a (hasseDeriv d Q)| < C) : 0 < C :=
  (abs_nonneg _).trans_lt (hC 0 (mem_box.2 fun j ↦ Nat.zero_le _))
example : ¬ ((0 : ℝ) < (Finset.card (∅ : Finset ℕ) : ℝ) * 1 * 1) := by norm_num
example : ¬ ((1 : ℝ) < 1 * 1 * 1) := by norm_num
example : (∑ j : Fin 2, ((0 : ℝ) / (if j = 0 then (0 : ℝ) else 3))) = 0 := by simp
example : (∏ j : Fin 0, ((0 : ℝ) + 1)) = 1 := by simp
example : (box (fun _ : Fin 0 ↦ 0)).Nonempty :=
  ⟨0, mem_box.2 fun j ↦ Nat.zero_le _⟩
lemma zero_polynomial {σ : Type*} [Fintype σ] [DecidableEq σ]
    (r : σ → ℕ) (a x μ : σ → ℝ) {b c C : ℝ} (hb : 1 ≤ b) (hC : 0 < C)
    (hx : ∀ j, |x j - a j| ≤ b ^ (-μ j)) :
    |eval x (0 : MvPolynomial σ ℝ)| <
      (∏ j, ((r j : ℝ) + 1)) * C * b ^ (-c) := by
  apply Taylor281Project.cost_bound (fun j ↦ by simp) hb
    (fun d _ ↦ by simpa using hC) hx
  intro d _ h
  simp at h
lemma exact_original : @Roth.abs_eval_lt_of_le_index := by
  intro m _ Q r hd α c hidx h q hq κ hκ happ hqr C hC
  fail_if_success
    solve | simp only [abs_mul, abs_pow]
  exact Taylor281Project.original_recovery hd hidx hq hκ happ hqr (fun d _ ↦ hC d)
end Taylor281Shape
#print axioms Taylor281Shape.zero_polynomial
#print axioms Taylor281Shape.exact_original
'''
# Constant theorem has original theorem type; this is a composition failure probe plus new proof.
shape=shape.replace('lemma exact_original : @Roth.abs_eval_lt_of_le_index := by','lemma exact_original'+(D/'target-excerpt.lean.txt').read_text().split(':= by')[0].split('theorem abs_eval_lt_of_le_index',1)[1]+':= by').replace('  intro m _ Q r hd α c hidx h q hq κ hκ happ hqr C hC\n','')
p=D/'shape-executed.lean.txt';p.write_text(s+shape)
r={'id':'shape01','operation':'diagnostics','source':p.name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'receipt':'shape01-receipt.json','arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}};(D/'root-requests/shape01.json').write_text(json.dumps(r,indent=2)+'\n')
assert max(map(len,p.read_text().splitlines()))<=100
# Full Main inline reconstruction retaining every other original declaration/body.
main=(R/'Roth/Main.lean').read_text();main=main[main.index('namespace Roth'):]
main=main.replace('namespace Roth','namespace Taylor281Full\nopen Roth',1).replace('end Roth','end Taylor281Full')
original=(D/'target-excerpt.lean.txt').read_text().strip();assert original in main
main=main.replace(original,'')
caller=(D/'caller-excerpt.lean.txt').read_text().strip();assert caller in main
inline=(D/'callers2-executed.lean.txt').read_text().split('lemma caller_inline',1)[1].split('\nlemma caller_generic',1)[0]
inline='private lemma one_lt_roth_eval_bound_aux'+inline
main=main.replace(caller,inline.strip())
p=D/'fullmain-executed.lean.txt';p.write_text((D/'disk-prefix.lean.txt').read_text()+'\n'+main+'\n#print axioms Taylor281Full.roth_rat\n')
assert max(map(len,p.read_text().splitlines()))<=100
r.update(id='fullmain01',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='fullmain01-receipt.json');(D/'root-requests/fullmain01.json').write_text(json.dumps(r,indent=2)+'\n');print('Prepared shape/fullMain exact reconstruction, width PASS')
