# Roth.weight_eq_zero_iff — BORDERLINE-needs-human

## Phase 0 — baseline

The shared successful `lake build` covered 2467 jobs. All 17 source/pin hashes freshly match that baseline; production is unchanged. Declaration resolves at `Roth/Box.lean:91`, with no sorry. Full declaring module and sole caller module were read. [Baseline](../evidence/Roth.weight_eq_zero_iff/baseline-build.txt), [fresh hashes](../evidence/Roth.weight_eq_zero_iff/source-hashes.json), [Box](../evidence/Roth.weight_eq_zero_iff/Box-source.lean.txt), [Index](../evidence/Roth.weight_eq_zero_iff/Index-source.lean.txt).

## Phase 1 — mathematical content

A finitely supported natural multi-index has real weight Σⱼ dⱼ/rⱼ. If every natural denominator is positive, that weight vanishes exactly when the multi-index is zero. Nonnegative summands preclude cancellation; nonzero denominators then force each numerator to vanish. Conversely zero numerators give zero weight.

The full type is `∀ {σ : Type u} [Fintype σ] {r : σ → ℕ}, (∀ j, 0 < r j) → ∀ {d : σ →₀ ℕ}, Roth.weight r d = 0 ↔ d = 0`. There is no `DecidableEq σ` parameter: the preceding `omit` excludes it. No project theorem is explicitly called by the source proof; it unfolds project `weight` and simplifies arithmetic and finsupp equality. Native elaborated signature and axiom evidence are preserved below.

## Phase 2 — preliminary checks

BIG by the command's formal classification because the module lists this theorem under Main results; mathematically it is elementary bookkeeping. Definition-only one-line test is n/a for a theorem. Its one-line `simp [weight, …]` is not definitional equality and is not a ≤3-call certificate. No verdict is inherited from the parent definition.

## Phase 3 — exhaustive literature

Every named channel was executed. Search responses are represented only by exact requests, SHA256/bytes/status, source locators and original summaries; no article bodies are retained. Credential-bearing returned URL queries are stripped if detected, with counts in metadata.

| Channel | Actual search/access and finding |
|---|---|
| General web, current | `Roth theorem index positive weights sum i_j r_j zero`: Min Ru's university notes, Roth’s Theorem, Definition 1 pp. 2–3, positive integer denominator weights; [receipt](../evidence/Roth.weight_eq_zero_iff/web0-metadata.json). |
| General web, standard | `nonnegative finite sum zero if and only if each summand zero positive weights`: returned positive sums/probability and unrelated combinatorics; no sharper named theorem used; [receipt](../evidence/Roth.weight_eq_zero_iff/web1-metadata.json). |
| General web, abstract | `positive linear functional nonnegative cone kernel weighted sum zero`: ordered vector spaces/positive linear functionals; supports the language of positive cone but no claim of exact theorem match; [receipt](../evidence/Roth.weight_eq_zero_iff/web2-metadata.json). |
| Local source | clean.tex §4, lines 536–569 explicitly explains nonnegative weights and zero iff all exponents zero; [hash/excerpt](../evidence/Roth.weight_eq_zero_iff/local-literature.json). |
| nLab | Correct `site:ncatlab.org/nlab/show positive cone ordered vector space` query located positive cone; direct access failed unsupported XHTML; [search](../evidence/Roth.weight_eq_zero_iff/web3-metadata.json), [access](../evidence/Roth.weight_eq_zero_iff/web8-metadata.json). |
| nCatLab | Correct `site:ncatlab.org "ordered commutative monoid"` query found nearby order terminology. Direct ordered-commutative-monoid URL inaccessible; no exact theorem claimed; [search](../evidence/Roth.weight_eq_zero_iff/web4-metadata.json). |
| Stacks | Correct domain query `site:stacks.math.columbia.edu ordered monoid positive sum zero`: returned unrelated algebra/scheme references; no relevant exact result; [receipt](../evidence/Roth.weight_eq_zero_iff/web5-metadata.json). |
| MathOverflow | Correct domain query `site:mathoverflow.net positive weights weighted sum zero nonnegative`: positive weighted-sum questions, mostly different problems; no authoritative exact replacement; [receipt](../evidence/Roth.weight_eq_zero_iff/web6-metadata.json). |
| Recent arXiv | Correct domain query with years 2022–2026, within 2021-10-26 through 2026-10-26. Salami, *Roth's theorem on weighted projective lines*, 2610.17589 (2026-10-13), accessed abstract; its weighted geometry and warning about naive index rescaling do not negate elementary positive-sum separation. Other hits concern additive-combinatorial Roth; [search](../evidence/Roth.weight_eq_zero_iff/web7-metadata.json), [access](../evidence/Roth.weight_eq_zero_iff/web8-metadata.json). |
| ask_chatgpt_math | Unavailable in exposed tool inventory; optional channel honestly unexecuted. |

Primary source: [Min Ru, Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf), Definition 1 pp. 2–3, direct PDF accessible, lines 165–181. It confirms denominator-positive natural exponents; it does not independently assert the exact zero-fiber lemma. [Recent arXiv abstract](https://arxiv.org/abs/2610.17589) is supplementary context only. The exact project source supplies the strongest literature match. The standard abstract statement is separation of zero by a strictly positive weighted sum on the nonnegative cone. It requires no polynomial, root, or finite ambient variable set if the exponent vector is finitely supported.

## Phases 4a–4b — parameters and verified generality

| Parameter | Essential scope / tested alternative |
|---|---|
| `σ : Type*` | Already universe polymorphic, no inhabitance needed. |
| `[Fintype σ]` | Required by the fixed project definition, which sums over `univ`. Generic `Finsupp.weight` sums support and works on arbitrary σ; changing the parent is a representation redesign. |
| `[DecidableEq σ]` | Already absent; no weakening to claim. |
| `r : σ → ℕ` | The parent interface fixes natural denominators. Real positive weights are an expanded representation, not merely dropping an instance. |
| `d : σ →₀ ℕ` | Nonnegativity prevents cancellation; arbitrary signed coefficients/weights cannot be substituted without hypotheses. |
| `hr : ∀ j, 0 < r j` | Actual mechanically verified weakening: `∀ j ∈ d.support, 0 < r j`, same original conclusion. Zero denominators off support are irrelevant. |
| Strict positivity | Cannot weaken to nonnegativity on occupied coordinates: division by zero is defined as zero in Lean, annihilating a nonzero exponent. |

Verdict: STRICTLY NARROWER THAN STANDARD positive-support principle, with one verified assumption localization. Proposed fixed-interface restatement:

```lean
theorem weight_eq_zero_iff {r : σ → ℕ} {d : σ →₀ ℕ}
    (hr : ∀ j ∈ d.support, 0 < r j) : Roth.weight r d = 0 ↔ d = 0
```

The global version follows by `fun j _ ↦ hr j`. Root's `WeightEqZeroAssessment.support_positive` compiled under this exact weakening. A separate positive-real `Finsupp.weight` theorem removes ambient finiteness; its new helper proof is not an existing mathlib replacement. Cost: support localization CHEAP; parent representation migration MODERATE. Neither cost determines the verdict.

## Phase 4c — nine modern-idiom checks

| # | Check | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of hypotheses | No: positivity depends on the particular weight function/support; a global custom instance would obscure local data. Existing `NonTorsionWeight` is relevant only with the full ordered-codomain assumptions. |
| 2 | Sequences versus filters | n/a: finite algebraic sum, no topology. |
| 3 | Universal property | No new object constructed; existing additive-hom representation is preferable to a new universal-property class. |
| 4 | Bundled substructures | Possible NNReal-valued weights encode positivity/nonnegativity, but require a coercion bridge and nonzero weights; no direct ℝ specialization. |
| 5 | Typeclass hierarchy | Yes: positive `Finsupp.weight` is meaningful in ordered additive settings. Tested positive-real form drops ambient Fintype; the arbitrary ordered-additive-monoid form is also compiled; no untested maximal hierarchy is claimed. |
| 6 | Higher category | n/a: no categories. |
| 7 | Existing modern API | Yes: `Finsupp.weight : (σ →₀ ℕ) →+ M` composes with map-zero/map-add, support API and polynomial weighted degrees. Project reciprocal sum requires a bridge. |
| 8 | Concrete-via-abstract diagnostic | Fires: `weight` appears only in the first unfolding (the single proof line); no later project-specific operation exists. Content is a nonnegative-sum zero theorem plus denominator/cast separation. The generic positive-real proof works on arbitrary σ. |
| 9 | False-generalization guard | Reject arbitrary signed nonzero weights: +1 and −1 cancel on two nonzero exponents. Reject zero natural denominators even on Unit. Keep positive weights / positivity on occupied support; preserve natural coefficients. |

The compiled abstract signature is:

```lean
theorem positive_weight {σ M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {w : σ → M} (hw : ∀ j, 0 < w j) {d : σ →₀ ℕ} :
    Finsupp.weight w d = 0 ↔ d = 0
```

This compiled theorem has arbitrary ambient `σ`; its exact classes are `AddCommMonoid M`, `PartialOrder M`, and `IsOrderedAddMonoid M`. It has no `CanonicallyOrderedAdd M` assumption, so it applies to ℝ with its usual order. It is new scratch code, not an existing library lemma. The separately compiled ordered-field representation has `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, `r : σ → K`, and positivity only on `d.support`, with conclusion `(∑ j, (d j : K) / r j) = 0 ↔ d = 0`. The compiled strict Bool witness takes `d = Finsupp.single false 1` and `r j = if j then 0 else 1`: positivity holds at every `j ∈ d.support`, while global positivity fails at `true`. Thus the localization is strictly weaker, not merely a restatement.

Modern idiom available: yes, explicitly positive ordered `Finsupp.weight`, with finite-support rather than ambient Fintype. This improves reuse by multivariate polynomial/power-series weighted support; no new category machinery is justified. The existing canonical-order zero theorem is a partial match, not a proof for ℝ.

## Phase 4.5 — infrastructure risks

n/a: theorem. All six definition-only rows (diamond, reducibility leak, noncanonical unfolding, instance priority, universes, coercions) are inapplicable: this declaration introduces no data, instances, coercion or definitional reduction rule. This does not assert that a hypothetical NNReal parent refactor has no infrastructure cost.

## Phase 4.6 — proof strategy

| # | Check | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Elements versus bundled inclusions | No ideal/submodule containment; coordinate extensionality is appropriate. Bundled additive weight is a useful representation alternative. |
| 3 | Sequences versus nets | n/a, no convergence. |
| 4 | Explicit construction versus universal property | n/a, no construction. |
| 5 | Missing useful helper | Candidate: positive-weight zero-fiber theorem for `Finsupp.weight` in ordered additive codomain, rather than only canonical order; positive-real route verified. This is an API-design question, not established absence. |

Current strategy MATHLIB-IDIOMATIC for the fixed project representation: sum-zero nonnegativity plus pointwise zero. Representation refactor would expose additive-hom API but should not hide the required positivity hypothesis.

## Phase 5 — all five actual mathlib methods

Each method was invoked on current reciprocal sum, literature-standard nonnegative finite sum, and abstract positive finsupp weight. Exact queries and complete responses are in `search-{current,literature,abstract}-{finder,loogle,leansearch,local}.json`; [current Finder](../evidence/Roth.weight_eq_zero_iff/search-current-finder.json), [standard Loogle](../evidence/Roth.weight_eq_zero_iff/search-literature-loogle.json), [abstract Loogle](../evidence/Roth.weight_eq_zero_iff/search-abstract-loogle.json), [abstract LeanSearch](../evidence/Roth.weight_eq_zero_iff/search-abstract-leansearch.json), [local](../evidence/Roth.weight_eq_zero_iff/search-abstract-local.json), [untruncated source searches](../evidence/Roth.weight_eq_zero_iff/source-search.json).

| Method | Finding |
|---|---|
| Lean-Finder | Existing canonical-order `Finsupp.weight_eq_zero_iff_eq_zero`, nonnegative finite sum theorem; abstract le-weight lower bound. External indexed revision can differ from pinned source. |
| Loogle | Current reciprocal pattern empty; standard finite-sum pattern finds sum-zero lemmas; abstract pattern returns canonical-order weight theorem. |
| LeanSearch | Same positive candidates, plus `Finsupp.degree_eq_zero_iff` and `Finsupp.coe_eq_zero`; degree is not a variable-weight replacement. |
| rg | Pinned full source and full-name matches inspected. Positive candidate theorem at `Mathlib/Data/Finsupp/Weight.lean:173`; lower bound at :150; sum-zero in `Algebra/Order/BigOperators/Group/Finset.lean`. Homogenization's unrelated weight theorem is not this map. |
| lean_local_search | Actual calls returned source hits but `index=unavailable`. Empty local standard-name response is not evidence of absence; source/native checks establish positive candidates. |

Pinned `Finsupp.weight_eq_zero_iff_eq_zero` requires `[AddCommMonoid M] [PartialOrder M] [IsOrderedAddMonoid M] [CanonicallyOrderedAdd M]` and `[NonTorsionWeight ℕ w]`. ℝ has negative elements and cannot have its standard order canonically ordered from zero, so specializing M=ℝ fails its essential assumption. NNReal works at the conceptual level, but needs non-torsion construction, coefficient/smul/division identification and coercion-of-sum/zero bridge. These steps are not definitional and have not yielded a direct ≤3-call replacement. [Pinned source](../evidence/Roth.weight_eq_zero_iff/Finsupp-Weight-source.lean.txt).

Conclusion: found partial match and building blocks; no claim that exhaustive searches prove absence. The positive-real helper is new scratch mathematics, not a fourth existing search result. No exact?/search timeout is used as absence evidence.

## Phase 5.5 — statement shape

Normal form is `weight … = 0 ↔ d = 0`, with zero finsupp on RHS. Equivalent forms are `∀ j, d j = 0`, `d.support = ∅`, and positivity `0 < weight … ↔ d ≠ 0`; avoid introducing O(n²) equivalence wrappers. Existing `Finsupp.ext_iff`/`coe_eq_zero` explain the normal form. Syntactic alternatives actually tested: original global positivity, localized support positivity, and arbitrary-σ positive-real `Finsupp.weight`. At the unique current caller global `hr` is convenient; support form accepts `fun j _ ↦ hr j` mechanically. No unused typeclass is present. `Fintype` is fixed by parent `weight`, not mathematically needed after changing representations. Overall RESTATE-BEFORE-SHIP if upstreaming: choose the abstract positive-weight API rather than exporting the Roth-specific reciprocal parent.

## Phases 6.0–6 — callers, inline audit, composition

Internal explicit source calls: **1**, in **1** file. `Roth/Index.lean:102`, inside `index_eq_zero_iff`, uses `rw [h, weight_eq_zero_iff hr] at hdw` to force an attained multi-index to zero. `Roth/Box.lean:31` is documentation, :91 declaration, not calls. No source caller elsewhere after full qualified/unqualified search. Searches for weight-zero and sum-zero/div-zero patterns found no separate inline rederivation. This is source usage, not a complete kernel or simp dependency closure. The theorem has no simp attribute.

The exact source replay closes by `simp`; Phase 6b routes such a composition to BORDERLINE unless a ≤3 existing-call term is actually established. Here it has not been established. Arithmetic/representation facts include at least: `Finset.sum_eq_zero_iff_of_nonneg`, `Nat.cast_nonneg`, `div_nonneg`, `div_eq_zero_iff`, natural cast zero/injectivity (`Nat.cast_eq_zero`), positivity-implies-nonzero (`ne_of_gt`/`LT.lt.ne'`), `Finsupp.ext_iff`, finsupp zero evaluation (`coe_zero`/`zero_apply`), and `Finset.mem_univ` for the universal index set. Logical simplifications of `or_false`, implications and quantifiers also occur. This is a lower-bound inventory of source-level dependencies, not an exact count of the elaborator's entire simp proof DAG; it already exceeds three. Extensionality and cast transport are not free definitional equalities. `weight` unfolding itself is definitional. `Nat.cast_nonneg` is instantiated for numerator and denominator. Source's `(hr _).ne'` supplies denominator nonzero; no cancellation guard may be omitted.

Alternative generic proof uses `Finsupp.le_weight_of_ne_zero`, `(hw j).le`, `not_le_of_gt`, coordinate `Finsupp.ext`, zero evaluation and `map_zero`. Even before the reciprocal bridge this is not certified as ≤3 existing arithmetic/representation facts. Adding a new helper and then counting it as a mathlib call would be circular accounting.

The compiled caller experiment `WeightEqZeroConsumerChecks.index_zero_step` matches the actual attained-weight shape: `hdw : Roth.weight r d = i` and `hi : i = 0`. It concludes `d = 0` by

```lean
(WeightEqZeroAssessment.support_positive (fun j _ ↦ hr j)).mp (hdw.trans hi)
```

The compiled `WeightEqZeroConsumerChecks.reversed` also verifies `d = 0 ↔ Roth.weight r d = 0` using `.symm` of the weakened helper. These are exact substitution fragments, not a full rebuild of a migrated `Roth/Index.lean` module. [Executed project source](../evidence/Roth.weight_eq_zero_iff/project-executed.lean.txt), [terminal native receipt](../evidence/Roth.weight_eq_zero_iff/native-project.json).

At the sole caller, retain existing rewrite while design is unresolved. If support-local API is adopted, replace the argument by `fun j _ ↦ hr j`. If the wrapper is eventually removed, inline the native-verified sum-zero proof at :102 after rewriting `h`; do not claim this is presently a ≤3-call mandated deletion. Alternative destination: existing project-local `Roth/Box.lean`, where it serves the index API.

## Phase 7 — verdict and concrete design questions

**BORDERLINE-needs-human.** The existing generic weight zero theorem does not specialize to ℝ. The original source is a closing simplification combining more than three arithmetic/representation facts, and has one genuine downstream use. Support positivity is a verified mechanical weakening, while a reusable upstream contribution would more naturally address positive `Finsupp.weight` in an ordered codomain. Search and proof evidence do not settle which API maintainers should prefer; no cost-based downgrade is involved.

1. Should `Mathlib/Data/Finsupp/Weight.lean` add a positive-weight zero-fiber lemma for ordered additive codomains lacking `CanonicallyOrderedAdd`, using the verified ordered-additive-monoid form?
2. Should that new theorem localize positivity/non-torsion to `d.support`, keeping irrelevant zero weights admissible?
3. Should project reciprocal weights migrate to an NNReal/generic `Finsupp.weight` representation with a real coercion bridge, or retain the present project interface?

No unresolved verification remains after the native receipts below; these are upstream API choices, not requests to interrupt the overview. Keep production unchanged, record the candidate gap, and revisit after resolving representation policy. A YES decision would need an actual agreed generic statement and upstream review; this package makes no unsupported YES grouping or reviewer nomination.

## Phase 8 — verification and handoff

[Verification map](../evidence/Roth.weight_eq_zero_iff/verification.json) identifies exact executed sources, native receipts and source-hash checks. Both project target/support-local proof and isolated mathlib-only original/generic/false-guard experiments were verified by root; standard axioms only, no raised limits or production edits. Rejected attempts, if any, remain separate. [Assessment](../evidence/Roth.weight_eq_zero_iff/assessment.json), [portable validator](../evidence/Roth.weight_eq_zero_iff/validate.py), [current artifact manifest](../evidence/Roth.weight_eq_zero_iff/copy-manifest.json).
