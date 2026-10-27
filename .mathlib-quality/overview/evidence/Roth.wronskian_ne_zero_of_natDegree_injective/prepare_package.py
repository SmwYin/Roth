from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
name='Roth.wronskian_ne_zero_of_natDegree_injective'
def write(n,d): (p/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
sha=lambda b:hashlib.sha256(b).hexdigest()
typ=json.loads((p/'native-selected.json').read_text())['target']['selected_messages'][0].split(' : ',1)[1]
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
write('assessment.json',dict(declaration=name,canonical=47,source='Roth/Wronskian.lean:148',verdict='YES-but-generalise-first',completed=True,allphases='PASS',phases={k:'PASS' for k in phases},justified_na={'2b':'theorem, definition-only one-line test','4.5':'theorem; all six infrastructure rows n/a with individual reasons in report'},unresolved=[],root_acceptance='pending'))
accepted=[]
for label in ['target','domain','recovery','abstract','guards']:
 source='native-'+label+'-executed.lean.txt';receipt='native-'+label+'-success.json'
 accepted.append(dict(label=label,source=source,source_sha256=sha((p/source).read_bytes()),receipt=receipt))
write('verification.json',dict(declaration=name,accepted=accepted,standard_axioms=['propext','Classical.choice','Quot.sound'],unresolved=[],inputs='source-pin-hashes.json',mathlib_inputs='mathlib-source-hashes.json',source_links={'Roth/Wronskian.lean':'source-wronskian.lean.txt','.mathlib-quality/references/clean.tex':'source-clean.tex.txt'},web_metadata=sorted(f.name for f in p.glob('web-*-metadata.json')),native_boundary='Root alone executed native tools. Worker prepared code and reviewed actual complete raw receipts. Accepted sources preserve exact executions; composition and intermediate failures segregated.',rejected_composition=dict(source='native-composition-executed.lean.txt',receipt='native-composition-rejected.json'),isolated_target_guard=['domain'],expected_axiom_messages={'target':'WronskianDistinctAssessment.replay','domain':'DistinctDegreeProbe.generalized','recovery':'WronskianDistinctRecover.caller_rebuilt','abstract':'DistinctDegreeAbstract.existing','guards':'DistinctDegreeGuards.domain_needed'}))
write('overview-entry.json',dict(declaration=name,kind='theorem',type=typ,what='Nonzero polynomials of distinct degrees have nonzero normalized Hasse Wronskian in characteristic zero.',how='One coefficient equals product of leading coefficients times a binomial determinant; Vandermonde gives nonvanishing.',hypotheses=['Field K','CharZero K','all family members nonzero','natural-degree function injective'],project_dependencies=['Roth.wronskian','Roth.coeff_wronskian_of_natDegree_injective','Roth.det_choose_eq'],caller_summary=dict(total_explicit_proof_callers=1,within_file=1,outside_file=0,internal_use_count_excluding_declaring_file=0,callers=['Roth/Wronskian.lean:210 Roth.wronskian_ne_zero_of_linearIndependent'],inline_rederivations=[]),mathlib_api_audit='Mathlib has binary Polynomial.wronskian, an explicit n-tuple TODO, and generic Matrix.det_vandermonde_ne_zero_iff. All five actual methods searched current/literature/abstract forms; no direct family replacement. Local index unavailable does not prove absence.',moral_duplications='Generic coefficient nonzero and Vandermonde nonzero steps already abstract. Hasse coefficient and binomial conversion bridges remain new mathematical helpers; downstream criterion cannot be used circularly.',generalization='Verified same-parent Field weakening removes global CharZero in favor of cast-degree injectivity. Separately verified expanded CommRing+IsDomain form. No factorial-nonzero premise needed. ZMod2 positive and negative guards; ZxZ zero-divisor guard.',missing_api='N-ary Hasse Wronskian top-coefficient/nonvanishing API, supported by cancellation-free binomial determinant identity.',junk=False,action='YES-but-generalise-first: /generalise target for cast-degree hypothesis; group with accepted coefficient theorem and coordinate determinant support; /cleanup before upstream Wronskian.lean PR. Sole caller supplies Nat.cast_injective.comp hinj.'))
repo=Path('/Users/ramin/LEAN/Roth')
canonical=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
write('canonical-metadata.json',next(x for x in canonical if x['name']==name))
def manifest():
 files=[]
 for f in sorted(p.iterdir()):
  if not f.is_file() or f.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']: continue
  dst=f'.mathlib-quality/overview/mathlibable/{name}.md' if f.name=='report.md' else f'.mathlib-quality/overview/evidence/{name}/{f.name}'
  b=f.read_bytes();files.append(dict(source=str(f),destination=dst,sha256=sha(b),bytes=len(b)))
 write('copy-manifest.json',dict(declaration=name,files=files))
manifest()
