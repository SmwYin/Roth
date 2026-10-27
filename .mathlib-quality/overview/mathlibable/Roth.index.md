# Roth.index — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** The underlying weighted support minimum is already `AddMonoidAlgebra.infDegree`. An independently compiled all-P/all-r bridge preserves the project zero convention and removes the project aliases from its replacement term.

## Phase 0 — Doctor

Canonical declaration 133 is the public noncomputable definition `Roth.index` at `Roth/Index.lean:58`. The entire declaring module and all explicit consuming declarations were read; [Index source](../evidence/Roth.index/Index.lean.txt), [caller inventory](../evidence/Roth.index/callers.json), and [canonical entry](../evidence/Roth.index/canonical-entry.json) preserve them. The module develops weighted order at a point, differentiation, sums, products, renaming and the univariate multiplicity specialization.

The [baseline build](../evidence/Roth.index/baseline-build.txt) completed successfully, exit 0, 2467 jobs, no reported warnings/errors. Reuse is justified by fresh equality of all 17 source/pin hashes, not by the historical baseline commit alone: [inputs](../evidence/Roth.index/inputs.json), [hash check](../evidence/Roth.index/input-hash-check.json). No production changes or new worker build are claimed.

## Phase 1 — Comprehend

For a real polynomial P in a finite set of variables, translate the variables by α and examine the finite support of P(X+α). The index is the least sum of exponents divided by the corresponding natural parameters r. Equivalently, for nonzero P it is the smallest such weight of a Hasse derivative that does not vanish at α. The zero polynomial has index 0 in this implementation; division by a zero parameter contributes 0, so the definition permits all r, including mixed zero parameters.

Full elaborated type:

```lean
@Roth.index : {σ : Type u_1} → [inst : Fintype σ] →
  MvPolynomial σ ℝ → (σ → ℝ) → (σ → ℕ) → ℝ
```

The body is `sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))`. Parameters: arbitrary-universe σ indexes variables; Fintype supplies the global finite sum in weight; P is the input, α the translation center, and r the denominators. There are no positivity or nonvanishing hypotheses on the definition. `Roth.weight` and `MvPolynomial.taylor` are project declarations, hence do not count as mathlib building blocks in composition. The body is a construction, with no proof hypotheses. Original definition uses only standard axioms. [Exact original and full printer](../evidence/Roth.index/index-original-executed.lean.txt), [canonical audit source](../evidence/Roth.index/index-audit-executed.lean.txt) and [complete native receipt](../evidence/Roth.index/index-original-audit-receipt.json) establish this without printer elision. The runtime canonical audit reports exactly 293 requested, unique, present, and value-bearing declarations, with 39 direct kernel-value consumers of index; this differs intentionally from the explicit-source count.

## Phase 2 — Preliminary definition checks

BIG: the main named mathematical concept of the module and a central quantity in Roth's argument. One substantive body line, so ONE-LINER.

| Exemption | Applies? | Evidence |
|---|---|---|
| Defeq barrier | no | The exact RHS agrees by rfl. No caller requires an opaque or irreducible anchor. |
| Typeclass diamond prevention | no | A real-valued function introduces no instance or alternate scalar action. |
| Semantic intent / stable API | yes | `indexSet`, `le_index_iff`, `index_mul`, `main_lemma` and `abs_eval_lt_of_le_index` use a compact point-centered index API. The 34 source callers provide actual evidence. |

ONE-LINER WITH-EXEMPTION. This exemption is independently checked; it does not settle whether the name belongs upstream.

## Phase 3 — Exhaustive literature

Only requests, response bytes/digests and sanitized locators are archived, together with original summaries. [Three general forms](../evidence/Roth.index/web0-metadata.json), [nLab/nCatLab/Stacks](../evidence/Roth.index/web1-metadata.json), [MO/arXiv](../evidence/Roth.index/web2-metadata.json), [refinement](../evidence/Roth.index/web3-metadata.json), [recent monomial valuations](../evidence/Roth.index/web4-metadata.json), [direct primary access](../evidence/Roth.index/web-primary-metadata.json), [explicit nCatLab-path refinement](../evidence/Roth.index/web-ncatlab-metadata.json).

| Channel | Actual request / locator | Result |
|---|---|---|
| General web, specific | `Roth theorem index polynomial minimum sum i_j r_j derivatives index zero infinity` | Roth's ICM1958 account, p.206, describes the least weighted derivative order nonvanishing at a point. [Primary locator](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf). Indexed excerpt inspected; direct open failed because the 74,705,952-byte PDF exceeded the fetch limit. |
| General web, general | `weighted order of vanishing polynomial positive real weights monomial valuation` | Weighted orders and monomial valuations use linear forms on exponent vectors. This supports arbitrary nonnegative real weights, while a total monomial ordering additionally needs tie-breaking. The minimum support weight alone does not require a total monomial order. |
| General web, aliases | `Dyson lemma index polynomial multiplicity weighted index` | [Vojta, Understanding Dyson's Lemma](https://people.math.rochester.edu/faculty/ttucker/Upstate2012.dir/Slides.dir/Vojta.pdf), definition under Detailed Description: weighted index of a local divisor equation on a product of smooth curves. Confirms geometric use beyond this polynomial proof; local equations/coordinates are an expanded setting, not a drop-in Lean weakening. |
| ChatGPT math MCP | Standard form, generality, historical evolution | n/a: ask_chatgpt_math unavailable; no answer fabricated. |
| Local references | `index|P_\\alpha|weightedOrder` in clean.tex | [Local search](../evidence/Roth.index/local-literature.json), [§4 excerpt](../evidence/Roth.index/clean-index-excerpt.tex.txt): positive REAL denominators, finite support minimum, zero value +∞. Integral weights give a weightedOrder route; arbitrary real weights require the support minimum. |
| nLab | `site:ncatlab.org/nlab weighted valuation order vanishing polynomial`, then valuation-page refinement | [Valuation](https://ncatlab.org/nlab/show/valuation), Definition and Rational functions: additive valuation has zero value +∞ and least nonzero degree as a model. Direct open failed with unsupported XHTML; indexed definition was inspected. This is adjacent structural context, not an exact point-index API. |
| nCatLab categorical | `site:ncatlab.org "monomial" "valuation"`; explicit refinement `site:ncatlab.org/ncatlab "monomial" "valuation" weighted polynomial order of vanishing` | Broad query returned same-host nLab pages. The explicit nCatLab-path request returned only off-path nLab-hosted Bhatt–Snowden Faltings notes, whose excerpt concerns finite group schemes and was rejected as a point-index hit. No direct nCatLab result or categorical universal property was located. This is an actual failed-to-find targeted query, not an absence proof or an independent publication. |
| Stacks | `site:stacks.math.columbia.edu order vanishing polynomial multiplicity valuation` | [Tag 02MB](https://stacks.math.columbia.edu/tag/02MB), Definition 10.121.2: order along a one-dimensional local Noetherian domain via module length. Direct page inspected. Adjacent geometry; it does not replace a multivariate weighted support minimum with arbitrary r. |
| MathOverflow | `site:mathoverflow.net weighted order vanishing polynomial monomial valuation` | [Monomial orders](https://mathoverflow.net/questions/476147/how-should-we-picture-the-set-of-monomial-orders-positive-monoid-orders-on) discusses nonnegative real weight linear forms, rational independence and tie-breaking. Useful distinction: this index need not choose a unique leading monomial. No purported proof is taken from an answer. |
| Recent arXiv, 2021-10-27–2026-10-27 | Roth/Dyson query; refined `site:arxiv.org/abs/ "monomial valuations" after:2021-10-27` | Original query returned unrelated additive-combinatorial Roth and econometric Roth papers, rejected. [Dutta–Ghosh, arXiv:2609.03451](https://arxiv.org/abs/2609.03451), submitted 2026-09-03, abstract directly connects monomial valuations to Taylor expansions over valued positive-characteristic fields. Abstract inspected; no full-paper equivalence claimed. Other recent monomial-valuation hits concern geometry and are supplementary. |

Literature synthesis: weighted index/order of vanishing is standard; point translation converts it to a finite coefficient-support minimum. The manuscript is broader in real denominator weights and differs at zero. Natural reciprocal weights are a special case; positivity is needed for the usual interpretation, not for constructing a finite minimum. Replacing zero by +∞ is an explicit representation change, not an equality in ℝ. The source warning about not converting infinite order to a natural number refers to preserving its +∞ convention; the project deliberately projects zero to 0 instead.

## Phase 4a–4b — Generality

| Parameter | Actual role | Fixed-interface versus expanded representation |
|---|---|---|
| σ : Type u | arbitrary variable universe | Fintype is used by Roth.weight, not polynomial finite support. A Finsupp-supported sum eliminates this assumption in an expanded representation. |
| Fintype σ | summing over all variables | Not mechanically droppable while retaining Roth.weight's signature. Actual genericIndex uses d.sum instead. Fintype-choice independence is separately tested. |
| ℝ coefficients | supports evaluating Hasse derivatives and real arithmetic in later results | Construction only needs CommSemiring R and support of a translated polynomial; actual generalized construction is universe-polymorphic in R. No field/domain/char-zero hypothesis is needed to define it. |
| P | polynomial | Every polynomial has finite support even for infinite σ. Power-series extension with arbitrary negative/real weights may have unbounded-below support, so it is not an unconditional generalization of a finite attained minimum. |
| α : σ→ℝ | arbitrary center | CommSemiring R-valued centers suffice for translation. No finiteness/support/regularity assumption. |
| r : σ→ℕ | reciprocal weights, including rj=0 | Real weights give the manuscript's positive-real denominator form. No positivity can be silently added when comparing to the original definition. |
| ℝ result | uses sInf ∅=0 | WithTop ℝ, infDegree, and untopD0 preserve all original values; keeping top instead restores the manuscript's zero convention as a separate interface. |

A verified expanded definition and its specialization are retained in native evidence. Generality status is strictly narrower in representation than the finite-support weighted-order construction; there are no claimed mechanically droppable parameters in the unchanged weight/taylor signature. Real-valued arbitrary weights and coefficient semirings are concrete generalizations, not merely suggested signatures. Existing `AddMonoidAlgebra.infDegree` already abstracts the coefficient-support minimum to a semilattice with top. Existing `MvPowerSeries.weightedOrder` instead uses natural additive weights and ENat values.

## Phase 4c — All nine modern-idiom questions

| # | Question | Assessment |
|---|---|---|
| 1 | Typeclasses / instances | CommSemiring supplies coefficient algebra in generalized construction. A new Index class would add no useful inference. |
| 2 | Filters / nets | No convergence or topological limiting argument. |
| 3 | Universal-property replacement | Translation already uses free-algebra evaluation aeval. The support minimum is an order construction, not another universal algebra object. |
| 4 | Bundled substructure | Use the existing support/degree API; no closed subset or ad hoc submodule occurs. |
| 5 | Weaken field to semiring/module | Yes: support minimum and translation work over CommSemiring. Later multiplicativity can require domain hypotheses independently. |
| 6 | Higher category | No higher-categorical data in this real scalar. |
| 7 | Concrete index / ordered structure | Yes: arbitrary σ through finite support; arbitrary weight maps and semilattice-top target through infDegree. This enables nonintegral weights and preserves infinity until deliberate projection. |
| 8 | Concrete-via-abstract diagnostic | Body has zero occurrences of index; Taylor appears once as a finite-support input, followed only by image and sInf. Diagnostic fires: the abstract object is a weighted minimum of support, already represented by infDegree. Translation specifies the center and remains genuine data. |
| 9 | False-generalization guard | Preserve 0 at P=0 and all zero-denominator cases in the comparison. Reject unconditionally identifying arbitrary-real-weight formal power-series infima with attained minima, and reject replacing formal polynomials by pointwise functions over finite rings. A generic valuation bundle would require laws not provided by the definition and its ℝ zero convention. Arbitrary real weights still define a finite minimum, but nonnegativity theorems then require nonnegative-weight hypotheses; they are not transported without those conditions. |

Modern idiom: exploit existing generic infDegree/weight and retain point translation as specialization. Replacing the stable point-index name is a separate API decision; no cost argument is used.

## Phase 4.5 — Definition infrastructure risk

| Risk | Verdict | Actual probe / interpretation |
|---|---|---|
| Typeclass diamond | none observed | Synthesize real conditionally complete order; compare two Fintype values by subsingleton equality. Existing scalar/order instances are selected; index introduces no instance. |
| Reducibility leak | low | Exact body equality by rfl, ordinary semireducible def, no reducible attribute; the operation is noncomputable support/order data. |
| Noncanonical unfolding | low | `fail_if_success simp only` tests that the equation does not close solely from simp's rewrite set; rfl then closes it. Explicit `simp [index]` remains an intentional unfolding at local consumers. |
| Instance priority collision | none | Synthesis occurs with existing instances and with alternate Fintype data; the declaration is a value, has no priority and registers no search rule. |
| Universe issues | none observed | Arbitrary u generic probes and a finite ULift to universe 1 elaborate; no universe-0 variable restriction. Coefficients stay ℝ in the original, with independent universe v in the expanded construction. |
| Coercion ambiguity | none observed | Actual Finset support-to-Set expression and polynomial-to-power-series coercion are tested; function application uses ordinary function evaluation. No custom CoeFun/CoeSort is introduced. |

Overall LOW; no HIGH row. All six have actual native exercises rather than theorem-kind exemptions. [Accepted exact probes](../evidence/Roth.index/index-probes-final-executed.lean.txt), [complete raw success](../evidence/Roth.index/index-probes-final-receipt.json) cover named directUnfold, genericSpecialization, zero, zeroWeights, beta, universeProbe, fintypeIndependence, noAutomaticUnfold and positiveWeightedOrder. Initial congruence/unknown image-lemma attempts and the second zero-weight simplification failure are archived as rejected evidence, not accepted verification.

## Phase 4.6 — All five proof-strategy questions

| Question | Assessment |
|---|---|
| ε–δ versus filters | n/a mathematical content: no topology. |
| Elements versus point-free algebra | Existing aeval already handles translation structurally. Generic support degree is preferable organization to a second coefficient-minimum theory. |
| Sequences versus nets | No analytic sequence argument. |
| Construction versus universal property | aeval is the universal substitution construction; no additional class required. |
| Missing helpers mathlib should have | The finite sInf/infDegree projection bridge is normalization API, not an existing named point-index. The project weightedOrder bridge also contains actual minimum/weight normalization proof; it cannot be counted as an already existing mathlib call. |

Strategy verdict: **REFACTOR-RECOMMENDED** for an upstream proposal: reuse generic support-degree and weight constructions, with one bridge preserving project conventions. The present one-line definition is mathematically clear; any refactor must preserve zero and r=0 behavior. This is an organization choice, not a proof-performance or cost claim.

## Phase 5 — Five actual mathlib methods

[Raw formal requests and receipts](../evidence/Roth.index/formal-search.json) retain all actual calls, including failed-to-find exact patterns. [Current source search](../evidence/Roth.index/rg-current.json), [literature form](../evidence/Roth.index/rg-literature.json), [abstract support-degree form](../evidence/Roth.index/rg-abstract.json) supply pinned source evidence.

| Method | Current point-index | Standard weighted order | Abstract minimum support degree |
|---|---|---|---|
| Finder | Specific Roth query returned irrelevant bounds, not a replacement | weightedOrder, weightedOrder_le, existence/characterization | infDegree, infDegree_withTop_some_comp, support-degree inequalities |
| Loogle | Exact polynomial→point→natweights→ℝ pattern returned no items | weightedOrder and finite/top API | sInf image generic facts, then exact infDegree pattern and laws |
| LeanSearch | Univariate multiplicity and weightedOrder, analytic adjacent results | weightedOrder, weighted homogeneous components | infDegree and support-degree sum/product inequalities |
| rg | No exact independent point-index definition found | Pinned weightedOrder in Order.lean; natural weights | Pinned infDegree in MonoidAlgebra/Degree.lean:624; Finset inf'/sInf normalization |
| local | Project index and scratch replay hits (not mathlib replacements) | weightedOrder family | infDegree and WithTop comparison |

All services returned isError=false; local index reports unavailable, so its missing/generated hits are not absence evidence. Remote indexes may differ from the pin; native positive checks determine usable signatures. No absence verdict rests on a timeout or search failure. The mathematical order construction is present as `AddMonoidAlgebra.infDegree`; weightedOrder is a complementary natural-weight/power-series API. Weighted total degree is a maximum, hence not this minimum. Univariate rootMultiplicity alone cannot represent multiple independent weights.

## Phase 5.5 — Statement shape

Normal forms: (1) finite real sInf of weighted Taylor support, (2) infDegree in WithTop ℝ followed by untopD0, (3) normalized natural weightedOrder for positive integral denominators, (4) direct finite Finsupp-weight minimum with arbitrary weights. The canonical generic construction is infDegree. A comparison should have generic degree/projection on its RHS and avoid a quadratic network of pairwise normal forms. The existing index_eq_weightedOrder_div has the correct specialized direction but imposes positive r and initially P≠0.

Syntactic generality: a point-centered index is convenient for 34 consumers; generic infDegree avoids a parallel order theory, and real reciprocal weights cover the manuscript. Neither removing α nor replacing P by a support set gives the same *point-centered* interface, though either describes the abstract core. Keep arguments in their natural polynomial/point/weights order for local use.

Superfluous-argument audit: P, α and r each change the value in examples, so are not unused. σ is genuinely arbitrary. Fintype is required only by the current global-sum parent interface, with verified supported-sum replacement; ℝ coefficients are similarly an interface restriction, not a mathematical necessity. No positivity/nonvanishing premise exists to remove. Normal form: REFACTOR toward infDegree. Syntactic generality: RESTATE to arbitrary finite-support weights if a new layer is proposed. Superfluous fixed-interface arguments: NONE mechanically droppable; Fintype and ℝ admit the separately verified expanded representation. Overall **RESTATE-BEFORE-SHIP** if any new upstream layer is proposed.

## Phase 6.0 — Every explicit caller and inline audit

Fresh lexical enumeration strips nested/block/line comments and counts the standalone index identifier, including statements and bodies. **34 distinct explicit callers, 60 occurrences:** Index 16, Theta 8, MainLemma 9, Main 1. K excluding the declaring module is 18 declarations in three files. This is not kernel/simp dependency closure. [Caller inventory](../evidence/Roth.index/callers.json) includes every declaration's exact fragment, source hash, reference lines and refactor plan. The definition is not dead code.

| Caller | File:line | Occurrences |
|---|---|---|
| `Roth.le_index_of_forall_eval_eq_zero` | `Roth/MainLemma.lean:419` | 1 |
| `Roth.exists_hasseDeriv_eval_ne_zero` | `Roth/MainLemma.lean:454` | 1 |
| `Roth.exists_hasseDeriv_index_eval_bound_aux` | `Roth/MainLemma.lean:477` | 3 |
| `Roth.exists_mem_RSet_le_index_aux` | `Roth/MainLemma.lean:550` | 1 |
| `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | `Roth/MainLemma.lean:581` | 1 |
| `Roth.exists_mem_RSet_le_index_of_log_bound_aux` | `Roth/MainLemma.lean:618` | 1 |
| `Roth.exists_auxiliary_polynomial_of_log_bound_aux` | `Roth/MainLemma.lean:643` | 1 |
| `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | `Roth/MainLemma.lean:692` | 1 |
| `Roth.main_lemma` | `Roth/MainLemma.lean:735` | 2 |
| `Roth.indexSet` | `Roth/Theta.lean:62` | 1 |
| `Roth.index_le_Θ` | `Roth/Theta.lean:99` | 1 |
| `Roth.Θ_le_of_forall_index_le` | `Roth/Theta.lean:124` | 1 |
| `Roth.index_unique_le_log_div` | `Roth/Theta.lean:223` | 1 |
| `Roth.sum_max_sub_le_index_det` | `Roth/Theta.lean:376` | 7 |
| `Roth.index_separated_mul_le_aux` | `Roth/Theta.lean:414` | 1 |
| `Roth.index_det_le` | `Roth/Theta.lean:457` | 1 |
| `Roth.index_le_lem6` | `Roth/Theta.lean:556` | 2 |
| `Roth.index_le_weight` | `Roth/Index.lean:69` | 1 |
| `Roth.exists_weight_eq_index` | `Roth/Index.lean:76` | 1 |
| `Roth.le_index_iff` | `Roth/Index.lean:85` | 1 |
| `Roth.index_nonneg` | `Roth/Index.lean:93` | 1 |
| `Roth.index_eq_zero_iff` | `Roth/Index.lean:98` | 1 |
| `Roth.index_sub_weight_le_index_hasseDeriv` | `Roth/Index.lean:109` | 2 |
| `Roth.le_index_sum` | `Roth/Index.lean:118` | 2 |
| `Roth.index_eq_weightedOrder_div` | `Roth/Index.lean:143` | 1 |
| `Roth.index_mul` | `Roth/Index.lean:162` | 3 |
| `Roth.index_prod` | `Roth/Index.lean:175` | 2 |
| `Roth.index_neg` | `Roth/Index.lean:190` | 3 |
| `Roth.index_C_mul` | `Roth/Index.lean:195` | 4 |
| `Roth.index_mul_left_weights` | `Roth/Index.lean:200` | 4 |
| `Roth.index_rename` | `Roth/Index.lean:212` | 4 |
| `Roth.index_le_card` | `Roth/Index.lean:224` | 1 |
| `Roth.index_unique` | `Roth/Index.lean:234` | 1 |
| `Roth.abs_eval_lt_of_le_index` | `Roth/Main.lean:380` | 1 |

Each row's plan is to retain the local API, or transport it through the verified whole-function bridge to infDegree; if the name is removed, expand that exact expression at every statement/body occurrence. Sum/product/derivative theorems retain their nonzero hypotheses under the project's zero convention. No claim of a fully migrated production build is made. [Inline audit](../evidence/Roth.index/rg-inline.json) distinguishes the own sInf body, its support manipulations and generic library degree infrastructure; no additional independent point-index implementation was found.

## Phase 6 — Actual composition experiments

The direct original-body equality is rfl; expanding project parents gives a finite weighted minimum of an `aeval` substitution. The [mathlib-only preparation](../evidence/Roth.index/mathlib-probe-prep.lean.txt) distinguishes input construction from the normalization bridge; the accepted execution is archived separately.

The positive integral-parameter alternative is independently checked by `positiveWeightedOrder`: it extends the existing project theorem to P=0 by a separate zero case. This is **a project bridge**, not a preexisting mathlib replacement. A naive extension using D=∏r to mixed-zero r is invalid: D may vanish while the index still records a positive contribution from a different coordinate. The all-r infDegree route does not clear denominators.

The infDegree replacement preserves infinity internally and projects it to 0 with untopD0. Its generic finite-support bridge uses an empty/nonempty case split, `Finset.coe_inf'` and `Finset.inf'_eq_csInf_image`; the old sInf form is **not definitionally equal** to the new form. The empty branch is a separate simp normalization of the two default values, not included in the two nonempty-branch lemma calls. This normalization is new proved glue from existing general lemmas, not an already named point-index theorem. The core named mathematical object, minimum support degree for an arbitrary weight function, is already infDegree. The one-line replacement term counts infDegree plus its explicit default-value projection; translation and weighting specify its input data. Fully expanding the inputs invokes aeval and Finsupp.weight as well, for four named construction operations before counting X/C constructors, support projections or arithmetic. Thus no claim is made that the entire old-spelling equality is a ≤3-call proof. Composition conclusion: the existing more-general infDegree representation is usable after the verified normalization bridge; the old expression requires a genuine normalization proof. This supports the more-general-object NO-mathlib-has-it route, rather than a false ≤3-call NO-composable classification.

The construction is not justified by a closing `simp [definitions]` experiment. Phase 6b's trivial-simp caution is respected: any such expanded consumer simplification alone would be BORDERLINE. The decisive positive hit is the independently checked existing generic support-degree definition and its representation bridge; the specialized power-series normalization and project lemmas do not count as library building blocks.

The [accepted mathlib-only finite bridge](../evidence/Roth.index/index-mathlib-infdegree-final-executed.lean.txt) and [raw success](../evidence/Roth.index/index-mathlib-infdegree-final-receipt.json) prove the arbitrary-weight/CommSemiring/arbitrary-σ comparison. The initially deprecated real import and two unsuccessful rewrite shapes are retained separately as rejected attempts, with complete receipts; they do not count as accepted evidence.

The [fully expanded mathlib-only construction](../evidence/Roth.index/index-expanded-mathlib-executed.lean.txt) with [complete raw success](../evidence/Roth.index/index-expanded-mathlib-receipt.json) defines denominatorIndex using only aeval, infDegree, untopD and Finsupp.weight, without Fintype, project imports or project definitions. Its denominatorBridge explicitly identifies the supported-sum form. The [original-to-expanded bridge](../evidence/Roth.index/index-expanded-bridge-executed.lean.txt), [native success](../evidence/Roth.index/index-expanded-bridge-receipt.json), specializes this to the actual original definition. Both weightBridge and fullyExpandedBridge print only standard axioms. The closing simp normalization there transports an already proved representation bridge; it is not itself evidence of an existing mathlib point-index law.

The [actual caller experiment](../evidence/Roth.index/index-consumers-executed.lean.txt), [raw success](../evidence/Roth.index/index-consumers-receipt.json), proves targetBridge for every P and r, then transports the entire real set indexSet, including its existential polynomial/point data and coprimality predicate. No own/downstream index theorem is used to prove the target bridge. The caller proof uses the newly proved bridge as transport, explicitly not as a preexisting library lemma. All named accepted proofs print standard axioms. Persistent disk evidence is complete/nonpartial with no errors or warnings; required target assertions are scoped to new regions 16132, 16453, 16522 and 16552 to avoid historical info-message confusion.

## Phase 7 — Verdict and concrete action

**NO-mathlib-has-it**, in the more general support-degree representation. `AddMonoidAlgebra.infDegree` already computes the mathematical minimum underlying this definition, with arbitrary degree function and ordered target. Its `WithTop ℝ` specialization followed by default-zero projection recovers every value of Roth.index, including P=0 and all r with zero entries. The one-line replacement is:

```lean
(AddMonoidAlgebra.infDegree (fun d ↦ (Roth.weight r d : WithTop ℝ)) (taylor α P)).untopD 0
```

This is a specialization/projection of an existing named object, not a claim that mathlib exports a declaration named Roth.index. The native target bridge proves its equality to the old sInf expression. That bridge is not rfl: it uses a support empty/nonempty split and two existing finite-order normalization lemmas. The proof and its call count are exposed in Phase 6, rather than hidden in a new helper advertised as preexisting mathlib API. Parent weight and Taylor are independently expanded to Finsupp.weight and aeval in mathlib-only evidence.

The one-line semantic exemption supports a useful **project-local** wrapper; it does not identify a missing generic minimum object upstream. The real-weight and coefficient-semiring generalizations likewise land on existing infDegree rather than requiring another definition. This decision does not inherit the earlier Taylor or weight verdict, does not depend on implementation cost, and is not inferred from negative search results. Existing weightedOrder is independently useful for multiplicativity; no claim that infDegree alone supplies every later index theorem is made.

Action: retain the convention-bearing wrapper in `Roth/Index.lean`; if refactoring, implement it using the displayed infDegree projection and use the all-P/all-r bridge to transport every listed caller. The row-by-row plans in callers.json cover all statement/body references. Keep nonzero premises on sum/product/comparison theorems where the real zero convention requires them. If eliminating the local name, inline that exact projected infDegree expression at all 60 occurrences; this is mechanically justified by the bridge, though retaining the documented local name is clearer. The alternative destination is this project module, not Archive or an unrelated satellite. There is no proposed upstream PR for the definition; independently useful comparison lemmas or later laws require their own assessment.

## Phase 8 — Handoff

All phases are complete, with verification unresolved=[] and root acceptance pending. [Assessment](../evidence/Roth.index/assessment.json), [verification](../evidence/Roth.index/verification.json), [overview entry](../evidence/Roth.index/overview-entry.json), [current copy manifest](../evidence/Roth.index/copy-manifest.json), and [portable validator](../evidence/Roth.index/validate.py) complete the handoff. The validator checks accepted exact source/receipt pairs, scoped required information and standard axioms, complete native success, all 17 inputs and candidate hashes, all 34 explicit caller fragments, all search channels, exact 293 canonical-name order including private names, current artifact hashes/bytes, links, and the tracked credential guard. It supports scratch and integrated layouts and treats current copy-manifest as authoritative; any historical worker-copy-manifest is not a substitute. Production, pins, Git and progress records remain unchanged by this worker.
