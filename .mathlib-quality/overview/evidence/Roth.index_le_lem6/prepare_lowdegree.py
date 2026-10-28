from pathlib import Path
D=Path(__file__).resolve().parent;s=(D/'noq-executed.lean.txt').read_text();s=s[:s.index('\n#check @LemSix213NoQ.replay')];s=s.replace('LemSix213NoQ','LemSix213LowDegree')
f=Path('/private/tmp/roth-overview/assess/Roth.min_le_sum_max/minsum206-finite-executed.lean.txt').read_text();f=f[f.index('namespace MinSum206Finite'):f.index('theorem originalViaStronger')]+ '\nend MinSum206Finite\n';f=f.replace('MinSum206Finite','LemSix213Finite')
s=s[:s.index('namespace LemSix213LowDegree')]+f+'\n'+s[s.index('namespace LemSix213LowDegree'):]
start=s.index('private lemma index_numeric_bound_aux');end=s.index('omit [DecidableEq τ]',start)
n=s[start:end].replace('(hrp : 3 ≤ rp)','(hrp : 1 ≤ rp)').replace('(rp * θ ^ 2 / 3)','(rp * θ ^ 2 / 2)').replace('(0 : ℝ) < 3','(0 : ℝ) < 1').replace('3 * l ≤ 4 * rp','2 * l ≤ 4 * rp').replace('linear_combination 3 * hk','linear_combination 2 * hk')
s=s[:start]+n+s[end:]
start=s.index('theorem replay');end=s.index('omit [DecidableEq τ]',start)
n=s[start:end].replace('(hrp : 3 ≤ (r none : ℝ))','(hrp : 1 ≤ (r none : ℝ))').replace('(0 : ℝ) < 3','(0 : ℝ) < 1').replace('min_le_sum_max (θ :=','LemSix213Finite.generic (θ :=')
s=s[:start]+n+s[end:]
s=s.replace('replay hδ0 hδ1 hrp hratio hr₁ hR hh','replay hδ0 hδ1 (by linarith only [hrp]) hratio hr₁ hR hh')
s+='\n#check @LemSix213LowDegree.replay\n#print axioms LemSix213LowDegree.replay\n#print axioms LemSix213LowDegree.Θ_option_le\n#print axioms LemSix213LowDegree.Θ_lt\n#print axioms LemSix213Finite.generic\n'
s=s.replace('      (∀','      (∀')
# Wrap only an extended helper-call line.
s=s.replace('  exact (LemSix213Finite.generic (θ := index (map (Int.castRingHom ℝ) R) α r) (rp := r none) l).trans', '  exact (LemSix213Finite.generic\n    (θ := index (map (Int.castRingHom ℝ) R) α r) (rp := (r none : ℝ)) l).trans')
long=[(i,len(l)) for i,l in enumerate(s.splitlines(),1) if len(l)>100];assert not long,long
(D/'lowdegree-executed.lean.txt').write_text(s);Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print('prepared',len(s.splitlines()))
