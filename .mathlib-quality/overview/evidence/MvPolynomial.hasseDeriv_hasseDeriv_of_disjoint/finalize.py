from pathlib import Path
import json, hashlib, shutil
p = Path(__file__).resolve().parent
r = Path.cwd()
target = 'MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint'
def put(name, value):
    (p/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')
for stem, local in [('raw', 'raw'), ('final', 'final')]:
    for suffix in ['success.json', 'executed.lean.txt']:
        shutil.copyfile('/private/tmp/roth-overview/hasseDisjoint-'+stem+'-'+suffix, p/(local+'-'+suffix))
for suffix in ['rejected.json', 'rejected.lean.txt']:
    shutil.copyfile('/private/tmp/roth-overview/hasseDisjoint-extra-'+suffix, p/('extra-'+suffix))
disk = r/'.lake/roth-overview-session/NextHasseChecks.lean'
retained = p/'final-executed.lean.txt'
assert disk.read_bytes() == retained.read_bytes()
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
put('final-source-check.json', dict(original_execution_path=str(disk.relative_to(r)), matched_at_freeze=True, retained_sha256=sha(retained), disk_sha256=sha(disk)))
formal=json.loads((p/'formal-search.json').read_text())
for x in formal:
    if x['method']=='local':
        query={'current':'hasseDeriv_hasseDeriv_of_disjoint','literature':'hasseDeriv_comp','abstract':'prod_eq_one'}[x['form']]
        x['request']=dict(query=query,project_root=str(r),limit=8)
put('formal-search.json',formal)
web=json.loads((p/'web-receipts.json').read_text())
summaries=[
    'Three distinct generality-level searches returned canonical Hasse binomial normalization, divided-power and iterative higher-derivation literature.',
    'Site searches investigated nCatLab, Stacks, MathOverflow, recent arXiv; Stacks differential operators and MO positive-characteristic motivation are adjacent, not exact replacement.',
    'Direct nLab XHTML400 and ncatlab path unavailable; recent arXiv full HTML and primary1212.5788PDF returned. Definitions2.1/2.2 distinguish Leibniz from iterativity.',
    'Search snippets returned nLab multivariable definition over commutative rigs. Primary mini-course PDF, Stacks09CH and MO71423 accessed; recent operators research contextual.',
    'Primary1212.5788HTML accessible, nLab direct XHTML400, recent abstracts accessible,2506.19489§4.2Definition4.8 and course Definition2.1.1 located.'
]
for row, summary in zip(web,summaries):row['summary']=summary
put('web-receipts.json',web)
phases={x:'PASS' for x in ['0','1','2','3','4a','4b','4c','4.6','5','5.5','6.0','6','7','8']}
phases['4.5']='N/A: theorem, all six infrastructure dimensions explained'
a=dict(declaration=target,file='Roth/HasseDeriv.lean',line=185,verdict='YES-add-as-is',category='YES-add-as-is',completed=True,root_acceptance='pending',production_edits=False,phases=phases,unresolved=[],baseline_hashes_matched=17,axioms=['propext','Classical.choice','Quot.sound'],composition='NOT-COMPOSABLE from existing pinned mathlib: new multivariate parent composition is not an existing mathlib building block.',generality='MAXIMALLY GENERAL for geometric support-separation corollary; scalar-cast-one criterion verified strictly weaker in characteristic2 and already subsumed by unrestricted parent law.',modern_idiom='Q8=yes diagnostic; supplied composition law plus factor1 is generic one_smul, not normalization of canonical family. No material public modernization established. Bundled and lattice equivalent shapes verified.',caller_scope='One explicit invocation at Separation156, Option.some/none support proof and reverse rewrite verified as a scoped fragment.',missing_api='Canonical multivariate Hasse composition for disjoint differential supports, grouped with parent iterativity.',upstream=dict(path='Mathlib/Algebra/MvPolynomial/HasseDeriv.lean',pr_title='feat(Algebra/MvPolynomial/HasseDeriv): add composition for disjoint differential orders',group_with=['MvPolynomial.hasseDeriv','MvPolynomial.coeff_hasseDeriv','MvPolynomial.hasseDeriv_map','MvPolynomial.hasseDeriv_rename','MvPolynomial.hasseDeriv_hasseDeriv'],reviewer_candidates=['Yaël Dillies','Moritz Firsching'],reviewer_receipt='reviewer-commits.json'),limitations=['Optional ask_chatgpt_math unavailable','Local symbol index unavailable; source fallback positive only','nLab XHTML400 and categorical direct path unavailable','External search revisions may differ from pinned mathlib','Caller scoped fragment, not full Separation rebuild','Rejected Loogle identifier/rate-limit and native extra attempt retained separately'])
v=dict(accepted=[],unresolved=[],rejected_receipts=['extra-rejected.json'],policy='Only complete native successes accepted. Final disk includes all current target checks; raw code imports only mathlib.')
for stem,purpose in [('raw','Independent raw construction, coefficient identity, choose cocycle, iterativity and disjoint-support law; absence guards and parent Semiring failure'),('final','Target type/axioms/replay, scalar and natural factor conditions, bundled/swapped/lattice shapes, scoped caller, Nat failure and ZMod2 overlap')]:
    receipt=stem+'-success.json';source=stem+'-executed.lean.txt'
    d=json.loads((p/receipt).read_text());sc=d['result']['structuredContent'];native=sc.get('result',sc);ds=native.get('items',native.get('diagnostics',[]))
    assert native['success'] and not native.get('partial',False) and not native.get('timed_out',False)
    assert not any(x.get('severity') in ['error','warning'] for x in ds)
    a.setdefault('diagnostics',{})[source]=dict(success=True,partial=False,timed_out=False,errors=0,warnings=0,elapsed_ms=d['elapsed_ms'])
    e=dict(source=source,receipt=receipt,purpose=purpose,source_sha256=sha(p/source),partial=False)
    if 'code' not in d['request']:e['source_check']='final-source-check.json'
    v['accepted'].append(e)
put('assessment.json',a);put('verification.json',v)
put('overview-entry.json',dict(name=target,type='∀ {σ R : Type*} [CommSemiring R] {d e : σ →₀ ℕ}, Disjoint d.support e.support → ∀ P : MvPolynomial σ R, hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P',what='Hasse derivatives in disjoint variable supports compose with no binomial scalar.',how='General iterativity then support-disjoint finite-product factors equal1.',hypotheses=a['generality'],project_dependencies=['MvPolynomial.hasseDeriv','MvPolynomial.hasseCoeff','MvPolynomial.hasseDeriv_hasseDeriv'],caller_summary=a['caller_scope'],mathlib_api_audit='All five actual methods on current/literature/abstract forms; univariate iteration is analogue only; lattice predicate equivalence verified.',moral_duplications='Support-separated corollary of new general composition; not a ≤3call composition from existing pinned mathlib.',generalization=a['generality'],missing_api=a['missing_api'],junk='No: reusable geometric API supporting separated-variable determinant proof.',action='YES-add-as-is with parent multivariate API; run generalise and cleanup, optionally bundle; retain geometric support interface.'))
files=[]
for f in sorted(p.iterdir()):
    if not f.is_file() or f.name in ['copy-manifest.json','validation-receipt.json','root-review.json']:continue
    dst='.mathlib-quality/overview/mathlibable/'+target+'.md' if f.name=='report.md' else '.mathlib-quality/overview/evidence/'+target+'/'+f.name
    files.append(dict(source=f.name,destination=dst,sha256=sha(f),bytes=len(f.read_bytes())))
put('copy-manifest.json',dict(files=files))
print('Complete package frozen:',len(files),'supporting artifacts')
