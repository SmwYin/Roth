# Full /mathlibable assessment — `MvPolynomial.hasseDeriv`

**Category: YES-add-as-is. All assessment gates complete; independent root acceptance pending.** This is the characteristic-free multivariate Hasse derivative as an `R`-linear endomorphism, with arbitrary variables. The univariate `Polynomial.hasseDeriv` is a model and a compatibility target, not a replacement for the arbitrary-variable operator. This assessment is confined to the definition at `Roth/HasseDeriv.lean:57`; it does not assign verdicts to its non-glue API theorems.

Assessment date: 2026-10-26. Assigned branch: `ramin-cleanup`. Production source snapshot: `99f19fda4b3cbee38fc0d31af76075834f5cc265`; published input checkpoint: `0db8fd0`. Mathlib pin: `5ed2965256430c3649e86755f9576b54eca72435`, Lean v4.34.0. No production source or pin was edited. No Git operation was performed by this worker.

Links use the intended tracked layout: report `.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv.md`, supporting directory `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/`. The supporting directory contains `assessment.json`, `evidence/` and `probes/`; the report is copied separately. Scripts run from the project root, with paths derived from their own location. Historical tool receipts preserve the actual session paths.

## Phase 0 — Doctor

- **Baseline build PASS:** exit 0, 2467 jobs, reused from the existing shared baseline. Independently rechecked all **17/17 source/pin hashes** against that baseline; no redundant build. [Baseline](../evidence/MvPolynomial.hasseDeriv/evidence/baseline-build.txt), [manifest](../evidence/MvPolynomial.hasseDeriv/evidence/input-manifest.json), [comparison](../evidence/MvPolynomial.hasseDeriv/evidence/baseline-hash-verification.json).
- **Declaration resolves:** public `noncomputable def`, unique qualified target at `Roth/HasseDeriv.lean:57`. The actual native hover returned its type and no diagnostics. [Raw hover receipt](../evidence/MvPolynomial.hasseDeriv/evidence/target-hover.json).
- **No `sorry`, new axiom declaration, unsafe/native trust, or limit raise** in the target or proposed scratch experiments. Compiler axiom result: only standard `propext`, `Classical.choice`, `Quot.sound`. [Exact source](../evidence/MvPolynomial.hasseDeriv/probes/TargetRisk.lean), [raw native receipt](../evidence/MvPolynomial.hasseDeriv/evidence/target-risk-lsp.json): `partial=false`, `success=true`, zero errors, zero failed dependencies. A scratch-only missing-module-docstring style warning is retained; no linter suppression was introduced.
- Module: defines multivariate Hasse derivatives, coefficient and composition rules, partial-derivative relations and compatibility with the univariate operator.

Actual elaborated type from the native hover:

```lean
MvPolynomial.hasseDeriv.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
    [CommSemiring R] (d : σ →₀ ℕ) :
    MvPolynomial σ R →ₗ[R] MvPolynomial σ R
```

The two universes are independent. In contrast with `hasseCoeff`, **`R` and `[CommSemiring R]` really occur in this declaration's elaborated type**.

## Phase 1 — Comprehend

For a finitely supported natural multiindex `d`, the Hasse derivative `Δ_d` is the coefficient-linear operator determined by
`Δ_d(a X^k) = (∏_{j ∈ supp(d)} binom(k_j,d_j)) a X^(k-d)`.
If some `d_j > k_j`, the binomial factor is zero; thus the truncated subtraction used for natural exponents does not produce a spurious surviving term. Extending this rule linearly gives an operator on polynomials over every commutative semiring, including positive characteristic, without division by factorials.

| Parameter / hypothesis | Mathematical role |
|---|---|
| `{σ : Type u}` | Arbitrary variable set, possibly infinite or empty |
| `{R : Type v}` | Arbitrary coefficient carrier |
| `[CommSemiring R]` | Coefficient addition, multiplication, natural casts and the existing `MvPolynomial σ R`/module structures |
| `d : σ →₀ ℕ` | Differentiation multiplicities, with finite support |

No further hypotheses. Conclusion (mathematics): the `R`-linear Hasse differential operator of multiorder `d`. Conclusion (Lean): n/a, definition; the displayed result type is a bundled linear map. This is not an analytic/Fréchet derivative and is not an ordinary Leibniz derivation when the order exceeds one.

## Phase 2 — Preliminary checks

**Size: BIG.** It introduces a standard named mathematical operator and the main definition underpinning the module's principal identities. This classification does not reduce the exhaustive search width.

**Body: three substantive source lines; MULTI-LINE.** [Exact excerpt](../evidence/MvPolynomial.hasseDeriv/evidence/target-excerpt.lean). Counting lines is not the substantive reason to keep the name: even if formatted as one line, the semantic/API exemption applies.

| One-line exemption, assessed additionally | Applies? | Actual evidence |
|---|---|---|
| Avoid defeq abuse | No special exemption needed | It is an ordinary semireducible definition; `hasseDeriv_monomial` and `hasseDeriv_apply` explicitly unfold it. No deliberately sealed barrier is evidenced. |
| Avoid typeclass diamonds | No | It creates neither a new type nor an instance. |
| Semantic intent / API stability | **Yes** | `Roth.genWronskian`, `Roth.kronHasse`, `MvPolynomial.coeff_taylor`, and `Roth.index_sub_weight_le_index_hasseDeriv` use the operator as the same named object; the theorem API characterizes it independently of its coefficient-storage implementation. There are 41 caller declarations outside this file. |

Conclusion: MULTI-LINE, with an independently established semantic exemption. The previous standalone `hasseCoeff` NO verdict is not inherited: that scalar alias and this standard family of linear endomorphisms are different assessment targets.

## Phase 3 — Exhaustive literature protocol

The following are actual searches/reads, including empty results and failed fetches. Curated search observations (exact requests, titles, URLs, outcomes and concise original analysis) are in [web1](../evidence/MvPolynomial.hasseDeriv/evidence/web1.json), [web2](../evidence/MvPolynomial.hasseDeriv/evidence/web2.json), [web3](../evidence/MvPolynomial.hasseDeriv/evidence/web3.json), [web4](../evidence/MvPolynomial.hasseDeriv/evidence/web4.json), and the separately linked channel logs. Only original concise analysis is used below; mathematical standard-form claims rely on the primary manuscript/papers, not search aggregators or an unanswered question.

| Channel | Actual query / inspection | Outcome | Standard form / significance |
|---|---|---|---|
| Web | `multivariate Hasse derivative definition Taylor coefficients arbitrary field` | Batch results returned | Standard monomial/Taylor definitions; primary commutative-ring and higher-derivation sources. |
| Web | `Hasse Schmidt derivation polynomial ring commutative ring divided derivatives multi index` | Batch results returned | Standard monomial/Taylor definitions; primary commutative-ring and higher-derivation sources. |
| Web | `hyperderivatives divided power derivatives multivariate polynomial definition` | Batch results returned | Standard monomial/Taylor definitions; primary commutative-ring and higher-derivation sources. |
| nLab | `site.ncatlab.org Hasse Schmidt derivation higher derivative` | Batch results returned | Contextual nLab/MO/recent-paper results; no individual-query completeness inferred. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivation differential operators polynomial` | Batch results returned | Contextual nLab/MO/recent-paper results; no individual-query completeness inferred. |
| MathOverflow | `site:mathoverflow.net Hasse derivative polynomial multivariate` | Batch results returned | Contextual nLab/MO/recent-paper results; no individual-query completeness inferred. |
| recent arXiv | `site:arxiv.org Hasse derivatives multivariate 2022 2023 2024 2025` | Batch results returned | Contextual nLab/MO/recent-paper results; no individual-query completeness inferred. |
| Stacks | `"Hasse" site:stacks.math.columbia.edu` | Batch results returned | Mostly nLab/other Hasse topics; isolated follow-ups below avoid false channel coverage. |
| nLab | `"Hasse" site:ncatlab.org/ncatlab` | Batch results returned | Mostly nLab/other Hasse topics; isolated follow-ups below avoid false channel coverage. |
| recent arXiv | `"Hasse derivative" "2024" site:arxiv.org` | Batch results returned | Mostly nLab/other Hasse topics; isolated follow-ups below avoid false channel coverage. |
| recent arXiv | `"multivariate Hasse" "2022" site:arxiv.org` | Batch results returned | Mostly nLab/other Hasse topics; isolated follow-ups below avoid false channel coverage. |
| recent arXiv | `site:arxiv.org/abs/ "Hasse" "multivariate" "2024"` | Empty | No result for this exact 2024-specific query; recent 2022/2023 papers inspected separately. |
| Stacks | `site:stacks.math.columbia.edu "Hasse" "Schmidt"` | Empty | No direct indexed Hasse–Schmidt result; related tag 07GK opened separately. |
| nCatLab | `site:ncatlab.org/ncatlab/ "Hasse-Schmidt"` | Batch results returned | Returns nLab and graded-bimonoid perspective; no separate categorical replacement. |
| recent arXiv | `"Fast Multivariate Multipoint Evaluation over All Finite Fields" arxiv` | Batch results returned | Primary 2022 application identified; characteristic-free formula assessed using manuscript and published Definition3.4. |
| Web | `"Hasse derivatives" "commutative semiring"` | Batch results returned | Primary 2022 application identified; characteristic-free formula assessed using manuscript and published Definition3.4. |
| ChatGPT MCP | Capability discovery for `ask_chatgpt_math` | **n/a: unavailable** | No consultation claimed; other channels unchanged. |
| Local references | `rg -n 'Delta\|derivative\|derivatives\|Hasse' .mathlib-quality/references/clean.tex`; read lines 119–155 | Yes | Exact semiring monomial definition and finite-support linear-map implementation. |
| nLab direct page | Hasse–Schmidt derivative | Indexed definition read; direct XHTML fetch unsupported | Several-indeterminate commutative-rig form; mandatory secondary channel, not primary mathematical authority. |
| Stacks direct primary source | [Tag 07GK](https://stacks.math.columbia.edu/tag/07GK) | Opened | Divided-power ideal structure is related but is not this polynomial endomorphism. |
| MathOverflow direct page | [Question 510672](https://mathoverflow.net/questions/510672/hasse-derivative-and-laurent-denis-lemma) | Opened | Context only; initial suggestion is corrected on the page, no theorem inferred. |
| Recent arXiv direct records | [2305.04537](https://arxiv.org/html/2305.04537v1), [2205.00342](https://arxiv.org/abs/2205.00342) | Opened full 2023 HTML and full 2022 HTML via its actual abstract-page link | Both inside the five-year interval 2021-10-26–2026-10-26. |

[One record per actual web query](../evidence/MvPolynomial.hasseDeriv/evidence/literature-queries.json) also preserves the original batch association and relevant result URLs. The separate nCatLab channel is **n/a as a required restatement** after the brief searches: this target is a coordinate operator, and the related categorical interpretation supplies no mechanical semantic-preserving replacement. All other eight channels were run, except optional unavailable ChatGPT.

Primary mathematical anchors:

- [Bhargava et al., *Fast Multivariate Multipoint Evaluation over All Finite Fields*](https://doi.org/10.1145/3652025), Definition 3.4, defines the derivative by extracting the `z^d` coefficient of `f(x+z)` over a commutative ring. The search service returned that definition; direct DOI opening returned 403. Following the actual HTML link on the [2022 arXiv record](https://arxiv.org/abs/2205.00342) then opened the [primary v1 full text](https://arxiv.org/html/2205.00342v1): §3.2, Definition 3.4 gives that coefficient characterization and property 3.5 gives its binomial-weighted monomial-sum formula. [Curated access/locator receipt](../evidence/MvPolynomial.hasseDeriv/evidence/recent-html.json). An earlier guessed v3 URL returned 404 and is not cited as read text.
- [Narváez Macarro, *Hasse–Schmidt derivations, divided powers and differential smoothness*](https://www.numdam.org/item/AIF_2009__59_7_2979_0/) (2009), and [Barajas, *High-order derivations of the Hasse–Schmidt algebra*](https://arxiv.org/html/2305.04537v1) (2023), establish the surrounding commutative-algebra framework. Barajas Definition 1.1 concerns families of linear maps and a higher product law; it is not identical to this particular coordinate operator.
- Takloo-Bighash–Yin's local primary manuscript §1 gives precisely the characteristic-free monomial normalization assessed here. The mathematical identification of the monomial and translated-coefficient definitions follows by the binomial theorem; that comparison is analysis of the definitions, not a claim that a new Lean equivalence theorem was verified in this assessment.

**Literature summary.** Concept: multivariate Hasse derivative / divided differential operator, a particular coordinate Hasse–Schmidt family. Sources agree on the normalization; field, commutative-ring and commutative-semiring presentations differ in scope, not factorial scaling. Finite-variable sources are encompassed by arbitrary `σ` with finitely supported exponents. The current declaration already uses the characteristic-free semiring form from the local source. General Hasse–Schmidt derivations on arbitrary algebras and divided-power ideals are adjacent abstractions, not stronger signatures obtained by dropping one assumption of this operator.

## Phase 4 — Generality

| Parameter / assumption | Current Lean form | Standard-form comparison | Weakening conclusion |
|---|---|---|---|
| Variables | `σ : Type u`, no extra instance | Literature commonly fixes finitely many variables | Already broader; handles any variable type without `Fintype`, `Finite`, `DecidableEq`, `Nonempty` or `Unique`. |
| Coefficients | `R : Type v` | Arbitrary commutative ring/semiring in characteristic-free definitions | Already arbitrary, independent universe. |
| Coefficient laws | `[CommSemiring R]` | Local manuscript explicitly gives this scope | Needed even to form pinned `MvPolynomial σ R` (Basic:81); no characteristic-zero, domain, field, subtraction or invertibility assumption. |
| Derivative index | `σ →₀ ℕ` | Nonnegative finite multiindex / multiset of differentiated variables | This represents finite differential order; arbitrary non-finitely-supported functions are not finite-order polynomial differential operators. |
| Codomain/bundling | `MvPolynomial σ R →ₗ[R] MvPolynomial σ R` | Coefficient-linear operator | Appropriate: retains additivity and scalar linearity for generic map/linear-map API. |

**Generality verdict: MAXIMALLY GENERAL for this standard polynomial operator and pinned `MvPolynomial` API.** No literature-required weakening found; no successful weakening is proposed. The candidate `[CommSemiring R] → [Semiring R]` is blocked by the domain type itself, not a guessed proof dependency. Actual rejected-weakening probe is complete: `#check_failure MvPolynomial σ S` with explicitly bound `σ` and `[Semiring S]` reports missing `CommSemiring S`. [Executed isolated source](../evidence/MvPolynomial.hasseDeriv/probes/MathlibOnly.lean), [raw complete receipt](../evidence/MvPolynomial.hasseDeriv/evidence/mathlib-only-lsp.json). Rebuilding the polynomial type for noncommutative coefficients or replacing it by an arbitrary algebra is a different foundational development, not a mechanically verified generalization ticket. Cost is not used to select the verdict.

### Phase 4c — All nine modern-idiom questions

| # | Question | Applies? / answer | Reformulation and downstream |
|---|---|---|---|
| 1 | Preambles → typeclasses | No change | `CommSemiring` is already a typeclass; the operator is already bundled. |
| 2 | Sequences/metrics → filters | No | Pure finite algebra; no topology. |
| 3 | Construction → universal-property class | No required restatement | `Finsupp.lsum` already uses linear extension from coefficients. A universal Hasse–Schmidt algebra class describes a different, larger object; it would not remove the need for coordinate components. |
| 4 | Closure predicate → bundled substructure | No | No ad hoc closure predicate; output already a `LinearMap`. |
| 5 | Field/vector space → module/(semi)ring | Already done | `CommSemiring R`/`R`-linear map covers torsion and positive characteristic. Replacing by `Derivation` would impose the wrong product rule on higher orders. |
| 6 | 1-category → higher category | No | No categorical theorem or construction. The brief categorical-channel check supplies no concrete mathlib downstream improvement. |
| 7 | Concrete index → arbitrary monoid | No | Natural multiplicities, subtraction and binomial coefficients encode differentiation order. A generic additive monoid has no replacement for these data; changing it is not the same object. |
| 8 | Concrete witness hides abstract proof | No | Explicit body diagnostic: no special field, dimension, polynomial or other named concrete witness appears; no initial `rw` hides one. `σ`, `R` and `d` are generic throughout the three-line construction. Zero occurrences of a concrete witness is inapplicability, not evidence that an arbitrary linear operator should replace the Hasse operator. |
| 9 | False-generalisation guard | No accepted widening changes meaning | No widening proposed. Reject calling an arbitrary higher derivation, divided-power ideal or ordinary `Derivation` the same coordinate Hasse derivative. Keep the original semiring/multiindex/operator semantics. |

**Modern-idiom verdict: no further required mathematical reorganization.** The current type already makes the useful modern move: characteristic-free algebra and a bundled linear operator. A translated-polynomial coefficient characterization would complement the API rather than weaken or replace this operator's signature.

### Phase 4.5 — Diamond / definitional-equality risk

Actual [risk/type/probe source](../evidence/MvPolynomial.hasseDeriv/probes/TargetRisk.lean) and [complete native diagnostic receipt](../evidence/MvPolynomial.hasseDeriv/evidence/target-risk-lsp.json) pass: `partial=false`, `success=true`, no errors or failed dependencies. The final warm poll took 530ms; this is not claimed as the initial import-loading time.

| Risk | Verdict | Evidence / rationale |
|---|---|---|
| Typeclass diamond | NONE | Target introduces no class, type, instance or alternative module action. Its result uses the existing coefficientwise `Module R (MvPolynomial σ R)`; the instance originates from `AddMonoidAlgebra`'s module transport, as pinned Module.lean:59–75 shows. Actual `#synth` selects `AddMonoidAlgebra.instModule`. |
| Reducibility leak | LOW | Ordinary `noncomputable def`, no reducibility attribute. The body is explicitly unfoldable; equality to the displayed body by `rfl` compiled. `noncomputable` does not install a new typeclass or coercion. |
| Noncanonical unfolding | LOW | `hasseDeriv_monomial`/`hasseDeriv_apply` explicitly unfold the definition; most downstream proofs use `coeff_hasseDeriv`. No simp attribute on the definition causes global raw expansion. Truncated subtraction is documented and zeroed by the binomial coefficient. |
| Instance-priority collision | NONE | Not an instance; no priority registration. Ordinary linear-map/module instances are reused, not redeclared. |
| Universe issues | NONE | Actual hover shows independent `u_1,u_2`. Generic universes and concrete Type 0/Type 1 applications all elaborated; no finite/decidable variable constraint in source or type. |
| Coercion ambiguity | NONE | Output is the existing `LinearMap` structure and uses its standard function coercion; no `CoeFun`/`CoeSort` is registered. Explicit coercion-to-function probe elaborates to `fun d ↦ ⇑(hasseDeriv d)`. |

**Overall risk: LOW** with all requested risk probes passed; no HIGH row identified. The low risk is normal definitional exposure of a noncomputable coefficient extension, mitigated by the monomial/coefficient API. No new instance path is proposed.

### Phase 4.6 — Proof strategy

| # | Question | Applies? | Alternative / cost |
|---|---|---|---|
| 1 | Topology via neighborhoods → filters | No | No topology. |
| 2 | Element algebra → substructure inclusion | No | This constructs a linear endomorphism; not an inclusion proof. |
| 3 | Sequence analysis → nets | No | No analysis. |
| 4 | Object construction → universal property | Already uses the relevant generic extension | `Finsupp.lsum` extends a family of coefficient-linear monomial maps; no hand-written additivity/scalar proof. |
| 5 | Missing helper mathlib should supply | No helper needed to construct this operator | The substantive gap is the named multivariate Hasse operator and its characterization/API, rather than a missing finite-sum manipulation. |

**Strategy: MATHLIB-IDIOMATIC.** It mirrors pinned `Polynomial.hasseDeriv`, itself a linear monomial extension. The `AddMonoidAlgebra.coeffLinearEquiv` bridge follows the current coefficient-storage representation. There is no proof body with unnecessary element chasing to refactor. A Taylor-coefficient implementation is a valid future alternative but needs its characterization proof; no unverified equivalence is passed off as a three-call replacement.

## Phase 5 — Five actual mathlib search methods

[Exact requests](../evidence/MvPolynomial.hasseDeriv/evidence/search-requests.json) retain all arguments. External search indices are aids; the pinned source and compiler decide candidate applicability. The local-name API explicitly returned `index: unavailable` alongside source-fallback matches, so it is not treated as an exhaustive elaborated index.

| Method | Actual queries | Observed results and assessment |
|---|---|---|
| A Lean-Finder | `multivariate Hasse derivative linear map polynomial binomial coefficients`; `Multivariate polynomial higher divided Hasse derivative via coefficient of f(X+Y); linear maps on finitely supported monomials` | Returns `Polynomial.hasseDeriv`, its monomial/coefficient/composition API and `MvPolynomial.mkDerivationₗ`; none is the arbitrary-multiindex operator. [First](../evidence/MvPolynomial.hasseDeriv/evidence/finder1.json), [second](../evidence/MvPolynomial.hasseDeriv/evidence/finder2.json). |
| B Loogle | `MvPolynomial _ _ →ₗ[_] MvPolynomial _ _`; `"hasseDeriv"` | First returns weighted homogeneous components; second univariate Hasse API. A linear-map type alone does not identify the operator. [First](../evidence/MvPolynomial.hasseDeriv/evidence/loogle1.json), [second](../evidence/MvPolynomial.hasseDeriv/evidence/loogle2.json). |
| C LeanSearch | Monomial/binomial description; broader arbitrary-variable semiring Taylor-coefficient description | Returns univariate Hasse derivative, Laurent-series Hasse derivative, ordinary `pderiv`/`mkDerivation` API. [First](../evidence/MvPolynomial.hasseDeriv/evidence/leansearch1.json), [second](../evidence/MvPolynomial.hasseDeriv/evidence/leansearch2.json). |
| D Source grep | Full untruncated `\bMvPolynomial\.hasseDeriv\b` over all Mathlib; whole-library `hasse\|hyperderiv\|divided.*deriv\|deriv.*divided`; `Taylor\|taylor\|Hasse\|hasse\|hyperderiv\|divided.*deriv` in both multivariate-polynomial directories | Exact and multivariate-topic searches exit 1, no textual hit. Whole-library search retains univariate and Laurent-series hits plus unrelated Hasse diagrams/arithmetic. [Exact](../evidence/MvPolynomial.hasseDeriv/evidence/grep-full.json), [wide](../evidence/MvPolynomial.hasseDeriv/evidence/grep-wide.json), [multivariate](../evidence/MvPolynomial.hasseDeriv/evidence/grep-mv.json). No truncation of stored grep results. |
| E Name-pattern API | `hasseDeriv`; `taylor` | Returns the project target and project Taylor API plus mathlib univariate/Laurent names. Project results are explicitly excluded from claims about mathlib availability; source fallback is useful despite unavailable index. [Hasse](../evidence/MvPolynomial.hasseDeriv/evidence/local1.json), [Taylor](../evidence/MvPolynomial.hasseDeriv/evidence/local2.json). |

Searched both current monomial-linear form and literature's translated-coefficient/characteristic-free form. There is no separate accepted modern restatement left unsearched.

Pinned-source candidate verification ([source identities](../evidence/MvPolynomial.hasseDeriv/evidence/source-identities.json)):

- `Polynomial.hasseDeriv`, `Mathlib/Algebra/Polynomial/HasseDeriv.lean:59`: index `ℕ`, domain/codomain `Polynomial R`, over `Semiring R`; cannot automatically accept an arbitrary `σ →₀ ℕ` or `MvPolynomial σ R`.
- `MvPolynomial.pderiv`, `Mathlib/Algebra/MvPolynomial/PDeriv.lean:61`: one variable `i : σ`, bundled ordinary `Derivation`; repeated application produces factorial multiples, with no factorial inverse available over arbitrary semirings.
- `MvPolynomial.mkDerivationₗ`, `Mathlib/Algebra/MvPolynomial/Derivation.lean`: constructs first-order derivations from variable images, not the higher divided normalization.
- `LaurentSeries.hasseDeriv`, `Mathlib/RingTheory/LaurentSeries.lean:118`: natural-order univariate series operator with additive-group coefficients; different domain and coefficient hypotheses.
- `Finsupp.lsum`, `Mathlib/LinearAlgebra/Finsupp/LSum.lean:97`, and `AddMonoidAlgebra.coeffLinearEquiv`, `Mathlib/Algebra/MonoidAlgebra/Module.lean:75` (generated additive counterpart): generic linear-extension/storage primitives. They can construct the target once its specific binomial kernel is supplied, but they do not already express Hasse differentiation.

**Search conclusion: partial matches and generic construction primitives, no verified existing multivariate Hasse operator.** The isolated pinned-environment compiler gate **PASS**: `#check_failure MvPolynomial.hasseDeriv` reports unknown constant, direct univariate replacement reports a linear-map domain/type mismatch, the positive `exact?` control succeeds, the full monomial-specification `fail_if_success exact?` passes, and the explicit generic construction with its monomial proof elaborates successfully. [Source](../evidence/MvPolynomial.hasseDeriv/probes/MathlibOnly.lean), [raw native receipt](../evidence/MvPolynomial.hasseDeriv/evidence/mathlib-only-lsp.json): `partial=false`, `success=true`, `timed_out=false`, zero errors/warnings or failed dependencies, elapsed 4922ms. This is a scoped assessment of searched/checked routes, not a mathematical proof that no definable equivalent can exist anywhere in the library.

## Phase 5.5 — Statement shape

**Normal form.** Equivalent mathematical presentations are (1) monomial/binomial linear extension, (2) `z^d` coefficient of `P(X+z)`, and (3) factorial-normalized iterated partials over a `ℚ`-algebra. The third changes assumptions and is not the universal normal form. Pinned mathlib has a canonical univariate `Polynomial.hasseDeriv` and ordinary multivariate `pderiv`, but no verified canonical arbitrary-multiindex operator. Propose `MvPolynomial.hasseDeriv d : … →ₗ[R] …` as the characteristic-free normal form, with monomial/coefficient/translated-polynomial characterizations around it. For an equality exposing its implementation, put the linear-extension expression on the RHS; no iff orientation is at issue for a definition.

**Syntactic alternatives inspected:** unbundled function `MvPolynomial σ R → MvPolynomial σ R`; existing bundled linear endomorphism; `Module.End R (MvPolynomial σ R)` notation; translated-polynomial coefficient definition. Choose the current `→ₗ[R]` form: pointwise callers use its coercion, while `map_sum`, scalar compatibility and endomorphism composition are available without reproving linearity. An unbundled function would discard useful structure. `Module.End` is an equivalent display, not a mathematical improvement. The Taylor form requires an equivalence proof and is not asserted as an already compiled alternative in this report.

| Argument / class | Essentially needed? | Audit |
|---|---|---|
| `σ` | Yes | Coordinate type for both input polynomial and differential order; arbitrary already. |
| `R` | Yes | Coefficient type and scalar type; arbitrary already. |
| `[CommSemiring R]` | Yes in this API | Required by pinned `MvPolynomial`; natural scalar factors and coefficient-linear extension use its structures. |
| `d` | Yes | Distinguishes all derivative orders; order zero, positive order and different coordinate orders are different maps. |

**Normal form: OK. Syntactic generality: OK. Superfluous arguments: NONE. Overall: SHIP-AS-STATED.** “As stated” concerns the mathematical type/operator; it does not approve all surrounding file imports, helper names or unassessed theorems for a PR.

## Phase 6 — Complete caller and composition checks

**Internal use count excluding the declaring file: 72 code-bearing lines, 79 target occurrences, 41 distinct caller declarations, 8 files.** Within the declaring file: 20 lines / 29 occurrences / 18 caller declarations. Whole project: 92 lines / 108 occurrences / 59 caller declarations. Repeated occurrences in one line are not counted as separate independent callers. No external-to-repository consumer was established.

[Complete caller evidence](../evidence/MvPolynomial.hasseDeriv/evidence/call-sites.json) and [portable comment-stripping/caller script](../evidence/MvPolynomial.hasseDeriv/evidence/audit-sources.py) preserve every actual code-bearing line and caller name. Qualified `Polynomial.hasseDeriv` and unqualified uses in the univariate `Wronskian.lean` are excluded after source disambiguation. Caller boundaries use the corrected inventory, not its original named-assignment parser. This is a direct written-reference audit, not a claimed opaque/simp dependency closure.

| File:line | Caller | Actual code excerpt |
|---|---|---|
| `Roth/CoeffNorm.lean:136` | `Roth.abs_coeff_hasseDeriv_le` | `\|(((hasseDeriv d P).coeff e : ℤ) : ℝ)\| ≤ 2 ^ (∑ j, r j) * B := by` |
| `Roth/CoeffNorm.lean:149` | `Roth.normOne_hasseDeriv_le` | `(hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P := by` |
| `Roth/CoeffNorm.lean:247` | `Roth.degreeOf_det_hasseDeriv_le` | `degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j := by` |
| `Roth/CoeffNorm.lean:261` | `Roth.abs_coeff_det_hasseDeriv_le` | `\|(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)\| ≤` |
| `Roth/CoeffNorm.lean:265` | `Roth.abs_coeff_det_hasseDeriv_le` | `calc _ ≤ normOne (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det :=` |
| `Roth/GenWronskian.lean:34` | `Roth.genWronskian` | `(Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det` |
| `Roth/GenWronskian.lean:49` | `Roth.genWronskian_eq_zero_of_not_linearIndependent` | `congrArg (hasseDeriv (D μ)) hg` |
| `Roth/GenWronskian.lean:146` | `Roth.kronHasse` | `fun P ↦ kronecker k (hasseDeriv d P)` |
| `Roth/GenWronskian.lean:216` | `Roth.exists_hasseDeriv_kronecker_eq_sum` | `Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P) := by` |
| `Roth/GenWronskian.lean:241` | `Roth.wronskian_kronecker_eq_sum_aux` | `∑ d ∈ s μ, c μ d * kronecker k (hasseDeriv d (φ ν))) : wronskian (fun ν ↦ kronecker k (φ ν)) =` |
| `Roth/GenWronskian.lean:245` | `Roth.wronskian_kronecker_eq_sum_aux` | `det_sum_rows s c (fun μ d ν ↦ kronecker k (hasseDeriv d (φ ν)))` |
| `Roth/HasseDeriv.lean:67` | `MvPolynomial.hasseDeriv_monomial` | `hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by` |
| `Roth/HasseDeriv.lean:68` | `MvPolynomial.hasseDeriv_monomial` | `simp [hasseDeriv]` |
| `Roth/HasseDeriv.lean:74` | `MvPolynomial.hasseDeriv_apply` | `hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by` |
| `Roth/HasseDeriv.lean:75` | `MvPolynomial.hasseDeriv_apply` | `simp [hasseDeriv, sum_def]` |
| `Roth/HasseDeriv.lean:90` | `MvPolynomial.coeff_hasseDeriv` | `(hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by` |
| `Roth/HasseDeriv.lean:112` | `MvPolynomial.hasseDeriv_zero_apply` | `theorem hasseDeriv_zero_apply (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by` |
| `Roth/HasseDeriv.lean:120` | `MvPolynomial.hasseDeriv_zero` | `theorem hasseDeriv_zero : hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] _) :=` |
| `Roth/HasseDeriv.lean:126` | `MvPolynomial.hasseDeriv_C` | `theorem hasseDeriv_C {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by` |
| `Roth/HasseDeriv.lean:135` | `MvPolynomial.hasseDeriv_map` | `(P : MvPolynomial σ R) : hasseDeriv d (map f P) = map f (hasseDeriv d P) := by` |
| `Roth/HasseDeriv.lean:145` | `MvPolynomial.hasseDeriv_rename` | `hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) := by` |
| `Roth/HasseDeriv.lean:176` | `MvPolynomial.hasseDeriv_hasseDeriv` | `hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by` |
| `Roth/HasseDeriv.lean:186` | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | `(P : MvPolynomial σ R) : hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := by` |
| `Roth/HasseDeriv.lean:201` | `MvPolynomial.pderiv_hasseDeriv` | `pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P := by` |
| `Roth/HasseDeriv.lean:211` | `MvPolynomial.degreeOf_hasseDeriv_le` | `degreeOf j (hasseDeriv d P) ≤ degreeOf j P := by` |
| `Roth/HasseDeriv.lean:220` | `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | `(h : degreeOf j P < d j) : hasseDeriv d P = 0 := by` |
| `Roth/HasseDeriv.lean:226` | `MvPolynomial.hasseDeriv_monomial_mul` | `(g : MvPolynomial σ R) : hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g := by` |
| `Roth/HasseDeriv.lean:244` | `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | `(hf : ∀ j ∈ d.support, degreeOf j f = 0) : hasseDeriv d (f * g) = f * hasseDeriv d g := by` |
| `Roth/HasseDeriv.lean:254` | `MvPolynomial.hasseDeriv_single_aeval_X` | `hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) =` |
| `Roth/HasseDeriv.lean:267` | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | `uniqueAlgEquiv R σ (hasseDeriv (R := R) (Finsupp.single (default : σ) n) P) =` |
| `Roth/HasseDeriv.lean:287` | `MvPolynomial.factorial_smul_hasseDeriv_single` | `(n.factorial : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv (R := R) j))^[n] P := by` |
| `Roth/Index.lean:63` | `Roth.mem_support_taylor_iff` | `d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 := by` |
| `Roth/Index.lean:70` | `Roth.index_le_weight` | `(h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d :=` |
| `Roth/Index.lean:77` | `Roth.exists_weight_eq_index` | `∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by` |
| `Roth/Index.lean:86` | `Roth.le_index_iff` | `c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by` |
| `Roth/Index.lean:110` | `Roth.index_sub_weight_le_index_hasseDeriv` | `(hk : hasseDeriv k P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :` |
| `Roth/Index.lean:111` | `Roth.index_sub_weight_le_index_hasseDeriv` | `index P α r - weight r k ≤ index (hasseDeriv k P) α r := by` |
| `Roth/Index.lean:238` | `Roth.index_unique` | `have key (d : σ →₀ ℕ) : eval α (hasseDeriv d P) = q.coeff (d default) := by` |
| `Roth/Index.lean:240` | `Roth.index_unique` | `exact (eval₂_uniqueAlgEquiv (f := hasseDeriv d P) (φ := RingHom.id ℝ) (a := α)).symm` |
| `Roth/Main.lean:385` | `Roth.abs_eval_lt_of_le_index` | `(hC : ∀ i : Fin m →₀ ℕ, \|eval (fun _ ↦ α) (hasseDeriv i Q)\| < C) :` |
| `Roth/Main.lean:392` | `Roth.abs_eval_lt_of_le_index` | `have hterm : ∀ d ∈ box r, \|eval (fun _ ↦ α) (hasseDeriv d Q) *` |
| `Roth/Main.lean:395` | `Roth.abs_eval_lt_of_le_index` | `by_cases h0 : eval (fun _ ↦ α) (hasseDeriv d Q) = 0` |
| `Roth/MainLemma.lean:362` | `Roth.exists_ne_modByMonic_eq` | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ C)` |
| `Roth/MainLemma.lean:365` | `Roth.exists_ne_modByMonic_eq` | `∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f := by` |
| `Roth/MainLemma.lean:369` | `Roth.exists_ne_modByMonic_eq` | `⟨(diag (hasseDeriv p.1.1 W.1) %ₘ f).coeff p.2, abs_le.1 (hC W.1 W.2 p.1.1 p.1.2 p.2.1 p.2.2)⟩` |
| `Roth/MainLemma.lean:404` | `Roth.eval_hasseDeriv_sub_eq_zero` | `(h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f) :` |
| `Roth/MainLemma.lean:405` | `Roth.eval_hasseDeriv_sub_eq_zero` | `eval (fun _ ↦ α) (hasseDeriv j (map (Int.castRingHom S) (W' - W''))) = 0 := by` |
| `Roth/MainLemma.lean:406` | `Roth.eval_hasseDeriv_sub_eq_zero` | `have hdvd : f ∣ diag (hasseDeriv j (W' - W'')) := by` |
| `Roth/MainLemma.lean:421` | `Roth.le_index_of_forall_eval_eq_zero` | `(hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) :` |
| `Roth/MainLemma.lean:456` | `Roth.exists_hasseDeriv_eval_ne_zero` | `weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 :=` |
| `Roth/MainLemma.lean:462` | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | `: \|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\| <` |
| `Roth/MainLemma.lean:464` | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | `have hdQ : ∀ j, degreeOf j (hasseDeriv k P) ≤ r j := fun j ↦` |
| `Roth/MainLemma.lean:466` | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | `have heval := abs_eval_le (hasseDeriv i (hasseDeriv k P))` |
| `Roth/MainLemma.lean:480` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `\|eval α (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\| < C)` |
| `Roth/MainLemma.lean:485` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `\|eval α (hasseDeriv i (map (Int.castRingHom ℝ) Q))\| < C := by` |
| `Roth/MainLemma.lean:488` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `have hQev : eval z (map (Int.castRingHom ℝ) (hasseDeriv k P)) ≠ 0 := by` |
| `Roth/MainLemma.lean:490` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `refine ⟨hasseDeriv k P, fun h0 ↦ hQev (by rw [h0, map_zero, map_zero]),` |
| `Roth/MainLemma.lean:500` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `\|((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)\| ≤ (1 + A) ^ ((∑ k, r k) + 1 - f.natDegree) *` |
| `Roth/MainLemma.lean:503` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `have hdP : ∀ k, degreeOf k (hasseDeriv j P) ≤ r k := fun k ↦` |
| `Roth/MainLemma.lean:505` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `have hsupp : ((hasseDeriv j P).support.card : ℝ) ≤ ((∏ k, (r k + 1) : ℕ) : ℝ) := by` |
| `Roth/MainLemma.lean:507` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `have hcD : ∀ k, \|((diag (hasseDeriv j P)).coeff k : ℝ)\| ≤` |
| `Roth/MainLemma.lean:519` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | `(j : σ →₀ ℕ) (i : ℕ) : \|(diag (hasseDeriv j P) %ₘ f).coeff i\| ≤ (⌊B * β ^ 3⌋₊ : ℤ) := by` |
| `Roth/MainLemma.lean:532` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | `\|((diag (hasseDeriv j P) %ₘ g).coeff i : ℝ)\| ≤ B * β ^ 3 := by` |
| `Roth/MainLemma.lean:538` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | `have hreal : \|((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)\| ≤ B * β ^ 3 := by` |
| `Roth/MainLemma.lean:553` | `Roth.exists_mem_RSet_le_index_aux` | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ (C : ℤ))` |
| `Roth/MainLemma.lean:602` | `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ (Cn : ℤ) := by` |
| `Roth/MainLemma.lean:649` | `Roth.exists_auxiliary_polynomial_of_log_bound_aux` | `\|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\| <` |
| `Roth/MainLemma.lean:701` | `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | `\|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k W)))\| <` |
| `Roth/MainLemma.lean:745` | `Roth.main_lemma` | `∀ i : Fin m →₀ ℕ, \|eval (fun _ ↦ α) (hasseDeriv i (map (Int.castRingHom ℝ) Q))\| <` |
| `Roth/Separation.lean:147` | `Roth.hasseDeriv_rename_mul_aeval` | `hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval` |
| `Roth/Separation.lean:148` | `Roth.hasseDeriv_rename_mul_aeval` | `(X none : MvPolynomial (Option τ) R) V) = rename some (hasseDeriv d U) * Polynomial.aeval` |
| `Roth/Separation.lean:353` | `Roth.det_hasseDeriv_separated` | `(Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ))` |
| `Roth/Separation.lean:514` | `Roth.exists_rat_factors_det_hasseDeriv_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *` |
| `Roth/Separation.lean:526` | `Roth.exists_rat_factors_det_hasseDeriv_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det with hFdef` |
| `Roth/Separation.lean:547` | `Roth.exists_det_eq_mul` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *` |
| `Roth/Taylor.lean:103` | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | `(ih : ∀ d, (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a)))` |
| `Roth/Taylor.lean:105` | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | `eval α (hasseDeriv d (monomial (Finsupp.single i n + k) a)) := by` |
| `Roth/Taylor.lean:121` | `MvPolynomial.coeff_taylor_monomial_aux` | `(taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a)) := by` |
| `Roth/Taylor.lean:135` | `MvPolynomial.coeff_taylor` | `(taylor α P).coeff d = eval α (hasseDeriv d P) := by` |
| `Roth/Taylor.lean:199` | `MvPolynomial.eq_sum_box_hasseDeriv` | `P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by` |
| `Roth/Taylor.lean:200` | `MvPolynomial.eq_sum_box_hasseDeriv` | `have h1 : taylor α P = ∑ d ∈ Roth.box r, monomial d (eval α (hasseDeriv d P)) := by` |
| `Roth/Taylor.lean:219` | `MvPolynomial.eval_eq_sum_box` | `eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by` |
| `Roth/Theta.lean:378` | `Roth.sum_max_sub_le_index_det` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0) (α : Option τ → ℝ)` |
| `Roth/Theta.lean:383` | `Roth.sum_max_sub_le_index_det` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by` |
| `Roth/Theta.lean:386` | `Roth.sum_max_sub_le_index_det` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R` |
| `Roth/Theta.lean:463` | `Roth.index_det_le` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` |
| `Roth/Theta.lean:466` | `Roth.index_det_le` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)` |
| `Roth/Theta.lean:470` | `Roth.index_det_le` | `have hFcoef (d) : \|(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv` |
| `Roth/Theta.lean:514` | `Roth.mapped_det_ne_zero_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` |
| `Roth/Theta.lean:516` | `Roth.mapped_det_ne_zero_aux` | `(Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +` |
| `Roth/Theta.lean:519` | `Roth.mapped_det_ne_zero_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` |
| `Roth/Theta.lean:520` | `Roth.mapped_det_ne_zero_aux` | `(Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +` |

**Inline re-derivation check.** Actual whole-project grep for `Finsupp.lsum|coeffLinearEquiv|monomial.*choose|choose.*monomial|\bDelta\b|\bΔ\b|deriv.*factorial|factorial.*deriv` finds the target's sole linear-extension construction, explanatory comments and the theorem relating factorial multiples to iterated partials. No second independent multivariate Hasse operator under another name was found in the inspected project sources. The coefficient/Taylor recurrence in `Roth/Taylor.lean` characterizes the same named operator rather than bypassing it; univariate `Polynomial.hasseDeriv` calls are separate objects. [Raw grep receipt](../evidence/MvPolynomial.hasseDeriv/evidence/inline-grep.json).

**Attempt 1 — univariate Hasse derivative.** Partial match only. A single-coordinate/univariate restriction can be transported by an equivalence when one exists, but arbitrary `σ` is not assumed `Unique`, and arbitrary multiorder is not one natural number in one variable. The project itself needs `hasseDeriv_single_aeval_X` and `uniqueAlgEquiv_hasseDeriv` to prove those compatibilities. These project theorems may not be used as mathlib replacements. Direct typed-replacement failure is tested in the isolated Mathlib-only environment.

**Attempt 2 — compose ordinary partial derivatives.** Does not give the target over arbitrary semirings. Repetition gives `n!` multiples, as the project's `factorial_smul_hasseDeriv_single` states; division/cancellation is unavailable in general. Even in characteristic zero the multi-coordinate ordering/iteration and normalization need their own justification, rather than three calls giving the current semiring operator.

**Attempt 3 — generic linear extension.** Construction succeeds in principle and is what the definition already uses:

```lean
Finsupp.lsum R (fun k : σ →₀ ℕ ↦
  (monomial (k - d)).comp
    (LinearMap.lsmul R R ((d.prod fun j n ↦ (k j).choose n : ℕ) : R))) ∘ₗ
  (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
```

This requires the new operator's specific monomial/binomial kernel; the underlying operations include support product, binomial coefficient, scalar multiplication, monomial formation, coefficient extension and composition. It is not a 1–3-call theorem specialization/composition of an existing differential operator. Counting this as an existing Hasse derivative would dismiss the pinned univariate definition for the same reason. The explicit semantic/API exemption and downstream uses establish why this named operation is valuable even though its construction uses generic primitives.

The independent Mathlib-only scratch experiment searches by `exact?` for a linear map satisfying the full monomial rule **before** introducing any local witness; it then constructs a witness with exactly the displayed kernel and proves the rule. It imports only the relevant Mathlib polynomial modules, with **no `Roth` import**. This is a generic-route check plus a positive consistency check of the construction; failure of one search tactic is not advertised as complete logical absence. Result: **PASS**, 4922ms, fully elaborated (`partial=false`, `success=true`, `timed_out=false`), with no errors, warnings or failed dependencies. A separate positive-control `exact?` example succeeds under the same imports, so the failed generic search is not explained by an unavailable tactic. The `#check_failure` diagnostics are informational expected failures, not compiler errors. [Exact executed source](../evidence/MvPolynomial.hasseDeriv/probes/MathlibOnly.lean), [raw native receipt](../evidence/MvPolynomial.hasseDeriv/evidence/mathlib-only-lsp.json).

**Attempt 4 — translated coefficient.** Mathematically `coeff_d(P(X+z))` defines the same operator. Pinned-source/search checks locate no ready-made multivariate Hasse/Taylor component operator. Implementing the lifted substitution and coefficient projection still needs the multivariate binomial characterization and its relationship to the monomial API; no verified ≤3-call existing replacement was found. No uncompiled new “generalization” is inferred from this equivalent characterization.

**Conclusion: NOT-COMPOSABLE as a ≤3-call replacement from an existing mathlib differential/Taylor API**, with the isolated compiler gate passed. This conclusion concerns the command's replacement criterion, not the obvious fact that generic mathlib primitives suffice to implement the new definition.

## Phase 7 — Verdict and actionable upstream plan

**Category: YES-add-as-is.** All required per-declaration evidence gates have passed; root acceptance is separate.

**Evidence:** Phase 3 identifies a standard characteristic-free multivariate operator with applications beyond Roth; Phase 4 finds its existing arbitrary-variable/commutative-semiring form suitable and no verified weakening or modern mathematical restatement required; Phase 4.5 finds LOW risk; Phase 4.6 accepts the linear-extension strategy; Phase 5 checks all five search channels and verifies the univariate/ordinary-derivative partial matches against pinned source; Phase 5.5 accepts its bundled statement shape; Phase 6 exhibits 41 external-to-file caller declarations and excludes univariate usage, with no verified three-call replacement.

**Why add it.** The concrete API gap is the missing multivariate counterpart to `Polynomial.hasseDeriv`: mathlib supplies characteristic-free univariate divided differentiation and first-order `MvPolynomial.pderiv`, but not a verified arbitrary finite multiorder normalized differential endomorphism on `MvPolynomial`. Iterating the first-order derivations does not recover it over arbitrary semirings. This operator supplies the canonical common object needed for multivariate Taylor coefficients, multiplicity/vanishing conditions and generalized Wronskians. The current project independently needs it in all three roles, and the primary multipoint-evaluation literature supplies another application family. This is more specific than an assertion that an exact name was not found.

Its `LinearMap` type immediately composes with mathlib's `map_sum`, scalar linearity and linear-map composition; its monomial/coefficient interface can extend the existing `pderiv` and univariate `Polynomial.hasseDeriv` APIs. A semantic definition is justified even if it is eventually implemented by a short coefficient-of-translation construction. The reviewed object is not a standalone alias for a scalar support product. Accordingly the earlier `hasseCoeff` NO verdict neither forces this derivative to be inlined nor automatically becomes a YES verdict for the coefficient helper.

**Proposed mathlib location:** `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`, beside `PDeriv.lean` and analogous to `Mathlib/Algebra/Polynomial/HasseDeriv.lean`.

**Proposed PR title:** `feat(Algebra/MvPolynomial/HasseDeriv): define multivariate Hasse derivatives`.

**PR grouping:** propose the definition together with its minimal computational interface (`hasseDeriv_monomial`, `hasseDeriv_apply`, `coeff_hasseDeriv`, zero/constant behavior) and bridges to univariate Hasse derivatives and partial derivatives. The named composition and scalar identities are natural subsequent API candidates. These are grouping recommendations only: their individual assessments remain unfinished and this report does not claim they have YES verdicts. The existing standalone `hasseCoeff` NO report remains in force; discuss a private/local product implementation, direct support product in the defining formula, or a reviewed package-level coefficient name before upstreaming that helper.

**Pre-PR actions:**

1. Run `/generalise MvPolynomial.hasseDeriv` to confirm no additional mechanical weakening, without inventing a noncommutative polynomial or arbitrary-algebra restatement.
2. Run `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv`, including import minimization and modern module/public style, against the intended upstream file. Carry the exact monomial normalization, arbitrary variable type and semiring scope through the cleanup.
3. Complete individual assessments for the proposed supporting theorems and settle the coefficient helper's package design. Do not propagate this verdict to substantive non-glue lemmas.
4. Pick a reviewer from recent `Algebra/MvPolynomial` contributions and verify the then-current mathlib snapshot for duplication before opening a PR.

**Alternative destination:** retaining the implementation in `Roth/HasseDeriv.lean` while preparing the coherent upstream API is appropriate. Its general algebraic content fits core mathlib rather than `Archive/` or a Roth-only historical theorem collection. No deletion/refactor of production callers is requested in this read-only assessment.

**Next action:** record this completed definition assessment after root acceptance; retain all production code unchanged. Assess `MvPolynomial.hasseDeriv_monomial` next in declaration order, and prepare a coherent multivariate Hasse derivative API upstream only after its members receive their own required checks.

## Phase 8 — Completion gate

**Assessment COMPLETE; independent root acceptance pending.** All phases 0–8 and required subphases are present: baseline/type/standard-axiom evidence; mathematical prose; size and all semantic-exemption rows; all nine literature channels or explicit valid unavailable/inapplicable reasons; parameter-by-parameter generality; informative compiled rejection of the only candidate typeclass weakening; all nine modern-idiom questions including Q8/Q9; all six infrastructure-risk rows with actual synthesis/defeq/coercion/universe checks; all five proof-strategy rows; five actual mathlib search methods; all three statement-shape audits; complete direct caller table and inline-rederivation check; isolated generic-route/positive-control/constructor proof with no target leakage; and actionable YES rationale, location, grouping and next actions.

Both compiler batches fully elaborated successfully through the root-owned persistent native Lean session. The target-risk batch has one honestly retained scratch module-docstring style warning, no errors, and only standard axioms. The isolated batch has no errors or warnings. Neither used `sorry`, extra axioms, native trust, limit raises or project imports in the Mathlib-only probe. No redundant CLI compiler or project build was started. Production sources/pins remain unchanged and all 17 baseline hashes match.

The remaining limitations are stated, not hidden: optional ChatGPT tool unavailable; local elaborated index unavailable (fallback results do not prove absence); external search indices may differ from the pin; scoped search/probe evidence is not a universal mathematical non-definability theorem. DOI/XHTML/guessed-version fetch failures are retained, while the relevant primary 2022 full text was subsequently opened successfully. [Assessment metadata](../evidence/MvPolynomial.hasseDeriv/assessment.json), [artifact validation](../evidence/MvPolynomial.hasseDeriv/validation.json), and [portable copy manifest](../evidence/MvPolynomial.hasseDeriv/copy-manifest.json) record completion; root has not yet accepted or published it.
