# /mathlibable — `MvPolynomial.hasseCoeff_eq_zero_iff`

This is a full assessment of the theorem written at `Roth/HasseDeriv.lean:80`, rather than an inherited verdict from `hasseCoeff`. Production Lean and pinned versions remain unchanged. Canonical destinations are `.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md` and `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_eq_zero_iff/`.

## Phase 0 — Doctor

The successful baseline is `lake build`, exit 0, 2467 jobs at input commit `99f19fda4b3cbee38fc0d31af76075834f5cc265`. Reuse is justified by a fresh comparison of all **17** production-source/pin hashes with the shared manifest: all match. Branch is `ramin-cleanup`. [Baseline receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/baseline-build.txt), [fresh integrity check](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/source-integrity.json), [pin identities](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/pins.json).

Module summary: multivariate Hasse derivatives and coefficient/composition/Taylor interfaces. The assessed declaration contains no `sorry`.

Compiler resolution, axioms, independent proof and isolated generic routes are recorded in the native receipts linked below. The independent proof must not invoke the theorem under assessment or close by its simp registration; the target is not a simp lemma.

## Phase 1 — Comprehend

Written signature:

```lean
theorem MvPolynomial.hasseCoeff_eq_zero_iff {σ : Type*} (d k : σ →₀ ℕ) :
    MvPolynomial.hasseCoeff d k = 0 ↔ ¬d ≤ k
```

The natural number product `∏ j ∈ d.support, (k j).choose (d j)` is zero precisely when the differentiation order exceeds the monomial exponent in at least one coordinate. No field, coefficient semiring, finite variable universe, or decidable equality hypothesis is part of this theorem. The support is finite even for an infinite variable type. If a coordinate fails the inequality, `d j > k j ≥ 0`, hence that coordinate belongs to `d.support`.

Project dependency: `MvPolynomial.hasseCoeff` in the statement and unfolding proof. The proof invokes generic finite-product vanishing, the scalar natural binomial criterion, support-restricted order, and classical propositional normalization. The theorem is a natural-number fact **before** coefficient-ring casting; after casting to a positive-characteristic coefficient ring, the forward implication “cast coefficient = 0 → failed coordinate bound” can fail (for example, `2.choose 1` modulo2). The implication “failed coordinate bound → cast coefficient = 0” remains valid.

[Canonical reviewed declaration and dependency inventory](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/inventory-target.json).

## Phase 2 — Preliminary classification

**SMALL**: a computational vanishing interface for multivariate binomial coefficients; no new structure and not a module main theorem. The Hasse name labels the coefficient family, rather than a theorem traditionally named after Hasse. **One-line-definition check: n/a**, because the declaration is a theorem; definition exemptions do not apply. The proof is one `simp` invocation spanning two lines, not narrow `rfl`/`unfold` glue. Therefore the full workflow is required despite the parent definition's NO verdict.

## Phase 3 — Exhaustive literature search

Exact web requests, response digests/status, relevant source URLs/locators and original summaries are preserved (copied webpage/search-response text is omitted): [specific/general/alias queries](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/web0.json), [nLab/nCatLab/Stacks/MO/arXiv queries](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/web1.json), [dedicated Stacks query](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/web2.json), [primary-source opens](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/web3.json), [recent multipoint paper query](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/web4.json), [arXiv inspection record](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/web5.json). Nine distinct actual web searches ran; the first three differ in generality and aliases.

| Channel | Query / inspected source | Result and relevance |
|---|---|---|
| Web specific | `multivariate Hasse derivative binomial coefficient multi index zero if exponent smaller` | Several-variable binomial monomial rule found. |
| Web general | `product binomial coefficients nonzero iff componentwise partial order` | Standard coordinatewise multi-index order; scalar binomial interval. |
| Web aliases | `Hasse Schmidt higher derivation divided derivatives multi index binomial` | Hasse-Schmidt / higher derivation / divided derivative operator context. |
| ChatGPT MCP | n/a: `ask_chatgpt_math` unavailable | Optional channel; no opinion invented. |
| Local references | `rg -n 'Delta|binom|otherwise|deriv' .mathlib-quality/references/clean.tex` | §Derivatives lines119–155 has binomial product on coordinatewise interval and zero otherwise. |
| nLab | `site:ncatlab.org Hasse Schmidt derivative binomial multi index` | [Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative) has several-variable extraction/divisibility formula. Direct XHTML fetch unsupported; actual indexed page context retained. |
| nCatLab | Same nCatLab-hosted source and its graded-bimonoid observation | Checked; no categorical improvement to finite arithmetic iff supplied. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt divided powers differential operators`; dedicated `site:stacks.math.columbia.edu "divided power" "polynomial"` | [07H4](https://stacks.math.columbia.edu/tag/07H4) gives binomial structure constants, arbitrary-variable construction and universal property for a different algebra. Not an exact replacement. |
| MathOverflow | `site:mathoverflow.net Hasse derivative binomial positive characteristic` | [Replacement for derivations in characteristic p?](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) identifies hyperdifferentiation alias and literature. Discovery only, not sole support for a technical claim. |
| Recent arXiv | `site:arxiv.org Hasse derivatives multivariate binomial 2021 2022 2023 2024 2025 2026` | [Barajas 2023](https://arxiv.org/html/2305.04537v1), Definitions1.1–1.2, treats universal families and ring algebras. [Multipoint evaluation 2022](https://arxiv.org/abs/2205.00342) applies multivariate Hasse derivatives. Both fall in the last five years; neither supplies a wider scalar natural vanishing criterion. |

The standard form is the multi-index binomial coefficient vanishing criterion, equivalently nonzero/positive iff the lower multi-index lies below the upper one. Finite tuples in the references extend to arbitrary variable types using finite support, already present here. Source formulas agree on the componentwise convention; operator universal properties are related infrastructure, not competing formulations of this scalar iff. [Concise original analysis for every channel](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/literature-analysis.json), [local query receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/local-ref-query.json), [local source excerpt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/local-reference.txt). One exploratory wrong arXiv identifier returned unrelated *Wiggle Island*; it is explicitly excluded, rather than treated as evidence.

## Phase 4a–4b — Generality

| Dimension | Current form | Weakening / comparison | Status |
|---|---|---|---|
| Variable type | arbitrary `σ : Type*` | No `Fintype`, `Finite`, `Nonempty`, `DecidableEq` needed | Already general. |
| Multi-indices | `σ →₀ ℕ` | Natural binomial order criterion requires natural entries | Correct domain. |
| Coefficient structure | none | Surrounding `R` and `[CommSemiring R]` are omitted by elaboration | No hypothesis to weaken. |
| Lower support | `d : σ →₀ ℕ` | Dropping lower finite support would require a product convention or finiteness hypothesis | Needed for the current finite product. |
| Upper exponent | `k : σ →₀ ℕ` | May broaden to `k : σ → ℕ` while product remains over `d.support`; bound becomes `∀j, d j ≤ k j` | Valid optional expanded-statement extension; current `hasseCoeff` signature fixes upper `Finsupp`. |
| Output | ℕ | Cast into arbitrary semiring can create extra zeros | Reject false widening; e.g. `2.choose 1 = 2` becomes zero mod2 although1≤2. |
| Abstract product | no-zero-divisor finite support product | `Finsupp.prod_eq_zero_iff` already abstracts arbitrary factor functions/codomains | Existing generic route, not a new missing generalization. |
| Equivalent predicates | zero iff not≤ | nonzero iff≤ and positivity iff≤ | Probe equivalent forms, not stricter mathematical generality. |

**Generality verdict: STRICTLY NARROWER than the verified arbitrary-upper-function form; hypothesis-minimal for the fixed parent API.** The lower index supplies the finite product support, so the upper exponent can be any `σ → ℕ`; unlike lower-support removal this requires no new product convention. The expanded form uses `∀j, d j ≤ k j` on the RHS. This is mathematically broader but changing the parent coefficient definition would change its foundational API; it is not an unneeded typeclass argument of the existing theorem. The parent definition assessment had already identified this optional extension. Its [actual verification receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/upper-lsp.json) and [exact executed code](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/probes/upper-executed.lean) are recorded below. This is one real mathematical widening, not a dropped instance: the expanded statement is

```lean
(d : σ →₀ ℕ) (k : σ → ℕ) :
  d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬ ∀ j, d j ≤ k j
```

Its proof uses the generic zero-factor criterion and the fact that an out-of-bound coordinate has nonzero lower exponent, hence belongs to `d.support`. Specializing `k` by function coercion gives the original bound definitionally. Rephrasing the theorem alone against the existing `hasseCoeff` cannot realize this widening without modifying or bypassing the foundational parent definition. The command's real-but-not-single-mechanical-edit routing therefore supports BORDERLINE rather than silently claiming no widening or issuing an unverified generalise-first instruction. Existing abstract zero-product API is broader again but still needs scalar-binomial/order normalization.

## Phase 4c — Modern mathlib idiom (all nine questions)

| # | Question | Answer / proposed form | Downstream consequence |
|---|---|---|---|
| 1 | Preambles → typeclasses? | No new hypotheses or classes needed. | Current `Finsupp` uses existing instances. |
| 2 | Sequences/metrics → filters? | No: finite combinatorial arithmetic. | n/a |
| 3 | Construction → universal property? | No object is constructed; Stacks' universal divided-power algebra is different. | No gain for this iff. |
| 4 | Sets with closure → bundled substructures? | No: indices already use bundled `Finsupp`. | Existing support/order API applies. |
| 5 | Field/vector-specific → weaker hierarchy? | No scalar structure in elaborated theorem. Upper-function support weakening is separate, verified below. | Already independent of coefficient rings. |
| 6 | 1-category → higher category? | No category in statement or proof. | No concrete downstream gain identified. |
| 7 | Concrete ℕ → arbitrary ordered monoid? | Not as same binomial object: arbitrary ordered monoids do not carry `Nat.choose`. | Abstract factor-product theorem is already available. |
| 8 | Concrete-via-abstract diagnostic? | **Yes**: `hasseCoeff` appears once in unfolding list, then zero times. Abstract form `f.prod g = 0 ↔ ∃ i ∈ f.support, g i (f i)=0` exists as `Finsupp.prod_eq_zero_iff`. | Reuse arbitrary no-zero-divisor codomain product API; remaining content is natural choose/order conversion. |
| 9 | False-generalisation guard? | Abstract product specialization preserves product content, but does not alone identify coordinatewise bounds. Arbitrary-semiring cast iff is rejected. | No false cast claim is shipped. |

Modern abstract organization is **already available in mathlib**, not a missing novel helper: `Finsupp.prod_eq_zero_iff` (and `prod_ne_zero_iff`). This improves the proof's entry point and avoids manually unfolding the generic product implementation. It does not automatically settle whether the residual named binomial/order iff merits API. Cost is CHEAP and is not used as a verdict factor.

## Phase 4.5 — Infrastructure risk

**Explicit n/a:** this is a theorem, not a `def`, `class` or `instance`. It installs no structure, instance, coercion, or alternative scalar path. The optional generic scratch witnesses are local evidence, not project or proposed infrastructure.

## Phase 4.6 — Proof strategy (all five questions)

| # | Check | Applies / result |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Element reasoning versus ideals/submodules | No substructure inclusion; finite support/order coordinates are the mathematical statement. |
| 3 | Sequences versus nets | No analysis. |
| 4 | Construction versus universal property | No construction. |
| 5 | Missing helper API | No: generic finite-support product vanishing/nonvanishing and natural binomial vanishing already exist. |

**MATHLIB-IDIOMATIC** mathematical strategy: reduce product vanishing to a zero scalar factor, then to a coordinate inequality. Prefer `Finsupp.prod_eq_zero_iff` to unfolding `Finsupp.prod` and falling back to `Finset.prod_eq_zero_iff`. This is a presentation improvement using existing API, not a new mathematical proof strategy or missing-helper ticket.

## Phase 5 — Actual five-method search, three forms

Forms searched: current named coefficient theorem; standard natural multi-binomial vanishing/nonvanishing; modern abstract finite-support product criterion. [All12 actual external/local API requests with raw complete API responses](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/search-api.json).

| Method | Current / standard / abstract actual queries | Findings |
|---|---|---|
| A Lean-Finder | `Multivariate Hasse derivative binomial coefficient product equals zero if and only if multi-index not less than exponent`; `Product of natural number binomial coefficients vanishes exactly when some lower index exceeds upper index`; `Finsupp product equals zero iff exists index in support with factor zero in monoid without zero divisors` | Univariate Hasse API; `Nat.choose_eq_zero_iff`, `choose_ne_zero_iff`; `Finsupp.prod_eq_zero_iff`, `prod_ne_zero_iff`, DFinsupp versions. |
| B Loogle | `"hasseCoeff"`; `Nat.choose _ _ = 0 ↔ _`; `Finsupp.prod _ _ = 0 ↔ _` | Named query empty; scalar and generic product criteria found. |
| C LeanSearch | `Hasse coefficient d k equals zero iff not d ≤ k`; `product of choose coefficients nonzero iff all lower indices at most upper indices`; `Finsupp prod equals zero iff exists index in support with factor zero` | Same exact scalar/generic candidates; Laurent/univariate derivatives do not prove arbitrary-index scalar iff. |
| D Source rg | full qualified target, `hasseCoeff`, `choose_eq_zero_iff`, `prod_eq_zero_iff`, nonzero/order variants and combinatorial product-choose variants | Full untruncated receipts linked below; candidate source examined at actual pin. |
| E Local name search | `hasseCoeff_eq_zero_iff`; `choose_eq_zero_iff`; `prod_eq_zero_iff` | Project target and positive pinned candidates returned via textual fallback; index **unavailable**, so no absence inference from it. |

External version indexes discover names only. The package pin, source hashes, source excerpts and compiler checks control applicability. [Full-name rg](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/full-qualified.json), [current-form rg](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/user-form.json), [standard-form rg](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/standard-form.json), [abstract rg](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/abstract-form.json), [variants](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/variants.json), [additional product/choose variants](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/additional-variants.json).

| Candidate at actual pin | Exact source | Relevance |
|---|---|---|
| `Finsupp.prod_eq_zero_iff` | `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:223` | Generic product zero iff supported zero factor. |
| `Finsupp.prod_ne_zero_iff` | same:224 | Universal supported nonzero criterion. |
| `Nat.choose_eq_zero_iff` | `Mathlib/Data/Nat/Choose/Basic.lean:122` | Scalar natural-binomial vanishing. |
| `Nat.choose_ne_zero_iff` | same:125 | Scalar nonzero iff lower≤upper. |
| `Finsupp.le_iff` | `Mathlib/Data/Finsupp/Order.lean:242` | Supported coordinate comparison equals global order. |
| `Polynomial.hasseDeriv_monomial` | `Mathlib/Algebra/Polynomial/HasseDeriv.lean` | One-variable operator formula; different output/type. Not direct substitute. |

[Pinned candidate hashes and excerpt boundaries](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/candidate-source-hashes.json), [generic source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/finsupp-product-source.lean), [scalar source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/choose-source.lean), [order source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/order-source.lean), [univariate source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/polynomial-hasse-source.lean).

Additional [whole-mathlib broad multi/binomial naming search](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/broad-naming-search.json) was saved in full (243lines). It also finds `Finsupp.multinomial` and `multinomial_update`; [pinned source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/multinomial-source.lean) shows a one-index total-degree factorial ratio, rather than the two-index product of independent coordinate binomials here. Thus this is a distinct combinatorial coefficient, not an exact replacement. `Nat.multichoose` similarly counts multicombinations in one coordinate and must not be confused with multivariate binomial products.

The searches positively establish generic building blocks; they do not establish universal absence of an exact theorem, particularly with unavailable local symbol index. The isolated elaborator probes test generic applicability without importing Roth or making the assessed theorem visible.

## Phase 5.5 — Statement shape

**Normal form:** RHS `¬ d ≤ k` uses the canonical `Finsupp` pointwise order and avoids keeping an existential witness plus support guard. This is useful precisely where callers already possess a failed coordinate bound. `hasseCoeff ≠ 0 ↔ d≤k` and `0<hasseCoeff ↔ d≤k` are equivalent natural-number forms, not new mathematical generalizations. Their probe proofs reuse the independent expanded witness, never the assessed theorem.

**Syntactic-generality attempt:** compare zero, nonzero and positivity forms, and the fully generic supported-factor form. For the three callers, zero iff supplies `.2` directly; switching to positive iff would require extra negation/order transformations. Keep the stated zero orientation if retaining the named interface.

**Superfluous arguments:** `d` chooses the factors/support, `k` chooses the upper binomial entries, `σ` is arbitrary and universe-polymorphic. No coefficient type/class or finite/decidable index assumptions survive elaboration. No unused hypothesis exists to drop. **SHIP-AS-STATED** as a local API statement; statement shape does not decide mathlib inclusion.

## Phase 6.0 — Every direct project caller

| Qualified caller | Declaration / actual use | Pattern |
|---|---|---|
| `MvPolynomial.coeff_hasseDeriv` | `Roth/HasseDeriv.lean:89`, use99 | `.2 hdk` where `hdk : ¬d≤k`, then simp kills monomial coefficient. |
| `MvPolynomial.hasseDeriv_C` | `Roth/HasseDeriv.lean:126`, use127 | `.2` at `(d,0)` after deriving `¬d≤0` from `d≠0`. |
| `MvPolynomial.coeff_taylor_monomial_single_add_aux` (private) | `Roth/Taylor.lean:101`, use113 | `.2` after a failed `i` coordinate produces `¬e≤k`; simp contradicts support membership. |

**K=3** direct callers, **3** explicit occurrences, **2** internal/file-local uses and **1** cross-file use. No caller uses both directions: all exploit vanishing from failed coordinate order. [Exact caller sources/counts](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/call-sites.json), [whole-project occurrence grep](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/all-callers.json), [inline-derivation grep](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/inline-derivations.json). The other product-zero mentions concern Wronskians or norm/index products, not duplicate Hasse-coefficient iff derivations. Counts cover explicit source references and do not claim opaque tactic/kernel dependency closure.

## Phase 6 — Composition and actual compiler verification

All heavy compiler work was serialized by the root session. The following are complete successful native receipts, not planned experiments:

| Batch | Exact executed source / raw receipt | Accepted evidence |
|---|---|---|
| Target disk document | [source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/probes/target-executed.lean), [receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/target-lsp.json) | `#check @target` resolves with arbitrary `σ` only; standard three axioms; independent original expanded proof compiles without invoking target. `partial=false`, `success=true`, no failed dependencies/errors. Two warnings belong to earlier scratch controls. |
| Isolated search **first** | [source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/probes/search-executed.lean), [receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/search-lsp.json) | No Roth import, no preceding new local proof witnesses. `#check_failure` confirms project target/definition unavailable in this import context. `exact?` proves the generic supported-zero-factor goal using `Finsupp.prod_eq_zero_iff`. Expanded original iff passes `first | exact? | simp [...]`; no exact-term suggestion for that first goal. |
| Optional upper-function extension | [source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/probes/upper-executed.lean), [receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/upper-lsp.json) | `upper_function (d : σ →₀ ℕ) (k : σ → ℕ)` proves vanishing iff `¬∀j,d j≤k j`, with no new product convention. Direct specialization back to a `Finsupp` upper index compiles. Success true, timeout false, zero errors/warnings, standard three axioms. |
| Isolated all positive routes | [source](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/probes/mathlib-executed.lean), [receipt](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/mathlib-lsp.json) | Expanded original, generic zero-product, nonzero, positivity, fully abstract supported-factor, short simp, and negated-nonzero routes all pass. No errors/warnings, timeout false. Every named new witness has only `propext`, `Classical.choice`, `Quot.sound`. |

The isolated batches retain only `Mathlib.Algebra.MvPolynomial.PDeriv` and `Mathlib.Algebra.Polynomial.HasseDeriv` as imports. Successful local probe witnesses are **new local proof evidence**, not pre-existing mathlib declarations. The `#check_failure` controls establish import isolation, not universal mathematical absence. `first` does not provide a formal trace for its failed alternatives, so we do not claim that the first search goal exhausts all possible exact terms.

Composition attempts:

1. Direct abstract theorem: `exact Finsupp.prod_eq_zero_iff` works for `f.prod g=0 ↔ ∃ i∈f.support, g i(f i)=0`. It does **not itself state** the original coordinate-order criterion; scalar vanishing and order/negation conversion remain.
2. Explicit generic rewrite route, accepted:

```lean
example (d k : σ →₀ ℕ) : d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simp [Finsupp.prod_eq_zero_iff, Nat.choose_eq_zero_iff, Finsupp.le_iff, not_forall]
```

3. Short simp route, accepted (generic product theorem is already in the simp set):

```lean
example (d k : σ →₀ ℕ) : d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simp [Nat.choose_eq_zero_iff, Finsupp.le_iff, not_forall]
```

4. Negated nonzero route, independently accepted:

```lean
example (d k : σ →₀ ℕ) : d.prod (fun j ↦ (k j).choose) = 0 ↔ ¬d ≤ k := by
  simpa only [Nat.choose_ne_zero_iff, ← Finsupp.le_iff, not_not] using
    not_congr (Finsupp.prod_ne_zero_iff (f := d) (g := fun j ↦ (k j).choose))
```

5. Finset route: unfold product, apply `Finset.prod_eq_zero_iff`, scalar criterion, support-restricted `Finsupp.le_iff`, negation. The expanded witness compiles but has more named ingredients; it is not a shorter direct composition. Fully generic routes also cover the no-zero-divisor typeclass pathway; no constructor-generated theorem is suggested by this proposition (no newly constructed object with an injectivity equation).

**Composition conclusion: trivial simp composition; policy BORDERLINE.** The installed command's Phase6b explicitly classifies `simp [Foo.bar, Bar.baz, Quux.zog]` as “borderline — record as trivial simp composition; user decides if worth a lemma.” That is exactly route3. It is not the preceding declaration's one bare existing evaluation theorem: the simp route performs generic product, scalar, support-order and logical normalization. Hiding the already registered product theorem from the explicit simp list does not turn this into a bare ≤3 direct mathematical-term chain. The accepted explicit and nonzero routes expose the ingredients. We therefore neither claim an exact named existing theorem nor force NO merely because the proof is short.

The initial requested `probe-mathlib.lean` draft included an unnecessary `0` argument to the generic theorem. The actual `#check` showed that unused section argument is omitted, and it was corrected **before execution**. Exact executed source above is authoritative; drafts are retained only as request history. No failed proof is counted as accepted evidence.

## Phase 7 — Verdict

**BORDERLINE-needs-human.** All evidence checks are complete; the remaining issue is API policy, not missing mathematical evidence or an unverified generalization. The theorem is adequate for the current coefficient signature and monomial callers, has a verified broader arbitrary-upper-function form, and is literature-standard and nonvacuous and useful at three explicit callers. The generic zero-product abstraction already exists, and the residual choose/order conversion is an accepted short simp composition. The command's explicit trivial-simp heuristic calls for a human judgment about whether such a named interface is worth retaining upstream. No cost-based downgrade is used.

Questions for a future upstream API decision:

1. Should the multivariate Hasse-derivative API retain a named natural-binomial vanishing iff because it is the semantic interface used by coefficient and Taylor arguments, despite the accepted generic simp derivation?
2. If `hasseCoeff` is inlined as recommended in its own completed assessment, should the residual product-of-choose/order iff receive a standalone theorem stated directly on `Finsupp.prod`, or should those three callers use local simp facts?
3. If a standalone theorem is desired, should it use the verified more general upper function `k : σ → ℕ`, specializing to finitely supported monomial exponents at callers?

**Recommended current project action:** retain this local theorem while performing this read-only overview. Do not mechanically delete it based on the parent's verdict. No production edit or answer to these upstream-policy questions is required to finish the repository assessment.

If the user chooses generic inlining later, the exact refactor is mechanical and call-site-specific:

- In `MvPolynomial.coeff_hasseDeriv`, replace `(hasseCoeff_eq_zero_iff d k).2 hdk` by a local `hz : hasseCoeff d k = 0` proved with `simpa [hasseCoeff, Nat.choose_eq_zero_iff, Finsupp.le_iff, not_forall] using hdk`; use `hz` in the existing simp call.
- In `MvPolynomial.hasseDeriv_C`, first retain the existing conversion from `hd : d≠0` to `hdk : ¬d≤0`; obtain the corresponding zero-product `hz` by the same generic simp derivation at `(d,0)`, then keep the existing rewrite with `hz`.
- In private `MvPolynomial.coeff_taylor_monomial_single_add_aux`, retain the current coordinate argument `fun hle ↦ h (le_zero_iff.1 (hi ▸ hle i)) : ¬e≤k`; derive `hz` with the generic simp derivation at `(e,k)` and use `hz` in the support contradiction.

When inlining `hasseCoeff` as well, replace its local occurrence by the explicit `d.prod (fun j ↦ (k j).choose)` expression and omit `[hasseCoeff]` from that local fact. These are refactor plans, not claimed compiled whole-project caller rewrites; production was expressly kept unchanged. The core independent product iff and both equivalent forms are actually compiler verified.

Alternative destination if no upstream theorem is desired: keep the helper in `Roth/HasseDeriv.lean` alongside the derivative API; it has concrete cross-file use and needs no `Archive/` or satellite-library move. Missing-API anchor is **none proven**: generic product and scalar vanishing infrastructure exist. The upstream question concerns packaging their order conversion, rather than an unsupported assertion of absence.

## Phase 8 — Acceptance and evidence scope

All phases0–8, all9 literature channels, all5 mathlib methods on all3 forms, all9 modern-idiom questions, all5 proof-strategy questions, all3 statement-shape checks and exact caller inventory are complete. Infrastructure-risk Phase4.5 is explicitly n/a for a theorem. Optional ChatGPT unavailable, local symbol index unavailable, unsupported nLab XHTML, one arXiv HTML404 and an excluded exploratory wrong-ID open are recorded limitations, not silently inferred absences. The successful isolated probes and target proof provide real receipts; no `sorry`, new axiom, unsafe/native computation or raised resource limit was introduced for accepted target probes.

[Machine assessment](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/assessment.json), [target-only overview entry](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/overview-entry.json), [portable link/hash validator](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/validate-artifacts.py), [validated links](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/evidence/report-links.json), [hashed copy manifest](../evidence/MvPolynomial.hasseCoeff_eq_zero_iff/copy-manifest.json).

Next step: carry the three numbered API-policy questions into any prospective mathlib contribution; keep the production source unchanged for this overview and continue to the next declaration after root acceptance.
