"""Prepare final publisher gate only after actual complete293 root review.
Prepared before the frontier; no Git, production edits, native execution or implicit acceptance.
"""
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path('/Users/ramin/LEAN/Roth');B=Path('/private/tmp/roth-overview');O=R/'.mathlib-quality/overview'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
assert sys.argv[1:]==['--root-reviewed-complete293']
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='ramin-cleanup'
p=load(O/'progress.json');order=load(O/'declaration-order.json');assert len(p['completed_declarations'])==292 and p['next_declaration']==order[292]['name']
N=p['next_declaration'];D=B/'assess'/N;a=load(D/'assessment.json');rr=load(D/'root-review.json');assert a['completed']and not a['unresolved']and rr['status']=='PASS'and H(D/'report.md')==rr['report_sha256']
I=load(B/'final-completed-inventory-preparation.json');assert I['completed_count']==293 and I['published_count']==292 and I['has_unpublished_final_candidate']
assert [x['declaration']for x in I['rows']]==[x['name']for x in order]
P=load(B/'final-pairwise-partitions/index.json');assert P['complete_project_pair_coverage']and P['pair_count']==42778 and P['inventory_sha256']==H(B/'final-completed-inventory-preparation.json')
ledger=load(B/'GLOBAL_PREPARATION_VALIDATION.json');assert ledger['status']=='PASS-preintegration-checks'and ledger['completed_declaration_count']==293
assert ledger['steps']and all(x['exit_code']==0 and H(Path(x['command'][1]))==x['script_sha256']for x in ledger['steps'])
plan=load(B/'FINAL_BUNDLE_PLAN.json');assert plan['status']=='FINAL-BUNDLE-PLAN'and plan['accepted_declaration_count']==293
for x in plan['files']:assert H(Path(x['source']))==x['sha256']and Path(x['source']).stat().st_size==x['bytes']<50_000_000
final=B/'FINAL_PROJECT_OVERVIEW_CANDIDATE.md';assert '293/293 declaration assessments complete'in final.read_text()
required={'inventory','cross_file_dependencies','mathlib_api_audit','semantic_pairwise_review','generality','missing_api','junk_and_reachability','all_mathlibable_reports','action_buckets','source_pin_preservation','final_build'}
root=load(B/'root-final-review.json');assert root['reviewer']=='root'and root['status']=='PASS'and root['root_reviewed']is True
assert root['mathematical_review']and root['overview_sha256']==H(final)and root['bundle_plan_sha256']==H(B/'FINAL_BUNDLE_PLAN.json')
assert set(root['checks'])==required and set(root['checks'].values())=={'PASS'}
base=load(O/'evidence/shared/input-manifest.json')['sources_and_pins'];assert len(base)==17
for f,x in base.items():assert H(R/f)==x['sha256']
build=load(B/'final-build-verification.json');assert build['status']=='PASS'
for b,cmd in [(build,['lake','build']),(build['lean_eval'],['lake','build','Roth.LeanEval'])]:
 assert b['command']==cmd and b['exit_code']==0 and H(Path(b['log']))==b['log_sha256']
 assert 'Build completed successfully'in Path(b['log']).read_text()
reports=[]
for i,x in enumerate(I['rows']):
 f=D/'report.md'if i==292 else R/x['report'];assert H(f)==x['report_sha256']
 reports.append(dict(declaration=x['declaration'],source=str(f),sha256=H(f)))
# Actual candidate/native/manifests and exact partition preservation are required before readiness.
for cmd in [['python3',str(D/'validate.py'),str(R)],['python3',str(B/'validate_partitioned_pair_evidence.py')],['python3',str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)]]:subprocess.run(cmd,cwd=R,check=True)
paths={Path(x['source'])for x in plan['files']}|{B/'FINAL_BUNDLE_PLAN.json',B/'GLOBAL_PREPARATION_VALIDATION.json',B/'root-final-review.json',Path(__file__).resolve(),B/'install_final_bundle.py',B/'commit_final_review.py'}
ready=dict(status='PASS',root_reviewed=True,declaration_count=293,checks=root['checks'],reports=reports,artifacts=[dict(source=str(f),sha256=H(f))for f in sorted(paths)],final_overview_source=str(final),final_overview_sha256=H(final),candidate_report_sha256=rr['report_sha256'],final_build=build,scope='Root independently reviewed complete293 assessment and global synthesis, actual dual builds and preintegration gates; postintegration portable gates remain mandatory before commit/push.')
(B/'final-readiness.json').write_text(json.dumps(ready,indent=2,ensure_ascii=False)+'\n');print('PASS final readiness prepared from actual root-reviewed complete293 evidence. Publisher/integration/portable tracked gates/commit/push still separate.')
