# Roth.reduction — canonical271

**BORDERLINE-needs-human. Assessment complete; root acceptance pending.** The exact original
proof, full actual caller, arbitrary real threshold, and full injective scaling argument have
been verified. Three future upstream API questions remain; they do not block this assessment.
No production source, pin, Git state, or persistent native document was changed by this worker.

## Phase0: baseline and scope

The declaration is public at `Roth/Main.lean:118`. All17 production source/pin hashes freshly
match the tracked shared manifest, and match again at freeze. The shared clean baseline built
2467 jobs. The accepted file-end Theta228 full build remains reusable; no file-end build is due
at271, next289. [Inputs](../evidence/Roth.reduction/inputs.json),
[baseline](../evidence/Roth.reduction/baseline-build.txt),
[final inputs](../evidence/Roth.reduction/fresh-final-inputs.json).

The entire588-line Main module and66-line downstream LeanEval module were read. Explicit
source searches used `rg --no-ignore` across the canonical production inventory. The focused
original replay copies the exact target declaration only, with basename `replay` in a fresh
namespace and `open Roth`; no private helper closure is needed. Its original imported public
prerequisites remain available. This is not a whole-module replay.
[Reading](../evidence/Roth.reduction/source-reading.json),
[exact replay](../evidence/Roth.reduction/original-executed.lean.txt),
[raw native](../evidence/Roth.reduction/original-receipt.json).

Root exclusively executed all native and project-LSP requests through its persistent session.
Worker prepared source/hash/request archives and inspected the full returned diagnostics. The
stable18 mathlib prefix and nine disk imports were preserved. Root authorized precisely the
additional Asymptotics and LiouvilleWith modules for isolated comparison, with no Roth import.
[Authorization](../evidence/Roth.reduction/import-authorization.json),
[verification](../evidence/Roth.reduction/verification.json).

## Phase1: mathematical content and exact type

An irrational real algebraic number with infinitely many fixed-unit rational approximation
pairs at exponent κ>2 yields an irrational algebraic integer with infinitely many such pairs
at an exponent still greater than2. The exponent may decrease. The proof produces a positive
natural M, chooses κ′=(κ+2)/2, discards finitely many bounded denominators, and sends
(h,q) to (M*h,q). Numerator scaling multiplies the error by M; exponent slack absorbs M.

The full native type, including all mathematical parameters, is:

```lean
∀ {α : ℝ}, Irrational α → IsAlgebraic ℚ α → ∀ {κ : ℝ},
  2 < κ → (Roth.approxSet α κ).Infinite →
  ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧
    (Roth.approxSet α' κ').Infinite
```

`α` is the starting real, `κ` the exponent; irrationality supplies the irrational scaled
output, algebraicity supplies an integral multiple, and infinity supplies unbounded good pairs.
The literal original proof references exactly `Roth.approxSet`,
`Roth.exists_nat_mul_isIntegral`, `Roth.eventually_div_rpow_lt`, and
`Roth.approxSet_den_le_finite` in its kernel value. The type references approxSet.
[Full type](../evidence/Roth.reduction/native-type.json),
[exact filtered dependencies](../evidence/Roth.reduction/dependencies-receipt.json).

The original `pp.all` kernel print has137118 characters elided, and the broad BODY_CONSTANTS
print has515 characters elided. This is not a complete kernel body dump. Both raw elisions are
preserved and disclosed; the full written source, full tagged type, standard-axiom output,
nonelided project dependency list, and complete canonical kernel-value audit remain available.
Subsingleton equality verifies exact proposition signature agreement, not proof construction
identity.

## Phase2: preliminary classification

SMALL: this is a reduction helper, rather than the named final theorem or a new structure.
It appears in the module proof outline; the main-results list names roth/roth_rat/integral Roth.
The one-line-definition test is n/a because this is a theorem. Its proof is substantive and
not a direct arithmetic midpoint wrapper.

## Phase3: exhaustive literature

Every named channel and three actual general queries were executed. Exact requests and
returned-response serialized SHA256/byte/status metadata are saved without article/search
bodies. Locators contain clean complete URLs and original concise summaries.
[Literature records](../evidence/Roth.reduction/literature.json).

| Channel | Actual query or locator | Finding |
|---|---|---|
| General specific | Roth theorem reduction algebraic integers positive integer multiple exponent epsilon | Klazar explicitly teaches this algebraic-to-integral reduction. |
| General broader | irrationality exponent invariant rational affine transformations multiplication | Constant and height formulations surfaced; no fixed-pair equivalence inferred. |
| General alias | Diophantine approximation absorb multiplicative constant smaller exponent Roth reduction | Exponent slack is the relevant mechanism, not preservation of a unit constant at the same exponent. |
| Optional math opinion | ask_chatgpt_math | Justified n/a: unavailable; other channels unchanged. |
| Local reference | clean.tex §6, lines1150–1198 | Gives positive M, h′=Mh, any2<κ′<κ, finite denominator discard and irrationality. |
| nLab | site:ncatlab.org/nlab Roth theorem Diophantine approximation algebraic integers | Background on irrationality/integral elements; no exact scaling result. |
| Distinct nCatLab | site:ncatlab.org/ncatlab irrationality exponent rational approximation; retry with Diophantine approximation | Returned nLab/other namespaces; no exact in-namespace hit, not an absence claim. |
| Stacks | site:stacks.math.columbia.edu algebraic integral multiple rational; additional integral/multiple/algebraic query | No exact approximation theorem. Direct tag00H3 is unrelated integrality over ideals, explicitly not supporting the target. |
| MathOverflow | site:mathoverflow.net Roth theorem algebraic integers reduction | Applications/generalizations discussion, no exact pair reduction. |
| Recent arXiv | site:arxiv.org Roth theorem formalization algebraic integers after:2021-10-29 before:2026-10-30; further affine/exponent queries with same dates | Recent p-adic Roth and affine singular-vector papers concern different statements; additive-combinatorics Roth hits excluded. |

[Batch0](../evidence/Roth.reduction/web-batch0.json),
[batch1](../evidence/Roth.reduction/web-batch1.json),
[batch2](../evidence/Roth.reduction/web-batch2.json),
[batch3](../evidence/Roth.reduction/web-batch3.json),
[local excerpt](../evidence/Roth.reduction/local-excerpt.tex.txt).

Primary supporting web evidence is [Klazar's2025 teaching record](https://kam.mff.cuni.cz/~klazar/AKTC25.html),
Lecture2 February28, which explicitly lists this reduction; Lecture3 treats irrational algebraic
integers. The exact argument comes from the project authors' local clean.tex §6. Recent primary
context includes [Kalitzin–Murru](https://arxiv.org/abs/2603.10561) and
[Datta–Xu](https://arxiv.org/abs/2208.02212), without identifying their p-adic/singular-vector
statements with this theorem. These channels do not establish a uniquely preferred upstream API.

The classical reduction uses threshold2 because its caller proves Roth. Our arbitrary threshold
t is an independently verified elementary generalization of that proof, rather than a claim
that external literature names a separate t-threshold theorem. Mathlib's LiouvilleWith packages
an existential multiplicative constant and uses frequently-atTop denominators with exact equality
excluded; this is a useful alternative representation with different application obligations.

## Phase4a–b: generality, actual proofs and recovery

| Parameter or hypothesis | Role and verified scope |
|---|---|
| α:ℝ | Real order, absolute value, rpow and Archimedean finite slices are used; no unproved field generalization proposed. |
| Irrational α | Supplies irrational Mα. The independent scaling lemma drops irrationality entirely. No assertion of absolute logical minimality of this existential reduction. |
| IsAlgebraic ℚ α | Supplies the positive integral multiple. Scaling alone needs neither algebraicity nor integrality. |
| κ:ℝ | Arbitrary real exponent; scaling works with any κ′<κ, including negative exponents. |
| 2<κ | Replaceable by arbitrary real t<κ; actual mathlib-only theorem proves t<κ′<κ. |
| Infinite approximation pairs | Removed only a finite bounded-denominator slice; then injective numerator-map image. No rational reduction or finite-fiber substitution hidden here. |
| M>0 in scaling | Ensures this numerator map is injective and preserves irrationality when used in reduction. It is not claimed necessary for the weaker standalone Infinite conclusion: at M=0 all (0,q>0) already approximate0. |

The verified candidate is:

```lean
theorem threshold {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α)
    {t κ : ℝ} (hκ : t < κ) (hinf : (approxSet α κ).Infinite) :
    ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ t < κ' ∧ κ' < κ ∧
      (approxSet α' κ').Infinite
```

The actual independent scaling statement is:

```lean
theorem scaling {α κ κ' : ℝ} (M : ℕ) (hM0 : 0 < M) (hκ : κ' < κ)
    (hinf : (approxSet α κ).Infinite) : (approxSet (M * α) κ').Infinite
```

The exact112-line isolated source reconstructs approxSet and the three prerequisites with only
mathlib imports, guards both absent Roth names with `#check_failure`, proves the full scaling
image/membership argument, obtains the arbitrary midpoint threshold, and recovers the original
statement at t=2. These are fresh checked scratch proofs, not existing mathlib declarations.
The original prerequisite proof templates are explicitly copied from canonical267/269
(approximation set/finite slice),268 (integral scalar), and270 (powergap), freshly elaborated;
preparation/audit mechanics were adapted from270. No previous verdict was inherited.
[Exact proofs](../evidence/Roth.reduction/isolated-executed.lean.txt),
[clean raw result](../evidence/Roth.reduction/isolated-receipt.json).

Current threshold specificity is therefore verified, not guessed. Whether the generalized
pair statement should be upstreamed is a separate API judgment. The positive generalization
has no cost-based downgrade.

## Phase4c: nine modern-idiom rows

| # | Question | Assessment and concrete consequence |
|---|---|---|
|1|Typeclasses/instances|No: elementwise Irrational/IsAlgebraic are existing predicates; creating instances would change the interface without useful inference.|
|2|Filters/nets|Yes comparison: LiouvilleWith uses frequently-atTop denominators and permits a constant. It composes with nat_mul and frequently_lt_rpow_neg; no exact fixed-pair equivalence claimed.|
|3|Universal property|No: an existential witness is being chosen, not a canonical construction with a universal property.|
|4|Bundled substructure|No for approximation pairs, which are not closed under algebraic operations. Integral closure can supply the scalar prerequisite through existing algebraic API.|
|5|Hierarchy weakening|No validated real-to-field weakening: real powers and finite integer intervals matter. The algebraic-only prerequisite has broader existing APIs.|
|6|Higher categories|No categorical mathematical content in this reduction.|
|7|Concrete index|ℤ numerators and positive ℕ denominators encode rational approximation. Arbitrary groups would change the arithmetic representation; no unsupported replacement.|
|8|Concrete-via-abstract|Yes: threshold2 appears only in gap/midpoint/output. After choosing an integral multiple, the scaling proof uses no algebraicity or irrationality. Actual generic t and independent scaling proofs remove these restrictions for that subproblem.|
|9|False-generalization guard|Pass for arbitrary t and positive-scalar scaling. LiouvilleWith is explicitly a different predicate, same exponent there is not silently transported to fixed-unit pairs. At exponent1 rational0 is LiouvilleWith; irrationality cannot be inferred indiscriminately.|

[Identifier diagnostic](../evidence/Roth.reduction/concrete-diagnostic.json).
The useful contemporary alternative is either reusable fixed-pair scalar transport or a carefully
proved bridge to existing LiouvilleWith. It would enable the existing affine/filter API rather
than duplicating it, but that bridge was not claimed proved here.

## Phase4.5: six infrastructure risks

All six rows—typeclass diamond, reducibility leak, noncanonical unfolding, instance priority,
universe polymorphism, coercion ambiguity—are justified n/a for a theorem: this declaration
introduces no instance, data definition, coercion or definitional-equality diamond. Proposed
scaling/threshold are also theorems. Representation choice is a mathematical API question.

## Phase4.6: proof strategy, five rows

| # | Strategy question | Assessment |
|1|Topology ε–δ versus filters|The powergap prerequisite already uses Tendsto/rpow divergence; reduction need not repeat the limit proof.|
|2|Element algebra versus substructures|Integral-multiple existence can use integralClosure infrastructure; the real error comparison is appropriately pointwise.|
|3|Sequences versus nets|No explicit sequence construction. Infinite.sdiff/image is natural for actual pair preservation; frequent denominators offer a distinct idiom.|
|4|Universal-property construction|n/a: no categorical universal object.|
|5|Missing helper API|A generic fixed-unit pair scalar-transport theorem factors out the substantive argument; it was actually proved here. Existing LiouvilleWith invariance should be reused if that representation is adopted.|

REFACTOR-RECOMMENDED for an upstream API: expose generic scaling and arbitrary threshold, or
integrate via a proved LiouvilleWith bridge. Local original strategy is mathematically sound.
No estimate of implementation effort determined the verdict.

## Phase5: fifteen actual formal-search cells

All three forms were searched by all five methods, with exact raw receipts and queries.
Remote indexes may differ from the pin; positive relevant APIs were read in pinned sources and
native checked in the isolated proof. Local index errors are recorded as limitations, not absence.

| Form | LeanFinder | Loogle | LeanSearch | pinned rg | local name search |
|---|---|---|---|---|---|
|Current algebraic-to-integral reduction|Liouville roots/approximation hits|Integral/algebraic multiple hits|Liouville/Dirichlet partials|exists_integral_multiple|index:error; source hits only|
|Literature/constant-affine form|LiouvilleWith rational invariance|LiouvilleWith integer/natural/rational multiplication|LiouvilleWith multiplication|full LiouvilleWith API|index:error; source hits only|
|Abstract infinite transport|Infinite.diff etc.|Infinite.image/infinite_image_iff|injective image/finite difference|Infinite.sdiff/image|index:error; source hits only|

[Complete15-cell matrix](../evidence/Roth.reduction/formal-search-matrix.json),
[full-name search](../evidence/Roth.reduction/full-name-search.json).
The final matrix links each full raw receipt. Two Loogle rate-limit returns were preserved and
then successfully retried. Initial remote-search orchestration failed at serialization because
btoa was unavailable; those initial result objects were lost, not represented as archived.
All definitive remote searches were rerun with correct serialization. The incident and exact
initial forms/patterns are [recorded](../evidence/Roth.reduction/search-orchestration-rejected.json).

Relevant pinned existing APIs are `IsAlgebraic.exists_integral_multiple`,
`Irrational.natCast_mul`, `Set.Infinite.sdiff`, `Set.Infinite.image`, `Set.Infinite.mono`,
`mul_right_injective₀`, `Function.Injective.prodMap`, `LiouvilleWith.nat_mul`,
`LiouvilleWith.mul_rat`, `LiouvilleWith.exists_pos`, `LiouvilleWith.mono`, and
`LiouvilleWith.frequently_lt_rpow_neg`. The first group supplies ingredients; the second group
works with the existential-constant predicate. No exact original pair reduction was identified.
The new scaling proof is not relabeled as an existing library hit.

## Phase5.5: statement shape

Normal form: the two relevant forms are fixed-unit pair infinitude and existential-constant
frequent denominators. Mathlib has the second as LiouvilleWith; they are not definitionally the
same. Do not introduce orthogonal equivalences without selecting a target API and proving the
needed bridge. No RHS-normalization claim is being made for this existential theorem.

Syntactic generality: the tested arbitrary t theorem returns both t<κ′ and κ′<κ. The exact
original theorem is recovered at t=2. The caller experiment intentionally uses a weaker
arbitrary-t corollary omitting the unused upper inequality; it is not advertised as the identical
primary signature. Exposing a chosen M or a given κ′ would make scaling reusable independently.

Superfluous arguments: hα constructs irrationality; halg constructs integrality; hκ chooses the
midpoint; hinf drives finite subtraction and injective image. No ordinary typeclasses or unused
arguments are present. The numeral2 is generalizable, with actual proof. Neither dropping
irrationality from the final reduction nor generalizing ℝ was asserted. RESTATE-BEFORE-SHIP
if a pair API is chosen; the native candidate makes the statement concrete.

## Phase6.0: callers, inlining and dependence scopes

| Actual caller | Source | Verification |
|---|---|---|
|Roth.roth|Main:576, within theorem beginning573|Entire original signature/body replayed with literal reduction and generic threshold recovery.|

There is one explicit proof call, zero external-to-file direct callers, zero direct type
consumers, two documentation mentions, and one declaration head. No equivalent reduction is
independently rederived inline elsewhere. `exists_reduced_approx` performs rational reduction
and finite-fiber analysis, not this injective scalar transformation.
[Search](../evidence/Roth.reduction/caller-complete-search.json),
[inline search](../evidence/Roth.reduction/inline-complete-search.json),
[caller source](../evidence/Roth.reduction/caller-Roth.roth.lean.txt).

The293 canonical constants were enumerated directly from tracked declaration-order, preserving
private-name modules and exact order; pre-execution checking and runtime293 unique/present/value
counts passed. Only Roth.roth directly uses the target kernel value. Project type/value
transitive consumers are Roth.roth, Roth.roth_rat, and LeanEval thueSiegelRoth. The target is not
in the simp set. Source lexical/body/type occurrences, direct kernel dependencies, simp
membership and project transitive closure are distinct audited scopes.
[Canonical scope](../evidence/Roth.reduction/canonical-consumers.json),
[raw scope](../evidence/Roth.reduction/consumer-scope-receipt.json).

Both full caller variants compile, and native Subsingleton equality checks their exact original
proposition signatures and the recovered reduction signature. Noncircularity traverses
project/private/scratch definitions and checks every frontier constant for Roth.reduction or
Roth.roth. Mathlib/core frontier constants are not recursively expanded. Checked counts are
2795/2796 for the callers and459 for the generic threshold; no forbidden original was reached.
[Full caller proofs](../evidence/Roth.reduction/caller3-executed.lean.txt),
[raw caller03](../evidence/Roth.reduction/caller3-receipt.json),
[scope explanation](../evidence/Roth.reduction/inline-audit.json).

caller01 attempted unrestricted mathlib/core expansion and returned a45-second partial timeout;
it is unaccepted, not a theorem failure. caller02 is clean redundant evidence; caller03 adds
exact signature checks. scope01 had an empty-line style warning; scope02 is clean. Every exact
native source and full raw returned receipt, including those superseded attempts, is retained.
No raised limits, sorry, new axiom, unsafe or native_decide were used in accepted sources.

## Phase6: composition and semantic guards

**NOT-COMPOSABLE** from ≤3 existing mathlib calls for the actual fixed-unit pair statement.
The isolated composition experiment runs `exact?` and simp closing probes before introducing
any same-result scratch helper. They do not close. Direct LiouvilleWith.nat_mul does not typecheck
as this theorem. A full fallback proof reconstructs the prerequisites and closes the actual
statement, confirming that the negative probes did not obscure an unproved goal.
[Exact experiment](../evidence/Roth.reduction/scope2-executed.lean.txt),
[clean raw result](../evidence/Roth.reduction/scope2-receipt.json),
[composition accounting](../evidence/Roth.reduction/composition.json).

The structural skeleton is finite subtraction, injective image and monotonicity, but the
membership estimate, scalar positivity and rpow gap are real proof work. A short composition
of newly proved scratch scaling and midpoint does not count as an existing mathlib replacement.
Finite search/probe failures do not prove global library absence.

A native counterexample shows the naive map (h,q)↦(2h,q) need not preserve membership at the
same exponent with unit constant: α=3/4,h=0,q=1,κ=0. This only refutes that direct pair map
claim; it does not refute a global same-exponent Infinite theorem. The strict midpoint guard
at t=κ and LiouvilleWith1 at rational0 were also checked. Thus no hidden equality/irrationality
or exponent-preservation claim supports this verdict.

## Phase7: verdict and concrete next action

**BORDERLINE-needs-human**, independently assessed. The substantive fixed-pair map theorem is
verified and threshold2 is demonstrably specializable from arbitrary t. Existing mathlib
LiouvilleWith invariance is strong relevant API but does not directly replace this representation.
A choice of upstream approximation API remains, rather than an uncompleted mathematical proof
or a cost objection. One explicit caller is useful context, not proof that the lemma is junk.

1. Should upstream consumers keep fixed-unit unreduced pair infinitude as a public representation,
   or expose this reduction through a separately proved bridge to existing LiouvilleWith?
2. If pairs are retained, should generic positive-natural scalar transport be the primary API,
   with the algebraic-to-integral reduction a project-local corollary?
3. If an integral reduction is public, should its statement use arbitrary real threshold t and
   explicitly return κ′<κ, as the checked candidate does?

These are future upstream design questions, not a request for user permission to finish this
assessment. Keep the existing theorem project-local pending that choice. A fixed-pair API would
need a proposed number-theoretic home near LiouvilleWith, with layering decided alongside its
representation; a LiouvilleWith route should reuse its affine laws and prove a precise bridge
first. No speculative YES PR title/reviewer/grouping is offered for a BORDERLINE verdict.

## Phase8: overview integration and validation

The overview entry includes the full native Lean type, mathematical argument, every project
body dependency, caller scope, pairwise duplication distinctions, verified generalization,
missing API and actionable local destination. The pairwise comparisons are:

| A | B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
|reduction|exists_nat_mul_isIntegral|No, algebraic prerequisite only|No, no approximation transport in prerequisite|Reuse scalar API; retain transport content.|
|reduction|eventually_div_rpow_lt|No, asymptotic estimate only|Only exponent-gap substep shared|Reuse powergap; do not classify full theorem by midpoint arithmetic.|
|reduction|exists_reduced_approx|No, integral scalar versus reduced rational witnesses|Different maps, injective image versus finite fibers|Do not unify the transformations.|
|scaling candidate|LiouvilleWith.nat_mul|Different predicates/constant normalization|Related scalar estimate|Choose representation and prove bridge before replacement.|

[Assessment](../evidence/Roth.reduction/assessment.json),
[overview entry](../evidence/Roth.reduction/overview-entry.json),
[portable read-only validator](../evidence/Roth.reduction/validate.py),
[current recursive manifest](../evidence/Roth.reduction/copy-manifest.json),
[actual both-layout checks](../evidence/Roth.reduction/final-validation.json),
[secret guard](../evidence/Roth.reduction/secret-guard.json).
