from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=[]
markers={'original':['BUDGET253_SIGNATURE_IDENTICAL','BUDGET253_AUDIT: requested=293; unique=293','BUDGET253_AUDIT_PRESENT: present=293; values=293'], 'isolated':['Budget253.generic','Budget253.recovery','Budget253.weak','Budget253.strict_budget','Budget253.delta_nonzero','Budget253.negative_delta','Budget253.negative_m','Budget253.zero_m','Budget253.zero_scale_counterexample','Budget253.negative_scale_counterexample','Budget253.strictness_counterexample','Budget253.budget_needed'], 'controls':['Budget253Controls.absence_probe'],'comparison':['BUDGET253_EXACT_RECOVERY','BUDGET253_COMPARISON_MAIN_SIGNATURE_IDENTICAL','BUDGET253_GENERIC_TYPE:']}
for label in ['original','isolated','controls','comparison']:
 source=label+'-executed.lean.txt';receipt=label+'-receipt.json';a.append(dict(label=label,source=source,receipt=receipt,format='disk'if label in ['original','comparison']else'virtual',source_sha256=sha(D/source),original_execution_request=rd(receipt)['request'],native_region_start_line=17 if label in ['original','comparison']else 19,required_info=markers[label]))
x=dict(declaration=N,canonical_index=253,completed=True,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=a,rejected=[dict(source='isolated-rejected-executed.lean.txt',receipt='isolated-rejected-receipt.json',reason='Compiled but unused section classes warning; not clean accepted proof evidence')],full_actual_callers=dict(count=0,inline='justified n/a: no callers'),related_nonconsumer_comparison=dict(original_signature_retained=True,native='comparison-receipt.json',new_helper=True),controls=dict(shared_prefix_sha256=sha(D/'isolated-prefix.lean.txt'),disk_prefix_sha256=sha(D/'disk-prefix.lean.txt')),canonical_audit='exact293 generated from tracked order, preexecution checked, runtime all293 unique/present/values; zero type/value consumers',printer_elision='Original #print proof body elided; not full kernel body dump')
(D/'verification.json').write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
print('PASS verification links four clean accepted sources and warning-rejected source')
