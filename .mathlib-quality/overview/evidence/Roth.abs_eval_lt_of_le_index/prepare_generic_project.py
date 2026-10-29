from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index')
g=(D/'generic-body.lean.txt').read_text().split('#print axioms')[0]
project='''
namespace Taylor281Project
open Roth MvPolynomial
lemma cost_bound {σ : Type*} [Fintype σ] [DecidableEq σ]
    {Q : MvPolynomial σ ℝ} {r : σ → ℕ} (hd : ∀ j, degreeOf j Q ≤ r j)
    {a x μ : σ → ℝ} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ box r, |eval a (hasseDeriv d Q)| < C)
    (hx : ∀ j, |x j - a j| ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ box r, eval a (hasseDeriv d Q) ≠ 0 → c ≤ ∑ j, μ j * d j) :
    |eval x Q| < (∏ j, ((r j : ℝ) + 1)) * C * b ^ (-c) := by
  conv_lhs => rw [eq_sum_box_hasseDeriv a r Q hd]
  convert Taylor281Generic.expansion_bound
    (show (box r).Nonempty from ⟨0, mem_box.2 fun j ↦ Nat.zero_le _⟩)
    hb hC hx hvanish using 1
  rw [card_box]
  push_cast
  rfl

lemma original_recovery {m : ℕ} [NeZero m] {Q : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ}
    (hd : ∀ j, degreeOf j Q ≤ r j) {α c : ℝ} (hidx : c ≤ index Q (fun _ ↦ α) r)
    {h : Fin m → ℤ} {q : Fin m → ℕ} (hq : ∀ j, 0 < q j) {κ : ℝ} (hκ : 0 ≤ κ)
    (happ : ∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ)
    (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) {C : ℝ}
    (hC : ∀ d ∈ box r, |eval (fun _ ↦ α) (hasseDeriv d Q)| < C) :
    |eval (fun j ↦ (h j : ℝ) / q j) Q| < (∏ j, ((r j : ℝ) + 1)) * C *
      (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
  have hqR : ∀ j, (0 : ℝ) < q j := fun j ↦ by exact_mod_cast hq j
  have hbase : (1 : ℝ) ≤ q 0 := by exact_mod_cast hq 0
  have hx : ∀ j, |(h j : ℝ) / q j - α| ≤ (q 0 : ℝ) ^ (-((r 0 : ℝ) * κ / r j)) := by
    intro j
    calc |(h j : ℝ) / q j - α| ≤ 1 / (q j : ℝ) ^ κ := by
          simpa only [abs_sub_comm] using happ j
      _ = (q j : ℝ) ^ (-κ) := by rw [Real.rpow_neg (hqR j).le, one_div]
      _ ≤ ((q 0 : ℝ) ^ ((r 0 : ℝ) / r j)) ^ (-κ) :=
          Real.rpow_le_rpow_of_nonpos (by positivity) (hqr j) (neg_nonpos.2 hκ)
      _ = (q 0 : ℝ) ^ (-((r 0 : ℝ) * κ / r j)) := by
          rw [← Real.rpow_mul (hqR 0).le]
          congr 1
          ring
  have hw : ∀ d ∈ box r, eval (fun _ ↦ α) (hasseDeriv d Q) ≠ 0 →
      (r 0 : ℝ) * c * κ ≤ ∑ j, ((r 0 : ℝ) * κ / r j) * d j := by
    intro d _ hd0
    have hh := mul_le_mul_of_nonneg_left (hidx.trans (index_le_weight hd0))
      (mul_nonneg (Nat.cast_nonneg (r 0)) hκ)
    convert hh using 1
    · ring
    · rw [weight, Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      ring
  convert cost_bound hd hbase hC hx hw using 1 <;> congr 2 <;> ring
end Taylor281Project
#print axioms Taylor281Project.cost_bound
#print axioms Taylor281Project.original_recovery
'''
p=D/'project-executed.lean.txt';p.write_text((D/'disk-prefix.lean.txt').read_text()+'\n'+g+project)
r={'id':'project01','operation':'diagnostics','source':p.name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'receipt':'project01-receipt.json','arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}}
(D/'root-requests/project01.json').write_text(json.dumps(r,indent=2)+'\n')
print('Prepared complete generic project bound/localized box hC/exact recovery')
