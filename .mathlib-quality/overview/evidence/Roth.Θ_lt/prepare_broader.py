from pathlib import Path
import re
D=Path(__file__).resolve().parent
s=Path('/private/tmp/roth-overview/assess/Roth.Θ_option_le/lowdegree-executed.lean.txt').read_text();s=s[:s.index('\n#check @ThetaOption214Low.replay')];s=s.replace('ThetaOption214Low','Theta228Broad');s=re.sub(r'\breplay\b','Θ_option_le',s)
a=s.index('section Lemma7');pre=s[:a];body=s[a:]
for old,new in [('(hrlast : 3 ≤','(hrlast : 1 ≤'),('→ ℕ}, 3 ≤','→ ℕ}, 1 ≤'),('have h : (3 : ℝ) ≤','have h : (1 : ℝ) ≤'),('(0 : ℝ) < 3','(0 : ℝ) < 1'),(': (3 : ℝ) ≤ r 0',': (1 : ℝ) ≤ r 0')]:body=body.replace(old,new)
body=re.sub(r'\bΘ_lt\b','replay',body)
s=pre+body+'\n#check @Theta228Broad.replay\n#print axioms Theta228Broad.replay\n'
assert all(len(l)<=100 for l in s.splitlines());(D/'broader-executed.lean.txt').write_text(s);Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('Prepared broader',len(s.splitlines()),'lines; exact first9 imports retained; targeted degree threshold only')
