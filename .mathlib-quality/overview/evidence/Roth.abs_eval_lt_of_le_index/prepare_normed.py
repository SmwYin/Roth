from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index')
s=(D/'generic-body.lean.txt').read_text().split('#print axioms')[0]
s=s.replace('Taylor281Generic','Taylor281Normed').replace('{σ : Type*} [Fintype σ]','{σ K : Type*} [Fintype σ] [NormedField K]')
s=s.replace('{μ x : σ → ℝ}','{μ : σ → ℝ} {x : σ → K}').replace('{a x μ : σ → ℝ} {A : (σ →₀ ℕ) → ℝ}','{a x : σ → K} {μ : σ → ℝ} {A : (σ →₀ ℕ) → K}')
s=s.replace('|x j|','‖x j‖').replace('|∏ j, x j ^ d j|','‖∏ j, x j ^ d j‖').replace('Finset.abs_prod','norm_prod').replace('|x j ^ d j|','‖x j ^ d j‖').replace('abs_pow','norm_pow')
s=s.replace('|A d|','‖A d‖').replace('|x j - a j|','‖x j - a j‖').replace('|eval x (','‖eval x (').replace('^ d j)|','^ d j)‖').replace('|A d * ∏ j, (x j - a j) ^ d j|','‖A d * ∏ j, (x j - a j) ^ d j‖')
s=s.replace('abs_nonneg','norm_nonneg').replace('Finset.abs_sum_le_sum_abs','norm_sum_le').replace('abs_mul','norm_mul')
p=D/'normed-executed.lean.txt';p.write_text((D/'isolated-prefix.lean.txt').read_text()+'\n'+s+'\n#print axioms Taylor281Normed.expansion_bound\n#check_failure Roth.abs_eval_lt_of_le_index\n')
r={'id':'normed01','operation':'run_code','source':p.name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'receipt':'normed01-receipt.json','arguments':{}};(D/'root-requests/normed01.json').write_text(json.dumps(r,indent=2)+'\n');print('Prepared normed field actual test; no extra imports')
