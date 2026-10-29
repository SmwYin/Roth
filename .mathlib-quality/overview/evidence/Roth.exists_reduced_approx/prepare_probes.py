exec(open('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx/prepare.py').read().split("code=prefix+")[0])
# All newly proved arithmetic facts below live in a mathlib-only namespace.
extra='import Mathlib.NumberTheory.DiophantineApproximation.Basic\n'
p= (D/'isolated-prefix.lean.txt').read_text()+extra+'\n#check_failure Roth.exists_reduced_approx\nnamespace Reduced274\n'
p+='\n'.join(next(x for x in meta if x['name']=='Roth.'+nm)['source'].replace('private theorem','theorem') for nm in ['approxSet','approxSet_den_le_finite','eventually_div_rpow_lt','approxSet_num_den_mem_aux'])+'\n'
p+=target['source'].replace('theorem exists_reduced_approx','theorem positive')+'\n'
p+='''
-- Generic image/fiber transfer is independent of rational arithmetic.
theorem infinite_image_of_finite_fibers {A B : Type*} {s : Set A} (f : A → B)
    (hs : s.Infinite) (hf : ∀ b ∈ f '' s, {a ∈ s | f a = b}.Finite) :
    (f '' s).Infinite := fun hi ↦ hs (Set.Finite.of_finite_fibers f hi hf)

-- The irrational Dirichlet theorem supplies reduced pairs directly.
theorem dirichlet_pairs {α : ℝ} (hα : Irrational α) : (approxSet α 2).Infinite := by
  refine ((Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational hα).image
    (f := fun x : ℚ ↦ (x.num, x.den))
    (fun _ _ _ _ hxy ↦ Rat.ext (congrArg Prod.fst hxy) (congrArg Prod.snd hxy))).mono ?_
  rintro _ ⟨x, hx, rfl⟩
  refine ⟨x.den_pos, ?_⟩
  simpa only [← Rat.cast_def, Real.rpow_ofNat] using hx

-- All real exponents are allowed; the positive branch retains the original hypothesis.
theorem unrestricted {α : ℝ} (hα : Irrational α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) :
    ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ) := by
  by_cases hκ : 0 < κ
  · exact positive hα hκ hinf Q₀
  · obtain ⟨hq, hm, hlt, hcop⟩ := positive hα (by norm_num : (0 : ℝ) < 2)
      (dirichlet_pairs hα) Q₀
    refine ⟨hq, ⟨hm.1, hm.2.trans_le ?_⟩, hlt, hcop⟩
    have hq1 : (1 : ℝ) ≤ hq.2 := by exact_mod_cast hm.1
    gcongr
    exact (le_of_not_gt hκ).trans (by norm_num : (0 : ℝ) ≤ 2)

-- Exact current signature recovered from the unrestricted theorem.
example {α : ℝ} (hα : Irrational α) {κ : ℝ} (_hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) :
    ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ) :=
  unrestricted hα hinf Q₀

-- Test the threshold edge case and the normalized rational form explicitly.
example {α κ : ℝ} (hα : Irrational α) (hi : (approxSet α κ).Infinite) :
    ∃ hq ∈ approxSet α κ, 0 < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ) :=
  unrestricted hα hi 0
#check @Set.Finite.of_finite_fibers
#check @Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational
#check @Rat.den_dvd
#check @Rat.num_div_den
#print axioms Reduced274.positive
#print axioms Reduced274.unrestricted
#print axioms Reduced274.infinite_image_of_finite_fibers
end Reduced274
'''
(D/'isolated-executed.lean.txt').write_text(p)
dump('root-requests/isolated01.json',{'id':'isolated01','operation':'run_code','source':'isolated-executed.lean.txt','source_sha256':sha(D/'isolated-executed.lean.txt'),'receipt':'isolated-receipt.json','arguments':{},'extra_import':'Mathlib.NumberTheory.DiophantineApproximation.Basic','authorization':'pending'})
# Full actual sole caller, inlining the exact target body through an exact local term.
caller=next(x for x in meta if x['name']=='Roth.exists_approximants')
cs=caller['source'].replace('theorem exists_approximants','theorem replay')
cs=cs.replace('  choose g hgmem hglt hgcop using fun Q₀ : ℕ ↦ exists_reduced_approx hα hκ hinf Q₀',
'''  have reduced : ∀ Q₀ : ℕ, ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧
      IsCoprime hq.1 (hq.2 : ℤ) := by
    intro Q₀
'''+''.join('  '+line+'\n' for line in target['body'].removeprefix('by\n').splitlines())+'''  choose g hgmem hglt hgcop using reduced''')
# private helper is copied into this fresh namespace, not reached via forbidden numerical name.
c=prefix+'\nnamespace Reduced274Caller\nopen Roth\n'+helper['source'].replace('private theorem','theorem')+'\n'+cs+'''
end Reduced274Caller
example : @Roth.exists_approximants = @Reduced274Caller.replay := Subsingleton.elim _ _
#print axioms Reduced274Caller.replay
'''
(D/'callers-executed.lean.txt').write_text(c)
dump('root-requests/callers01.json',{'id':'callers01','operation':'diagnostics','source':'callers-executed.lean.txt','source_sha256':sha(D/'callers-executed.lean.txt'),'receipt':'callers-receipt.json','original_audit':False,'arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}})
(D/'caller-excerpt.lean.txt').write_text(caller['source']+'\n')
for name in ['isolated-executed.lean.txt','callers-executed.lean.txt']:
 s=(D/name).read_text();assert max(map(len,s.splitlines()))<=100,(name,max(map(len,s.splitlines())))
print('Prepared isolated arithmetic/generic/unrestricted/recovery and full sole caller inline')
