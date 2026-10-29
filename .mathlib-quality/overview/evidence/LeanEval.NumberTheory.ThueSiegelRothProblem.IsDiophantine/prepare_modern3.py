from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent
s=(D/'modern2-executed.lean.txt').read_text()
s=s.replace('''  simp only [uniform_iff, irrational_mul_ratCast_iff, hr, true_and,
    LiouvilleWith.mul_rat_iff hr]''','''  rw [uniform_iff, uniform_iff]
  constructor
  · rintro ⟨hx, h⟩
    exact ⟨Irrational.of_mul_ratCast r hx,
      fun hp ↦ h ((LiouvilleWith.mul_rat_iff hr).mpr hp)⟩
  · rintro ⟨hx, h⟩
    exact ⟨hx.mul_ratCast hr, fun hp ↦ h ((LiouvilleWith.mul_rat_iff hr).mp hp)⟩''')
s=s.replace('end Diophantine290Modern','''lemma liouville_not_uniform {x : ℝ} (hx : Liouville x) : ¬ UniformBound 2 x := by
  intro h
  have hh := (uniform_iff.mp h).2 (hx.liouvilleWith 3)
  norm_num at hh
#print axioms Diophantine290Modern.liouville_not_uniform
end Diophantine290Modern''')
assert max(map(len,s.splitlines()))<=100
(D/'modern3-executed.lean.txt').write_text(s)
(D/'root-requests/modern03.json').write_text(json.dumps(dict(id='modern03',operation='run_code',source='modern3-executed.lean.txt',source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='modern03-receipt.json',arguments={}),indent=2)+'\n')
print('Prepared modern03 structured rational scaling and Liouville false guard')
