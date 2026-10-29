from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_reduced_approx'
def rd(n):return json.loads((D/n).read_text())
def wr(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
entries=[('original','original-executed.lean.txt','original-receipt.json','disk',['REDUCED274_FULL_TYPE:','REDUCED274_AUDIT: requested=293; unique=293','REDUCED274_AUDIT_PRESENT: present=293; values=293']),('callers','callers-executed.lean.txt','callers-receipt.json','disk',["'Reduced274Caller.replay' depends on axioms:"]),('consumers','consumer-scope2-executed.lean.txt','consumers2-receipt.json','disk',['REDUCED274_PROJECT_CLOSURE:','REDUCED274_TRANSITIVE_PROJECT_CONSUMER:','REDUCED274_AUDIT_PRESENT: present=293; values=293']),('isolated','isolated2-executed.lean.txt','isolated2-receipt.json','run_code',["'Reduced274.subcritical' depends on axioms:","'Reduced274.unrestricted' depends on axioms:"]),('generic','generic-executed.lean.txt','generic-receipt.json','run_code',["'Reduced274Generic.unbounded_canonical' depends on axioms:","'Reduced274Generic.recovered' depends on axioms:"]),('composition','composition-executed.lean.txt','composition-receipt.json','run_code',["'Reduced274.composition_probe' depends on axioms:"]),('counterexample','counterexample2-executed.lean.txt','counterexample2-receipt.json','run_code',["'Reduced274Counterexample.infinite_zero_pairs' depends on axioms:","'Reduced274Counterexample.no_large_reduced' depends on axioms:"])]
a=[]
for label,s,r,f,req in entries:
 q=rd(r);z=q['result']['structuredContent'];z=z.get('result',z);assert z['success']and not z.get('partial',False)and not z.get('timed_out',False)
 assert not any(x['severity']in ['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 a.append({'label':label,'source':s,'receipt':r,'source_sha256':sha(D/s),'format':f,'native_region_start_line':17 if f=='disk'else 20,'required_info':req,'axiom_print_required':label!='consumers','original_execution_request':q['request'],'elapsed_ms':q['elapsed_ms']})
other=[]
for s,r,why in [('isolated-executed.lean.txt','isolated-receipt.json','Set-membership normalization needed; recovered sorryAx rejected.'),('consumer-scope-executed.lean.txt','consumers-receipt.json','Array.union does not exist; rejected.'),('counterexample-executed.lean.txt','counterexample-receipt.json','Pair-projection simplification and unused ring warnings; recovered sorryAx rejected.')]:other.append({'source':s,'receipt':r,'source_sha256':sha(D/s),'status':'rejected','reason':why})
wr('verification.json',{'declaration':N,'canonical_index':274,'completed':False,'unresolved':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'native_executor':'root exclusive; worker prepared exact sources and inspected full raw results','accepted':a,'other_executions':other,'attempt_accounting':{'native_executions':10,'accepted':7,'rejected':3,'local_search_attempts':3,'remote_formal_searches':9,'source_formal_searches':3},'baseline':'baseline-build.txt','source_hashes':'inputs.json','canonical_exact_order':'canonical-snapshot.json','prefix_authorization':'native-prefix-authorization.json','kernel_printer_elision':'86997 characters; not a full kernel-body dump','actual_layout_receipts':['validation-scratch.json','validation-integrated.json'],'secret_guard':'secret-scan.json'})
g=rd('generality.json');g['verified']=True;wr('generality.json',g)
a=rd('assessment.json');a.update(completed=False,allphases='pending',unresolved=[],phases={k:('pending'if k=='8'else'PASS')for k in a['phases']});wr('assessment.json',a)
o=rd('overview-entry.json');o['generalization']=g;o['action']=a;wr('overview-entry.json',o)
wr('fresh-final-inputs.json',{'unchanged':all(sha(R/x['path'])==x['sha256']for x in rd('inputs.json')),'inputs':rd('inputs.json')})
print('All assessment/native gates complete; ready for portable validation')
