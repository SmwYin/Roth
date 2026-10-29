from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.roth_of_isIntegral')
meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
def norm(s):return re.sub(r'\s+',' ',s).strip()
target=src('Roth.roth_of_isIntegral');original=(D/'original-executed.lean.txt').read_text();callers=(D/'callers-executed.lean.txt').read_text()
assert norm(target.replace('theorem roth_of_isIntegral','theorem replay',1))in norm(original)
for n in ['exists_roth_parameters_aux','exists_roth_approximants_aux','one_lt_roth_eval_bound_aux','roth_product_bound_aux','roth_log_bound_aux']:
 s=src('Roth.'+n);assert norm(s)in norm(original)and norm(s)in norm(callers)
body=target.replace('theorem roth_of_isIntegral','have integral_inline',1)
inline='\n'.join('  '+x for x in body.splitlines())
caller=src('Roth.roth').replace('theorem roth','theorem roth_inline',1).replace(' := by\n',' := by\n'+inline+'\n',1).replace('(roth_of_isIntegral hα\' hint\' hinf\')','(integral_inline hα\' hint\' hinf\')')
assert norm(caller)in norm(callers)
rat=src('Roth.roth_rat').replace('theorem roth_rat','theorem roth_rat_replay',1).replace('refine roth hα','refine roth_inline hα',1);assert norm(rat)in norm(callers)
ev=(R/'Roth/LeanEval.lean').read_text();ev=ev[ev.index('namespace LeanEval.NumberTheory.ThueSiegelRothProblem'):].replace('namespace LeanEval.NumberTheory.ThueSiegelRothProblem','namespace Integral287LeanEval',1).replace('end LeanEval.NumberTheory.ThueSiegelRothProblem','end Integral287LeanEval').replace('(Roth.roth _h_irr','(Integral287Callers.roth_inline _h_irr')
assert norm(ev)in norm(callers)
print('PASS root independently reconstructed exact target+five helpers, full actual caller with literal target inlining, full rational caller and entire LeanEval module preserving statements. Native/report acceptance separate.')
