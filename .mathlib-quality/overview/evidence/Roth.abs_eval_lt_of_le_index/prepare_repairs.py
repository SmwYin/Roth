from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index')
def req(id,p,mode):
 s=p.read_text();assert max(map(len,s.splitlines()))<=100
 args={}if mode=='run_code'else{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}
 (D/f'root-requests/{id}.json').write_text(json.dumps({'id':id,'operation':mode,'source':p.name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'receipt':id+'-receipt.json','arguments':args},indent=2)+'\n')
s=(D/'shape-executed.lean.txt').read_text().replace('(hC 0 (mem_box.2 fun j ↦ Nat.zero_le _))','(hC 0 (mem_box.2 fun _ ↦ Nat.zero_le _))').replace('(∏ j : Fin 0,','(∏ _j : Fin 0,').replace('⟨0, mem_box.2 fun j ↦ Nat.zero_le _⟩\nlemma zero_polynomial','⟨0, mem_box.2 fun _ ↦ Nat.zero_le _⟩\nlemma zero_polynomial').replace('lemma zero_polynomial {σ : Type*} [Fintype σ] [DecidableEq σ]','lemma zero_polynomial {σ : Type*} [Fintype σ]').replace('  apply Taylor281Project.cost_bound','  classical\n  apply Taylor281Project.cost_bound')
p=D/'shape2-executed.lean.txt';p.write_text(s);req('shape02',p,'diagnostics')
s=(D/'fullmain-executed.lean.txt').read_text();a=s.index('/-- If `Q` has index');b=s.index('-- Choose the polynomial',a);s=s[:a]+s[b:];p=D/'fullmain2-executed.lean.txt';p.write_text(s);req('fullmain02',p,'diagnostics')
s=(D/'normed2-executed.lean.txt').read_text().replace('Taylor281Normed','Taylor281Ring').replace('[NormedField K]','[NormedCommRing K] [NormOneClass K]')
s=s.replace('  rw [norm_prod]','  apply (Finset.norm_prod_le _ _).trans')
s=s.replace('        rw [norm_pow, Real.rpow_mul hb0.le, Real.rpow_natCast]','        apply (norm_pow_le _ _).trans\n        rw [Real.rpow_mul hb0.le, Real.rpow_natCast]')
s=s.replace('    rw [norm_mul]','    apply (norm_mul_le _ _).trans_lt')
s=s.replace('[NormedCommRing K] [NormOneClass K] {b : ℝ}', '[NormedCommRing K] [NormOneClass K]\n    {b : ℝ}')
p=D/'normedring-executed.lean.txt';p.write_text(s);req('normedring01',p,'run_code')
print('Prepared repairs+normedcommring actual width PASS')
