from pathlib import Path
import re,json
D=Path(__file__).resolve().parent;R=Path.cwd();prefix=(D/'disk-prefix.lean.txt').read_text()
raw='''(fun (α κ : ℝ) ↦
      ({hq : ℤ × ℕ | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ} : Set (ℤ × ℕ)))
      '''
s=(R/'Roth/Main.lean').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Approx267Inline\nopen Roth',1).replace('end Roth','end Approx267Inline')
body=re.sub(r'/\-.*?\-/','',body,flags=re.S)
body=re.sub(r'def approxSet \(α κ : ℝ\) : Set \(ℤ × ℕ\) :=\n  .*\n','',body)
body=re.sub(r'\bapproxSet\b',raw,body)
t=(R/'Roth/LeanEval.lean').read_text();other=t[t.index('namespace LeanEval.NumberTheory.ThueSiegelRothProblem'):].replace('namespace LeanEval.NumberTheory.ThueSiegelRothProblem','namespace Approx267InlineLeanEval',1).replace('end LeanEval.NumberTheory.ThueSiegelRothProblem','end Approx267InlineLeanEval');other=re.sub(r'/\-.*?\-/','',other,flags=re.S);other=other.replace('Roth.approxSet ',raw+' ')
public=['approxSet_den_le_finite','reduction','exists_reduced_approx','exists_approximants','roth_of_isIntegral','roth','roth_rat']
checks='\n'.join('example : @Roth.'+n+' = @Approx267Inline.'+n+' := Subsingleton.elim _ _\n#print axioms Approx267Inline.'+n for n in public)
checks+='\nexample : @LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff =\n    @Approx267InlineLeanEval.isDiophantine_iff := Subsingleton.elim _ _\n'
checks+='example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =\n    @Approx267InlineLeanEval.thueSiegelRoth := Subsingleton.elim _ _\n'
checks+='\n#print axioms Approx267InlineLeanEval.isDiophantine_iff\n#print axioms Approx267InlineLeanEval.thueSiegelRoth\n'
privates=[('Roth.Main','Roth.approxSet_num_den_mem_aux','Approx267Inline.approxSet_num_den_mem_aux'),('Roth.Main','Roth.exists_roth_approximants_aux','Approx267Inline.exists_roth_approximants_aux'),('Roth.LeanEval','LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux','Approx267InlineLeanEval.exists_pos_div_rpow_lt_aux')]
for i,(mod,n,copy)in enumerate(privates):
 checks+='\nelab "originalPrivate267_'+str(i)+'" : term => do\n  Lean.Meta.mkConstWithFreshMVarLevels (Lean.mkPrivateNameCore `'+mod+'\n    `'+n+')\nexample : originalPrivate267_'+str(i)+' = @'+copy+' := Subsingleton.elim _ _\n#print axioms '+copy+'\n'
checks=checks.replace(' := Subsingleton.elim _ _', ' :=\n    Subsingleton.elim _ _')
full=prefix+body+'\n'+other+'\n'+checks
# The long inline lambda is split without altering token contents.
long=[(i+1,len(l),l)for i,l in enumerate(full.splitlines())if len(l)>100]
if long:print(long);raise SystemExit(1)
(D/'inline-executed.lean.txt').write_text(full);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(full)
print('Prepared full Main/LeanEval direct-caller inlining;12 signature equalities',len(full.splitlines()))
