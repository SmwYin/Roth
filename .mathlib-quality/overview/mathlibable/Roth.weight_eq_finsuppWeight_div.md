# Roth.weight_eq_finsuppWeight_div — full assessment

**Verdict: NO-mathlib-has-it**, by the independently checked parent re-aim to linear-map naturality of `Finsupp.weight` / `Finsupp.linearCombination`. The common-denominator arithmetic is a genuine representation bridge; this is not a claim that the old statement has a three-call proof or is definitionally equal to the generic law.

## Phase 0 — baseline and identity

Canonical declaration 142 is the public theorem at Roth/Index.lean:130. The entire declaring module and its sole caller were read; [Index source](../evidence/Roth.weight_eq_finsuppWeight_div/Index.lean.txt), [Box parent](../evidence/Roth.weight_eq_finsuppWeight_div/Box.lean.txt), [metadata](../evidence/Roth.weight_eq_finsuppWeight_div/canonical-target.json). The successful 2467-job build is reused after freshly matching all 17 production/pin hashes: [baseline](../evidence/Roth.weight_eq_finsuppWeight_div/baseline-build.txt), [inputs](../evidence/Roth.weight_eq_finsuppWeight_div/inputs.json). No production/pins/Git/progress edits were made. No prefilter or glue inheritance applies.

The complete native original type/body/axioms and canonical293 audit are archived in [verification](../evidence/Roth.weight_eq_finsuppWeight_div/verification.json). Standard axioms only, no sorry, unsafe, native_decide or raised limits. Required audit info is scoped to the new region; earlier info is not counted as fresh evidence.

## Phase 1 — comprehend

Let r be a positive natural parameter at every coordinate of a finite variable type, and d a finitely supported natural multi-index. Put D=∏ᵢrᵢ. Then the real rational weight ∑ⱼdⱼ/rⱼ equals the natural monomial weight with generator weights D/rⱼ, cast into ℝ and divided by D. Divisibility rⱼ∣D makes natural division exact; positivity ensures D≠0, so the final cancellation is valid.

Full elaborated type:
```lean
@Roth.weight_eq_finsuppWeight_div : ∀ {σ : Type u} [Fintype σ] {r : σ → ℕ},
  (∀ j, 0 < r j) → (d : σ →₀ ℕ) →
  Roth.weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ↑(∏ i, r i)
```

σ is universe-polymorphic; Fintype enumerates the product and old full sum. r is essential denominator data, hr supplies nonzero product, d is the exponent vector, and ℝ is the original target. No DecidableEq binder survives. The sole project dependency in the target's statement/body is Roth.weight. Proof expands both weights, commutes casts with sums/products and exact natural division, then cancels the nonzero common denominator coordinatewise.

## Phase 2 — preliminary

SMALL: arithmetic implementation bridge, no new structure, not a named-person theorem or module main result. One-line definition-only test: n/a, theorem. Literature width remains exhaustive.

## Phase 3 — exhaustive literature

Only exact requests, response hashes/bytes/status, titles/URLs/locators and original summaries are retained. Returned URL query parameters, including signed-download credentials, were removed; no credential values are retained.

| Channel | Actual request and result |
|---|---|
| General specific | [web0](../evidence/Roth.weight_eq_finsuppWeight_div/web0-metadata.json): Roth index polynomial clear denominators product r weights D r_j. Roth ICM1958 p206 defines derivative order by reciprocal parameters; AMS and expository Roth accounts found. |
| General standard | [web1](../evidence/Roth.weight_eq_finsuppWeight_div/web1-metadata.json): rational weighted degree common denominator integral weights monomial. Weighted monomial degrees and integer weight representations; no exact new law inferred from partial matches. |
| General abstract/aliases | [web2](../evidence/Roth.weight_eq_finsuppWeight_div/web2-metadata.json): linear combination scalar multiplication clearing rational denominators weighted sum. Author-written linear algebra texts give scalar linearity of combinations. |
| ChatGPT mathematics | n/a: ask_chatgpt_math unavailable; no simulated answer. |
| Local clean.tex | [exact excerpt](../evidence/Roth.weight_eq_finsuppWeight_div/clean-excerpt.tex.txt), §4 lines530–558. Positive real parameters define index; the Lean note explicitly prescribes D=∏r and natural weights D/r only for positive integral parameters. |
| nLab | [web3](../evidence/Roth.weight_eq_finsuppWeight_div/web3-metadata.json): site:ncatlab.org/nlab free module linear combination. Free-module extension and finite linear combinations. Primary free-module page open failed HTTP400 unsupported XHTML; indexed results accessible. |
| nCatLab distinct namespace | [web4](../evidence/Roth.weight_eq_finsuppWeight_div/web4-metadata.json): site:ncatlab.org/ncatlab rational weights graded algebra. Returned /nlab and /schreiber results, outside requested namespace; no exact nCatLab hit. This is an honest attempted channel, not evidence of absence. |
| Stacks | [web5](../evidence/Roth.weight_eq_finsuppWeight_div/web5-metadata.json): site:stacks.math.columbia.edu weighted graded algebra degree. Opened [00JL §10.56](https://stacks.math.columbia.edu/tag/00JL), especially Lemma10.56.2, where monomial degree is exponent-weight sum and lcm provides divisible degree. Adjacent structural context, not the precise reciprocal identity. |
| MathOverflow | [web6](../evidence/Roth.weight_eq_finsuppWeight_div/web6-metadata.json): site:mathoverflow.net rational weights weighted degree denominator. Question143522 discusses common denominators for rational weights; no exact library theorem inferred. |
| Recent arXiv, last five years | [web7](../evidence/Roth.weight_eq_finsuppWeight_div/web7-metadata.json): dated2022–2026 Roth weighted index search found [Salami2610.17589v1](https://arxiv.org/html/2610.17589v1#S8), submitted2026-10-13, within2021-10-27–2026-10-27. Primary §8 inspected; its counterexample concerns floor-based degree-box dimension rescaling, not exact scalar linearity when denominators divide. Unrelated statistical Roth/weight results rejected. |

[Primary opens and access limitations](../evidence/Roth.weight_eq_finsuppWeight_div/web8-metadata.json), [recent primary initial inspection](../evidence/Roth.weight_eq_finsuppWeight_div/web9-metadata.json), [exact §8 lines656–675 inspection](../evidence/Roth.weight_eq_finsuppWeight_div/web10-metadata.json). Supplementary primary locator: [Roth ICM1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf). No article bodies persisted.

Synthesis: the standard concept is clearing rational monomial-weight denominators, an instance of linearity of a finitely supported linear combination. Literature allows arbitrary positive real reciprocal parameters, but a natural common-denominator presentation requires rational/integral data; arbitrary irrational weights cannot be silently discretized. The useful abstract law is naturality under linear maps. No historical-novelty claim is made.

## Phase 4a — every parameter and generality

| Parameter | Current | General form / result |
|---|---|---|
| σ : Type u | Arbitrary universe | Already polymorphic. General linear-map law and support-local denominator version require no finite ambient σ. |
| Fintype σ | Product over every coordinate | Essential to unchanged full-product spelling; arbitrary σ works with an independently supplied D, nonzero cast D, and divisibility only on d.support. This is a representation extension, not deleting a binder from an ill-typed old definition. |
| r : σ → ℕ | Positive integral denominators | Natural quotients are exact only with divisibility. General support-local form assumes rⱼ∣D on active coordinates and a nonzero cast D. General scalar law permits arbitrary assigned target weights. |
| hr : ∀j,0<rj | Global positivity | For naturals equivalent to coordinatewise nonzero, which makes D nonzero. Support-local D formulation needs (D:K)≠0 and active-coordinate divisibility instead. Merely requiring active r positive while retaining full D fails if an inactive coordinate is zero. |
| d : σ →₀ ℕ | Natural monomial exponents | Appropriate exponent semantics. Generic linearCombination allows semiring-valued coefficients, independently verified; this is linear algebra, not a claim that polynomial exponents may become arbitrary signed coefficients. |
| ℝ | Ordered complete field | Proof is algebraic; accepted Semifield K with nonzero cast common denominator suffices. CharZero is sufficient to obtain that from nonzero natural D, but is unnecessary in the strongest checked form. No order, subtraction, topology or completeness needed; in positive characteristic natural nonzero D alone does not imply nonzero cast D. |
| D fixed as product | Convenient common multiple | Any natural D whose cast is nonzero and that is divisible by each active denominator suffices, including an lcm or support product. Verified support-local form. |

## Phase 4b — exact schema and verified weakenings

Current representation is STRICTLY NARROWER than the accepted abstract existing law, and broader denominator arithmetic is verified separately. This supports reusing existing API, not a novel-generalization claim.

```lean
-- Existing generic law, unchanged arbitrary ambient index:
(f : M →ₗ[R] N) (w : σ → M) (d : σ →₀ R) :
  f (Finsupp.weight w d) = Finsupp.weight (f ∘ w) d
-- = Finsupp.apply_linearCombination R f w d

-- Actual denominator representation extension:
[Semifield K]
(r : σ → ℕ) (d : σ →₀ ℕ) (D : ℕ) (hD : (D : K) ≠ 0)
(hdiv : ∀ j ∈ d.support, r j ∣ D) :
  Finsupp.weight (fun j ↦ (r j : K)⁻¹) d =
    (Finsupp.weight (fun j ↦ D / r j) d : K) / D
```

The exact accepted Lean sources and complete native receipts are indexed in verification.json. A newly proved supportClear is representation glue, never counted as a preexisting mathlib theorem. The strongest supportClear drops CharZero: divisibility plus (D:K)≠0 implies every active cast denominator is nonzero, allowing Nat.cast_div. The fixed old parent interface still needs Fintype and returns ℝ. Global nonzero weights under Fintype are a literal weakening of hr syntax only because positive naturals and nonzero naturals are equivalent.

## Phase 4c — nine modern-idiom checks

| # | Diagnostic | Finding and concrete downstream consequence |
|---|---|---|
| 1 | Typeclasses | Yes: Semifield with nonzero cast denominator for arithmetic, Semiring/Module for generic law. Removes unnecessary real order/completeness. |
| 2 | Filters/topology | No: finite algebraic equality, no convergence. |
| 3 | Universal property | Yes: free-module linearCombination; apply_linearCombination transports assigned generators through a linear map. Cast and scaling become exact specializations. |
| 4 | Bundled substructures | No set-with-closure predicate. Bundled linear maps are relevant, enabling composition and natural scalar restriction. |
| 5 | Hierarchy | Yes: Semifield instead of ℝ/field; generic module law is already upstream. |
| 6 | Higher categories | No: ordinary module naturality fully describes this scalar computation; no higher coherence needed. |
| 7 | Concrete index/codomain | Yes: arbitrary σ via support-local D; arbitrary semifield K for arithmetic. No global Fintype needed in naturality. |
| 8 | Concrete-via-abstract | Yes: after weight unfolding the body never uses real-specific operations beyond cast/division/nonzero cancellation. Identifier audit finds Roth.weight only in the initial unfolding; real positivity is used solely for D≠0. Accepted proofs replace that with algebraic nonzero product and the existing generic map law. |
| 9 | False-generalization guard | Reject dropped nonzero-D guard, mixed-zero full products, nondivisible natural quotients and irrational-weight discretization. Bool mixed-zero example has LHS1 RHS0; d=0 and all-zero/single-coordinate cases may still satisfy the equality. Thus positivity is sufficient and globally necessary for a uniform all-d statement on mixed coordinates, not logically necessary in every individual case. |

Modern idiom available, already in mathlib. Actual consequence: cast the natural weighted sum by a bundled ℕ-linear map, then scale all assigned generator values by D⁻¹ using the same law; compare the resulting generator functions. This composes with arbitrary linear target maps and supports infinite ambient index sets.

## Phase 4.5 — infrastructure risk

n/a: theorem. The six checks (typeclass diamonds, reducibility leak, noncanonical unfolding, priorities, universes, coercion ambiguity) introduce no definitions/instances here. Broader representation uses existing canonical ℕ-modules and DFunLike maps; no custom instances proposed.

## Phase 4.6 — proof strategy

| # | Check | Result |
|---|---|---|
| 1 | Topology ε–δ/filter | n/a, no topology. |
| 2 | Algebra elements/bundled inclusions | Bundled linear-map naturality is useful; no ideal/submodule inclusion problem. |
| 3 | Analysis sequences/nets | n/a, no limits. |
| 4 | Construction/universal property | Yes: existing free-module extension transports cast/scaling without coordinate sum manipulations. |
| 5 | Missing helpers mathlib should have | No missing generic cast/scaling law: apply_linearCombination supplies both. A convenience denominator-clearing spelling is proved as local glue, not asserted absent from all generated API. |

REFACTOR-RECOMMENDED toward generic naturality plus an explicit denominator certificate. Arithmetic remains necessary to identify assigned generators. No cost-based verdict is used.

## Phase 5 — actual five methods × three forms

Every service was actually invoked, all raw requests/results retained as search-{form}-{method}.json; rg receipts contain exact commands and untruncated output. External index revisions can differ; pinned source and native positive checks determine usability. Local index=unavailable is source fallback presence evidence, never proof of absence.

| Method | Current common denominator | Literature weighted degree | Abstract module naturality |
|---|---|---|---|
| Finder | Finsupp.weight/weight_apply, partial | weighted homogeneous degree laws, adjacent | apply_linearCombination and map_finsupp_linearCombination, exact generic hit |
| Loogle | Finsupp.weight family | Nat.cast_div_charZero exact division cast | Finsupp.apply_linearCombination exact signature |
| LeanSearch | weight, weight_apply; localization common-denominator adjacent | isWeightedHomogeneous_monomial and weightedTotalDegree, related but not denominator bridge | apply_linearCombination and alias exact generic hit |
| rg pinned | exact cast arithmetic/weight expansion | weight_eq_sum, weighted homogeneous monomial | linearCombination_linear_comp, apply_linearCombination, alias |
| Local | Finsupp.weight and project target | cast_div_charZero | apply_linearCombination; index unavailable fallback |

Pinned positive candidate: `Finsupp.apply_linearCombination`, Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:93 (alias `LinearMap.map_finsupp_linearCombination`:452), [source](../evidence/Roth.weight_eq_finsuppWeight_div/LinearCombination.lean.txt). `Finsupp.weight` is its AddMonoidHom view, Mathlib/Data/Finsupp/Weight.lean:82; [source](../evidence/Roth.weight_eq_finsuppWeight_div/Weight.lean.txt). `Nat.cast_div_charZero`, Mathlib/Data/Nat/Cast/Field.lean, requires divisibility and CharZero; [source](../evidence/Roth.weight_eq_finsuppWeight_div/Field.lean.txt).

Conclusion: found the analogous generic cast/scaling law for the re-aimed parent in mathlib, independently verified. No claim of an existing theorem named Roth.weight_eq_finsuppWeight_div or of search-proved absence of its arithmetic spelling.

## Phase 5.5 — statement shape

1. Normal forms: old full-sum reciprocal weight; support-based Finsupp.weight; cast/scaled natural Finsupp.weight; linear-map image of linearCombination. Canonical generic operation is Finsupp.weight/linearCombination. Original RHS is sensible for its weightedOrder consumer; choose one project bridge into the generic object, avoiding a network of wrapper equivalences.
2. Syntactic generality: global product D is easy for the sole caller, while support-local arbitrary D is more reusable and needs weaker ambient finiteness. Both forms were actually compiled. Reuse the abstract map law for upstream API.
3. Superfluous arguments: r and d change values; hr enables uniform D cancellation; Fintype needed by old full product/weight syntax. No unused DecidableEq. Order/completeness and ℝ are removable only in expanded representation, verified with semifield. None can be silently erased from unchanged parent spelling.

Overall RESTATE-BEFORE-SHIP if proposing any upstream statement: use existing generic naturality. Project-local denominator bridge may remain with its direct rewrite orientation for weightedOrder.

## Phase 6.0 — complete callers and inline audit

One distinct explicit caller declaration, `Roth.index_eq_weightedOrder_div`, Roth/Index.lean:143, with two proof-body applications at152 and155. Zero statement applications; zero callers outside declaring module. [Caller fragment and full per-use plan](../evidence/Roth.weight_eq_finsuppWeight_div/callers.json), [two complete searches](../evidence/Roth.weight_eq_finsuppWeight_div/complete-caller-search.json), [canonical-inventory lexical enumeration](../evidence/Roth.weight_eq_finsuppWeight_div/lexical-enumeration.json). Direct kernel consumer is the same sole declaration, separately audited; these are distinct notions of dependency.

| Use | Refactor |
|---|---|
| Index152, reverse rewrite | After hdw and ENat.toNat_natCast, rewrite the cast/scaled natural weight backwards using the checked original-parent representation bridge; finish index_le_weight as before. |
| Index155, forward rewrite | Replace reciprocal weight by cast/scaled natural weight, preserve existing div_le_div_of_nonneg_right and weightedOrder_le argument. |

Inline audit [receipt](../evidence/Roth.weight_eq_finsuppWeight_div/rg-inline.json): product/natural weights recur in the same weightedOrder bridge and index_mul's finiteness witness. No independent denominator-clearing derivation bypasses this helper. It is active local API; no dead-code claim.

## Phase 6 — actual composition and guards

The generic re-aimed law is one existing call:
```lean
example (f : M →ₗ[R] N) (w : σ → M) (d : σ →₀ R) :
    f (Finsupp.weight w d) = Finsupp.weight (f ∘ w) d :=
  Finsupp.apply_linearCombination R f w d
```
It specializes to natural casting via `(Nat.castAddMonoidHom K).toNatLinearMap` and to generator scaling via `DistribSMul.toLinearMap ℕ K c`. These are independently checked mathlib-only, with a #check_failure guard excluding the project target. The denominator bridge then proves the generator identity using rⱼ∣D, Nat.cast_div and (D:K)≠0 cancellation. CharZero with natural D≠0 is an independently compiled sufficient specialization. The support-local version verifies finite support is enough; the actual old-parent bridge and entire sole-caller replay verify that the representation change works in project context.

Old-form direct composition conclusion: NOT-COMPOSABLE in ≤3 existing calls. It needs weight_eq_sum/weight_apply, casts of sums/products/division, distribution, divisibility, reassociation and nonzero cancellation. A closing simp [definitions] alone would be Phase6b BORDERLINE evidence, not NO-composable. Neither a newly named bridge nor a project theorem is counted as an existing primitive. The decisive NO route is Mode B's explicit parent re-aim rule: the generic assigned-generator map law already exists, and its exact arithmetic representation bridge was independently proved. Normalization complexity does not erase that positive generic hit.

Mixed-zero guard: for Bool denominators r(true)=1, r(false)=0 and d=single true1, the real reciprocal weight is1, while D=0 makes normalized natural weight0. Therefore dropping positivity/nonzero-D from the full-product identity is false. Zero d is a valid exception; empty σ has D=1 and d=0. All-zero denominators yield zero weight and RHS0; one-variable zero denominator also gives0. These exceptions prohibit overstating pointwise necessity. Support-local D permits inactive zero denominators because divisibility is checked only on support.

## Phase 7 — verdict and action

**NO-mathlib-has-it**, via `Finsupp.apply_linearCombination` and the independently verified natural-cast/scaling specializations. The parent Roth.weight is the reciprocal-real specialization of Finsupp.weight; prior parent reports were read as context, while the analogous generic law and denominator-clearing bridge were established afresh. This applies Mode B's re-aim gate, not blanket inheritance.

Retain a documented implementation bridge in **Roth/Index.lean** if desired. If eliminating the local theorem, refactor the sole caller's two rewrites using the checked replacement in the table, after migrating its reciprocal weight representation; preserve hr, hP and all weighted-order finite-value guards. The exact full-caller replay demonstrates both uses, without invoking the target theorem. Do not replace the old theorem by a nonexistent one-line denominator lemma or count the new bridge as upstream API.

Alternative destination: the existing project Index module, where the arithmetic choice D=∏r implements a particular weightedOrder representation. No Archive/satellite contribution is appropriate. No upstream PR proposed; YES-only proposed file/title/group/reviewer/cleanup/generalise steps are n/a. No unresolved verification; root independent acceptance pending.

## Phase 8 — package

[Assessment](../evidence/Roth.weight_eq_finsuppWeight_div/assessment.json), [verification](../evidence/Roth.weight_eq_finsuppWeight_div/verification.json), [overview entry](../evidence/Roth.weight_eq_finsuppWeight_div/overview-entry.json), [current manifest](../evidence/Roth.weight_eq_finsuppWeight_div/copy-manifest.json), [portable validator](../evidence/Roth.weight_eq_finsuppWeight_div/validate.py). All required phases and all named literature/formal-search channels are complete. Current manifest is authoritative; historical worker manifests and integration root-review/root-acceptance are excluded from recursive coverage. Production/pin hashes, exact canonical order293, native successes/standard axioms, actual callers, links and credential guard are checked before freeze.
