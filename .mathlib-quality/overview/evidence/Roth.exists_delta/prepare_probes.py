from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth')
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def request(i,n,op='diagnostics'):
 put('root-requests/'+i+'.json',dict(id=i,operation=op,source=n,source_sha256=hashlib.sha256((D/n).read_bytes()).hexdigest(),receipt=i+'-receipt.json',arguments={} if op=='run_code' else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)))
pre=(D/'disk-prefix.lean.txt').read_text();iso=(D/'isolated-prefix.lean.txt').read_text()
generic='''
open scoped Topology
namespace Delta276Generic
-- Newly proved schema; its quantitative envelopes are parameters, not discarded.
theorem simultaneous {f p q : ℝ → ℝ} {U B K : ℝ} (hU : 0 < U)
    (hf : ContinuousAt f 0) (hp : ContinuousAt p 0) (hq : ContinuousAt q 0)
    (hq0 : q 0 ≠ 0) (hf0 : f 0 < B) (hquot : p 0 / q 0 < K) :
    ∃ δ : ℝ, 0 < δ ∧ δ < U ∧ f δ < B ∧ p δ / q δ < K := by
  exact ((eventually_lt_nhds hU).and
    ((hf.eventually_lt continuousAt_const hf0).and
      ((hp.div hq hq0).eventually_lt continuousAt_const hquot))).exists_gt

-- Point selection alone is already an existing API, not the full quantitative bridge.
example {P : ℝ → Prop} (hP : ∀ᶠ x in 𝓝 (0 : ℝ), P x) : ∃ x, 0 < x ∧ P x :=
  hP.exists_gt
#check @ContinuousAt.eventually_lt
#check @Filter.Eventually.and
#check @Filter.Eventually.exists_gt
#check @ContinuousAt.div
#print axioms simultaneous
end Delta276Generic
'''
(D/'generic-executed.lean.txt').write_text(iso+'\n#check_failure Roth.exists_delta\n'+generic);request('generic01','generic-executed.lean.txt','run_code')
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());target=next(x for x in meta if x['name']=='Roth.exists_delta')['source'];body=target.split(':= by\n',1)[1]
recovery='''
namespace Delta276Recovery
open Roth
theorem recovered {n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
    (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ := by
  have hm0 : (0 : ℝ) < m := by exact_mod_cast (Nat.zero_le _).trans_lt hm
  have hm' : (16 * n ^ 2 : ℝ) < m := by exact_mod_cast hm
  have h4n : 4 * (n : ℝ) < √(m : ℝ) := Real.lt_sqrt_of_sq_lt (by nlinarith only [hm'])
  have hgap : 2 * (n : ℝ) * √(m : ℝ) < m / 2 := by
    nlinarith only [Real.sq_sqrt hm0.le,
      mul_lt_mul_of_pos_right h4n (Real.sqrt_pos.mpr hm0)]
  apply Delta276Generic.simultaneous (f := fun δ ↦
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ))
    (p := fun δ ↦ (m : ℝ) * (1 + 4 * δ))
    (q := fun δ ↦ gam δ n m - eta δ m) (by positivity)
  · exact (Real.continuousAt_rpow_const 0 _ (.inr (by positivity))).const_mul _ |>.add
      (by fun_prop)
  · fun_prop
  · unfold gam lam eta
    exact ((continuousAt_const.sub (by fun_prop)).div_const 2).sub
      ((Real.continuousAt_rpow_const 0 _ (.inr (by positivity))).const_mul _)
  · have : 0 < gam 0 n m - eta 0 m := by
      simpa [gam, lam, eta, Real.zero_rpow (by positivity : (1 / 2 : ℝ) ^ m ≠ 0)]
        using (show 0 < ((m : ℝ) - 4 * n * √(m : ℝ)) / 2 by linarith)
    exact this.ne'
  · simpa [eta, Real.zero_rpow (by positivity : (1 / 2 : ℝ) ^ m ≠ 0)] using hgap
  · simpa [gam, lam, eta, Real.zero_rpow (by positivity : (1 / 2 : ℝ) ^ m ≠ 0),
      div_div_eq_mul_div, mul_comm] using h47'
example : @recovered = @Roth.exists_delta := Subsingleton.elim _ _
-- Strict cap forces m≠0; deleting hm admits m=0 and no positive δ<1/0.
theorem zero_dimension_impossible : ¬ ∃ δ : ℝ, 0 < δ ∧ δ < 1 / (0 : ℝ) := by
  simp
example {κ : ℝ} (hκ : 2 < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 ∧
    eta δ 1 + 2 * (1 + 3 * δ) * (0 : ℕ) * √(1 : ℝ) < 1 / 2 ∧
    (1 : ℝ) * (1 + 4 * δ) / (gam δ 0 1 - eta δ 1) < κ := by
  simpa using (recovered (n := 0) (m := 1) (by norm_num) (by simpa using hκ))
#print axioms recovered
#print axioms zero_dimension_impossible
end Delta276Recovery
'''
(D/'recovery-executed.lean.txt').write_text(pre+generic+recovery);request('recovery01','recovery-executed.lean.txt')
caller=next(x for x in meta if x['name']=='Roth.exists_roth_parameters_aux')['source'];(D/'caller-excerpt.lean.txt').write_text(caller+'\n')
inline='  have delta_choice '+target.split('theorem exists_delta ',1)[1].split(':= by\n',1)[0]+':= by\n'+''.join('  '+l+'\n' for l in body.splitlines())
c=caller.replace('private lemma exists_roth_parameters_aux','theorem replay').replace(':= by\n',':= by\n'+inline,1).replace(':= exists_delta hm h47\'',':= delta_choice hm h47\'')
(D/'inline-executed.lean.txt').write_text(pre+'\nnamespace Delta276Inline\nopen Roth\n'+c+'\n#print axioms replay\nend Delta276Inline\n');request('inline01','inline-executed.lean.txt')
# Entire actual Main continuation in fresh namespace: helper closure + downstream full bodies.
s=(R/'Roth/Main.lean').read_text();continuation=s[s.index('-- Choose the polynomial, coefficient bound'):s.rindex('end Roth')]
continuation=continuation.replace('private lemma','lemma').replace(':= exists_delta hm h47\'',':= Delta276Recovery.recovered hm h47\'')
(D/'callers-executed.lean.txt').write_text(pre+generic+recovery+'\nnamespace Delta276Callers\nopen Roth\n'+continuation+'\n#print axioms roth_of_isIntegral\n#print axioms roth\n#print axioms roth_rat\nend Delta276Callers\n');request('callers01','callers-executed.lean.txt')
# Actual independent composition test, prior to any generic schema.
c=target.replace('theorem exists_delta','theorem checked').replace(':= by\n',':= by\n  fail_if_success simp\n  fail_if_success aesop\n',1)
(D/'composition-executed.lean.txt').write_text(pre+'\nnamespace Delta276Composition\nopen Roth\n'+c+'\n#print axioms checked\nend Delta276Composition\n');request('composition01','composition-executed.lean.txt')
for n,args in [('source-search',['rg','--no-ignore','-n',r'\bexists_delta\b','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','-w','exists_delta','--','Roth','Roth.lean']),('source-inventory',['rg','--files','--no-ignore','Roth']),('inline-search',['rg','--no-ignore','-n','eventually_nhds_iff|exists_between|exists_delta','Roth','Roth.lean']),('literature-local',['rg','-n',r'roth:eq4[789]|lem:m-delta|Decreasing|delta.*small',' .mathlib-quality/references/clean.tex'.strip()])]:
 z=subprocess.run(args,capture_output=True,text=True);put(n+'.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
for form,pat in [('current','exists_delta|eta.*gam|gam.*eta'),('standard','ContinuousAt.eventually_lt|eventually_lt_nhds'),('abstract','theorem.*exists_gt|theorem.*Eventually.and|theorem.*Eventually.exists')]:
 args=['rg','-n',pat,'.lake/packages/mathlib/Mathlib'];z=subprocess.run(args,capture_output=True,text=True);put('formal-'+form+'-rg.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
print('Prepared generic01/recovery01/inline01/callers01/composition01; no production writes')
