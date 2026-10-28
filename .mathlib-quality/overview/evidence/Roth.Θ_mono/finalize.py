from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent
N='Roth.Θ_mono'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(n):return json.loads((D/n).read_text())
def wr(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
accepted=[]
requirements={
'original':(1,['THETAMONO191_FULL_TYPE:','THETAMONO191_AUDIT: requested=293; unique=293','THETAMONO191_AUDIT_PRESENT: present=293; values=293']),
'project':(344,["'Assessment191.bridge' depends on axioms", "'Assessment191.height_subset' depends on axioms", "'Assessment191.replacement' depends on axioms", "'Assessment191.all_bounds' depends on axioms", "'Assessment191.monotone_all' depends on axioms"]),
'isolated':(16,["'Assessment191Isolated.abstract_mono' does not depend on any axioms", "'Assessment191Isolated.nonneg_real_mono' depends on axioms", "'Assessment191Isolated.subset_alone_false' depends on axioms"]),
'callers':(375,["'Assessment191Callers.caller_theta_scaled_unique_le_aux' depends on axioms", "'Assessment191Callers.caller_theta_prefix_lt_aux' depends on axioms"])}
for label,(line,req)in requirements.items():
 prefix='theta-mono191-'+label+'-';s=prefix+'executed.lean.txt';r=prefix+'receipt.json'
 accepted.append(dict(label=label,source=s,source_sha256=sha(D/s),receipt=r,format='raw'if label=='isolated'else'disk',native_region_start_line=line,required_info=req,original_execution_request=rd(r)['request']))
wr('verification.json',dict(declaration=N,unresolved=[],accepted=accepted,rejected=[],standard_axioms=['propext','Classical.choice','Quot.sound'],audit=dict(source='theta-mono191-original-executed.lean.txt',receipt='theta-mono191-original-receipt.json',requested=293,unique=293,present=293,values=293),canonical_direct_consumers=['_private.Roth.Theta.0.Roth.theta_scaled_unique_le_aux','_private.Roth.Theta.0.Roth.theta_prefix_lt_aux'],canonical_direct_type_consumers=[],composition=dict(parent_reaim_checked=True,bridge_definitional=True,height_inclusion_definitional=False,strict_three_existing_call_term_verified=False,parent_project_lemma_counted_as_mathlib_block=False,actual_caller_replays=2,actual_call_occurrences=2,no_circular_use_of_target_in_new_proof=True,no_global_absence_claim=True,verified_hypothesis_deletion='hB',generic_empty_negative_counterexample=True)))
cmd=['rg','--files','--no-ignore','Roth','-g','*.lean'];z=subprocess.run(cmd,cwd='/Users/ramin/LEAN/Roth',text=True,capture_output=True)
wr('source-inventory.json',dict(request=cmd,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,root_module='Roth.lean'))
