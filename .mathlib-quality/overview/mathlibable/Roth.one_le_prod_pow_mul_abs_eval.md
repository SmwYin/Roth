# `Roth.one_le_prod_pow_mul_abs_eval` — YES-but-generalise-first

Canonical279, `Roth/Main.lean:324–344`. Fresh independent assessment; root acceptance pending.

## Phase0 — Baseline and scope

The unchanged 2467-job baseline build succeeded. All17 source/pin hashes freshly match the tracked shared manifest ([inputs.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/inputs.json), [baseline-build.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/baseline-build.txt)). Full Main588lines and LeanEval66lines were read; all production Lean sources were freshly searched using no-ignore rg and git grep. No production, pins, Git, overview or progress were modified by this worker.

Root exclusively executed native and local LSP requests. Original proof replay uses exactly the target, renamed `Integer279Original.replay`, in a fresh namespace and no private helper closure. Its complete source and original/replay proposition type agreement are checked. The loaded original full type and direct kernel value/type constants were audited; the pp.all body printer explicitly elides89281characters, so this is not claimed as a complete printed kernel body. The complete written proof is archived. Canonical array came directly from tracked order, all293 unique names in exact order including correct private modules; runtime293present/293values. One direct body consumer, no direct type consumer. See [original-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/original-executed.lean.txt), [original-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/original-receipt.json), [canonical-consumers.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/canonical-consumers.json).

## Phase1 — Mathematics and full native type

For an integer polynomial Q in finitely many coordinates with each coordinate degree at most rⱼ, evaluate at integer numerator hⱼ divided by positive natural denominator qⱼ. If this value is nonzero, multiplying its absolute value by ∏qⱼ^rⱼ yields at least1. This is an exact denominator estimate; no reduced fractions or algebraicity assumptions enter.

```lean
∀ {m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ},
  (∀ (j : Fin m), degreeOf j Q ≤ r j) →
    ∀ (h : Fin m → ℤ) {q : Fin m → ℕ},
      (∀ (j : Fin m), 0 < q j) →
        (eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) ((map (Int.castRingHom ℝ)) Q) ≠ 0 →
          1 ≤ (∏ j : Fin m, ↑(q j) ^ r j) * |(eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) ((map (Int.castRingHom ℝ)) Q)|
```

The proof constructs N=Σ_d coeff(Q,d)·∏ⱼ hⱼ^dⱼ qⱼ^(rⱼ−dⱼ). For each support monomial, `monomial_le_degreeOf` and hQ justify dⱼ≤rⱼ; denominator cancellation identifies N's real cast with the product-scaled evaluation. Positivity makes the denominator product nonzero, hne makes N nonzero, and `Int.one_le_abs` supplies the discrete lower bound. This is neither integrality alone nor positivity alone. Project proof dependencies: `[]`; all ingredients are mathlib constants. [target-excerpt.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/target-excerpt.lean.txt).

## Phase2 — Preliminary checks

SMALL: a finite arithmetic helper, no new structure or named theorem; module main-results list names Roth's theorems. Literature still exhaustive. Definition-only one-line check: n/a, theorem. Six infrastructure risks: n/a, theorem introduces no definition, instance, coercion, reducibility or unfolding path; each recorded in [phase-checks.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/phase-checks.json).

## Phase3 — Exhaustive literature

| Channel | Exact query / evidence | Result and relevance |
|---|---|---|
| Specific web | `integer multivariate polynomial rational evaluation product denominators lower bound`; [web-batch0.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch0.json) | Elementary Liouville/height and denominator-clearing context; not an exact formal-library replacement. |
| General web | `clearing denominators multivariable polynomial integer nonzero value Liouville inequality`; [web-batch0.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch0.json) | Elementary Liouville/height and denominator-clearing context; not an exact formal-library replacement. |
| Aliases web | `Liouville inequality polynomial rational points multidegree product heights`; [web-batch0.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch0.json) | Elementary Liouville/height and denominator-clearing context; not an exact formal-library replacement. |
| nLab | `site:ncatlab.org/nlab polynomial rational points height Liouville`; [web-batch3.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch3.json) | Localization/height context or adjacent results; no exact coordinatewise theorem identified. |
| nCatLab distinct namespace | `site:ncatlab.org/ncatlab polynomial localization denominator clearing`; [web-batch3.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch3.json) | Localization/height context or adjacent results; no exact coordinatewise theorem identified. |
| Stacks | `site:stacks.math.columbia.edu polynomial localization denominators`; [web-batch3.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch3.json) | Localization/height context or adjacent results; no exact coordinatewise theorem identified. |
| MathOverflow | `site:mathoverflow.net multivariate polynomial rational points Liouville inequality`; [web-batch6.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch6.json) | Localization/height context or adjacent results; no exact coordinatewise theorem identified. |
| Recent arXiv | `site:arxiv.org Liouville inequality polynomial rational points height after:2021-10-29 before:2026-10-30`; [web-batch6.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/web-batch6.json) | Localization/height context or adjacent results; no exact coordinatewise theorem identified. |
| Local | `clean.tex` §7 eq54, lines1646–1656; [literature-local.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/literature-local.json), [local-excerpt.tex.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/local-excerpt.tex.txt) | Exact arithmetic step: coordinate degree bounds clear each denominator and yield a nonzero integer. |
| Optional math consultation | ask_chatgpt_math unavailable | justified n/a; no substitute channel invented. |

Primary external locator: Waldschmidt, *Linear independence of logarithms of algebraic numbers*, Introduction p.ii lines51–53 and Chapter3, identifies the elementary rational denominator lower bound as a Liouville estimate ([author's notes](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/LIL.pdf)). [Stacks10.9](https://stacks.math.columbia.edu/tag/00CM) supplies the localization universal property, which handles invertibility and fractions but not an archimedean separation constant. [primary.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/primary.json) records requests, responseSHA/bytes/status and concise original summaries. No article or search-result bodies persisted. Recent arXiv query used exactly the five-year window, including out-of-topic returns honestly. nCatLab was searched under `/ncatlab` distinctly; out-of-namespace results are not represented as exact nCatLab hits.

Standard mathematical content: clearing coordinate denominators followed by nonzero integer separation, a rational special case of Liouville estimates. Broader number-field/height versions need norm/product-formula machinery and are not mechanically the same theorem. Finite coordinate labels and a chosen ordered-field realization do not add arithmetic substance. These literature distinctions motivate the mechanical Fintype/ordered-field widening, not an unsupported claim that all normed fields have the integer bound.

## Phase4a–b — Every parameter and generality

| Parameter / hypothesis | Role and weakening result |
|---|---|
| m, Fin m | Finite coordinate labeling only. Arbitrary `Fintype ι` compiles with original proof; empty coordinates allowed. |
| Q over ℤ | Semantic integer separation, not merely convenient coefficients. Constant rational1/2 disproves unconditional rational coefficient extension. |
| r : coordinates→ℕ | Genuine reusable coordinate degree ceilings; no fixed Roth constants. They may be0. Dropping degree bounds fails on X² evaluated at1/2 with r=1. |
| h : coordinates→ℤ | Genuine numerator data; no sign or coprimality constraint. Arbitrary rational numerators would require additional denominator factors. |
| q natural, hq positive | Nonzero denominator is essential. Signed integers q≠0 compile with absolute product. q=0, Q=1,r=1 falsifies original conclusion. |
| hQ coordinate degree bound | Essential to nonnegative complement exponent r−d, validated by explicit counterexample when removed. |
| hne nonvanishing | Essential; Q=0 gives0 on the right. |
| real target | Only ordered-field cast/arithmetic/abs used; arbitrary linearly ordered field compiles mechanically. |
| no extra assumptions | No `NeZero m`, positivity of r, irrationality, algebraicity or coprimality needed or introduced. |

STRICTLY NARROWER THAN STANDARD; two mechanical widenings are actually verified in [generic01-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/generic01-receipt.json): replace Fin m by arbitrary Fintype and ℝ by arbitrary ordered field. No proof strategy change is needed for this primary weakening. Signed denominators also verify ([signed01-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/signed01-receipt.json)):

```lean
theorem signed {ι K : Type*} [Fintype ι] [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (Q : MvPolynomial (ι) ℤ) {r : ι → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : ι → ℤ) {q : ι → ℤ} (hq : ∀ j, q j ≠ 0)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ |∏ j, (q j : K) ^ r j| * |eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)|
```

The natural-positive convenience form uses the original body over arbitrary Fintype and ordered field. Exact original signature recovery is a single application of our newly proved generic theorem, compiled mathlib-only ([recovery-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/recovery-executed.lean.txt), [recovery01-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/recovery01-receipt.json)). This is new generic proof evidence, not a replacement already in mathlib. recovery01 has the exact written original signature in a mathlib-only module; it does not import or assert native original-versus-recovery proof equality.

Algebraic clearing alone compiles over arbitrary characteristic-zero field with signed nonzero denominators, without order. A separate norm estimate compiles only with explicit `hsep : ∀ z : ℤ, z ≠ 0 → 1 ≤ ‖(z : K)‖` ([clearing3-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/clearing3-executed.lean.txt), [clearing03-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/clearing03-receipt.json)). Characteristic zero alone does not imply hsep; p-adic fields provide the familiar obstruction (`Padic.norm_p_lt_one` in pinned PadicNumbers). No new separation typeclass is proposed. [edges-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/edges-executed.lean.txt) and [edges01-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/edges01-receipt.json) verify zero-denominator, zero-value, missing-degree, rational-coefficient guards and exact Fin0 specialization.

The algebraic layer generalizes further than characteristic-zero fields: arbitrary commutative semirings R and S, a ring homomorphism f:R→S, and supplied inverses biⱼ·f(bⱼ)=1 suffice. This is the direct multivariate analogue of existing DenomsClearable's semiring/inverse interface; eval₂ avoids the support-map injectivity premise entirely. No CharZero, injective map, no-zero-divisors, field or order assumptions are needed for this equality. The complete new proof and clean native verification are [generic-clearing-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/generic-clearing-executed.lean.txt) and [generic-clearing01-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/generic-clearing01-receipt.json). This is an independently proved missing helper, not an existing mathlib replacement. Its concrete effect is to reuse coordinatewise denominator clearing for maps into localizations and quotient semirings; the inverse equation is the required interface. Numeric separation remains an additional arithmetic property, supplied by integer coefficients and ordered-field absolute value in the primary estimate. The characteristic-zero field clearing03 is therefore a verified intermediate specialization, not claimed as the most general algebraic API.

```lean
theorem clearing_semiring {ι R S : Type*} [Fintype ι] [CommSemiring R] [CommSemiring S]
    (f : R →+* S) (Q : MvPolynomial ι R) {r : ι → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (a b : ι → R) (bi : ι → S)
    (hbi : ∀ j, bi j * f (b j) = 1) :
    ∃ N : R, f N = (∏ j, f (b j) ^ r j) * eval₂ f (fun j ↦ f (a j) * bi j) Q
```

## Phase4c — Modern idiom nine rows

| Question | Answer | Proposal / consequence |
|---|---|---|
| Typeclasses | yes | Replace fixed real realization by Field K, LinearOrder K, IsStrictOrderedRing K; verified generic01. Same integer estimate applies over ℚ and other ordered fields. |
| Filters/nets | no | Finite algebraic sum/product identity, no convergence. No topology introduced. |
| Universal property | partial | The new commutative-semiring/ring-hom/inverse proof supplies coordinatewise image membership without injectivity; localization explains its interface, but does not supply the degree bound or integer separation. |
| Bundled substructure | partial | Image/range membership or ∃N equality can express clearing; no bespoke class required. The verified clearing_semiring proof works without field, order, CharZero or injectivity. |
| Hierarchy weakening | yes | Real to linearly ordered field mechanically; field division and finite commutative products genuinely used. Univariate existing ordered-field API gives the correct hierarchy target. |
| Higher categories | no | No categorical coherence content. None. |
| Concrete index | yes | Fin m to arbitrary Fintype ι, including empty types. No coordinate-renaming/equivalence transport required by callers. |
| Concrete-via-abstract diagnostic | yes | Fin m occurs zero times in proof body; real annotations throughout serve only casts, field arithmetic and order. Integer coefficients remain semantic: Int.one_le_abs supplies discrete separation. Generic field proof and explicit hsep norm proof compile; not mere identifier-count speculation. |
| False-generalization guard | PASS | Signed denominators require absolute product; CharZero alone insufficient for norm separation; q=0 and missing hne/degree rejected by compiled counterexamples. Exact original signature recovered, including Fin0. |

Concrete-via-abstract diagnostic is explicit: `Fin m` occurs0times in original body; real annotations persist as casts/order arithmetic, while `Int.one_le_abs` is indispensable ([concrete-diagnostic.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/concrete-diagnostic.json)). Accepted mechanical proofs substantiate the abstraction. Real improvement: arbitrary finite coordinate types need no relabeling, ℚ and other ordered targets need no detour through ℝ, and the clearing equality can feed other separated norms if the required property is supplied. Exact original conclusion and empty dimension are retained.

## Phase4.6 — Proof strategy five rows

| Question | Answer | Assessment |
|---|---|---|
| Topology epsilon/delta | n/a | No topology |
| Point-free algebra | partial | Separate integer-image equality (clearing) from arithmetic lower bound; localization alone misses sharp exponent product. |
| Analysis sequences | n/a | No limits |
| Universal-property construction | n/a | Witness integer numerator is computational finite-sum identity, not a new object requiring category machinery. |
| Missing helpers | yes | Coordinatewise multivariate denominator-clearing equality is the concrete missing API; new clearing_semiring is our own proof over arbitrary commutative semirings, not an existing theorem. |

REFACTOR-RECOMMENDED before upstreaming: expose coordinatewise clearing as a helper and derive the integer lower bound afterward. Explicit support expansion is a natural finite polynomial argument. Avoid presenting a new norm abstraction as necessary for the primary ordered-field result. The actual missing helper and its complete new proof are archived; no cost-based verdict.

## Phase5 — All15 formal search cells

| Form | Finder | Loogle | LeanSearch | Pinned rg | Root local search |
|---|---|---|---|---|---|
| current | [formal-current-leanfinder.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-current-leanfinder.json) | [formal-current-loogle.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-current-loogle.json) | [formal-current-leansearch.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-current-leansearch.json) | [formal-current-rg.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-current-rg.json) | [formal-current-local.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-current-local.json) |
| standard | [formal-standard-leanfinder.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-standard-leanfinder.json) | [formal-standard-loogle.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-standard-loogle.json) | [formal-standard-leansearch.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-standard-leansearch.json) | [formal-standard-rg.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-standard-rg.json) | [formal-standard-local.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-standard-local.json) |
| abstract | [formal-abstract-leanfinder.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-abstract-leanfinder.json) | [formal-abstract-loogle.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-abstract-loogle.json) | [formal-abstract-leansearch.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-abstract-leansearch.json) | [formal-abstract-rg.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-abstract-rg.json) | [formal-abstract-local.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-abstract-local.json) |

Remote semantic queries find `one_le_pow_mul_abs_eval_div`, `denomsClearable_of_natDegree_le`, `denomsClearable_natDegree`; abstract form also finds `Int.one_le_abs`. Loogle current/standard return empty, abstract returns separation primitive. Pinned sources and native signatures were independently verified, not inferred from external index revisions. Root local current/standard had indexerror and abstract warming; a relevant standard exact-candidate retry is retained ([formal-standard-local-retry.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-standard-local-retry.json)). None of these index states proves absence. [formal-search-matrix.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-search-matrix.json) records every query and receipt.

The newly verified semiring/ring-hom/inverse modern form received a supplemental full five-method search, preserving the original15 cells: [formal-semiring-leanfinder.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-semiring-leanfinder.json), [formal-semiring-leansearch.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-semiring-leansearch.json), [formal-semiring-loogle.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-semiring-loogle.json), [formal-semiring-rg.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-semiring-rg.json), [formal-semiring-local.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/formal-semiring-local.json). Finder and LeanSearch again return the univariate DenomsClearable family and eval₂ APIs; Loogle is empty; pinned rg finds no multivariate clearing law in the searched modules. Local search reports indexerror with4 hits and supplies no absence evidence. The localization integer-normalization hits also concern univariate polynomials and clearing coefficient denominators, not this coordinatewise evaluation identity.

Concrete mathlib gap: `Mathlib/Algebra/Polynomial/DenomsClearable.lean:65–105` supplies only a univariate polynomial and one denominator with one natDegree; it cannot directly represent Q in independent coordinates with ∏qⱼ^rⱼ. `MvPolynomial.isLocalization` concerns localizing coefficient rings at a submonoid; it neither calculates the sharp coordinate denominator product nor supplies a unit lower bound for a nonzero integer. Evaluation expansion, support degree bounds and `Int.one_le_abs` are the existing primitives. Native candidate signatures: [composition03-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/composition03-receipt.json). Full pinned sources: [mathlib-source-0.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/mathlib-source-0.lean.txt), [mathlib-source-1.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/mathlib-source-1.lean.txt), [mathlib-source-2.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/mathlib-source-2.lean.txt).

## Phase5.5 — Statement shape three rows

| Check | Verdict | Concrete result |
|---|---|---|
| Normal form | RESTATE | eval₂ Int.castRingHom avoids map+eval transport; algebraic ∃N identity plus lower-bound corollary. Product-times-absolute form directly matches caller trans_lt; reciprocal form equivalent with positive denominator product. |
| Syntactic generality | RESTATE | Use arbitrary Fintype variables and ordered target field. signed q!=0 with absolute product, plus positive-natural convenience wrapper. shape02 verifies eval₂ bridge. |
| Superfluous arguments | NONE mathematically; representation restrictions | Q,r,h,q determine actual polynomial and points. hQ,hq,hne each needed by counterexamples; no NeZero m, coprimality, algebraicity, irrationality, or positivity of r assumed. Fin/Real restrictions can be widened. |

Overall RESTATE-BEFORE-SHIP. [shape2-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/shape2-executed.lean.txt) and [shape02-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/shape02-receipt.json) verify eval₂ normal form via eval_map. This bridge uses the new signed lemma and is not claimed as an existing arithmetic replacement. Product-times-absolute form fits the existing caller more directly than reciprocal or interval membership; signed absolute form preserves the mathematics. No superfluous proof premise was silently dropped.

## Phase6.0 — Full callers and duplication

| Actual caller | Use | Verification |
|---|---|---|
| private `Roth.one_lt_roth_eval_bound_aux`, Main453–478, call476 | Lower denominator bound chained by `.trans_lt` with the Taylor upper bound | Complete original body and signature retained; original target removed from fresh full Main replay and complete original proof literally inserted at call. |

One same-file call; zero external-to-file calls (the skill's count excluding declaring file is0). The module doc reference at38 and declaration at324 are not proof callers. Source lexical search and direct293 kernel consumer audit independently agree on the sole proof caller. No direct type consumers; no claim of a complete arbitrary simp/transitive closure. The target has no simp attribute. The downstream public chain reaches roth_of_isIntegral, roth, roth_rat and LeanEval.thueSiegelRoth; the latter is transitive, not an additional explicit target caller. [callers.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/callers.json), [source-search.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/source-search.json), [tracked-source-search.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/tracked-source-search.json).

Entire original Main namespace body was replayed with original local declarations, except target deletion and literal caller proof insertion; orphan target docstring removed as scratch-only cleanup. Existing public Roth definitions remain imported for project ingredients. This full caller experiment is stronger than a chopped caller prefix but does not claim replacing all transitive project ingredients with mathlib. Full sources [source-Main.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/source-Main.lean.txt), [source-LeanEval.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/source-LeanEval.lean.txt), accepted fullMain source [callers3-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/callers3-executed.lean.txt), raw [callers03-receipt.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/callers03-receipt.json).

| Pair compared | Same statement? | Same proof? | Action |
|---|---|---|---|
| Target / existing univariate one_le_pow_mul_abs_eval_div | No: independent rational coordinates and individual degree exponents vs one variable/denominator | Same final integer separation; new multivariate denominator identity required | Generalize multivariate API; retain univariate existing theorem. |
| Target / Theta leading-coefficient lower estimates | No: polynomial value vs nonzero coefficient | Shares `Int.one_le_abs` only | Do not unify different statements; share mathlib primitive. |
| Target / abs_eval_lt_of_le_index | No: lower arithmetic bound vs Taylor analytic upper bound | Different arguments | Complementary caller ingredients, not duplication. |
| Target / new generic and signed scratch forms | Original specializes exactly | Original proof transfers mechanically | Upstream generic primary and original convenience specialization. |

Inline-derivation search finds no independent reconstruction elsewhere; Theta lines215/482/488 concern leading coefficients. [inline-search.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/inline-search.json). No junk/dead-code recommendation: the integer-clearing argument is substantive even though it has one explicit caller.

## Phase6 — Actual composition experiments

1. Direct application of existing `one_le_pow_mul_abs_eval_div` fails because it consumes `Polynomial ℤ`, one rational coordinate and natDegree, rather than multivariate map/eval with coordinate ceilings.
2. `Int.one_le_abs` alone fails because the target is a scaled real evaluation; a nonzero integer witness and cast equality must first be proved.
3. Closure with `simp only [eval_map]` fails: normalizing evaluation spelling does not prove integrality or discrete separation.

All three failures are required-closure `fail_if_success` probes in [composition3-executed.lean.txt](../evidence/Roth.one_le_prod_pow_mul_abs_eval/composition3-executed.lean.txt); the theorem then closes with our newly proved generic lemma, whose source is fully present. The accepted receipt has no errors/warnings. This is NOT-COMPOSABLE from <=3 existing calls. An iterated univariate argument would have to clear earlier rational coefficients and track degree bounds, which is itself new algebra; a common-denominator/total-degree estimate generally loses the sharp product ∏qⱼ^rⱼ. No timed-out tactic or empty search is treated as an absence proof, and no generated generic helper is miscounted as an existing primitive.

## Phase7 — Actionable verdict

**YES-but-generalise-first**, reasons LITERATURE-WEAKENING and MODERN-IDIOM. Mathlib has the analogous univariate denominator-clearing theorem but lacks the coordinatewise multivariate clearing identity with individual degree bounds and its exact nonzero integer lower bound. This gap is concrete: support-degree complement exponents must be bounded and polynomial evaluation must be identified with a cast integer. It cannot be replaced by positivity, localization membership alone, or a <=3-call separation theorem. The complete original argument mechanically supports arbitrary finite coordinate types and ordered fields, with exact recovery and caller verification; these changes preserve the mathematical content and eliminate unnecessary coordinate/real representation constraints.

Proposed exact home: new `Mathlib/Algebra/MvPolynomial/DenomsClearable.lean`, adjacent to Eval/Degrees and parallel to the univariate DenomsClearable module. Avoid adding order/localization dependencies to foundational Eval merely to accommodate this result. Put the verified commutative-semiring/ring-hom/inverse algebraic clearing equality first, then ordered-field signed estimate and positive-natural corollary. Primary proof generalization is mechanical; splitting the helper is a concrete proof organization improvement, not a condition that changes the verdict.

Proposed PR title: **feat(Algebra/MvPolynomial): clear denominators of rational evaluations**. Ship this independent algebraic API first. Accepted related YES candidates `MvPolynomial.eval_eq_sum_box` and `Roth.abs_eval_le` (both YES-but-generalise-first, tracked progress PASS) concern evaluation APIs but belong to distinct Taylor/upper-bound work; group documentation/use examples if useful, not their unrelated proof development into the first clearing PR. `Roth.main_lemma` is already accepted YES-add-as-is but should remain a later Roth-specific PR. No old verdict was inherited.

Reviewer candidates based on actual relevant recent pinned commits: Elias Judin, `d1f304c611eb2e7507ea2393df3d155563609d8e` (2026-07-07, eval API parity #39865), and Yaël Dillies, `631b214f7c30ea1a438ddac7b63fbae0c595a874` (2026-09-02, MvPolynomial coeff refactor #41427). This selects potential reviewers from source history; it does not assert they reviewed these commits. Local git log is exact ([reviewer-commits.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/reviewer-commits.json)); GitHub page fetches returned cache misses, recorded honestly ([reviewer-web.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/reviewer-web.json)).

Pre-PR actions: `/generalise Roth.one_le_prod_pow_mul_abs_eval` (retain verified Fintype/ordered-field widening and signed variant); `/cleanup Roth/Main.lean Roth.one_le_prod_pow_mul_abs_eval` and cleanup the new mathlib module; choose a relevant reviewer above; replace only Main476 with the new positive-natural theorem after adding the generic API. Keep the project wrapper until that API exists. A downstream fallback home is a project-local arithmetic lemma module; Archive is unnecessary for this reusable finite polynomial bound. Production sources were intentionally unchanged for this assessment.

## Phase8 — Evidence and limitations

Accepted exact executed sources, full raw requests/results, timings, prefix controls, standard axioms and full attempt accounting are in [verification.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/verification.json). Failed/warning-bearing attempts are preserved separately and excluded from success evidence: clearing02 and shape01 recovered sorryAx after elaboration errors; composition02 had unreachable nested tactic warning; callers02 had orphan-docstring empty-line warning. composition01, callers01 and clearing01 were preparation-only and never executed, as documented in [preparation-only.json](../evidence/Roth.one_le_prod_pow_mul_abs_eval/preparation-only.json). No limit raises, new axioms, sorry, unsafe or native_decide in accepted proof sources. Stable18 mathlib-only imports and nine disk imports unchanged; no added imports. Original body printer elision is disclosed, local index limitations remain search limitations, and no new full literal build was due at frontier279 (next Main file boundary289; prior successful boundary228 and fresh matching baseline are reusable under root contract).

Portable current-manifest validation checks all17 inputs, exact canonical293 ordered names/private modules, source/request hashes, accepted raw diagnostics, standard axioms, complete original replay and full caller reconstruction, all15 searches, literature metadata, report links and both scratch/integrated layouts. Secret scan accompanies the frozen package. Native assessment and actual current-manifest, both-layout and secret validation have passed. Assessment completed; unresolved[]; root acceptance pending independent integration.
