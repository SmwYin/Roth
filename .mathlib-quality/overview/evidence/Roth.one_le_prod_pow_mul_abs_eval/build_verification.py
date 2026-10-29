from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.one_le_prod_pow_mul_abs_eval'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def rd(n):return json.loads((D/n).read_text())
def source_entry(label,src,rec,format,infos,axioms=True):
 q=rd(rec);return dict(label=label,source=src,receipt=rec,format=format,source_sha256=hashlib.sha256((D/src).read_bytes()).hexdigest(),elapsed_ms=q['elapsed_ms'],original_execution_request=q['request'],native_region_start_line=15 if format=='disk'else 19,required_info=infos,axiom_print_required=axioms)
accepted=[source_entry(*x)for x in [
('original','original-executed.lean.txt','original-receipt.json','disk',['INT279_FULL_TYPE:','INT279_AUDIT: requested=293; unique=293','INT279_AUDIT_PRESENT: present=293; values=293',"'Integer279Original.replay' depends on axioms:"]),
('generic','generic-executed.lean.txt','generic01-receipt.json','run_code',["'Integer279.generic' depends on axioms:"]),
('signed','signed-executed.lean.txt','signed01-receipt.json','run_code',["'Integer279.signed' depends on axioms:"]),
('recovery','recovery-executed.lean.txt','recovery01-receipt.json','run_code',["'Integer279.recovery' depends on axioms:"]),
('edges','edges-executed.lean.txt','edges01-receipt.json','run_code',[],False),
('clearing','clearing3-executed.lean.txt','clearing03-receipt.json','run_code',["'Integer279.clearing' depends on axioms:","'Integer279.separatedNorm' depends on axioms:"]),
('composition','composition3-executed.lean.txt','composition03-receipt.json','run_code',["'Integer279.compositionProbe' depends on axioms:","one_le_pow_mul_abs_eval_div."]),
('callers','callers3-executed.lean.txt','callers03-receipt.json','disk',["'Integer279Full.roth_rat' depends on axioms:"]),
('shape','shape2-executed.lean.txt','shape02-receipt.json','run_code',["'Integer279.eval₂Form' depends on axioms:"]),
('semiring-clearing','generic-clearing-executed.lean.txt','generic-clearing01-receipt.json','run_code',["'Integer279.clearing_semiring' depends on axioms:"])
]]
other=[]
for src,rec,reason in [('clearing2-executed.lean.txt','clearing02-receipt.json','Implicit field metavariable in helper application; recovered sorryAx, rejected.'),('composition2-executed.lean.txt','composition02-receipt.json','Unreachable nested positivity tactic warning, rejected.'),('callers2-executed.lean.txt','callers02-receipt.json','Orphan target docstring created empty-line style warning, rejected.'),('shape-executed.lean.txt','shape01-receipt.json','eval₂ hne supplied before eval_map normalization; recovered sorryAx, rejected.')]:
 q=rd(rec);other.append(dict(source=src,receipt=rec,source_sha256=hashlib.sha256((D/src).read_bytes()).hexdigest(),reason=reason,elapsed_ms=q['elapsed_ms']))
dump('verification.json',dict(declaration=N,canonical_index=279,completed=False,unresolved=[],accepted=accepted,other_executions=other,standard_axioms=['propext','Classical.choice','Quot.sound'],attempt_accounting=dict(native_executions=len(accepted)+len(other),accepted=len(accepted),rejected=len(other),preparation_only=rd('preparation-only.json')),root_exclusive_executor=True,full_literal_build='not due279; accepted unchanged baseline2467jobs and previous228 boundary; next due289',native_ownership='root throughout, worker never invoked native/projectLSP or wrote persistent scratch',release='worker has no further native requests; ownership remains root'))
fresh=rd('inputs.json')
for x in fresh:assert hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256']
dump('fresh-final-inputs.json',dict(inputs=fresh,unchanged=True))
s=(D/'report.md').read_text();s=s.replace('This is new generic proof evidence, not a replacement already in mathlib.','This is new generic proof evidence, not a replacement already in mathlib. recovery01 has the exact written original signature in a mathlib-only module; it does not import or assert native original-versus-recovery proof equality.')
key='## Phase4c — Modern idiom nine rows'
extra='''The algebraic layer generalizes further than characteristic-zero fields: arbitrary commutative semirings R and S, a ring homomorphism f:R→S, and supplied inverses biⱼ·f(bⱼ)=1 suffice. This is the direct multivariate analogue of existing DenomsClearable's semiring/inverse interface; eval₂ avoids the support-map injectivity premise entirely. No CharZero, injective map, no-zero-divisors, field or order assumptions are needed for this equality. The complete new proof and clean native verification are '''+f'[{"generic-clearing-executed.lean.txt"}](../evidence/{N}/generic-clearing-executed.lean.txt) and [generic-clearing01-receipt.json](../evidence/{N}/generic-clearing01-receipt.json).'+''' This is an independently proved missing helper, not an existing mathlib replacement. Its concrete effect is to reuse coordinatewise denominator clearing for maps into localizations and quotient semirings; the inverse equation is the required interface. Numeric separation remains an additional arithmetic property, supplied by integer coefficients and ordered-field absolute value in the primary estimate. The characteristic-zero field clearing03 is therefore a verified intermediate specialization, not claimed as the most general algebraic API.

```lean
'''+(D/'generic-clearing-body.lean.txt').read_text().split(':= by')[0].strip()+'''
```

'''
s=s.replace(key,extra+key)
s=s.replace('Put algebraic clearing equality first, then ordered-field signed estimate and positive-natural corollary.','Put the verified commutative-semiring/ring-hom/inverse algebraic clearing equality first, then ordered-field signed estimate and positive-natural corollary.')
s='\n'.join(l.rstrip()for l in s.splitlines())+'\n';(D/'report.md').write_text(s)
o=rd('overview-entry.json');o['generalization']['algebraic_helper_type']=(D/'generic-clearing-body.lean.txt').read_text().split(':= by')[0].strip();o['generalization']['algebraic_generality']='Verified arbitrary commutative semirings and ring hom with coordinate denominator inverses, no CharZero/injective map/field/order. Numeric bound requires integer separation separately.';dump('overview-entry.json',o)
p=rd('phase-checks.json');p['modern9'][2][2]='Verified commutative-semiring/ringhom clearing with denominator inverse equations; localization explains interface but does not supply separation.';p['proofstrategy5'][4][2]='Verified new clearing_semiring helper: arbitrary CommSemiring source/target and denominator inverse equations, eval₂ avoids injectivity. Separate integer lower bound.';dump('phase-checks.json',p)
print('Native10 accepted,4 rejected exact archived; semiring helper integrated, inputs17 fresh')
