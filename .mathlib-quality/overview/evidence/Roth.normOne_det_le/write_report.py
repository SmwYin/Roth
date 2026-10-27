from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.normOne_det_le'
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
modern=[
('Bundled/typeclass structure','yes','Use existing RingSeminorm R with explicit p 1 ≤ 1, not a new global norm instance; applies to multiple seminorms on same ring.'),
('Filters/topology','no','Finite sum/product estimate needs no convergence or topology.'),
('Universal property','no','Bounds an existing determinant; does not construct a universal object.'),
('Bundled substructures','no','No set-with-closure predicate appears.'),
('Algebraic hierarchy','yes','Replace MvPolynomial σ ℤ by arbitrary CommRing R; no domain, field, nontriviality or completeness required.'),
('Higher categories','no','Numerical finite determinant bound has no categorical enrichment to preserve.'),
('Concrete index','yes','Replace Fin l by arbitrary Fintype n with DecidableEq; factorial and exponent use card n.'),
('Concrete-via-abstract','yes','After det_apply the proof has zero MvPolynomial mentions. Every normOne occurrence is the size map or its abstract law witness. GenericDet and RingSeminorm specialization compile.'),
('False generalization guard','PASS','RingSeminorm is submultiplicative, not multiplicative AbsoluteValue. (X+1)(X-1)=X²-1 has length2 while factors have length2 each. Sup/Gauss norm, spectral determinant and field norm are different objects. Keep unit bound for empty index and unrestricted C.')]
strategy=[('epsilon-delta','no','No topology.'),('point-free subobjects','no','Entry estimates and real order do not encode ideal inclusions.'),('sequences to filters','no','Finite determinant.'),('universal construction','no','Determinant already defined.'),('missing helper','yes','General RingSeminorm determinant factorial bound is the contribution; reuse Finset generic sum/product induction and Matrix.det_apply rather than another coefficient-specific bound.')]
infra=[('typeclass diamond','n/a: theorem','No global instance introduced; local evidence bundles existing laws in RingSeminorm.'),('reducibility leak','n/a: theorem','Proof does not define a production reducible alias.'),('noncanonical unfolding','n/a: theorem','Proposed theorem states p M.det, with ordinary bundled-function application.'),('instance priority','n/a: theorem','No instance declaration or priority.'),('universes','n/a: theorem','Generic probes quantify R and n independently in Type*.'),('coercions','n/a: theorem','Uses existing RingSeminorm FunLike coercion; no new coercion.')]
params=[('σ : Type*','already arbitrary','No Fintype or DecidableEq on polynomial variables.'),('l : ℕ / Fin l','generalize','Arbitrary finite n; verified generalIndex and genericDet.'),('MvPolynomial σ ℤ','generalize','Arbitrary commutative ring R with real RingSeminorm p; exact specialization packaged and compiled.'),('C : ℝ','retain','No nonnegativity hypothesis needed: empty case C^0=1; nonempty entry bounds supply nonnegative upper values as required.'),('M square matrix','retain','Matrix.det needs square finite index and commutative ring; dropping commutativity/subtraction not supported by this determinant API.'),('hM all entries','retain','Needed uniform entry estimate; no premise unused. Removing yields false bound already for1x1.')]
out('generality.json',dict(verdict='STRICTLY NARROWER THAN STANDARD',reason='MODERN-IDIOM',parameter_rows=params,modern_rows=modern,strategy_rows=strategy,infrastructure_rows=infra,expanded_forms=[dict(name='arbitrary finite index',verified=True,status='PASS',native='consumers/generalIndex'),dict(name='arbitrary CommRing and size axioms',verified=True,status='PASS',native='raw/genericDet'),dict(name='existing RingSeminorm and polynomial specialization',verified=True,status='PASS',native='bundled and package')],modern_verdict='Existing RingSeminorm determinant theorem independently useful; no foundational normOne change required.',strategy_verdict='REFACTOR-RECOMMENDED',shape=dict(normal='RingSeminorm application and card factorial scalar multiplication',syntactic='general finite n and uniform hM',superfluous='none; preserve unit bound and empty case',overall='RESTATE-BEFORE-SHIP')))
out('callers.json',dict(named_count=1,occurrence_count=1,external_to_declaring_file=0,callers=[dict(name='Roth.abs_coeff_det_hasseDeriv_le',file='Roth/CoeffNorm.lean',lines=[268],replacement='Retain normOne_det_le as local corollary of general RingSeminorm theorem, or use the compiled generalIndex bound; full coefficient determinant caller replay preserves the final ring normalization.')],inline_audit='No independent coefficient-L1 determinant factorial proof. CoeffNorm.degreeOf_det_hasseDeriv_le uses Leibniz expansion for degrees; Theta.sum_max_sub_le_index_det uses index valuations; Wronskian.coeff_wronskian_of_natDegree_injective computes an exact coefficient. These are different estimates.',native_audit=dict(requested=293,unique=293,present=293,values=293,direct_consumers=['Roth.abs_coeff_det_hasseDeriv_le'],status='PASS')))
link=lambda f:f'[{f}](../evidence/{N}/{f})'
s='''# Roth.normOne_det_le — full mathlibable assessment

Canonical **88/293**, `Roth/CoeffNorm.lean:119–128`. **YES-but-generalise-first**, reason **MODERN-IDIOM**. The primary contribution is a determinant bound for an existing `RingSeminorm`, over any commutative ring and finite index type. The polynomial result becomes a local specialization. This assessment changes no production source or pin.

## Phase 0 — baseline

The shared baseline build succeeded (2467 jobs); all17 current source/pin hashes freshly match its manifest. Target resolution, full native type, proof and standard axioms were checked. The entire CoeffNorm module and its complete sole named caller were read. No prefilter or parent-verdict inheritance applies: this is a substantive determinant inequality.

Evidence: LINKS0.

## Phase 1 — mathematics and native type

```lean
∀ {σ : Type u_1} {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ},
  (∀ μ ν, Roth.normOne (M μ ν) ≤ C) → Roth.normOne M.det ≤ ↑l.factorial * C ^ l
```

The coefficient L1 size of a determinant is bounded by the number of permutations times the uniform bound for each product of entries. Expand the determinant as a sum indexed by permutations; apply the coefficient triangle inequality; each sign is ±1 and does not change size; apply submultiplicativity to the l factors and compare their nonnegative sizes with C. Finally there are l! permutations. Empty matrices are allowed: determinant1 and C^0=1, including negative C. For positive dimension the entry hypothesis provides needed nonnegative bounds. No global C≥0 or nonempty condition is introduced.

Project dependencies used by the current proof are normOne, normOne_sum_le, normOne_neg, normOne_prod_le and normOne_nonneg. The generic proof replaces all of them with existing RingSeminorm laws and existing Finset induction. Native source and receipts: LINKSNATIVE.

## Phase 2 — preliminary checks

**BIG**: normOne_det_le is explicitly a Main result in the module docstring and supplies the determinant estimate in Lemma3. Definition-only one-line/exemption check: **n/a: theorem**. Its proof has multiple substantive steps. The full literature protocol still runs.

## Phase 3 — exhaustive literature

Exact requests, returned-response SHA256/bytes/status, source locators and concise original summaries are archived. No full returned article/search body is persisted; returned URL query parameters are removed. Failed opens are recorded honestly.

| Channel | Actual request | Finding |
|---|---|---|
| General specific | polynomial coefficient l1 norm determinant factorial bound length | Polynomial L1 is called length; determinant coefficient estimate agrees with local Lemma3. web-0 |
| General broad | determinant bound n factorial Banach algebra submultiplicative norm | Normed/Banach algebra context; spectral Banach determinants are distinct. web-0 |
| General aliases | Leibniz determinant formula ring seminorm entry bound factorial | Signed permutation formula and n! products explain the estimate. web-0 |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Optional configured channel absent. |
| Local references | clean.tex Lemma3 proof lines437–497 | Exact coefficient L1 determinant factorial estimate and triangle/submultiplicativity. |
| nLab | site:ncatlab.org/nlab determinant Banach algebra norm | Indexed determinant/normed algebra/Banach ring context. web-1 |
| nCatLab | site:ncatlab.org/ncatlab determinant seminorm | Returns nLab determinant/norm pages; no distinct nCatLab theorem. web-2 |
| Stacks | site:stacks.math.columbia.edu determinant Leibniz formula commutative ring | Tags0FJ9 and related determinant construction over rings, not a seminorm inequality. web-3 |
| MathOverflow | site:mathoverflow.net determinant Banach algebra norm bound | Scalar upper estimates and trivial determinant estimates; block and spectral variants distinct. web-4 |
| Recent arXiv | site:arxiv.org determinant Banach algebra bound after:2021-10-27 before:2026-10-28 | 2026 Hankel determinant bounds and unrelated results; no exact general bound identified. web-5 |
| Supplementary primary opens | Stacks0FJ9;2015 Studia Mathematica article abstract;arXiv2608.07563;nLab Banach ring | First three opened; nLab failed400 unsupported application/xhtml+xml. web-6 |

Evidence: LINKSWEB; LINKSLIT.

The concept is the elementary Leibniz factorial determinant estimate under a submultiplicative coefficient length or ring seminorm. The local paper states the concrete polynomial form. The abstract ring-seminorm version is a mathematical inference from the same finite proof, verified in Lean; the searches are not claimed to locate a published theorem with precisely the proposed bundled signature. No completeness, field, or analytic determinant is involved. Stacks exterior-power determinants, spectral Banach determinants, and extremal Hankel bounds do not supply replacements.

## Phase 4a — every parameter and generality dimension

| Parameter | Current restriction | Result |
|---|---|---|
| σ | arbitrary Type* | Already unrestricted; no finite/decidable variable requirement. |
| l / Fin l | natural-sized matrix | Verified arbitrary Fintype n with card n factorial/exponent. |
| Entries | MvPolynomial σ ℤ | Verified arbitrary CommRing R and existing RingSeminorm R. This removes the concrete polynomial coefficient restriction in the theorem only. |
| Codomain | ℝ | Retained to use existing RingSeminorm; no unverified ordered-codomain widening claimed. |
| C | arbitrary real | Retained; global C≥0 would unnecessarily restrict the empty case. |
| M | square matrix | Determinant has square finite index. Current commutative-ring determinant uses subtraction/signs and commutative multiplication; no semiring or noncommutative determinant generalization claimed. |
| hM | all entries ≤C | Essential already for1×1; not dropped. |

The fixed parent normOne definition is unchanged. Generality is attained by replacing the standalone determinant statement, rather than rebuilding coefficient norms throughout the project. No upstream coefficient convolution instance is assumed.

## Phase 4b — verified weakening

**STRICTLY NARROWER THAN STANDARD / MODERN-IDIOM.** Two verified axes: arbitrary finite index and arbitrary commutative-ring entries with a real ring seminorm. Proposed upstream primary signature (actual compiled form, candidate name `Matrix.ringSeminorm_det_le`):

```lean
variable {R n : Type*} [CommRing R] [Fintype n] [DecidableEq n]
theorem ringSeminorm_det_le (p : RingSeminorm R) (hp : p 1 ≤ 1)
    (M : Matrix n n R) {C : ℝ} (hM : ∀ i j, p (M i j) ≤ C) :
    p M.det ≤ (Fintype.card n).factorial * C ^ Fintype.card n
```

The displayed signature is an excerpt, not an executable proof artifact; complete exact executable proofs are linked in verification.json. The compiled genericDet proof uses only nonnegative/subadditive/submultiplicative/neg-invariant size, size0=0 and size1≤1. The bundled seminormDet uses the existing RingSeminorm coercion and laws. The local coeffSeminorm package and exact original-statement recovery verify the representation bridge; no global norm instance is introduced. The arbitrary-index full caller also compiles. Cost: CHEAP mechanical abstraction of this proof; cost is not a verdict reason. Evidence: LINKSGEN and LINKSNATIVE.

## Phase 4c — modern idiom, all nine rows

| # | Question | Applies? | Consequence |
|---|---|---|---|
| 1 | Typeclasses/bundling | yes | Existing RingSeminorm bundles laws, supports multiple seminorms without instance choice. |
| 2 | Filters/topology | no | Finite algebraic estimate. |
| 3 | Universal property | no | No object constructed. |
| 4 | Bundled substructure | no | No closure predicate. |
| 5 | Algebra hierarchy | yes | Arbitrary CommRing, no field/domain/completeness/nontriviality. |
| 6 | Higher categories | no | No categorical statement. |
| 7 | Concrete index | yes | Arbitrary finite n, cardinal factorial/power. |
| 8 | Concrete-via-abstract | yes | Zero MvPolynomial mentions in proof body after determinant expansion; normOne mentions supply only size/law witnesses. Actual generic and bundled proofs compile. |
| 9 | False-generalization guard | PASS | RingSeminorm retains submultiplicativity; AbsoluteValue demands equality and cannot model coefficient L1 cancellation. Empty case keeps p1≤1. |

Concrete downstream consequences: the same determinant estimate applies to any chosen submultiplicative real ring seminorm, including polynomial coefficient L1 after local bundling, ordinary normed commutative-ring sizes with a unit bound, and multiple weighted seminorms once supplied. No new determinant proof is needed per concrete witness. Existing Matrix.det_le requires multiplicativity, so it cannot cover all of these. The original proof never inspects coefficients or monomials: the semantic abstraction is independent of future coefficient-size infrastructure. The ordinary norm/weighted possibilities describe applications of the axioms, not claimed newly compiled instances.

False-generalization example: (X+1)(X−1)=X²−1 has L1 size2, while both factors have size2; multiplicative AbsoluteValue would incorrectly demand2=4. Replacing L1 by a sup/Gauss norm, polynomial evaluation norm, field norm, or a spectral determinant changes the quantity. The guard rejects these substitutions. No claim of an available raw MvPolynomial norm instance is used.

## Phase 4.5 — infrastructure risks

n/a: theorem. The six individually justified rows are in generality.json: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priority, universes and coercion ambiguity. The proposed theorem uses the existing RingSeminorm FunLike coercion; local packaging evidence is not a new production structure or global instance.

## Phase 4.6 — all five proof-strategy rows

| # | Question | Finding |
|---|---|---|
| 1 | epsilon-delta versus filters | n/a: finite estimate. |
| 2 | element proof versus subobjects | n/a: entrywise real bounds. |
| 3 | sequences versus nets | n/a: no limits. |
| 4 | construction versus universal property | n/a: determinant already defined. |
| 5 | missing mathematical helper | yes: general RingSeminorm determinant bound. |

**REFACTOR-RECOMMENDED**: move the existing Leibniz/sum/product argument to RingSeminorm. Reuse Matrix.det_apply', Finset.le_sum_of_subadditive, Finset.le_prod_of_submultiplicative_of_nonneg, Finset.prod_le_prod₀, Int.units_eq_one_or and Fintype.card_perm. The exact bound is the missing helper, not another finite induction principle. The resulting polynomial corollary is shorter; no analytic machinery is required.

## Phase 5 — five actual mathlib methods on three forms

Twelve actual formal calls are retained with full raw responses. Current form is coefficient L1 polynomial determinants; literature-standard form is a normed-ring determinant bound; abstract form is a nonnegative/subadditive/submultiplicative neg-invariant size on a commutative ring. Local search reports index unavailable; its source hits cannot prove absence. External indices may differ from the pin; all positive candidates were checked at the pin.

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Lean-Finder | Matrix.det_le partial match; other polynomial determinant facts | Matrix.det_le; dominance facts distinct | Matrix.det_le; multiplicative norm context distinct |
| Loogle | det/MvPolynomial nonvanishing | det/norm no result | det/AbsoluteValue no result |
| LeanSearch | Matrix.det_le and determinant API | Matrix.det_le and matrix norm entry bounds | Matrix.det_le plus generic submultiplicative Finset induction |
| rg | rg-current/full-name | rg-literature | rg-abstract |
| local | project/scratch target hits excluded | Matrix.det_le source hit | RingSeminorm and its class/source |

Evidence: LINKSSEARCH; pinned exact source modules and hashes: LINKSMATHLIB.

`Matrix.det_le`, Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean42, has arbitrary finite index and codomain ordered ring, but its abv is a multiplicative AbsoluteValue. It also assumes source Nontrivial. Its exact native signature is retained. It is a genuine analogous theorem, not a specialization source for coefficient L1 or a merely submultiplicative RingSeminorm. RingSeminorm already exists with all required axioms; no determinant theorem for it was found by the completed searches/source audit. The positive API gap is the finite determinant factorial bound for this existing submultiplicative structure, beyond AbsoluteValue.map_prod. Absence is an evidence-based search conclusion, not a logical proof about every possible derivation.

## Phase 5.5 — all three statement-shape checks

Normal form: local normOne application versus bundled p M.det; upstream propose the latter. Existing Matrix.det_le uses n! • C^card; the compiled real form n! * C^card differs only by nsmul_eq_mul, so choose one convention consistently at cleanup. No iff/RHS rewrite orientation issue occurs.

Syntactic generality attempted and compiled: arbitrary finite index, explicit RingSeminorm, unchanged entrywise hM. The abstract hypotheses version proves sufficiency, but bundled p is easier for callers to supply. Full exact polynomial recovery verifies that no hidden representation conversion is required beyond local bundling.

Superfluous-argument audit: σ determines polynomial type; l/n determines determinant; M entries and hM supply uniform size bounds; C determines RHS. CommRing supports determinant signs and commuting products; Fintype/DecidableEq support finite determinant. hp is needed for empty index since arbitrary ring seminorms need not take1 to≤1 (scaled norms give a counterexample). All proposed assumptions are used, no Nontrivial/CompleteSpace/NormOneClass is added. **RESTATE-BEFORE-SHIP**, with bundled primary statement and arbitrary finite index.

## Phase 6.0 — every caller and inline audit

One named caller, one occurrence: **Roth.abs_coeff_det_hasseDeriv_le, CoeffNorm268**. External-to-declaring-file callers:0. Module docstring mentions and declaration head are not callers. The full consumer is replayed using the generalized finite-index proof instead of the target; original statement is also recovered through the compiled seminorm package. Callsite plan: keep normOne_det_le locally as that specialization, preserving the existing consumer call; alternatively substitute the general bound after packaging p. No deletion is necessary for an upstream general theorem.

No separate coefficient-L1 factorial determinant rederivation was found. CoeffNorm degree determinant bound uses degree sums; Theta's index determinant bound uses valuation-type minima; Wronskian computes an exact leading coefficient. These share Leibniz expansion but prove different statements. They are not duplicate coefficient norms.

Fresh direct proof-value audit covers all293 canonical names in tracked exact order,293unique, all present with values. Only Roth.abs_coeff_det_hasseDeriv_le directly uses the target. Private names are generated with Lean.mkPrivateNameCore. Portable validator compares the whole ordered array with tracked metadata. This audit concerns direct constants in proof values, not transitive kernel/simp dependency closure. Evidence: LINKSCALLERS.

## Phase 6 — actual composition experiments

1. Full original proof replay verifies the coefficient theorem at the pin.
2. Isolated Roth-free13-import genericDet reconstructs the bound from existing sum/product/order APIs, with new sign and factorial assembly. Missing-target guard confirms it cannot call the project target.
3. Isolated15-import seminormDet proves the existing RingSeminorm restatement and checks Matrix.det_le and exact seminorm law signatures.
4. Local coeffSeminorm package and original-statement recovery compile, making the representation bridge concrete; no new global instance.
5. Full sole consumer and arbitrary-index proof replay compile, and complete293 audit identifies the sole direct user.

Attempt Matrix.det_le: partial mathematical analog, fails its multiplicativity requirement for coefficient L1. Attempt norm notation: does not establish a determinant bound or compatible representation by itself. Attempt Finset sum/product: succeeds only as a new multi-step proof involving sign cases, product monotonicity and factorial/cardinality normalization. These new helpers are not existing mathlib replacements. No ≤3 existing-call derivation of the exact or generic bound is supplied. **NOT-COMPOSABLE under the strict Phase6 gate**; no unfolded-definition simp composition is presented as a NO certificate. One local caller is a weak reuse signal, outweighed by the independent existing RingSeminorm API gap. No cost-based downgrade or inherited parent verdict applies.

## Phase 7 — verdict and actionable upstream proposal

**YES-but-generalise-first (MODERN-IDIOM).** Add a primary determinant factorial bound for existing RingSeminorm R, with hp:p1≤1 and arbitrary Fintype n; retain the project normOne spelling as a local corollary. This is a verified abstraction of the standalone proof, with exact original recovery, not a request to redesign normOne across the project. It fills the submultiplicative gap beside Matrix.det_le, whose multiplicative AbsoluteValue cannot represent the intended L1 size. No unrelated new structure, instance or large foundational migration is a prerequisite.

Proposed exact new file: **Mathlib/LinearAlgebra/Matrix/Seminorm.lean**, importing Matrix.Determinant.Basic and Analysis.Normed.Unbundled.RingSeminorm. Proposed PR title: **feat(LinearAlgebra/Matrix): bound determinants under ring seminorms**. Proposed main name: Matrix.ringSeminorm_det_le (cleanup may choose RingSeminorm.det_le for namespace consistency). Provide a direct proof rather than ship the unbundled genericDet helper automatically; that helper is verification evidence for the abstraction.

Grouping against freshly read progress87: keep this as a separate general matrix/seminorm PR. Existing accepted YES determinant-adjacent Roth.det_choose_eq, Roth.coeff_wronskian_of_natDegree_injective and Roth.wronskian_ne_zero_of_natDegree_injective concern binomial/Wronskian structure and should remain in their algebraic groups. Accepted Hasse/Taylor YES results can depend on the generic determinant bound in downstream work without being bundled in this small infrastructure PR. The grouping list is actual accepted progress, not inferred from names.

Reviewer selection from relevant recent pinned commits: **Thomas Browning**, f932a30b0efd4855a092f755a28e53b11c254049,2026-08-26, added missing RingSeminorm API; **Eric Wieser**, a5c1af9396,2026-09-10, recent RingSeminorm structure/FunLike instance work. These are candidates, not claims that either approved the proposal. Matrix.AbsoluteValue's recent Kim Morrison2026 module cleanup is less mathematical than the seminorm API work. No contact was made. Evidence: LINKSPR.

Required next actions before any upstream submission:

1. Run `/generalise Roth.normOne_det_le` using the verified RingSeminorm signature, retaining hp and empty matrices; make the original a local specialization.
2. Run `/cleanup Roth/CoeffNorm.lean Roth.normOne_det_le` and cleanup the proposed new Mathlib/LinearAlgebra/Matrix/Seminorm.lean primary theorem, including naming, minimal imports, normalization and proof style.
3. Consider deriving the old AbsoluteValue bound from the new real-valued theorem only when its codomain specializes toℝ; do not reduce its currently broader ordered-ring codomain.
4. Run ordinary upstream tests/import checks and select the relevant reviewer candidates. This read-only assessment does not submit a PR.

Alternative local destination remains Roth/CoeffNorm.lean for the concrete wrapper; the generic seminorm theorem belongs in the general matrix API. No unresolved judgment question or permission request is needed to complete the assessment.

## Phase 8 — handoff and verification

verification.json records four accepted exact executed sources and full raw receipts. Two other recordings are retained separately: a partial warming response and a completed rejected normalization attempt with recovered sorryAx. The accepted correction uses explicit coeffSeminorm_apply/card_fin simplification and a typed Fin-index helper. Rejected attempts are not validation evidence; accepted outputs have success=true, partial=false, no error/warning/sorry, and standard axioms only (propext,Classical.choice,Quot.sound). All new Lean snippets have≤100-column lines; no raised limits, new axiom, sorry, unsafe or native_decide. Complete native proofs, source hashes, all method/channel evidence, exact canonical order, current manifest hashes/bytes and portable links are checked by validate.py. Historical worker-copy-manifest never replaces the current copy-manifest.json. Root acceptance is pending independent review.

LINKSFINAL.
'''
repls={'LINKS0':['baseline-build.txt','inputs.json','input-hash-check.json','source-module.lean.txt','canonical-order.json'], 'LINKSNATIVE':['verification.json','native-original-executed.lean.txt','native-original-success.json','native-raw-executed.lean.txt','native-raw-success.json','native-seminorm-executed.lean.txt','native-seminorm-success.json','native-consumers-executed.lean.txt','native-consumers-success.json'], 'LINKSWEB':[f'web-{i}.json' for i in range(7)],'LINKSLIT':['local-literature.txt','local-literature-source.json','rg-local-literature.json'],'LINKSGEN':['generality.json'],'LINKSSEARCH':['formal-search.json','rg-current.json','rg-literature.json','rg-abstract.json','rg-full-name.json'],'LINKSMATHLIB':['mathlib-inputs.json']+[f'mathlib-source-{i}.lean.txt' for i in range(5)],'LINKSCALLERS':['callers.json','rg-callers.json','rg-inline.json','canonical-audit-array.lean.txt','native-consumers-executed.lean.txt','native-consumers-success.json'],'LINKSPR':['reviewer-git.json','accepted-yes-grouping.json'],'LINKSFINAL':['rejected-warming-executed.lean.txt','rejected-warming-receipt.json','rejected-failed-executed.lean.txt','rejected-failed-receipt.json','assessment.json','overview-entry.json','verification.json','validate.py','copy-manifest.json']}
for k,v in repls.items():s=s.replace(k,', '.join(map(link,v)))
(D/'report.md').write_text(s)
phases={x:'PASS' for x in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; six risk rows justified'
out('assessment.json',dict(declaration=N,canonical_index=88,verdict='YES-but-generalise-first',reason='MODERN-IDIOM',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True))
out('overview-entry.json',dict(declaration=N,kind='theorem',type='∀ {σ : Type u_1} {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ}, (∀ μ ν, Roth.normOne (M μ ν) ≤ C) → Roth.normOne M.det ≤ ↑l.factorial * C ^ l',what='Bounds coefficient L1 size of an l×l polynomial determinant by l! C^l.',how='Leibniz expansion, subadditive finite sum, sign invariance, submultiplicative finite product, entrywise monotonicity, count permutations.',hypotheses='Arbitrary variables σ and l; all entries size≤C; C unrestricted; includes empty matrix.',project_dependencies=['Roth.normOne','Roth.normOne_sum_le','Roth.normOne_neg','Roth.normOne_prod_le','Roth.normOne_nonneg'],caller_summary='One direct named caller: Roth.abs_coeff_det_hasseDeriv_le at CoeffNorm268; exact293unique canonical proof-value audit confirms.',mathlib_api_audit='Matrix.det_le requires multiplicative AbsoluteValue; existing RingSeminorm supports submultiplicativity but searched determinant law missing.',moral_duplications='Analog of Matrix.det_le for merely submultiplicative real seminorms; degree/index/Wronskian determinant expansions prove different laws.',generalization='Verified arbitrary CommRing R, existing RingSeminorm p with p1≤1, arbitrary Fintype n; exact normOne specialization packaged and compiled.',missing_api='RingSeminorm determinant factorial bound beyond multiplicative AbsoluteValue.map_prod.',junk='Not junk: module Main result and direct Lemma3 consumer.',action='YES-but-generalise-first MODERN-IDIOM: propose Matrix.ringSeminorm_det_le in new Mathlib/LinearAlgebra/Matrix/Seminorm.lean; keep local normOne corollary; run /generalise and /cleanup.'))
