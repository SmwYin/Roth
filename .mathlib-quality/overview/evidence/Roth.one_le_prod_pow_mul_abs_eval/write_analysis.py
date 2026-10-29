from pathlib import Path
import json,hashlib,re
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.one_le_prod_pow_mul_abs_eval';V='YES-but-generalise-first'
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def link(f):return f'[{f}](../evidence/{N}/{f})'
nt=json.loads((D/'native-type.json').read_text());nt.update(type=nt['full_type'],original_project_dependencies=[],full_kernel_printer_body=False,elided_characters=[89281]);dump('native-type.json',nt)
forms=['current','standard','abstract'];methods=['leanfinder','loogle','leansearch','rg','local'];cells=[]
for f in forms:
 for m in methods:
  name=f'formal-{f}-{m}.json';a=json.loads((D/name).read_text());s=a.get('result',{}).get('structuredContent',{});cells.append(dict(form=f,method=m,receipt=name,query=a.get('request'),status=('index '+s.get('index','unknown')+'; not absence evidence')if m=='local'else'actual returned search',summary=('partial univariate denominator-clearing hit; no exact multivariate weighted product theorem found'if f!='abstract'else'integer separation and localization building blocks, no coordinatewise lower-bound theorem')))
dump('formal-search-matrix.json',dict(cells=cells,standard_retry='formal-standard-local-retry.json',conclusion='Partial match one_le_pow_mul_abs_eval_div; algebraic summand expansion and integer separation primitives. No <=3-existing-call proof established; local index limitations explicitly not absence. Remote indexes may differ from pin.'))
qs=[]
for i in [0,3,6]:qs.extend(json.loads((D/f'web-batch{i}.json').read_text())['request']['search_query'])
dump('literature.json',dict(general_queries=qs[:3],channels=[dict(channel=n,query=q['q'],receipt='web-batch'+str((i//3)*3)+'.json')for i,(n,q)in enumerate(zip(['web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'],qs))],optional_channel=dict(channel='ask_chatgpt_math',status='n/a: unavailable; optional channel omitted honestly'),local_channel=dict(channel='local',receipt='literature-local.json',locator='clean.tex §7 eq54, lines1646–1656'),third_party_bodies_persisted=False,primary='primary.json',summary='Exact local coordinatewise denominator clearing; broader literature calls the rational nonzero-value lower bound a Liouville estimate. Finite coordinate labels and ordered field realization do not supply extra arithmetic assumptions.'))
modern=[
('Typeclasses','yes','Replace fixed real realization by Field K, LinearOrder K, IsStrictOrderedRing K; verified generic01.','Same integer estimate applies over ℚ and other ordered fields.'),
('Filters/nets','no','Finite algebraic sum/product identity, no convergence.','No topology introduced.'),
('Universal property','partial','Localization universal property explains denominator inverses but does not produce coordinatewise r bound or integer separation.','clearing03 separates image membership from archimedean bound.'),
('Bundled substructure','partial','Image/range membership or ∃N equality can express clearing; no bespoke class required.','New clearing proof can be reused without order.'),
('Hierarchy weakening','yes','Real to linearly ordered field mechanically; field division and finite commutative products genuinely used.','Univariate existing ordered-field API gives the correct hierarchy target.'),
('Higher categories','no','No categorical coherence content.','None.'),
('Concrete index','yes','Fin m to arbitrary Fintype ι, including empty types.','No coordinate-renaming/equivalence transport required by callers.'),
('Concrete-via-abstract diagnostic','yes','Fin m occurs zero times in proof body; real annotations throughout serve only casts, field arithmetic and order. Integer coefficients remain semantic: Int.one_le_abs supplies discrete separation.','Generic field proof and explicit hsep norm proof compile; not mere identifier-count speculation.'),
('False-generalization guard','PASS','Signed denominators require absolute product; CharZero alone insufficient for norm separation; q=0 and missing hne/degree rejected by compiled counterexamples.','Exact original signature recovered, including Fin0.')]
strategy=[('Topology epsilon/delta','n/a','No topology'),('Point-free algebra','partial','Separate integer-image equality (clearing) from arithmetic lower bound; localization alone misses sharp exponent product.'),('Analysis sequences','n/a','No limits'),('Universal-property construction','n/a','Witness integer numerator is computational finite-sum identity, not a new object requiring category machinery.'),('Missing helpers','yes','Coordinatewise multivariate denominator-clearing equality is the concrete missing API; new clearing03 is own proof, not an existing theorem.')]
shape=[('Normal form','RESTATE','eval₂ Int.castRingHom avoids map+eval transport; algebraic ∃N identity plus lower-bound corollary. Product-times-absolute form directly matches caller trans_lt; reciprocal form equivalent with positive denominator product.'),('Syntactic generality','RESTATE','Use arbitrary Fintype variables and ordered target field. signed q!=0 with absolute product, plus positive-natural convenience wrapper. shape02 verifies eval₂ bridge.'),('Superfluous arguments','NONE mathematically; representation restrictions','Q,r,h,q determine actual polynomial and points. hQ,hq,hne each needed by counterexamples; no NeZero m, coprimality, algebraicity, irrationality, or positivity of r assumed. Fin/Real restrictions can be widened.')]
risks=[dict(risk=x,status='n/a',reason='Theorem; introduces no definitional equality, coercion or instance search path.')for x in ['Typeclass diamond','Reducibility leak','Non-canonical unfolding','Instance priority collision','Universe-polymorphism issues','Coercion ambiguity']]
dump('phase-checks.json',dict(modern9=modern,proofstrategy5=strategy,statement_shape3=shape,infrastructure_risks=risks,size=dict(verdict='SMALL',reason='Arithmetic helper; not a new structure, named theorem, or module main result.'),definition_one_line='n/a: theorem',generality='STRICTLY NARROWER; mechanical arbitrary Fintype and ordered-field proof verified',strategy_verdict='REFACTOR-RECOMMENDED: expose algebraic clearing equality, derive lower bound using integer separation',statement_shape_verdict='RESTATE-BEFORE-SHIP',composition='NOT-COMPOSABLE from <=3 existing calls'))
source=R/'.mathlib-quality/references/clean.tex';dump('literature-source.json',dict(path=str(source.relative_to(R)),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),bytes=source.stat().st_size))
dump('mathlib-inputs.json',[dict(path='.lake/packages/mathlib/'+p,archive=f'mathlib-source-{i}.lean.txt',sha256=hashlib.sha256((D/f'mathlib-source-{i}.lean.txt').read_bytes()).hexdigest())for i,p in enumerate(['Mathlib/Algebra/Polynomial/DenomsClearable.lean','Mathlib/RingTheory/MvPolynomial/Localization.lean','Mathlib/Algebra/MvPolynomial/Eval.lean'])])
body=json.loads((D/'target-metadata.json').read_text())['body'];dump('concrete-diagnostic.json',{'Fin m_body_lines':sum('Fin m'in l for l in body.splitlines()),'real_annotation_body_lines':sum('ℝ'in l for l in body.splitlines()),'integer_separation_body_lines':[l for l in body.splitlines()if'Int.one_le_abs'in l],'conclusion':'Real and Fin are representation constraints; integer separation is a semantic requirement. Mechanical generic ordered field proof independently verified; norm variant explicitly supplies hsep.'})
g=(D/'generic-body.lean.txt').read_text().split(':= by')[0].strip();signed=(D/'signed-body.lean.txt').read_text().split(':= by')[0].strip()
o=dict(declaration=N,kind='theorem',type=nt['full_type'],what='A nonzero integer multivariate polynomial value at rational coordinates has absolute value at least the reciprocal of the product of denominators raised to coordinate degree bounds.',how='Constructs the integer numerator N by summing cleared monomials; MvPolynomial.monomial_le_degreeOf bounds exponents and MvPolynomial.eval_eq\' identifies its cast with the scaled evaluation. Nonvanishing and Int.one_le_abs then give the lower bound.',hypotheses='Integer coefficients; coordinate degree bounds r; positive natural denominators; nonzero evaluation. No coprimality, algebraicity, irrationality, nonempty dimension or positive degree hypothesis.',project_dependencies=[],caller_summary='One explicit proof use, same file private one_lt_roth_eval_bound_aux at Main:476 (full453–478); zero external-file source calls. One direct canonical body consumer, no type consumers. Full original Main proof replay with literal inlining succeeds; LeanEval is a transitive consumer only.',mathlib_api_audit='Existing one_le_pow_mul_abs_eval_div and DenomsClearable are univariate; MvPolynomial.isLocalization localizes coefficient rings but does not supply coordinatewise denominator degree clearing or its separation estimate.',moral_duplications='Shares discrete integer separation with Theta coefficient estimates and univariate Liouville bound; not the same statement. Taylor upper bound is complementary, not duplicate.',generalization=dict(verified=True,reason=['LITERATURE-WEAKENING','MODERN-IDIOM'],proposed_type=signed,natural_wrapper_type=g,mechanical='Fin m -> arbitrary Fintype; ℝ -> ordered field; original body otherwise unchanged',extended='Signed integer denominators with absolute product; CharZero field algebraic clearing; norm target requires explicit integer separation bound',recovery='recovery01 exact original written signature, Fin0 edges01'),missing_api='Coordinatewise multivariate polynomial denominator-clearing equality at arbitrary rational points with individual degree bounds, and nonzero integer lower-bound corollary.',junk='KEEP: substantive clearing argument, used in the Roth contradiction. No dead-code or trivial existing-mathlib composition justification for deletion.',action='Generalize and split clearing equality from ordered-field estimate, retain natural-positive convenience theorem for current caller. Proposed new Mathlib/Algebra/MvPolynomial/DenomsClearable.lean; use eval₂ normal form; review independent algebraic PR before replacing project wrapper.')
dump('overview-entry.json',o)
phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']}
phases['8']='pending'
dump('assessment.json',dict(declaration=N,canonical_index=279,verdict=V,completed=False,allphases='pending',phases=phases,unresolved=[],root_acceptance='pending',parent_verdict_inherited=False,cost_based_verdict=False))
report=f'''# `{N}` — {V}

Canonical279, `Roth/Main.lean:324–344`. Fresh independent assessment; root acceptance pending.

## Phase0 — Baseline and scope

The unchanged 2467-job baseline build succeeded. All17 source/pin hashes freshly match the tracked shared manifest ({link('inputs.json')}, {link('baseline-build.txt')}). Full Main588lines and LeanEval66lines were read; all production Lean sources were freshly searched using no-ignore rg and git grep. No production, pins, Git, overview or progress were modified by this worker.

Root exclusively executed native and local LSP requests. Original proof replay uses exactly the target, renamed `Integer279Original.replay`, in a fresh namespace and no private helper closure. Its complete source and original/replay proposition type agreement are checked. The loaded original full type and direct kernel value/type constants were audited; the pp.all body printer explicitly elides89281characters, so this is not claimed as a complete printed kernel body. The complete written proof is archived. Canonical array came directly from tracked order, all293 unique names in exact order including correct private modules; runtime293present/293values. One direct body consumer, no direct type consumer. See {link('original-executed.lean.txt')}, {link('original-receipt.json')}, {link('canonical-consumers.json')}.

## Phase1 — Mathematics and full native type

For an integer polynomial Q in finitely many coordinates with each coordinate degree at most rⱼ, evaluate at integer numerator hⱼ divided by positive natural denominator qⱼ. If this value is nonzero, multiplying its absolute value by ∏qⱼ^rⱼ yields at least1. This is an exact denominator estimate; no reduced fractions or algebraicity assumptions enter.

```lean
{nt['full_type']}
```

The proof constructs N=Σ_d coeff(Q,d)·∏ⱼ hⱼ^dⱼ qⱼ^(rⱼ−dⱼ). For each support monomial, `monomial_le_degreeOf` and hQ justify dⱼ≤rⱼ; denominator cancellation identifies N's real cast with the product-scaled evaluation. Positivity makes the denominator product nonzero, hne makes N nonzero, and `Int.one_le_abs` supplies the discrete lower bound. This is neither integrality alone nor positivity alone. Project proof dependencies: `[]`; all ingredients are mathlib constants. {link('target-excerpt.lean.txt')}.

## Phase2 — Preliminary checks

SMALL: a finite arithmetic helper, no new structure or named theorem; module main-results list names Roth's theorems. Literature still exhaustive. Definition-only one-line check: n/a, theorem. Six infrastructure risks: n/a, theorem introduces no definition, instance, coercion, reducibility or unfolding path; each recorded in {link('phase-checks.json')}.

## Phase3 — Exhaustive literature

| Channel | Exact query / evidence | Result and relevance |
|---|---|---|
'''
for i,(n,q)in enumerate(zip(['Specific web','General web','Aliases web','nLab','nCatLab distinct namespace','Stacks','MathOverflow','Recent arXiv'],qs)):
 report+=f"| {n} | `{q['q']}`; {link('web-batch'+str((i//3)*3)+'.json')} | "+('Elementary Liouville/height and denominator-clearing context; not an exact formal-library replacement.'if i<3 else'Localization/height context or adjacent results; no exact coordinatewise theorem identified.')+' |\n'
report+=f'''| Local | `clean.tex` §7 eq54, lines1646–1656; {link('literature-local.json')}, {link('local-excerpt.tex.txt')} | Exact arithmetic step: coordinate degree bounds clear each denominator and yield a nonzero integer. |
| Optional math consultation | ask_chatgpt_math unavailable | justified n/a; no substitute channel invented. |

Primary external locator: Waldschmidt, *Linear independence of logarithms of algebraic numbers*, Introduction p.ii lines51–53 and Chapter3, identifies the elementary rational denominator lower bound as a Liouville estimate ([author's notes](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/LIL.pdf)). [Stacks10.9](https://stacks.math.columbia.edu/tag/00CM) supplies the localization universal property, which handles invertibility and fractions but not an archimedean separation constant. {link('primary.json')} records requests, responseSHA/bytes/status and concise original summaries. No article or search-result bodies persisted. Recent arXiv query used exactly the five-year window, including out-of-topic returns honestly. nCatLab was searched under `/ncatlab` distinctly; out-of-namespace results are not represented as exact nCatLab hits.

Standard mathematical content: clearing coordinate denominators followed by nonzero integer separation, a rational special case of Liouville estimates. Broader number-field/height versions need norm/product-formula machinery and are not mechanically the same theorem. Finite coordinate labels and a chosen ordered-field realization do not add arithmetic substance. These literature distinctions motivate the mechanical Fintype/ordered-field widening, not an unsupported claim that all normed fields have the integer bound.

## Phase4a–b — Every parameter and generality

| Parameter / hypothesis | Role and weakening result |
|---|---|
| m, Fin m | Finite coordinate labeling only. Arbitrary `Fintype ι` compiles with original proof; empty coordinates allowed. |
| Q over ℤ | Semantic integer separation, not merely convenient coefficients. Constant rational1/2 disproves unconditional rational coefficient extension. |
| r : coordinates→ℕ | Genuine reusable coordinate degree ceilings; no fixed Roth constants. They may be0. Dropping degree bounds fails on X² evaluated at1/2 with r=1. |
| h : coordinates→ℤ | Genuine numerator data; no sign or coprimality constraint. Arbitrary rational numerators would require additional denominator factors. |
| q natural, hq positive | Nonzero denominator is essential. Signed integers q≠0 compile with absolute product. q=0, Q=1,r=1 falsifies original conclusion. |
| hQ coordinate degree bound | Essential to nonnegative complement exponent r−d, validated by explicit counterexample when removed. |
| hne nonvanishing | Essential; Q=0 gives0 on the right. |
| real target | Only ordered-field cast/arithmetic/abs used; arbitrary linearly ordered field compiles mechanically. |
| no extra assumptions | No `NeZero m`, positivity of r, irrationality, algebraicity or coprimality needed or introduced. |

STRICTLY NARROWER THAN STANDARD; two mechanical widenings are actually verified in {link('generic01-receipt.json')}: replace Fin m by arbitrary Fintype and ℝ by arbitrary ordered field. No proof strategy change is needed for this primary weakening. Signed denominators also verify ({link('signed01-receipt.json')}):

```lean
{signed}
```

The natural-positive convenience form uses the original body over arbitrary Fintype and ordered field. Exact original signature recovery is a single application of our newly proved generic theorem, compiled mathlib-only ({link('recovery-executed.lean.txt')}, {link('recovery01-receipt.json')}). This is new generic proof evidence, not a replacement already in mathlib.

Algebraic clearing alone compiles over arbitrary characteristic-zero field with signed nonzero denominators, without order. A separate norm estimate compiles only with explicit `hsep : ∀ z : ℤ, z ≠ 0 → 1 ≤ ‖(z : K)‖` ({link('clearing3-executed.lean.txt')}, {link('clearing03-receipt.json')}). Characteristic zero alone does not imply hsep; p-adic fields provide the familiar obstruction (`Padic.norm_p_lt_one` in pinned PadicNumbers). No new separation typeclass is proposed. {link('edges-executed.lean.txt')} and {link('edges01-receipt.json')} verify zero-denominator, zero-value, missing-degree, rational-coefficient guards and exact Fin0 specialization.

## Phase4c — Modern idiom nine rows

| Question | Answer | Proposal / consequence |
|---|---|---|
'''
for q,a,b,c in modern:report+=f'| {q} | {a} | {b} {c} |\n'
report+=f'''
Concrete-via-abstract diagnostic is explicit: `Fin m` occurs0times in original body; real annotations persist as casts/order arithmetic, while `Int.one_le_abs` is indispensable ({link('concrete-diagnostic.json')}). Accepted mechanical proofs substantiate the abstraction. Real improvement: arbitrary finite coordinate types need no relabeling, ℚ and other ordered targets need no detour through ℝ, and the clearing equality can feed other separated norms if the required property is supplied. Exact original conclusion and empty dimension are retained.

## Phase4.6 — Proof strategy five rows

| Question | Answer | Assessment |
|---|---|---|
'''
for q,a,b in strategy:report+=f'| {q} | {a} | {b} |\n'
report+=f'''
REFACTOR-RECOMMENDED before upstreaming: expose coordinatewise clearing as a helper and derive the integer lower bound afterward. Explicit support expansion is a natural finite polynomial argument. Avoid presenting a new norm abstraction as necessary for the primary ordered-field result. The actual missing helper and its complete new proof are archived; no cost-based verdict.

## Phase5 — All15 formal search cells

| Form | Finder | Loogle | LeanSearch | Pinned rg | Root local search |
|---|---|---|---|---|---|
'''
for f in forms:report+='| '+f+' | '+' | '.join(link(f'formal-{f}-{m}.json')for m in methods)+' |\n'
report+=f'''
Remote semantic queries find `one_le_pow_mul_abs_eval_div`, `denomsClearable_of_natDegree_le`, `denomsClearable_natDegree`; abstract form also finds `Int.one_le_abs`. Loogle current/standard return empty, abstract returns separation primitive. Pinned sources and native signatures were independently verified, not inferred from external index revisions. Root local current/standard had indexerror and abstract warming; a relevant standard exact-candidate retry is retained ({link('formal-standard-local-retry.json')}). None of these index states proves absence. {link('formal-search-matrix.json')} records every query and receipt.

Concrete mathlib gap: `Mathlib/Algebra/Polynomial/DenomsClearable.lean:65–105` supplies only a univariate polynomial and one denominator with one natDegree; it cannot directly represent Q in independent coordinates with ∏qⱼ^rⱼ. `MvPolynomial.isLocalization` concerns localizing coefficient rings at a submonoid; it neither calculates the sharp coordinate denominator product nor supplies a unit lower bound for a nonzero integer. Evaluation expansion, support degree bounds and `Int.one_le_abs` are the existing primitives. Native candidate signatures: {link('composition03-receipt.json')}. Full pinned sources: {link('mathlib-source-0.lean.txt')}, {link('mathlib-source-1.lean.txt')}, {link('mathlib-source-2.lean.txt')}.

## Phase5.5 — Statement shape three rows

| Check | Verdict | Concrete result |
|---|---|---|
'''
for q,a,b in shape:report+=f'| {q} | {a} | {b} |\n'
report+=f'''
Overall RESTATE-BEFORE-SHIP. {link('shape2-executed.lean.txt')} and {link('shape02-receipt.json')} verify eval₂ normal form via eval_map. This bridge uses the new signed lemma and is not claimed as an existing arithmetic replacement. Product-times-absolute form fits the existing caller more directly than reciprocal or interval membership; signed absolute form preserves the mathematics. No superfluous proof premise was silently dropped.

## Phase6.0 — Full callers and duplication

| Actual caller | Use | Verification |
|---|---|---|
| private `Roth.one_lt_roth_eval_bound_aux`, Main453–478, call476 | Lower denominator bound chained by `.trans_lt` with the Taylor upper bound | Complete original body and signature retained; original target removed from fresh full Main replay and complete original proof literally inserted at call. |

One same-file call; zero external-to-file calls (the skill's count excluding declaring file is0). The module doc reference at38 and declaration at324 are not proof callers. Source lexical search and direct293 kernel consumer audit independently agree on the sole proof caller. No direct type consumers; no claim of a complete arbitrary simp/transitive closure. The target has no simp attribute. The downstream public chain reaches roth_of_isIntegral, roth, roth_rat and LeanEval.thueSiegelRoth; the latter is transitive, not an additional explicit target caller. {link('callers.json')}, {link('source-search.json')}, {link('tracked-source-search.json')}.

Entire original Main namespace body was replayed with original local declarations, except target deletion and literal caller proof insertion; orphan target docstring removed as scratch-only cleanup. Existing public Roth definitions remain imported for project ingredients. This full caller experiment is stronger than a chopped caller prefix but does not claim replacing all transitive project ingredients with mathlib. Full sources {link('source-Main.lean.txt')}, {link('source-LeanEval.lean.txt')}, accepted fullMain source {link('callers3-executed.lean.txt')}, raw {link('callers03-receipt.json')}.

| Pair compared | Same statement? | Same proof? | Action |
|---|---|---|---|
| Target / existing univariate one_le_pow_mul_abs_eval_div | No: independent rational coordinates and individual degree exponents vs one variable/denominator | Same final integer separation; new multivariate denominator identity required | Generalize multivariate API; retain univariate existing theorem. |
| Target / Theta leading-coefficient lower estimates | No: polynomial value vs nonzero coefficient | Shares `Int.one_le_abs` only | Do not unify different statements; share mathlib primitive. |
| Target / abs_eval_lt_of_le_index | No: lower arithmetic bound vs Taylor analytic upper bound | Different arguments | Complementary caller ingredients, not duplication. |
| Target / new generic and signed scratch forms | Original specializes exactly | Original proof transfers mechanically | Upstream generic primary and original convenience specialization. |

Inline-derivation search finds no independent reconstruction elsewhere; Theta lines215/482/488 concern leading coefficients. {link('inline-search.json')}. No junk/dead-code recommendation: the integer-clearing argument is substantive even though it has one explicit caller.

## Phase6 — Actual composition experiments

1. Direct application of existing `one_le_pow_mul_abs_eval_div` fails because it consumes `Polynomial ℤ`, one rational coordinate and natDegree, rather than multivariate map/eval with coordinate ceilings.
2. `Int.one_le_abs` alone fails because the target is a scaled real evaluation; a nonzero integer witness and cast equality must first be proved.
3. Closure with `simp only [eval_map]` fails: normalizing evaluation spelling does not prove integrality or discrete separation.

All three failures are required-closure `fail_if_success` probes in {link('composition3-executed.lean.txt')}; the theorem then closes with our newly proved generic lemma, whose source is fully present. The accepted receipt has no errors/warnings. This is NOT-COMPOSABLE from <=3 existing calls. An iterated univariate argument would have to clear earlier rational coefficients and track degree bounds, which is itself new algebra; a common-denominator/total-degree estimate generally loses the sharp product ∏qⱼ^rⱼ. No timed-out tactic or empty search is treated as an absence proof, and no generated generic helper is miscounted as an existing primitive.

## Phase7 — Actionable verdict

**YES-but-generalise-first**, reasons LITERATURE-WEAKENING and MODERN-IDIOM. Mathlib has the analogous univariate denominator-clearing theorem but lacks the coordinatewise multivariate clearing identity with individual degree bounds and its exact nonzero integer lower bound. This gap is concrete: support-degree complement exponents must be bounded and polynomial evaluation must be identified with a cast integer. It cannot be replaced by positivity, localization membership alone, or a <=3-call separation theorem. The complete original argument mechanically supports arbitrary finite coordinate types and ordered fields, with exact recovery and caller verification; these changes preserve the mathematical content and eliminate unnecessary coordinate/real representation constraints.

Proposed exact home: new `Mathlib/Algebra/MvPolynomial/DenomsClearable.lean`, adjacent to Eval/Degrees and parallel to the univariate DenomsClearable module. Avoid adding order/localization dependencies to foundational Eval merely to accommodate this result. Put algebraic clearing equality first, then ordered-field signed estimate and positive-natural corollary. Primary proof generalization is mechanical; splitting the helper is a concrete proof organization improvement, not a condition that changes the verdict.

Proposed PR title: **feat(Algebra/MvPolynomial): clear denominators of rational evaluations**. Ship this independent algebraic API first. Accepted related YES candidates `MvPolynomial.eval_eq_sum_box` and `Roth.abs_eval_le` (both YES-but-generalise-first, tracked progress PASS) concern evaluation APIs but belong to distinct Taylor/upper-bound work; group documentation/use examples if useful, not their unrelated proof development into the first clearing PR. `Roth.main_lemma` is already accepted YES-add-as-is but should remain a later Roth-specific PR. No old verdict was inherited.

Reviewer candidates based on actual relevant recent pinned commits: Elias Judin, `d1f304c611eb2e7507ea2393df3d155563609d8e` (2026-07-07, eval API parity #39865), and Yaël Dillies, `631b214f7c30ea1a438ddac7b63fbae0c595a874` (2026-09-02, MvPolynomial coeff refactor #41427). This selects potential reviewers from source history; it does not assert they reviewed these commits. Local git log is exact ({link('reviewer-commits.json')}); GitHub page fetches returned cache misses, recorded honestly ({link('reviewer-web.json')}).

Pre-PR actions: `/generalise {N}` (retain verified Fintype/ordered-field widening and signed variant); `/cleanup Roth/Main.lean {N}` and cleanup the new mathlib module; choose a relevant reviewer above; replace only Main476 with the new positive-natural theorem after adding the generic API. Keep the project wrapper until that API exists. A downstream fallback home is a project-local arithmetic lemma module; Archive is unnecessary for this reusable finite polynomial bound. Production sources were intentionally unchanged for this assessment.

## Phase8 — Evidence and limitations

Accepted exact executed sources, full raw requests/results, timings, prefix controls, standard axioms and full attempt accounting are in {link('verification.json')}. Failed/warning-bearing attempts are preserved separately and excluded from success evidence: clearing02 and shape01 recovered sorryAx after elaboration errors; composition02 had unreachable nested tactic warning; callers02 had orphan-docstring empty-line warning. composition01, callers01 and clearing01 were preparation-only and never executed, as documented in {link('preparation-only.json')}. No limit raises, new axioms, sorry, unsafe or native_decide in accepted proof sources. Stable18 mathlib-only imports and nine disk imports unchanged; no added imports. Original body printer elision is disclosed, local index limitations remain search limitations, and no new full literal build was due at frontier279 (next Main file boundary289; prior successful boundary228 and fresh matching baseline are reusable under root contract).

Portable current-manifest validation checks all17 inputs, exact canonical293 ordered names/private modules, source/request hashes, accepted raw diagnostics, standard axioms, complete original replay and full caller reconstruction, all15 searches, literature metadata, report links and both scratch/integrated layouts. Secret scan accompanies the frozen package. Assessment completed; unresolved[]; root independently accepts and integrates.
'''
(D/'report.md').write_text(report)
print('Wrote independent report/overview/phases/literature/formal matrix metadata')
