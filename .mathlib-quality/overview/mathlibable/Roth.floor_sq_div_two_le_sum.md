# Roth.floor_sq_div_two_le_sum

**BORDERLINE-needs-human**, canonical declaration201, assessed2026-10-28. All required phases are complete; verification unresolved=[]; independent root acceptance is pending. The remaining questions concern which upstream API is useful, not proof verification. No production source, pin, Git state, or overview record was modified by this worker.

## Phase 0 — Doctor and baseline

The declaration is a theorem at `Roth/Theta.lean:289–297`, without `sorry` or a simp attribute. The successful baseline build reported2467jobs. Fresh hashes of all17 production inputs/pins match that baseline, so reusing it is valid: [baseline](../evidence/Roth.floor_sq_div_two_le_sum/baseline-build.txt), [fresh hashes](../evidence/Roth.floor_sq_div_two_le_sum/source-hashes.json), [baseline inputs](../evidence/Roth.floor_sq_div_two_le_sum/input-manifest.json).

The full985-line declaring module was read: it constructs sets of bounded integer polynomials and proves the three Θ estimates (Lemmas5–7). This endpoint is a scalar arithmetic fact in the Lemma6 section; it uses no project declaration. The full module body was replayed under a fresh namespace, including every downstream private and public declaration: [source](../evidence/Roth.floor_sq_div_two_le_sum/source-Theta.lean.txt), [full-module execution](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-fullmodule-executed.lean.txt), [native receipt](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-fullmodule-receipt.json).

## Phase 1 — Comprehend

For a nonnegative real number a, put n=⌊a⌋. Summing the nonnegative differences a−ν for ν=0,…,n gives at least n²/2. In fact the sum equals (n+1)(a−n/2), so its excess over n²/2 is (n+1)(a−n)+n/2, which is nonnegative.

The sole scalar parameter is `{a : ℝ}` and the sole hypothesis is `ha : 0 ≤ a`. The implicit section variables σ,τ and their finite/decidable instances do not occur in the actual elaborated type. There is no hidden project parameter. The notation is natural-valued floor; for negative a this convention gives0 and the sum is a, so the hypothesis matters.

Full native type, with no field elision:

```lean
∀ {a : ℝ}, 0 ≤ a → ↑⌊a⌋₊ ^ 2 / 2 ≤
  ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ↑ν)
```

The proof casts `Finset.sum_range_id_mul_two (n+1)` into ℝ, rewrites sum subtraction and the constant sum, and closes the polynomial inequality using `Nat.floor_le ha`. Standard axioms are exactly `[propext, Classical.choice, Quot.sound]`: [type](../evidence/Roth.floor_sq_div_two_le_sum/native-type.json), [exact original audit source](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-original-executed.lean.txt), [raw receipt](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-original-receipt.json). The large `#print` kernel body contains an explicit48381-character printer elision; this is disclosed rather than claimed as a complete kernel-body dump. Type, axioms, exact written source, and canonical kernel-value audit remain complete.

## Phase 2 — Preliminary checks

SMALL: elementary unnamed arithmetic helper, not one of the module's main results or a new structure. Proof has six substantive tactic lines. One-line-definition test: n/a, kind theorem. No definition-only exemption or inherited verdict applies. Literature breadth is exhaustive regardless of size.

## Phase 3 — Exhaustive literature

Every named channel was attempted. The command's informal “nine-channel” label is not used to invent an additional synthesis channel. Requests, returned-response SHA256/byte counts, statuses, locators and original concise summaries are preserved; full returned web bodies are not archived.

| Channel | Actual query / locator | Result and relevance |
|---|---|---|
| Web specific | `"sum" "alpha" "floor" "Roth" "Lemma 6"` | No exact external endpoint surfaced; local source below supplies it. |
| Web general | `sum arithmetic progression a minus k floor a quadratic lower bound` | General finite affine progression identity found. |
| Web aliases | `triangular number arithmetic series Gauss sum formula floor real` | Standard triangular-number/Gauss summation form found. |
| ChatGPT math MCP | Tool unavailable | Optional channel n/a; no substituted model answer counted as evidence. |
| Local references | Fresh `rg` of `clean.tex`, exact first FACT at857–876 | Exact theorem and arithmetic-series proof; [excerpt](../evidence/Roth.floor_sq_div_two_le_sum/clean-lemma6-excerpt.tex.txt), [request/hash](../evidence/Roth.floor_sq_div_two_le_sum/local-literature.json). |
| nLab | `site:ncatlab.org/nlab arithmetic series floor function triangular numbers` | [Floors and ceilings](https://ncatlab.org/nlab/show/floor): greatest-integer/order-adjoint characterization. No distinct triangular-bound API asserted. |
| nCatLab | `site:ncatlab.org/ncatlab arithmetic progression floor sum`, retry `site:ncatlab.org/ncatlab "floor"` | Returned /nlab pages outside requested /ncatlab namespace. No relevant distinct nCatLab result; scope mismatch recorded honestly. |
| Stacks | `site:stacks.math.columbia.edu arithmetic progression sum integers`, retry with quoted `"arithmetic progression"` | No relevant exact hit; this scalar finite-sum inequality is not an algebraic-geometry structure. |
| MathOverflow | `site:mathoverflow.net "floor" "arithmetic progression" sum`; retry `"sum" "floor" "quadratic"` | Related floor-sum indexing pages; [quadratic-floor-sum question](https://mathoverflow.net/questions/515251/an-elementary-proof-of-a-lower-bound-for-a-quadratic-floor-sum) concerns floor(a²/p), a different object. |
| Recent arXiv | `site:arxiv.org "triangular numbers" "floor" after:2021-10-28 before:2026-10-29` | Empty exact query; broader retry without `"floor"` found [2608.27697](https://arxiv.org/abs/2608.27697), whose abstract uses k(k+1)/2; no target lower bound. |

Evidence: [web0](../evidence/Roth.floor_sq_div_two_le_sum/web-0.json), [web1](../evidence/Roth.floor_sq_div_two_le_sum/web-1.json), [web2](../evidence/Roth.floor_sq_div_two_le_sum/web-2.json), [empty arXiv query](../evidence/Roth.floor_sq_div_two_le_sum/web-3.json), [retries and primary-source opening](../evidence/Roth.floor_sq_div_two_le_sum/web-4.json).

The primary authored teaching source [Kondratieva and Rowsell, *Sequences and Series*, CMS, §2.2.1](https://cms.math.ca/wp-content/uploads/2023/02/atom14.pdf) states the general finite arithmetic-series formula. Together with the project's exact fact, it identifies the content as elementary arithmetic-progression summation followed by an order bound. The broader algebraic identity is ∑ν=0ⁿ(a−ν)=(n+1)(a−n/2). The searched literature does not establish a distinct named theorem for this particular floor-square estimate, or specifically advocate an abstract partial-order Lean interface. Abstract generality below is a verified mathematical reformulation of the same finite sum, rather than a literature claim about preferred formalization. The recent window uses the actual assessment date2026-10-28; earlier accepted records were not rewritten.

## Phase 4a — Every parameter and hypothesis

| Parameter / feature | Current form | Assessment and actual check |
|---|---|---|
| Scalar | ℝ | The unchanged proof compiles for `Field K`, `LinearOrder K`, `IsStrictOrderedRing K`, `FloorSemiring K`; no completeness, topology or real logarithms used. |
| Floor structure | Natural floor | `FloorSemiring` suffices; `FloorRing` is stronger than necessary and separately compiles via its standard instance. |
| Order | Linear order on ℝ | Pinned `Nat.floor_le` requires LinearOrder. For the different division-free cutoff statement, PartialOrder with IsOrderedRing suffices; no unsupported same-signature partial-order claim. |
| Cutoff | n=⌊a⌋₊ | Proof needs only a natural n with `(n:K)≤a`; arbitrary-cutoff theorem compiled. This removes floor, without changing summands/indexing. |
| `ha` | 0≤a | Cannot drop uniformly: `a=-1` gives0≤−1. Compiled `nonnegNecessary` explicitly proves natural floor(−1)=0. |
| Division | `/2` in a field | Division-free stronger `(n:K)^2+n≤2*sum` compiles over CommRing/PartialOrder/IsOrderedRing, no strictness or characteristic-zero class. This is a changed representation, not literal hypothesis removal. |
| Index | ν:ℕ, inclusive0,…,n | Keep natural finite interval; arbitrary additive index groups do not carry this cutoff/counting operation without additional structure. |
| Constants | square and2 | Result follows from a stronger n(n+1)/2 lower bound; arbitrary denominators/exponents are not asserted. |
| Section instances | Finite σ,τ and DecidableEq | Absent from actual type; no artificial weakening claim. |

## Phase 4b — Mechanical generality verdict

The real specialization is strictly narrower than the verified scalar/cutoff forms. Exact isolated source and clean receipts: [generality source](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-isolated-executed.lean.txt), [receipt](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-isolated-receipt.json). All proofs are independent of Roth imports and guarded by `#check_failure Roth.floor_sq_div_two_le_sum`.

```lean
-- Verified same expression and floor, generalized scalar.
{K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
[FloorSemiring K] {a : K} (ha : 0 ≤ a) :
  (⌊a⌋₊ : K)^2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊+1), (a-ν)

-- Verified stronger division-free form; floor is no longer needed.
{K : Type*} [CommRing K] [PartialOrder K] [IsOrderedRing K]
{a : K} (n : ℕ) (hn : (n : K) ≤ a) :
  (n : K)^2+n ≤ 2 * ∑ ν ∈ Finset.range (n+1), (a-ν)
```

The first is a mechanical scalar generalization; the second changes statement shape and is not silently presented as a one-edit weakening. Keeping current ha is essential under natural floor. `Nat.floor_le` itself requires only Semiring/LinearOrder/FloorSemiring; field subtraction/division comes from the remaining expression. The weak-order cutoff proof uses only positivity of n+1 and a−n plus Gauss equality; it avoids linear-order automation. The exact identity also compiles for Field/CharZero with no order/floor. No claim of the absolutely weakest possible equality scalar hierarchy is made. A mechanical CommRing→Ring probe of the division-free core failed because `linear_combination` requires CommSemiring at the equality normalization step. This is a limitation of the chosen normalization infrastructure, not evidence that commutativity is mathematically necessary: natural casts are central. The failed source/receipt is retained separately and rejected.

## Phase 4c — All nine modern-idiom rows

| # | Question | Applies and evidence |
|---|---|---|
| 1 | Typeclasses replace bundled preambles | Yes for scalar structure: verified standard classes; ha is an element inequality and stays a proposition. |
| 2 | Filters/nets replace metric or sequence proofs | No: finite scalar sum; no limit or metric hypothesis. |
| 3 | Universal-property characterization | No constructed object; floor already uses standard floor classes. |
| 4 | Bundled substructure replaces closure predicate | No closure predicate or substructure. |
| 5 | Weaken field-specific hierarchy | Yes: division-free stronger cutoff form over partially ordered commutative rings, verified; literal `/2` expression still needs division. |
| 6 | Higher-category analogue | No categorical statement. |
| 7 | Concrete indices generalize | Scalar ℝ generalizes as above; natural counting index is intentional and retained. |
| 8 | Concrete-via-abstract diagnostic | Yes: six proof lines contain no Real-specific operation; floor only provides the bound `Nat.floor_le`. Replacing floor by n and supplied n≤a compiles. Literal ℝ occurs once as the cast target; subsequent proof is abstract polynomial order algebra. |
| 9 | False-generalization guard | Pass: same finite affine sum with standard ring subtraction; setting n=floor(a), using floor_le and the verified bridge recovers the real result. Replacing subtraction by truncated semiring subtraction or replacing natural floor by integer floor for negative a is not asserted. |

Modern idiom is available: arbitrary-cutoff ring bound, with floor result as a corollary, or an exact affine-sum equality. It enables finite-sum rewriting without floor imports and supports weak-order rings. Verified bridges are in [composition source](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-composition-executed.lean.txt), [receipt](../evidence/Roth.floor_sq_div_two_le_sum/floorsum201-composition-receipt.json). These are **new scratch helpers**, not existing mathlib replacement calls. Generality is not itself proof that this API should be exported.

## Phase 4.5 — Infrastructure risks

Theorem n/a for all six definition-only risks: diamonds, fragile definitional equalities, reducibility barriers, instance overlap, coercion loops and elaboration drift. No new instance/definition is proposed in this assessment; scalar class hypotheses are standard. This is a justified kind-based n/a, not an omitted phase.

## Phase 4.6 — All five strategy rows

| # | Strategy diagnostic | Assessment |
|---|---|---|
| 1 | ε-δ versus filters | n/a, no topology. |
| 2 | Element algebra versus substructure inclusions | n/a, a scalar finite arithmetic identity has no useful ideal/submodule counterpart. |
| 3 | Sequences versus nets | n/a, no convergence. |
| 4 | Construction versus universal property | n/a, no construction. |
| 5 | Missing helper that should exist | Potential exact affine-sum/cutoff API would remove repetitive cast/distribution arithmetic; selection requires upstream judgment. |

The mathematical strategy is MATHLIB-IDIOMATIC: Gauss formula plus order algebra. An API refactor is recommended if this family is upstreamed: supply the exact affine sum or general cutoff statement first. The two nearby helpers share normalization, which is a real API motivation; no implementation-cost downgrade is used.

## Phase 5 — Five actual mathlib methods on all forms

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current floor-square lower bound | [0](../evidence/Roth.floor_sq_div_two_le_sum/search-0.json): reciprocal-floor/harmonic near misses | [1](../evidence/Roth.floor_sq_div_two_le_sum/search-1.json): logarithmic/floor sums | [2](../evidence/Roth.floor_sq_div_two_le_sum/search-2.json): floor division, not finite affine bound | [current](../evidence/Roth.floor_sq_div_two_le_sum/rg-current.json) | [3](../evidence/Roth.floor_sq_div_two_le_sum/search-3.json): project endpoint only |
| Literature arithmetic progression / Gauss identity | [4](../evidence/Roth.floor_sq_div_two_le_sum/search-4.json): sum_range_id and sum_range_id_mul_two | [5](../evidence/Roth.floor_sq_div_two_le_sum/search-5.json): same | [6](../evidence/Roth.floor_sq_div_two_le_sum/search-6.json): same, Nat.triangle_succ | [standard](../evidence/Roth.floor_sq_div_two_le_sum/rg-standard.json) | [7](../evidence/Roth.floor_sq_div_two_le_sum/search-7.json): Gauss signatures |
| Abstract scalar/cutoff/finite-sum form | [8](../evidence/Roth.floor_sq_div_two_le_sum/search-8.json): unrelated quadratic bounds | [9](../evidence/Roth.floor_sq_div_two_le_sum/search-9.json): Gauss identity among broader hits | [10](../evidence/Roth.floor_sq_div_two_le_sum/search-10.json): interval transport, range lower bound | [abstract](../evidence/Roth.floor_sq_div_two_le_sum/rg-abstract.json) | [11](../evidence/Roth.floor_sq_div_two_le_sum/search-11.json): sum_range_sub telescoping family |

Local index status was `warming`, so empty/partial local results are not absence evidence. External indexes may differ from this repository pin. Exact relevant source files were read and hashed in [mathlib inputs](../evidence/Roth.floor_sq_div_two_le_sum/mathlib-inputs.json). All full-name/current-pattern rg outputs are untruncated archived receipts. The isolated native `#check` batch verifies full candidate signatures in the pin, rather than trusting search results.

Pinned useful building blocks:

* `Finset.sum_range_id_mul_two (n)` gives `(∑i<n,i)*2=n*(n-1)` over ℕ; n+1 removes truncated subtraction before casting.
* `Finset.sum_range_id` gives the natural divided formula; directly casting natural division would require its own bridge, so the multiplication form is used.
* `Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_range`, `nsmul_eq_mul`, natural cast normalization, and `Nat.floor_le ha` handle the actual expression.
* `Finset.sum_range_sub` is telescoping for differences of a supplied function. It does not supply the polynomial antiderivative identity or positivity premise automatically. It is a strategy alternative, not an exact endpoint hit.

No exact existing theorem or verified ≤3-existing-call replacement emerged. This is a scoped search conclusion, not a global mathematical absence proof. A fresh native `fail_if_success solve | exact?` ran once before any new helper was declared; bounded direct/normalization/rule probes also failed to close. Their failure is not treated as a theorem of absence.

## Phase 5.5 — Statement shape and scope

1. `range(n+1)` includes ν=n, correctly matching0≤ν≤floor(a); if a is integral, the extra endpoint contributes0. Replacing it with range(n) requires a bridge and is not defeq.
2. Exact affine-sum equality `(n+1)*(a−n/2)` is stronger algebraic normalization with no order/floor; compiled `exactSum` and `viaExactSum` recover the endpoint with actual floor_le/nonnegative-natural obligations.
3. Arbitrary natural n≤a and division-free n²+n≤2sum preserve the same sum while supporting weaker scalar structures; `ringCutoff` and `viaRingCutoff` compile. This is expanded representation, not merely deleting an unused instance from the original fixed real statement.

Standalone arithmetic belongs near finite sums/floor arithmetic if upstreamed. Proposed future exact identity home is `Mathlib/Algebra/BigOperators/Intervals.lean`; ordered cutoff home is `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean` or a dedicated interval-sum file after checking import layering. A floor corollary needs both floor and Finset layers; do not add it directly to Floor.Semiring, which asserts Finset absent. Paths are provisional design options, not asserted accepted destinations.

## Phase 6.0 — Complete callers and inline audit

Fresh scoped `rg --no-ignore`, tracked `git grep`, and enumeration across all17 baseline source/pin entries agree: the only target occurrence is its declaration at289. There are **zero explicit callers**, **zero direct canonical type/value consumers**, and no simp attribute. Native scan used all293 names in exact tracked order,293 runtime-unique,293 present,293 values. [Lexical enumeration](../evidence/Roth.floor_sq_div_two_le_sum/lexical-enumeration.json), [rg](../evidence/Roth.floor_sq_div_two_le_sum/callers.json), [tracked grep](../evidence/Roth.floor_sq_div_two_le_sum/tracked-callers.json), [inventory](../evidence/Roth.floor_sq_div_two_le_sum/inventory-callers.json), [canonical gates](../evidence/Roth.floor_sq_div_two_le_sum/canonical-gates.json).

Thus actual caller refactor/replay count is0 and n/a; no call is silently blackboxed. The full985-line module replay includes all potential local consumers and confirms the original module remains independently elaborated. Kernel direct consumers and source references are separate audits, not confused with transitive simp dependency closure. “Unused within the tracked project” does not mean dead for unknown external clients.

Inline audit found related algebra, not an unrecorded use or identical rederivation: [audit](../evidence/Roth.floor_sq_div_two_le_sum/inline-audit.json), [fresh search](../evidence/Roth.floor_sq_div_two_le_sum/inline-search.json).

* `mul_div_two_le_sum_max_aux` at304–320 uses Gauss/cast/sum distribution to bound lθ/2 under l≤θr, with sign/zero cases. [Complete body](../evidence/Roth.floor_sq_div_two_le_sum/inline-mul_div_two_le_sum_max_aux.lean.txt).
* `mul_sq_div_three_le_sum_max_of_pos_aux` at322–348 sets n=floor(θr), uses both n≤θr and θr<n+1, and proves the **stronger/different** (θr)²/3 sum bound before scaling/subset transport. Its explicit polynomial certificate cannot be replaced just by this target, whose n²/2 conclusion and no large-a assumption are insufficient. [Complete body](../evidence/Roth.floor_sq_div_two_le_sum/inline-mul_sq_div_three_le_sum_max_of_pos_aux.lean.txt).

## Phase 6 — Actual composition experiments

The old proof is reproduced independently under mathlib-only imports with every premise discharged. It needs the Gauss equality, natural successor simplification, casts, subtraction/constant/cardinal/nsmul sum normalization and nonlinear positivity from the actual floor bound. Compressing these into a short tactic script is not a verified term using at most three existing calls.

The abstract `cutoff` proof takes actual n≤a and proves the sum bound; `ringCutoff` proves the stronger n²+n≤2sum with `mul_nonneg (add_nonneg (Nat.cast_nonneg n) zero_le_one) (sub_nonneg.mpr hn)`. These are **new proofs**. They are not counted as existing mathlib APIs to manufacture NO-composable. Likewise `exactSum` is newly derived from Gauss plus full cast/sum normalization.

Actual endpoint bridges were compiled:

```lean
have h := ringCutoff (K := ℝ) ⌊a⌋₊ (Nat.floor_le ha)
nlinarith [Nat.cast_nonneg (α := ℝ) ⌊a⌋₊]
```

and

```lean
rw [exactSum]
nlinarith [Nat.floor_le ha]
```

Both show how a future abstract API would serve the original endpoint. Neither is an existing-mathlib replacement because `ringCutoff`/`exactSum` are new scratch helpers. The original target is absent from isolated imports, no project helper is counted, and all actual positivity/floor premises are visible. Failed initial sources and receipts are kept separately: two isolated failures and two scalar-annotation bridge failures, plus the Ring mechanical probe; recovered sorryAx in those receipts is explicitly rejected. [Verification record](../evidence/Roth.floor_sq_div_two_le_sum/verification.json) identifies all accepted/rejected runs.

## Phase 7 — Verdict and concrete upstream questions

**BORDERLINE-needs-human.** This is standard elementary arithmetic, and verified broader useful forms exist. Mathlib already contains the Gauss core; no exact endpoint or strict three-existing-call composition has been verified. The zero-caller floor corollary alone has a weak local API-demand signal, while nearby different bounds suggest a reusable normalization layer. The decision concerns API scope and preferred theorem shape, not execution time, proof length alone, or unverified inability to generalize.

1. Should mathlib export a generic affine arithmetic-series equality for casts in `range(n+1)`, allowing both local floor/max proofs to share normalization?
2. Should the stronger division-free arbitrary-cutoff inequality be exported as an ordered finite-sum API, with floor-square inequality a downstream corollary?
3. If either general API is accepted, is a separately named natural-floor-square corollary useful enough to export, or should this currently unused project endpoint remain local/be removed?

Recommended next action: discuss that API choice, retaining `Roth/Theta.lean` as the alternative local destination meanwhile. Every explicit caller refactor plan is vacuous (K=0); removal would require confirming external compatibility. No production deletion was performed. If upstream interest is confirmed, run `/generalise Roth.floor_sq_div_two_le_sum` and `/cleanup Roth/Theta.lean Roth.floor_sq_div_two_le_sum` against the chosen statement and review the neighboring arithmetic helpers together. No proposed PR or grouping is asserted as accepted; YES-only reviewer/PR-selection obligations are n/a for this BORDERLINE verdict.

## Phase 8 — Package and verification limits

The portable read-only [validator](../evidence/Roth.floor_sq_div_two_le_sum/validate.py) checks current copy-manifest hashes/bytes, required metadata, all phases,17 fresh source/pin hashes, exact canonical293 source order and runtime audit, clean complete native receipts, standard axioms, formal/literature requests, full-module body, links, and secret scan. [Assessment](../evidence/Roth.floor_sq_div_two_le_sum/assessment.json), [phase evidence](../evidence/Roth.floor_sq_div_two_le_sum/phase-evidence.json), [overview entry](../evidence/Roth.floor_sq_div_two_le_sum/overview-entry.json), [verification](../evidence/Roth.floor_sq_div_two_le_sum/verification.json).

Accepted runs use no new axiom, sorry, unsafe, native_decide or resource-limit increases; no warnings/errors remain and disk receipts have partial=false. Rejected native attempts remain honest evidence, never accepted proof. A single successful composition guard proves only failure of the specific attempted closure tactics. Local symbol index warming and web namespace/no-hit results are disclosed. Unresolved verification is empty.

At freeze the isolated virtual prefix is the previous stable17 plus `Mathlib.Algebra.Order.Archimedean.Real.Basic` as import18, needed for the real floor instance. The disk document retains all original nine imports and its last clean full-module201 source. Full-module body and canonical names are preserved exactly. Root independently reviews, accepts, integrates, validates and owns any commit/push.
