# coding: utf-8
from pathlib import Path
import shutil,json,hashlib
P=Path('/private/tmp/roth-overview/assess/Roth.\u0398_equiv');T=Path('/private/tmp/roth-overview')
def dump(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
accepted=[]
for k,region,infos in [('original',15,['THETAEQUIV193_FULL_TYPE:','THETAEQUIV193_AUDIT: requested=293; unique=293','THETAEQUIV193_AUDIT_PRESENT: present=293; values=293']),('project',344,["'ThetaEquiv193.familyEq' depends on axioms:","'ThetaEquiv193.replay' depends on axioms:","'ThetaEquiv193.fullBridge' depends on axioms:"]),('callers',383,["'ThetaEquiv193Caller.caller193' depends on axioms:"]),('isolated',16,["'ThetaEquiv193Isolated.law' does not depend on any axioms","'ThetaEquiv193Isolated.reindex' depends on axioms:",'@Equiv.iSup_congr :'])]:
 sn='theta-equiv193-'+k+'-executed.lean.txt';rn='theta-equiv193-'+k+'-receipt.json'
 for n in [sn,rn]:shutil.copyfile(T/n,P/n)
 r=json.loads((P/rn).read_text());accepted.append(dict(label=k,source=sn,receipt=rn,source_sha256=hashlib.sha256((P/sn).read_bytes()).hexdigest(),format='raw'if k=='isolated'else'disk',original_execution_request=r['request'],native_region_start_line=region,required_info=infos))
for n in ['theta-equiv193-audit-executed.lean.txt','theta-equiv193-project-rejected-executed.lean.txt','theta-equiv193-project-rejected-receipt.json']:shutil.copyfile(T/n,P/n)
r=json.loads((P/'theta-equiv193-original-receipt.json').read_text());z=r['result']['structuredContent'];z=z.get('result',z)
type_=next(x['message'].split(': ',1)[1]for x in z['items']if x['message'].startswith('THETAEQUIV193_FULL_TYPE:'))
dump('native-type.json',dict(type=type_,axioms=['propext','Classical.choice','Quot.sound'],source_line=159))
dump('verification.json',dict(declaration='Roth.\u0398_equiv',unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=[dict(source='theta-equiv193-project-rejected-executed.lean.txt',receipt='theta-equiv193-project-rejected-receipt.json',reason='Initial preparation lacked do return and inverse simp; root corrected those before execution. Executed attempt still had nested local polymorphic universe declaration, nonzero simp and degree composition issues; rejected in full, not accepted as proof.')],audit=dict(source='theta-equiv193-audit-executed.lean.txt',receipt='theta-equiv193-original-receipt.json',requested=293,unique=293,present=293,values=293),canonical_direct_consumers=['_private.Roth.Theta.0.Roth.theta_lt_succ_aux'],canonical_direct_type_consumers=[],composition=dict(parent_reaim_checked=True,outer_law_existing='congrArg',reindex_law_existing='Equiv.iSup_congr',bridge_definitional=False,full_arithmetic_family_bridge_verified=True,strict_three_existing_call_term_verified=False,parent_project_lemma_counted_as_mathlib_block=False,actual_caller_replays=1,actual_call_occurrences=1,no_circular_use_of_target_in_new_proof=True,no_global_absence_claim=True)))
