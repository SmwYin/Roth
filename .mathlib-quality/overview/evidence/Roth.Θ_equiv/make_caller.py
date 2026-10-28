# coding: utf-8
from pathlib import Path
p=Path('/private/tmp/roth-overview/assess/Roth.\u0398_equiv')
s=Path('Roth/Theta.lean').read_text();a=s.index('private lemma theta_lt_succ_aux');b=s.index('\nprivate lemma theta_lt_of_large_delta_aux',a)
t=s[a:b].replace('private lemma theta_lt_succ_aux','lemma caller193')
t=t.replace('Θ_equiv e.symm','ThetaEquiv193.replay e.symm')
helpers=['theta_denominators_one_lt_aux','theta_phi_lt_aux']
prefix='namespace ThetaEquiv193Caller\nopen Roth MvPolynomial\n'
for i,h in enumerate(helpers):
 prefix+='elab "callerHelper193'+str(i)+'" : term =>\n  Lean.Meta.mkConstWithFreshMVarLevels (Lean.mkPrivateNameCore `Roth.Theta\n    `Roth.'+h+')\n'
 t=t.replace(h,'callerHelper193'+str(i))
(p/'caller-preparation.lean.txt').write_text(prefix+t+'\n#print axioms ThetaEquiv193Caller.caller193\nend ThetaEquiv193Caller\n')
