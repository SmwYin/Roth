from pathlib import Path
import json
D=Path(__file__).resolve().parent;s=(D/'original-executed.lean.txt').read_text();row=json.load(open(D/'target-metadata.json'));c=Path('Roth/MainLemma.lean').read_text();c=c[c.index('namespace Roth'):].replace('namespace Roth','namespace Theta228\nopen Roth',1).replace('end Roth','end Theta228')
helper=row['signature'].replace('theorem Θ_lt','have endpoint',1)+' := '+row['body'];helper='\n'.join('  '+l for l in helper.splitlines())
c=c.replace('  simpa [eta] using Θ_lt n hδpos',helper+'\n  simpa [eta] using endpoint n hδpos')
s+='\n'+c+'\nnamespace Theta228\n#print axioms theta_lt_eta_of_sq_log_bound_aux\nend Theta228\n';assert all(len(l)<=100 for l in s.splitlines());(D/'inline-executed.lean.txt').write_text(s);Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print('prepared actual endpoint-body inline and complete MainLemma',len(s.splitlines()))
