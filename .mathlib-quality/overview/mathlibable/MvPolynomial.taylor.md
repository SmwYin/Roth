# MvPolynomial.taylor — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The exact translation endomorphism is a single application of mathlib's universal substitution `aeval`. However, this is a documented mathematical operator with concrete consumers (`coeff_taylor` and `Roth.index`) that benefit from a stable named API. The semantic/API-stability exemption is real; it does not decide whether upstream wants that extra name. No production changes are proposed by this assessment.

## Phase 0 — Doctor

Resolved public noncomputable definition at `Roth/Taylor.lean:42–43`, canonical declaration 53. The entire declaring module and the entire actual external caller module `Roth/Index.lean` were read. [Archived Taylor](../evidence/MvPolynomial.taylor/Taylor-module.lean.txt), [archived Index](../evidence/MvPolynomial.taylor/Index-module.lean.txt), and [canonical entry](../evidence/MvPolynomial.taylor/canonical-entry.json) preserve source and provenance.

[Baseline build](../evidence/MvPolynomial.taylor/baseline-build.txt): `lake build`, exit 0, 2467 jobs, no warnings/errors. Reuse is justified by a fresh comparison of every one of the 17 production-source/pin hashes against the shared baseline manifest: [inputs](../evidence/MvPolynomial.taylor/inputs.json), [hash check](../evidence/MvPolynomial.taylor/input-hash-check.json). This is build reuse, not a claim of a new worker build.

Root's native target run completed successfully with `partial=false`, no failed dependencies, errors or warnings. The exact original definition and an independently named replay agree by `rfl`. A first namespace-ambiguous `C` attempt was rejected and is archived separately, not counted as verification. [Accepted native target receipt](../evidence/MvPolynomial.taylor/native-target-success.json), [exact executed disk source](../evidence/MvPolynomial.taylor/native-target-executed.lean.txt), [rejected attempt](../evidence/MvPolynomial.taylor/native-target-rejected.json).

## Phase 1 — Comprehend

Given a commutative semiring R and any set of variables σ, translation by a vector α sends a formal polynomial P(X) to P(X+α), replacing each variable independently. It fixes coefficients and preserves addition, multiplication and the R-algebra structure. This is formal polynomial substitution; it does not identify polynomials with their pointwise functions over finite rings.

Full native elaborated type:

```lean
@MvPolynomial.taylor : {σ : Type u_1} →
  {R : Type u_2} → [inst : CommSemiring R] →
    (σ → R) → MvPolynomial σ R →ₐ[R] MvPolynomial σ R
```

The body is exactly `aeval fun j ↦ X j + C (α j)`. σ and R have independent arbitrary universes; α is arbitrary, including infinite support. No finite-variable, decidable-equality, characteristic-zero, field, domain, nontriviality or subtraction assumption appears. The declaration has no project-body dependencies: `aeval`, `X`, `C`, and the existing algebra instances are mathlib. Original and replay depend only on `propext`, `Classical.choice`, `Quot.sound`; no new axiom or sorry is accepted.

## Phase 2 — Size and definition necessity

BIG: this introduces the named translation operator, explicitly listed as the module's main definition. Body count: one substantive line, hence ONE-LINER.

| Exemption | Applies? | Concrete evidence |
|---|---|---|
| Avoid defeq abuse | no | `taylor_apply` and native `exact_bridge` are rfl; no consumer requires an opaque boundary or controlled reduction for correctness. |
| Avoid typeclass diamonds | no | It is an AlgHom value, not a class, type alias or instance declaration. |
| Semantic intent / API stability | yes | `coeff_taylor` names the Hasse coefficient interpretation, and `Roth.index` takes the support of a translated polynomial. The name separates translation from arbitrary substitution and stabilizes both statements. |

Conclusion: **ONE-LINER WITH-EXEMPTION**. The exemption is independently established from these consumers; it is not inherited from `Polynomial.taylor`. Direct expansion remains mathematically complete, so API taste remains the substantive decision.

## Phase 3 — Exhaustive literature

Exact requests, returned-response byte counts and SHA256 digests are retained in the seven metadata receipts; response bodies are deliberately not persisted. [General forms](../evidence/MvPolynomial.taylor/web-0-metadata.json), [named sources](../evidence/MvPolynomial.taylor/web-1-metadata.json), [MO/recent arXiv](../evidence/MvPolynomial.taylor/web-2-metadata.json), [nLab refinement](../evidence/MvPolynomial.taylor/web-3-metadata.json), [Stacks refinement](../evidence/MvPolynomial.taylor/web-4-metadata.json), [arXiv refinement](../evidence/MvPolynomial.taylor/web-5-metadata.json), [categorical query and access limits](../evidence/MvPolynomial.taylor/web-6-metadata.json). The following rows give original concise summaries, not copied article bodies.

| Channel | Actual query / locator | Result and significance |
|---|---|---|
| General web — specific | `multivariate polynomial Taylor shift P(X+a) Hasse derivatives arbitrary ring` | Bhargava et al., [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025), §3.2 Definition 3.4: Hasse coefficients are coefficients of substitution f(x+z) over a commutative ring. Direct conceptual match. |
| General web — general | `polynomial ring translation automorphism additive group action arbitrary commutative ring` | [Universal properties of polynomial rings](https://fenix.tecnico.ulisboa.pt/downloadFile/563568428826591/ring_algebras.pdf): assigning generators determines the algebra map. Explains why the current body is already universal substitution. |
| General web — alias | `Taylor shift multivariate polynomial substitution translation operator` | von zur Gathen–Matera, [Shifted varieties and discrete neighborhoods around varieties](https://vonzurgathen.online/wp-content/uploads/2019/07/2019GathenMateraDiscreteTubesArxiv1812.07020.pdf), §6, (6.2)–(6.3): Taylor expansion and shift invariance over finite fields; confirms the operator matters outside Roth. Older paper; not counted as recent arXiv. |
| ChatGPT math MCP | Standard form, generality and historical-evolution question | n/a: `ask_chatgpt_math` unavailable in tool inventory; no answer fabricated. |
| Local references | `Taylor|P_\\alpha|translation|translated` in clean.tex | §4, lines 501–554, defines Pα(X)=P(X+α), used to compute the index. Source initially works over ℝ in finitely many variables; this Lean definition is already broader. [Exact local search](../evidence/MvPolynomial.taylor/local-literature.json). |
| nLab | `site:ncatlab.org/nlab/show/polynomial+ring free commutative algebra` | [Polynomial](https://ncatlab.org/nlab/show/polynomial), definition and properties: arbitrary-set polynomial algebra is free commutative algebra; supports `aeval` as canonical universal-property construction. |
| nCatLab categorical | `site:ncatlab.org "polynomial" "universal" "algebra"` and additive-group/affine-space queries | [Affine space](https://ncatlab.org/nlab/show/affine%2Bspace), translation-group action viewpoint; [affine line](https://ncatlab.org/nlab/show/affine%2Bline), additive group scheme. These are adjacent abstractions, not a proof that current operator should be replaced by a category definition. nLab and nCatLab share the same host; these are separate actual queries, not independent publications. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring change variables automorphism translation`, then universal-property refinement | [Tag 07XB](https://stacks.math.columbia.edu/tag/07XB) uses the polynomial universal property; [Tag 07H5](https://stacks.math.columbia.edu/tag/07H5) concerns divided-power polynomial algebras, a different object. No direct named Taylor-shift result located; do not substitute divided-power algebra for MvPolynomial. |
| MathOverflow | `site:mathoverflow.net multivariate polynomial translation Hasse derivatives` | [Replacement for derivations in characteristic p?](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) and [interpolation question](https://mathoverflow.net/questions/357689/interpolating-multivariate-polynomials-from-their-partial-derivatives) confirm Hasse/characteristic sensitivity. Adjacent use, not a stronger definition of translation. |
| Recent arXiv, window 2021-10-27 to 2026-10-27 | `site:arxiv.org multivariate Taylor shift Hasse derivative 2022 2023 2024 2025 2026`, then exact-title refinement | [arXiv:2205.00342](https://arxiv.org/abs/2205.00342), Bhargava–Ghosh–Guo–Kumar–Umans, submitted 2022-04-30, directly relevant to multipoint evaluation and Hasse substitution. Other returned analytic Taylor-measure/spectral-shift papers concern different objects and are rejected. |

Access limits: direct opening of the nLab polynomial page returned unsupported `application/xhtml+xml` (400), while indexed search supplied its definition. `arxiv.org/html/2205.00342v3` returned 404, so no claim of having inspected that HTML version; the arXiv abstract and the journal's indexed §3.2 supplied the relevant locators. Search-result crawled/published labels are not relied on for the five-year date: the actual arXiv submission date is used.

Literature synthesis: standard names are polynomial translation, shift and Taylor shift. Formal substitution works over commutative semirings; rings additionally supply inverse translation, and fields are unnecessary for the operator. The arbitrary-variable universal-property construction is already available. Function translation and infinite power-series substitution are different representations with extra issues; they are not mechanical weakenings of this definition. No disagreement in mathematical content was found.

## Phase 4a–4b — Generality

| Parameter / hypothesis | Current form | Standard comparison | Weakening decision |
|---|---|---|---|
| σ | arbitrary Type u | often finitely many variables in applications | Already more general; no Fintype/DecidableEq needed. |
| R | arbitrary Type v | literature rings or fields | Semiring form already removes negatives and division. |
| CommSemiring R | commutative coefficients | needed by current MvPolynomial/AlgHom interface | No droppable field in this hierarchy; noncommutative or nonunital polynomials change the interface and object. |
| α | any σ → R | arbitrary translation vector | No support, regularity or nonzero condition to drop. |
| output | bundled R-algebra endomorphism | substitution preserving algebra | Correct structure, stronger than mere function or linear map, and preserves every existing semiring case. |

Verdict: **MAXIMALLY GENERAL in the fixed MvPolynomial/AlgHom representation**, zero verified hypothesis weakenings. We do not claim an uncompiled Semiring-only generalization. Allowing arbitrary target algebras and arbitrary substitutions is already `MvPolynomial.aeval`, not new translation API. Ring-only equivalences add a richer representation under stronger hypotheses and must complement, not replace, the semiring operator. Native replay works with arbitrary universe parameters and with σ=`Type 1`, R=ℕ.

## Phase 4c — Modern idiom

| # | Question | Assessment / concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | Already `[CommSemiring R]`, canonical algebra instances; no new class justified. |
| 2 | Filters instead of metric/sequences | No topology or convergence. |
| 3 | Universal property instead of construction | Already `aeval`, the free algebra extension; `aeval_unique` characterizes it. Creating another universal-property class would duplicate infrastructure. |
| 4 | Bundled substructures | Already bundled AlgHom, so map_mul/map_sum/map_pow apply. Over CommRing a new AlgEquiv yields injectivity generically; this is a complementary bundle, not a substructure-lattice problem. |
| 5 | Weaker hierarchy | Already semiring, not field or ring. Inverse translation genuinely needs negative coefficients. |
| 6 | Higher categories | No higher-categorical content needed to expose this generator assignment. |
| 7 | Concrete index generalization | Arbitrary σ already; the additive translation parameters σ → R could be packaged into an additive action. Such packaging needs new action laws and cannot be cited as an existing replacement. |
| 8 | Concrete-via-abstract diagnostic | The one body line contains no `taylor` occurrence and uses only `aeval`. Diagnostic fires positively: the more abstract map is precisely existing universal substitution. The concrete mathematical choice X+α remains the semantic content; abstracting that assignment away gives `aeval` itself. |
| 9 | False-generalization guard | Reject replacing formal polynomials by pointwise functions (finite-field evaluation is not faithful), or arbitrary MvPowerSeries translation (nonzero constants obstruct unrestricted formal substitution). AlgEquiv only under CommRing preserves the intended shift but cannot replace the CommSemiring map. |

Modern-idiom verdict: **current construction is already idiomatic**. A new CommRing AlgEquiv is a useful compatible extension, not evidence requiring generalise-first. The [raw exact experiment](../evidence/MvPolynomial.taylor/native-raw-executed.lean.txt) constructs it using translations ±α and proves injectivity by `(translateEquiv α).injective`. This concretely could replace `taylor_neg_taylor`-based manual injectivity at Taylor:187. An additive action could organize composition/zero identities; none is claimed as preexisting mathlib translation infrastructure.

## Phase 4.5 — Infrastructure risk (definition: all six rows apply)

| Risk | Verdict | Evidence / mitigation |
|---|---|---|
| Typeclass diamond | none | No new type or instance. Target algebra uses existing `AddMonoidAlgebra.algebra`, confirmed by #synth for ℕ and Type 1 variables. No second R-action introduced. |
| Reducibility leak | low | Ordinary semireducible def, no reducible attribute. Native bridge rfl confirms transparent definitional equality; no heavy computation or class search is hidden. |
| Noncanonical unfolding | low | `taylor_apply` is rfl and names the expansion explicitly; targeted X/C simp rules preserve semantic usage. No global simp unfolding or instance unfolding introduced by this definition. |
| Instance priority collision | none | Definition is an AlgHom value, not an instance; no priority or competing search path. |
| Universe polymorphism | none observed | Native type has independent u_1/u_2, replay is universe polymorphic, and the explicit σ=Type 1, R=ℕ probe succeeds. No finite/universe coercion is forced. |
| Coercion ambiguity | none observed | Existing AlgHom CoeFun only; native application/map_mul probes elaborate. A complementary AlgEquiv would use its standard coercion/toAlgHom path, no custom CoeFun needed. |

Overall risk **LOW**, no HIGH rows. [Raw native receipt](../evidence/MvPolynomial.taylor/native-raw-success.json) establishes actual synthesis, coercion, universe, reducibility and complementary equivalence probes rather than a theorem-kind n/a shortcut.

## Phase 4.6 — Proof strategy

| Question | Applies? | Idiom / cost |
|---|---|---|
| Topology ε–δ versus filters | no | No topology. |
| Algebra elements versus bundled maps | yes, already optimal | `aeval` produces a bundled map in one call; no elementwise preservation proof. |
| Analysis sequences versus nets | no | No analysis. |
| Explicit construction versus universal property | already universal | Existing free-algebra extension `aeval`; changing to another universal-property class duplicates API. |
| Missing helper API | no for definition | No helper needed to define shift. Named coefficient/composition/inverse APIs may be useful companion work and are separately assessed. |

Strategy verdict: **MATHLIB-IDIOMATIC**. No proof refactor is needed to construct the object. The AlgEquiv experiment is new companion infrastructure, with nontrivial inverse normalization; it is not a one-call replacement for the current semiring operator.

## Phase 5 — Five actual methods × three forms

[Complete exact requests and raw formal-search receipts](../evidence/MvPolynomial.taylor/formal-search.json) preserve all twelve API calls. Full source-search commands/results are [current](../evidence/MvPolynomial.taylor/rg-current.json), [literature](../evidence/MvPolynomial.taylor/rg-literature.json), [abstract](../evidence/MvPolynomial.taylor/rg-abstract.json), and [untruncated full-name search](../evidence/MvPolynomial.taylor/rg-full-name.json). Thus all five methods were actually used on all three forms; rg supplies the fifth method to the four service methods.

| Method | Current translation | Literature universal substitution | Abstract action/equivalence |
|---|---|---|---|
| Lean-Finder | Polynomial.taylorAlgHom/Equiv, MvPolynomial.bind₁ | Polynomial.algEquivAevalXAddC variants, univariate shifts | Univariate affine equivalences and inverse laws |
| Loogle | AlgHom endomorphism pattern: aeval_X_left, rename, expand | MvPolynomial.aeval: exact generic substitution constructor | AlgEquiv endomorphism pattern: renameEquiv_refl, NoetherNormalization.varChange, not the shift |
| LeanSearch | Univariate Taylor/affine API | MvPolynomial.aeval, aevalTower, bind₁ | AlgEquiv.aut, univariate affine equivalence, generic function translate |
| rg pinned source | No multivariate named shift; direct project def | Eval:569 aeval, Monad:69 bind₁, aeval_unique/comp_aeval | Rename:213 renameEquiv, univariate taylorEquiv, generic function translate |
| lean_local_search | Project taylor and univariate names returned | aeval family returned | Many unrelated translate names returned |

Every service response has isError=false. The local index reports `unavailable` for each form: returned source hits are useful, but absence and generated declarations cannot be inferred. Remote snapshots may differ from the pinned checkout; native #check confirms the positive aeval and univariate Taylor candidates. `#check_failure MvPolynomial.taylor` in the mathlib-only environment confirms this name is not imported there, not a universal mathematical absence proof.

Concluded: **exact existing generic construction in MvPolynomial.aeval**, with bind₁ an identical variable-substitution interface. No named multivariate translation API located by these methods. Polynomial.taylorAlgHom/Equiv are genuine analogues for a single variable; arbitrary σ has no canonical one-variable identification, so they are not general replacements. `rename` maps variables to variables, not X+constants. Generic `translate` acts on functions via negative argument shift and needs a group, not on formal semiring polynomials. No parent verdict is inherited.

## Phase 5.5 — Statement shape

Normal forms considered: (1) `aeval (fun j ↦ X j + C (α j))`, (2) `bind₁` with that assignment, (3) unbundled P ↦ P(X+α), (4) CommRing AlgEquiv. Mathlib's canonical generic substitution is aeval. The current body uses it directly; a named operator would be a semantic API layer, not a rival substitution implementation. RHS convention is respected by `taylor_apply` (named expression unfolds to aeval on RHS); no quadratic network of equivalence lemmas is proposed.

Syntactic generality: the native replay tests the current AlgHom shape and pointwise multiplication; the complementary AlgEquiv tests a richer ring-only interface. Keep the AlgHom as baseline: generic homomorphism rewriting works without carrying P as an extra parameter. Adding an explicit target-algebra argument or arbitrary generator map simply restates existing aeval and dilutes translation semantics.

Superfluous arguments: both σ and R determine the domain and codomain; CommSemiring supplies the existing polynomial algebra interface; α determines the generator images. No extra implicit finite, classical-choice instance, field or characteristic argument is present. `noncomputable` matches the existing finitely supported polynomial evaluation construction; it is not a mathematical hypothesis. Shape verdict **OK**, no verified mechanical restatement required.

## Phase 6.0 — Every explicit caller and inline audit

There are **24 distinct explicit source callers, 17 in Taylor and 7 in Index; 41 `taylor` identifier occurrences inside these declarations**. Counts include statement and body occurrences, exclude docstrings and the own definition, and distinguish `Polynomial.taylor` in `index_unique`. These are source-level references, not opaque kernel or simp-dependency closure. [Exact caller sources, line occurrences, counts, hashes and per-caller plan](../evidence/MvPolynomial.taylor/callers.json).

| Caller | Source | Explicit occurrences | Action if named API is rejected |
|---|---|---|---|
| `Roth.index` | `Roth/Index.lean:59` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `Roth.mem_support_taylor_iff` | `Roth/Index.lean:63` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `Roth.index_le_weight` | `Roth/Index.lean:71` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `Roth.exists_weight_eq_index` | `Roth/Index.lean:79,80` | 2 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `Roth.index_eq_weightedOrder_div` | `Roth/Index.lean:145,148` | 2 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `Roth.index_mul` | `Roth/Index.lean:169` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `Roth.index_mul_left_weights` | `Roth/Index.lean:202,203` | 2 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_apply` | `Roth/Taylor.lean:47` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_X` | `Roth/Taylor.lean:51` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_C` | `Roth/Taylor.lean:55` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_monomial` | `Roth/Taylor.lean:60` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.coeff_taylor_monomial_single_add_aux` | `Roth/Taylor.lean:103,104,109` | 3 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.coeff_taylor_monomial_aux` | `Roth/Taylor.lean:121` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.coeff_taylor` | `Roth/Taylor.lean:135` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.eval_taylor` | `Roth/Taylor.lean:142,143` | 2 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_taylor` | `Roth/Taylor.lean:147,148` | 4 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_zero` | `Roth/Taylor.lean:152,153` | 2 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_map` | `Roth/Taylor.lean:158,159` | 3 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_rename` | `Roth/Taylor.lean:165,166` | 3 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.degreeOf_taylor_le` | `Roth/Taylor.lean:171` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_neg_taylor` | `Roth/Taylor.lean:182` | 2 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_injective` | `Roth/Taylor.lean:187` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.taylor_eq_zero_iff` | `Roth/Taylor.lean:192` | 1 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |
| `MvPolynomial.eq_sum_box_hasseDeriv` | `Roth/Taylor.lean:200,208` | 3 | Expand each taylor application to aeval at X+α; retain semantic theorem/definition under its own name. |

The same-file count is 17 distinct declarations. In the command’s internal-use convention, K excludes the declaring file: K=7 distinct consuming declarations in one other project file, `Roth/Index.lean`, for 24 total source callers. No usage outside this project was established. `taylor` is not dead code: the coefficient identity and index definition materially use it. Each row's expansion is definitionally equal as an entire AlgHom, established by the target rfl bridge. If expanding all sites, replace `simp [taylor, …]` with the same aeval normalizations, drop the tautological taylor_apply bridge, and replace X/C/monomial helpers with generic aeval_X/algHom_C/aeval_monomial. Supporting mathematical Taylor/Hasse lemmas must be retained or restated; deleting the operator does not delete their content.

[Inline derivation search](../evidence/MvPolynomial.taylor/rg-inline.json) found the own body, its apply bridge and a local one-variable factorization in Taylor. Mathlib's CartanExists uses a general affine assignment into a univariate target (`C(...) * X + C(...)`), not a duplicate arbitrary-variable translation endomorphism. No hidden exact multivariate shift was identified. This audit is textual and not a claim of exhaustive elaborated dependency discovery.

## Phase 6 — Actual composition and caller experiments

The exact inline construction is one mathlib constructor, with X and C supplying the generator expression:

```lean
noncomputable def translate {σ R : Type*} [CommSemiring R] (α : σ → R) :
    MvPolynomial σ R →ₐ[R] MvPolynomial σ R :=
  MvPolynomial.aeval fun j ↦ MvPolynomial.X j + MvPolynomial.C (α j)
```

The [mathlib-only native experiment](../evidence/MvPolynomial.taylor/native-raw-success.json) proves this well typed, preserves products by `map_mul`, and checks the pinned universal substitution and univariate candidate signatures. Target replay equals original as an AlgHom by rfl. There is no new mathematical proof required for construction. **Composition verdict: COMPOSABLE exactly (one aeval constructor)**, with the semantic-definition exemption creating the upstream judgment rather than hiding this count.

Root additionally ran [exact caller source](../evidence/MvPolynomial.taylor/native-callers-executed.lean.txt) with [complete native success](../evidence/MvPolynomial.taylor/native-callers-success.json): actual X, C, and monomial consumer forms follow in one existing mathlib call each; the coefficient theorem's statement transports through the definitional bridge; the exact Index RHS is checked as a typed sInf/weight/support expression and agrees by rfl. The coefficient identity is a project theorem used to demonstrate caller compatibility, not counted as an existing mathlib building block. The Index test is an exact definition-body fragment, not a claim of a freshly built migrated Index module. Entire-AlgHom definitional equality makes all 24 source expansions type compatible; no migrated production build was performed because edits are outside assessment scope.

The raw CommRing AlgEquiv is explicitly new infrastructure. Its newly constructed left/right inverse obligations close by simp on `comp_aeval_apply` and zero substitution. Phase 6b’s trivial-simp caution applies only to those inverse obligations here: they are not an existing-call proof of a preexisting equivalence, and their simp closure does not classify the original definition. The original definition is exactly the one-aeval construction above; its BORDERLINE verdict independently concerns the semantic/API-stability exemption. Its generic injectivity benefit is verified, but its existence cannot force a NO-mathlib-has-it verdict for the semiring definition. No timeout/failed search is promoted to a proof of absence.

## Phase 7 — Verdict and actionable alternatives

**BORDERLINE-needs-human**, for API design, not unresolved verification. Literature confirms a standard operator; semiring/arbitrary-variable generality is appropriate; the ordinary definition is low risk; all exact construction and caller evidence is clean. The choice is between a useful stable name anchoring the substantive Hasse coefficient API and an exactly sufficient generic aeval term. The semantic exemption defeats an automatic one-line rejection but does not itself establish an upstream gap that must receive a new definition.

Concrete upstream questions (no user interaction required to complete this read-only assessment):

1. Should the multivariate Hasse/Taylor API expose a stable `MvPolynomial.taylor` AlgHom, or state the coefficient theorem directly for `aeval (fun j ↦ X j + C (α j))`?
2. If a named operator is accepted, should `taylor` denote the AlgHom directly or follow univariate `taylor`/`taylorAlgHom` naming and coercion conventions?
3. Should a separate CommRing `taylorEquiv` accompany the semiring map in the same API, with generic injectivity replacing the project's standalone inverse-based proof?

Next action: retain the definition in `Roth/Taylor.lean` pending these design choices. If rejected, mechanically expand the exact aeval term at every one of the 24 listed callers with the row-by-row plan; this is the appropriate project-local destination rather than Archive or a satellite library. If accepted, proposed upstream file `Mathlib/Algebra/MvPolynomial/Taylor.lean`, PR title **feat(Algebra/MvPolynomial): translation and Taylor coefficients**. Group only with independently accepted YES Hasse contributions from [current progress-derived grouping](../evidence/MvPolynomial.taylor/accepted-grouping.json), especially `MvPolynomial.hasseDeriv` and `MvPolynomial.coeff_hasseDeriv`; their verdicts are not inherited here. Run `/generalise MvPolynomial.taylor` and `/cleanup Roth/Taylor.lean MvPolynomial.taylor`, then review companion lemmas individually before submission. Candidate relevant reviewers from [recent source commit history](../evidence/MvPolynomial.taylor/reviewer-history.json): Yaël Dillies (MvPolynomial refactor), Aaron Liu (evaluation duplicate removal), Marcelo Lynch (section-variable cleanup); selection is a suggestion, not a claim they agreed to review. No cost argument is used in this verdict.

Phase 7 gates: all required phases and actual search channels present; exact mathematical construction and API-stability tension documented; no claimed unverified weakening or universal absence; no univariate blanket inheritance; all six infrastructure risks and every explicit caller covered. BORDERLINE questions are bounded and concrete, while verification unresolved remains empty.

## Phase 8 — Consolidated handoff and verification

This report consolidates Phases 0–7 above and supplies a complete, read-only assessment. [Assessment](../evidence/MvPolynomial.taylor/assessment.json), [verification manifest](../evidence/MvPolynomial.taylor/verification.json), [overview entry](../evidence/MvPolynomial.taylor/overview-entry.json), [current copy manifest](../evidence/MvPolynomial.taylor/copy-manifest.json), and [portable validator](../evidence/MvPolynomial.taylor/validate.py) accompany all exact sources and raw receipts. Root acceptance is pending. Mathematical upstream choices remain in Phase 7; there are no outstanding native checks. The validator checks current hashes and bytes, all required phases, complete accepted native responses, permitted axioms, input/source hashes, links, actual searches and credential guard. Historical worker-copy manifests must not replace current artifact validation. Web metadata contains exact queries and response digests; returned credential-bearing URLs are not archived, and the tracked secret guard is run before freeze.
