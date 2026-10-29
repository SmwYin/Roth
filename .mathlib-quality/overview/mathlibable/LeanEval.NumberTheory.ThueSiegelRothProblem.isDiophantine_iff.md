# `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`

Verdict: **BORDERLINE-needs-human**. The equivalence contains reusable mathematical content beyond a short composition. A fresh proof establishes the stronger all-real statement, and a generic real cutoff works without any positivity assumption on that cutoff. Upstream design remains a choice of canonical interface, rather than a question about whether the proof can be generalized. This assessment is independent of the verdict on `IsDiophantine` and does not assess the later named Roth declaration.

## Phase0: baseline and scope

The unchanged17 source/pin hashes freshly match the shared successful2467-job baseline. The complete66-line LeanEval module and the full actual caller were read. Target resolves at Roth/LeanEval.lean:42, public theorem, no sorry. The module proves the LeanEval interface from `Roth.roth`. Root exclusively executed native checks; workers used only remote formal search and file reads. Stable18 isolated imports and disk9 remained unchanged; root freshly authorized the19th LiouvilleWith import after pinned-header review.

[Fresh input hashes](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/inputs.json); [baseline](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/baseline-build.txt); [module](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/source-LeanEval.lean.txt); [prefix controls](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/prefix-controls.json).

## Phase1: statement and proof

For each positive epsilon a real number has a strictly positive constant bounding every positive-denominator rational approximation error below by C/q^(2+epsilon), precisely when infinitely many unreduced approximation pairs can occur only at exponents at most2. The original supplies irrationality as a hypothesis. There is no algebraicity assumption in this equivalence.

The forward direction assumes kappa>2 and uses epsilon=(kappa-2)/2. `Roth.eventually_div_rpow_lt` absorbs1/C into the positive exponent gap. Removing the finite set of bounded-denominator pairs using `Roth.approxSet_den_le_finite` gives an approximation violating the uniform lower bound. Conversely, the exponent hypothesis makes the pair set at2+epsilon finite. The private helper inserts(0,1), takes a minimum of positive weighted errors, and halves it and1 to produce a strict positive constant valid both inside and outside the exceptional set.

Full native type (tagged kernel type, with binder types):

```lean
∀ {x : ℝ},
  Irrational x →
    (LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2)
```

Project dependencies are `IsDiophantine`, `Roth.approxSet`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`, and the private `exists_pos_div_rpow_lt_aux` in Roth.LeanEval. The canonical project name is used here; the loaded private kernel name is recorded only in raw audit evidence.

[Exact original proof and helper replay](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/original-executed.lean.txt); [full native receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/original01-receipt.json); [native type](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/native-type.json); [dependencies](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/project-dependencies.json). Original replay copies exactly the target and private helper lines20–39 into a fresh namespace. Proof equality via Subsingleton.elim confirms exact type agreement, not identity of proof construction. The pp.all kernel body is explicitly elided by139691characters; this is not claimed to be a full pretty-printed proof. The exact source proof, complete tagged type, actual kernel value access, used constants and standard-axiom audit are retained.

## Phase2: preliminary classification

SMALL: a characterization lemma rather than a named main theorem or new mathematical structure. Its two directions nevertheless require real reasoning. One-line definition check: n/a, theorem. No prefilter or inherited parent verdict applies.

## Phase3: exhaustive literature

| Channel | Actual query | Outcome |
|---|---|---|
| web-specific | `irrationality exponent equivalent for every epsilon positive constant lower bound rational approximation` | Irrationality exponent has equivalent eventual lower-bound presentations; Tao optimization page explicitly gives the sup/inf comparison. |
| web-general | `Diophantine approximation uniform lower bound finite exceptions arbitrary exponent irrationality measure` | Constants and finite exceptional sets recur throughout approximation theory; distinguish uniform-in-p,q lower constants from uniform approximation exponents. |
| web-alias | `Roth theorem irrationality measure epsilon constant formulation equivalence` | Aliases irrationality exponent and measure; Roth statements commonly use finiteness for every positive epsilon. |
| nlab | `site:ncatlab.org/nlab irrationality exponent Diophantine approximation` | Related irrational-number page discusses nonzero rational differences and constructive distinctions; no exact equivalence found. |
| ncatlab | `site:ncatlab.org/ncatlab irrationality exponent Diophantine approximation` | Actual distinct namespace query returned only nLab or unrelated pages, no in-namespace theorem; no categorical reformulation established. |
| stacks | `site:stacks.math.columbia.edu irrationality measure rational approximation` | No matching Stacks result returned; this is real Diophantine analysis rather than an algebraic geometry API. |
| mathoverflow | `site:mathoverflow.net irrationality exponent lower bound constant epsilon Roth` | Finite-solutions discussion and historical discussion corroborate epsilon quantifier; not evidence of a mathlib replacement. |
| arxiv | `site:arxiv.org irrationality exponent Diophantine lower bounds after:2021-10-29 before:2026-10-30` | Recent Aaronson–Nakada paper treats arbitrary irrationality exponent and Diophantine/Liouville classes, confirming nonalgebraic downstream settings. |
| Optional mathematical second opinion | ask_chatgpt_math | Unavailable tool, justified n/a; all other channels completed. |
| Local references | rg Roth/\kappa/irrational/approximation in clean.tex | §6 gives the pair formulation and exponent-gap constant absorption; no exact LeanEval iff printed. |

- [Martine Queffelec, Diophantine approximation and expansions of real numbers](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B46/pdf/B46_010.pdf), §2 p215 and Definition3.1 p217; web lines17–24,72–83: Uses nonexact rational approximants and defines the irrationality exponent for irrational reals as a supremum over approximation orders. This supports varying the cutoff and retaining exact-error conventions carefully.
- [Jon Aaronson and Hitoshi Nakada, Extravagance, irrationality and Diophantine approximation](https://arxiv.org/abs/2409.19393), v1 submitted2024-09-28; v5 2025-09-04; abstract and §1: Studies Diophantine and Liouville behavior for invariant measures and examples with arbitrary irrationality exponent. Generic cutoff statements therefore serve more than the algebraic Roth application.
- [Extravagance, irrationality and Diophantine approximation, HTML](https://arxiv.org/html/2409.19393v5), §1 Introduction, abstract: Recent primary paper supplies a modern dynamical context; it does not identify an existing formal equivalence.
- [The irrationality measure of pi](https://teorth.github.io/optimizationproblems/constants/7a.html), Description of constant lines3–11: Explicitly compares a supremum of infinitely-often exponents with an infimum of eventual lower-bound exponents. Used for formulation only, not numerical bounds.
- [irrational number in nLab](https://ncatlab.org/nlab/show/irrational%2Bnumber), Definitions: Discusses positivity versus nonequality with rational numbers and their classical equivalence; no exponent-bound bridge identified.
- [Estimate number of solutions in Roth theorem](https://mathoverflow.net/questions/249176/estimate-number-of-solutions-in-the-roths-theorem), Question and answers: Frames Roth in terms of finitely many solutions for each epsilon and discusses quantitative refinements.
- [History question: Roth theorem before Roth](https://mathoverflow.net/questions/149600/history-question-roths-theorem-on-approximating-algebraic-numbers-before-rot/149653), Question and answer: Highlights the separate universal quantifiers over algebraic irrational numbers and positive epsilon; does not justify dropping epsilon.

The primary survey identifies the irrationality exponent as a supremum for irrational real numbers, with generic exponent cutoffs beyond algebraic reals. The exact-minimum argument upgrades eventual lower bounds to all positive denominators. The literature often excludes exact equality or counts reduced rational values: the unreduced pair convention must be kept distinct. No claim about the badly approximable epsilon0 endpoint follows. The nCatLab query was genuinely separate from nLab; its out-of-namespace returns are recorded honestly. No Stacks result or higher categorical formulation was established. Exact requests, returned response SHA256/byte counts/status, clean URLs/locators and original short summaries are archived; no article or search-result bodies are persisted.

[Literature accounting](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/literature.json); [web0](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/web-batch0.json); [web1](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/web-batch1.json); [web2](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/web-batch2.json); [web3](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/web-batch3.json); [local query](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/literature-local.json).

## Phase4a–b: every parameter and verified generality

| Parameter or convention | Decision | Mathematical reason |
|---|---|---|
| x:Real | Retain | Real absolute values, rational discreteness and real exponent asymptotics are used. No arbitrary-field weakening claimed. |
| hx:Irrational x | Remove, verified | Uniform bounds fail at the exact rational numerator/denominator. The exponent bound also fails at rational x, since exact multiples give infinitely many pairs at every kappa. |
| Fixed2 | Generic real t, verified | Only gap arithmetic uses2. The proof applies to any t, including nonpositive t; no positivity hypothesis is needed. |
| Integer/natural denominators | Preserve positive denominator semantics | Lift positive integer q to natural for pair membership; normalize casts explicitly. Replacing integer numerators by arbitrary field elements destroys discreteness. |
| Strict upper approximation error | Preserve in pair convention | The finite-exception complement gives a weak lower inequality; halve constants to recover strict lower bounds. |
| Positive epsilon | Retain | A smaller exponent inside the gap is essential. No epsilon0 or badly approximable equivalence asserted. |

Verified all-real project statement:

```lean
theorem all_real {x : ℝ} :
    LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x ↔
      ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2
```

Verified mathlib-only generic statement, with `UniformBound t x` the complete displayed lower-bound formula and `pairSet` the complete pair formula reconstructed from mathlib operations:

```lean
lemma uniform_pair_iff_all_real {t x : ℝ} :
    UniformBound t x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t
lemma pair_liouville_iff_all_real {t x : ℝ} :
    (∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t) ↔
      Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t
```

The mathlib-only source reconstructs finite bounded-denominator sets, finite positive minima, exponent-gap absorption and pair/frequency transport. It replays accepted290modern3 proofs under a new namespace and extends them here; these are credited as authored proofs, never as existing mathlib theorems. It also proves cutoff monotonicity, rational addition and nonzero rational scaling invariance, rational and Liouville countercases, and C/2 equivalence of strict/weak lower bounds. Fixed2 recovery is definitional. The full project recovery retains the original caller signature and uses `all_real.mpr` with the unchanged Roth proof.

[Generic and semantic proof](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/modern-executed.lean.txt); [generic raw receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/modern01-receipt.json); [project all-real recovery and full actual caller](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/recovery-executed.lean.txt); [recovery receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/recovery01-receipt.json). Current form is strictly narrower in the verified hx binder and semantic cutoff; the upstream representation question is separate from correctness or cost.

## Phase4c: modern idiom, all9 rows

| Row | Applies | Reformulation or reason |
|---|---|---|
| typeclasses | no | The hypothesis concerns one real number; a Prop typeclass would create implicit search rather than improve inference. |
| filters | yes | LiouvilleWith uses frequently atTop denominators; exponent_iff and pair_liouville_iff_all_real connect it to pairs. |
| universal property | no | No constructed object or universal mapping property. |
| bundled substructure | no | Approximation pairs are a subset, not closed algebraic data; a subtype is not a replacement for Infinite. |
| hierarchy | no | Real rpow and rational discreteness are used; arbitrary ordered fields lack the stated analytical API. |
| higher categories | no | No categorical content; distinct nCatLab query supplied none. |
| indices | yes | The exponent cutoff2 is a semantic parameter t, unlike the indispensable integer/natural rational indexing. No positivity on t is needed. |
| concrete via abstract | yes | Counted literal2 in original body: it enters gap arithmetic only; generic proof replaces it uniformly by t. The proof has no special arithmetic property of2. |
| false-generalization guard | PASS | All-real pair iff is valid because rational exact multiples make both sides false. Liouville cutoff alone is true at rationals with cutoff2; retain Irrational conjunct. Do not identify pair sets with reduced rational sets. |

Concrete-via-abstract diagnostic: the original uses literal2 only in epsilon/gap arithmetic; it does not invoke a special property of2. The generic t proof verifies that observation. The pair-set identifier remains in the finite/cofinal transport, so no claim that arbitrary sets of pairs satisfy the theorem is made. Modern LiouvilleWith form directly enables the existing `add_rat_iff`, `mul_rat_iff`, `mono`, and `frequently_lt_rpow_neg` API. The fresh affine and cutoff consequences demonstrate this downstream improvement.

False-generalization guard: exact unreduced multiples force rational pair sets infinite at every exponent, whereas LiouvilleWith excludes equality. The bare all-Liouville-exponent bound at2 is true at rationals. Dropping Irrational from that bridge would be false; dropping the original hx from the pair equivalence is valid. Positive constants and epsilon quantifiers remain.

## Phase4.5: infrastructure risk

All six rows—typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe polymorphism and coercion ambiguity—are n/a for this theorem. It introduces no definition, instance or coercion. Any future predicate packaging needs its own definition review.

## Phase4.6: proof strategy, all5 rows

| Kind | Applies | Idiom or gap |
|---|---|---|
| topology | yes | Use existing atTop exponent-gap limits; LiouvilleWith frequently_lt_rpow_neg handles absorbing a constant. |
| algebra | no | No ideal/submodule inclusion or point-free algebraic law. |
| analysis | yes | Filters already drive gap; pair-denominator cofinality bridge still needs a proof. |
| categories | no | No universal-property construction. |
| missing helpers | yes | Finite exceptional approximations to positive strict uniform constant; generic exponent-cutoff equivalence; rational-pair irrationality derivation. These are authored proof content. |

REFACTOR-RECOMMENDED: keep the existing filter asymptotics and finite positive-minimum reasoning, extract the reusable equivalence and make the current project theorem a fixed2 specialization. The finite-exception and pair/frequency conversion helpers are substantive missing bridges rather than a three-call wrapper. This recommendation is mathematical organization, not a cost rationale.

## Phase5: all15 formal search cells

| Form | Finder | Loogle | LeanSearch | rg pinned source | local LSP via root |
|---|---|---|---|---|---|
| Current fixed2 uniform/pairs | LiouvilleWith and constant absorption | Irrational equivalences, not target | LiouvilleWith plus metric-a.e. result | No target; Diophantine-equation hits unrelated | index error; target hit only, no absence inference |
| Standard generic exponent bound | LiouvilleWith, forall_liouvilleWith_iff | LiouvilleWith affine equivalences | Bounded-denominator separation and Dirichlet results | No named full bridge identified | index error with empty items; no absence inference |
| Abstract predicate/frequency | LiouvilleWith.irrational, mono | mono, irrational, affine lemmas | exists_pos and frequently_lt_rpow_neg | Relevant source and measure API | index warming with50 related entries; no absence inference |

[All exact requests and raw results](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/formal-search-matrix.json); [untruncated full-name search](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/full-name-search.json); [pinned module hashes](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/mathlib-inputs.json); [candidate signatures](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/candidates01-receipt.json). Remote indexes can differ from this pin; candidate signatures were checked on the pinned environment through root.

`LiouvilleWith.frequently_lt_rpow_neg` handles absorbing a constant at a smaller exponent, but does not itself prove a uniform positive lower constant from finite exceptional pairs. `Irrational.eventually_forall_le_dist_cast_div_of_denom_le` separates an irrational real from bounded denominators; this is a relevant tool, not the full weighted-exponent equivalence. `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational` is a Dirichlet endpoint statement counting reduced rational values, not the requested upper-exponent equivalence. `forall_liouvilleWith_iff` concerns all exponents and Liouville numbers, not a bounded cutoff. No exact or more-general existing theorem was verified as a replacement.

## Phase5.5: all3 statement-shape checks

| Check | Outcome | Action |
|---|---|---|
| normal form | REFACTOR | Prefer uniform lower bounds ↔ Irrational x ∧ all LiouvilleWith exponents bounded, with existing predicate family on RHS. Pair bridge remains useful at project boundary. |
| syntactic generality | RESTATE | Drop hx for full all-real pair equivalence, parameterize cutoff t in generic API; fixed2 project statement recovered definitionally. |
| superfluous arguments | DROP1 | hx occurs in private helper but is derivable from either side of full iff. x and real rational indexing remain essential. |

Candidate canonical RHS: Irrational x together with an upper bound on all LiouvilleWith exponents. This avoids inventing a scalar irrationality measure with extended-real endpoint conventions and gives O(n) bridges to one family. A pair-based theorem is still useful at the current project boundary. Its minimal exact cleanup is the all-real statement, whose correctness and caller were checked.

## Phase6: callers, inlining and actual composition

| Actual caller | Source use | Verification |
|---|---|---|
| LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth, Roth/LeanEval.lean:63 | `(isDiophantine_iff _h_irr).mpr (Roth.roth ...)` | Full original body re-elaborated with the entire iff proof inlined; full generalized replacement re-elaborated with exact original signature. |

Internal use count1; external-to-file0. Canonical metadata and `rg --no-ignore` production inventory agree. No independent inline rederivation found in production. The exact293 loaded canonical audit finds one direct body consumer, no direct type consumer; it is not a claim about the entire transitive dependency graph. Target has no simp attribute, so source, body, type, simp and transitive scopes are kept distinct.

[Caller accounting](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/callers.json); [fresh lexical search](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/source-search.json); [complete inline source](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/inline-executed.lean.txt); [inline raw receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/inline01-receipt.json); [generic actual caller](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/recovery-executed.lean.txt).

Attempt1 uses existing `LiouvilleWith.frequently_lt_rpow_neg` and denominator separation. It is partial: it still requires pair cofinality, an intermediate exponent and finite positive strictification. Attempt2 uses `Set.exists_min_image`, `Set.Infinite.sdiff` and exponent asymptotics: these are building blocks but the inequalities and exceptional-set assembly are real proof steps. The isolated `exact?` probes for current and generic forms and `simp only [UniformBound,pairSet]` do not close the iff. Probes precede authored bridge theorems, so cannot rediscover them accidentally. NOT-COMPOSABLE from existing mathlib in<=3 calls. No production inlining is recommended merely because a full inline proof can be made to compile.

[Exact composition probes](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/composition2-executed.lean.txt); [raw composition receipt](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/composition02-receipt.json).

Pairwise moral-duplication check:

| A | B | Same statement | Same proof | Decision |
|---|---|---|---|---|
| isDiophantine_iff | private positive-minimum helper | No; helper is one direction at a fixed exponent | Shared reverse direction | Keep helper or general finite-exception API |
| isDiophantine_iff | Roth.eventually_div_rpow_lt | No; latter is pure asymptotics | Forward direction uses gap | Reuse asymptotic ingredient |
| isDiophantine_iff | Roth.reduction | No; reduction changes algebraic real to integral | Both absorb constants | Share gap theorem; no duplicate iff |
| isDiophantine_iff | forall_liouvilleWith_iff | No; unbounded-all-exponents vs bounded cutoff | Different quantifier conversion | Existing theorem is not a replacement |

## Phase7: independent verdict and actionable alternatives

**BORDERLINE-needs-human**, on canonical upstream API design. This is mathematically reusable across arbitrary real irrationality-exponent bounds and genuinely needs proof beyond current building blocks. Verified irrationality removal and parameterized cutoff establish the available stronger statements. The issue is whether to export both pair and uniform predicates or orient their bridges toward existing LiouvilleWith. A bare fixed2 theorem against two project definitions would prematurely settle that choice. Neither the definition's earlier verdict, the usefulness of the final named Roth theorem, nor implementation cost determines this verdict.

Concrete future upstream questions (assessment complete, no user blocker):

1. Should upstream expose a named UniformBound t x predicate, or keep the lower-bound quantifiers inside equivalences to Irrational x ∧ ∀p, LiouvilleWith p x → p ≤ t?
2. Should the canonical public bridge use denominator-frequency LiouvilleWith directly, keeping unreduced pairSet and its equivalence in a secondary interface module?
3. Should the generic finite-exception strictification and rational-pair irrationality lemmas ship together with the cutoff equivalence, with fixed2 LeanEval wrappers remaining project-local?

Retain locally now; a subsequent authorized cleanup can remove hx and change the sole caller to `all_real.mpr`, using the verified source. For upstream, use the provisional new module `Mathlib/NumberTheory/Transcendental/Liouville/Diophantine.lean` importing LiouvilleWith, with the generic cutoff bridge and finite-exception helpers as one designed API. This is a proposed home, not a claimed accepted YES grouping. No existing mathlib-call deletion plan is supported. No PR is opened, and no production source is changed.

## Phase8: evidence and acceptance

[Verification ledger](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/verification.json); [phase tables](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/phase-checks.json); [canonical snapshot](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/canonical-snapshot.json); [portable validator](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/validate.py); [copy manifest](../evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/copy-manifest.json). Native verification uses standard axioms only and default resources, complete nonpartial diagnostics, zero errors/warnings and no PANIC in any accepted message. Sources/requests are immutable; no sorry, new axiom, unsafe, native_decide or limit raise is accepted. The rejected composition01 source/receipt is retained separately: its positive #check used the wrong Real namespace and two binders triggered implicit-use lints; corrected composition02 passes with no warnings. Root acceptance is pending independent review. Final fileend293 dual builds belong to the root's final boundary gate.
