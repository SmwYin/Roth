#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,shutil
D=Path(__file__).resolve().parent; R=Path.cwd(); T=D.parent.parent; N='Roth.det_sum_rows'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(D/n).write_text(json.dumps(v,indent=2)+'\n')
def native(rec):
 x=rec['result'];x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
for p in T.glob('det-sum-rows-*'):
 if p.is_file():shutil.copyfile(p,D/p.name)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[116]['name']==N
save('canonical-snapshot.json',order);save('canonical-entry.json',order[116])
s=(D/'det-sum-rows-audit-executed.lean.txt').read_text();arr=re.search(r'let names : Array Lean.Name := #\[.*?\]',s,re.S).group(0)
(D/'canonical-audit-array.lean.txt').write_text(arr+'\n')
r=native(json.loads((D/'det-sum-rows-original-receipt.json').read_text()));msg=[x['message'] for x in r['items'] if x.get('line',0)>=8218 and x['message'].startswith(N+'.')][0]
(D/'original-type.txt').write_text(msg+'\n')
accepted=[]
for label,start in {'original':8218,'audit':8222,'raw-clean':1,'dependent':1,'abstract':1,'drop':1,'consumer-clean':8541,'recovery':1}.items():
 sn=f'det-sum-rows-{label}-executed.lean.txt';rn=f'det-sum-rows-{label}-receipt.json';rec=json.loads((D/rn).read_text());nr=native(rec);assert nr['success'] and not nr.get('partial',False)
 ds=nr.get('items',nr.get('diagnostics',[]));assert not [x for x in ds if x.get('severity') in ['error','warning']]
 names=[]
 for x in ds:
  if x.get('line',0)>=start:
   m=re.match(r"'([^']+)' depends on axioms:",x.get('message',''))
   if m:names.append(m[1])
 accepted.append(dict(label=label,source=sn,source_sha256=sha(D/sn),receipt=rn,original_execution_request=rec['request'],execution_kind='persistent-disk' if 'file_path' in rec['request'] else 'run-code',native_region_start_line=start,expected_axiom_declarations=names))
rejected=[]
for label in ['raw','simp','consumer']:
 sn=f'det-sum-rows-{label}-executed.lean.txt';rn=f'det-sum-rows-{label}-receipt.json';rec=json.loads((D/rn).read_text());nr=native(rec);ds=nr.get('items',nr.get('diagnostics',[]));errs=[x['message'] for x in ds if x.get('severity') in ['error','warning']];assert errs
 rejected.append(dict(label=label,source=sn,receipt=rn,reason='; '.join(errs),original_execution_request=rec['request']))
save('verification.json',dict(declaration=N,accepted=accepted,rejected=rejected,unresolved=[],production_unchanged=True,standard_axioms=['propext','Classical.choice','Quot.sound'],canonical_direct_consumers=['_private.Roth.GenWronskian.0.Roth.wronskian_kronecker_eq_sum_aux'],notes=['Persistent disk full receipts have historical info; proof assertions scoped to fresh target regions. All-file errors/warnings/axioms checked.','Run-code has diagnostics and no partial field; guarded #check_failure expected failures are informational diagnostics.','Rejected raw/simp/caller drafts retain sorryAx and are excluded from accepted proof evidence.','Exact abstract weighted simpa succeeds; exact weighted determinant one-shot simpa fails. Explicit representation bridge is separately clean.','Exact strongest dependent theorem recovers original Fin l type in mathlib-only isolation; actual Wronskian caller replay is separately verified.']))
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; all six infrastructure categories accounted for'
save('assessment.json',dict(declaration=N,canonical_index=117,source='Roth/GenWronskian.lean:228',verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,composition='BORDERLINE trivial simp composition',verified_weakening='arbitrary finite square J; row-dependent I; original recovery and actual caller checked',future_api_questions=['Determinant-specific weighted expansion convenience theorem?','Prefer generic weighted multilinear finite-sum helper?','Use finite arbitrary square index and row-dependent summand types if accepted?']))
save('overview-entry.json',dict(declaration=N,kind='theorem',type='@'+msg.replace(N+'.{u_3, u_4}',N,1),what='Expand determinant whose rows are finite linear combinations into finite choices, weighted by coefficient products.',how='Specialize existing multilinear finite-sum law, extract simultaneous scalars, normalize function/matrix/scalar representations.',hypotheses=['CommRing A; arbitrary A, no field/domain/characteristic condition','Fin l square matrix; arbitrary summand type ι; finite support per row','arbitrary s,c,N with no nonempty/nonzero assumptions'],project_dependencies=[],caller_summary='One explicit same-file private caller wronskian_kronecker_eq_sum_aux at line245, no external-to-file caller. Exact293 canonical audit agrees; clean full caller replay available.',mathlib_api_audit='MultilinearMap.map_sum_finset and map_smul_univ provide abstract mathematical content; detRowAlternating supplies determinant witness; explicit normalization bridge checked. One-shot weighted determinant simpa fails, abstract weighted simpa succeeds.',moral_duplications='Standard multilinearity, already represented by two generic mathlib laws; convenience wrapper inclusion is a Phase6b taste decision.',generalization='Verified arbitrary finite square J and dependent I:J→Type*, original Fin l recovery. Abstract CommSemiring module-valued weighted expansion verified separately; determinant itself still requires CommRing.',missing_api='Possible named weighted multilinear finite-sum convenience law or determinant-specific row-expansion corollary, not a claimed missing mathematical theorem.',junk='Live single-use helper; private local lemma or inlining is concrete alternative.',action='BORDERLINE-needs-human: choose determinant convenience theorem, generic weighted helper, or local-only expansion. If upstreamed broaden finite/dependent indices; no production edits.'))
save('optional-tool-availability.json',dict(ask_chatgpt_math='unavailable',local_index='unavailable; source-backed positive hits only',external_index='Finder default version may differ from pinned project; candidates source/native checked'))
# Freeze the current package manifest last; caller runs credential scan and validator before acceptance.
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dst,sha256=sha(p),bytes=p.stat().st_size))
save('copy-manifest.json',dict(declaration=N,files=files))
print('Packaged',len(files),'artifacts; accepted',len(accepted),'rejected',len(rejected))
