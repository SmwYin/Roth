# MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint — full fresh assessment

Verdict: **YES-add-as-is**, grouped with the multivariate Hasse derivative API. Root acceptance pending. The support-separation corollary makes the new iterativity law usable without redoing its finite-product argument in proofs about independent sets of variables. This is a read-only assessment; production sources and pins stay unchanged.

## 0. Baseline and scope

All 17 source/pin SHA256 hashes freshly match the shared successful baseline (exit 0, 2467 jobs, no reported warnings/errors). Target resolves uniquely as the public theorem at Roth/HasseDeriv.lean:185. Entire declaring module and entire sole explicit caller module Roth/Separation.lean were read. No sorry, new axioms, resource-limit increases or production edits. Target's actual elaborated type and standard axiom receipt are archived with the accepted native source.

## 1. Mathematical statement

Let R be any commutative semiring and let σ be any set of polynomial variables. For finite natural multi-indices d,e whose supports do not intersect, differentiating first in order e and then in order d gives exactly the Hasse derivative of order d+e. The general composition factor is a product of binomial coefficients; disjointness makes every factor one, without a characteristic or factorial-invertibility restriction.

```lean
∀ {σ R : Type*} [CommSemiring R] {d e : σ →₀ ℕ},
  Disjoint d.support e.support → ∀ P : MvPolynomial σ R,
    hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P
```

Roles: σ indexes variables; R supplies coefficients; CommSemiring is the pinned polynomial parent interface; d,e specify differential orders; h expresses variable separation; P is arbitrary. Project dependencies: hasseDeriv, hasseCoeff, hasseDeriv_hasseDeriv. Proof: general iterativity, Finset.prod_eq_one, disjoint support values vanish, Nat.choose_self, then cast-one and one_smul.

## 2. Preliminary checks

**SMALL**: standard support-separated specialization, not a new structure or a module-listed main theorem. The theorem is not rfl/single-unfold glue and has no inherited verdict. One-line definition test n/a (theorem); the short proof relies on the new parent composition theorem.

## 3. Exhaustive literature protocol

Exact requests and returned-response SHA256/bytes are recorded in web-receipts.json. No full copyrighted web bodies are retained. The following summaries are original.

| Channel | Actual requests / source locator | Finding |
|---|---|---|
| Web, specific | Hasse derivatives disjoint multi indices composition binomial coefficient iterative | Recognizes iterativity and coefficient-defined partial Hasse operators. |
| Web, general | multivariate Hasse Schmidt derivations iterativity disjoint support arbitrary characteristic commutative ring | Higher derivations versus iterative higher derivations must be distinguished. |
| Web, aliases | divided power differential operators independent variables Hasse derivative composition | Divided-power terminology and standard arbitrary-characteristic polynomial operator. |
| Optional ChatGPT math | unavailable in session | n/a, expressly optional; no substitute claimed. |
| Local references | clean.tex123–150,414–424,457–464,578–584 | Canonical monomial definition over semirings; separated variables used in determinant proof; general product-binomial identity explicitly581–582. The present corollary follows because different coordinates have zero overlapping orders. |
| nLab | Hasse-Schmidt derivative and derivation; search plus direct opens | Search returned several-variable polynomial definition over commutative rigs and historical1937 reference. Direct XHTML fetch400 recorded honestly. [Definition](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative). |
| nCatLab | site:ncatlab.org Hasse Schmidt derivation iterative, categorical direct path | Categorical/graded-bimonoid formulation investigated; direct ncatlab path unavailable. No separate established categorical theorem is claimed. |
| Stacks | site:stacks.math.columbia.edu Hasse derivatives divided differential operators; tag09CH read | General differential-operator order/composition and divided powers are adjacent, not an exact replacement for the canonical multivariate formula. [Finite order operators](https://stacks.math.columbia.edu/tag/09CH). |
| MathOverflow | site:mathoverflow.net Hasse derivatives iterativity multivariate; question71423 read | Positive-characteristic motivation and hyperdifferentiation terminology; not evidence of exact disjoint law. [Discussion](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p). |
| Recent arXiv,2021-10-26 onward | Hasse Schmidt derivations2022–2026; Hasse2024/2025iterative | [2506.19489](https://arxiv.org/abs/2506.19489),2025, fullHTML§4.2Definition4.8 read: generalized operator iteration systems. [2407.13604](https://arxiv.org/abs/2407.13604),2024/revised2025, abstract and contents: infinite-variable polynomial-module Hasse–Schur derivatives, adjacent rather than an exact theorem. |
| Primary classical/abstract | [Hoffmann–Kowalski1212.5788](https://arxiv.org/html/1212.5788), Definitions2.1/2.2; [Narváez-Macarro mini-course](https://personal.us.es/narvaez/course_HS_2018.pdf),Definition2.1.1pp14–15,Proposition2.1.6p18 | General HS families satisfy higher Leibniz; iterativity is an additional condition. External composition of coordinate families explains independent variable blocks, but arbitrary HS families cannot replace canonical polynomial iterativity without compatibility assumptions. |

Concept: separated-variable composition of canonical multivariate Hasse derivatives. Sources agree on coefficient extraction/binomial normalization. Standard literature sometimes assumes fields or finite variables; the current arbitrary-variable commutative-semiring formulation is at least as general. General formal-group/HS machinery changes the object and carries an iterativity hypothesis; it does not make the canonical polynomial proof automatic.

## 4a–b. Parameters and verified generality

| Parameter / hypothesis | Assessment and actual verification |
|---|---|
| σ : Type* | Arbitrary universe/type, including empty/infinite variable sets. Finsupp is finite differential support, not Fintype σ. No DecidableEq/nonempty assumption. |
| R : Type*, CommSemiring R | No field, domain, nontriviality, cancellation, inverses, CharZero or factorial units. Only Semiring fails to form pinned MvPolynomial σ R in the isolated native guard. A noncommutative replacement representation is a separate parent API project. |
| d,e | Arbitrary finite natural multi-orders. Zero orders allowed. Ordinary non-natural orders would change polynomial/binomial semantics. |
| h : Disjoint d.support e.support | Genuine sufficient geometric condition; dropping it outright is false. Accepted ℕ/Unit/X² counterexample gives2versus1. Swapping d,e preserves the conclusion by symmetry and add_comm. |
| P | Arbitrary polynomial, no coefficient/degree/support bound; allP nature verified. |
| Scalar-one alternative | Native scalar_one compiles with (hasseCoeff d (d+e):R)=1, and nat_factor_one with natural factor=1. In ZMod2, overlapping orders1,2 have natural factor3 but cast1, so the cast condition strictly extends the support condition. |
| Equivalent ordered-Finsupp disjointness | Finsupp.disjoint_iff gives an equivalent h : Disjoint d e shape; pinned signature and actual proof checked in final native source. It is equivalent syntactic packaging, not a weaker mathematical assumption. |

Generality verdict: **MAXIMALLY GENERAL for this support-separation corollary**. This does not claim h is necessary for equality: the verified scalar-one criterion is strictly weaker over some rings. Replacing geometric separation by an equality involving the normalization factor would discard the corollary's semantic and caller interface, while being already the direct specialization of the unrestricted parent composition law. Recommend retaining the geometric corollary and exposing the unrestricted parent; the scalar-one experiment is supporting evidence, not a mandatory competing public theorem. No unsupported claim that all finite-characteristic extensions force changing this result.

## 4c. Nine modern-idiom checks

| # | Diagnostic | Finding / concrete downstream consequence |
|---|---|---|
| 1 | Typeclasses in place of preambles | Already CommSemiring and bundled linear operators. Disjoint is a value-level relation on two arguments, not a missing global instance. |
| 2 | Filters/nets | No topology/convergence; n/a. |
| 3 | Universal properties | Translation coaction/iterative HS action organizes the parent law, but needs a canonical polynomial instance. No existing bundled action shortcut verified. |
| 4 | Bundled substructures | Operators already LinearMaps; bundled composition identity verified, enabling LinearMap.comp substitution/extensional rewriting without changing mathematical generality. |
| 5 | Vector spaces → modules | Already semiring-level, no field/inverse assumptions. Abstract module families require an actual iterativity law, not just linearity. |
| 6 | Higher categorical language | Graded-bimonoid literature is relevant explanation, but no necessary categorical reorganization of this elementary law demonstrated. |
| 7 | Abstract index type | σ is fully arbitrary. Natural finite multi-orders are essential coordinate polynomial data. Finsupp.disjoint_iff offers equivalent lattice notation. |
| 8 | Concrete proof through abstract predicate | Diagnostic fires: **yes**. In the production proof the first composition-rewrite line contains hasseDeriv once (in the parent theorem name); no later proof-body occurrence remains. The operator survives in the goal only as a common scalar-module element. Parent composition rewrite leaves the canonical operator as a common scalar module element. Remaining content is factor=1 from support disjointness. An arbitrary family with a supplied composition law has the analogous one_smul corollary, but that premise includes the entire operator normalization; it is not existing mathlib proof of the concrete family. Generic one_smul already exists. |
| 9 | False-generalization guard | Reject unrestricted removal of support condition, arbitrary HS Leibniz without iterativity, and treating ordinary derivative factorial division as valid in characteristicp. Actual ℕ counterexample verifies the first rejection; ZMod2 witness verifies why the cast condition is only sufficient rather than an equivalent support reformulation. |

Modern idiom available: equivalent bundled/lattice shapes exist; **no material mathematical modernization requiring replacement of the geometric corollary**. The bundled form is useful alongside the pointwise form. The actual caller rewrites backwards under arbitrary polynomial input with an already available support-disjoint witness, so the current form applies directly.

## 4.5. Infrastructure risk

n/a—theorem introduces no new structure, reduction rule or instance. All six dimensions checked: no typeclass diamond; no new reducibility exposure; no noncanonical object unfolding; no instance priority; no new universe constraint beyond the parent; no new coercion. This does not replace the separate risk assessment of the parent definition.

## 4.6. Five proof-strategy checks

| # | Question | Finding |
|---|---|---|
| 1 | ε–δ vs filters | n/a, algebraic finite identity. |
| 2 | Element algebra vs subobject inclusion | No ideal/submodule inclusion. Bundled LinearMap.comp proof is equivalent; the scalar finite-product proof is naturally coordinatewise. |
| 3 | Sequences vs nets | n/a, no limits. |
| 4 | Construction vs universal property | No object is constructed in this theorem; translation coaction belongs to proving parent iterativity. |
| 5 | Missing helper API | Yes: multivariate parent hasseDeriv_hasseDeriv is new API to upstream with hasseDeriv and coeff_hasseDeriv. Optional hasseCoeff support-factor=1 helper is finite-product wrapper, not an independent large result. |

Strategy: **MATHLIB-IDIOMATIC**, applying the general parent law and reducing coefficient product to1. No proof duplication by repeating the full coefficient/cocycle calculation in production. The isolated raw witness does repeat it strictly for assessment verification.

## 5. Actual five-method search

Full exact formal responses in formal-search.json; source commands/results in source-search.json. These establish usable candidates, not global absence.

| Method | Current / literature / abstract actual query | Result |
|---|---|---|
| Finder | Hasse derivatives multi indices with disjoint supports compose to derivative of sum; iterative higher divided partial derivatives independent variables compose; LinearMap composition coefficient shift operators disjoint Finsupp support binomial product equals one | Polynomial.hasseDeriv_comp and LaurentSeries.hasseDeriv_comp are analogues; other hits analytic derivatives/unrelated linear composition. |
| Loogle | "hasseDeriv","disjoint"; Polynomial.hasseDeriv(_),Polynomial.hasseDeriv(_); Disjoint,Finsupp.support | Current no hit; univariate derivative facts; abstract successful retry gives Finsupp.disjoint_iff, support_single_disjoint, prod_add_index_of_disjoint. First abstract Finset.Disjoint identifier invalid; corrected requests hit rate limits before success. Rejected attempts retained. |
| LeanSearch | Same three independently executed natural-language forms as Finder | Current mostly sum/analytic derivatives, abstract general linear-map facts. No matching concrete multivariate operator identity. |
| rg | Full target name, hasseDeriv_comp/HS/iterative derivations; pinned polynomial/MvPolynomial sources; product/disjoint patterns | Only existing univariate/Laurent composition, finite-product/disjoint infrastructure. Full explicit target-name/source caller searches untruncated. |
| local name | hasseDeriv_hasseDeriv_of_disjoint; hasseDeriv_comp; prod_eq_one | Source fallback finds project target, pinned composition analogues and generic product lemmas. Index unavailable, so no empty-index absence inference. |

Pinned Polynomial.hasseDeriv_comp takes natural orders and **Semiring** polynomial coefficients, not an arbitrary σ-family; transporting each of arbitrary many coordinates via separate polynomial equivalences is not a ≤3call proof. LaurentSeries analogue is a different carrier too. Finsupp.disjoint_iff changes only the support predicate, not the operator law.

Fresh isolated raw native code imports only mathlib. #check_failure guards confirm the exact project target and parent operator are not available under those imports; a reconstructed delta family requires coefficient induction and a product-binomial cocycle before proving the separated law. Native exact? positive control is recorded; no negative search timeout is treated as absence. The mathematical missing API is explicit, not an inference from search emptiness.

## 5.5. Three statement-shape checks

1. **Normal form**: Δd(ΔeP)=Δ(d+e)P reduces nested derivatives on RHS; no unconditional simp attribute to force proof obligations. Bundled .comp equality verified; same law.
2. **Syntactic generality**: swapped orders verified; implicit d,e inferred from h/P usage; h:Disjoint d e via Finsupp.disjoint_iff is equivalent. Current support witness is already constructed at sole caller, so a forced restatement brings no demonstrated application gain.
3. **Superfluous arguments**: actual type uses σ,R,d,e,P and h; no inherited Fintype/DecidableEq/Nonempty assumptions. Literal Semiring parent fails; dropping h rejected by concrete native counterexample. Scalar criterion checked separately.

Shape verdict: **KEEP-CURRENT-SHAPE**, optionally supply bundled form with parent API.

## 6. Composition, callers and inline audit

| Explicit caller | Use | Validation and refactor implications |
|---|---|---|
| Roth.hasseDeriv_rename_mul_aeval, Roth/Separation.lean:156 | Reverse rewrite of Δ(d.mapDomain some+single none ν) into successive derivatives; hdisj proved from Option.some/none variable separation | Exact support construction plus rewrite replay checked for arbitrary Option-indexed P in separated_caller. This validates the algebraic rewrite fragment, not a new full build of Separation. Production unchanged and baseline hashes match. |

Internal use count0. Exactly1explicit executable invocation; module's doc-comment mentions are not callers. Broad inline grep includes the general composition in Index113 (not an invocation of this theorem), source general theorem proof, and Option-separated hdisj proof. Source-level references do not certify opaque kernel or simp dependency closure; this theorem has no simp attribute. Indirect separated determinant call at Separation365 is through hasseDeriv_rename_mul_aeval and is not another direct call.

Composition result: **NOT-COMPOSABLE from existing pinned mathlib in ≤3calls** for the concrete operator. Local parent+Finset.prod_eq_one+one_smul is short but parent is the newly proposed project contribution, so cannot support NO-composable. Root independently replayed the theorem and full raw construction without importing project definitions in isolated code. If parent is upstreamed, retain this geometric corollary as part of the same API: it prevents repeating a support-product calculation at separated-coordinate consumers. No claim that this is an independent deep theorem.

## 7. Verdict and action

**YES-add-as-is.** Gap: a reusable variable-separation composition law for the new multivariate polynomial Hasse operator. Its substance is standard characteristic-free coordinate independence, and it directly supports independent blocks of variables in algebraic determinant and differential-operator arguments. Existing univariate iteration and generic finite-product lemmas do not provide the canonical arbitrary-variable law by themselves. The geometric interface has a direct consumer and avoids exposing normalization arithmetic there. Its inclusion is conditional on shipping the parent API; no standalone addition against nonexistent mathlib definitions is proposed.

- Upstream path: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean.
- Proposed PR title: feat(Algebra/MvPolynomial/HasseDeriv): add composition for disjoint differential orders.
- Group with accepted YES hasseDeriv, coeff_hasseDeriv, hasseDeriv_map, hasseDeriv_rename and hasseDeriv_hasseDeriv; helper hasseCoeff gets inlined/reviewed as appropriate.
- Before PR: `/generalise MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`; preserve verified scalar-condition findings; `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`; settle consistent pointwise/bundled naming, prove full module and downstream checks.
- Reviewer candidates Yaël Dillies and Moritz Firsching from actual pinned recent history of polynomial Hasse/MvPolynomial derivative files (reviewer-commits.json). This is a suggestion, not an external contact.
- Alternative destination if maintainers prefer a minimal parent API: keep the named geometric corollary project-local in Roth/HasseDeriv.lean and use the now-upstream parent rule. No deletion is performed here.

## 8. Evidence and verification

The accepted raw snippet reconstructs the Hasse operator, proves its coefficient law, choose cocycle, full iterativity, and then disjoint-support specialization. The accepted final disk snippet includes actual target type/axioms, independent replay, bundled and swapped shapes, scalar-one and natural-factor conditions, Option-separated caller fragment, ℕ overlap counterexample, and characteristic2overlap witness. All accepted diagnostics are complete successes with no errors or warnings and only propext/Classical.choice/Quot.sound axioms (or no axioms). Rejected attempts are retained separately and are not accepted proof evidence. Exact sources are archived as .lean.txt, with actual execution paths in raw receipts. No sorry/unsafe/native_decide/newaxioms/raisedlimits.

See verification.json for exact accepted source/receipt/hash pairs, source-search.json for complete source commands, formal-search.json for all actual five-method results, web-receipts.json and web-sources.json for requests/locators/summaries, input-manifest.json and reference-hashes.json for input integrity, and validate.py for portable read-only checks. Root independently reviews before publication.

Limits: optional ask_chatgpt_math unavailable; local symbol index unavailable; nLab direct XHTML400/nCatLab direct path unavailable; external indexes may differ from pinned version; native caller experiment verifies scoped rewrite and support construction, not full project rebuild or implicit dependency closure. These do not constitute unresolved proof obligations.
