"""Install already reviewed final artifacts after publisher293; no Git or Lean execution.
This script is prepared ahead of the frontier. It cannot install a partial final review.
"""
from pathlib import Path
import hashlib,json,shutil,sys,subprocess,re
R=Path('/Users/ramin/LEAN/Roth');B=Path('/private/tmp/roth-overview');O=R/'.mathlib-quality/overview'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
assert sys.argv[1:]==['--after-publisher293']
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='ramin-cleanup'
p=load(O/'progress.json');assert p['status']=='complete'and len(p['completed_declarations'])==293 and p['next_declaration']is None
ready=load(B/'final-readiness.json');assert ready['status']=='PASS'and ready['root_reviewed']is True and ready['declaration_count']==293
assert len(ready['checks'])==11 and set(ready['checks'].values())=={'PASS'}
plan=load(B/'FINAL_BUNDLE_PLAN.json');assert plan['status']=='FINAL-BUNDLE-PLAN'and plan['accepted_declaration_count']==293
inv=load(B/'final-completed-inventory-preparation.json');assert inv['completed_count']==293
final=Path(ready['final_overview_source']);assert H(final)==ready['final_overview_sha256']
for a in ready['artifacts']:assert H(Path(a['source']))==a['sha256']
base=load(O/'evidence/shared/input-manifest.json')['sources_and_pins']
for f,v in base.items():assert H(R/f)==v['sha256']
# Check every destination and source before the first tracked mutation.
for a in plan['files']:
 dest=R/a['destination'];assert dest.is_relative_to(O/'evidence/final')
 assert H(Path(a['source']))==a['sha256']and Path(a['source']).stat().st_size==a['bytes']<50_000_000
assert len({a['destination']for a in plan['files']})==len(plan['files'])
reconcile=load(B/'final-readme-reconciliation-preparation.json');readme=R/reconcile['target']
assert H(readme)==reconcile['original_sha256']and readme.read_text().count(reconcile['old'])==1
for a in plan['files']:
 dest=R/a['destination'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a['source'],dest)
D=O/'evidence/final'
shutil.copyfile(B/'final-readiness.json',D/'final-readiness.json')
planned={Path(a['source']).resolve()for a in plan['files']};extra=[]
for a in ready['artifacts']:
 source=Path(a['source'])
 if source.resolve()in planned:continue
 dest=D/source.name
 assert not dest.exists()or H(dest)==a['sha256'],dest
 shutil.copyfile(source,dest)
 extra.append(dict(source=str(source),destination=str(dest.relative_to(R)),sha256=H(dest),bytes=dest.stat().st_size))
manifest=dict(plan,copied_to_repository=True,status='INSTALLED-FINAL-REVIEW-BUNDLE',original_plan_sha256=H(B/'FINAL_BUNDLE_PLAN.json'),readiness_support_artifacts=extra)
(D/'copy-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
shutil.copyfile(final,R/'PROJECT_OVERVIEW.md')
links='\n\nFinal supporting evidence: [native dependency graph](evidence/final/final-kernel-graph.json), '+\
 '[canonical direct dependencies](evidence/final/final-canonical-direct-dependencies.json), '+\
 '[native binder repairs](evidence/final/final-inventory-type-repair-plan.json), '+\
 '[historical metadata resolutions](evidence/final/final-project-dependency-reviewed-resolutions.json), '+\
 '[full pairwise comparison index](evidence/final/pairwise/README.md), '+\
 '[both actual final builds](evidence/final/final-build-verification.json), and '+\
 '[copied evidence manifest](evidence/final/copy-manifest.json).'
readme.write_text(readme.read_text().replace(reconcile['old'],reconcile['replacement']+links))
for md in [R/'PROJECT_OVERVIEW.md',readme]:
 for href in re.findall(r'\]\(([^)]+)\)',md.read_text()):
  if not href.startswith(('https://','http://','#')):assert(md.parent/href.split('#')[0]).exists(),(md,href)
for a in plan['files']:assert H(R/a['destination'])==a['sha256']
# These are actual checks against the copied repository layout, not private scratch dependencies.
commands=[['python3',str(D/'validate_portable_semantic_pairs.py'),str(R),str(D/'pairwise'),str(D/'final-completed-inventory-preparation.json'),'--require-complete'],['python3',str(D/'validate_portable_global_evidence.py'),str(R),str(D),'--require-complete'],['python3',str(O/'evidence/shared/scan_evidence_secrets.py')]]
receipts=[]
for cmd in commands:
 q=subprocess.run(cmd,cwd=R,text=True,capture_output=True);receipts.append(dict(command=cmd,exit_code=q.returncode,stdout=q.stdout,stderr=q.stderr));print(q.stdout,end='',flush=True)
 assert q.returncode==0,q.stderr
(D/'postintegration-validation.json').write_text(json.dumps(dict(status='PASS',checks=receipts,production_changed=False),indent=2,ensure_ascii=False)+'\n')
(D/'README.md').write_text("""# Final whole-repository review evidence

All293 canonical declaration assessments and all42,778 unordered semantic comparisons
are complete. Production Lean sources and the17 source/pin hashes remain unchanged.

The inventory/pair evidence was assembled immediately before publication of declaration293,
from292 tracked assessments plus its complete independently root-reviewed candidate.
Its original preparation labels and temporary source paths are retained as provenance;
they do not indicate unfinished assessments at this final commit. All293 reports and their
accepted evidence now exist in the tracked repository. Read the authoritative
[progress record](../../progress.json) and [final overview](../../../../PROJECT_OVERVIEW.md).

- [Root final review](root-final-review.json) and [publication readiness](final-readiness.json).
- [Installed evidence manifest](copy-manifest.json), preserving exact source hashes/locations.
- [Actual postintegration validation](postintegration-validation.json).
- [Both literal final builds](final-build-verification.json), including exact logs and hashes.
- [Complete inventory](final-completed-inventory-preparation.json).
- [Every semantic comparison, by module pair](pairwise/README.md).
- [Native direct dependency graph](final-kernel-graph.json) and
  [canonical mapping](final-canonical-direct-dependencies.json).
- [Native binder repairs](final-inventory-type-repair-plan.json) and
  [historical dependency metadata resolutions](final-project-dependency-reviewed-resolutions.json).

Raw native receipts and exact executed source archives are preserved unchanged. Direct
kernel references do not establish full generated/simp/transitive closure or external
deadness. Pair judgments are mathematical reviews, not machine proofs of inequivalence.
Private declarations have the explicitly justified public-contribution prefilter; the
applicable source/native/caller assessments are complete. Optional ask_chatgpt_math was
unavailable; unsuccessful and warming attempts are retained separately from accepted proofs.

The portable validators accept the repository and evidence-directory paths as arguments;
they do not require the original private scratch registries. Preparation/generator scripts
retain historical local paths and are supplied as provenance, without that portability claim.
""")
for href in re.findall(r'\]\(([^)]+)\)',(D/'README.md').read_text()):
 assert (D/href).exists(),href
print('PASS actual final copied bundle/overview/README links and portable complete293 checks. No commit or push performed.')
