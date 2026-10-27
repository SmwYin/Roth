# `Roth.exists_hasseDeriv_kronecker_eq_sum` — full mathlibable assessment

**BORDERLINE-needs-human.** The uniform higher chain rule is substantive, but the public Kronecker-specific finite-sum spelling should be reconsidered alongside a general substitution API. Native experiments verify arbitrary polynomial substitution over a rational algebra with a commutative semiring coefficient interface and merely finite variables. The literature also gives a characteristic-independent explicit Hasse chain rule. The decision is which upstream API should be primary: order-filtered span membership, finite coefficients, or explicit Taylor coefficients. This is an API-design question, not a claim that the verified weakening failed, a cost downgrade, or a pending verification task.

## Phase 0 — baseline

The declaration resolves at `Roth/GenWronskian.lean:214`, canonical index 116. The full module and its sole explicit caller, in the same module, were read. The existing successful **2467 jobs** baseline is reusable: all 17 source/pin hashes were freshly recomputed and match the shared input manifest. Production sources and pins remain unchanged. Native elaboration, original axiom checks, and the exact ordered 293-name audit pass with no errors, warnings, partial elaboration, missing constants, or nonstandard axioms. The audit finds precisely `Roth.exists_genWronskian_ne_zero` as a direct canonical consumer. This audit is not a claim about all implicit kernel/simp dependency closure.

Evidence: [fresh inputs](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/inputs.json), [baseline](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/baseline-build.txt), [native verification](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/verification.json), [original receipt](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-original-receipt.json), [canonical audit](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-audit-receipt.json).

## Phase 1 — content and full statement

Fix a finite variable set, a characteristic-zero field, a Kronecker substitution κ, and a derivative order μ. There is one finite collection of multi-indices d, all of total order at most μ, and polynomial coefficients c_d, such that the μ-th univariate Hasse derivative of κ(P) is the sum of c_d κ(Δ_d P), for **every** polynomial P. The coefficients and index set are chosen before P; this uniformity is essential for simultaneous row operations in the Wronskian argument.

The native full type, with the inferred witness types made explicit for readability, is:

```lean
@Roth.exists_hasseDeriv_kronecker_eq_sum :
  ∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] [CharZero K] (k μ : ℕ),
    ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K),
      (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K,
        Polynomial.hasseDeriv μ (Roth.kronecker k P) =
          ∑ d ∈ s, c d * Roth.kronecker k (MvPolynomial.hasseDeriv d P)
```

`K` supplies coefficients; the field and characteristic-zero assumptions allow division by successor integers in the underlying induction. `σ` is universe-polymorphic, and `Fintype σ` selects the enumeration used by the concrete parent `kronecker`. `k` is any natural base and μ any natural derivative order. There is no `1 < k`, degree/injectivity condition, nonzero-polynomial assumption, linear independence premise, or `l` parameter. The exact printer output is retained in [original type](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/original-type.txt).

Proof: private `hasseDeriv_kronecker_mem` proves the uniform operator belongs to a polynomial-module span. `Finsupp.mem_span_image_iff_linearCombination` then supplies finitely supported coefficients. Take their support and evaluate the resulting function equality at P. The private proof first shows differentiation raises the filtered span order by at most one using the algebraic chain rule and `pderiv_hasseDeriv`; induction converts the univariate Hasse derivative using `Polynomial.hasseDeriv_comp` and division by μ+1. The extraction is generic linear algebra; the membership is the substantive higher chain rule. Reading only the last four proof lines would obscure this distinction.

## Phase 2 — preliminary checks

**SMALL:** this is a helper in the proof of nonvanishing generalized Wronskians, not the module's main result or a new structure. The named Kronecker substitution alone does not make this a named main theorem. The one-line definition test is **n/a: theorem**; all three definition exemptions are likewise n/a. Its short extraction proof is assessed with its project premise, rather than counted as a self-contained mathlib composition.

## Phase 3 — exhaustive literature

Exact executed requests, returned-response SHA256/byte counts, and safe source locators are in [web receipts](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/web-receipts.json). Full article/search bodies are not archived. Returned signed/credential queries would be removed in full before archival; these requests required no such redaction. Search-engine crawl/publication summaries are not used as dates of the underlying papers.

| Channel | Actual request / locator | Result and concise relevance |
|---|---|---|
| Web, current | `Hasse derivatives multivariate polynomial substitution higher chain rule Faà di Bruno` | Found algebraic Hasse chain-rule and ordinary higher chain-rule sources. |
| Web, standard | `Hasse Schmidt derivation substitution polynomials finite sum order chain rule` | Found substitution-map theory and Hasse derivatives defined through Taylor coefficients. |
| Web, aliases/application | `Kronecker substitution generalized Wronskian differential operators bounded order` | Found generalized Wronskian sources; does not identify the Kronecker-specific spelling as the canonical API. |
| Optional mathematical second opinion | availability inventory for `ask_chatgpt_math` | n/a: unavailable. No invented external second opinion; all remaining channels executed. |
| Local source | `clean.tex` §2, especially lines 279–307 | The paper states the finite combination of operators of order ≤μ for the chosen curve, with rational coefficients. The local source uses ordinary iterated derivatives, converted to Hasse derivatives by factorials. [Exact local excerpt](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab Hasse Schmidt derivative chain rule substitution`; Hasse–Schmidt derivative page | Indexed page defines multivariate Hasse derivatives over a commutative rig. Direct open failed with unsupported XHTML content type; the indexed result was accessible. This is secondary contextual evidence, not the primary proof source. |
| nCatLab | `site:ncatlab.org/ncatlab Hasse Schmidt derivation substitution`; attempted nCatLab Hasse–Schmidt derivation URL | No independent categorical target retrieved; direct open inaccessible. Relevant categorical viewpoint is optional organization of the same finite algebraic expansion, not a verified replacement. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivations differential operators polynomial`; [tag 09CH](https://stacks.math.columbia.edu/tag/09CH) | §10.133 defines order-filtered differential operators and principal parts over ring maps. This supports a possible abstract API, but does not directly provide this coefficient expansion. |
| MathOverflow | `site:mathoverflow.net Hasse derivative chain rule multivariate substitution` | Found [Zeros of compositions of polynomials and derivatives](https://mathoverflow.net/questions/129554/zeros-of-compositions-of-polynomials-and-derivatives). It distinguishes derivatives along a curve from arbitrary ambient partial derivatives, motivating the false-generalization guard. Not used as primary theorem authority. |
| Recent arXiv, last five years | `site:arxiv.org Hasse Schmidt derivations substitution 2022 2023 2024 2025 2026`; [2305.04537](https://arxiv.org/abs/2305.04537) | Paul Barajas, submitted 2023-05-08, concerns high-order derivations of Hasse–Schmidt algebras. Related modern infrastructure; the abstract is not a direct proof of this theorem. |
| Supplementary primary source | Forbes–Shpilka, [arXiv:1303.0084v2 §5, Lemma 5.5](https://arxiv.org/html/1303.0084v2) | Explicit Hasse chain rule over any commutative ring, for arbitrary polynomial substitution. §5.1 fixes ring generality; Lemma 5.5 sums over weighted multi-indices. This is a 2013 source, not counted as recent arXiv. |

The standard concept is the algebraic higher chain rule / multivariate Faà di Bruno formula for Hasse derivatives. In the primary formula, tuples ℓ_j satisfy ∑j j|ℓ_j|=μ, and the outer derivative has multi-index ∑jℓ_j. Hence its total order is ≤μ. Grouping terms with the same outer multi-index gives uniform coefficients depending only on γ and μ. This explains the target's mathematical content and its natural arbitrary-γ formulation. The literature's characteristic-independent result is stronger than the native rational-algebra experiment; the former has **not** been claimed as a compiled Lean weakening. The local Wronskian paper's rational/ordinary-derivative formulation explains the current proof strategy, but does not force it as the optimal upstream scope.

## Phases 4a–4b — parameters and verified generality

| Parameter / premise | Current interface | Test and conclusion |
|---|---|---|
| Coefficients | `Field K` | Verified expanded representation over `CommSemiring R` plus `Algebra ℚ R`; this permits nonfields and zero divisors. No claim that deleting Field alone from the old `kronecker` parent compiles. |
| Characteristic | `CharZero K` | Replaced in the new representation by rational scalar structure. The successor-scalar cancellation is performed after restricting scalars to ℚ. This removes the explicit CharZero class, but is not a characteristic-free theorem. |
| Variables | `Fintype σ` | Arbitrary γ has no enumeration in its statement; `Finite σ` suffices. A local `Fintype.ofFinite σ` is used only to form the derivative sum in the helper proof. Original Kronecker needs its chosen Fintype enumeration. |
| Substitution | `x_j ↦ X^(k^(e j))` | Verified arbitrary `γ : σ → Polynomial R`. None of the exponent-specific properties, base bounds, or digit-injectivity facts occur in the transferred proof. |
| `k : ℕ` | natural base | Consumed only in constructing γ. It disappears in the generalized theorem; no assumption on k is necessary. |
| `μ : ℕ` | derivative order / total degree bound | Retained. The induction and derivative-order filtration use its natural-number structure. An arbitrary ordered index would change the concept. |
| Uniformity | ∃s c before ∀P | Retained and verified in generalized statement and actual caller. Swapping these quantifiers would weaken the result needed for Wronskians. |
| Finite coefficients | finset s plus total function c | Retained in experiment. Finsupp-supported coefficients and span membership are equivalent candidate public interfaces. |
| Universes / `l` | arbitrary universes; no `l` | No universe specialization introduced; `l` is correctly absent. |

**STRICTLY NARROWER THAN STANDARD**, supported by actual native proofs, not paper inference alone. The strongest verified restatement is:

```lean
theorem exists_hasseDeriv_aeval_eq_sum
    {R σ : Type*} [CommSemiring R] [Algebra ℚ R] [Finite σ]
    (γ : σ → Polynomial R) (μ : ℕ) :
    ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial R),
      (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ R,
        Polynomial.hasseDeriv μ (aeval γ P) =
          ∑ d ∈ s, c d * aeval γ (hasseDeriv d P)
```

Evidence: [strongest exact source](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-semiring-executed.lean.txt), [native receipt](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-semiring-receipt.json), [recovery and actual caller](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-semiring-consumer-clean-receipt.json). The initial field/arbitrary-γ and intermediate rational commutative-ring variants also compile cleanly and are retained as stages of the verified mathematical boundary. Initial drafts with unused-instance warnings and a consumer with a wrong named argument are separately rejected evidence. Their recovered `sorryAx` is not accepted proof evidence.

The transfer is mechanical across several private operators/helper proofs, with rational scalar cancellation and the independently verified semiring first-order chain rule. These new proofs are not pre-existing mathlib theorems. The old concrete parent remains fixed; the experiment re-aims its theorem at existing `MvPolynomial.aeval`. It does not pretend the old field interface was weakened by a single class edit. Characteristic-independent coefficients would instead require the full Taylor/Hasse chain-rule development from the primary source. That future API choice is kept separate from the completed assessment.

## Phase 4c — nine modern-idiom rows

| # | Question | Assessment and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles? | Already class-based. The verified rational scalar structure replaces invertibility assumptions with `Algebra ℚ R`; no new custom predicate is needed. |
| 2 | Filters/nets/topology? | No: finite algebraic equality; no topology or convergence. |
| 3 | Universal property? | Possible future principal-parts/Hasse–Schmidt interpretation, supported by Stacks. No native bridge supplied, and no assertion it immediately shortens this proof. |
| 4 | Bundled substructure? | Yes internally: `Submodule.span` already encodes order filtration. A public span-membership theorem composes with `span_mono`, scalar restriction, and derivative-stability. Native extraction proves how to recover finite coefficients. |
| 5 | Field→module/(semi)ring? | Yes, verified `CommSemiring R` with rational algebra. Serves polynomial rings and coefficient algebras with zero divisors; derivative-stability helpers require no rational structure. |
| 6 | Higher category? | No demonstrated benefit: finite polynomial identities do not require higher-categorical infrastructure. |
| 7 | Concrete index abstraction? | Natural derivative order and Finsupp natural exponents are mathematical, not incidental indices. σ is already arbitrary; replace its enumerator by `Finite σ` only after re-aiming substitution. |
| 8 | Concrete-via-abstract diagnostic? | Yes. In the four-line extraction proof, `kronecker` occurs only inside the private premise's name, with zero direct unfolded uses; `k` occurs only as its argument. Inspecting the premise chain shows the exponent-specific expression only as γ and γ′. The arbitrary-γ proof and original recovery compile. This enables arbitrary polynomial curves, including affine and nonlinear substitutions, through one higher chain-rule API. |
| 9 | False-generalization guard? | No semantic mismatch in verified proposals: exact original recovery and actual caller replay pass. Reject replacing Hasse by ordinary derivatives without factorials, requiring outer order exactly μ (nonlinear γ contributes lower orders), interchanging ∃c/∀P, or allowing unrelated operators merely sharing the word derivative. |

Modern idiom is available and mathematically useful. Its concrete verified benefits are reuse for arbitrary polynomial curves, rational coefficient algebras, enumeration-free theorem statements, and a choice between span and finitely supported coefficient API. The full characteristic-free literature form remains a future development target, not accepted native evidence.

## Phase 4.5 — infrastructure risk

**n/a: theorem**, with each requested category accounted for: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance-priority collisions, universe constraints introduced by a definition, and coercion ambiguity are all n/a because this declaration adds only a proof constant. It introduces no instance, coercion, structure, or new computation rule. Existing parent-interface constraints were analyzed above; the probe's private operator definitions are experimental evidence, not production additions.

## Phase 4.6 — proof strategy

| # | Strategy question | Answer |
|---|---|---|
| 1 | Topology via filters? | n/a: no topology. |
| 2 | Algebra via submodule inclusions? | Already largely idiomatic: filtration and span induction organize derivative stability. Prefer exposing arbitrary-γ membership as the structural theorem; finite coefficients follow by generic extraction. |
| 3 | Sequences vs nets? | n/a: finite sums and natural induction, not limits. |
| 4 | Universal-property construction? | Principal parts offers a broader route, but no verified simplification in this pin; do not substitute a slogan for a proof. |
| 5 | Missing helpers mathlib should have? | The higher substitution law relative to multivariate Hasse derivatives, and either its Taylor-coefficient formula or filtered-span corollary. Accepted earlier first-order semiring chain-rule evidence supplies one genuine prerequisite; it does not itself prove higher-order membership. |

**REFACTOR-RECOMMENDED:** separate generic span extraction from the higher chain rule, re-aim at arbitrary `aeval`, and choose the characteristic scope and coefficient representation before shipping. The existing span argument is coherent for rational algebras; the characteristic-independent literature uses Taylor coefficients instead of division. No cost-based conclusion is drawn.

## Phase 5 — actual five-method search on all three forms

[Raw formal-search receipts](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/formal-search-raw.json) retain every request and complete response, including the malformed Loogle query, rate-limited retry, and successful valid retry. [Source receipts](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/source-search-raw.json) retain exact commands, statuses, and untruncated stdout/stderr. External indices use their own snapshots (Finder defaults to v4.28.0), whereas all claimed candidate signatures and experiments are checked against the repository pin.

| Method | Current Kronecker form | Standard higher Hasse chain rule | Abstract filtered-operator form |
|---|---|---|---|
| Finder | Uniform finite expansion query; univariate Hasse API | Faà di Bruno / bounded total order; Hasse operator composition | Pullback/filter query; derivation and Kähler API |
| Loogle | `Polynomial.hasseDeriv, MvPolynomial.aeval`: empty | Initial placeholder invalid; rate retry rejected; valid `Polynomial.hasseDeriv, Polynomial.comp`: empty | `Submodule.span, Finsupp.linearCombination`: finds extraction infrastructure |
| LeanSearch | Uniform Kronecker expansion; Hasse, Taylor near matches | Higher substitution / Faà di Bruno; partial matches | Differential-operator pullback; derivation/Kähler near matches |
| Source `rg` | Kronecker and Hasse/aeval variants; no target | `hasseDeriv_comp`, `FaaDiBruno`, `taylor_coeff` | Hasse–Schmidt/differential-operator names and span/extraction theorem names |
| Local name search | `hasseDeriv_kronecker`: project/scratch hits only | `hasseDeriv_comp`: univariate operator rule | `mem_span_image_iff_linearCombination`: mathlib extraction theorem |

Local symbol indices report `unavailable`; source-backed hits remain useful, but empty local results do not prove absence. Full-name source search for the current and generalized target names has no mathlib hit. The accepted isolated probe confirms the project target is absent from those imports with `#check_failure`.

Pinned candidates:

* `Polynomial.hasseDeriv_comp`, `Mathlib/Algebra/Polynomial/HasseDeriv.lean:154`, composes two **operators** on one polynomial; it does not differentiate a substituted polynomial. Native signature verifies this distinction.
* `Polynomial.factorial_smul_hasseDeriv`, same file:133, converts ordinary iterates to Hasse derivatives after multiplying by factorial. It does not supply the evaluated multivariate expansion or uniform coefficients.
* `Polynomial.taylor_coeff`, `Mathlib/Algebra/Polynomial/Taylor.lean:68`, describes one-variable translated coefficients. It suggests a characteristic-independent proof route, but does not provide the multivariate substitution/bounded-degree grouping theorem. The exact pinned source is archived; no missing candidate result is invented.
* `Finsupp.mem_span_image_iff_linearCombination`, `Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean`, and `Finsupp.linearCombination_apply` express span membership by supported coefficients. Native signatures and actual generic extraction compile.
* `Submodule.mem_span_image_iff_exists_fun`, same file:395, extracts a finite support with subtype-indexed coefficients; `Submodule.mem_span_image_finset_iff_exists_fun'`, same file:410, extracts a total coefficient function on a fixed finite image. Both signatures were checked in the pin in a late native candidate probe. These closer interfaces still require the uniform operator-membership premise; neither supplies the higher chain rule.
* Analytic `ContDiff.FaaDiBruno` requires analytic/normed-space infrastructure and is not a substitute over arbitrary algebraic fields or semirings. First-order derivation/Kähler API only reaches the μ=1 layer without further induction and coefficient work.

Conclusion: **partial matches and genuine extraction infrastructure; no verified existing theorem or ≤3-call replacement for the full uniform higher substitution law**. This is a scoped search/composition conclusion, not a proof of global absence. No repeated expensive local Hasse-delta `exact?` experiment is presented as evidence; the generic extraction, candidate signatures, full source search, and actual new helper proofs establish the precise boundary checked here.

## Phase 5.5 — statement shape

**Normal form.** Three equivalent interfaces are span membership of the uniform function, supported Finsupp coefficients with a function equality, and finite s plus coefficients with pointwise equality. Existing mathlib normalizes the first two through `Finsupp.mem_span_image_iff_linearCombination`. The third is useful to `choose` witnesses for determinant rows, but is not established as the unique canonical higher-chain-rule surface. The operator equality has the higher derivative on the left and the expansion on the right, so RHS normalization is appropriate.

**Syntactic generality experiment.** The mathlib-only [extraction probe](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-extraction-executed.lean.txt) works for arbitrary functions `v : α → β → A`, a set s, and an arbitrary span member F over any commutative semiring. It produces finite coefficient witnesses and evaluates `congrFun hsum.symm b` exactly as the target. It compiles without Roth imports and preserves the essential precondition `F ∈ span A (v '' s)`. Thus the pointwise finite form is recoverable, but extracting it does not manufacture the missing membership premise.

**Superfluous arguments.** No unused `l`, base inequality, domain assumption, or coefficient-polynomial premise occurs. Fintype is necessary for the fixed Kronecker interface but not the arbitrary-γ interface. Field+CharZero are replaced by rational algebra in the accepted experiment; none of those changes imply a char-free Lean proof. **RESTATE-BEFORE-SHIP** for general substitution, scalar assumptions, and public representation.

## Phase 6.0 — callers and inline audit

| Explicit caller | Role | Internal count / external count | Refactor experiment |
|---|---|---|---|
| `Roth.exists_genWronskian_ne_zero`, `Roth/GenWronskian.lean:260` | Chooses uniform s,c for μ in `Fin l`; these feed determinant row expansion and the order bounds | 1 same-file call; 0 other source-module calls | Replaced the target call by the verified arbitrary-γ rational-semiring theorem specialized at the Kronecker monomials. Replayed the full caller, using the actual existing private determinant helper through a term elaborator. PASS, clean axioms. |

The explicit source search and exact293 canonical direct-consumer audit agree. Inline-derivation search finds the private membership/derivative-span chain and the determinant helper's hypothesis, not another independently repeated finite-extraction proof. Source-level counts do not imply dead code, a full simp closure, or a whole-project dependency graph. This theorem is live and not tagged simp. [Strongest full caller execution](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/exists-hasse-kronecker-semiring-consumer-clean-executed.lean.txt) preserves the caller's mathematical conclusion; its private-term elaborator only accesses the real constant and adds no axiom.

## Phase 6 — composition experiments

1. **Actual generic extraction:** accepted mathlib-only `ExistsHasseExtraction.extract` proves the same final span-to-finite conversion over `CommSemiring A`. It needs a span-membership hypothesis. The finishing `simpa` unfolds linear combination/Finsupp sum and evaluates a function equality. Even ignoring the missing premise, this is a normalization proof rather than a bare ≤3-call term; Phase 6b does not automatically route it to NO.
2. **Whole higher law:** the current private membership theorem is a project result. `Finsupp.mem_span_image_iff_linearCombination` cannot prove it. Transferring its derivative-span induction to arbitrary γ, rational scalars, and Finite variables gives new proofs, checked natively; those helpers are not existing mathlib replacement calls.
3. **Original recovery and actual consumer:** the generalized theorem specializes definitionally through `aeval` to the original `kronecker` substitution, and the sole caller compiles unchanged apart from the target invocation. This verifies semantic preservation and usefulness of the proposed abstraction, not presence in the pin.

Overall **NOT-COMPOSABLE** from identified existing mathlib building blocks in ≤3 calls. No NO verdict is justified merely by counting the extraction proof while hiding its project premise. The parent `kronecker` was independently assessed NO because it is `aeval`; the re-aim rule was applied here by searching the analogous law about `aeval`. No analogous full higher law was found or verified. No blanket parent verdict was inherited.

## Phase 7 — verdict and actionable choices

**BORDERLINE-needs-human.** The finite uniform expansion is standard mathematical content and the verified arbitrary-γ rational-algebra generalization is useful. The exact Kronecker spelling is an application-specific endpoint. Primary literature gives a stronger characteristic-independent chain rule with explicit coefficients. The choice of characteristic scope and public representation determines the right upstream theorem; proof length or implementation cost does not determine this verdict. All assessment checks and claimed proof experiments are complete; `unresolved=[]` records that fact, while the following questions concern future upstream design.

1. Should the primary API be arbitrary-γ order-filtered span membership, with the finite-coefficient conclusion obtained using existing Finsupp span API?
2. Should the primary API instead state the characteristic-independent explicit Hasse–Taylor chain rule over commutative rings, with rational-algebra span and finite-sum corollaries derived from it?
3. If a rational-algebra result is introduced independently, should the finite-coefficient corollary be public or remain a Wronskian application helper?

Provisional future home: `Mathlib/Algebra/MvPolynomial/ChainRule.lean`, importing the accepted proposed `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` API and univariate Hasse derivatives. The original Kronecker-specific corollary can remain project-local in `Roth/GenWronskian.lean`; no new Kronecker wrapper is required upstream. A characteristic-free Taylor implementation may warrant a dedicated Hasse/Taylor file once import layering is decided. No production edit, deletion, or unverified refactor is authorized by this read-only assessment.

Already accepted related YES declarations, read directly from current progress, include `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.pderiv_hasseDeriv`, and `Roth.derivative_aeval`. These are possible grouping prerequisites, not inherited verdicts for this theorem. If upstream design selects an affirmative follow-up, run `/generalise Roth.exists_hasseDeriv_kronecker_eq_sum` for the chosen target, then `/cleanup Roth/GenWronskian.lean Roth.exists_hasseDeriv_kronecker_eq_sum`, and review import layering and the actual caller. Recent pinned-file commits identify Moritz Firsching (Hasse API) and Yaël Dillies (MvPolynomial API) as relevant reviewer candidates; no review request was sent. Suggested eventual PR topic: `feat(Algebra/MvPolynomial): higher chain rule for polynomial substitution`.

## Phase 8 — completion record

The consolidated report includes the baseline, full content, theorem-appropriate preliminaries, every literature channel, parameter checks, all nine idiom rows, six infrastructure categories, all five strategy rows, actual five-method × three-form searches, all three shape checks, sole explicit caller and inline audit, composition experiments, and a scoped actionable verdict. Accepted native evidence and rejected attempts are separated in [verification](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/verification.json). [Portable validator](../evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/validate.py) checks current manifests, source/pin freshness, exact canonical order, native success and standard axioms, full phase completion, all links and evidence checksums in either scratch or integrated layout. Root independent acceptance remains pending.
