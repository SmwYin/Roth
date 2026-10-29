from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
s=(D/'isolated2-executed.lean.txt').read_text()
s=s[:s.index('#check_failure')]+s[s.index('open Filter'):s.index('theorem nonpositive')]+'''
example {κ κ' : ℝ} :
    (∀ M : ℝ, ∃ Q : ℕ, ∀ q : ℕ, Q < q →
      M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ') ↔ κ' < κ := by
  constructor
  · intro h
    by_contra! hκ
    obtain ⟨Q, hQ⟩ := h 1
    have hx : (0 : ℝ) < (Q + 2 : ℕ) := by positivity
    have hx1 : (1 : ℝ) ≤ (Q + 2 : ℕ) := by exact_mod_cast (by omega : 1 ≤ Q + 2)
    have hpow := Real.rpow_le_rpow_of_exponent_le hx1 hκ
    exact not_lt_of_ge (one_div_le_one_div_of_le (Real.rpow_pos_of_pos hx κ) hpow)
      (hQ (Q + 2) (by omega))
  · intro hκ M
    exact recovery hκ

example : ¬ ((1 : ℝ) / (0 : ℝ) ^ (2 : ℝ) < 1 / (0 : ℝ) ^ (1 : ℝ)) := by
  norm_num
example : ¬ ((0 : ℝ) / (2 : ℝ) ^ (0 : ℝ) < 0 / (2 : ℝ) ^ (0 : ℝ)) := by
  norm_num

example {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by
  fail_if_success solve | exact?
  fail_if_success solve | apply?
  exact recovery hκ
#print axioms eventual_filter
#print axioms recovery
end Decay270Generic
'''
s=s.replace('open Filter','#check_failure Roth.eventually_div_rpow_lt\nopen Filter',1)
assert max(map(len,s.splitlines()))<=100
(D/'supplement-executed.lean.txt').write_text(s)
r=dict(id='supplement01',operation='run_code',source='supplement-executed.lean.txt',source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='supplement-receipt.json',arguments={})
(D/'root-requests/supplement01.json').write_text(json.dumps(r,indent=2)+'\n')
print('Prepared uniform exponent necessity iff, q0/C0 guards, exact?/apply? closure probes')
