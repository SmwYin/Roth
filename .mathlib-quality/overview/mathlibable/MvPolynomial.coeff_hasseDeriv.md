# Full /mathlibable assessment — `MvPolynomial.coeff_hasseDeriv`

**Verdict: YES-add-as-is.** This is the substantive coefficient interface of the characteristic-free multivariate Hasse derivative, rather than a definitional wrapper. It fills the arbitrary-variable counterpart of `Polynomial.hasseDeriv_coeff`. The new abstract and alternative-implementation witnesses tested below are not pre-existing mathlib replacements. Assessment completed on 2026-10-26; independent root acceptance is pending.

Scope: the public theorem at `Roth/HasseDeriv.lean:89`, branch `ramin-cleanup`, Lean v4.34.0, pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`. No production source, pin or tracked file was edited by this assessor. Links use the eventual tracked report/evidence layout. Raw formal-tool results are retained; web evidence contains exact requests, response digests, access outcomes, bibliographic locators and original summaries, with no copied full responses or articles.

## Phase 0 — Doctor

All **17/17 production-source and pin hashes match** the shared clean baseline (exit 0, 2467 build jobs). Reuse is conditional on the actual comparison, not the earlier reports' existence. [Hash comparison](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/baseline-hash-verification.json), [input manifest](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/input-manifest.json), [baseline build](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/baseline-build.txt), [branch receipt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/branch.json).

The declaration resolves uniquely and elaborates. Native inspection captures the actual type, full proof term and axioms; an independent copy of the induction proof closes without invoking the assessed theorem. [Raw native target receipt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/target-lsp.json). [Executed target inspection and independent proof](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/target-executed.lean). Only standard `propext`, `Classical.choice`, `Quot.sound` occur. The target has no `sorry`, unsafe/native trust, axiom declaration, raised limit or `[simp]` attribute. [Exact written excerpt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/target-excerpt.lean).

Actual type:

```lean
MvPolynomial.coeff_hasseDeriv.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
    [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (MvPolynomial.hasseDeriv d P).coeff e =
      (MvPolynomial.hasseCoeff d (e + d) : R) * P.coeff (e + d)
```

The module develops multivariate Hasse derivatives, their coefficients, composition, partial derivatives and compatibility with univariate Hasse differentiation.

## Phase 1 — Comprehend

Let `P` be a polynomial in an arbitrary set of variables over a commutative semiring. After taking its Hasse derivative of multiorder `d`, the coefficient at exponent `e` is the original coefficient at `e+d`, multiplied by the product of binomial coefficients `binom(e_j+d_j,d_j)` over the finite support of `d`. Terms whose original exponents do not dominate `d` vanish; every surviving exponent has a unique predecessor, so no different input monomials contribute to the same output coefficient.

| Parameter | Role / hypothesis |
|---|---|
| `σ : Type u` | Arbitrary variable set, including empty and infinite types |
| `R : Type v` | Coefficient carrier in an independent universe |
| `[CommSemiring R]` | Pinned polynomial type, natural casts, multiplication and linear-map structures |
| `d : σ →₀ ℕ` | Finite differentiation multiorder |
| `e : σ →₀ ℕ` | Finite exponent at which the output coefficient is read |
| `P : MvPolynomial σ R` | Arbitrary input polynomial |

There are no extra propositions: no characteristic-zero, field, domain, nontriviality, finite-variable or decidable-equality assumptions. The conclusion is the equality displayed above. The arithmetic is coefficient multiplication by a natural cast, not division by a factorial.

## Phase 2 — Preliminary checks

**BIG:** the module explicitly lists this theorem among its main results, and its docstring names it the main computational interface. The proof has eleven substantive lines (classical choice, additive polynomial induction, exponent-equality and domination cases). **One-line check: n/a, theorem.** No definition-based exemption or inherited verdict is used. The separately assessed parent definition does not decide this substantive identity's verdict.

## Phase 3 — Exhaustive literature

Every requested channel was actually searched/read or has an explicit availability/relevance outcome. Exact query requests, returned-response SHA256 digests and curated observations are retained in [web1](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/web1.json), [web2](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/web2.json), [web3](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/web3.json), [web4](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/web4.json). A digest identifies the tool-returned representation, not a separately obtained HTTP body. A batched response is not attributed exhaustively to each constituent query.

| Channel | Actual query / access | Outcome and relevance |
|---|---|---|
| Web, specific | `multivariate Hasse derivative coefficient binomial e d polynomial arbitrary ring` | Returned characteristic-free polynomial derivative references. |
| Web, general | `Hasse Schmidt derivation multivariate polynomial coefficient divided powers commutative ring` | Returned the general higher-derivation framework; distinguish the coordinate operator from an arbitrary higher derivation. |
| Web, aliases | `hyperderivative multivariate Taylor coefficients Hasse derivative` | Returned Taylor-coefficient and hyperdifferentiation aliases. |
| ChatGPT MCP | Capability inventory for `ask_chatgpt_math` | n/a: unavailable in this session. No external mathematical consultation is claimed. |
| Local references | Actual `rg` plus read of `clean.tex:120–155` | Exact same coefficient identity is specified in the primary manuscript §1, including commutative-semiring scope. [Search](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-literature.json), [excerpt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-manuscript.txt). |
| nLab | `site:ncatlab.org "Hasse-Schmidt" derivative`; direct Hasse–Schmidt derivative page | Indexed several-variable commutative-rig definition read. Direct fetch failed with unsupported XHTML (400); no full direct-page read claimed. |
| nCatLab | `site:ncatlab.org/ncatlab/ "Hasse" coefficient`; direct `ncatlab/show/graded+bimonoid` | Path inaccessible. Indexed graded-bimonoid context from the nLab-domain search considered; categorical comultiplication is related, but supplies no mechanically stronger coefficient identity. Separate categorical restatement n/a for this coordinate computation. |
| Stacks | `site:stacks.math.columbia.edu "Hasse" "Schmidt"`; `site:stacks.math.columbia.edu "Hasse-Schmidt"`; direct tag 07GK | Direct divided-powers definition read. These maps on an ideal are an adjacent notion, not this coefficient identity. No negative result inferred from a broad batched search. |
| MathOverflow | `site:mathoverflow.net "Hasse derivative" polynomial` | Replacement-for-derivations discussion identifies hyperdifferentiations and jet literature. Context only, not primary authority for the formula. |
| Recent arXiv | `site:arxiv.org "Hasse" "multivariate" "2022"`; `site:arxiv.org "multivariate" "Hasse derivatives" after:2021-10-26`; direct 2205.00342v1 | Primary 2022 full text read, §3.2 Definition 3.4 / property 3.5. Falls within 2021-10-26–2026-10-26. Subsequent find operations locate the coefficient expansion explicitly. |

Primary external mathematical anchor: Bhargava–Ghosh–Guo–Kumar–Umans, [*Fast Multivariate Multipoint Evaluation Over All Finite Fields*](https://arxiv.org/html/2205.00342v1), §3.2. Definition 3.4 defines the derivative by extracting the shifted-polynomial coefficient; property 3.5 gives its binomial-weighted monomial expansion over a commutative ring. Extracting one coefficient from that expansion gives the target identity by the unique exponent `e+d`; this last reindexing is the assessor's mathematical comparison. The [local primary manuscript](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-manuscript.txt) explicitly states the exact identity and extends the coefficient algebra to commutative semirings.

[Stacks tag 07GK](https://stacks.math.columbia.edu/tag/07GK), Definition 23.2.1, concerns divided powers of ideal elements. It is not a replacement formulation of the coordinate Hasse derivative. The [MathOverflow discussion](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) is only search context. No copied external passage is used as mathematical proof.

**Literature summary:** standard name: multivariate Hasse derivative / divided differential operator / hyperdifferentiation. The normalization is binomial, with no factorial denominator; finite-variable fields and commutative rings are common presentations, and the local semiring presentation is strictly no more restrictive. Arbitrary Hasse–Schmidt families and divided powers are related but do not determine these particular coordinate components. No source requires narrowing the arbitrary-variable semiring statement.

## Phase 4a–4b — Generality

| Parameter / hypothesis | Current form | Standard form / weakening analysis |
|---|---|---|
| Variable set | Arbitrary `Type u` | Already covers all finite-variable literature and arbitrary infinite/empty variable sets. No `Fintype`, `Nonempty`, `DecidableEq` to drop. |
| Coefficient carrier | Arbitrary `Type v` | Independent universe; no fixed characteristic or special coefficient ring. |
| Algebra laws | `CommSemiring R` | Local standard scope. Attempting `Semiring S` fails already at pinned `MvPolynomial σ S`, before the proof. Isolated `#check_failure` verifies this. |
| Derivative index `d` | Finitely supported natural function | Finite differential order is the intended object. Allowing an infinite-support order would require a new definition (naturally zero on finite polynomials), not weakening this theorem's binders. Negative orders are integration rather than this differential operator. |
| Coefficient index `e` | Finitely supported natural function | Required by coefficient extraction on a polynomial. Unlike a pointwise upper bound in the scalar vanishing theorem, `e` is an actual polynomial exponent; an unrestricted upper function cannot simply replace it. |
| Polynomial `P` | Arbitrary multivariate polynomial | No degree/support restriction; universal input is needed. A module-valued finitely supported function is a different domain/API, not a mechanically weakened `MvPolynomial` type. |

**Generality verdict: MAXIMALLY GENERAL for this polynomial coefficient identity.** No verified hypothesis weakening is available. The [exact executed isolated source](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/mathlib-executed.lean) and [complete success receipt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/mathlib-lsp.json) contain the independent expanded identity, bundled corollary, rejected semiring weakening and new abstract helper. Both new coefficient proofs have accepted `fail_if_success exact?` checks, with a positive search control earlier in the same file. Explicit `#check_failure` controls reject the project target and an unrelated prior assessment witness, confirming isolation. The isolated semiring rejection checks the type itself. No successful global broadening is claimed from a failed `exact?` search, and cost is not used in the verdict.

### Phase 4c — All nine modern-idiom questions

| # | Question | Answer, proposed form, concrete consequences |
|---|---|---|
| 1 | Preambles → typeclasses | Already uses `CommSemiring` and generic type parameters; no bundled algebra hypotheses to replace. |
| 2 | Sequences/metrics → filters | No topology or convergence. |
| 3 | Construction → universal property | The operator already uses linear extension from monomials. This theorem computes that extension; a new universal characterization does not eliminate coefficient computation. |
| 4 | Closure predicates → bundled substructures | No unbundled closure predicate. A verified optional bundled equality `(lcoeff R e).comp (hasseDeriv d) = (hasseCoeff d (e+d):R) • lcoeff R (e+d)` exposes generic linear-map composition, but the elementwise equality is easier for all eight actual rewriting callers. Keep it as the primary interface. |
| 5 | Field/vector space → module/semiring | Already characteristic-free and semiring-general. `Semiring` rejected by domain; changing to a general module requires a separate coefficient-storage operator. |
| 6 | 1-category → higher category | No categorical statement. Graded comultiplication context gives no concrete stronger coefficient API in pinned mathlib. |
| 7 | Concrete indices → arbitrary additive monoid | Natural multiplicities and binomial weights encode differentiation. Generic shifts on cancellative monoids are broader algebraic machinery, but have no canonical replacement for these binomial weights or polynomial exponents. |
| 8 | Concrete-via-abstract proof diagnostic | **Diagnostic fires:** `hasseDeriv` occurs only in the initial monomial rewrite, with zero later occurrences; the proof then reasons about a weighted lowering operator. A new generic theorem for arbitrary `L`, weight `w`, monomial law and vanishing outside `d ≤ k` is explicitly tested in the accepted isolated batch. It abstracts the collision argument, but adds three data/hypothesis arguments, and none of the eight callers supplies a different operator. No existing downstream proof is blocked by the concrete statement. Thus this is optional helper extraction rather than a required replacement of the characteristic Hasse coefficient API. |
| 9 | False-generalisation guard | The optional arbitrary-lowering theorem really specializes back to the target once the binomial monomial/vanishing laws are supplied; it is a new helper, not evidence that all higher derivations have this formula. Replacing by an arbitrary Hasse–Schmidt derivation or divided powers of an ideal would change the object and is rejected. No meaning-changing widening is accepted. |

**Modern-idiom verdict: no required restatement.** Bundled coefficient maps and a pullback implementation were investigated explicitly. `Finsupp.lcomapDomain` along injective translation `e ↦ e+d`, after coefficientwise binomial weighting, has an immediate coefficient rule. Equating it to the current monomial extension still requires the substantive vanishing/unique-predecessor proof. Switching implementations would exchange which interface is definitional; it does not establish a pre-existing replacement or a stronger mathematical statement. The generic lowering witness is new code and has no evidenced additional project consumer. A hypothetical future reuse alone does not force replacing the natural coefficient lemma with a more cumbersome universal hypothesis theorem.

### Phase 4.5 — Diamond / defeq risk

**n/a: theorem.** No definition, class, instance, coercion or definitional equality is introduced by this declaration. Parent-definition infrastructure risks were assessed separately and are not inherited as this theorem's verdict.

### Phase 4.6 — Proof strategy: all five checks

| # | Question | Applies? / analysis |
|---|---|---|
| 1 | Topology: explicit neighborhoods vs filters | No topology. |
| 2 | Algebra: elements vs substructure inclusions | No submodule/ideal inclusion is being proved. Computing an individual coefficient is the intended computational statement; additive polynomial induction is natural. The verified bundled map identity is an optional corollary, not a shorter proof of the coefficient rule. |
| 3 | Analysis: sequences vs nets | No analysis. |
| 4 | Category theory: construction vs universal property | The linear extension is already bundled; no categorical construction is repeated. |
| 5 | Missing helper API which should be upstream | The generic weighted-lowering coefficient lemma is a possible future extraction. The current proof uses only polynomial induction, coefficient-of-monomial computation and zero-weight reasoning; it does not route around missing filters, universal properties or basic algebraic automation. Its optional extraction merely relocates the same case split until another operator needs it. |

**Proof-strategy verdict: MATHLIB-IDIOMATIC.** The eleven-line induction separates the only essential cases: reconstructed exponent, surviving domination, and zero-weight failure. A sum-based proof modeled on univariate `hasseDeriv_coeff` is equivalent but still needs finite-sum isolation and off-diagonal vanishing. No evidence that changing strategy gives a mathematically superior route. The independent proof succeeds without referring to the assessed theorem; new-witness proofs are distinguished from existing API.

## Phase 5 — Full five-method search

All methods were actually run on the current form, literature form and abstract/generic forms, with a further pullback search. Remote-index versions are discovery aids, never the pinned-source authority. Local searches return positive source hits with **index unavailable**; no empty-index absence inference is made.

| Method | Current form | Literature form | Abstract / modern form |
|---|---|---|---|
| A Lean-Finder | `coefficient of multivariate Hasse derivative of order d at exponent e is product binomial coefficients times coefficient at e+d` | `Taylor coefficient multivariate polynomial divided higher derivative arbitrary characteristic` | `finitely supported sum linear map coefficient formula injective shift with zero weights outside upper set`; further weighted-`comapDomain` query |
| B Loogle | `Polynomial.hasseDeriv, Polynomial.coeff` | `MvPolynomial.coeff, "taylor"` returned unknown-identifier error; retried `"taylor", "coeff"` successfully | `Finsupp.lsum, "apply"`; `"comapDomain", "apply"` |
| C LeanSearch | `coefficient of multivariate Hasse derivative equals binomial coefficient times shifted coefficient` | `Taylor expansion multivariate polynomial coefficients Hasse derivatives` | `Finsupp lsum coefficient at index of sum of monomials injective index map`; further `Finsupp lcomapDomain injective function apply coefficient comapDomain` |
| D Pinned-source rg | Full untruncated `coeff_hasseDeriv|hasseDeriv_coeff`; all MvPolynomial Hasse spellings | MvPolynomial/Polynomial Taylor files and coefficient extraction | `lsum_apply`, `sum_eq_single`, `comapDomain_apply`, `mapDomain_apply_of_injective`, `linearCombination_apply`, plus full pullback source read |
| E Local-name pattern | `hasseDeriv` | `taylor` | `lsum_apply`, `lcomapDomain` |

Raw actual API receipts: [finder current](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/finder-current.json), [finder literature](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/finder-literature.json), [finder abstract](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/finder-abstract.json), [finder pullback](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/finder-pullback.json); [Loogle current](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/loogle-current.json), [literature failure](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/loogle-literature.json), [successful retry](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/loogle-retry.json), [abstract](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/loogle-abstract.json), [pullback](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/loogle-pullback.json); [LeanSearch current](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/search-current.json), [literature](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/search-literature.json), [abstract](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/search-abstract.json), [pullback](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/search-pullback.json); [local current](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-current.json), [literature](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-literature-api.json), [abstract](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-abstract.json), [pullback](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/local-pullback.json). Pinned [full-name search](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/full-name-search.json), [current](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/grep-current.json), [literature](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/grep-literature.json), [abstract](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/grep-abstract.json), [source hashes](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/pinned-sources.json).

[Pinned candidate source snippets and hashes](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/candidate-source-inspection.json) corroborate remote discovery. Candidate audit:

| Candidate | Pinned source / result | Why it does not replace target |
|---|---|---|
| `Polynomial.hasseDeriv_coeff` | `Algebra/Polynomial/HasseDeriv.lean:67` | Exact one-variable analogue, requiring a polynomial in one variable. Arbitrary `σ` is not supplied by one application; recursive reindexing and compatibility would be new proofs. |
| `Polynomial.taylor_coeff` | `Algebra/Polynomial/Taylor.lean` | Shifted univariate polynomial evaluated derivative; not arbitrary multivariate Hasse coefficient extraction. |
| `LaurentSeries.hasseDeriv_coeff` | `RingTheory/LaurentSeries.lean:134` | One integer exponent for a Laurent series; not natural multiindices in arbitrary variables. |
| `MvPolynomial.coeff_pderiv` | `Algebra/MvPolynomial/PDeriv.lean` | First partial derivative only. Repeated partials introduce factorials, which cannot be canceled in an arbitrary semiring/positive characteristic. |
| `Finsupp.lsum_apply`, `MvPolynomial.coeff_monomial`, `Finset.sum_eq_single` | Pinned linear-extension, coefficient and finite-sum API | Expand a sum and isolate a candidate summand; do not prove other summands vanish when truncated subtraction has collisions below `d`. |
| `Finsupp.comapDomain_apply`, `Finsupp.lcomapDomain` | `Data/Finsupp/Basic.lean:517`, `LinearAlgebra/Finsupp/Defs.lean:200` | Immediate coordinate rule for a different constructed pullback. No existing equality to current `hasseDeriv`; that equality has the same substantive proof burden. |
| `MvPolynomial.coeff_weightedHomogeneousComponent`, `coeff_rename_mapDomain` | Finder candidates, checked against pinned source | Projection and variable renaming preserve/restrict exponents differently; neither lowers multiindices with binomial weights. |

**Search conclusion:** partial analogues and generic building blocks found, but no verified existing arbitrary-variable coefficient theorem or ≤3-call derivation. A mathlib-only witness expands exactly the production linear-map construction and binomial product; `fail_if_success exact?` confirms that direct search does not close its coefficient identity, then a full independent proof closes it. This is bounded executable evidence for the tested route, not a universal impossibility assertion. The target is unavailable to the isolated environment; new local witness definitions are explicitly named as such. The first isolated attempt inferred the product codomain as `R` while `Nat.choose` returns naturals; explicit `((d.prod ... : ℕ) : R)` fixed the witness annotation, preserving the natural-binomial semantics. The failed attempt and its elaboration-recovery `sorryAx` are retained as failure history and never used as successful proof evidence: [initial source](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/mathlib-initial.lean), [initial receipt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/mathlib-initial-lsp.json). Only the final batch is successful, with zero errors/failed dependencies, no sorry, and standard axioms. Its one scratch line-length warning is retained; no linter suppression or limit raise was added.

## Phase 5.5 — Statement shape

**Normal forms:** possible presentations are (1) pointwise coefficient equality, (2) equality of coefficient functions by `funext`, (3) bundled coefficient-map composition equality, (4) symmetric equality, (5) shifted-polynomial Taylor coefficient characterization. The pinned univariate API uses the same pointwise shifted input-coefficient normal form. The proposed multivariate canonical form is the current equality, expanding output derivative on the left to one scalar product on the right. RHS convention: **respected**; no cycle of pairwise equivalences is introduced.

**Syntactic alternatives actually attempted:** the isolated witness has a bundled `lcoeff` composition equality; native target-shape probes test equivalent coefficient-function and bundled forms. [Executed target shape source](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/shape-executed.lean) and [complete success receipt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/shape-lsp.json) retain actual successful checks. An initial `ext P` bundled-map proof hit the default heartbeat limit; replacing it with explicit `LinearMap.ext` passed without raising any limit. [Failed source](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/shape-initial.lean), [raw failure](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/shape-initial-lsp.json). The two pre-existing scratch style warnings are retained, not suppressed. Explicitly passing the input polynomial and output exponent supports every current `rw`/`simp` caller directly; bundled maps require an extra application/congruence step there. The full finite product introduces an unnecessary `[Fintype σ]`, and reversing the equality worsens rewriting. **Chosen form: current pointwise equality.**

| Argument / instance | Essential? | Explanation |
|---|---|---|
| `σ` | Yes | Indexes the polynomial variables and multiindices; already universe-polymorphic. |
| `R` | Yes | Arbitrary coefficient carrier, not a fixed ring. |
| `CommSemiring R` | Yes | Pinned `MvPolynomial` and `R`-linear operator types require it; rejected drop is compile-checked. |
| `d` | Yes | Specifies the differential order and weights/shift. |
| `e` | Yes | Specifies which coefficient is read and which original coefficient contributes. |
| `P` | Yes | Specifies the arbitrary polynomial; moving it into an implicit binder or bundled map is equivalent syntax, not assumption weakening. |

**Statement-shape verdict: SHIP-AS-STATED.** Normal form OK; syntactic generality OK; no superfluous arguments. No `[simp]` attribute is asserted or changed by this assessment.

## Phase 6.0 — Complete qualified caller and inline audit

The [exact qualified/bare-token search](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/caller-search.json) was disambiguated using the [independently reviewed declaration inventory](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/reviewed-inventory-entry.json). It finds **8 direct caller declarations, 11 invocation occurrences**: seven callers in the same file, one outside. The target declaration and module-docstring reference are excluded. A bare substring hit in `abs_coeff_hasseDeriv_le` or its downstream callers is not a call of this theorem.

| Qualified caller | Declaration / use line | Occurrences | How used / inlining assessment |
|---|---|---:|---|
| `MvPolynomial.hasseDeriv_zero_apply` | `HasseDeriv.lean:112` / 114 | 1 | `ext` followed by coefficient simplification. Without interface needs the coefficient proof for every exponent, not just generic evaluation. |
| `MvPolynomial.hasseDeriv_map` | 134 / 137 | 1 | Coefficientwise naturality under coefficient maps; combines coefficient map API with identity. |
| `MvPolynomial.hasseDeriv_hasseDeriv` | 175 / 178 | 3 | Computes both derivatives and the right-hand side to reduce to binomial composition. |
| `MvPolynomial.pderiv_hasseDeriv` | 200 / 203 | 2 | Reconciles first-derivative coefficient formula with Hasse binomial factors. |
| `MvPolynomial.degreeOf_hasseDeriv_le` | 210 / 213 | 1 | Transfers nonzero output support to original exponent `e+d`. |
| `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | 219 / 222 | 1 | Shows all output coefficients vanish because shifted exponents exceed a degree bound. |
| `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | 266 / 270 | 1 | Matches arbitrary-variable interface to the existing univariate coefficient theorem under `Unique σ`. This compatibility proof depends on target; reversing it is circular and still restricts variables. |
| `Roth.abs_coeff_hasseDeriv_le` | `CoeffNorm.lean:134` / 137 | 1 | Reduces an integer derivative-coefficient bound to one original coefficient and a binomial bound. |

**Internal use count: 7 declarations / 10 occurrences; external: 1 declaration / 1 occurrence.** Complete explicit source references only: no exhaustive opaque kernel or tactic-generated dependency closure is claimed. Since the target is not `[simp]`, no hidden use through a registered target simp rule is asserted.

**Inline-derivation audit:** [broader search](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/inline-search.json) covers all production files using Hasse derivatives, binomial factors, coefficient/subtraction reconstruction and binomial vanishing. Other monomial-induction proofs (`hasseDeriv_rename`, monomial multiplication and composition-related helpers) prove different transformation laws; they do not duplicate this coefficient identity. No independent inlined duplicate was found in the reviewed source. Under the new generic-lowering witness, each caller would still need this named operator's monomial/zero-weight specialization unless a named coefficient lemma is retained; that is an argument for the computational interface, not a pre-existing three-call inlining plan.

## Phase 6 — Composition

Tested routes:

1. **Definitional unfolding / simp / exact search:** expanding `Finsupp.lsum` yields a coefficient sum, not the one shifted coefficient. Actual isolated direct search is guarded before the new proof. A subsequent complete batch adds `fail_if_success rfl` and `fail_if_success { simp [delta]; done }` before any local coefficient theorem, alongside `exact?`; `done` makes failure-of-closure, rather than mere simp progress, the tested condition. [Exact guarded source](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/route-executed.lean), [complete success receipt](../evidence/MvPolynomial.coeff_hasseDeriv/evidence/route-lsp.json). These are bounded primitive-route tests; the target cannot discharge itself.
2. **Univariate Hasse formula:** works only after a one-variable equivalence; the project's `uniqueAlgEquiv_hasseDeriv` is a downstream compatibility theorem using this target. Neither circular reuse nor assuming `Unique σ` replaces an arbitrary-variable identity.
3. **Iterated `pderiv`:** identifies factorial-scaled derivatives, but cannot cancel natural factorials in the current coefficient semiring. This would lose positive-characteristic content.
4. **Generic sum isolation:** `lsum_apply`, coefficient summation/monomial and `sum_eq_single` still require proving off-diagonal zero and the bound/subtraction cases. Packing that reasoning into one `simp`/`aesop` invocation is not a three-call mathematical composition.
5. **Pullback of weighted coefficients:** generic `comapDomain_apply` computes the alternate pullback. Its equality with the existing monomial extension is new mathematical work. No newly proved witness or equivalence is counted as a mathlib building block.
6. **Abstract weighted lowering `L`:** verified new helper abstracts exactly this proof. It is not in the pinned API and carries its own substantive proof; specializing a newly proved helper does not make the target composable from existing mathlib.

**Composition verdict: NOT-COMPOSABLE from the verified existing mathlib API in ≤3 calls.** The obstruction is the vanishing/collision argument intrinsic to truncated exponent subtraction. Actual successful independent proofs are retained as positive evidence of that mathematical content; bounded failed direct searches are not advertised as universal absence proofs.

## Phase 7 — Verdict and gate

**YES-add-as-is.** Concrete gap: the arbitrary-variable, commutative-semiring coefficient rule corresponding to `Polynomial.hasseDeriv_coeff`, adjacent to the missing multivariate Hasse operator in `Mathlib/Algebra/MvPolynomial`. It is the central coefficient theorem needed to compose Hasse differentiation with coefficient maps, support/degree reasoning, partial derivatives and integer coefficient estimates. The full caller table makes these consequences concrete. Literature, generality, modern idiom, statement shape and independent compiler evidence support keeping this exact interface; it is more than a wrapper around existing API.

The parent scalar alias's `NO-composable` verdict is not inherited: the binomial product spelling can be inlined while the substantive coefficient identity remains. Likewise the monomial/apply wrapper assessments do not predetermine this theorem. A future upstream version may inline `hasseCoeff` in its statement if that standalone alias is omitted, without changing this theorem's mathematics or coefficient normal form.

**Existing mathlib API this enables:** `MvPolynomial.ext` reduces polynomial equalities to coefficients, then this identity makes `MvPolynomial.coeff_map` and natural-cast compatibility usable in `hasseDeriv_map`. Combined with `MvPolynomial.mem_support_iff`, it transfers a nonzero derivative coefficient to the shifted input exponent, enabling `MvPolynomial.monomial_le_degreeOf` and degree bounds as the actual `degreeOf_hasseDeriv_le` caller demonstrates. Combined with `MvPolynomial.coeff_pderiv`, it aligns the existing first-partial-derivative API with Hasse multiorder shifts. These are actual pinned caller compositions, not hypothetical applications.

**Proposed mathlib location:** `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`, adjacent to `Mathlib/Algebra/MvPolynomial/PDeriv.lean`.

**Proposed PR title:** `feat(Algebra/MvPolynomial): add multivariate Hasse derivative coefficient formula`.

**PR grouping:** ship with the already-assessed `YES-add-as-is` definition `MvPolynomial.hasseDeriv` as one multivariate Hasse API PR. Include this substantive coefficient theorem; do not infer inclusion verdicts for later unassessed identities. The scalar `hasseCoeff` alias may be inlined according to its separate completed assessment.

**Pre-PR checklist before opening:**

- [ ] `/generalise MvPolynomial.coeff_hasseDeriv` — confirm no easy further weakening in the actual proposed upstream context.
- [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.coeff_hasseDeriv` — run the full audit and diff gates on the contribution.
- [ ] Pick a mathlib reviewer based on recent commits to `Mathlib/Algebra/MvPolynomial/`; perform that selection when preparing the upstream PR. No reviewer has been contacted by this assessment.

Suggested destination is the general algebra library, with the operator definition and its coefficient interface. No satellite/Archive destination is indicated: characteristic-free polynomial coefficient computation is general algebra and has existing univariate precedent. No production refactor, deletion, upstream submission or implementation swap is authorized by this assessment.

Gate checks: all nine literature channels accounted for; at least three distinct actual web queries; recent primary arXiv inspected; all five mathlib search methods on all forms and pullback route; all nine 4c questions and false-generalisation check; theorem-kind risk n/a; all five strategy questions; all three shape checks; full qualified caller/inline audit; isolated complete successful proof without target contamination; no new axioms, sorry, unsafe/native trust or limit raises; verified baseline hashes; portable links/hash manifest validated. No workflow execution gate remains unresolved. Optional unavailable ChatGPT, local-index unavailability and failed direct XHTML/nCatLab access are explicitly retained limitations, not mathematical negative evidence.

## Phase 8 — Next action

Prepare the multivariate Hasse operator and this coefficient identity for a focused upstream PR, then run the full cleanup/pre-submit workflow on the actual proposed contribution. Keep this theorem's coefficient normal form; consider a bundled `lcoeff` corollary or a generic weighted-lowering helper only when there is a concrete additional consumer. This assessment makes no tracked production edit and submits nothing upstream.
