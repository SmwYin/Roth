from pathlib import Path
import re
D=Path(__file__).resolve().parent
s=(D/'broader-executed.lean.txt').read_text();caller=Path('Roth/MainLemma.lean').read_text();caller=caller[caller.index('namespace Roth'):].replace('namespace Roth','namespace Theta228Caller\nopen Roth',1).replace('end Roth','end Theta228Caller');caller=re.sub(r'\bΘ_lt\b','Theta228Broad.replay',caller)
# Original caller statement remains unchanged; its≥3 input proves the new≥1 bound.
caller=caller.replace('(by simpa only [Fin.rev_zero, Nat.cast_ofNat] using (Nat.cast_le (α := ℝ)).2 hrlast)', '(by have h := (Nat.cast_le (α := ℝ)).2 hrlast\n        simpa only [Fin.rev_zero] using (show (1 : ℝ) ≤ r (Fin.rev 0) by linarith))')
s+='\n'+caller+'\nnamespace Theta228Caller\n#print axioms theta_lt_eta_of_sq_log_bound_aux\nend Theta228Caller\n'
assert all(len(l)<=100 for l in s.splitlines());(D/'callers-executed.lean.txt').write_text(s);Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print('prepared complete MainLemma caller module',len(s.splitlines()),'lines')
