# Roth.normOne_add_le — full mathlibable assessment

Verdict: **BORDERLINE-needs-human**. The integer-polynomial spelling is useful local API; the reusable upstream design is a generic subadditive Finsupp support sum or a compatible L1 structure. Fresh checks prove both the direct common-support route and an L1 metric route, but neither supplies a replacement using at most three existing mathlib calls without new bridge work. Three concrete future API choices are recorded below; this read-only assessment is complete and needs no user answer to finish.

## Phase 0 — baseline and identity

Declaration 82/293 is the public theorem at `Roth/CoeffNorm.lean:77–83`. The entire module and its sole explicit caller were read. The module develops coefficient length and its Hasse derivative, determinant, diagonal and evaluation estimates for Roth's theorem. Baseline `lake build` succeeds with 2467 jobs; all 17 source/pin hashes freshly match the shared baseline manifest. The target contains no sorry, debug option or raised limit. [Baseline](../evidence/Roth.normOne_add_le/baseline-build.txt), [inputs](../evidence/Roth.normOne_add_le/inputs.json), [hash gate](../evidence/Roth.normOne_add_le/input-hash-check.json), [module](../evidence/Roth.normOne_add_le/source-module.lean.txt), [canonical order](../evidence/Roth.normOne_add_le/canonical-order.json).

## Phase 1 — exact mathematical content

For two integer multivariate polynomials in any set of variables, the sum of absolute values of the coefficients of their sum is at most the sum of their coefficient lengths. Coefficients absent from one polynomial contribute zero. Put all three finite sums over the union of the two supports, apply the real absolute-value triangle inequality coefficientwise, and distribute the sum over addition.

Full native type (from the actual target print, with implicit section binder restored):

```lean
∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ),
  Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q
```

Parameters: arbitrary universe-polymorphic variable type `σ`, and the two polynomials `P,Q`. No finiteness, degree, positivity, nonzero or coefficient-bound hypotheses. Integer coefficients and real-valued absolute sum are fixed by parent `Roth.normOne`, not theorem typeclass hypotheses that can simply be deleted. The proof uses project support-padding three times, finite-sum additivity/monotonicity and `abs_add_le` after coefficient/cast normalization.

## Phase 2 — preliminary checks

**SMALL**: elementary coefficient-length triangle law, neither a new mathematical structure nor a main named/person theorem. Literature width remains exhaustive. One-line definition-only test: **n/a, theorem**; its seven proof lines do not invoke definition exemptions or justify automatic inherited triage.

## Phase 3 — exhaustive literature

All actual exact requests, returned-response hashes/byte counts, locators and concise original summaries are preserved. Full returned article/search bodies are not archived. URLs with query parameters are sanitized; no signed credentials are retained. The optional `ask_chatgpt_math` consultation on standard form, generality and historical evolution is **n/a: unavailable**.

| Channel | Exact query/access | Result and scope |
|---|---|---|
| General web, specific | `polynomial coefficient l1 norm triangle inequality sum absolute coefficients` | Identifies coefficient lp norms and finite vector l1 triangle inequality. |
| General web, general | `finitely supported functions l1 norm triangle inequality subadditive sum` | Finite support needs no summability/convergence premise. |
| General web, aliases | `coefficient length polynomial norm sum absolute values triangle inequality` | Coefficient l1 is polynomial length; distinguish height and integral norms. |
| Mathematical ChatGPT MCP | Standard form/generality/historical evolution consultation | n/a: `ask_chatgpt_math` unavailable. |
| Local reference | Actual rg and `clean.tex:437–497` | Lemma 3 proof explicitly introduces coefficient absolute sum and uses the triangle estimate, including scalar multiples. |
| nLab | `site:ncatlab.org/nlab l1 norm triangle inequality`; direct norm/p-norm and normed-vector-space pages | Indexed norm/p-norm contexts; direct norm and p-norm fail 400 unsupported XHTML; initial plus URL 404 and encoded-space retry inaccessible. No inaccessible body inferred. |
| nCatLab | `site:ncatlab.org/ncatlab norm triangle inequality`; direct homepage | Search returns mostly nLab adjacent material; homepage inaccessible. This finite sum estimate has no needed categorical construction. |
| Stacks | `site:stacks.math.columbia.edu norm triangle inequality polynomial` | No useful exact hit. Exploratory tag 0E8Q is unrelated glueing-in-closed-fibres material and excluded as evidence. No scheme hypotheses belong here. |
| MathOverflow | `site:mathoverflow.net polynomial sum absolute coefficients norm` | Question 465899 explicitly uses the coefficient-vector l1 norm of integer polynomials; adjacent use rather than proof authority. |
| Recent arXiv, actual five-year window | `site:arxiv.org polynomial coefficient l1 norm triangle inequality after:2021-10-27 before:2026-10-28` | August 2026 paper 2608.20790 studies coefficient lq comparisons; nearby circle integral norm hits concern a different object. No new hypothesis for this law. |
| Supplementary primary access | NIST DLMF 1.2 and arXiv 2608.20790 metadata | DLMF 1.2.45–52 provides real/complex finite lp norms and triangle inequality; arXiv metadata confirms date and coefficient comparison scope. |

[NIST DLMF §1.2(v), equations 1.2.45–52](https://dlmf.nist.gov/1.2#v) gives the standard finite vector norm and triangle inequality. The coefficient polynomial specialization is an inference using a common finite support, not a claim that DLMF names this Lean theorem. [Han–Kim–Seoane-Sepúlveda, Classical polynomial inequalities for quadratic forms on an octagonal sector](https://arxiv.org/abs/2608.20790) concerns sharp coefficient comparisons, not a new basic triangle inequality. The local primary manuscript directly supplies the intended coefficient length use.

Sources agree on coefficient l1, also called length. Real/complex coefficient vectors and arbitrary finite support are broader standard forms; replacing coefficient l1 by circle integral L1, max coefficient height or Mahler measure changes the object. No historical evolution of this elementary law is established by these searches. The most useful algebraic abstraction aggregates an indexed subadditive size over finitely supported coefficients; norm-specific properties beyond subadditivity are unnecessary.

Evidence: [web 0](../evidence/Roth.normOne_add_le/web-0.json), [web 1](../evidence/Roth.normOne_add_le/web-1.json), [web 2](../evidence/Roth.normOne_add_le/web-2.json), [web 3](../evidence/Roth.normOne_add_le/web-3.json), [web 4](../evidence/Roth.normOne_add_le/web-4.json), [web 5](../evidence/Roth.normOne_add_le/web-5.json), [web 6](../evidence/Roth.normOne_add_le/web-6.json), [web 7](../evidence/Roth.normOne_add_le/web-7.json), [local excerpt](../evidence/Roth.normOne_add_le/local-literature.txt), [local hash](../evidence/Roth.normOne_add_le/local-literature-source.json), [local search](../evidence/Roth.normOne_add_le/rg-local-literature.json).

## Phase 4a — all parameters and hypotheses

| Component | Current form | Expanded representation and reason |
|---|---|---|
| `σ : Type*` | Arbitrary variables, no typeclass | Already unrestricted; abstract Finsupp can replace exponent vectors by any index `ι`. |
| `P,Q` | Two integer multivariate polynomials | Coefficient Finsupp `f,g` need `AddZeroClass M`; multiplication/commutativity of addition is unused. Both objects remain essential. |
| Coefficients | Fixed integers within parent interface | Abstract additive coefficients permit coordinate size functions; no ring multiplication, division or order on coefficients is required. |
| Output | Fixed real numbers | `AddCommMonoid N`, `Preorder N`, `IsOrderedAddMonoid N` support finite aggregation/monotonicity; partial/linear order and field laws are unnecessary. |
| Size | Absolute value of real integer cast | Indexed `size : ι → M → N` with coordinatewise subadditivity; zero preservation gives the exact support-padding proof. |
| Zero condition | Absolute value sends 0 to 0 | A further expanded form can require only nonnegativity at 0, by zero-truncating size on zero coefficients; this is separately tested, not assumed. |
| Additional hypotheses | None | No theorem premise to drop. Finite support is built into polynomial/Finsupp, not finite variable type. |

## Phase 4b — generality status

**MAXIMALLY GENERAL at the fixed parent interface**: arbitrary `σ` and no theorem hypotheses to weaken. Expanded Finsupp representations expose actual broader mathematics; their fresh successful checks are the mechanical evidence rather than guesses. These are new helper proofs, not existing mathlib replacements. A possible upstream form should use `Preorder`, not unnecessarily require `PartialOrder`. Exact zero-preservation is sufficient for support padding; it is not necessary for all subadditive support sums. The strictly broader nonnegative-at-zero theorem also compiles: zero-truncate size, prove its subadditivity, and observe support sums are unchanged. Constant size 1 gives support cardinality and verifies that strict expansion. No claim of class-minimality or absolute maximal generality is made. [Generic/direct source](../evidence/Roth.normOne_add_le/native-target-executed.lean.txt), [generic/direct receipt](../evidence/Roth.normOne_add_le/native-target-success.json), [broader generality and consumer source](../evidence/Roth.normOne_add_le/native-consumers-generality-executed.lean.txt), [receipt](../evidence/Roth.normOne_add_le/native-consumers-generality-success.json).

## Phase 4c — all nine modern-idiom rows

| # | Question | Result and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | No explicit bundled hypotheses to convert; expanded coefficient/output interfaces use standard classes. |
| 2 | Metric versus filters | No convergence; finite support computation does not benefit from filters. |
| 3 | Construction versus universal property | No object construction in this theorem; no universal-property class is needed. |
| 4 | Bundled substructure | No closure predicates or subobject lattice; not applicable. |
| 5 | Hierarchy weakening | Yes after representation expansion: `AddZeroClass M` and ordered additive output suffice; no ring, field, scalar multiplication or completeness. |
| 6 | Higher category | No categorical statement; no justified categorification. |
| 7 | Concrete index | `σ` already arbitrary; coefficient exponent index can become arbitrary `ι`, useful for Finsupp weights, coefficient sizes and support cardinality. |
| 8 | Concrete-via-abstract diagnostic | Fires: three body lines mention `normOne_eq_sum_of_support_subset` inside the first `rw` command; zero named-parent occurrences follow that command. Only coefficient addition/cast and `abs_add_le` remain; no multiplication/degree reasoning. Replacing all padding calls by generic Finsupp padding yields the same finite-sum proof. |
| 9 | False-generalization guard | Abstract size-subadditivity recovers precisely the original coefficient triangle law; no multiplicativity/norm definiteness is invented. Max height, integral L1 and arbitrary norms on polynomial functions are different objects. The metric-only WithLp Finsupp instance must not be mislabeled a bundled normed group. |

Modern idiom: a generic Finsupp support-sum subadditivity API or a compatible L1 bundle can organize this proof. The concrete benefit is sharing the addition proof across coefficient types and sizes, then supplying the subadditivity witness to `Finset.le_sum_of_subadditive`; it is not cosmetic categorification. Cost is a sequencing observation only, never the verdict criterion.

## Phase 4.5 — infrastructure risks

n/a: theorem introduces no definitions, classes, instances or coercions. All six definition-specific risks—typeclass diamonds, reducibility leaks, noncanonical unfolding, priority collisions, universe infrastructure and coercion ambiguity—are inapplicable. Proposed future L1 bundles would require their own infrastructure audit; no instance is installed by this assessment.

## Phase 4.6 — five proof-strategy rows

| # | Strategy question | Answer |
|---|---|---|
| 1 | ε–δ versus filters | No topology/convergence argument. |
| 2 | Elements versus subobject inclusions | Coordinatewise addition is intrinsic; ideal/submodule inclusions do not express this quantitative estimate. |
| 3 | Sequences versus nets | No limits. |
| 4 | Construction versus universal property | No construction. |
| 5 | Missing helpers that should exist | Generic support-sum subadditivity is a candidate API improvement; exact additive Finsupp sum law exists but does not apply to absolute value. A metric bridge is examined separately. |

Strategy: **REFACTOR-RECOMMENDED for upstream design**. Prefer one reusable Finsupp size law or compatible L1 API over exporting an integer-polynomial-only proof. Current common-support proof is mathematically direct. The helper question remains upstream API design; the assessment does not disguise a newly proved helper as one existing mathlib call.

## Phase 5 — all five actual search methods × three forms

| Method | Current coefficient norm | Literature l1/length | Abstract indexed subadditive sum |
|---|---|---|---|
| Lean-Finder | Mahler coefficient-sum bound and unrelated polynomial results | Norm sum bounds and PiLp L1 coordinate norm formula | `Finset.le_sum_of_subadditive`, `Finsupp.sum_le_sum`, `sum_le_sum_index` |
| Loogle | Two invalid placeholder/identifier attempts retained; quoted successful retry gives coefficient family | Exact `norm_add_le` | Finsupp sum inequality pattern returns no hit |
| LeanSearch | Absolute value/sum triangle building blocks | `norm_sum_le` and nnnorm bounds | Generic finite subadditivity and Finsupp sum monotonicity |
| `rg` pinned source | No mathlib `normOne_add_le` spelling | Norm/lp source inspected; polynomial norm file defines sup rather than coefficient L1 | Exact additive sum law, support padding and Finsupp order inequalities |
| Local name search | Project-specific add name | Norm-add family | No sum-add inequality hit; index explicitly unavailable, so this is not absence evidence |

[Formal receipts](../evidence/Roth.normOne_add_le/formal-search.json), [current rg](../evidence/Roth.normOne_add_le/rg-current.json), [literature rg](../evidence/Roth.normOne_add_le/rg-literature.json), [abstract rg](../evidence/Roth.normOne_add_le/rg-abstract.json), [full-name rg](../evidence/Roth.normOne_add_le/rg-full-name.json). External indexes can differ from the pinned mathlib revision. Failed searches are retained and never treated as proofs of absence.

Pinned candidates: `Finsupp.sum_of_support_subset` handles arbitrary zero-preserving sizes; `Finsupp.sum_add_index'` needs **equality** `size(a+b)=size a+size b`, which absolute value does not satisfy. `Finsupp.sum_le_sum` compares two summands on the same fixed support; `sum_le_sum_index` needs monotone sizes and an ordered coefficient domain, whereas absolute value is not monotone on integers. `Finset.le_sum_of_subadditive` is the finite-sum extension and requires the very triangle witness under assessment. Generic `norm_add_le` needs the correct `SeminormedAddGroup`, so it is not an unchecked replacement for `Roth.normOne`. `WithLp 1` Finsupp supplies metric structure; representation/addition-distance normalization requires actual work. PiLp L1 needs a finite coordinate type, obtainable only after choosing a common finite support, so its presence alone does not close the old interface.

Sources: [Finsupp sums](../evidence/Roth.normOne_add_le/mathlib-finsupp-basic.lean.txt), [Finsupp order](../evidence/Roth.normOne_add_le/mathlib-finsupp-order.lean.txt), [Finsupp lp metric](../evidence/Roth.normOne_add_le/mathlib-lp-finsupp.lean.txt), [polynomial norm](../evidence/Roth.normOne_add_le/mathlib-norm.lean.txt), [norm triangle](../evidence/Roth.normOne_add_le/mathlib-norm-group.lean.txt), [coefficient representation](../evidence/Roth.normOne_add_le/mathlib-monoid-algebra.lean.txt), [pinned hashes](../evidence/Roth.normOne_add_le/mathlib-inputs.json).

## Phase 5.5 — three statement-shape checks

Normal form: `normOne (P+Q) ≤ normOne P + normOne Q` is correctly oriented and natural as a subadditivity witness. Finsupp normal form expands coefficient aggregation without changing addition; a metric triangle form encodes distances to 0 and needs the proper bridge.

Syntactic alternatives actually prepared/tested: original replay; direct generic support-padding proof; indexed Finsupp size form; nonnegative-at-zero variant; WithLp 1 metric triangle. The original is easiest at `Finset.le_sum_of_subadditive`; a generic size form is easier for upstream reuse. Superfluous-argument check: `σ`, `P` and `Q` all specify objects in the conclusion; no theorem class/premise is unused. Expanded output only needs preorder, not partial order. **SHIP-AS-STATED locally**; any upstream addition should restate against the chosen generic interface first.

## Phase 6.0 — all callers and inline audit

Exactly one explicit occurrence beyond the declaration, one named caller, no caller outside the declaring file:

| Caller | Use | Concrete refactor plan |
|---|---|---|
| `Roth.normOne_sum_le`, `CoeffNorm 90–92` | Passes `normOne_add_le` as the binary subadditivity witness to `Finset.le_sum_of_subadditive` | Replace that witness by the complete fresh `NormAddAssessment.direct` proof inline if removing the helper, or by specialization of a separately accepted future Finsupp size law. Retain `normOne_zero.le` and the finite-sum theorem. Full consumer replay is required and recorded. |

The inline rg also finds `Roth/HasseDeriv.lean:163` using support-add padding for binomial algebra, not an independent coefficient triangle derivation. No other complete triangle proof is rederived inline. This is useful local API, and one caller does not establish dead code or justify deletion without a refactor.

Source occurrence counts are not kernel/simp dependency closure. The fresh native 293-value direct-proof audit checks all canonical written values, including private and LeanEval declarations: requested 293, present 293, values 293, sole direct consumer `Roth.normOne_sum_le`. No additional direct implicit/simp consumer was found among those 293 values. This does not recursively inspect opaque/generated helper bodies or quantify external users. Full replacement consumer replay succeeds with standard axioms. [Caller rg](../evidence/Roth.normOne_add_le/rg-callers.json), [inline rg](../evidence/Roth.normOne_add_le/rg-inline.json), [caller/dependency scope](../evidence/Roth.normOne_add_le/callers.json), [fresh consumer and audit receipt](../evidence/Roth.normOne_add_le/native-consumers-generality-success.json).

## Phase 6 — actual composition experiments

Original support-padding replay and replacement using only mathlib support-padding are checked independently. Exact integer coefficient addition representation is definitional (`AddMonoidAlgebra.coeff_add` is rfl); the L1 metric bridge is not definitional. The direct proof uses three support-padding calls, `Finset.sum_add_distrib`, `Finset.sum_le_sum`, `abs_add_le`, and cast normalization—more than three existing mathematical calls. Its short source layout does not make it a composition using at most three existing calls.

The generic zero-preserving Finsupp lemma is a **new proof** with the same finite-support bookkeeping. Specializing this freshly proved helper is not a valid NO-composable witness. `norm_add_le` without a matching normed-group instance is insufficient. The metric route successfully synthesizes `MetricSpace (WithLp 1 (ι →₀ ℤ))` and successfully checks failure of the corresponding `SeminormedAddCommGroup` inference. Fresh `zeroDistance` and `addDistance` prove zipWith/mapRange equality by extensionality, simplify rpow at 1 and use `Finsupp.sum_mapRange_index` plus `Int.norm_eq_abs`. A final `dist_triangle` application then yields the inequality. Those two new bridge lemmas are actual work, not existing mathlib calls. Merely printing `dist_triangle` or normalizing the whole goal by `simp [defs]` would not by itself prove a claim of at most three existing calls (Phase 6b specifically treats trivial simp composition as BORDERLINE). [Metric source](../evidence/Roth.normOne_add_le/native-metric-executed.lean.txt), [full metric receipt](../evidence/Roth.normOne_add_le/native-metric-success.json).

The isolated mathlib-only proof uses exactly the stable 13 imports, guards `#check_failure Roth.normOne_add_le`, proves the generic law and specializes it to integer coefficient Finsupps, then proves the finite-sum caller. It imports no Roth module. This closes circularity concerns from the persistent project environment. [Raw source](../evidence/Roth.normOne_add_le/native-raw-executed.lean.txt), [raw receipt](../evidence/Roth.normOne_add_le/native-raw-success.json), [original replay](../evidence/Roth.normOne_add_le/native-original-executed.lean.txt), [original receipt](../evidence/Roth.normOne_add_le/native-original-success.json).

The parent `Roth.normOne` was NO-composable via Finsupp aggregation, not NO-has-it via a replacement parent carrying this law. Consequently **no Mode B parent re-aim override** forces a has-it result here. Declaration 78's historical triangle replay is context only and is not counted as fresh 82 native evidence. All native accepted/rejected sources and complete receipts are linked in the final verification record.

## Phase 7 — verdict and actionable plan

**Category: BORDERLINE-needs-human.** Literature confirms the standard coefficient l1 triangle law. The parent interface has no unused hypotheses, while fresh verified broader forms move the content to Finsupp indexed sizes, even nonnegative-at-zero sizes. All five searches locate building blocks and nearby generic norm APIs, but no checked one-line exact replacement. The direct route exceeds the ≤ 3-call composition bar. The metric route works only after freshly proving two representation/translation bridges; this is not evidence that the old spelling was already a one-line mathlib specialization. No blanket absence theorem is asserted by unsuccessful search.

The remaining judgment is API organization: should upstream add the generic algebraic inequality now, extend the newly present Finsupp Lp metric with compatible normed-group structure, or keep this finite coefficient convenience downstream until that structure is settled? These alternatives expose the same coefficient l1 content and different reuse paths. This is a mathematical-library design choice, not a cost-based downgrade. The one local caller favors a compact local helper, while the abstract support-sum and support-card tests show reuse beyond Roth. The existing polynomial sup norm is a different object and is not a substitute.

Concrete future upstream questions (no response required to complete this read-only report):

1. Add an indexed `Finsupp.sum_add_le` law to `Mathlib/Data/Finsupp/Order.lean`, with the broader nonnegative-at-zero form as primary API?
2. Prefer compatible L1 seminormed-group structure/translation-distance lemmas in `Mathlib/Analysis/Normed/Lp/Finsupp.lean`, so standard `norm_add_le` supplies this law after a checked coefficient bridge?
3. Keep `Roth.normOne_add_le` in `Roth/CoeffNorm.lean` until one of those upstream interfaces is chosen, then refactor the sole caller through the chosen general law?

Action now: preserve the local theorem and production sources. If the generic inequality route is chosen, start from the exact verified generic/nonnegative-at-zero source, run `/generalise Roth.normOne_add_le` and `/cleanup Roth/CoeffNorm.lean Roth.normOne_add_le`, and separately review upstream naming/zero assumptions. If deletion is chosen locally, replace the sole finite-sum witness by the entire direct proof; a replacement using at most three existing calls is not claimed. There is no unconditional YES PR grouping/reviewer requirement or NO deletion mandate for this BORDERLINE outcome. Alternative local destination remains the existing coefficient-estimate module.

## Phase 8 — verification and handoff

All five fresh accepted native sets return complete success, partial=false, no warnings/errors/failed dependencies and standard axioms only (`propext`, `Classical.choice`, `Quot.sound`). The first generality/consumer attempt was rejected solely for deprecated `if_pos`/`if_neg` warnings; its exact source and raw receipt remain separate, and the clean accepted retry uses `ite_eq_left/right`. Requested preparations are retained as preparations, not claimed executions. No extra axioms, placeholders, unsafe/native-decide proofs or raised limits are accepted.

The complete package contains [assessment](../evidence/Roth.normOne_add_le/assessment.json), [verification](../evidence/Roth.normOne_add_le/verification.json), [overview entry](../evidence/Roth.normOne_add_le/overview-entry.json), [generality record](../evidence/Roth.normOne_add_le/generality.json), [current copy manifest](../evidence/Roth.normOne_add_le/copy-manifest.json) and [portable read-only validator](../evidence/Roth.normOne_add_le/validate.py). Scratch and integrated evidence resolve the same report links; integration-added `root-acceptance.json` is exempt from worker inventory, while the current manifest is always validated. All 17 inputs, archive hashes/bytes, formal/literature channels, native scope/axioms and credential scan are checked. `completed=true`, all phases PASS or theorem-n/a, unresolved=[]; the three upstream taste questions are deliberate final recommendations, not unfinished verification. Root acceptance stays pending until independent review.
