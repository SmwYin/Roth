from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.abs_coeff_diag_le'
def load(n):return json.loads((D/n).read_text())
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def link(n,label=None):return f'[{label or n}](../evidence/{N}/{n})'
modern=[('Typeclass hierarchy','Use CommSemiring R with an arbitrary subadditive f; AddGroupSeminorm R is an existing bundled specialization under CommRing R, verified.'),('Filters/topology','n/a: every sum is finite; no convergence premise.'),('Universal properties','aeval already bundles substitution. Total-degree fibers describe its action on the monomial basis; no new universal-property construction needed.'),('Bundled structures','Existing AddGroupSeminorm and SubadditiveHomClass/map_add_le_add avoid inventing a coefficient-size class. Bare f permits weaker semiring generality.'),('Module hierarchy','No vector space or scalar field is used. Codomain generalizes to ordered additive monoid N with Preorder/IsOrderedAddMonoid, cardinal expressed by nsmul, verified.'),('Higher categories','n/a: no higher coherence data appears.'),('Concrete indices','σ already arbitrary Type u; empty/infinite variable types work because P has finite support. n:ℕ is intrinsic to univariate polynomials.'),('Concrete-via-abstract','Fires: after diagonal monomial expansion, only finite-sum triangle/cardinality inequalities remain; coefficients need not be integers, nor size multiplicative. Fiber-sum and seminorm experiments compile and recover exact original.'),('False-generalization guard','Keep constant-X substitution and total-degree fiber; power-series diagonal extraction and arbitrary valuation are different operations. A fiber-card bound needs only fiber-local hB and no B≥0. Widening fiber.card to support.card uses B≥0, supplied by original global hB 0; do not silently discard this premise.')]
strategy=[('Topology ε–δ versus filters','n/a: finite algebraic estimate.'),('Element versus subobject argument','No ideal/submodule inclusion is involved. Coefficient fiber rewrite followed by subadditivity is appropriate.'),('Sequences versus nets','n/a: no asymptotic or topological statement.'),('Construction versus universal property','Current aeval already is the canonical substitution; a fresh homomorphism construction would duplicate infrastructure.'),('Missing helpers','A named coefficient-fiber identity would expose the reusable bridge. Once it is proved, sum and cardinal bounds use existing Finset APIs. Whether to upstream bridge alone or estimate too is a concrete design question.')]
infra=[(x,'n/a: theorem; introduces no data, instance, reducibility rule or coercion path.') for x in ['Typeclass diamond','Reducibility leak','Noncanonical unfolding','Instance priority collision','Universe-polymorphism issue','Coercion ambiguity']]
out('generality.json',dict(parameter_rows=[dict(parameter='σ : Type u',analysis='Already arbitrary; no finite/nonempty/decidable hypothesis.'),dict(parameter='P : MvPolynomial σ ℤ',analysis='Essential; fixed diag parent accepts integers. Expanded aeval representation supports CommSemiring R.'),dict(parameter='B : ℝ',analysis='Arbitrary real bound; global hB entails nonnegative. Expanded codomain N uses nsmul.'),dict(parameter='hB : ∀ d, |(coeff d : ℝ)| ≤ B',analysis='Essential size control; generic fiber variant requires only the degree-n support fiber. Original bound recovered with B≥0 from hB0.'),dict(parameter='n : ℕ',analysis='Essential coefficient index; no range or degree assumption needed.')],expanded_forms=[dict(name=n,verified=True,status='PASS',source='native-consumers-executed.lean.txt',receipt='native-consumers-success.json') for n in ['CommSemiring coefficient-fiber equality','Subadditive coefficient size map to ℝ','AddGroupSeminorm over CommRing','Preordered additive monoid codomain N','Fiber-local hB and fiber cardinality','Exact integer original recovery and full caller']],modern_rows=[dict(question=q,analysis=a)for q,a in modern],strategy_rows=[dict(question=q,analysis=a)for q,a in strategy],infrastructure_rows=[dict(risk=q,analysis=a)for q,a in infra],verdict='Expanded representation strictly more general and eligible for YES-but-generalise-first; fixed-parent representation alone is not disqualifying. BORDERLINE follows from trivial-simp normalization/composition and concrete upstream API packaging choice, not a missing droppable typeclass or representation cost.'))
phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; six infrastructure rows documented'
out('assessment.json',dict(declaration=N,canonical_index=92,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,reason='Upstream API choice: coefficient fiber identity versus generic subadditive/fiber estimate versus integer application wrapper; exact expanded forms and caller verified, no <=3 existing-call replacement established.'))
t=load('native-type.json')['type']
out('overview-entry.json',dict(declaration=N,kind='theorem',type=t,what='Each coefficient after identifying all variables is bounded by input support cardinality times a uniform input coefficient bound.',how='Expand diagonal polynomial into monomials; coefficient linearity and integer cast give finite sum; triangle inequality and sum≤card·B finish, treating off-degree terms as zero.',hypotheses='Arbitrary σ, integer polynomial P, real B with every input coefficient bounded in cast absolute value, arbitrary output index n; hB implies B≥0.',project_dependencies=['Roth.diag','Roth.diag_eq_sum'],caller_summary='One explicit external-to-file private caller Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux at MainLemma.lean:509; exact canonical293 direct proof audit agrees and full caller replay passes.',mathlib_api_audit='Finset.abs_sum_le_sum_abs, Finset.le_sum_of_subadditive, Finset.sum_le_card_nsmul plus polynomial coefficient/evaluation normalization are existing blocks, not an established direct diagonal estimate. New assessment helpers are not mathlib replacements.',moral_duplications='A finite-fiber pushforward triangle bound; abstract Finset inequalities exist but the polynomial substitution-to-fiber bridge is real normalization, not definitional equality.',generalization='Verified CommSemiring coefficients, arbitrary subadditive size map and ordered additive monoid codomain; CommRing AddGroupSeminorm specialization. Stronger support-fiber sum/cardinality and fiber-local hypothesis recover original.',missing_api='Optional coefficient formula for constant-X substitution, followed by a design choice about exposing a generic estimate. No missing finite-sum inequality infrastructure.',junk='Used by sole remainder coefficient estimate in Roth main lemma; not dead. No rewrite attribute or instance side effects.',action='BORDERLINE: decide upstream coefficient-fiber API and estimate scope. Keep local theorem until that choice; exact replay demonstrates migration if generic API is selected.'))
web=[]
for i in range(7):
 w=load(f'web-{i}.json')
 for q in w['request'].get('search_query',[]):web.append('| '+w['channel']+' | `'+q['q']+'` | '+w['summary']+' '+link(f'web-{i}.json','receipt')+' |')
formal=[]
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 fs=[]
 for form in ['current','standard','abstract']:
  x=load(method+'-'+form+'.json');r=x['response'].get('structuredContent',{});ns=[z.get('name',z.get('formal_name','')) for z in r.get('items',[])];fs.append(form+': '+(', '.join(ns[:3])or 'no items')+(' (index unavailable)'if r.get('index')=='unavailable'else '')+' '+link(method+'-'+form+'.json','raw'))
 formal.append('| '+method+' | '+'; '.join(fs)+' |')
r=f'''# `{N}` — declaration 92/293

**BORDERLINE-needs-human.** The useful general content is a coefficient sum over a total-degree fiber, followed by existing finite-sum inequalities. Whether mathlib should expose that bridge alone or a generic size estimate is an upstream API decision. The integer-only fixed-parent wrapper is not the proposed upstream interface. All verification is complete, unresolved[]; root acceptance pending. Production, pins and progress remain unchanged.

## Phase 0 — baseline

Fresh hashes of all17 sources/pins match the shared successful `lake build` baseline (2467 jobs, exit0). The theorem resolves at `Roth/CoeffNorm.lean:174`, has no placeholders, and its full native proof/axioms were obtained. Module purpose: coefficient l1 and sup bounds for integer multivariate polynomials, derivatives, diagonal substitution and evaluation. Read the full declaring module and the full sole caller module. {link('inputs.json')} {link('input-hash-check.json')} {link('baseline-build.txt')} {link('source-module.lean.txt')} {link('source-callers.lean.txt')}

## Phase 1 — comprehend

Let P have integer coefficients of absolute value at most B. Replacing every variable by x groups monomials by total degree. Each output coefficient is the sum of coefficients in one such group, so its absolute value is at most the number of input monomials times B. Cancellation is permitted; the bound deliberately uses the whole support instead of the smaller degree fiber.

Full elaborated native type:

```lean
{t}
```

σ is an arbitrary variable type; P and coefficient index n are essential; B is a real upper bound and hB is its global coefficient certificate. No finiteness, nonzero, degree or characteristic hypothesis is needed. The proof rewrites by project `diag_eq_sum`, takes coefficients and casts through a finite sum, then applies `Finset.abs_sum_le_sum_abs` and `Finset.sum_le_card_nsmul`. `Polynomial.coeff_monomial` gives either the original coefficient or0. In the latter case the global hB entails B≥0. {link('native-type.json')} {link('native-original-executed.lean.txt')} {link('native-original-success.json')}

## Phase 2 — preliminary classification

BIG under the command's literal rule: the module docstring lists this theorem among its main results. Mathematically it is an elementary coefficient estimate used inside Lemma9. One-line definition-only test: n/a, theorem. No verdict is inferred from proof length.

## Phase 3 — exhaustive literature

All named channels checked, with three distinct actual general-web queries (specific diagonal estimate, multivariate coefficient l1 form, abstract subadditive fiber form). `ask_chatgpt_math` unavailable: optional channel n/a, including historical-formulation consultation. Local clean.tex §6 line1449 states exactly the number-of-terms times coefficient-bound estimate; lines1443–1467 place it between the Hasse and monic remainder bounds. {link('local-literature.txt')} {link('local-literature-source.json')}

| Channel | Exact query | Result / relevance |
|---|---|---|
'''+ '\n'.join(web)+f'''

Primary locators: [nLab polynomial](https://ncatlab.org/nlab/show/polynomial) search explains polynomial rings as free commutative algebras and homogeneous degree fibers (direct open failed unsupported XHTML); [Stacks07XB](https://stacks.math.columbia.edu/tag/07XB), proof line36, uses the polynomial universal property but does not state this estimate; [MathOverflow426978](https://mathoverflow.net/questions/426978/comparing-the-truncated-ell1-norm-of-polynomial-coefficients-with-the-supr), lines32–40, supplies coefficient-l1 terminology while studying a different supremum comparison; [Wang–Su–Wang–Zhang2403.12716](https://arxiv.org/abs/2403.12716), submitted19March2024, abstract lines16–20 studies reversible Kronecker reductions, not identifying all variables. Direct access receipts/status: {link('web-6.json')}.

Standard concept: triangle inequality for coefficients collected under polynomial specialization, or finite-fiber pushforward. In arithmetic the size is absolute value and height; abstractly subadditivity suffices, with no multiplicativity or topology. Literature confirms the integer statement in its application and broader ring/seminorm language, not a single universally named diagonal-coefficient theorem. Exclude power-series diagonal extraction (equal multiindices), diagonal forms, integral L1 norms and reversible Kronecker substitutions as exact matches. No absence claim follows from unsuccessful searches. Web evidence stores exact requests, response digest/bytes/status, locators and original summaries, never article/search bodies; returned URL queries omitted.

## Phase 4a — every parameter / hypothesis

| Parameter | Essential / weakening analysis |
|---|---|
| σ : Type u | Already arbitrary; finite support makes finite/nonempty variable assumptions unnecessary. |
| P : MvPolynomial σ ℤ | Essential. ℤ is fixed by parent diag, so replacing it requires an expanded aeval representation; it is not a named typeclass premise on this theorem. |
| B : ℝ | Arbitrary real upper bound. Generic ordered-additive codomain formulation is verified with nsmul. |
| hB | Essential coefficient control. Stronger fiber result needs only coefficients actually contributing to degree n. Exact original implies B≥0 from hB0. |
| n : ℕ | Essential output coefficient index; no extra degree/range restriction needed. |

## Phase 4b — mechanically verified generality

The expanded representation is STRICTLY MORE GENERAL. Under `[CommSemiring R]`, the output coefficient equals
`∑ k ∈ P.support.filter (fun k ↦ k.degree = n), P.coeff k`.
For any f:R→N with f0≤0 and f(a+b)≤f a+f b, where N is an additive commutative monoid with Preorder and IsOrderedAddMonoid, applying f is bounded by the sum of f of input coefficients over that fiber. A fiber-local bound B then gives fiber.card • B. No nonnegativity of B or of f is needed for this fiber estimate. Exact compiled signatures/proofs: {link('native-consumers-executed.lean.txt')}; isolated mathlib-only version with original target/diag absent: {link('native-raw-executed.lean.txt')} {link('native-raw-success.json')}.

The additive seminorm specialization over arbitrary CommRing R is separately compiled using `map_add_le_add f`, not a guessed nonexistent f.add_le field. Exact integer recovery chooses f(z)=|(z:ℝ)|, uses Int.cast_add/abs_add_le, and widens fiber.card≤support.card using B≥0 from hB0. The complete sole consumer is replayed through this new specialization. These experiments are real proofs, **not existing mathlib calls**. The generalizations preserve the original on specialization; no strongest-possible claim about all hierarchy axes is made. {link('generality.json')} {link('native-consumers-success.json')}

The fixed parent diag remains integer-valued, so these verified generalizations use an expanded aeval representation rather than dropping a named target typeclass. That representation change alone does not rule out YES-but-generalise-first: an expanded form can be the right upstream contribution. Here BORDERLINE follows from the trivial-simp normalization/composition signal and the concrete choice of coefficient-fiber versus size-estimate API, not the absence of a droppable typeclass or the cost of changing representation.

## Phase 4c — nine modern-idiom rows

| Question | Assessment / downstream consequence |
|---|---|
'''+ '\n'.join('| '+q+' | '+a+' |'for q,a in modern)+f'''

Concrete improvements: the verified CommSemiring formula handles ℕ and finite-characteristic coefficients; AddGroupSeminorm handles sizes on arbitrary commutative rings without a multiplicative norm; fiber sums retain sharper information than support.card·B and compose directly with existing subadditivity APIs. The original local remainder estimate still follows exactly. No topology, module norm or higher category is required.

## Phase 4.5 — infrastructure risk

'''+ '\n'.join('- '+q+': '+a for q,a in infra)+f'''

Overall n/a: theorem. Using an existing bundled seminorm in an experimental theorem creates no new instance.

## Phase 4.6 — five proof-strategy rows

| Question | Assessment |
|---|---|
'''+ '\n'.join('| '+q+' | '+a+' |'for q,a in strategy)+f'''

Current strategy: MATHLIB-IDIOMATIC finite-support coefficient argument. A reusable coefficient-fiber equality is an optional API improvement and cleaner route to sharp estimates; all sum inequalities already exist. This is a packaging issue, not a reason to rebuild polynomial evaluation.

## Phase 5 — five actual methods on three forms

| Method | Requests and results |
|---|---|
'''+ '\n'.join(formal)+f'''
| rg | Current coefficient/substitution form {link('rg-current.json')}; literature sum/absolute/cardinality form {link('rg-literature.json')}; abstract subadditivity/pushforward form {link('rg-abstract.json')}; full exact name {link('rg-full-name.json')}. |

Initial Loogle calls were rate-limited; rejected search receipts preserved and retried after the rate window. All final12 searches returned successfully. Local index reports unavailable; source hits remain useful but an empty local result is not absence evidence. External revisions can differ (e.g. PartialOrder versus pinned Preorder); pinned signatures and successful uses are controlling.

| Existing candidate | Pinned source / disposition |
|---|---|
| Finset.abs_sum_le_sum_abs | Mathlib/Algebra/Order/BigOperators/Group/Finset.lean; triangle inequality, used in original. |
| Finset.le_sum_of_subadditive | Same module; generic subadditivity, actual pinned Preorder signature and proof compiled. |
| Finset.sum_le_card_nsmul | Same module; cardinality bound with Preorder/AddLeftMono, compiled. |
| Polynomial.finsetSum_coeff, coeff_monomial | Mathlib/Algebra/Polynomial/Coeff.lean and Basic.lean; coefficient expansion/selection. |
| MvPolynomial.eval₂_eq | Mathlib/Algebra/MvPolynomial/Eval.lean; support expansion requires product-power/monomial normalization, not an existing coefficient bound. |
| map_add_le_add | Existing SubadditiveHomClass method, instantiated for AddGroupSeminorm; actual signature checked. |
| Gauss norm/Chebyshev/power-series hits | Different hypotheses or operations: supremum of coefficients, bounds from value/root estimates, or infinite substitution. No direct replacement established. |

{link('mathlib-inputs.json')} records pinned source hashes/archives. Search conclusion: existing finite-sum building blocks and evaluation bridge ingredients found; no verified exact <=1-call diagonal estimate. This is not a proof of absence. The newly proved diagonal helpers, project normOne lemmas and earlier assessment snippets are excluded from existing-call counts.

## Phase 5.5 — three statement-shape checks

Normal form: original cardinal product bound is useful for its single caller. Generic upstream candidate should use `aeval (fun _ ↦ Polynomial.X)` with coefficient-fiber sum on RHS, then a size-sum or nsmul bound. Scalar `fiber.card • B` specializes to `(fiber.card:ℝ)*B`; coefficient-fiber equality is oriented toward its finite-sum RHS. Do not create a new integer-only diag definition upstream.

Syntactic generality: actually tried the source-style coefficient-monomial expansion (original), fiber-sum identity, generic subadditive and cardinal fiber forms, bundled seminorm form, preordered codomain form and exact old-interface recovery. All accepted forms compile. Keeping both sum and cardinal conclusions separate lets users supply nonuniform input bounds without reverting to a uniform B.

Superfluous argument audit: σ,P,n,B,hB all serve statement roles; no explicit class premise exists to drop. Global hB is stronger than needed in expanded fiber form, but replacing it without changing the conclusion requires respecting sign in support-card enlargement. No proposed finite/nonzero assumption. Overall RESTATE-BEFORE-SHIP if upstream, with API choice unresolved as design, not verification.

## Phase 6.0 — callers and inline audit

Internal uses excluding declaring file:1; external-to-file distinct files:1; explicit semantic occurrence:1. Docstring and declaration occurrences are not callers.

| Caller | Use | Actual migration experiment |
|---|---|---|
| private Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux, Roth/MainLemma.lean:509 | Bounds diagonal Hasse coefficients before norm_coeff_modByMonic_le; combines target with box support-card bound. | Replaced target by exact integer recovery from new generic fiber estimate; replayed full caller with same statement and all remaining source proof steps, clean. |

Inline search finds other triangle/cardinality inequalities but no extra independent derivation of this same diagonal estimate; the floor/remainder consumers use the named private caller. {link('rg-callers.json')} {link('rg-inline.json')} {link('callers.json')}.

Fresh canonical array generated directly from tracked JSON preserves exact order and private Lean names. Native runtime:293 entries,293 unique,293 present,293 values. Exactly one direct proof consumer, `_private.Roth.MainLemma.0.Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`. This is source/canonical direct-constant evidence, not opaque kernel/simp dependency closure. {link('canonical-audit-array.lean.txt')} {link('canonical-order.json')} {link('native-consumers-executed.lean.txt')} {link('native-consumers-success.json')}

## Phase 6 — composition experiments

Attempt1: source proof from diagonal monomial expansion. Exact original elaborates and uses two principal inequality calls, but first rewrites through the project diag_eq_sum, coefficient sum, integer cast and nsmul bridge, then proves a conditional monomial bound. Project diag_eq_sum does not count as a mathlib block; unfolding it adds eval₂/product-power/monomial normalization. Thus this is not a verified <=3 existing-call term.

Attempt2: mathlib-only polynomial expansion → new coefficient-fiber equality → existing Finset.le_sum_of_subadditive → existing Finset.sum_le_card_nsmul. This fully compiles; beyond existing primitives it includes the new coefficient-fiber normalization. The final generic cardinal theorem uses only a short chain **after** the new helper is available; counting that helper as existing would be circular evidence. Exact original recovery and caller replay compile but require the positivity/cardinality comparison too. Accepted isolated evidence guards missing Roth.diag and target and imports no Roth. {link('verification.json')}

Composition conclusion: no <=3 existing-call term established for the old statement. The finite-sum part itself is composable; the normalization bridge is a genuine small proof. Phase6b's trivial simp composition signal applies to the bridge, while upstream usefulness hinges on which reusable bridge/estimate should be public. This supports BORDERLINE API design, not automatic NO-composable and not a novelty claim based on search failure. Parent diag was NO-composable and prior expansion BORDERLINE; the NO-has-it parent re-aim gate does not automatically apply, and this theorem is not literal rfl glue.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, because the stronger, verified contribution has multiple sensible API boundaries and the old integer interface belongs to the arithmetic application. This is independent of cost and of prior verdicts. Literature supplies the application; mathlib supplies inequalities; the experiments identify a sharper coefficient-fiber bridge that would enable more generic norms and nonuniform bounds.

1. Should mathlib expose a named coefficient-fiber formula for constant-X evaluation, and derive bounds at call sites?
2. Should it additionally expose the generic subadditive fiber-sum bound (ordered additive codomain), a bundled AddGroupSeminorm corollary, or both?
3. Should the coarse integer support.card·B specialization remain a project-local helper in Roth/CoeffNorm.lean while the reusable bridge is discussed upstream?

If upstream is chosen, consider the coefficient identity near `Mathlib/Algebra/MvPolynomial/Eval.lean` with polynomial-coefficient imports reviewed; put norm-specific corollaries in an appropriately importing estimates module. If declined, keep this helper in Roth/CoeffNorm.lean or inline its original expansion/triangle proof into the sole named MainLemma caller. The full replay provides a migration plan but uses newly proved helpers; it does not justify deletion in favor of a nonexistent existing mathlib theorem. Accepted YES declarations were freshly read from progress, recorded in {link('accepted-yes-grouping.json')}; PR title/grouping/reviewer selection is n/a for this BORDERLINE assessment. These are future design questions, not blockers to completing the read-only assessment.

## Phase 8 — verification and handoff

Accepted original type/proof/axioms, isolated mathlib-only generic proof, and native combined generic/seminorm/integer/caller/codomain/canonical-audit receipts all completed successfully, no errors/warnings, standard axioms only. Disk receipts explicitly partial=false; completed virtual receipt has no partial flag and success=true. Initial seminorm attempt used nonexistent f.add_le and recovered sorryAx; preserved separately as rejected and never counted. A root line-length preflight prevented an initial append; an unchanged-file diagnostic from that incident is excluded because it did not execute the consumer. Accepted actual source is wrapped<=100. {link('verification.json')}

{link('validate.py')} is portable and read-only, checks current copy-manifest (historical worker manifest never substitutes), exact executed source hashes,17 inputs and pinned mathlib source hashes, success/nonpartial/noerror/standard axioms, fresh ordered private-name canonical293 array, all phases/searches/links and secret guard. Root independent acceptance is pending. No production edits are part of this package.
'''
(D/'report.md').write_text(r)
