# Roth.index_nonneg — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** Independently re-aiming at the parent's existing mathlib counterpart `AddMonoidAlgebra.infDegree` finds the finite-inf lower-bound introduction law `Finset.le_inf_iff.mpr`. Nonnegative support degrees give nonnegative infDegree. A fresh actual-context proof checks the all-P/all-r real projection bridge, including empty support. This is not a blanket inherited verdict or a claim of a ≤3-call old-form mathlib proof.

## Phase 0 — Doctor

Canonical declaration138, public theorem at `Roth/Index.lean:93`. The entire declaring module and all three consuming declarations were read; [Index](../evidence/Roth.index_nonneg/Index.lean.txt), [Theta](../evidence/Roth.index_nonneg/Theta.lean.txt), [callers](../evidence/Roth.index_nonneg/callers.json), [canonical entry](../evidence/Roth.index_nonneg/canonical-entry.json). Index develops weighted order at a point, differentiation, sums, products, renaming and multiplicity. Theta uses its nonnegativity in a supremum and determinant estimate.

The shared successful [baseline build](../evidence/Roth.index_nonneg/baseline-build.txt) exited0 after2467 jobs. Reuse rests on fresh matching of all17 production-source/pin hashes, not the baseline commit alone: [inputs](../evidence/Roth.index_nonneg/inputs.json), [hash result](../evidence/Roth.index_nonneg/input-hash-check.json). Production, pins and Git were not changed by this assessment.

## Phase 1 — Comprehend

Full native type:

```lean
Roth.index_nonneg.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ]
  (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ), 0 ≤ Roth.index P α r
```

Translate P to P(X+α), weight each exponent d by the sum of d(j)/r(j), and take the real infimum over its finite coefficient support. Every term is nonnegative because both exponent and denominator are natural numbers, including the totalized real division convention at r(j)=0. `Real.sInf_nonneg` also covers empty support since real sInf∅=0. Thus the theorem holds at P=0 without a nonvanishing assumption. The proof is exactly `Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)`.

σ is arbitrary-universe, Fintype supplies Roth.weight's global finite sum; P, α and r select the quantity. There are no further hypotheses. Project dependencies are `Roth.index`, `Roth.weight`, `Roth.weight_nonneg` and `MvPolynomial.taylor`. In particular weight_nonneg is project API and cannot be counted as an existing mathlib building block.

Fresh [original source](../evidence/Roth.index_nonneg/index-nonneg-original-executed.lean.txt), [canonical audit](../evidence/Roth.index_nonneg/index-nonneg-audit-executed.lean.txt) and [complete raw native receipt](../evidence/Roth.index_nonneg/index-nonneg-original-audit-receipt.json) establish type, full body and standard axioms, without printer elision. Target-scoped audit counters are293 requested/unique/present/value-bearing, in canonical exact order, with3 direct kernel-value consumers. Required target info is scoped to new native region2741/2744; historical diagnostics do not substitute for the target audit.

## Phase 2 — Preliminary classification

**SMALL**: an elementary lower-bound consequence of the index definition, used as local API by three results. Phase2b definition-only one-line/exemption test is **n/a — theorem**. Its one substantive proof line is not a one-line definition exemption claim.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/bytes/status, sanitized locators and selected titles are preserved, without article/search-result bodies: [general forms](../evidence/Roth.index_nonneg/web0-metadata.json), [nLab/nCatLab/Stacks](../evidence/Roth.index_nonneg/web1-metadata.json), [MO/arXiv/Roth](../evidence/Roth.index_nonneg/web2-metadata.json), [refinement](../evidence/Roth.index_nonneg/web3-metadata.json), [primary direct access](../evidence/Roth.index_nonneg/web4-metadata.json). [Local search](../evidence/Roth.index_nonneg/local-literature-search.json), [manuscript excerpt](../evidence/Roth.index_nonneg/clean-excerpt.tex.txt), [original synthesis](../evidence/Roth.index_nonneg/literature-summary.json).

| Channel | Exact query / locator | Result and limits |
|---|---|---|
| General specific | `Roth polynomial index nonnegative weighted derivatives index definition` | Roth's 2020 chapter locator discusses multivariate multiplicities. USNA Polynomial Index hit is a different root-cell enumeration and is rejected. |
| General standard | `weighted order of vanishing polynomial nonnegative weights minimum support` | Weighted approximation and sum-of-squares hits concern different objects; not evidence for this theorem. Refined historical query below finds the defining derivative-weight minimum. |
| General abstract | `finite infimum nonnegative values minimum semilattice lower bound` | Finite-semilattice literature describes a greatest lower bound. [Finite distributive semilattices](https://gonzalezluciano.github.io/files/articulos/Finite_distributive_semilattices.pdf), introductory finite-meet discussion, is structural context. Nonnegative minimum follows from the greatest-lower-bound property; that implication is our synthesis. |
| ChatGPT math | Standard form, generality and historical evolution | n/a: ask_chatgpt_math unavailable. No fabricated consultation. |
| Local clean.tex | `index|nonnegative|ind\(P\)|non-negative` | §4, definition and immediately following lemma: positive real denominators, nonnegative weights, zero index convention +∞. The current project projects zero to0; the nonnegativity conclusion survives. |
| nLab | `site:ncatlab.org/nlab nonnegative valuation weighted order vanishing` | [Valuation ring](https://ncatlab.org/nlab/show/valuation%2Bring) provides surrounding valuation context. Refined meet query below supplies exact order structure. |
| nCatLab explicit path | `site:ncatlab.org/ncatlab finite meet lower bound nonnegative valuation` | Returned nLab-hosted order/valuation material, not an exact /ncatlab hit. No categorical replacement theorem inferred. |
| Stacks | `site:stacks.math.columbia.edu order vanishing nonnegative regular function` | [Tag02MB](https://stacks.math.columbia.edu/tag/02MB), Definition10.121.2, defines order of a nonzero local regular element using module length. Adjacent nonnegativity context; its one-dimensional geometric hypotheses are unnecessary for a finite support minimum. Direct page inspected. |
| MathOverflow initial | `site:mathoverflow.net weighted order vanishing nonnegative monomial valuation` | No exact target theorem identified in this first batch; refined query below obtains a concrete weighted support minimum. |
| Recent arXiv initial | `site:arxiv.org after:2021-10-27 weighted index polynomial Roth nonnegative order vanishing` | No exact weighted-index nonnegativity result identified; no absence inference. Window2021-10-27 through2026-10-27. |
| General historical refinement | `Roth rational approximations index polynomial nonnegative minimum derivatives 1958` | [Roth ICM1958 p206](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) defines the least weighted derivative order that does not vanish. Indexed p206 inspected; direct PDF open failed because74705952-byte content exceeds fetch limit. |
| MO refinement | `site:mathoverflow.net "monomial" "valuation" weights` | [Extension of homomorphism to place](https://mathoverflow.net/questions/190937/extension-of-homomorphism-to-place-in-quotient-field-or-of-local-ring-to-valuat/191371), answer's displayed weighted support minimum, gives an example min(i+mj), zero value∞. Useful naming/representation context, not a proof imported from an answer. |
| Recent arXiv refinement | `site:arxiv.org after:2021-10-27 "monomial valuations" Taylor` | [Dutta–Ghosh arXiv2609.03451](https://arxiv.org/abs/2609.03451), submitted2026-09-03, abstract connects monomial valuations and Taylor expansions in valued positive-characteristic fields. Abstract directly inspected; adjacent research, no full-paper theorem equivalence claimed. |
| nCatLab refinement | `site:ncatlab.org/ncatlab "meet" "lower bound"` | Returns [nLab meet](https://ncatlab.org/nlab/show/meet) and nLab/publications paths, not a /ncatlab namespace hit. Indexed meet definition and empty-meet top example inspected. Direct nLab open failed unsupported application/xhtml+xml. |
| Direct primary access | Tag02MB; nLab meet; ICM1958; arXiv2609.03451 | Stacks and arXiv opened successfully; nLab XHTML and ICM size failures retained honestly in the metadata. |

Standard names are **weighted index**, **weighted order of vanishing**, and abstractly **lower-bound introduction for a finite meet**. Sources agree on the finite-minimum idea. The manuscript uses positive real denominator parameters and +∞ at zero; the project uses natural parameters allowing zeros and real value0 at zero. Nonnegativity needs only nonnegative support weights; positivity is unnecessary. Historical derivative wording converts to the Taylor coefficient-support formulation. Arbitrary degree maps are not automatically multiplicative valuations; valuation context does not add a law beyond what the checked hypotheses supply.

## Phase 4a–4b — Generality

| Parameter / hypothesis | Current role | Verified expanded form / necessity |
|---|---|---|
| σ : Type u | polynomial variables | Arbitrary support index A:Type u in abstractLaw; not restricted to a finite variable set. |
| Fintype σ | Roth.weight global sum | Fixed by unchanged parent signature. No mechanical removal while retaining that parent is claimed. Finite coefficient support suffices in abstractLaw/projectedLaw, with no Fintype A. |
| ℝ coefficients | real polynomial | Arbitrary Semiring R:Type v in both checked abstract laws; no domain, nontriviality, characteristic zero or commutativity needed for support-degree bounds. Translation's CommSemiring requirements are separate. |
| P | translated finite-support input | Any AddMonoidAlgebra R A; no nonzero premise, including empty support. |
| α | point of translation | Only chooses input support; disappears from the abstract order law. Actual target bridge retains α. |
| r : σ→ℕ | nonnegative reciprocal weights | Any D:A→T with a support-local lower-bound premise. In projectedLaw, arbitrary D:A→ℝ with ∀d∈support,0≤D d. No additivity, injectivity or strictly-positive denominator premise is needed. |
| 0 and ℝ result | designated lower bound and zero-default projection | Any c:T with SemilatticeInf T and OrderTop T in abstractLaw, independent universe w; no linearity, addition or Zero required. Projected real nonnegativity retains fallback0. |
| Other premises | none | No hidden nonempty-variable, DecidableEq σ, P≠0 or positive-r hypothesis is introduced. |

Fresh isolated [exact source](../evidence/Roth.index_nonneg/index-nonneg-mathlib-executed.lean.txt) and [raw clean native success](../evidence/Roth.index_nonneg/index-nonneg-mathlib-receipt.json) actually compile both widened laws. The generic statement is:

```lean
-- [Semiring R] [SemilatticeInf T] [OrderTop T]
-- D : A → T, P : AddMonoidAlgebra R A, c : T
(∀ d ∈ P.coeff.support, c ≤ D d) → c ≤ AddMonoidAlgebra.infDegree D P
-- Existing proof term: Finset.le_inf_iff.mpr
```

Generality verdict: **STRICTLY NARROWER THAN STANDARD in expanded representation**, with four checked abstraction dimensions: support carrier, coefficient carrier, degree map and ordered target/lower bound. No unchanged-parent hypothesis weakening is asserted. The generic law already exists, so this does not justify YES-but-generalise-first. Moving the parent and sharing its projection bridge is a moderate representation refactor; cost does not decide the verdict.

## Phase 4c — All nine modern-idiom checks

| # | Question | Applies / concrete consequence |
|---|---|---|
|1| Typeclasses instead of bundled preambles | Yes: Semiring, SemilatticeInf and OrderTop expose existing finite-support order API and permit arbitrary semilattice-valued degrees. No new NonnegativeIndex class needed. |
|2| Sequences/metrics to filters | No topology, sequence or convergence argument. |
|3| Construction to universal property | Yes: greatest lower bound introduction is exactly the finite meet universal property, already Finset.le_inf_iff.mpr. It supplies any lower bound, not merely0. |
|4| Set with closure to bundled substructure | No closure predicate. Existing Finset coefficient support is the appropriate finite object. |
|5| Field/vector space to semiring/module | Yes: arbitrary Semiring coefficients compile. No real field facts enter the support-order law. Translation and reciprocal-weight construction are separately specialized. |
|6| Higher category | No useful higher-categorical content in a scalar inequality. Poset-limit language adds no downstream consequence beyond the finite-meet API. |
|7| Concrete ordered index to abstract structure | Yes: any SemilatticeInf+OrderTop and c. Nonlinearly ordered degrees and bounds use the same theorem; no minimum-attainment assumption needed. |
|8| Concrete-via-abstract diagnostic | Fires: original one-line body contains zero occurrences of `index` or `taylor`; only Real.sInf_nonneg, image introduction and weight_nonneg occur. It uses solely nonnegative values of the support image. The abstract finite-meet lower-bound law covers every finite coefficient-support construction. |
|9| False-generalization guard | Preserve empty support and all r including zero denominators. Reject dropping nonnegative-degree premise for arbitrary signed real D: a singleton support of degree−1 has negative minimum. Reject projecting top to arbitrary negative fallback, and reject claiming valuation multiplicativity for arbitrary D. No infinite-series attained-minimum claim is made. |

Modern idiom available: **yes, already in mathlib**. Separating support bounds from point/weight normalization permits the generic infDegree API and prevents repeated bespoke nonnegativity proofs. This is an organizational mathematical improvement with explicit support-degree downstream uses.

## Phase 4.5 — Infrastructure risk

All six rows — typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priority collision, universe infrastructure and coercion ambiguity — are **n/a — theorem**. This proof of Prop introduces no data, instances or coercions; parent-definition risks were assessed separately.

## Phase 4.6 — All five proof-strategy checks

| Question | Assessment |
|---|---|
| ε–δ / neighborhoods versus filters | n/a: no topology. |
| Elements versus algebraic inclusions | No ideal/submodule/subring inclusion. Pointwise support bounds are exactly the finite-inf premise. |
| Sequences versus nets | n/a: no analytic limits. |
| Construction versus universal property | Existing greatest-lower-bound introduction gives the abstract proof directly; no new universal-property class or construction. |
| Helpers mathlib should have | No missing nonnegative-support lower-bound law. Real.sInf_nonneg already proves the old order step; coe_inf′ and untopD handle projection. Shared parent normalization is an actual bridge proof, not a missing derivative theorem. |

**MATHLIB-IDIOMATIC** for the current real-sInf definition: the one-line proof uses its exact existing nonnegativity API. After parent migration use generic finite-inf introduction; a shared bridge makes that refactor clearer, without a new theorem contribution. No claim that the longer displayed representation check is a golfing improvement.

## Phase 5 — Five actual methods × three forms

[Exact formal requests and complete raw receipts](../evidence/Roth.index_nonneg/formal-search.json) preserve12 actual calls: Finder, Loogle, LeanSearch and local search on each current/standard/abstract form. [Current rg](../evidence/Roth.index_nonneg/rg-current.json), [standard rg](../evidence/Roth.index_nonneg/rg-literature.json), [abstract rg](../evidence/Roth.index_nonneg/rg-abstract.json) provide pinned source searches as the fifth method.

| Method | Current point-index nonnegative | Standard weighted order nonnegative | Abstract support-inf lower bound |
|---|---|---|---|
| Finder | Nonnegative derivative root weights, Mahler measure; rejected as different objects | weightedOrder bounds and weight lower bounds | infDegree and support-inf degree inequalities |
| Loogle | hasseDeriv/nonnegative pattern empty | weightedOrder family | **Finset.le_inf**, **Finset.le_inf_iff** and neighboring monotonicity |
| LeanSearch | derivative root weight and weighted homogeneous objects; not target | weighted-order surrounding API | **Finset.le_inf**, **Finset.le_inf′**, le_sInf |
| rg | Old target, three applications and Real.sInf_nonneg invocation | weightedOrder source and weight_nonneg | infDegree abbreviation, generated dual finite-inf law and WithTop projection |
| local | Project/scratch/history target hits | Pinned weightedOrder declarations | Broad le_inf name neighbors; local index unavailable |

All12 returned isError=false. Local index unavailable is a limitation, not absence evidence; scratch/history hits are not mathlib building blocks. Remote index revisions may differ from the pinned checkout. Positive signatures and proofs are freshly native-checked:

- `Finset.le_inf_iff` is generated by `@[to_dual ... le_inf_iff]` from `Finset.sup_le_iff`, `Mathlib/Data/Finset/Lattice/Fold.lean:99`; its .mpr is exactly support-bound introduction.
- `AddMonoidAlgebra.infDegree`, `Mathlib/Algebra/MonoidAlgebra/Degree.lean:624`, abbreviates finite coefficient-support infimum. Its generic lower-bound statement needs one existing law call.
- `Finset.le_inf'_iff`, generated dual at Fold:557, gives nonempty finite-inf bounds with explicit nonempty proof and degree-map arguments. `Finset.coe_inf'`, Fold:538, and `WithTop.untopD_coe` identify the real projection.
- `Real.sInf_nonneg` is defined at `Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:258`; signature `(∀x∈s,0≤x) → 0≤sInf s` exactly matches the old order engine. This theorem does not itself construct the project's weights.
- `WithTop.le_untopD_iff`, generated dual at `Mathlib/Order/WithBot.lean:468`, offers an alternative projection criterion requiring the fallback bound at top. Its signature was checked; the accepted proof uses the more explicit empty/nonempty split.

Conclusion: **found in mathlib as Finset.le_inf_iff.mpr on the more general infDegree parent**, with Real.sInf_nonneg as the old real-infimum analogue. No absence claim rests on a search failure.

## Phase 5.5 — All three statement-shape checks

Normal forms considered: (i) original0≤real sInf of weighted Taylor support, (ii) support-local lower-bound introduction for infDegree, (iii) nonnegative real projection of lifted support-inf, (iv) order-bottom nonnegativity for natural weightedOrder in ENat. The canonical abstract order content is already finite-inf introduction. This statement is an inequality, so an iff rewrite RHS orientation is n/a; the shared equality bridge sends the parent to generic infDegree.

Syntactic alternatives actually compiled: arbitrary bound c/degree map D over a semilattice; support-local nonnegative D with real zero-default projection; original all-P/all-r replacement through the actual bridge. Generic support membership is easiest to supply for a finite-inf consumer; the old no-premise point statement remains convenient at all three local callers. No new family of pairwise equivalences is proposed.

Superfluous arguments: σ/Fintype/ℝ/P/α/r are all fixed by the unchanged parent quantity; there are no proof hypotheses to remove. Generalized support-law removes Fintype and point data by changing representation, not by silently dropping them from the original signature. Nonnegative-degree premise is necessary in the expanded signed-real setting. No P≠0 or positivity assumption should be added.

Normal form **REFACTOR** to existing support-inf; syntactic generality **RESTATE** to existing generic lower-bound law for upstream consideration; unchanged-parent superfluous arguments **NONE**. Overall **RESTATE-BEFORE-SHIP**, which here would duplicate existing mathlib API.

## Phase 6.0 — Complete callers and inline audit

[Canonical inventory and fresh rg/git-grep receipts](../evidence/Roth.index_nonneg/complete-caller-search.json), [caller fragments/plans](../evidence/Roth.index_nonneg/callers.json), [direct kernel consumers](../evidence/Roth.index_nonneg/direct-consumers.json). Searches use --no-ignore across Roth/ and Roth.lean, independently cross-checked with tracked git-grep. Both yield4 source lines: declaration and3 applications in3 declarations. **Internal use count K=2 excluding declaring file, one distinct external file Theta**. Canonical audit independently finds3 direct kernel-value consumers. These are direct consumers, not opaque/transitive/simp dependency closure. The target is not tagged simp and is not dead code.

| Caller and exact reference | Usage | Refactor after shared parent bridge |
|---|---|---|
| Roth.index_eq_zero_iff, Index:100 | `(index_nonneg P α r).antisymm′ ...` | Supply projected finite-inf nonnegative bound at antisymmetry. Keep evaluation/attainment proof. |
| Roth.Θ_nonneg, Theta:110 | `exact index_nonneg _ _ _` | After Real.sSup_nonneg and destructuring indexSet, apply support-inf nonnegativity to translated mapped integer polynomial. Keep the surrounding supremum argument. |
| Roth.sum_max_sub_le_index_det, Theta:395 | `add_nonneg (index_nonneg _ _ _) ...` inside max_le | Supply projected support-inf nonnegativity as this add_nonneg premise. Keep weight_nonneg/h2, derivative estimates, determinant expansion and product/sum bounds. |

[Inline search](../evidence/Roth.index_nonneg/rg-inline.json) finds only the target and these uses for explicit0≤index/nonnegativity patterns; no independent re-derivation of the same law was found. This lexical observation is not a hidden-dependency closure proof. Three real consumers support a project convenience API, while the generic mathematical law already exists.

## Phase 6 — Actual composition and bridges

Attempt1, original spelling: the existing proof combines Real.sInf_nonneg and Set.forall_mem_image.mpr with **project** weight_nonneg. It is a valid project proof, **not** a ≤3-call mathlib-only replacement. Re-expanding the project weight introduces real denominator nonnegativity, finite sums and translation/support normalization; no false call count is assigned to those steps.

Attempt2, re-aimed parent: `Finset.le_inf_iff.mpr hD` proves `c ≤ AddMonoidAlgebra.infDegree D P` in **one existing mathlib call**. With c=0 and support-local nonnegative D, this is exactly the analogous nonnegativity law. Fresh [isolated source](../evidence/Roth.index_nonneg/index-nonneg-mathlib-executed.lean.txt) and [native success](../evidence/Roth.index_nonneg/index-nonneg-mathlib-receipt.json) prove it over arbitrary universes and Semiring/SemilatticeInf/OrderTop. ProjectedLaw separately handles nonempty support by coe_inf′/untopD_coe/le_inf′_iff, and empty support by inf_empty/untopD_top. There is no hidden P≠0 assumption.

I independently inspected the parent's [isolated complete mathlib bridge](../evidence/Roth.index_nonneg/index-expanded-mathlib-executed.lean.txt) and [raw success](../evidence/Roth.index_nonneg/index-expanded-mathlib-receipt.json): finsetBridge distinguishes empty support and normalizes nonempty inf′ to real csInf image; denominatorBridge expands reciprocal Finsupp.weight. The [actual bridge](../evidence/Roth.index_nonneg/index-consumers-executed.lean.txt), [receipt](../evidence/Roth.index_nonneg/index-consumers-receipt.json), [fully expanded bridge](../evidence/Roth.index_nonneg/index-expanded-bridge-executed.lean.txt), [receipt](../evidence/Roth.index_nonneg/index-expanded-bridge-receipt.json) match index for **all P and all r**, including zero polynomial and mixed zero denominators. They are newly proved nondefinitional representation bridges, not existing mathlib replacement calls.

The fresh [actual originalReplacement](../evidence/Roth.index_nonneg/index-nonneg-target-executed.lean.txt) and [complete native success](../evidence/Roth.index_nonneg/index-nonneg-target-receipt.json) rewrite IndexConsumers133.targetBridge then perform the explicit support split, use finite-inf introduction and Roth.weight_nonneg. They never invoke Roth.index_nonneg or a downstream index law. This has **more than three normalization/building-block steps** and includes project API. Conclusion for the bare old spelling: **NOT-COMPOSABLE as a claimed ≤3-call mathlib term**. The deciding result is the one-call re-aim hit, independently bridged.

Fresh [whole Index and whole Theta replay](../evidence/Roth.index_nonneg/index-nonneg-callers-executed.lean.txt) and [complete native receipt](../evidence/Roth.index_nonneg/index-nonneg-callers-receipt.json) replace all3 applications: Index's local replacement is derived from originalReplacement; both Theta applications directly call originalReplacement. Target identifier index_nonneg is absent from the accepted replay. Replacement and all3 consuming declarations print standard axioms; no recovered sorryAx, unsafe proof, native_decide or raised limits. A preparation-only width guard caught a103-character caller line, wrapped before the first native execution. Prepared and executed sources are retained separately; **no rejected native attempts** occurred.

A hypothetical closing simp[defs] alone would have Phase6b's BORDERLINE status. It is not the basis here: ModeB explicitly requires **NO-mathlib-has-it** when the already-existing parent has the analogous law, after independently verifying law and representation bridge. Both checks passed. No cost-based downgrade or automatic verdict inheritance is used.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it** via `Finset.le_inf_iff.mpr` on `AddMonoidAlgebra.infDegree`. Finite-inf introduction already accepts any support-local lower bound; nonnegativity is its c=0 instance. The whole old form retains project normalization rather than becoming definitionally equal to the generic order law. All-P/all-r actual bridge and full consumer replay establish compatibility, without claiming the bridge as existing API.

First migrate the parent to projected infDegree or retain one shared project-local bridge. Replace the3 applications at Index:100, Theta:110 and Theta:395 with the generic finite-inf lower-bound law after projection. Supply weight_nonneg (or its expanded sum/reciprocal proof) as the support-local premise, handle empty support by fallback0, and retain each caller's surrounding steps listed above. Do not duplicate the normalization bridge at all3 sites. Delete index_nonneg after these replacements if removing wrappers; the replay verifies all argument instantiations and placements.

Alternative destination: **Roth/Index.lean project-local manuscript convenience API**, where the compact no-premise statement is useful to the3 consumers. No Archive or satellite library is needed for this specialized elementary spelling. No upstream PR is proposed, so YES-only PR path/title/grouping/reviewer-selection steps are n/a. Neighboring index laws need their own re-aim checks.

## Phase 8 — Handoff

All required phases complete, verification unresolved=[], root acceptance pending. [Assessment](../evidence/Roth.index_nonneg/assessment.json), [verification](../evidence/Roth.index_nonneg/verification.json), [overview entry](../evidence/Roth.index_nonneg/overview-entry.json), [current manifest](../evidence/Roth.index_nonneg/copy-manifest.json), [portable read-only validator](../evidence/Roth.index_nonneg/validate.py). The validator checks fresh17 source/pin hashes, current artifact hashes/bytes and portable links, exact canonical293 name order including private names, target-scoped native audit and standard axioms, all3 callers, all formal and literature channels, and credential hygiene. Current copy-manifest remains authoritative; integration-only root-acceptance.json is exempt from worker manifest coverage.
