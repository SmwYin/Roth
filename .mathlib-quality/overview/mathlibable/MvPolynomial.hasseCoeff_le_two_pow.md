# Full mathlibable assessment: MvPolynomial.hasseCoeff_le_two_pow

**Verdict: BORDERLINE-needs-human.** The bound is elementary but does more than a demonstrated three-call term: multiplication of coordinatewise choose estimates also needs power/product normalization and support/full-product conversion. Two downstream coefficient estimates use it. A support-local hypothesis weakening and a sharper arbitrary-variable support bound actually compile. Whether to add a generic finite-product binomial estimate upstream, or keep the Hasse-named packaging locally, is an API-design question. This assessment does not inherit a verdict from the scalar alias or its full-product helper.

## Phase 0 — Baseline and identity

Canonical declaration 24 is the theorem at Roth/HasseDeriv.lean:276, with conclusion on line277. The initial assignment's line277 was the continuation; source grep and canonical ordering fix the actual head. The full declaring module and full CoeffNorm caller module were read. No production source, pins, Git state or progress records are changed.

The shared baseline lake build succeeded (2467 jobs). All 17 source/pin hashes were freshly compared before reuse: [baseline](../evidence/MvPolynomial.hasseCoeff_le_two_pow/baseline-build.txt), [input manifest](../evidence/MvPolynomial.hasseCoeff_le_two_pow/input-manifest.json), [fresh check](../evidence/MvPolynomial.hasseCoeff_le_two_pow/input-check.json). [Source hashes](../evidence/MvPolynomial.hasseCoeff_le_two_pow/source-hashes.json) cover declaring module, actual callers, local reference and pinned positive building blocks. Exact native sources and complete receipts are indexed in [verification](../evidence/MvPolynomial.hasseCoeff_le_two_pow/verification.json).

## Phase 1 — Mathematical content and full type

For finite variable type σ, natural exponent multiindices d,k, and a box bound r, the product of binomial factors associated with a Hasse derivative is at most 2 raised to the sum of box side exponents:
`hasseCoeff d k ≤ 2 ^ (∑ j, r j)` when `∀ j, k j ≤ r j`.

The actual elaborated type is:
```lean
theorem MvPolynomial.hasseCoeff_le_two_pow {σ : Type*} [Fintype σ]
    {d k : σ →₀ ℕ} {r : σ → ℕ} (hk : ∀ j, k j ≤ r j) :
    MvPolynomial.hasseCoeff d k ≤ 2 ^ (∑ j, r j)
```

No R or CommSemiring parameter occurs despite the surrounding section. The proof replaces support product with full product, rewrites the power of a sum as a product of powers, and uses `Nat.choose_le_two_pow` followed by monotonicity of natural powers at each coordinate, lifted with `Finset.prod_le_prod`. It needs no assumption d≤k: a violating binomial factor is zero and the estimate remains valid. Empty variable types, d=0, zero r, and k=0 are allowed. It is an inequality in ℕ, before casts into coefficient estimates. [Exact source excerpt](../evidence/MvPolynomial.hasseCoeff_le_two_pow/target-excerpt.lean.txt).

## Phase 2 — Size and one-line test

SMALL: finite combinatorial bound, with no new structure or analytic machinery. The one-line definition-only test is n/a: this is a theorem, not a definition, class or instance. A short proof signals potential composability but does not bypass the full search. Actual native replay verifies the source proof independently of a call to the target.

## Phase 3 — Exhaustive literature

All required named channels were attempted, including three distinct general queries: [full table and summaries](../evidence/MvPolynomial.hasseCoeff_le_two_pow/literature.md), [exact requests, response hashes/bytes/status and locators](../evidence/MvPolynomial.hasseCoeff_le_two_pow/web-requests.json), [local source](../evidence/MvPolynomial.hasseCoeff_le_two_pow/reference-excerpt.tex). Optional ask_chatgpt_math is unavailable. Direct nCatLab access failed; indexed nLab content was accessible. These limitations do not establish absence.

Local clean.tex section3 lines457–461 explicitly bounds the coefficient of a differentiated monomial by B times the product of coordinate binomial coefficients, then B2^S. [Multiplicity codes section3](https://people.csail.mit.edu/dmoshkov/courses/codes/Multiplicity.pdf) and [multipoint evaluation section3.2](https://mrinalkr.bitbucket.io/papers/MME2.pdf) supply standard multivariate Hasse formulations. [nLab's several-indeterminate definition](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative) supplies the binomial product interpretation; [Stacks07GK](https://stacks.math.columbia.edu/tag/07GK) supplies related divided-power context. Recent 2022 and2024 arXiv applications were checked within the five-year window; their abstracts do not claim this exact estimate.

Literature-standard mathematical target, inferred from the Hasse formulas and scalar binomial-row bound rather than located as a named finite-set theorem in these sources: for any finite set S and ordinary natural-valued functions d,k,r, pointwise box bounds on S give
`(∏ j ∈ S, (k j).choose (d j)) ≤ 2 ^ (∑ j ∈ S, r j)`.
The global finite-variable result is a useful specialization. Selecting S=support(d) both sharpens the exponent and removes global finiteness. No historical shift in the elementary estimate was evidenced.

## Phases 4a–4b — Every parameter and generality

| Parameter or condition | Audit and verified conclusion |
|---|---|
| Universe/type σ | Already arbitrary universe/type. Global Fintype only enumerates the literal global sum. |
| Fintype σ | Essential to the stated expression `∑ j, r j`; not essential to the mathematical support estimate. Arbitrary-σ support bound compiles. This is a changed representation/exponent, not silently dropping an instance from an ill-typed expression. |
| d : σ →₀ ℕ | Supplies derivative orders and product support. No bound, nonzero or disjointness hypothesis needed. Full finite-set formulation can instead take an ordinary function d. |
| k : σ →₀ ℕ | Only pointwise values are used. Finite support of k is a representation restriction, unnecessary in raw finite-product form. |
| r : σ → ℕ | Arbitrary natural box bounds; no finite support or positivity hypothesis. |
| hk : ∀j,k j≤r j | Strictly stronger than necessary. The literal conclusion compiles under only `∀ j ∈ d.support, k j ≤ r j`; root's native weaker_global proof establishes this actual weakening. |
| ℕ, choose, base2 | Natural combinatorics is intrinsic to choose. A generic product-of-bounds theorem can abstract the final order/product step, but cannot replace binomial entries by arbitrary ordered scalars without hypotheses. |
| R / CommSemiring R | Absent from elaborated type, hence nothing to weaken. No characteristic-zero, Nontrivial, Nonempty, DecidableEq parameter is present. |

Verified forms:
```lean
-- Same conclusion; weaker hypothesis:
∀ j ∈ d.support, k j ≤ r j
-- Arbitrary σ; stronger support-sensitive conclusion:
hasseCoeff d k ≤ 2 ^ (∑ j ∈ d.support, r j)
```

The support bound is a real strengthening, while finite-set ordinary-function form exposes the combinatorial API. The global theorem is STRICTLY NARROWER by its hk hypothesis; the verified weakening is not a conjectural generalise-first claim. An upstream YES would first decide the scalar representation and ship the support-local/general finite-set form. This mathematical fact alone does not force a YES verdict for the project alias.

## Phase 4c — All nine modern idiom questions

| Q | Applies? | Reformulation and concrete downstream consequence |
|---|---|---|
| 1 Typeclasses | No | Fintype already packages global enumeration. A pointwise bound is data-dependent and should not become an instance. |
| 2 Filters/topology | No | Finite natural inequality has no convergence or metric hypothesis. |
| 3 Universal property | No | No object construction is characterized here; product monotonicity is existing API. |
| 4 Bundled substructures | No | No closure predicate/subobject occurs. A finite support is already a Finset. |
| 5 Hierarchy | No | No field/vector-space restriction to weaken. The result is scalar ℕ combinatorics. |
| 6 Higher categories | No | No categorical construction or coherence issue. |
| 7 Concrete indices | Partly | σ already arbitrary. Removing Fintype requires changing global sum to finite-set/support sum; native support_bound verifies it and enables infinitely many ambient variables. ℕ binomial indices remain intrinsic. |
| 8 Concrete-via-abstract | Yes | After expanding hasseCoeff, no polynomial operation appears. The proof uses only finite products of natural binomial factors and pointwise bounds; ordinary-function finite-set form serves other combinatorial products and both coefficient-norm consumers without a Hasse scalar alias. |
| 9 False-generalisation guard | No false generalization accepted | Support sum and support-local hk preserve and strengthen the same binomial factor. Replacing2 by arbitrary base without a lower bound is false: on a singleton S, r(*)=1 and d(*)=k(*)=0 give1≤0^1 false. This is a direct mathematical illustration, not a claimed native guard witness. Replacing natural choose by field/semiring values without an order-compatible bound changes content. |

Q8 diagnostic: the identifier hasseCoeff occurs in the statement/full-product rewrite; after that first rewrite, the proof tail uses none of hasseCoeff, hasseDeriv, polynomial coefficients or the coefficient semiring. It still uses the binomial bound, so a generic order theorem alone is not the exact target. This is an actual proof abstraction with a concrete finite-set consumer, not categorical ornamentation. [Q8 evidence](../evidence/MvPolynomial.hasseCoeff_le_two_pow/q8-diagnostic.json).

## Phase 4.5 — Six infrastructure risks

Theorem n/a in all six rows: no new definitional equality/reducibility boundary; no inheritance diamond; no coercion diamond; no typeclass instance or instance-search cost; no new computability/choice interface; no new overlapping computational or simplifier definition. The existing scalar alias's earlier assessment remains separate. This theorem is not tagged simp. Naming/public-API choices still matter, but are not definition infrastructure hazards.

## Phase 4.6 — All five proof strategy questions

| Row | Applies? | Finding |
|---|---|---|
| 1 ε-δ versus filters | No | No topology. |
| 2 Elements versus subobjects | No | Coordinatewise inequalities and finite products are the appropriate abstraction; ideals/submodules do not help. |
| 3 Sequences versus nets | No | No limits. |
| 4 Construction versus universal property | No | No categorical object constructed. |
| 5 Missing helper that should exist | Design question | A general Finset/Nat product-choose bound may be useful, but is not an already available replacement. Existing prod_le_prod, choose bound, power monotonicity and power-sum normalization already prove it. |

Current strategy MATHLIB-IDIOMATIC: no induction on polynomials or characteristic-zero factorial division. Optional refactor: prove raw finite-set combinatorial bound first, then specialize support/global forms. That changes API organization, not a cost-based verdict.

## Phase 5 — All five actual methods on three forms

The independently executed forms are current Hasse scalar/global box, literature finite product of binomial coefficients, and abstract pointwise-power/product order bound.

| Method | Current | Literature | Abstract |
|---|---|---|---|
| A Lean-Finder | Natural choose/pow bounds and irrelevant multinomial inequality | Exact scalar choose_le_two_pow | prod_le_pow_card, pow_card_le_prod and submultiplicative relatives |
| B Loogle | choose_le_two_pow and choose_succ_le_two_pow | Nat.choose + Finset.prod gives identities/Lucas relatives, no target | Finset.prod + inequality to power gives uniform-cardinality bound and unrelated analysis |
| C LeanSearch | choose_le_two_pow; natural choose bounds | choose bound plus prod_le_pow_card | prod_le_pow_card/prod_le_one and norm-product relatives |
| D rg source | Full target name, alias/bound patterns | choose/product and relevant Finsupp/Choose directories | prod_le_prod, pow_le_pow_right, prod_pow_eq_pow_sum |
| E local symbol/name | Project target only | Pinned choose_le_two_pow | Pinned prod_le_prod and namespace distractors |

[Formal-search index and all raw receipts](../evidence/MvPolynomial.hasseCoeff_le_two_pow/formal-search.json), [untruncated exact CLI source/caller/inline receipts](../evidence/MvPolynomial.hasseCoeff_le_two_pow/source-search.json). Local index explicitly reports unavailable, even when source-name hits are returned; no negative inference is made from that index. An old evidence excerpt hit is not a mathlib declaration. External service indexes may use a different revision; positive building blocks are checked in the pinned native environment.

Positive candidates: Nat.choose_le_two_pow at Mathlib/Data/Nat/Choose/Bounds.lean:96; Finset.prod_le_prod at Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:111; Finset.prod_pow_eq_pow_sum at Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:656; Nat.pow_le_pow_right for exponent monotonicity. [Choose source](../evidence/MvPolynomial.hasseCoeff_le_two_pow/choose-excerpt.lean.txt), [product source](../evidence/MvPolynomial.hasseCoeff_le_two_pow/prod-excerpt.lean.txt), [power/product source](../evidence/MvPolynomial.hasseCoeff_le_two_pow/pow-product-excerpt.lean.txt). Finsupp.prod_fintype + Nat.choose_zero_right perform alias expansion to full product. Uniform prod_le_pow_card is not exact: r varies with j, so a uniform exponent/cardinality bound loses information. Multinomial factorial ratios are different quantities. No exact named target replacement is claimed; the conclusion is positive compositional evidence plus an API choice, not proof of absolute absence.

## Phase 5.5 — Three statement-shape checks

**Normal form:** natural inequality is the strongest convenient pre-cast form. Pointwise product bound and power-of-sum bound are mathematically equivalent after Finset.prod_pow_eq_pow_sum, but that equality needs a theorem, not definitional equality. No nontrivial implication is hidden by equality reversal. Support-sum form is sharper.

**Syntactic generality:** implicit d,k,r inferred from goal are convenient in both consumers; explicit S and ordinary d,k,r is natural for a general combinatorial theorem. Pointwise order notation k≤r requires coercion/ordinary-function packaging, with no mathematical gain over ∀j. Literal weakened hk and support form were compiled.

**Superfluous arguments:** no unused R, ring, positivity, nonempty or dominance d≤k parameter. Global Fintype is tied to the RHS, while upper k's finite support is unused mathematically. Overall RESTATE-BEFORE-SHIP if upstream: prefer support-local hk and explicitly decide finite-set versus scalar alias interface.

## Phase 6.0 — Every explicit caller and inline audit

| Caller | Declaration/invocation | Purpose and migration |
|---|---|---|
| Roth.abs_coeff_hasseDeriv_le | CoeffNorm.lean:133 / invocation140 | For supported e+d, combine monomial_le_degreeOf and hP into hk, cast natural bound to ℝ with exact_mod_cast. |
| Roth.normOne_hasseDeriv_le | CoeffNorm.lean:147 / invocation157 | Same natural bound for each supported monomial k, cast to ℝ before multiplying absolute coefficient. |

Two explicit invocations in two declarations, one external file; internal-use count excluding declaring file is2. Both qualified/unqualified source forms and potential inline choose/power derivations were searched across production sources. No duplicate inline re-derivation of the target was found. Power-product rewrites in GenWronskian/MainLemma and diagonal substitution are related normalizations, not extra callers. This is explicit source scope, not opaque kernel/simp closure. [Caller excerpt](../evidence/MvPolynomial.hasseCoeff_le_two_pow/caller-excerpt.lean.txt), [search receipts](../evidence/MvPolynomial.hasseCoeff_le_two_pow/source-search.json). Two consumers show utility; they do not automatically establish upstream necessity.

## Phase 6 — Actual composition experiments

Attempt1: source replay succeeds natively using the existing project full-product helper, followed by:
```lean
rw [← Finset.prod_pow_eq_pow_sum]
exact Finset.prod_le_prod fun j _ ↦
  (Nat.choose_le_two_pow _ _).trans (Nat.pow_le_pow_right two_pos (hk j))
```
This has three bound-producing calls plus the nondefinitional product/power normalization; the project full-product bridge is additional. It is not a demonstrated ≤3-call exact replacement.

Attempt2: remove project helper entirely and state the raw finite-product inequality with ordinary functions. Native mathlib-only verification tests precisely the finite combinatorial content, guarding target absence with check_failure. A separate native target-import check verifies the real-cast consumer pattern. This proves that no Hasse operator identity is needed. It does not make the new raw finite-product helper into an existing library theorem.

Attempt3: support-sensitive estimate succeeds without global Fintype and with hk only on d.support. The same original conclusion under weaker hk succeeds by support bound, power monotonicity and Finset.sum_le_sum_of_subset. The global/source and support versions all have standard axioms.

Strict Phase6a result: **NOT-COMPOSABLE within the demonstrated ≤3-call criterion**; elementary four-building-block proof exists. Parent scalar/product helpers cannot count as mathlib calls. This does not by itself force YES: the theorem packages a project scalar alias and the best upstream combinatorial statement is an API-design choice. No claim rests on failed exact? automation, a timeout, an unavailable local index, or untested absence. [Exact accepted sources, raw complete receipts and axioms](../evidence/MvPolynomial.hasseCoeff_le_two_pow/verification.json).

## Phase 7 — Actionable verdict and API questions

**BORDERLINE-needs-human.** The useful mathematical bound is standard finite combinatorics and both current consumers have the expected cast-compatible instantiation. The literal hypothesis can be weakened, but a standalone MvPolynomial lemma about an alias previously assessed NO-composable is not automatically an upstream gap. Conversely, the four-call normalization proof does not meet the strict NO-composable threshold, and utility at two consumers supports retaining a named local interface. There is no cost-based downgrade.

Concrete future upstream questions:

1. Should mathlib expose a generic Nat/Finset theorem bounding products of binomial coefficients by a power of2, or leave the four-building-block proof to downstream users?
2. If exposed, should the primary theorem use an arbitrary finite set and ordinary functions, with support/global Hasse wrappers derived locally?
3. If a Hasse-facing public estimate is also wanted, should it use the sharper support-sum exponent and only support-local hk?

Recommended immediate action: retain the theorem locally in Roth/HasseDeriv.lean pending that design choice; no production deletion is proposed by this assessment. The literal hk weakening is verified and suitable for a later authorized generalise/cleanup pass. Alternative local destination if separating operator algebra from scalar combinatorics: a project-local binomial-factor helper near coefficient estimates in Roth/CoeffNorm.lean. It is not junk/dead code.

If the wrapper is omitted in a future refactor, migrate **both** callers: replace the exact_mod_cast invocation at CoeffNorm140 and157 by the expanded full product proof with Finsupp.prod_fintype, Nat.choose_zero_right, Finset.prod_pow_eq_pow_sum, Finset.prod_le_prod, Nat.choose_le_two_pow and Nat.pow_le_pow_right; preserve each existing monomial_le_degreeOf/hP bound. The verified raw finite-product/cast witness is the reviewable template. Do not replace the wrapper with a call to a newly invented helper and call that existing mathlib. If a generic finite-product theorem is first added upstream, invoke it with S=univ, k=e+d at140 and k=k at157, respectively. Rebuild both consumers/project after the eventual authorized change.

YES-specific upstream path, PR title and reviewer selection are n/a to the selected BORDERLINE verdict. Already accepted YES declarations in progress belong to the operator/coefficient API and do not imply acceptance of this scalar-bound wrapper. Phase7 gate: all literature/formal methods, all parameter/modern/strategy/risk/shape rows, both explicit callers and inline audit, real native witnesses, and three concrete design questions are present.

## Phase 8 — Completion evidence

[Assessment](../evidence/MvPolynomial.hasseCoeff_le_two_pow/assessment.json), [overview entry](../evidence/MvPolynomial.hasseCoeff_le_two_pow/overview-entry.json), [verification](../evidence/MvPolynomial.hasseCoeff_le_two_pow/verification.json), [current copy manifest](../evidence/MvPolynomial.hasseCoeff_le_two_pow/copy-manifest.json), [portable read-only validator](../evidence/MvPolynomial.hasseCoeff_le_two_pow/validate.py). Completion is frozen after actual native receipts and manifest/link validation; root independently accepts and integrates it. Questions concern future API design, not unresolved verification or permission to continue the repository assessment.
