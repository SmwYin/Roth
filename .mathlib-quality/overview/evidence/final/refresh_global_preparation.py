"""Revalidate root-reviewed aggregate preparation; no Git/native Lean/mathematical auto-assessment.
Run only after inventory and every new semantic pair/action disposition are root-reviewed.
Optional --preintegration-final uses explicit root-reviewed293 candidate; portable tracked-layout
checks then run separately after publisher293 integration and before any final commit/push.
"""
from pathlib import Path
import subprocess,json,hashlib,time,sys
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();I=json.loads((B/'final-completed-inventory-preparation.json').read_text());n=I['completed_count'];pre='--preintegration-final'in sys.argv
if pre:assert n==293 and I['has_unpublished_final_candidate']and I['published_count']==292
else:assert n==len(json.loads((R/'.mathlib-quality/overview/progress.json').read_text())['completed_declarations'])
steps=[('refresh_action_synthesis_coverage.py',[]),('validate_action_synthesis_coverage.py',[]),('prepare_final_indexes.py',['--accepted-final-candidate']if pre else[]),('refresh_junk_current_coverage.py',[]),('render_final_inventory_preview.py',[]),('render_cross_file_preview.py',[]),('render_pairwise_preview.py',[]),('prepare_partitioned_pair_evidence.py',['--require-complete']if pre else[]),('validate_partitioned_pair_evidence.py',[]),('render_partitioned_pair_tables.py',['--require-complete']if pre else[])]
if not pre:steps+=[('validate_portable_semantic_pairs.py',[str(R),str(B/'final-pairwise-partitions'),str(B/'final-completed-inventory-preparation.json')]),('validate_portable_global_evidence.py',[str(R),str(B)])]
# Preview never silently becomes the final overview; --require-complete renderer is a later
# separately reviewed step after real final build logs and the complete293 scope are ready.
steps+=[('render_whole_overview_preparation.py',[])]
ledger={'status':'RUNNING','completed_declaration_count':n,'scope':'Root-reviewed aggregate preparation only; not final whole-repository readiness or permission to mark project done','preintegration_final_candidate':pre,'portable_tracked_layout_checks_deferred_until_postintegration':pre,'steps':[]}
try:
 for name,args in steps:
  p=B/name;cmd=['python3',str(p),*args];start=time.monotonic();r=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
  ledger['steps'].append(dict(command=cmd,script_sha256=H(p),exit_code=r.returncode,elapsed_ms=round((time.monotonic()-start)*1000),stdout=r.stdout,stderr=r.stderr));print(r.stdout,end='',flush=True)
  if r.returncode:raise RuntimeError(name+': '+r.stderr)
 ledger['status']='PASS-preintegration-checks'if pre else'PASS-completed-prefix-checks'
except Exception:
 ledger['status']='FAIL';(B/'GLOBAL_PREPARATION_VALIDATION.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n');raise
(B/'GLOBAL_PREPARATION_VALIDATION.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
r=subprocess.run(['python3',str(B/'prepare_final_bundle_plan.py')],cwd=R);assert r.returncode==0
print('PASS recorded actual aggregate validation commands/exit statuses/output/timings; bundle plan prepared, no tracked edits')
