# Roth.le_index_sum — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** The independently checked analogous finite-sum law on `AddMonoidAlgebra.infDegree` is exactly `AddMonoidAlgebra.supDegree_sum_le` with `B := OrderDual T`. A common lower bound follows by `Finset.le_inf_iff` and transitivity. The old real-valued convention additionally requires a nonzero sum and explicit projection/translation normalization. This is a fresh parent re-aim assessment, not inheritance from a neighboring result.

## Phase 0 — Doctor

Canonical declaration141 is the public theorem at `Roth/Index.lean:118`. The entire [Index module](../evidence/Roth.le_index_sum/Index.lean.txt), its sole external [Theta module](../evidence/Roth.le_index_sum/Theta.lean.txt), and relevant Taylor/weight interfaces were read. Index develops a support minimum at a point, its derivative/sum/product laws and renaming/univariate specializations. Theta applies the sum law to a determinant expansion in the proof of Lemma6. [Canonical entry](../evidence/Roth.le_index_sum/canonical-entry.json).

The [baseline](../evidence/Roth.le_index_sum/baseline-build.txt) succeeded with exit0,2467 jobs and no reported errors/warnings. All17 source/pin hashes freshly match the shared baseline manifest: [inputs](../evidence/Roth.le_index_sum/inputs.json), [check](../evidence/Roth.le_index_sum/input-hash-check.json). Assessment makes no production, pin, Git, overview or progress edits.

## Phase 1 — Comprehend

If a finite sum of real multivariate polynomials is nonzero and every nonzero summand has index at least c at the same point and relative to the same denominators, then the sum has index at least c. The hypothesis ignores zero summands. σ indexes variables; Fintype supports the parent's global weight sum; ι is the arbitrary summand index type; s is its finite subset; f is the polynomial family; α is the center, r the natural denominators, and c an arbitrary real lower bound. Universes of σ and ι are independent. There is no positive-r, nonempty-σ, domain, or c≥0 premise.

Full native elaborated type:

```lean
Roth.le_index_sum.{u_1, u_2} : ∀ {σ : Type u_1} [inst : Fintype σ]
  {ι : Type u_2} {s : Finset ι} {f : ι → MvPolynomial σ ℝ}
  {α : σ → ℝ} {r : σ → ℕ}, ∑ i ∈ s, f i ≠ 0 →
  ∀ {c : ℝ}, (∀ i ∈ s, f i ≠ 0 → c ≤ Roth.index (f i) α r) →
    c ≤ Roth.index (∑ i ∈ s, f i) α r
```

The proof invokes le_index_iff for the sum. A Hasse coefficient nonzero in the sum is the sum of individual evaluated Hasse coefficients, so some summand coefficient is nonzero. That summand is nonzero, and its assumed index bound and le_index_iff imply the required weight bound. Cancellation may remove coefficients and increase the minimum; it cannot introduce a coefficient absent from all summands.

[Original source](../evidence/Roth.le_index_sum/le-index-sum-original-executed.lean.txt), [audit source](../evidence/Roth.le_index_sum/le-index-sum-audit-executed.lean.txt), [complete native receipt](../evidence/Roth.le_index_sum/le-index-sum-original-audit-receipt.json) provide full type/body without printer elision, standard axioms and a fresh exact293 requested/unique/present/value-bearing canonical audit. Required information is scoped to new region1062/1065, not historical scratch messages. Exactly one direct kernel consumer is Roth.sum_max_sub_le_index_det.

## Phase 2 — Preliminary

**BIG:** explicitly listed among the Index module's main results and used in the determinant argument. One-line definition check and all definition exemptions are **n/a — theorem**. This classification does not reduce the search protocol. The proof has real coefficient selection, so no automatic glue prefilter applies.

## Phase 3 — Exhaustive literature

Only exact requests, response UTF-8 bytes/SHA256/status and sanitized titles/URLs are archived, with original concise summaries. [Specific/standard/abstract web queries](../evidence/Roth.le_index_sum/web-0-metadata.json), [nLab/nCatLab/Stacks](../evidence/Roth.le_index_sum/web-1-metadata.json), [MO/recent requests](../evidence/Roth.le_index_sum/web-2-metadata.json), [refined/direct access](../evidence/Roth.le_index_sum/web-3-metadata.json), [recent arXiv refinement](../evidence/Roth.le_index_sum/web-4-metadata.json), [local search](../evidence/Roth.le_index_sum/local-literature-search.json), [manuscript excerpt](../evidence/Roth.le_index_sum/clean-excerpt.tex.txt), [summary](../evidence/Roth.le_index_sum/literature-summary.json).

| Channel | Actual request / locator | Finding and limitation |
|---|---|---|
| General web specific | `Roth polynomial index sum minimum order vanishing Lemma addition` | [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf), Definition1 pp2–3, defines the weighted index and explicitly states the binary sum/min inequality. Direct PDF open succeeded. [Roth ICM1958 p206](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) gives the weighted derivative minimum; indexed passage inspected. |
| General web standard | `weighted order polynomial sum minimum valuation inequality` | Valuation minimum inequality and weighted-order language; binary inequality implies finite common-bound form by iteration. This implication is mathematical synthesis, not a claim that every source displays the exact finite-sum Lean statement. |
| General web abstract | `finite support infimum degree sum order dual semilattice` | Order-duality/finite-meet material; [Barr–Wells Category Theory for Computing Science §5.4.6](https://www.math.mcgill.ca/barr/papers/ctcs.pdf) describes inf/sup semilattices and opposite order. This clarifies duality, not a new polynomial law. |
| ChatGPT math | Standard/generality/history consultation | n/a: ask_chatgpt_math unavailable. No fabricated response or extra synthetic channel. |
| Local references | clean.tex530–618, especially Lemma4-1 and proof | Index0=∞, sum index≥min, proof by vanishing of all low-weight coefficients. The current theorem is the finite common-bound version used for determinant terms in Lemma6. |
| nLab | `site:ncatlab.org/nlab valuation ultrametric inequality` | [valuation, Definition](https://ncatlab.org/nlab/show/valuation) gives v0=∞ and v(x+y)≥min. Indexed text accessible; direct open failed unsupported application/xhtml+xml. This law is adjacent valuation structure; arbitrary degree maps need not be multiplicative valuations. |
| nCatLab | `site:ncatlab.org/ncatlab valuation sum infimum`; refined `site:ncatlab.org/ncatlab "valuation"` | Explicit namespace requests returned nLab and other same-host pages, no exact /ncatlab hit. Honest out-of-namespace outcome, not proof of absence. |
| Stacks | `site:stacks.math.columbia.edu valuation v x+y minimum`; refined tag query | [00I8 §10.50 Valuation rings](https://stacks.math.columbia.edu/tag/00I8) opened successfully; valuation-ring/associated ordered-value context. Search also returned algebra.pdf p285. No exact weighted finite-polynomial-sum theorem claimed. |
| MathOverflow | `site:mathoverflow.net weighted order polynomial sum valuation minimum` | [510730, lower bound on p-adic valuation of binomial sum](https://mathoverflow.net/questions/510730/lower-bound-on-p-adic-valuation-of-binomial-sum), answer discussion explicitly applies the finite-sum minimum principle. Related support-order discussion appears in [476147](https://mathoverflow.net/questions/476147/how-should-we-picture-the-set-of-monomial-orders-positive-monoid-orders-on). No proof imported from these discussions. |
| Recent arXiv,2021-10-27–2026-10-27 | Broad weighted-order/Roth requests; refined `site:arxiv.org/abs/ "monomial valuations" after:2021-10-27` | Broad batch did not expose an exact recent hit. Refined query returned [Kim2604.18465](https://arxiv.org/abs/2604.18465), abstract on quasi-monomial valuations computing α/δ, and [Dutta–Ghosh2609.03451](https://arxiv.org/abs/2609.03451), abstract connecting monomial valuations and Taylor expansions. Both are recent related context, no claim they supply new finite-sum API. |

Historical derivative-index wording and modern translated coefficient-support language describe the same characteristic-zero point quantity. The manuscript permits positive real denominators and uses∞at zero; the project admits natural denominators including0 and projects the zero polynomial to0. The additive law survives arbitrary support weights, with∞at zero; the old zero-default form needs hs. This is elementary support monotonicity, not a complete valuation construction.

## Phase 4a–4b — Every parameter and generality

| Current parameter / hypothesis | Checked broader form / necessity |
|---|---|
| σ/Fintype | Arbitrary A in finiteInfLaw, with no algebraic structure or finiteness on A. MvPolynomial support is finite even for infinite σ. Fintype remains fixed by unchanged Roth.weight. |
| ℝ polynomial coefficients | Semiring R for the support-degree law, with independent universe. No commutativity, field, domain, Nontrivial or characteristic assumptions. The point aeval version uses CommRing for the available translation-nonzero equivalence. |
| P-family f | Arbitrary AddMonoidAlgebra R A in abstract law; polynomial aeval specialization separately checked. |
| α | Only chooses translation; absent from abstract law. Retained in checked point and original forms. |
| r and weight | Arbitrary D:A→T, no positivity, additivity or injectivity. Reciprocal-natural denominators are just one degree map; rj=0 is allowed. |
| c/result | Arbitrary SemilatticeInf T with OrderTop T, independent universe; not necessarily linear or additive. ProjectedLaw specializes T=WithTop ℝ and projects finite order. |
| ι/s | Arbitrary summand index universe and finite subset; no Fintypeι. Empty s is valid for top-valued law; hs excludes it in projected old form. |
| hs sum≠0 | Removed in unprojected abstract law, retained for old/projected real convention. Empty sum and X+(-X) guards verify necessity. |
| hf nonzero summands only | Old form avoids impossible positive lower bounds on index0=0. Abstract statement bounds all summands; a zero summand has infDegree⊤, hence automatic. Actual projectedLaw handles this distinction explicitly. |

**STRICTLY NARROWER THAN STANDARD in representation**, while no mechanical fixed-parent weakening is claimed. The standalone broader statements actually compile; no hypothetical migration is counted as validation. [Final mathlib-only source](../evidence/Roth.le_index_sum/le-index-sum-mathlib-final-executed.lean.txt) and [raw success](../evidence/Roth.le_index_sum/le-index-sum-mathlib-final-receipt.json) check the abstract semilattice law, commonLowerBound and real projection. There is an independently verified existing law, so these weakenings do not motivate a new upstream theorem.

## Phase 4c — All nine modern-idiom rows

| # | Diagnostic | Finding / downstream consequence |
|---|---|---|
|1| Typeclasses | Semiring and SemilatticeInf/OrderTop express exact needs; no new Index class. Reuses dual degree API for arbitrary coefficients and targets. |
|2| Filters | n/a: finite algebraic support, no topology/convergence. |
|3| Universal property | Common lower bounds use finite meet introduction; support containment of sums supplies inequality. Existing finite infimum, no new universal construction. |
|4| Bundled substructures | A coefficient-vanishing filtration could package addition closure, but is unnecessary for one sum inequality. No new submodule/ideal closure assertion made. |
|5| Field to semiring/module | Yes: all sum-support reasoning works over Semiring; no multiplication/domain fact used. Point transport is separated. |
|6| Higher categories | No coherence/categorical structure; expressing meets as poset limits adds no concrete benefit here. |
|7| Concrete ordered index | Yes: arbitrary semilattice target and arbitrary D. Enables incomparable degree values and nonintegral weights through the same API. |
|8| Concrete-via-abstract | Fires: after map_sum twice the proof only selects a nonzero summand coefficient and compares lower bounds. No specific analytic property of real coefficients, reciprocal weights or point geometry appears. Abstract finiteInfLaw isolates this exact support content. |
|9| False-generalization guard | Preserve zero convention explicitly; reject removing hs after untopD0 because full cancellation yields0; reject equality with the minimum because partial cancellation can increase order; reject arbitrary infinite-support infima without boundedness; reject arbitrary D as multiplicative valuation. |

Modern idiom **already available**: OrderDual specialization of supDegree_sum_le plus finite meet introduction. REFACTOR-RECOMMENDED for upstream organization; moderate shared projection/translation refactor for old consumers, never a cost-based verdict.

## Phase 4.5 — Six infrastructure risks

All six are **n/a — theorem**: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe infrastructure, coercion ambiguity. The target introduces only a proof of Prop, no instance/data/coercion. Generic universes are verified in replacement probes; this does not purport to audit a hypothetical filtration bundle.

## Phase 4.6 — All five proof-strategy rows

| Question | Finding |
|---|---|
| ε–δ to filters | n/a: no topology. |
| Elements to algebraic inclusions | Support of sum is contained in union of summand supports; generic supDegree_sum_le already packages this. No ideal structure needed. |
| Sequences to nets | n/a: finite sum. |
| Construction to universal property | Finite meet introduction discharges a common bound; use existing Finset.le_inf_iff. |
| Missing helper | No missing sum-degree estimate: OrderDual specializes existing supDegree_sum_le. Projection/point translation normalization is an explicit bridge, not preexisting API. |

Strategy verdict **REFACTOR-RECOMMENDED** after parent re-aim. Current coefficient-selection proof is correct and useful as manuscript-facing local API, but the generic support law belongs to existing degree theory.

## Phase 5 — Five actual methods × three forms

[Complete formal receipts](../evidence/Roth.le_index_sum/formal-search.json) preserve12 actual requests: Finder/Loogle/LeanSearch/local on current, literature and abstract forms. [Current rg](../evidence/Roth.le_index_sum/rg-current.json), [literature rg](../evidence/Roth.le_index_sum/rg-literature.json), [abstract rg](../evidence/Roth.le_index_sum/rg-abstract.json) provide fifth method. All services returned; failures are not absence evidence. Local index unavailable is a limitation; external revisions may differ from the pin. [Pinned hashes](../evidence/Roth.le_index_sum/mathlib-inputs.json).

| Method | Current Hasse/index form | Standard weighted-order form | Abstract infDegree form |
|---|---|---|---|
| Finder | Weight/degree bounds, adjacent weightedOrder_le | min_weightedOrder_le_add; analytic order analogues | supDegree_sum_le, le_infDegree_add, infDegree |
| Loogle | Quoted Hasse+sum: empty | weightedOrder+sum query: two returned hits | exact supDegree_sum_le signature |
| LeanSearch | min_weightedOrder_le_add and unrelated weight bounds | power-series/analytic min-add laws | supDegree_sum_le and degree_sum_le |
| rg | Own theorem and determinant caller | Pinned weightedOrder law family | Pinned supDegree_sum_le and infDegree abbreviations |
| local | Own theorem | weightedOrder_sum empty; index unavailable | supDegree_sum_le source hit; index unavailable |

Positive candidate verified natively: `AddMonoidAlgebra.supDegree_sum_le`, Mathlib/Algebra/MonoidAlgebra/Degree.lean270, states the sum's supremum degree≤sup of individual degrees with Semiring/SemilatticeSup/OrderBot. With B=OrderDual T, that very term has the exact finite-infDegree law. Both supDegree and infDegree abbreviate support folds, so this is genuine definitional specialization, requiring no new support proof. `AddMonoidAlgebra.le_infDegree_add`, Degree627, is the binary analogous law. `Finset.le_inf_iff`, generated dual from Fold.lean99, supplies the common bound. `WithTop.coe_untopD_le`, generated dual in Order/WithBot.lean593, handles zero-default projection inputs; `Finset.coe_inf'` handles a nonempty sum support. `MvPowerSeries.min_weightedOrder_le_add` is the adjacent natural-weight/ENat law, not needed to clear denominators here.

Conclusion: **found existing analogous law** in the parent's representation. The exact unprojected finite sum inequality is one existing call; its common-bound version is finite-meet introduction plus transitivity.

## Phase 5.5 — All three statement-shape checks

Normal forms checked: original common real lower bound with nonzero summand guard; finite infimum of infDegrees≤infDegree sum; coefficient vanishing below a cutoff; projected generic point order. The finite-infimum inequality is the canonical existing generic form. For callers already holding a common bound, le_inf_iff followed by trans is natural. No iff orientation issue or new quadratic collection of equivalent forms is needed.

Syntactic generality: finiteInfLaw, commonLowerBound and projectedLaw actually compile; pointProjectedLaw and replacement test center/translation and the old exact arguments. All-summand hypotheses are weaker in the top-valued form than they look, because zero is top. In the real fallback form the guarded premise is essential to retain positive c without assuming nonzero every f i.

Superfluous-argument audit: σ/ι/s/f/α/r/c all specify mathematical data; Fintype/ℝ remain fixed by current parent. hs is necessary with fallback0. The per-summand nonzero implication is useful rather than redundant. No positivity, nonempty variables or nonzero-every-summand should be added. Overall **RESTATE-BEFORE-SHIP**, which would duplicate existing degree API.

## Phase 6.0 — Complete caller and inline audit

[Complete ignore-independent searches](../evidence/Roth.le_index_sum/complete-caller-search.json), [fresh comment-stripped lexical enumeration](../evidence/Roth.le_index_sum/lexical-enumeration.json), [full caller fragment](../evidence/Roth.le_index_sum/callers.json), [direct consumers](../evidence/Roth.le_index_sum/direct-consumers.json). Fresh rg--no-ignore and tracked git-grep agree on docstring, declaration and sole application. Canonical source inventory covers all production modules. There are **one source caller/application, K=1 outside Index, one external module**, and independently one direct kernel-value consumer. Neither count asserts opaque/simp/transitive dependency closure. Target has no simp attribute and is used, not junk.

Roth.sum_max_sub_le_index_det at Theta.lean398 applies `le_index_sum hdet` after Matrix.det_apply'. The bound is shared by all nonzero signed permutation products; subsequent proof uses nonzero entries, sign invariance, index_prod and the entry derivative estimate. Refactor its sole call to the checked replacement at identical arguments, or after shared parent migration introduce the common bound with le_inf_iff and apply finiteInfLaw, preserving hdet and real projection. Do not duplicate the normalization bridge at each use.

[Inline audit](../evidence/Roth.le_index_sum/rg-inline.json) finds this theorem and determinant proof, plus unrelated index-sum/product statements; it finds no additional independent re-derivation of the exact additive lower-bound law. The sum in index_prod is a product law, not another additive proof. Source names are searched across canonical inventory despite ignore rules.

## Phase 6 — Actual composition and representation experiments

[Final isolated proof](../evidence/Roth.le_index_sum/le-index-sum-mathlib-final-executed.lean.txt) and [complete raw receipt](../evidence/Roth.le_index_sum/le-index-sum-mathlib-final-receipt.json) establish:

```lean
-- [Semiring R] [SemilatticeInf T] [OrderTop T]
s.inf (fun i ↦ AddMonoidAlgebra.infDegree D (f i)) ≤
    AddMonoidAlgebra.infDegree D (∑ i ∈ s, f i) :=
  AddMonoidAlgebra.supDegree_sum_le (B := OrderDual T)
```

commonLowerBound uses `(Finset.le_inf_iff.mpr hf).trans (finiteInfLaw D s f)`: expanded, three existing calls (finite meet introduction, transitivity, supDegree_sum_le); finiteInfLaw is only the one-call specialization, not an extra mathematical helper. projectedLaw is a real normalization proof: lift individual real bounds by coe_untopD_le, handle zero summands as top, then project the nonempty sum-support infimum via coe_inf'. Its new proof does not count as preexisting mathlib API. Initial and clean attempts failed in proving support nonempty because broad simp distributed coeff over the sum and simp-only did not use coeff_eq_zero through negation; rejected receipts preserve recovered sorryAx and are never accepted. Final uses explicit Finsupp.support_nonempty_iff and AddMonoidAlgebra.coeff_eq_zero and has only standard axioms.

The parent [isolated bridge](../evidence/Roth.le_index_sum/index-mathlib-infdegree-final-executed.lean.txt), [success](../evidence/Roth.le_index_sum/index-mathlib-infdegree-final-receipt.json), [fully expanded isolated bridge](../evidence/Roth.le_index_sum/index-expanded-mathlib-executed.lean.txt), [success](../evidence/Roth.le_index_sum/index-expanded-mathlib-receipt.json) were independently inspected. Empty support maps to fallback0; nonempty support uses coe_inf' and inf'_eq_csInf_image. Expanded weights use finite-support reciprocal Finsupp.weight. The [actual target bridge](../evidence/Roth.le_index_sum/index-consumers-executed.lean.txt), [receipt](../evidence/Roth.le_index_sum/index-consumers-receipt.json), [fully expanded point bridge](../evidence/Roth.le_index_sum/index-expanded-bridge-executed.lean.txt), [receipt](../evidence/Roth.le_index_sum/index-expanded-bridge-receipt.json) preserve all P and all r, including mixed zeros. The old index is not definitionally equal to projected infDegree; these are newly proved bridges.

Fresh [target and aeval point-law source](../evidence/Roth.le_index_sum/le-index-sum-target-final-executed.lean.txt), [clean native receipt](../evidence/Roth.le_index_sum/le-index-sum-target-final-receipt.json) at region1384, [guards](../evidence/Roth.le_index_sum/le-index-sum-guards-executed.lean.txt), [full caller replay](../evidence/Roth.le_index_sum/le-index-sum-callers-executed.lean.txt) and [combined clean receipt](../evidence/Roth.le_index_sum/le-index-sum-guards-callers-final-receipt.json) at regions1455/1481 are accepted verification. Initial target application generated goals in hf/hs order; explicit refine corrected this. The next target attempt needed ne_eq to rewrite Taylor nonvanishing. The initial guard/caller batch had an unnecessarySimpa warning; simp at hh removed it. All five rejected attempts are separately preserved in the [verification record](../evidence/Roth.le_index_sum/verification.json), including sources/complete receipts; none is accepted proof evidence. Replacement invokes no target theorem or le_index_iff, and preserves the guarded bound. The caller replay substitutes exactly the sole application and prints standard axioms. The zero-sum guard is not a hypothetical issue: X and -X have equal positive point indices at0 while their sum has index0. Hence removing hs is false. All-zero-denominator specialization verifies no positivity premise sneaked into the replacement.

Old spelling is **NOT-COMPOSABLE as a bare ≤3-call mathlib term**: projection, Taylor transport, nonzero normalization and the project parent bridge are additional real steps. The analogous unprojected finite-sum law is **one existing call**, and its common-bound corollary≤3. A closing simp[defs] alone would invoke Phase6b BORDERLINE caution; it is not deciding evidence. ModeB's explicit re-aim rule requires NO-mathlib-has-it after independent law and bridge checks, both supplied here. The newly accepted140 derivative law is separate and does not provide this additive API; neither verdict is inherited.

## Phase 7 — Verdict and action

**NO-mathlib-has-it** via `AddMonoidAlgebra.supDegree_sum_le (B := OrderDual T)` on infDegree, with `Finset.le_inf_iff`/trans for common bounds. This is a direct existing analogous law, freshly specialized over arbitrary semiring, support type and semilattice with top. Search-negative results, costs and parent verdict alone play no role.

After using a shared parent normalization bridge or migrating the parent interface, replace Theta.lean398 with finite meet introduction and the dual sum law, retaining hdet to justify real fallback projection. The compiled full caller replay checks the original exact use via replacement. Delete le_index_sum after its sole application is replaced if eliminating wrappers. Keep all following signed-product and derivative estimates. Do not call the new projectedLaw an existing mathlib theorem, and do not pretend projection/aeval normalization is definitional in the old API.

Alternative local destination: **Roth/Index.lean**, as manuscript-facing convenience API for the determinant argument and old zero convention. It is useful local code, not dead code; an upstream duplicate is unnecessary. YES-only upstream path/title/grouping/reviewer-selection steps are n/a: no PR is proposed. The derivative estimate140 remains its independently accepted generalise-first contribution; this sum-law assessment does not change it.

## Phase 8 — Handoff

All phases complete, verification unresolved=[], root acceptance pending. [Assessment](../evidence/Roth.le_index_sum/assessment.json), [verification](../evidence/Roth.le_index_sum/verification.json), [overview entry](../evidence/Roth.le_index_sum/overview-entry.json), [current manifest](../evidence/Roth.le_index_sum/copy-manifest.json), [portable validator](../evidence/Roth.le_index_sum/validate.py). The validator checks required schema, phase completion, all accepted native proofs/full-file diagnostics and scoped info/axioms, exact293 canonical order, all17 current source/pin hashes, current manifest hashes/bytes, full sole caller replay, formal/literature channels, local links and secret scan. Historical manifests and root-only review/acceptance records do not replace current validation.
