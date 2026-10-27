from pathlib import Path
import hashlib,json,shutil,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='MvPolynomial.taylor_rename'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def rg(label,pattern,paths):
 args=['rg','-n',pattern,*paths];r=subprocess.run(args,cwd=R,text=True,capture_output=True)
 out('rg-'+label+'.json',dict(args=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));return r.stdout
for label,pattern,paths in [
 ('current',r'taylor_rename|rename.*taylor|taylor.*rename',['.lake/packages/mathlib/Mathlib/Algebra']),
 ('literature',r'rename_eval₂|rename_expand|rename_comp_expand',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
 ('abstract',r'aeval_rename|aeval_comp_rename|comp_aeval_apply',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),
 ('full-name',r'MvPolynomial\.taylor_rename|\b(theorem|lemma)\s+taylor_rename\b',['.lake/packages/mathlib/Mathlib']),
 ('callers',r'\btaylor_rename\b',['Roth.lean','Roth']),
 ('inline',r'rename_eq_aeval|aeval_rename|comp_aeval_apply|rename.*taylor|taylor.*rename',['Roth.lean','Roth']),
 ('local-literature',r'rename|renaming|larger polynomial|embedded|variable renaming',['.mathlib-quality/references/clean.tex'])]:rg(label,pattern,paths)
# Current form legitimately has no exact mathlib name: a zero-result rg is not an absence proof.
manifest=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=[]
for p,x in manifest['sources_and_pins'].items():
 f=R/p;inputs.append(dict(path=p,sha256=sha(f),baseline_sha256=x['sha256'],bytes=f.stat().st_size,match=sha(f)==x['sha256']))
assert len(inputs)==17 and all(x['match'] for x in inputs)
out('inputs.json',inputs);out('input-hash-check.json',dict(all_pass=True,count=17))
shutil.copy(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
entries=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());out('canonical-entry.json',next(x for x in entries if x['name']==N))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
if isinstance(order,dict):order=order.get('declarations',order.get('order',[]))
out('order-entry.json',next(x for x in order if x['name']==N))
links={'Roth/Taylor.lean':'Taylor-module.lean.txt','Roth/Index.lean':'Index-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Rename.lean':'MvPolynomial-Rename-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean':'MvPolynomial-Eval-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Monad.lean':'MvPolynomial-Monad-module.lean.txt'}
mi=[]
for p,n in links.items():
 shutil.copy(R/p,D/n)
 if p.startswith('.lake'):mi.append(dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size))
out('mathlib-inputs.json',mi)
clean=R/'.mathlib-quality/references/clean.tex';out('local-literature.json',dict(path=str(clean.relative_to(R)),sha256=sha(clean),bytes=clean.stat().st_size,lines='615–634',role='Lemma4-2 embedding and explicit variable-renaming implementation note'))
(D/'clean-excerpts.tex.txt').write_text('\n'.join(clean.read_text().splitlines()[614:635])+'\n')
out('callers.json',dict(named_callers=[dict(declaration='Roth.index_rename',file='Roth/Index.lean',line=216,role='rewrite translated renamed polynomial before support and weight transport',verified='full caller proof native-extra')],explicit_count=1,source_occurrences=['Roth/Taylor.lean:164 declaration','Roth/Index.lean:216 caller'],inline_audit='No independent inline rederivation found. Nearby hasseDeriv_rename is derivative naturality, not translation commutation.',limitations='Named source references, not exhaustive kernel/simp dependency closure. No simp attribute on target.'))
out('proof-body-diagnostic.json',dict(concrete_identifier='taylor',unfolded='aeval(X+Cα)',abstract='generic aeval/rename and AlgHom composition compatibility',existing=['aeval_rename','comp_aeval_apply'],bridge='Five mathematical fact applications for normalized shifted-generator equality; not definitional.'))
accepted=[]
for label in ['target','raw','extra']:
 for ending in ['executed.lean.txt','success.json']:shutil.copy(Path('/private/tmp/roth-overview')/f'taylor-rename-{label}-{ending}',D/f'native-{label}-{ending}')
 accepted.append(dict(label=label,source=f'native-{label}-executed.lean.txt',source_sha256=sha(D/f'native-{label}-executed.lean.txt'),receipt=f'native-{label}-success.json',proof_check=True))
rejected=[]
for p in Path('/private/tmp/roth-overview').glob('taylor-rename-raw-rejected*'):
 shutil.copy(p,D/p.name.replace('taylor-rename-','native-'))
if (D/'native-raw-rejected.json').exists():rejected=[dict(source='native-raw-rejected.lean.txt',receipt='native-raw-rejected.json',reason='Initial congr 1 stopped at AlgHom equality; subsequent funext failed. Corrected explicit congrArg on assignment functions. No limit change.')]
out('verification.json',dict(declaration=N,standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,inputs='inputs.json',mathlib_inputs='mathlib-inputs.json',source_links=links,composition=dict(raw_count=5,raw_math_facts=['aeval_rename','comp_aeval_apply','map_add','rename_X','rename_C'],abstract_single_call='aeval_rename f g P',old_form_not_defeq=True),unresolved=[]))
out('assessment.json',dict(declaration=N,canonical_index=68,source='Roth/Taylor.lean:164',kind='theorem',verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']},justified_na={'2b':'Theorem, not a data definition.','4.5':'Theorem creates no definition/instance; all six infrastructure risk rows n/a.'},unresolved=[],root_acceptance='pending',production_unchanged=True))
out('overview-entry.json',dict(declaration=N,kind='theorem',type='∀ {σ : Type u} {R : Type v} [CommSemiring R] {τ : Type w} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R), MvPolynomial.taylor α (MvPolynomial.rename f P) = MvPolynomial.rename f (MvPolynomial.taylor (α ∘ f) P)',what='Translation commutes with arbitrary variable renaming, restricting the shift along the variable map.',how='Generic aevaluation/renaming composition, then normalization of shifted generators.',hypotheses='Arbitrary independent-universe σ,τ,R; CommSemiring R; arbitrary map f including noninjective, arbitrary α,P. No finiteness/characteristic/nonzero assumptions.',project_dependencies=['MvPolynomial.taylor'],caller_summary='One explicit source caller Roth.index_rename at Index216; full native caller replay succeeds using fresh target replay. Its injectivity assumption belongs to support/weight transport.',mathlib_api_audit='aeval_rename and comp_aeval_apply are exact abstract compatibility laws. Original normalized translation square requires five mathematical facts; not a one-call defeq replacement.',moral_duplications='Generic substitution naturality specialized to shifted generators; close analogue rename_expand, not same substitution.',generalization='Maximal within parent CommSemiring interface; bundled AlgHom square and arbitrary target-algebra evaluation verified. No mechanical weakening established.',missing_api='No generic substitution gap; decision whether named multivariate translation API merits explicit rename convenience law.',junk='Used in index invariance, not dead code. One source use and generic derivation do not by themselves force deletion.',action='BORDERLINE: choose named convenience law versus generic substitution API, bundled square and naming/orientation. Read-only assessment complete; production unchanged.'))
