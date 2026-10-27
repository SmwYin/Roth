# Roth.card_filter_weight_le — full mathlibable assessment

**BORDERLINE-needs-human.** Lemma 8 contains real finite counting mathematics. The uncertainty is the appropriate upstream API: an arbitrary finite product-box lower-tail estimate, or a corollary of a stronger product-measure concentration theorem. This is not a cost-based downgrade. Keep the working theorem in `Roth/Lattice.lean` until that API choice is made.

## Phase 0 — Doctor

Resolved public theorem at `Roth/Lattice.lean:202`, canonical declaration132. All17 production/pin hashes freshly match the shared baseline manifest; baseline `lake build` succeeded with2467 jobs. Root additionally ran a fresh full build at this file boundary; its result is archived in the build receipt. No production or Git change was made by this assessment. The whole220-line declaring module,132-line Box module and762-line MainLemma caller module were read. [Inputs](../evidence/Roth.card_filter_weight_le/source-hashes.json), [baseline](../evidence/Roth.card_filter_weight_le/baseline-build.txt), [verification](../evidence/Roth.card_filter_weight_le/verification.json).

Native `#check`, `#print`, standard axioms and kernel values were checked. Complete canonical array293 has exact tracked order,293 unique names,293 present values. Sole direct kernel consumer is `_private.Roth.MainLemma.0.Roth.mul_card_filter_weight_le_aux`. The kernel pretty-printer body contains an explicit LEAN_MCP_MAX_OUTPUT_CHARS elision marker; no full kernel-body dump is claimed. The complete written proof, native type and canonical kernel-value audit remain available. These are direct value dependencies, distinct from transitive dependencies or simp closure. The validator checks fresh target markers, not historical messages. [Audit source](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-audit-executed.lean.txt), [raw receipt](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-original-audit-receipt.json).

## Phase 1 — Comprehend

For a nonnegative dimension m, positive integral side lengths r_j, and λ>0, count the natural lattice vectors 0≤d_j≤r_j whose normalized coordinate sum is at most (m−λ)/2. Their number is at most (2√m/λ) times the total box size ∏(r_j+1). Finsupp is a representation of ordinary tuples because the index type is finite. At m=0 the cutoff is negative, so the filtered box is empty.

Full native type:

```lean
∀ (m : ℕ) (r : Fin m → ℕ),
  (∀ (j : Fin m), 0 < r j) →
    ∀ {lam : ℝ},
      0 < lam → ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2}.card ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)
```

The induction splits λ≤2√m, where total cardinality suffices, from λ>2√m. In the second case split off the last coordinate, apply dimension m−1 with λ′=λ−1+2i/r_last, and sum the reciprocal bounds. The reflected-pair harmonic estimate is the analytic input. The m=0 and remaining m=1 cases are empty-filter arguments. [Complete source](../evidence/Roth.card_filter_weight_le/Roth-Lattice.lean.txt).

## Phase 2 — Preliminary checks

**BIG**: this is the module's advertised main lattice count estimate, Lemma8. The one-line definition-only test and its three definition exemptions are **n/a — theorem**, regardless of the short final induction driver. Its private helper closure contains the substantial argument.

## Phase 3 — Exhaustive literature

Every named channel was actually attempted. The informal nine-channel label includes the three general-web forms separately in this table; no synthetic extra channel is counted. Exact requests, serialized-return SHA256/byte counts, URLs and concise source summaries are retained; full web bodies are not retained.

| Channel | Actual query / access | Finding and standard form |
|---|---|---|
| General web, specific | `"Roth theorem" "lattice" "2" "lambda" count` | No exact external theorem located; general lattice results and arithmetic-progression Roth hits are excluded. |
| General web, broad | `Roth lemma lattice point count normalized sum r_i sqrt m concentration estimate` | Lattice counting/concentration analogues, no exact replacement. |
| General web, aliases | `"Formalizing Roth" "Lemma 8"`; later `Roth theorem lattice count lemma "lambda" "r" notes` and `"Roth" "number" "tuples" "lambda" "sqrt"` | Exact source found locally, not independently online. |
| ChatGPT mathematical opinion | Tool availability checked | n/a: `ask_chatgpt_math` unavailable; other channels unchanged. |
| Local clean.tex | `roth:lem8`, §6, lines1050–1153 | Exact primary manuscript lemma: m≥1, positive integer r_i and λ>0, identical2√m/λ bound. Current Lean also proves m=0. |
| nLab | `site:ncatlab.org/nlab "Chebyshev inequality" "probability"`; direct probability-theory, finite-set and Hoeffding pages | Indexed generic inequality page is not this theorem. Direct probability/finite-set fetches fail400 unsupported XHTML; Hoeffding page inaccessible. |
| nCatLab | `site:ncatlab.org "Roth" "lattice"`; `site:ncatlab.org/ncatlab "lattice point" "count"` and `"probability" "Chebyshev"`; direct nCatLab homepage | Targeted namespace queries returned unrelated nLab pages outside/ncatlab; no exact hit. Homepage inaccessible. No categorical standard restatement evidenced. |
| Stacks | `site:stacks.math.columbia.edu "lattice" "count" Roth`, `"Chebyshev"`; homepage | No exact hit; homepage identifies algebraic geometry scope. This is a finite probability/counting inequality, not an algebraic-geometric structure. |
| MathOverflow | `site:mathoverflow.net Roth lattice count simplex lemma` | Questions10266 (simplex),258412 (hypercube),273457 (box) concern algorithms/Davenport bounds; these are different from the normalized finite-box tail estimate. |
| Recent arXiv | `site:arxiv.org "lattice points" "concentration" after:2021-10-27 before:2026-10-28` | Niksiński2608.17302, submitted2026-08-18, primary abstract16–18: concentration in symmetric discrete convex bodies; related, not exact anisotropic box bound. |
| Supplementary primary probability | Hoeffding1963, *Probability Inequalities for Sums of Bounded Random Variables*, JASA58(301),13–30 | Primary PDF fetched,19pages but0 extractable lines; screenshot yielded locator only. No claim to have inspected its theorem text. This motivates a concentration route, not an exact source verification. |
| Supplementary primary Diophantine probability | Adiceam–Shirandami, *Probabilistic effectivity in the Subspace Theorem*,2026, abstract/introduction | Different problem: densities of algebraic vectors and approximation solutions. It does not supply Lemma8. |

[Web requests1](../evidence/Roth.card_filter_weight_le/web1-metadata.json), [2](../evidence/Roth.card_filter_weight_le/web2-metadata.json), [3](../evidence/Roth.card_filter_weight_le/web3-metadata.json), [4](../evidence/Roth.card_filter_weight_le/web4-metadata.json), [primary opens](../evidence/Roth.card_filter_weight_le/web5-metadata.json), [screenshot limit](../evidence/Roth.card_filter_weight_le/web6-metadata.json), [access failures](../evidence/Roth.card_filter_weight_le/web7-metadata.json), [explicit nCatLab queries](../evidence/Roth.card_filter_weight_le/web8-metadata.json), [local exact source](../evidence/Roth.card_filter_weight_le/local-literature.txt).

The exact standard identified is the elementary lattice estimate used in the Diophantine Roth proof, not Roth's theorem on arithmetic progressions. The manuscript uses ordered m-tuples; arbitrary finite indexing is equivalent relabelling. Probability language offers a different organizational entry point and potentially stronger bounds. No reviewed source establishes that the weak2√m/λ expression should itself be the primary probability API.

## Phases 4a–4b — Generality and verified guards

| Parameter / hypothesis | Exact role | Weakening result |
|---|---|---|
| m:ℕ | Number of finite coordinates and dimension of induction | Already allows0, stronger than manuscript m≥1. Replacing dimension by arbitrary real loses the tuple interpretation. |
| r:Fin m→ℕ | Integral coordinate lengths and denominator weights | ℤ-vector coordinates with0≤d are equivalent representation. Real side lengths with floor modify both distribution and centering, not a mechanical weakening. |
| hr:∀j,0<r j | Every normalized coordinate has a nondegenerate positive denominator | **Essential**: dropping/weakening to nonnegative fails at m=9,r≡0,λ=9. Cardinality1 exceeds2/3. Native counterexample compiled. |
| λ:ℝ | Arbitrary real deviation parameter | No field typeclass to mechanically weaken; sqrt and project parent weight are fixed real interfaces. A new ordered sqrt field formulation would be another development. |
| hλ:0<λ | Positive tail threshold and denominator | **Essential**: λ=0,m=0 makes LHS1,RHS0. Native counterexample compiled. Negative λ likewise cannot give a valid general count bound. |
| Fin m | A fixed finite enumeration | Arbitrary universe-polymorphic Fintype σ version **compiled**, using equivFin, a Finsupp equivalence, weight transport, filtered-card equivalence and product transport. This is a new proof, not a dropped unused premise. |
| Classical decisions | Local classical proof implementation | No user-visible DecidablePred/DecidableEq argument in original; the accepted arbitraryσ function formulation carries `[DecidableEq σ]` because its piFinset expression needs equality decisions while elaborating the statement. A classically scoped alternative was not tested. |

**Fixed-parent-interface verdict: MAXIMALLY GENERAL** for the original hypotheses; no proposed premise deletion survives the checked guards. **Expanded representation:** arbitraryσ and a function `piFinset` formulation are verified transports, not assumed definitional equality and not an existing mathlib replacement. The full expanded statement and original recovery are in the accepted source. [Guards](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-guards-final-executed.lean.txt), [finite transport](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-finite-index-clean-executed.lean.txt), [function representation](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-function-box-final-executed.lean.txt).

## Phase 4c — All nine modern-idiom questions

| # | Applies? | Diagnostic / proposed reformulation | Concrete downstream consequence |
|---|---|---|---|
|1 Typeclass preambles | no | Positive r and λ are value premises, not new structures needing global instances. | Avoid parameter-specific instance API. |
|2 Filters/nets | no | Finite count, no convergence or neighborhood argument. | None. |
|3 Universal property | no | Inequality about an existing finite box, no object construction. | None. |
|4 Bundled substructures | no | A bounded box is not a submodule or subgroup; closure is false. | Fintype.piFinset/finite intervals are the appropriate containers. |
|5 Algebraic hierarchy | no mechanical weakening | Parent weight is real-valued; sqrt and ordered division used essentially. | Rebuilding a scalar-parametric parent API is not an unused-instance edit. |
|6 Higher categories | no | No categorical structure participates in the count. | None. |
|7 Concrete index | yes, finite indexing | Arbitrary Fintype σ replaces Fin m; compiled transport. | Applies to product/subtype coordinate types with Fintype.card and Fintype.prod_equiv, avoiding manual re-enumeration at each use. |
|8 Concrete-via-abstract | yes, representation diagnostic | Original driver has zero literal `box`/`weight` occurrences after the signature and delegates to private helpers. Inspecting their bodies shows the input structure is bounded tuples plus normalized finite sums; accepted function-box bridge removes both project aliases. | Uses existing Fintype.piFinset, Finset.filter_map/card_map and ordinary sums. This is not license to ignore the helpers' nontrivial mathematics. |
|9 False-generalization guard | no for relabelling/function bridge; yes for dropping positivity or arbitrary distributions | Verified roundtrip preserves the same lattice vectors and bound. Degenerate side bounds are refuted; arbitrary dependent distributions require independence and expectation assumptions. | Prevents silently replacing box uniformity by unrelated random variables. |

Modern idiom available: **yes as an expanded API design**, not yet a mechanically approved premise weakening. A direct `piFinset` law avoids introducing the already redundant `Roth.box`/`weight` definitions upstream. A stronger product-measure tail theorem is a separate candidate design. These organize actual finite-product probability/counting uses, rather than adding abstraction merely for appearance.

## Phase 4.5 — Infrastructure risks

n/a — theorem. Typeclass diamonds, reducibility leak, noncanonical unfolding, instance priority collisions, universe-polymorphism definitions and coercion ambiguity are all definition/instance infrastructure checks. This declaration introduces no definition, instance or coercion. The proposed arbitraryσ statement is actually universe-polymorphic in the native proof.

## Phase 4.6 — Five proof-strategy rows

| # | Question | Result / alternative |
|---|---|---|
|1 Topology ε–δ versus filters | n/a: no topology argument. |
|2 Element algebra versus substructure inclusions | n/a: sums of tuple coordinates are essential; no invariant algebraic substructure. |
|3 Sequences versus nets | n/a: finite sums and induction, no limits. |
|4 Constructed categorical object versus universal property | n/a: no categorical construction. |
|5 Missing reusable helpers | yes: the main missing reusable unit is the finite-product lower-tail estimate, not cardinality of the box itself. Last-coordinate sections and reflected reciprocal sums are separate candidate API questions; existing generic fibre counting already handles abstract cardinal splitting. |

**REFACTOR-RECOMMENDED for upstream packaging**, not a claim that the native induction is wrong. Keep the elementary induction if selecting the direct counting API; state it on the chosen canonical finite-product representation. Alternatively use existing Chebyshev/product variance/Popoviciu machinery after proving uniform-box moment and count-to-measure bridges. No complete specialization from those probability lemmas to the lattice count is claimed. New bridge/moment proofs are not three-call compositions.

## Phase 5 — Five actual methods × three forms

| Method | Current Fin/Finsupp form | Literature tuple count | Abstract concentration form |
|---|---|---|---|
| Lean-Finder | Normalized box weight count query; unrelated Behrend/AP Roth hits | Exact2√m/λ tuple query; corners/Szemerédi/Behrend hits, all excluded | Chebyshev and variance lemmas found |
| Loogle | `Finset.card, Real.sqrt` no hits | `Finset.filter, Finset.card, (2 : ℝ), Real.sqrt` no hits | `ProbabilityTheory.variance, MeasureTheory.Measure` finds variance/variance_nonneg/covariance partial API |
| LeanSearch | Lattice weighted count; Behrend and asymptotic ZLattice hits excluded | Rectangular box normalized sum; ZLattice asymptotics/geometry-of-numbers excluded | `meas_ge_le_variance_div_sq`, `IndepFun.variance_sum` found |
| rg pinned mathlib | Full qualified-name and weight/filter/sqrt patterns no exact matches | Untruncated lattice count/Behrend source search; different estimates | Pinned exact variance/uniform names and signatures inspected |
| Local name-pattern tool | card_filter_weight_le returns project target and scratch replays, excluded | card_filter returns genuine `Finset.card_filter` plus project scratch copies | variance_sum returns genuine pinned variance source lemmas |

All three local responses report index unavailable; positive results were source-checked, and empty responses do not establish absence. External indexes may have different revisions. Complete exact requests/responses are preserved in the formal-search files; pinned source searches are untruncated. [Current](../evidence/Roth.card_filter_weight_le/search-current.json), [literature](../evidence/Roth.card_filter_weight_le/search-literature.json), [abstract](../evidence/Roth.card_filter_weight_le/search-abstract.json), [local current](../evidence/Roth.card_filter_weight_le/local-current.json), [local literature](../evidence/Roth.card_filter_weight_le/local-literature.json), [local abstract](../evidence/Roth.card_filter_weight_le/local-abstract.json), [pinned signatures](../evidence/Roth.card_filter_weight_le/mathlib-candidates.txt).

Pinned positive candidates were natively `#check`ed. A named Chebyshev application compiles mathlib-only with standard axioms; it proves exactly the probability theorem's own form. The isolated original-expanded and arbitrary finite function-box `exact?` guards record bounded nonclosure only: `fail_if_success` suppresses the inner reason, so this evidence does not distinguish no hit from search resource exhaustion. Target guard `#check_failure Roth.card_filter_weight_le` prevents importing the project's own theorem. [Direct probes](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-direct-search-clean-executed.lean.txt), [probability proof](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-probability-named-executed.lean.txt).

Conclusion: **partial matches and reusable infrastructure**, no independently verified exact existing theorem or≤3-call derivation. This is not an absolute proof of absence.

## Phase 5.5 — Statement shape

Normal-form alternatives: (a) filtered Finsupp box cardinality, (b) filtered function piFinset cardinality, (c) proportion of a dependent finite tuple type, (d) lower-tail measure of a sum under uniform product measure. Native relabelling and function-box recovery actually compile. Mathlib already supplies containers/weights/sums and probability notions, but no verified canonical theorem for this precise bound. Proposed counting normal form is the function `Fintype.piFinset` statement with ordinary finite sum; proposed probability alternative should instead expose a standard centered tail estimate. RHS convention is n/a for an inequality rather than an equivalence; no parallel web of pairwise equivalences is proposed.

Syntactic generality: original explicit m,r,hr and implicit λ works directly at the one caller. Arbitraryσ is easier for non-Fin coordinate types; function-box bridge is verified both ways for the existing caller representation. Do not replace the≤event by a strict event without proving the integer boundary treatment. No uniform project-wide coordinate conversion is necessary to retain the local corollary.

Superfluous-argument audit: m indexes both domain and threshold (essential); r sets support/normalization (essential); hr is essential by m9 guard; λ and hλ essential by m0/λ0 guard. No original explicit typeclass is unused. **RESTATEMENT BEFORE UPSTREAM SHIP** means choosing the public representation; it does not mean an unsupported weakening has been found.

## Phase 6.0 — Callers and inline audit

**1 explicit source occurrence outside declaration;1 caller file.**

| Caller | Use and migration plan |
|---|---|
| `Roth/MainLemma.lean:574`, private `mul_card_filter_weight_le_aux` beginning569 | Apply λ=4a√m, multiply the count by a, cancel positive factors to get half the total count. A future function-box API uses the verified card bridge at this site; retain current sign split, multiplication monotonicity and arithmetic normalization. |

[Exact caller table](../evidence/Roth.card_filter_weight_le/explicit-callers.json), [source search](../evidence/Roth.card_filter_weight_le/rg-callers.json), [inline audit](../evidence/Roth.card_filter_weight_le/rg-inline.json). No separate inline rederivation was found. Private induction lemmas prove cases of the theorem, not duplicate alternative public estimates. The canonical direct consumer agrees with the sole source caller. This is live API on the path through the auxiliary polynomial count to Roth's main lemma; one use alone does not make a real induction a wrapper.

Root replayed the exact original theorem using the three existing private Lattice helpers via actual constant-access elaborators, then replayed the complete actual MainLemma consumer replacing only the target call. Both compile with standard axioms. [Actual proof and caller](../evidence/Roth.card_filter_weight_le/card-filter-weight-le-actual-executed.lean.txt).

## Phase 6 — Composition experiments

1. `Finset.card_filter_le` plus box cardinality gives count≤total; after arithmetic this proves only λ≤2√m. It misses precisely the nontrivial large-deviation regime. Cannot discard that regime, which is used by the consumer.
2. `Finset.card_eq_sum_card_fiberwise` decomposes by the last coordinate; it does not supply the induction bound, λ′ positivity or reciprocal sum. The actual replay uses project private lemmas containing those new proofs, so those are not mathlib building blocks.
3. Probability route has existing `ProbabilityTheory.meas_ge_le_variance_div_sq` (Variance398), `variance_sum_pi`(449), `variance_le_sq_of_bounded`(501) and `PMF.toMeasure_uniformOfFintype_apply`(Uniform301). To reach the lattice count still requires moment/expectation formulas, uniform-product identification, event containment, real/ENNReal conversion and numerical bound. Pinned signatures and Chebyshev application are checked; **no complete specialization** to original count is asserted.
4. Expanded arbitraryσ/function-box bridge succeeds **using the original project theorem**. It is a positive representation experiment, not a mathlib-only proof and not evidence for either NO bucket. The actual bridge unfolds the aliases, rewrites `Finset.filter_map`/`card_map`, then normalizes with `simpa`; these are new representation proofs. Even a closing `simp [defs]` would be Phase6b borderline glue, not automatic NO-composable.

**NOT-COMPOSABLE on the verified evidence**: no≤3 existing mathlib-call derivation was produced. Parent box's earlier NO-composable verdict is not inherited; the dependent theorem is a substantive count estimate. Earlier BORDERLINE analytic/fibre assessments are context, not inherited reasoning.

## Phase 7 — Verdict and actionable design questions

**BORDERLINE-needs-human**, verification unresolved[]. The exact manuscript and actual caller support keeping the result. Guard tests prove that neither original positivity premise can simply be removed. A correct arbitrary finite function-box form and original recovery compile, but the exact upstream endpoint still requires selecting the public API. Existing concentration infrastructure is a serious alternative, and the weak2√m/λ bound should not be declared the canonical probability interface merely because it fits this one Diophantine proof.

1. Should mathlib expose the direct arbitrary-Fintype `piFinset` normalized lower-tail cardinality bound as a reusable finite combinatorics theorem, with the2√card/λ bound named explicitly?
2. Should the primary upstream theorem instead be a stronger centered product-measure tail estimate, with this weak lattice bound retained as its downstream/local corollary after the uniform-box moment bridge is proved?
3. If selecting the direct count API, should it live in a new `Mathlib/Combinatorics/Enumerative/LatticeCount.lean`, and should the reflected reciprocal-sum/fibre implementation remain private there, respecting the earlier BORDERLINE helper assessments?

Next action: retain `Roth/Lattice.lean` and its one MainLemma call while deciding these concrete upstream API questions; then run `/generalise Roth.card_filter_weight_le` against the chosen representation and `/cleanup Roth/Lattice.lean Roth.card_filter_weight_le` before any PR. This assessment neither applies that refactor nor opens a PR. A YES-specific PR title/reviewer/grouping is n/a for this verdict. The accepted YES history was consulted rather than inferred from helpful lemma names. No cost premise determined the verdict.

## Phase 8 — Evidence status

All required phases are PASS or the justified theorem infrastructure n/a. Accepted native sources, raw receipts, rejected attempts separately labeled, exact source/pin hashes, canonical order and independent build are in the portable ledger. [Assessment](../evidence/Roth.card_filter_weight_le/assessment.json), [verification ledger](../evidence/Roth.card_filter_weight_le/verification.json), [portable validator](../evidence/Roth.card_filter_weight_le/validate.py). Root acceptance remains pending until independent integration review.
