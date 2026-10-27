# MvPolynomial.eval_eq_sum_box — declaration 74/293

**Verdict: YES-but-generalise-first.** Production Lean sources and version pins remain unchanged. This is the last declaration in Roth/Taylor.lean. All applicable phases, five successful native sets, full Main caller replay and fresh file-milestone build are complete. Root independent acceptance is pending; no partial report is a publishable checkpoint.

## Phase 0 — baseline and exact declaration

Declaration resolves uniquely at **Roth/Taylor.lean217–220**, public theorem, no sorry. The entire declaring module and actual Main347–405 consumer/helper were read. The module develops translation, Hasse coefficient identification, inverse transport, polynomial expansion and its evaluation. Shared baseline is clean, 2467 jobs; [baseline](../evidence/MvPolynomial.eval_eq_sum_box/baseline-build.txt). All17 production source/pin hashes were freshly compared with that baseline and matched: [inputs](../evidence/MvPolynomial.eval_eq_sum_box/inputs.json), [hash check](../evidence/MvPolynomial.eval_eq_sum_box/input-hash-check.json). Exact canonical [metadata](../evidence/MvPolynomial.eval_eq_sum_box/canonical-entry.json) and [order](../evidence/MvPolynomial.eval_eq_sum_box/order-entry.json) are archived.

**Fresh Taylor file-completion full build: PASS**, `lake build`, exit0, **2467 jobs**, **6.669 seconds**, no warnings/errors. [Build receipt](../evidence/MvPolynomial.eval_eq_sum_box/file-completion-build.json), [exact output](../evidence/MvPolynomial.eval_eq_sum_box/file-completion-build.log). This is a real file-milestone run, not a reused baseline or claimed future build. The additional strongest full-center scratch proof was verified afterward; all production sources remained unchanged and their17 hashes were freshly rechecked.

## Phase 1 — mathematical content and full type

Let P be a polynomial in finitely many variables over a commutative ring A. Choose two arbitrary points α,x and coordinatewise natural degree bounds r. The value of P at x is the finite sum, over all multi-indices d bounded by r, of the Hasse derivative of order d evaluated at α, multiplied by the product of (xⱼ−αⱼ) to exponents dⱼ. This is an **exact finite identity**, valid in every characteristic, with no factorial division or analytic remainder.

Full native type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A), (∀ j, MvPolynomial.degreeOf j P ≤ r j) → MvPolynomial.eval x P = ∑ d ∈ Roth.box r, MvPolynomial.eval α (MvPolynomial.hasseDeriv d P) * ∏ j, (x j - α j) ^ d j
```

Parameters: σ is an arbitrary variable type, A an arbitrary commutative ring, Fintype supplies the finite product/box enumeration, DecidableEq supplies the current box construction, α and x are arbitrary centers/evaluation points, r is the coordinate bound and P is the polynomial. Sole mathematical hypothesis hP is ∀j, degreeOf j P≤r j. There is no positive degree, nonzero polynomial, characteristic-zero, domain, field, order, separation of x/α or denominator assumption.

**How:** Apply the evaluation ring homomorphism to `eq_sum_box_hasseDeriv`; homomorphism preservation of sums, multiplication, powers, subtraction, variables and constants turns the polynomial identity into its scalar form. The source does **not** repeat the binomial/Hasse proof. Direct project proof dependency is `MvPolynomial.eq_sum_box_hasseDeriv`; statement additionally mentions `MvPolynomial.hasseDeriv` and `Roth.box`. [Full source](../evidence/MvPolynomial.eval_eq_sum_box/Taylor-module.lean.txt).

## Phase 2 — preliminary checks

**BIG**, independently: the module lists `MvPolynomial.eval_eq_sum_box` under **Main results**, and it is the exact expansion used in the project's Diophantine upper estimate. No inference from the parent declaration's verdict is needed. Literature width remains exhaustive regardless.

One-line-definition check **n/a — theorem**. Its one-line source proof is a corollary of a substantive project theorem, not a one-line definition and not automatically a composition from existing mathlib. No definition exemption is asserted.

## Phase 3 — exhaustive literature protocol

Exact requests, original serialized-response SHA256/bytes, credential-safe URL metadata and concise original summaries are retained in [web0](../evidence/MvPolynomial.eval_eq_sum_box/web-0.json), [web1](../evidence/MvPolynomial.eval_eq_sum_box/web-1.json), [web2](../evidence/MvPolynomial.eval_eq_sum_box/web-2.json), [web3](../evidence/MvPolynomial.eval_eq_sum_box/web-3.json), [web4](../evidence/MvPolynomial.eval_eq_sum_box/web-4.json). Full returned article/search bodies are not archived. Returned URL queries/fragments are removed before storage; no signed download token is evidence.

| Channel | Actual query / locator | Outcome and relevance |
|---|---|---|
| Web specific | multivariate polynomial Taylor expansion Hasse derivatives evaluation arbitrary commutative ring | Primary [Bhargava–Ghosh–Guo–Kumar–Umans, JACM](https://doi.org/10.1145/3652025), §3.2 Definition3.4/Proposition3.5: Hasse derivatives extract translated coefficients over a commutative ring. §7.2 relates values at two points through Hasse derivatives; nilpotence is used for algorithmic truncation, not a restriction on the full finite polynomial identity. |
| Web general | Hasse derivatives polynomial Taylor formula base change algebra evaluation | Same ring-standard framework; evaluation along a coefficient map/algebra homomorphism is natural. The native arbitrary-algebra test, rather than an unsupported bibliographic assertion, verifies the exact proposed Lean form. |
| Web aliases | multivariate divided derivatives Taylor expansion finite characteristic interpolation | Primary [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5) search extract explains Hasse Taylor coefficients for arbitrary fields, motivating factorial-free form. Divided differences/analytic remainder results are different and not used as exact matches. |
| Optional ask_chatgpt_math | standard form/generality/history request | n/a: optional tool unavailable in this session; no simulated consultation or result. Other channels were not reduced. |
| Local references | clean.tex §4 lines500–529; §7 lines1655–1673 | Exact finite coordinate-box Taylor formula over ℝ and its substitution at hⱼ/qⱼ. [Locators/hash](../evidence/MvPolynomial.eval_eq_sum_box/local-literature.json), [excerpts](../evidence/MvPolynomial.eval_eq_sum_box/clean-excerpts.tex.txt). The actual Lean CommRing result is already broader than the real presentation. |
| nLab | site:ncatlab.org/nlab Hasse derivative Taylor polynomial ring | [Hasse–Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative), several-indeterminate section, treats the operators over commutative rigs. This supports not imposing characteristic/field hypotheses on coefficients; subtraction in the displayed difference form still requires additive inverses. |
| nCatLab | site:ncatlab.org/ncatlab polynomial algebra universal evaluation Taylor; later exact-prefix query | No separate exact categorical evaluated Taylor law returned; search exposed nLab free polynomial-algebra context. Direct nCatLab root open was inaccessible. No full category-theoretic result is claimed found; extra higher-categorical reformulation is inapplicable to this finite algebraic identity. |
| Stacks | site:stacks.math.columbia.edu divided power polynomial Taylor expansion; direct tag07H4 | [Divided power polynomial algebras](https://stacks.math.columbia.edu/tag/07H4) opened successfully. Related binomial arithmetic, but divided-power generators have different multiplication: this is **not** an interchangeable generalisation of ordinary polynomial Taylor expansion. |
| MathOverflow | site:mathoverflow.net Hasse Taylor expansion commutative ring, refined quoted query | [Question288218](https://mathoverflow.net/questions/288218/formal-multidimensional-taylor-series-expansion-over-commutative-rings) identifies factorial-free Hasse formulation; Q82970 similarly discusses arbitrary characteristic. Context/corroboration only; primary article and native proofs support the theorem. |
| Recent arXiv (last five years) | site:arxiv.org Hasse multivariate Taylor2022–2026; exact article title retry | [arXiv2205.00342](https://arxiv.org/abs/2205.00342), **submitted30Apr2022**, within five years of assessment date27Oct2026; abstract opened and authors/date confirmed. Multipoint evaluation demonstrates applications beyond Roth. It does not by itself assert the proposed algebra-target Lean statement. |

Access honesty: the primary JACM search response exposed the relevant §3.2/§7 contents, but the later direct DOI fetch returned **403**. Do not read this as a successful unrestricted article download. The arXiv abstract and Stacks page opened successfully. nCatLab root was inaccessible. No channel is marked a no-hit proof of mathematical absence.

**Synthesis:** standard name is exact algebraic multivariate Taylor expansion in Hasse derivatives, equivalently divided/binomial partial derivatives. Literature varies between fields and rings, polynomial identity versus scalar evaluation, coordinate-box or support/total-degree summation, and ordinary factorial-normalized versus Hasse operators. CommRing with no characteristic restriction is an appropriate difference-form coefficient setting. Algebra evaluation composes the same polynomial identity with a homomorphism; it preserves this exact mathematical content. No analytic topology, remainder or convergence condition belongs here.

## Phase 4a–4b — all parameters and verified generality

| Parameter / condition | Mathematical role | Generality outcome |
|---|---|---|
| σ : Type* | arbitrary finite variable labels | Keep arbitrary labels and independent universes; no Fin n specialization. |
| A : Type*, CommRing A | coefficients, differences x−α | No field/domain/CharZero needed. Same-ring difference form stays CommRing; in the verified scalar-extension form coefficient A only needs CommSemiring, while target B remains CommRing. |
| Fintype σ | full coordinate product and finite box | Retain for this representation; a support-indexed theorem would use a different sum/product, not a mere binder deletion. |
| DecidableEq σ | current construction of box | Verified removable as explicit input: statement-scoped Classical fixes box construction; original arbitrary supplied instance recovered using Subsingleton.elim and cases, propositionally rather than claimed definitionally. |
| α : σ→A | expansion center | Arbitrary, including zero; strongest verified form allows α : σ→B, including centers outside the image of A. No nonzero or distinct-coordinate requirement. |
| x : σ→A | evaluation point in coefficient ring | Verified widen BOTH α/x to σ→B for arbitrary CommRing A-algebra B; coefficients A may be CommSemiring. Evaluate P and its Hasse derivatives with aeval. Original recovered at B=A. |
| r : σ→ℕ | finite coordinate bounds | May be zero and may strictly exceed actual degrees. Natural multi-indices are polynomial exponents, not a spurious concrete numerical index. |
| P : MvPolynomial σ A | polynomial to expand | Arbitrary, including zero/constants. |
| hP : ∀j, degreeOf j P≤r j | prevents out-of-box terms | Keep. Removing the bound while retaining an arbitrarily small box would lose terms; no same-statement weakening proposed. |

**STRICTLY NARROWER THAN STANDARD / MODERN IDIOM.** The strongest verified restatement removes explicit DecidableEq, weakens coefficients from CommRing A to **CommSemiring A**, and allows **both center and evaluation point in an arbitrary commutative ring A-algebra B**. Original CommRing A=B and arbitrary supplied equality decision recover **propositionally, not definitionally** via Subsingleton.elim/cases. The full original Main estimate passes from this recovery as well as the two earlier recovery routes. Cost MODERATE but mechanical: coefficient-map degree transport plus Hasse-map/evaluation compatibility, with no new mathematical foundation.

Recommended signature (complete accepted proof is archived):

```lean
open Classical in
theorem target {σ A B : Type*} [CommSemiring A] [CommRing B] [Algebra A B] [Fintype σ]
    (α x : σ → B) (r : σ → ℕ) (P : MvPolynomial σ A)
    (hP : ∀ j, degreeOf j P ≤ r j) :
    aeval x P = ∑ d ∈ Roth.box r, aeval α (hasseDeriv d P) *
      ∏ j, (x j - α j) ^ d j
```

The proof maps P along algebraMap A B. Its degree bound follows from support_map_subset, degreeOf_le_iff and monomial_le_degreeOf; apply the already verified same-ring evaluated formula over B, then hasseDeriv_map and eval₂_eq_eval_map identify each evaluated derivative. No injectivity of algebraMap is assumed: coefficient maps can only remove support, which suffices for the bound. Independent universes are retained. The earlier verified center-in-A/algebraMap-valued formula is an **intermediate**, not falsely declared maximal. [Structured generality](../evidence/MvPolynomial.eval_eq_sum_box/generality.json).

## Phase 4c — nine modern-idiom rows

| # | Diagnostic | Answer, actual proposal and downstream value |
|---|---|---|
| 1 | Hypotheses versus typeclasses | Ring, finite enumeration and any scalar extension are already represented by typeclasses. Remove computational equality binder only through verified scoped Classical transport. No custom condition is introduced. |
| 2 | Filters/nets versus metrics | No: finite polynomial equality, no topology or limits. |
| 3 | Construction versus universal property | Evaluation is already the universal algebra homomorphism `aeval`; no new universal-property class is needed. Expose algebra-target form rather than a duplicate evaluation construction. |
| 4 | Closure predicates versus bundled substructure | No set-with-closure hypothesis. Degree-bounded submodules could package many polynomials but would add burden to the actual one-polynomial rewrite. |
| 5 | Hierarchy weakening | Original already CommRing, broader than real/field literature. Strongest verified scalar-extension form weakens coefficient A to CommSemiring while preserving CommRing in target B for differences. This is an actual checked weakening, not an unsupported subtraction-free same-ring claim. |
| 6 | Higher categorical generalisation | No: no categorical result or coherence data; abstraction for its own sake would not improve this identity. |
| 7 | Concrete index generalisation | σ arbitrary; natural exponents integral to ordinary polynomials. Arbitrary additive-group exponents would change to Laurent/group algebras and a different Hasse theory. |
| 8 | Concrete-via-abstract proof diagnostic | **Fires:** one proof line applies `congrArg (eval x)` to one project polynomial expansion. The transport uses homomorphism laws. Recommended arbitrary ring A-algebra evaluation allows BOTH center and point in B and uses existing `aeval`; its proof maps coefficients once and transports degrees/Hasse derivatives. Users need not manually map P to state or invoke the formula. It does **not** eliminate the Hasse expansion premise or replace it with mathlib. [Diagnostic](../evidence/MvPolynomial.eval_eq_sum_box/proof-body-diagnostic.json). |
| 9 | False-generalisation guard | Scoped equality choice changes computational representation only, with propositional recovery checked. Algebra evaluation preserves the polynomial identity under scalar interpretation. Replacing by divided-power algebra, an arbitrary function, unrestricted noncommutative images or non-natural exponents changes the object and is rejected. |

**Modern idiom available, verified:** the existing algebra-evaluation universal property supplies an arbitrary target B, allowing scalar extension and ring-valued evaluation without first mapping P into a new polynomial ring. Both center and point may range over B, and coefficients A need only be CommSemiring. The current theorem is the self-algebra CommRing specialization. Scoped Classical removes extraneous computational input with honest instance recovery. This is a real API improvement, not a cosmetic categorical restatement.

## Phase 4.6 — five proof-strategy rows

| # | Question | Outcome |
|---|---|---|
| 1 | ε–δ versus filters | n/a finite algebraic identity. |
| 2 | Element reasoning versus substructures | Existing homomorphism transport is already abstract; an ideal/submodule theorem would not shorten or clarify scalar equality. |
| 3 | Sequences versus nets | n/a no limits. |
| 4 | Ad hoc construction versus universal property | `eval`/`aeval` already use the polynomial universal property. Do not reconstruct an evaluation map. |
| 5 | Missing helpers mathlib should have | **Yes:** multivariate Hasse coefficient law and finite Taylor polynomial expansion, then this evaluation corollary. These are the substantive gaps. Generic preservation of sums/products/constants already exists; do not create wrappers for them. |

**MATHLIB-IDIOMATIC** mathematical strategy: transport the polynomial expansion once. Generalise both center/point and the coefficient ring hierarchy, and suppress extraneous equality-decision input before upstream submission; do not repeat a binomial induction merely to make the scalar theorem appear independent. Cost CHEAP for same-form binder removal, MODERATE for strongest coefficient-map degree/Hasse transport; no cost-based omission of the broader verified form. No cost-based verdict downgrade.

## Phase 4.5 — infrastructure risk

**n/a — theorem**, introducing no definition, instance, reducibility equation or coercion. Each of six rows is explicitly inapplicable: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe restriction from new data, coercion competition. Original and proposed statements are native-checked; this does not manufacture a new instance risk assessment for a theorem.

## Phase 5 — actual five-method mathlib search

All methods executed on **current**, **literature-standard**, and **abstract** forms; raw requests/responses: [formal-search](../evidence/MvPolynomial.eval_eq_sum_box/formal-search.json). Methods can find presence; empty search is not proof of absence. External indexes may differ from the pinned revision, so positive candidates are checked against pinned sources/native tools.

| Method | Three actual forms | Findings / limitation |
|---|---|---|
| Lean-Finder | multivariate polynomial value/box Hasse product differences; Hasse Taylor formula over ring; evaluate expansion along algebra hom | Returns univariate `Polynomial.taylor_coeff`, `sum_taylor_eq`, analytic taylorWithinEval and generic evaluation/expand laws. Analytic approximation is not this exact identity. |
| Loogle | `MvPolynomial.eval, "sum"`; `Polynomial.taylor, "sum"`; `MvPolynomial.aeval, "sum"` | `eval_sum`, `Polynomial.sum_taylor_eq`, `aeval_sum`. All3 query responses successful. Finite-field root-count/sum-vanishing hits are not Taylor. |
| LeanSearch | evaluated multivariate Hasse box law; ring-standard Taylor at arbitrary point; arbitrary-algebra finite coefficient/monomial sum | `eval₂_eq`, `eval₂_eq'`, `eval_eq'`, univariate `taylor_eval_sub`, `taylor_coeff`. These supply evaluation or univariate inputs, not multivariate Hasse coefficient identification. |
| rg pinned source | current eval/Taylor, literature Hasse, abstract eval₂/aeval transport plus full untruncated candidate-name grep | [Current](../evidence/MvPolynomial.eval_eq_sum_box/rg-current.json), [literature](../evidence/MvPolynomial.eval_eq_sum_box/rg-literature.json), [abstract](../evidence/MvPolynomial.eval_eq_sum_box/rg-abstract.json), [full name](../evidence/MvPolynomial.eval_eq_sum_box/rg-full-name.json). No exact full-name hit in mathlib. Positive complete pinned sources/hashes retained. |
| lean_local_search | eval_eq_sum_box; sum_taylor; eval₂_eq | Own theorem/univariate/generic evaluation candidates through source fallback. **Index unavailable for all3**. The abstract fallback is noisy (also historical evidence copies), so no indexed absence claim is made. |

Pinned positives: `Polynomial.sum_taylor_eq` Taylor208 requires **CommRing**, despite Finder's informal description saying semiring; formal type wins. `Polynomial.taylor_eval_sub` Taylor204 transports univariate evaluation. `MvPolynomial.eval₂_eq` Eval72 sums coefficients over support with support-coordinate product; `eval₂_eq'` Eval76/`eval_eq'`263 use full product with Fintype. `aeval_sum`698/`aeval_prod`702 and `aeval_X`587/`aeval_C`590 distribute evaluation. These do not supply multivariate Hasse coefficients or degree-box padding. A generic aeval-sum statement conditional on the desired expansion is a transport lemma, not a mathlib proof of Taylor's theorem.

## Phase 5.5 — statement shape

**Normal form:** equivalent formulations are polynomial reconstruction73, scalar evaluation74, algebra evaluation, support-indexed translation sum and coefficient identity63. The coefficient identity is the foundational normal form; polynomial reconstruction and scalar evaluation are natural derived API layers. Existing generic evaluation has canonical aeval/eval₂ spelling. The RHS expansion is suitable for the actual `rw` consumer; do not add both orientations as simp rules. This theorem is currently not tagged simp.

**Syntactic generality:** α/x/r/P explicit and hP pointwise match the actual Main rewrite. The strongest arbitrary-algebra theorem uses aeval at both B-valued center and point with coefficient A only CommSemiring; the original self-algebra evaluation is recoverable without changing Main's real statement. A separate scalar corollary may remain for convenient rewrites if maintainers want it; no blanket wrapper rule counts a newly contributed substantive parent as an already existing mathlib replacement.

**Superfluous-argument audit:** CommRing needed in the target for differences; coefficient CommSemiring is verified sufficient in the widened form. Fintype is needed for box/full product, α/x/r/P are meaningful values and hP prevents missing terms. Explicit DecidableEq is the verified computational requirement to suppress, not a mathematical finiteness condition. No hidden nonzero/positivity/characteristic assumption is present. **RESTATE-BEFORE-SHIP** with the successfully verified targets below; no untested weakening is marked complete.

## Phase 6.0 — actual callers, inline audit and duplication

| Exact named caller | Location | Pattern and action |
|---|---|---|
| `Roth.abs_eval_lt_of_le_index` | Roth/Main.lean390 | Rewrites the evaluation of Q at rational approximants into the box sum; subsequently bounds each term by index and Hasse derivative estimates and uses cardinality. Full consumer plus its actual private product-weight helper are replayed against the fresh evaluated law. |

**K=1 use outside the declaring file, one distinct file.** Docstring references and own declaration excluded. Explicit named-use search is not a claim to complete opaque kernel/simp closure. [Caller inventory](../evidence/MvPolynomial.eval_eq_sum_box/callers.json), [caller grep](../evidence/MvPolynomial.eval_eq_sum_box/rg-callers.json), [inline search](../evidence/MvPolynomial.eval_eq_sum_box/rg-inline.json). No independently rederived complete evaluated Hasse box formula was found. Other box sums count/bound values, while generic coefficient evaluation uses different coefficients.

| Decl A | Decl B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| eval_eq_sum_box | eq_sum_box_hasseDeriv | No: value identity versus polynomial identity | Evaluation transports substantive expansion | Derive scalar/algebra API; no repeated binomial proof. |
| eval_eq_sum_box | coeff_taylor | No: full finite scalar sum versus one translated coefficient | Uses polynomial reconstruction downstream | Foundation versus application layers; retain distinction. |
| eval_eq_sum_box | MvPolynomial.eval_eq' | No: Hasse coefficients at α and powers x−α versus original coefficients/powers x | Generic sum is a building block | Need new coefficient translation/box cutoff bridge. |
| eval_eq_sum_box | Polynomial.sum_taylor_eq | Same motif, different variable/index type | Generic evaluation after univariate expansion cannot identify multivariate Hasse data | Group useful analogues, not a direct duplicate. |
| eval_eq_sum_box | abs_eval_lt_of_le_index | No: exact algebraic identity versus strict analytic bound | Consumer applies identity then term/cardinality estimates | Keep algebra theorem independent of real/order assumptions. |

**KEEP**: standard exact theorem with real downstream use; not junk merely because source proof is one line or K=1. Once a full multivariate Taylor API is upstream, maintainers may choose how many evaluation convenience corollaries to expose; that later packaging does not turn a missing mathematical premise into an existing library fact.

## Phase 6 — actual composition and native verification

**Five accepted native sets**, all complete/nonpartial, success=true, no errors/warnings/failed dependencies, standard axioms only (propext, Classical.choice, Quot.sound). No sorry/admit/new axiom/unsafe/native_decide or resource-limit raise in accepted sources.

- [Target exact fragment](../evidence/MvPolynomial.eval_eq_sum_box/native-target-executed.lean.txt), [receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-target-success.json): original full type/print/axioms, original-shaped replay using fresh73, no-DecidableEq theorem and original-instance recovery. The fresh73 prerequisite fragments are separately retained: [inventory](../evidence/MvPolynomial.eval_eq_sum_box/prerequisites.json), [expansion](../evidence/MvPolynomial.eval_eq_sum_box/prerequisite73-target-executed.lean.txt), [recovery](../evidence/MvPolynomial.eval_eq_sum_box/prerequisite73-extra-executed.lean.txt). They are not relabeled independent74 executions.
- [Consumer exact fragment](../evidence/MvPolynomial.eval_eq_sum_box/native-consumers-executed.lean.txt), [receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-consumers-success.json): **full actual Main strict estimate plus private monomial power-weight helper**; evaluated-law call replaced by fresh74 recovery, no whole-target exact call.
- [Algebra exact fragment](../evidence/MvPolynomial.eval_eq_sum_box/native-algebra-executed.lean.txt), [receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-algebra-success.json): arbitrary independent-universe commutative A-algebra target, original self-algebra/arbitrary-DecidableEq recovery, and **full Main estimate again** using this broader recovery.
- [Isolated raw exact source](../evidence/MvPolynomial.eval_eq_sum_box/native-raw-executed.lean.txt), [receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-raw-success.json): no Roth imports; missing own-target guard; reconstructs shifted support polynomial independently, evaluates it along explicit RingHom A→+*B, and verifies positive univariate reconstruction evaluation. This has no Hasse identification or box-padding result and needs no Fintype in its support-indexed form.

- [Strongest full-center exact fragment](../evidence/MvPolynomial.eval_eq_sum_box/native-fullcenter-executed.lean.txt), [receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-fullcenter-success.json): coefficient CommSemiring A, arbitrary independent-universe CommRing A-algebra B, BOTH α/x B-valued, no explicit DecidableEq. Full proof transports coordinate-degree bounds by support_map_subset and uses hasseDeriv_map/eval₂_eq_eval_map. Original arbitrary-equality-instance statement recovered, and **full Main estimate replayed a third time** using this strongest recovery. Complete clean success first try, standard axioms; no new rejected preparation.

One algebra preparation contained only a long rewritten-line style warning, corrected by wrapping; [rejected source](../evidence/MvPolynomial.eval_eq_sum_box/native-algebra-rejected-1.lean.txt), [rejected receipt](../evidence/MvPolynomial.eval_eq_sum_box/native-algebra-rejected-1.json). It is not accepted proof evidence. A warming/partial response after new Main import was not counted as success; only final complete native receipts are accepted. No mathematical error is hidden behind a recovered placeholder.

Composition1: use `Polynomial.sum_taylor_eq` then evaluation. This succeeds for one variable in a univariate polynomial, but arbitrary σ→₀ℕ exponents and multivariate Hasse data are not a one-call specialization. No bijection from σ to Unit is available, and iterating polynomial presentations requires additional arguments.

Composition2: use `MvPolynomial.eval₂_eq'` on a translated polynomial and normalize x−α. This supplies a coefficient sum over its support, but two substantive ingredients remain: those coefficients are evaluated Hasse derivatives, and all terms outside the specified box vanish. They are project facts63/73, not existing mathlib mathematical calls. The native raw probe tests generic transport/expansion boundary rather than importing Roth and misidentifying the target as already present.

Composition3: the exact source uses `congrArg (eval x)` plus simplification **and `eq_sum_box_hasseDeriv`**, a newly assessed project theorem. This is an excellent derived project proof; it cannot justify `NO-composable-from-mathlib` because the crucial premise is absent from pinned mathlib. The Phase6b closing-simp heuristic alone also cannot erase this missing premise. No parent re-aim rule applies: the parent has a verified YES-generalise verdict, not an already existing more-general replacement.

**NOT-COMPOSABLE from≤3 existing mathlib mathematical calls.** Scope is the pinned environment and performed successful positive/composition tests; no failed search or rejected proof attempt is an absolute absence theorem.

## Phase 7 — actionable verdict and upstream plan

**YES-but-generalise-first: remove explicit equality-decision input, weaken coefficients to CommSemiring A, and allow both center and point in any CommRing A-algebra B.** The exact multivariate finite Hasse Taylor identity is a standard reusable algebraic tool, with applications to interpolation, multiplicity and evaluation algorithms beyond Roth. Existing mathlib supplies homomorphism transport and univariate Taylor results, but lacks the multivariate Hasse coefficient/finite-box expansion premise. A one-line proof conditional on that new premise is a sensible API corollary, not evidence that pinned mathlib already proves the theorem. The full original and generalised forms and the actual strict estimate consumer were verified, rather than just searching and proposing them.

Proposed file **Mathlib/Algebra/MvPolynomial/Taylor.lean**; proposed PR title **feat(Algebra/MvPolynomial): evaluated finite Hasse Taylor expansion**. Group with actual accepted YES declarations **MvPolynomial.eq_sum_box_hasseDeriv**, **MvPolynomial.coeff_taylor**, **MvPolynomial.hasseDeriv**, **MvPolynomial.coeff_hasseDeriv**; their actual verdicts were checked in progress, not inferred from useful names: [group evidence](../evidence/MvPolynomial.eval_eq_sum_box/proposed-pr-group.json). Expose the strongest B-valued center/point aeval theorem with coefficient CommSemiring; recover original scalar evaluation by taking B=A with CommRing A, and decide whether a named scalar corollary improves rewriting based on real consumers. This packaging choice is a future upstream decision, not unfinished assessment or a reason to discard the substantive result.

Before upstream submission:

- Run `/generalise MvPolynomial.eval_eq_sum_box` using the **verified strongest** coefficient-CommSemiring/B-valued-center-and-point/no-explicit-DecidableEq signature and original-instance recovery. Keep the degree bound, natural exponents, finite-box representation and CommRing assumption in target B; coefficient A only needs CommSemiring.
- Coordinate the foundational coefficient/polynomial expansion and replace downstream Roth.box branding with standard Finsupp interval/finite-box API. This upstream representation migration is a future implementation task, not falsely marked verified by this read-only assessment.
- Run `/cleanup Mathlib/Algebra/MvPolynomial/Taylor.lean MvPolynomial.eval_eq_sum_box`, complete import/dependent/simplification/performance submission gates, and retain exact full Main consumer validation. The survey's actual native/full-build gates are already complete; upstream submission gates are not silently equated with them.
- Suggested reviewers **Yaël Dillies** (coefficient refactor631b214f7c) and **Aaron Liu** (Eval cleanup274ed6d67d), based on recent relevant [Git history](../evidence/MvPolynomial.eval_eq_sum_box/reviewer-history.json). No availability promise, external PR, contact or message is made.

All applicable assessment phases complete; unresolved=[]; no required user input. Production remains unchanged. Root must independently accept, then update overview/progress and commit/push the completed declaration to the assigned branch.

## Phase 8 — completion and evidence

Production Lean, project structure and versions remain unchanged. All required literature/search, parameter/idiom/strategy/shape/caller/duplication and native verification is complete; actual successful native evidence and fresh Taylor file-milestone full build are incorporated. Root independently reviews/accepts the finished package before overview/progress update, commit and push. No external PR/reviewer message is sent.

[Assessment](../evidence/MvPolynomial.eval_eq_sum_box/assessment.json), [verification](../evidence/MvPolynomial.eval_eq_sum_box/verification.json), [overview entry](../evidence/MvPolynomial.eval_eq_sum_box/overview-entry.json), [portable validator](../evidence/MvPolynomial.eval_eq_sum_box/validate.py), [current manifest](../evidence/MvPolynomial.eval_eq_sum_box/copy-manifest.json). Validators check the current manifest; worker-copy-manifest is historical only if root preserves it. Local evidence links resolve in scratch and integrated layouts. Rejected preparation attempts are separate and never accepted proof evidence.
