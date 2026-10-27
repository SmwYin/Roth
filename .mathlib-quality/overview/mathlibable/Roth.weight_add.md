# `Roth.weight_add` — full assessment (canonical 33)

**Verdict: NO-mathlib-has-it**, under the verified parent re-aim rule. The exact present theorem has a verified term using three existing mathematical facts: `Nat.cast_add`, `add_div`, and `Finset.sum_add_distrib`. The abstract weighted-sum theorem is already `map_add (Finsupp.weight w)`. This assessment changes no production Lean files.

## Phase 0 — baseline and source

The reused baseline `lake build` succeeded with 2467 jobs and no reported warnings or errors. All 17 current source/pin hashes freshly match its manifest: [input check](../evidence/Roth.weight_add/input-check.json), [baseline](../evidence/Roth.weight_add/baseline-build.txt), [manifest](../evidence/Roth.weight_add/input-manifest.json). The public theorem resolves uniquely at `Roth/Box.lean:85`; it contains no sorry. Box supplies bounded multi-index finsets and real weights. Its entire 132-line module was read; [exact source](../evidence/Roth.weight_add/Box-source.lean.txt) and [source hashes](../evidence/Roth.weight_add/source-hashes.json) preserve the inputs. The relevant three caller declarations and surrounding proof contexts were read, with [exact excerpts](../evidence/Roth.weight_add/caller-literature-excerpts.json).

## Phase 1 — comprehension

For a finite set of variables, give an exponent vector `d` weight `Σ j, dⱼ/rⱼ`. Adding two exponent vectors adds their weights. The proof casts coordinatewise natural addition into the reals, distributes division over addition at each coordinate, and distributes the finite sum. No denominator positivity or nonzeroness is needed; division by zero contributes zero in Lean.

The full native elaborated type is:

```lean
@Roth.weight_add : ∀ {σ : Type u} [Fintype σ] (r : σ → ℕ) (d e : σ →₀ ℕ),
  Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e
```

`σ` is universe-polymorphic; `[Fintype σ]` supplies the ambient finite sum; `r` supplies natural denominators; `d,e` are finitely supported natural exponent vectors. There is no `[DecidableEq σ]` in the elaborated type: the source's preceding `omit` removes it. There are no additional hypotheses. Native resolution, original proof replay and standard axioms are preserved in [project receipt](../evidence/Roth.weight_add/native-project.json) and [executed source](../evidence/Roth.weight_add/project-executed.lean.txt).

## Phase 2 — preliminary checks

SMALL: a bookkeeping identity, with no new structure or named theorem, and not a module main result. Exhaustive literature width is retained. The proof has one substantive line; the one-line **definition** test and its three exemptions are n/a because this declaration is a theorem. Short proof length alone does not decide the verdict.

## Phase 3 — exhaustive literature

Exact requests, returned response SHA256/bytes/status, titles and URLs are retained as metadata only. Returned URL query strings are removed with explicit redaction metadata; the original response hash/bytes remain unchanged. A package audit found no AWS credential or signed/token URL patterns. No full external article or search-result bodies are persisted. The protocol's named channels are all accounted for below; no artificial extra channel is introduced to reconcile its informal “nine-channel” count.

| Channel | Actual query/access | Finding and limit |
|---|---|---|
| General web: specific | `Roth index polynomial weight sum i_j r_j additivity derivative index` | Searches the Roth normalization; local clean.tex gives the precise identity. |
| General web: general | `weighted degree monomials additive weight monoid homomorphism` | Weighted sums and weighted degree are the standard concept. |
| General web: alias | `weighted homogeneous polynomial degree additive weights linear functional` | Weighted/quasi-homogeneous terminology; monomial weight is a linear expression in exponents. |
| ChatGPT mathematical MCP | n/a: `ask_chatgpt_math` unavailable | No historical-formulation response was invented. |
| Local references | `rg` on `.mathlib-quality/references/clean.tex`; read §4 lines 530–588 | Positive real `rⱼ` occur in the index definition; the derivative-index proof explicitly splits `Σ(iⱼ+kⱼ)/rⱼ`. Exact excerpt is archived. |
| nLab | Corrected `site:ncatlab.org/nlab/show "free commutative monoid"`; direct open free commutative monoid | Search locates the standard free-monoid abstraction; full open fails with unsupported `application/xhtml+xml` (400). No claim of reading the full page. |
| nCatLab | Search for graded algebra and free commutative monoid on the same nCatLab-hosted nLab; direct open graded algebra | Same actual site; second categorical topic checked. Open fails with the same XHTML limitation; no higher-category theorem is claimed. |
| Stacks | Corrected `site:stacks.math.columbia.edu graded polynomial ring weighted degree`; directly opened Tag 00JL | Section 10.56 gives graded rings, adjacent context rather than this exact rational-weight lemma. |
| MathOverflow | Corrected `site:mathoverflow.net "weighted degree" monomial`; directly opened question 81001 | “What does the d-slice of a weighted polynomial algebra look like?” treats graded polynomial algebras and monomial degrees; no new independent weight-additivity assertion is needed. |
| Recent arXiv (2021-10-26 onward) | Corrected `site:arxiv.org/abs/ "weighted homogeneous" "2023"`; opened abs and HTML of 2312.04677v2 | Badilla-Céspedes–Castorena–Duarte, *Higher Jacobian matrix of weighted homogeneous polynomials and derivation algebras*, first submitted 2023-12-07, revised 2025-07-24; §1.2 is weighted homogeneous context, not an exact Roth API prescription. |
| Supplementary primary reference | Opened MIT *Notes for 18.721, Introduction to Algebraic Geometry*, located §1.8.7, printed p.23 | Defines weighted degree by the exponent/weight dot product. This independently identifies the usual formula. |

Requests are in [web0](../evidence/Roth.weight_add/web0-metadata.json), [web1](../evidence/Roth.weight_add/web1-metadata.json), [web2](../evidence/Roth.weight_add/web2-metadata.json), [web3](../evidence/Roth.weight_add/web3-metadata.json), [primary opens](../evidence/Roth.weight_add/web4-metadata.json), [precise locators](../evidence/Roth.weight_add/web5-metadata.json), and [corrected domain queries](../evidence/Roth.weight_add/web6-metadata.json). Early searches accidentally used `site.` rather than `site:`; these are historical actual requests, superseded by the corrected requests and direct opens, and are not presented as successful domain filters.

Primary locators: [MIT §1.8.7](https://math.mit.edu/classes/18.721/ag-feb20.pdf#page=24), [Stacks 00JL](https://stacks.math.columbia.edu/tag/00JL), [recent arXiv §1.2](https://arxiv.org/html/2312.04677v2#S1.SS2), [MO question](https://mathoverflow.net/questions/81001/what-does-the-d-slice-of-a-weighted-polynomial-algebra-look-like).

Concept: additivity of monomial weighted degree, equivalently extension of generator weights to a homomorphism from the free commutative monoid. The weighted-degree literature often uses positive integer weights; the local index source uses reciprocal positive real parameters. Positivity is useful for later order statements but unnecessary for additivity. The abstract additive-monoid-valued formulation is an algebraic inference, verified against the existing pinned mathlib API, rather than a falsely attributed textbook quote. Historical evolution beyond these examples is not established by this search.

## Phases 4a–4b — all parameters and generality

| Parameter | Need in the current statement | Verified expanded representation |
|---|---|---|
| `{σ : Type*}` | Already arbitrary universe; no restriction to `Fin n`. | `arbitrary_weight` works for arbitrary σ, including infinite ℕ. |
| `[Fintype σ]` | Used by the *existing parent definition*'s `∑ j`; cannot erase from that signature. | Support-based `Finsupp.weight` removes ambient finiteness entirely; an infinite-index example compiles. Finite `Finset s` sums also compile. |
| `r : σ → ℕ` | Fixed by `Roth.weight`; no `0 < r j` assumption is present. | `nat_coefficients` uses arbitrary `r : σ → K` with `[DivisionSemiring K]`, hence arbitrary real and noncommutative division-semiring denominators. |
| `d,e : σ →₀ ℕ` | The two operands are genuinely used; neither can be dropped. | `finite_functions` takes arbitrary functions `σ → K` over a finite finset. `arbitrary_coefficients` takes `σ →₀ K` for any semiring acting on an additive commutative monoid. |
| Output ℝ | Parent-interface choice, not a real-analysis dependency of this proof. | DivisionSemiring formula above; abstract `M` with `[AddCommMonoid M]`, `[Module K M]` for semiring coefficients. For ℕ coefficients the natural module is automatic. |
| Decidable equality | Absent, not an opportunity to remove a hidden assumption. | All decisive current/abstract probes retain no public `[DecidableEq σ]`. |
| Positivity/nonzero denominators | No hypotheses to weaken. | An all-zero denominator example compiles and gives weight zero; adding positivity would unnecessarily narrow additivity. |

The current parent interface is maximally general *within the fixed `Roth.weight` signature*. The expanded mathematical representation is strictly broader, and all expansions above actually elaborate in the [mathlib-only source](../evidence/Roth.weight_add/raw-executed.lean.txt), [receipt](../evidence/Roth.weight_add/native-raw.json). They are not claimed to be a one-edit weakening of `Roth.weight` throughout the project. Their substantive abstract form is already in mathlib:

```lean
example {σ M K : Type*} [Semiring K] [AddCommMonoid M] [Module K M]
    (w : σ → M) (d e : σ →₀ K) :
    Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e :=
  map_add (Finsupp.weight w) d e
```

No new upstream generalization theorem is needed. The reciprocal-weight bridge is itself checked, but it is a proved representation equality, not definitional equality and not an existing replacement theorem.

## Phase 4c — nine modern-idiom rows

| # | Question | Finding / proposed form / concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | No new hypothesis packages to convert. Existing AddCommMonoid/Module classes already express the general weighted sum. |
| 2 | Filters instead of sequences/metrics? | No; finite algebraic identity. |
| 3 | Universal-property characterization? | Yes, conceptually: generator weights extend to an additive map from the free commutative monoid; existing `Finsupp.weight` already implements the linear-combination route, avoiding a new construction. |
| 4 | Bundled substructures? | No sets with closure predicates. A bundled **map**, `Finsupp.weight`, is useful: generic `map_add`, `map_sum`, `map_nsmul` become available. |
| 5 | Weaken field/vector-space hierarchy? | Yes in an expanded representation: any additive commutative monoid with the appropriate scalar action. This permits non-field-valued gradings; verified arbitrary_coefficients. |
| 6 | Higher categories? | No; no category-level coherence data enters this elementary identity. |
| 7 | Concrete index/value structure? | σ already arbitrary; ℕ coefficients and ℝ values can be abstracted as above. Existing Finsupp.weight supports infinite ambient variables, arbitrary generator weights, and semiring coefficients. |
| 8 | Concrete-via-abstract diagnostic? | Fires on the specialized parent operation: the sole body line contains `weight` once and no real-specific theorem. After unfolding, no Roth operation remains; only casts, division, and finite sums. Its abstract content is the existing map_add, not new mathematics about a distinguished Roth object. |
| 9 | False-generalization guard? | The reciprocal-weight specialization preserves the object, with a compiled bridge. Reject replacing reciprocal weights by `r` itself or replacing monomial weight by polynomial maximum degree/index: these change the mathematical function. Reject deletion of the second summand: a Unit example with r=1 shows the resulting equality is false. |

Modern idiom available: yes, already present upstream. It exposes generic homomorphism operations and arbitrary-variable weighted gradings, a real organizational benefit. Migrating the project parent is a separate representation refactor, not grounds for calling this exact theorem an existing one-call specialization without the bridge.

## Phase 4.6 — five proof-strategy rows

| # | Strategy question | Answer |
|---|---|---|
| 1 | ε–δ versus filters? | n/a: no topology. |
| 2 | Elements versus ideals/submodules? | No ideal or inclusion argument; for the fixed ratio definition the coordinate finite-sum proof is idiomatic. With a bundled parent, map_add is preferable. |
| 3 | Sequences versus nets? | n/a: no analysis. |
| 4 | Constructed category objects versus universal properties? | No categorical construction in this theorem; the existing Finsupp.weight already supplies the relevant additive map. |
| 5 | Missing helper that should exist? | No: Nat.cast_add, add_div, finite-sum distribution, and the bundled weighted map are all present. |

Current strategy: MATHLIB-IDIOMATIC for the current parent. A future parent migration should use `map_add`; no missing-helper PR is indicated. Cost is not used to choose the verdict.

## Phase 4.5 — infrastructure risk

n/a: theorem. The six risk rows (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism issues, coercion ambiguity) assess newly introduced definitions/classes/instances; this theorem introduces none. A suggested migration of the parent is not silently enacted here.

## Phase 5 — all five actual mathlib search methods

Each method was attempted on current ratio, literature weighted-degree, and abstract homomorphism forms. Raw requests/responses: [current](../evidence/Roth.weight_add/search-current.json), [literature](../evidence/Roth.weight_add/search-literature.json), [abstract](../evidence/Roth.weight_add/search-abstract.json), [abstract Loogle retry](../evidence/Roth.weight_add/search-abstract-loogle-retry.json). Initial exploratory receipts are also archived. [Exact CLI receipts](../evidence/Roth.weight_add/source-search.json) preserve untruncated rg output and exit statuses.

| Method | Current | Literature | Abstract |
|---|---|---|---|
| Lean-Finder | finite ratio sum query: weight_apply, unrelated centroid weights | monomial weighted-degree query: IsWeightedHomogeneous.mul and monomial theorem | AddMonoidHom.map_add and generic map_add |
| Loogle | `Finset.sum_add_distrib` exact signature | `Finsupp.weight` exact bundled definition | initial type-pattern query failed; retry `AddMonoidHom.map_add` returns exact signature |
| LeanSearch | ratio distribution query returns add_div and sum_div | weighted finite-exponent query returns weight_apply and homogeneous multiplication | additive homomorphism query returns map_add |
| rg source | Nat.cast_add; add_div; generated sum_add_distrib via prod_mul_distrib | weight and weight_eq_sum, WeightedHomogeneous usages | Hom/Defs map_add, bundled definition; exact Roth.weight_add/Finsupp.weight_add full-name declaration search has no hit |
| Local name search | sum_add_distrib query incomplete cardinal hits | Finsupp.weight family located | map_add query incomplete assorted namespaces |

Local search honestly reports `index: unavailable`; it is not evidence of absence. External indexes need not match this repository revision; pinned source reads and native positive probes verify the used candidates. WeightedHomogeneous.mul concerns multiplying polynomials with degree predicates, and is not itself the current ratio theorem. `Finset.sum_div` only factors a common denominator and is insufficient for coordinate-dependent `r`.

Pinned building blocks:

* `Nat.cast_add`, `Mathlib/Data/Nat/Cast/Defs.lean:100`: addition preserved by natural cast, under AddMonoidWithOne.
* `add_div`, `Mathlib/Algebra/Field/Basic.lean:36`: division distributes over numerator addition under DivisionSemiring, including zero denominators.
* `Finset.sum_add_distrib`, generated by `@[to_additive]` from `prod_mul_distrib`, `Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:310`: finite sum of pointwise sums equals sum of the two sums.
* `Finsupp.weight`, `Mathlib/Data/Finsupp/Weight.lean:82`, `weight_eq_sum` at line 100, and generic `map_add` in `Mathlib/Algebra/Group/Hom/Defs.lean`: the existing abstract route.

Conclusion: the abstract law exists as `map_add (Finsupp.weight w)`; for the exact current definition the three arithmetic building blocks compose. No absence claim rests on an empty search, timeout, or index limitation. No project lemma counts as a decisive mathlib building block.

## Phase 5.5 — three statement-shape checks

Normal form: OK. The expanded sum is on the RHS, matching generic map_add and finite-sum normalization. Reversed equality is equivalent and compiled as `WeightAddConsumerChecks.reversed`, but is less useful for the three rewrite callers. The bundled equality is the abstract alternate form, separately compiled; converting the parent is not a mere reorientation.

Syntactic generality: OK for current API. Explicit `r d e` is convenient for an applied equality; rewriting infers them at all three callers. Reverse orientation and bundled-map shape were actually tried, not assumed. Superfluous-argument audit: σ supplies the domain; Fintype supplies the parent sum; r supplies each denominator; both d and e contribute; no extra decidable equality, positivity, or unused proof arguments exist. NONE to drop within this signature. Overall SHIP-AS-STATED as a local helper, while upstream organization prefers the existing bundled API.

## Phases 6.0 and 6 — callers, inline audit, composition

Internal explicit source-use count: **3**, in **3 distinct external-to-Box files**. No self-use beyond its declaration. These are textual callers, not a claim to enumerate kernel or simp dependency closure; the theorem itself has no simp attribute.

| Caller | Use and mechanical refactor |
|---|---|
| `Roth/Lattice.lean:155`, private `card_filter_fiber_eq` | `rw [weight_add, weight_mapDomain ..., weight_single, mul_div_assoc]`. Insert a local equality for `d.mapDomain Fin.castSucc` and `single (Fin.last n) i` proved by the explicit term below; use it as the first rewrite, preserving subsequent mapDomain/single rewrites. `fin_split` verifies this exact index shape. |
| `Roth/Index.lean:114`, `index_sub_weight_le_index_hasseDeriv` | `simpa [weight_add, hiw] using index_le_weight ...`. Supply the equality for `(i,k)` by the term below and replace weight_add in this normalization with that equality; retain hiw and sub_le_iff_le_add. `index_bound` verifies the resulting weight/subtraction step, not the entire index theorem. |
| `Roth/Theta.lean:391`, `sum_max_sub_le_index_det` | `rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1`. Supply the equality for `(D μ).mapDomain some` and `single none ν` by the term below and use it for the first rewrite. `option_split` verifies the mapDomain+single application. |

Inline-derivation audit: rg of weight-plus-weight expressions, add_div and sum_add_distrib across `Roth/` finds no separate rederivation of this identity outside its proof. Three uses signal a useful local API; this signal does not manufacture an upstream gap when the direct arithmetic composition and the abstract map are already available.

Attempt 1: the original `simp [weight, add_div, Finset.sum_add_distrib]` succeeds. Under Phase 6b this alone is only a trivial-simp **borderline** signal; it does not justify NO by itself.

Attempt 2, exact old-form composition: the exact current statement elaborates with this term (line wrapping only; exact executed version is archived):

```lean
(congrArg (fun f : σ → ℝ ↦ ∑ j, f j)
  (funext fun j ↦ (congrArg (fun x : ℝ ↦ x / (r j : ℝ))
    (Nat.cast_add (d j) (e j))).trans (add_div _ _ _))).trans Finset.sum_add_distrib
```

There are exactly **three instantiated mathematical library theorem applications**, in dependency order: Nat.cast_add, add_div, Finset.sum_add_distrib. Core `congrArg`, `funext`, and `Eq.trans` only transport/compose these equalities; they supply no new arithmetic premise. The function-extensionality step establishes the pointwise normalization premise explicitly. `Roth.weight` unfolding and `(d+e) j = d j + e j` are definitional reductions in this term. In particular **Finsupp.add_apply is not an additional theorem application here**: the elaborator reduces it without rewriting. Nat.cast_add and add_div are not definitional and are both counted. This old-form proof uses neither simp nor the target theorem nor a downstream lemma.

The proof is `WeightAddAssessment.three_named_facts` in the project receipt, and `RawWeightAddAssessment.original_three_facts` independently repeats the formula with mathlib-only imports and `#check_failure Roth.weight_add`. The native root returned terminal success, no errors, no warnings, no timeout, project partial=false; all printed proof axioms are within propext/Classical.choice/Quot.sound. [Verification map](../evidence/Roth.weight_add/verification.json) ties exact executed sources to raw complete receipts and source checks.

Attempt 3: `map_add (Finsupp.weight w) d e` succeeds for arbitrary coefficients/weights and infinite ambient indices. The checked ratio bridge specializes it, but the bridge is a new proved normalization step. It is not mislabeled an existing one-call theorem about Roth.weight.

Conclusion: **COMPOSABLE**, based on Attempt 2, beyond the original simp-only evidence. Actual caller experiments verify all three distinct substitution shapes and the inequality manipulation; they do not claim three fully migrated source files or a production rebuild after a migration that was never performed.

## Phases 7–8 — verdict and action

**NO-mathlib-has-it.** The generic replacement parent `Finsupp.weight` already satisfies existing `map_add`. The explicit parent re-aim rule requires this verdict once that analogous law and its reciprocal-weight specialization have been verified. Cast/division normalization is a real bridge, not definitional equality; it does not turn the existing abstract law into a new upstream gap. The three-fact old-form proof remains valid but does not determine the final routing.

The alternative local destination is the existing `Roth/Box.lean`: a short named helper remains reasonable for three project rewrite sites if retaining the current parent interface. This mathematical assessment recommends no independent mathlib PR for it. If the project chooses wrapper removal, inline Attempt 2 via a local equality at **each of the three named callers**, as specified above, then delete weight_add and rebuild the affected modules. If the project instead migrates the parent to the existing Finsupp.weight reciprocal specialization, use `map_add` at those sites after proving/using the representation bridge. Neither migration is performed by this read-only overview.

All mandatory phases are complete; unresolved verification items: **[]**. Root independent acceptance remains pending. [Portable validator](../evidence/Roth.weight_add/validate.py) checks current manifest hashes/bytes, source/pin hashes, terminal native success, standard axioms, exact source bindings and report links in scratch or integrated layout.

## Re-aim rule correction and supplemental verification

The initial report classified the old ratio representation by its three-fact
composition. That classification overlooked `mathlibable.md`, Mode B,
**Re-aim rule** (installed lines 1192–1207): when a parent is NO-mathlib-has-it
because a more general definition D′ exists, and D′ has the analogous law,
record the dependent lemma as NO-mathlib-has-it citing that law.
Parent `Roth.weight` was already verified against `Finsupp.weight`.
Its analogous law is existing `map_add` for that bundled additive map.
This is a checked re-aim, not blind inheritance or an unsupported absence claim.

The [exact supplemental source](../evidence/Roth.weight_add/reaim-executed.lean.txt)
proves the reciprocal bridge and `RawWeightReaimChecks.add_via_existing_map` with
mathlib-only imports; [native receipt](../evidence/Roth.weight_add/native-reaim.json)
has terminal success, no errors/warnings, and standard axioms only.
No Roth import or target theorem is used. The bridge is explicitly a proved
normalization step and is not counted as an existing library lemma.
At the re-aimed interface the law is one existing `map_add` application.

Future action: coordinate parent migration to reciprocal `Finsupp.weight`,
then use `map_add` and the existing quotient bridge at the consumers already
audited above. Keep a project-local compatibility wrapper until the parent
and complete dependent modules compile. No independent upstream preservation
theorem is needed. Existing original-form composition, caller fragments,
generality checks, literature and searches remain valid; production is unchanged.
The [correction record](../evidence/Roth.weight_add/verdict-correction.json) preserves
the prior verdict and report hash. This changes the bucket, not the number
of completed declarations or the next declaration.
