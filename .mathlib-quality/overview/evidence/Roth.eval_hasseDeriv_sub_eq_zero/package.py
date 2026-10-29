from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.eval_hasseDeriv_sub_eq_zero'
def rd(n):return json.loads((D/n).read_text())
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
questions=['Should a generic equal-remainder evaluation law be public Polynomial API given the root-preservation law and short trans/congrArg derivation?', 'Should a coefficient-independent diagonal-evaluation bridge accompany multivariate Hasse API leaving the one-use vanishing corollary local?', 'If a Hasse corollary is desired should its hypothesis be equal remainders or divisibility of the diagonal difference?']
put('assessment.json',dict(declaration=N,canonical_index=251,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']},justified_na={'definition_one_line':'Theorem, not a data declaration.','infrastructure_six':'All six n/a: theorem adds no definitions, instances or coercions.','optional_chatgpt_math':'ask_chatgpt_math unavailable.'},unresolved=[],questions=questions,root_acceptance='pending',cost_based_verdict=False,parent_verdict_inherited=False))
accepted=[]
for label,fmt,required in [
 ('original','disk',['VANISH251_SIGNATURE_IDENTICAL','VANISH251_AUDIT: requested=293; unique=293','VANISH251_AUDIT_PRESENT: present=293; values=293']),
 ('isolated','run_code',['Vanish251Isolated.eval_eq_of_mod_eq','Vanish251Isolated.observe','Vanish251Isolated.divisibility','Vanish251Isolated.root_needed','Vanish251Isolated.equality_needed']),
 ('recovery','disk',['VANISH251_RECOVERY_SIGNATURE_IDENTICAL']),
 ('inline','disk',['VANISH251_INLINE_SIGNATURE_IDENTICAL','VANISH251_INLINE_NO_TARGET']),
 ('metadata','disk',['VANISH251_TYPE_CONSTANTS:','VANISH251_BODY_CONSTANTS:']),
 ('composition','disk',['Vanish251Project.generalized','Vanish251Project.direct'])]:
 src=('original'if label=='original'else label)+'-executed.lean.txt';rec='original-receipt.json'if label=='original'else label+'-receipt.json'
 accepted.append(dict(label=label,format=fmt,source=src,receipt=rec,source_sha256=sha(D/src),original_execution_request=rd(rec)['request'],native_region_start_line=17 if fmt=='disk' else 19,required_info=required))
rejected=[]
for p in sorted(D.glob('*rejected*-receipt.json')):
 s=p.name.replace('-receipt.json','-executed.lean.txt');rejected.append(dict(source=s,receipt=p.name,format='run_code'if s.startswith('isolated')else'disk'))
put('verification.json',dict(declaration=N,canonical_index=251,completed=True,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,warming=[],full_actual_callers=dict(count=1,original_signatures_verified=1,complete_original_module_inline=True,target_absent_from_new_caller=True),controls=dict(shared_prefix_sha256=sha(D/'isolated-prefix.lean.txt'),disk_prefix_sha256=sha(D/'disk-prefix.lean.txt'),production_sources_unchanged=True,extra_isolated_imports=0,shared_import_count=18,disk_import_count=9,file_end_build='Not required at251; accepted228 file-end build reused; next266.')))
print('Prepared completed metadata from accepted receipts; root acceptance pending')
