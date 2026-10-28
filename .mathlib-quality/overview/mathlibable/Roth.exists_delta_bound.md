# Roth.exists_delta_bound — full assessment (canonical234)

**Verdict: BORDERLINE-needs-human. Assessment complete; root acceptance pending.**
The theorem has substantive fixed-m content. Generic neighborhood transport alone does not
replace the square-root gap calculation or positivity of the real-power exponent. Keep it in
`Roth/MainLemma.lean` pending a decision on a future upstream Roth module and the generic helper
boundary. No production, pin, Git, overview or progress file was changed by this worker.

## Phase 0 — Baseline and scope

Fresh hashes of all17 production sources/pins match the shared input manifest. The reusable
baseline succeeded with2467 jobs. The previously accepted file-end Theta228 build remains the
last required fullbuild checkpoint; no new file-end build is due at234 (next266).
The public theorem resolves at `Roth/MainLemma.lean:77–93`, with16 proof lines and no sorry or
resource option. The whole MainLemma module, the entire actual caller and its surrounding
Main module, and LeanEval downstream context were read. Native execution was exclusive to this
worker, with the nine persistent imports preserved.

Evidence: [fresh17](../evidence/Roth.exists_delta_bound/inputs.json),
[baseline](../evidence/Roth.exists_delta_bound/baseline-build.txt),
[original MainLemma](../evidence/Roth.exists_delta_bound/source-MainLemma.lean.txt),
[full Main](../evidence/Roth.exists_delta_bound/source-Main.lean.txt),
[LeanEval](../evidence/Roth.exists_delta_bound/source-LeanEval.lean.txt).

## Phase 1 — Statement and proof

For each fixed pair of natural numbers n,m with m>16n², there is a positive radius δ₀ such that
all δ in **the closed interval [0,δ₀]** satisfy δ<1/m and
10^m δ^((1/2)^m)+2(1+3δ)n√m<m/2. This is uniform in δ for the fixed m; the radius is not uniform
in m. Both endpoints matter. The actual consumer evaluates the bound at0 before choosing a
positive δ, using positivity of γ(0)-η(0) to justify continuity of a quotient.

Full native type (from Lean.getConstInfo with pp.funBinderTypes, not a split #print body):

```lean
∀ {n m : ℕ},
  16 * n ^ 2 < m →
    ∃ (δ₀ : ℝ), 0 < δ₀ ∧ ∀ (δ : ℝ), 0 ≤ δ → δ ≤ δ₀ → δ < 1 / ↑m ∧ Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2
```

Parameters: n is the natural polynomial-degree parameter (zero allowed); m is the fixed natural
dimension; hm is the strict dimension threshold. No section variables or extra typeclasses are
hidden. The proof derives 4n<√m and hence the strict gap2n√m<m/2; continuity of a positive
real power makes the full left side strictly below m/2 near0. Choosing half the minimum of
1/m and a neighborhood radius gives strict bounds even atδ₀.
Source-level mathematical project dependency: `Roth.eta`, in statement and body.
The filtered opaque kernel-body list also contains `Roth.eta._proof_1` and
`Roth.gam._proof_1`, generated proof constants; this does not mean a mathematical invocation of
the public `Roth.gam` API.

[Native type/dependencies](../evidence/Roth.exists_delta_bound/native-type.json),
[full target source](../evidence/Roth.exists_delta_bound/target-excerpt.lean.txt),
[original native receipt](../evidence/Roth.exists_delta_bound/original-receipt.json),
[filtered body constants](../evidence/Roth.exists_delta_bound/project-receipt.json).
The #print pretty-printer **elides**118836 body characters and part of the long all-constants
list; neither is claimed as a full kernel-body dump. The complete unchanged executed source,
full tagged kernel type, axioms and canonical value audit are retained.

## Phase 2 — Size and one-line definition check

BIG under the command's rule: exists_delta_bound is explicitly listed in MainLemma's
`Main results`. This framing does not imply a YES verdict. The one-line-definition check is
n/a because this is a theorem; its proof is16 substantive lines. No definition exemption is
being inferred from its arithmetic spelling.

## Phase 3 — Exhaustive literature protocol

Every named channel was attempted; the three general queries are distinct actual requests.
Receipts retain exact requests, returned UTF-8 response SHA256/byte count/status, clean returned
titles/URLs and original summaries, without article or search-result bodies.

| Channel | Exact query or locator | Outcome and limitation |
|---|---|---|
| General web, specific | Roth theorem "16n" "delta" continuity parameters | No exact fixed-m numerical lemma identified. |
| General web, general | positive power perturbation strict inequality continuity sufficiently small parameter neighborhood | Continuity/perturbation context, not an exact numerical replacement. |
| General web, aliases | stability of strict inequalities under continuous perturbations open set | Strict conditions persist locally; this identifies the topology mechanism. |
| ChatGPT math | standard form, generality, historical evolution | Justified n/a: ask_chatgpt_math unavailable. No reduced search elsewhere. |
| Local references | clean.tex:1211ff, Lemma lem:m-delta, eqs29/30; §7 eqs47–49 | Exact source for fixed-m parameter choice; Lean stronger closed interval includes0. |
| nLab | site:ncatlab.org/nlab continuity strict inequality neighborhood | continuous map/topology/neighborhood pages give open-preimage and neighborhood formulations. Direct continuous-map open failed due unsupported XHTML, recorded separately. |
| Distinct nCatLab | site:ncatlab.org/ncatlab continuous real function positive neighborhood | Returned only out-of-namespace nLab pages; no in-namespace hit. This is not evidence of absence. |
| Stacks | site:stacks.math.columbia.edu continuous functions open inverse image neighborhoods | Topology chapter and scheme applications, no numerical Roth estimate. Refined query also returned constructibility material. A guessed tag004B was unrelated2-Yoneda and rejected. |
| MathOverflow | site:mathoverflow.net Roth theorem small delta parameters continuity | Roth applications and unrelated additive Roth material; no exact parameter law. |
| Recent arXiv | site:arxiv.org Roth theorem formalization parameters small delta after:2021-10-28 before:2026-10-29 | Date-bounded query returned mostly unrelated material. Refined Diophantine query also executed; no exact numerical law established. |
| Supplementary web API | mathlib4 ContinuousAt eventually_lt exists Icc subset neighborhood Real rpow | Official mathlib source/docs confirmed the topology APIs; pinned signatures independently checked. |

[General requests](../evidence/Roth.exists_delta_bound/web-general.json),
[nLab](../evidence/Roth.exists_delta_bound/nlab.json),
[nCatLab](../evidence/Roth.exists_delta_bound/ncatlab.json),
[Stacks](../evidence/Roth.exists_delta_bound/stacks.json),
[Stacks refinement](../evidence/Roth.exists_delta_bound/stacks-refine.json),
[MathOverflow](../evidence/Roth.exists_delta_bound/mathoverflow.json),
[recent arXiv](../evidence/Roth.exists_delta_bound/arxiv.json),
[arXiv refinement](../evidence/Roth.exists_delta_bound/arxiv-retry.json),
[mathlib web API](../evidence/Roth.exists_delta_bound/web-api.json),
[direct primary-source access and failures](../evidence/Roth.exists_delta_bound/primary-crosscheck.json),
[local excerpt](../evidence/Roth.exists_delta_bound/local-excerpt.tex.txt),
[local search](../evidence/Roth.exists_delta_bound/local-literature.json).

Literature summary: the exact result is fixed-m parameter selection in Roth's proof. Its
reusable topological component is preservation of a strict inequality near a continuity point.
The modern formulation uses filters, with eventual truth converted to a closed right interval.
This is an inference combining the local numerical source with the general continuity principle,
not a claim that an external source names this exact helper. The source's explicit minimum uses
E/(12n√m), later1/(24n), in a context with n≥2. Those displayed entries are not all positive at
n=0 under Lean's totalized division. The continuity proof and verified n=0,m=1 case avoid that
restriction. The Lean note only asks an open positive interval; the theorem proves more.

## Phase 4a — Generality of every parameter and premise

| Parameter/premise | Current role | Verified alternatives / reason |
|---|---|---|
| n:ℕ | Nonnegative degree parameter, may be0 | No 0<n premise exists to drop. Generic perturbation proof accepts arbitrary real coefficients. Replacing the degree type throughout Roth is a semantic restatement, not an unused-class edit. |
| m:ℕ | Fixed dimension controls10^m, exponent, √m and1/m | hm already implies m>0. No separate NeZero/Fintype class to remove. Uniform radius for unbounded m is impossible because δ₀<1/m. |
| hm:16n²<m | Strict initial gap | Native sharp_iff proves the **entire conclusion iff hm**; cannot drop it or weaken to≤. |
| δ:ℝ | The varied parameter | Real powers/real square roots genuinely use the real analytic API. No claim of a generic field weakening. |
| 0≤δ≤δ₀ | Closed domain, conclusion guarantees strict bounds | Both0 andδ₀ verified. Restricting to positive/open δ would weaken what the caller needs at0. |
| coefficients10,3,2,1/2 | Fixed Roth numerical choices | Verified arbitrary C,D,b,r,a and p>0 form below. Constants become reusable semantic parameters; this is a new generic theorem, not just a notation change. |

## Phase 4b — Verified generality verdict

For the original fixed interface: MAXIMALLY GENERAL with respect to removable hypotheses;
zero mechanical weakening opportunities. `sharp_iff` is stronger evidence than syntactic usage:
atδ=0 the conclusion forces the exact threshold16n²<m. Equality n=1,m=16 fails; m=0 fails.

A verified broader numerical family is:

```lean
{a b C D p r : ℝ} → 0 < a → 0 < p → b < r →
  ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 ≤ δ → δ ≤ δ₀ →
    δ < a ∧ C * δ ^ p + b + D * δ < r
```

Its exact proof is `Delta234Generic.small_power_perturbation`, newly written in this assessment.
No signs are needed on C,D,b,r. Substitution C=10^m, p=(1/2)^m, b=2n√m,
D=6n√m, a=1/m, r=m/2 yields the original expanded conclusion **only after proving hm gives
b<r and normalizing the affine expression**. The mathlib-only original_expanded proof and
project generic_specializes bridge both passed. The p=0 guard disproves replacement of p>0 by
p≥0 in this arbitrary-coefficient schema. This semantic parameterization is not used to issue
an unsupported mechanical YES-but-generalise-first verdict. Cost is not a verdict factor. The small_continuous continuity premise is sufficient, not claimed minimal: the search also returned upper-semicontinuity APIs. The sharp/maximality claim here applies only to the original hm premise, not to generic topological assumptions.

[Isolated exact source](../evidence/Roth.exists_delta_bound/isolated-executed.lean.txt),
[isolated clean native receipt](../evidence/Roth.exists_delta_bound/isolated-receipt.json),
[project endpoints and sharp iff](../evidence/Roth.exists_delta_bound/project-executed.lean.txt).

## Phase 4c — Modern idiom, all nine rows

| # | Diagnostic | Answer, reformulation and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | No new structure: hm is value-level numerical information, not a canonical instance. |
| 2 | Metric notions to filters | Yes for proof organization: an eventually true predicate at0 transports through nhdsWithin and closed intervals. Existing Filter.Eventually.and and neighborhood bases compose with other constraints. |
| 3 | Universal property instead of construction | No algebraic or categorical universal property; existence of a small radius is ordinary local topology. |
| 4 | Bundled substructure instead of closure set | No subalgebra/submodule or closure predicate. Set.Icc is already the appropriate set API. |
| 5 | Typeclass hierarchy weakening | No explicit structure hypothesis to weaken; concrete real powers are essential. The generic continuous helper uses an arbitrary real function. |
| 6 | Higher categories | No categorical structure or meaningful higher analogue in this numerical lemma. |
| 7 | Concrete index generalization | The generic continuity transport works on ordered topological spaces in the existing interval theorem; the full positive-real-power family still uses ℝ. Natural m remains an actual dimension in Roth. |
| 8 | Concrete-via-abstract | Partial yes: eta occurs on2 body lines (continuity function and zero simplification); after its first unfolding there are0 eta lines. The tail only uses an eventual predicate. The prefix still proves a nontrivial square-root gap. Generic perturbation and its specialization were compiled. |
| 9 | False-generalization guard | Passed for the verified family and bridge. Rejected shortcut: supplying continuity/eventuality without proving the strict gap and positive exponent silently changes the premise. Dropping p>0 fails atp=0. |

[Concrete diagnostic](../evidence/Roth.exists_delta_bound/concrete-diagnostic.json).
Modern idiom is available as a reorganization, with concrete consequences: neighborhood filters
combine independent strict bounds; mem_nhdsGE_iff_exists_Icc_subset produces the closed interval
without an ad hoc half-radius calculation. These tools do not erase the numerical prefix.
Whether a separate positive-power convenience API is desirable remains the upstream question.

## Phase 4.5 — Infrastructure risks

Justified n/a for this theorem. All six risks were scoped: typeclass diamonds (no instance added),
reducibility leaks (no data definition added), noncanonical unfolding (only explicit eta use),
instance-priority collisions (no registration), universe constraints (concrete ℕ/ℝ proposition),
coercion ambiguity (no coercion introduced). This is not a six-row definition risk verdict.

## Phase 4.6 — Proof strategy, all five rows

| # | Question | Result |
|---|---|---|
| 1 | ε-δ versus filters | REFACTOR-RECOMMENDED for the tail: use existing closed-right-interval basis after an eventual conjunction. Original already uses ContinuousAt.eventually_lt correctly. |
| 2 | Elementwise algebra versus substructures | n/a: numerical inequality, no ideal/submodule inclusion. |
| 3 | Sequences versus nets | No sequence argument. Continuity at0 already uses the neighborhood filter. |
| 4 | Construction versus universal property | n/a: no categorical construction. |
| 5 | Helper mathlib should have | Possible arbitrary positive-power perturbation convenience lemma. Basic topology transport already exists; search did not establish a missing foundational theorem. |

The proposed strategy removes manual radius shrinking; its accepted generic proof still has to
establish the initial strict gap. This is a mathematical organization recommendation, not a
cost argument or an assertion that a new helper already belongs to mathlib.

## Phase 5 — All15 formal cells plus five supplementary power-form searches

All five actual methods ran on current, literature-standard, and abstract forms. Exact requests
and full raw formal responses are retained in `search-<form>-<method>.json`.

| Form | Finder | Loogle | LeanSearch | rg pinned source | local name search |
|---|---|---|---|---|---|
| Current fixed-m Roth expression | Unrelated additive Roth/Behrend bounds | Chebyshev sqrt bound, different | Additive Roth, not Diophantine | No exact target; unrelated Roth and square estimates | Resolves project target/caller; index warming |
| Literature strict-continuity law | ContinuousAt.eventually_lt | Same positive exact hit | Same, plus semicontinuity variants | OrderClosed691, Pow/Continuity218, metric neighborhood API | Resolves eventually_lt; index warming |
| Abstract closed interval in a neighborhood | Eventually.exists_Ioo_subset and exists_gt | No hit | exists_Icc_mem_subset_of_mem_nhdsGE and related bases | LeftRightNhds311, Basic433/444 | Resolves closed-interval APIs; index warming |
| Supplementary arbitrary power perturbation | Akra–Bazzi estimates, different | No hit | rpow limit building blocks, not the full conclusion | rpow algebra/limits, no exact full numerical family | rpow symbols returned; index:error explicitly limits completeness |

[Current Finder](../evidence/Roth.exists_delta_bound/search-current-leanfinder.json),
[standard Loogle](../evidence/Roth.exists_delta_bound/search-standard-loogle.json),
[abstract LeanSearch](../evidence/Roth.exists_delta_bound/search-abstract-leansearch.json),
[current rg](../evidence/Roth.exists_delta_bound/search-current-rg.json),
[standard rg](../evidence/Roth.exists_delta_bound/search-standard-rg.json),
[abstract rg](../evidence/Roth.exists_delta_bound/search-abstract-rg.json),
[power searches](../evidence/Roth.exists_delta_bound/search-power-leansearch.json),
[local index limitation](../evidence/Roth.exists_delta_bound/search-power-local_search.json).
The validator checks every one of the20 receipts, not just these representative links.
External search indexes may differ from the pin. Warming/error local indexes are **not** evidence
of absence; pinned source inspection and actual signatures establish positive candidates.
The supplemental power-form no-hit queries likewise do not prove global nonexistence.

Pinned existing building blocks verified by native #check and successful use:
`Real.lt_sqrt_of_sq_lt` (Analysis/Real/Sqrt404), `Real.sq_sqrt`, `Real.sqrt_pos`,
`Real.continuousAt_rpow_const` (Analysis/SpecialFunctions/Pow/Continuity218), `Real.zero_rpow`,
`ContinuousAt.eventually_lt` (Topology/Order/OrderClosed691), `Metric.eventually_nhds_iff`,
`mem_nhdsGE_iff_exists_Icc_subset` (Topology/Order/LeftRightNhds311),
`nhdsWithin_le_nhds`, `Filter.Eventually.and`, `eventually_lt_nhds`.
Their full pinned modules are archived and hashed in
[mathlib inputs](../evidence/Roth.exists_delta_bound/mathlib-inputs.json).
Conclusion: exact full fixed-m result not found; genuine existing building blocks cover distinct
stages. No unsupported exact-match or ≤3-call full-result claim is made.

## Phase 5.5 — Statement shape, all three checks

Normal forms: current curried bounds, quantification over Set.Icc0δ₀, and an eventual predicate
at nhdsWithin0(Ici0). The last is the generic topological form; Set.Icc is the concrete closed
interval form. No orthogonal equivalence or reversed simp-normal-form theorem is proposed.
RHS convention is n/a to this existential theorem. The interval_shape equivalence direction
was compiled as a syntax alternative; curried premises remain convenient at both actual uses.

Syntactic generality: retained original fixed-m interface for the current project. Replacing it
by only a positive/open interval would lose the bound used at0. A supplied-event helper is a
separate layer, not an equivalent theorem without additional premises.
Superfluous argument audit: n and m occur essentially in the family; hm is necessary by the
verified sharp iff; no explicit typeclasses exist; positivity of m and exponent are derived,
not redundant supplied assumptions. Conclusion domain guards delimit the claimed uniform set.
Verdict SHIP-AS-STATED for the current local interface; a future generic public helper would
use the separately verified signature in Phase4b.

## Phase 6.0 — Complete caller and inline audit

Internal use count K=1 outside declaring file;1 distinct caller declaration in1 external file.
There are **two bound applications, not two callers**.

| Caller | Source usage | Both mathematical uses |
|---|---|---|
| Roth.exists_delta, Main.lean:227; call231 | obtain ⟨δ₀,hδ₀,hδ₀'⟩ := exists_delta_bound hm | hδ₀'0 at241 supplies nonzero quotient denominator; hδ₀'δ at247 supplies29/30 after choosingδ. |

Fresh `rg --no-ignore` over the production inventory agrees with tracked `git grep`; the only
other occurrence is a module docstring. No full bound rederived inline elsewhere was found;
Main.exists_delta has a **different** quotient-continuity step with the same local shrinking
pattern. Canonical audit requested293 unique names in exact tracked order, including private
module names, and observed293 present constants and293 values: exactly1 direct body consumer
Roth.exists_delta,0 direct type consumers. The theorem has no simp attribute.
Transitive callers through exists_roth_parameters_aux and the Roth theorems are distinct from
these direct source/kernel counts; no unmeasured simp or transitive closure count is asserted.

[Source enumeration](../evidence/Roth.exists_delta_bound/source-search.json),
[tracked crosscheck](../evidence/Roth.exists_delta_bound/tracked-source-search.json),
[inline pattern search](../evidence/Roth.exists_delta_bound/inline-audit.json),
[complete caller body](../evidence/Roth.exists_delta_bound/callers.json),
[scope audit](../evidence/Roth.exists_delta_bound/scope-audit.json).

Actual inlining experiment: complete Main module replay under Delta234Inline; the target call
was replaced by its full original proof as a local_bound, preserving both later applications.
Native isDefEq confirms the **original exists_delta signature retained**; an opaque value scan
confirms the replayed caller no longer directly refers to Roth.exists_delta_bound. All public
replayed Main declarations through roth/roth_rat have standard-axiom checks.
This verifies feasibility, not redundancy: the caller gained the entire substantive proof.
[Exact full inline replay](../evidence/Roth.exists_delta_bound/inline-executed.lean.txt),
[clean inline receipt](../evidence/Roth.exists_delta_bound/inline-receipt.json).

## Phase 6 — Composition experiments

1. Generic supplied-event transport compiles with two existing calls:

```lean
mem_nhdsGE_iff_exists_Icc_subset.mp (nhdsWithin_le_nhds he)
```

Here he is **the full eventual conjunction δ<1/m and the target strict inequality**. This is
not a proof of the original theorem from hm. Producing he requires the square-root gap,
positive exponent, continuity, the value at0 and an eventual conjunction. project.transport_full_event
explicitly records that stronger supplied premise.

2. Existing strict-continuity and radius-shrinking route: the original exact16-line arithmetic
proof succeeds in fullmodule replay. It uses square-root inequalities, positivity, continuity,
zero-rpow normalization and interval shrinking, exceeding3 calls with genuine reasoning.

3. New arbitrary-power route: small_power_perturbation plus gap_iff and a normalization proof
specializes successfully in a Roth-free mathlib-only source. These are **new generic proofs**;
counting them as existing mathlib calls would falsely hide the theorem's content.

4. The actual single caller inlining succeeds while retaining its type, as above. No closing
`simp [defs...]` composition of the full theorem was found or claimed. The bridge's simpa[eta]
unfolds only the representation after the new substantive theorem is proved.

Conclusion: **NOT-COMPOSABLE as the full original statement from hm in≤3 existing calls** on
this evidence. The purely topological transport is already present, and that narrower fact
cannot justify either NO bucket for the complete fixed-m result.

## Phase 7 — Verdict and future API questions

**BORDERLINE-needs-human**, independently assessed; no inherited verdict from eta or the
surrounding Roth theorem. The exact arithmetic threshold is sharp and the result supports the
actual quotient argument at0, so it is not junk. Yet the particular10^m/(1/2)^m/3 bookkeeping
family has only one direct consumer. Its arbitrary-power extension is a genuine reusable
semantic family, while the most abstract neighborhood transport already has existing mathlib
API. The unresolved matter is the desired public theorem boundary and audience, not proof
validity, missing investigation, or implementation cost.

1. Should the fixed-m numerical lemma remain local to a future Roth proof module, or be exported
   as public numerical API?
2. Would mathlib want a named arbitrary positive-power perturbation lemma, or should callers use
   ContinuousAt.eventually_lt and mem_nhdsGE_iff_exists_Icc_subset directly?
3. If a general helper is wanted, should its public conclusion use a supplied eventual predicate
   on nhdsWithin0(Set.Ici0), with the square-root gap kept in the Roth module?

These are concrete future upstream questions; they do not block this completed read-only
assessment or require stopping the user now. Alternative local destination: current
Roth/MainLemma.lean, because the exact constants encode Roth's parameter choice.
No YES home/title/reviewer/grouping is asserted. Current accepted verdict snapshot is retained
for provenance; parent names or usefulness were not used to infer accepted YES grouping.

## Phase 8 — Verification, preparation history and delivery

Four accepted sources passed completely with no warnings/errors, partial results, recovered
sorryAx, new axioms, unsafe/native_decide or resource raises:

| Native source | Verified result |
|---|---|
| original | Whole MainLemma replay with only target rename/namespace change; full native type/axioms; exact canonical293 order/unique/present/value audit. |
| isolated19 | Roth target absent; new generic power theorem, expanded original, sharp gap iff, m=0/equality/p=0 counterexamples. |
| inline | Whole Main replay, sole direct caller inlined, original caller type and absence of target reference checked. |
| project | Sharp iff for full named conclusion, n=0 case, both closed endpoints, generic bridge, interval form and supplied-event transport. |

[Verification ledger with exact requests/timings](../evidence/Roth.exists_delta_bound/verification.json).
Each disk source retains the exact9 imports. Exact18 isolated preflight rejected the missing
rpow continuity declaration; root authorized this declaration's isolated19 prefix only,
adding Mathlib.Analysis.SpecialFunctions.Pow.Continuity. Shared18 remains byte-identical.
[Prefix authorization](../evidence/Roth.exists_delta_bound/root-prefix-scope-authorization.json),
[prefix provenance](../evidence/Roth.exists_delta_bound/prefix-provenance.json).

Rejected attempts are retained separately: exact18 missing import; first generic gap proof used
a wrong multiplication lemma; project preparation lacked scoped topology notation and needed
explicit sqrt/cast normalization; two subsequent attempts diagnosed the eventual variable's
natural-number inference, resolved by explicit δ:ℝ. None is accepted proof evidence. Initial
whole-document loading was partial and is stored as warming. A clean initial printer pass
omitted allowOpaque for body constants, then was superseded. A preparation width guard failed
before the corrected original execution; no stale source was executed after that failure.
[Preparation record](../evidence/Roth.exists_delta_bound/preparation-checks.json).

The portable read-only validator checks the **current** copy manifest, source/pin hashes,
all accepted native diagnostics, standard axioms, exact293 array/order/private modules, source
caller inventory, complete replay relationships,20 formal cells, every named literature channel,
required overview keys/links and the shared secret guard. It supports scratch and integrated
layouts and excludes only manifest/root-review integration records from recursive coverage.

[Assessment](../evidence/Roth.exists_delta_bound/assessment.json),
[portable validator](../evidence/Roth.exists_delta_bound/validate.py),
[current manifest](../evidence/Roth.exists_delta_bound/copy-manifest.json).
