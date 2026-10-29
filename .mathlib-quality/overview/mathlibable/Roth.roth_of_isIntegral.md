# `Roth.roth_of_isIntegral` — canonical287

Verdict: **YES-but-generalise-first**, reason **MODERN-IDIOM**. This is the named BIG integral
Roth theorem. Its short assembly proof is not a composition from existing mathlib Roth content.

## Phase0 — baseline and scope

Fresh17 production/pin hashes match the tracked shared input manifest; baseline `lake build`
completed successfully with2467jobs. File-end228 successful build is reusable;287 is not a file-end
build gate (next289). No production source, pin, Git, progress, or overview mutation was performed.

Read full Main588 and LeanEval66; read the complete parameter/approximant/degree/Taylor/integer
lower-bound/log contradiction chain and local paper§7, equations46–54. Original replay copies the
exact target plus its five necessary private helper bodies in a fresh namespace and imports
existing public ingredients. Full unrelated Main replay is not claimed or required by the minimal
replay addendum. All native/LSP execution was performed by root; workers prepared immutable sources.

[Fresh inputs](../evidence/Roth.roth_of_isIntegral/inputs.json); [baseline](../evidence/Roth.roth_of_isIntegral/baseline-build.txt); [full Main](../evidence/Roth.roth_of_isIntegral/source-Main.lean.txt); [full LeanEval](../evidence/Roth.roth_of_isIntegral/source-LeanEval.lean.txt); [exact original replay](../evidence/Roth.roth_of_isIntegral/original-executed.lean.txt).

## Phase1 — statement and mathematical proof

For an irrational real algebraic integer α, if infinitely many pairs (h,q) in ℤ×ℕ, q>0,
satisfy |α−h/q|<q^(−κ), then κ≤2. Approximants need not be reduced in this set. The exponent
is an arbitrary real; the proof assumes κ>2 for contradiction and derives its positivity.

```lean
∀ {α : ℝ}, Irrational α → IsIntegral ℤ α → ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite → κ ≤ 2
```

Choose a monic integer equation for α, a coefficient bound A, a large dimension m and small δ
with m(1+4δ)/(γ−η)<κ. Irrationality turns infinitely many unreduced pairs into reduced fractions
with unbounded denominators, so one selects rapidly growing q_j and balances r_j log q_j.
Roth.main_lemma supplies an integer Q with high index at α, bounded derivatives and nonzero value
at the rational approximants. Clearing denominators gives 1≤∏q_j^r_j |Q(h/q)|. Taylor expansion
and the index lower bound give a strict upper estimate. The coefficient/degree products are
absorbed into q_0 powers. Taking logarithms yields (γ−η)κ<m(1+4δ), contradicting the chosen gap.
These are the actual arithmetic ingredients, not generic order lemmas furnishing Roth’s theorem.

[Paper§7](../evidence/Roth.roth_of_isIntegral/local-section7.tex.txt); [complete unelided constant inventory](../evidence/Roth.roth_of_isIntegral/constants01-receipt.json).

## Phase2 — size and definition check

BIG: named after Roth and explicitly listed as a project main result. Definition-only one-line
check: n/a, theorem. The17-line target orchestration invokes the substantive multivariate proof.
A single direct caller is an API-granularity observation, not evidence the named result is junk.

## Phase3 — exhaustive literature

| Channel | Actual query | Finding |
|---|---|---|
| web-specific | Roth theorem algebraic integer irrational finite rational approximations exponent greater than 2 | Roth 1955/1958: irrational algebraic number and infinite pair approximants imply exponent≤2; algebraic-integer reduction is standard. |
| web-general | Roth theorem generalizations number fields places subspace theorem irrationality exponent | Number-field and finite-place height formulations and higher-dimensional subspace theorem are genuine stronger theories, not current-proof typeclass weakenings. |
| web-alias | Thue Siegel Roth theorem irrationality measure uniform epsilon lower bound | Thue–Siegel–Roth/irrationality measure formulations use finite exceptions for every ε>0 or uniform positive lower constants. |
| nlab | site:ncatlab.org/nlab Roth theorem Diophantine approximation | Search finds number theory/Vojta pages; Vojta page open fails unsupported application/xhtml+xml. No direct usable generality theorem obtained. |
| ncatlab | site:ncatlab.org/ncatlab Roth theorem Diophantine approximation | Distinct namespace query actually issued; returned mostly /nlab results, not a matching /ncatlab mathematical statement. |
| stacks | site:stacks.math.columbia.edu "Roth" "approximation" | Independent retry returns bibliography names Rotthaus/Mike Roth, not the Diophantine theorem; no alternative statement obtained. |
| mathoverflow | site:mathoverflow.net Roth theorem irrationality measure | Question510766 discusses irrationality measure but conflates almost-everywhere measure2 with Roth and is not used as authoritative evidence. |
| arxiv | site:arxiv.org Roth theorem Diophantine approximation after:2021-10-29 before:2026-10-30 | Goel–Lunia–Ray 2502.00731v2, 2026-07-21, §3.2 Theorems3.2–3.3: number-field finite-place forms; Hindes2209.09182, 2022-09-19, abstract: positive-characteristic Roth analogue false. |

Optional ask_chatgpt_math was unavailable; its standard-form/generality/history query was not run.
Local clean.tex§7 was read completely. General web queries were three distinct specific/general/
alias forms. Additional independent channel retries and primary opens are retained. Search output
hashes/byte counts/status and clean titles/URLs are stored; full third-party bodies are not stored.
Returned signed URL queries were discarded, never used as source evidence. Namespace misses and
nLab fetch failure are limitations, not proofs of mathematical absence.

Standard concept: Thue–Siegel–Roth theorem. The real rational result has equivalent finite-exception,
exponent-bound and ε-dependent positive lower-bound forms. Algebraic-integral reduction is
classical. Number-field/place/product-formula and subspace theorems are broader results requiring
new machinery here; they are not a verified mechanical generalization of this implementation.
Positive-characteristic analogues are not valid without additional hypotheses.

Primary locators: [Roth1955, Mathematika2,1–20](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F);
[Roth’s1958 lecture, opening§1–2](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf);
[Goel–Lunia–Ray2026,§3.2 Theorems3.2–3.3](https://arxiv.org/html/2502.00731v2);
[Hindes2022, abstract](https://arxiv.org/abs/2209.09182).

[Literature records](../evidence/Roth.roth_of_isIntegral/literature.json); [web0](../evidence/Roth.roth_of_isIntegral/web-batch0.json), [web1](../evidence/Roth.roth_of_isIntegral/web-batch1.json), [web2](../evidence/Roth.roth_of_isIntegral/web-batch2.json), [web3](../evidence/Roth.roth_of_isIntegral/web-batch3.json), [web4](../evidence/Roth.roth_of_isIntegral/web-batch4.json), [web5](../evidence/Roth.roth_of_isIntegral/web-batch5.json), [web6](../evidence/Roth.roth_of_isIntegral/web-batch6.json), [web7](../evidence/Roth.roth_of_isIntegral/web-batch7.json), [web8](../evidence/Roth.roth_of_isIntegral/web-batch8.json).

## Phase4a–b — generality

| Parameter | Assessment | Reason |
|---|---|---|
| α : ℝ | Essential concrete arithmetic domain | Number-field/place versions exist, but are not a typeclass edit of this proof. No verified field weakening claimed. |
| Irrational α | Essential for current pair formulation | α=0 counterexample verified natively. Modern LiouvilleWith theorem can omit this binder because p>2 implies irrationality. |
| IsIntegral ℤ α | Actual monic polynomial assumption | Algebraic extension is the following project reduction-based Roth.roth; imported project theorem is not an existing mathlib replacement. |
| κ : ℝ | Arbitrary real exponent | No missing positive κ binder: contradiction assumes 2<κ and hence supplies every positivity use. |
| approxSet Infinite | Infinitely many unreduced integer/natural pairs | Finite-for-κ>2 equivalent verified. Reduced rational formulation is separately derived, not definitionally the same set. |
| Fixed constant1 | Representational, not essential for exponent-bound family | LiouvilleWith existential C transported via q<p; equality at one fixed exponent is not asserted. |
| Threshold2 | Semantic sharp constant | Dirichlet gives infinite reduced approximations at exponent2; replacing2 by arbitrary threshold would lose the named theorem. |
| Positive natural denominators | Part of approximation domain | q=0 excluded explicitly; integer positive-denominator API in LeanEval is bridged by lift to ℕ, not arbitrary sign removal. |

The classical pair statement has no safely droppable hypothesis. Integral→algebraic is implemented
by the following project theorem Roth.roth using reduction; it is not an existing mathlib theorem
and is not the basis of this verdict. The verified modern restatement is:

```lean
∀ {α p : ℝ}, IsIntegral ℤ α → LiouvilleWith p α → p ≤ 2
```

This accepts the existing existential-constant predicate and derives irrationality when p>2;
for p≤2 the conclusion is immediate. The bridge is an equivalence of the **all-exponent bounds**
for irrational α, not equivalence of fixed-C=1 pair membership with LiouvilleWith at one exponent.
Forward transport chooses q=(p+2)/2 and uses frequently_lt_rpow_neg; the reverse constructs
constant1 LiouvilleWith from unbounded positive denominators. The exact original pair predicate
is reconstructed from mathlib operations, and target absence is guarded with #check_failure.
The isolated proof takes the classical Roth theorem as an explicit premise. Together with the
separately replayed original theorem and identical pair predicate, this verifies the proposed
restatement and recovery modularly; it does not independently prove Roth in mathlib.

## Phase4c — all nine modern idioms

| Question | Applies | Concrete consequence |
|---|---|---|
| Typeclasses | No | Irrationality/integrality are point properties, not competing algebra structures; retain proposition hypotheses. |
| Filters | Yes | LiouvilleWith uses frequently atTop denominators and an existential multiplicative constant. The verified all-exponent bridge absorbs that constant by a strict exponent gap. |
| Universal property | No | No constructed object is characterized by a universal property. |
| Bundled substructures | No | The approximation set is not closed under algebraic operations; no Submodule/Subring replacement. |
| Hierarchy weakening | No | The complete proof needs real absolute value, logarithms, rpow, and integer denominator arithmetic; arbitrary ordered fields are not mechanically supported. |
| Higher categories | No | No categorical content. |
| Concrete indices | No | Integer numerators/natural positive denominators encode rational approximation. Arbitrary monoids would change the theorem; number-field heights require a separate arithmetic development. |
| Concrete-via-abstract diagnostic | Diagnostic fires; abstraction rejected | The target body has zero standalone α tokens and forwards hα once; this is orchestration through private helpers. Those helpers explicitly use the monic integral equation, reduced rational approximants and real logarithms. A generic order contradiction replaces the hypotheses by the entire hard theorem and supplies no Roth content. |
| False-generalization guard | PASS | Do not drop Irrational from unreduced pairs: α=0 supplies infinitely many (0,q) for every κ. LiouvilleWith excludes exact equality and infers irrationality only above exponent1; our modern theorem splits p≤2 first. |

Modern-idiom verdict: available and verified. Use LiouvilleWith so mono, rational affine invariance
and exponent-loss API apply directly. The new bridge proofs are original scratch work. No cost
or inherited verdict enters the decision.

## Phase4.5 — infrastructure

Theorem: all six definition risks are n/a (diamond, reducibility leak, noncanonical unfolding,
instance priority, universe polymorphism and coercion ambiguity). No new instance or definition
is proposed by the original declaration. Scratch pairSet is a test representation only.

## Phase4.6 — proof strategy

| Question | Applies | Alternative |
|---|---|---|
| Topology εδ | No global replacement | Parameter continuity already uses ContinuousAt; the decisive theorem is arithmetic, not an εδ topology lemma. |
| Algebra elements vs subobjects | No | Integer monomials and denominator divisibility are the substantive content; subobject inclusion does not prove nonvanishing/size bounds. |
| Sequences vs filters | Yes for public API | State exponent exclusion with LiouvilleWith, retaining finite selection of rapidly increasing approximants for the proof. |
| Category universal property | No | No categorical construction. |
| Missing helpers mathlib should have | Yes | Upstream Hasse/Taylor/index/main-lemma dependencies in staged PRs; the new bridge from bounded-denominator pair sets to frequently-atTop and the exponent-family equivalence are new scratch proofs, not current API replacements. |

REFACTOR-RECOMMENDED for public API organization: preserve the finite multivariate arithmetic
proof, expose exponent exclusion through LiouvilleWith, and stage the missing Hasse/Taylor/index/
main-lemma API. Generic filter transport alone does not replace the proof.

## Phase5 — fifteen formal search cells

| Form | Method | Receipt |
|---|---|---|
| current | leanfinder | [formal-current-leanfinder.json](../evidence/Roth.roth_of_isIntegral/formal-current-leanfinder.json) |
| current | leansearch | [formal-current-leansearch.json](../evidence/Roth.roth_of_isIntegral/formal-current-leansearch.json) |
| current | loogle | [formal-current-loogle.json](../evidence/Roth.roth_of_isIntegral/formal-current-loogle.json) |
| current | rg | [formal-current-rg.json](../evidence/Roth.roth_of_isIntegral/formal-current-rg.json) |
| current | local | [formal-current-local.json](../evidence/Roth.roth_of_isIntegral/formal-current-local.json) |
| standard | leanfinder | [formal-standard-leanfinder.json](../evidence/Roth.roth_of_isIntegral/formal-standard-leanfinder.json) |
| standard | leansearch | [formal-standard-leansearch.json](../evidence/Roth.roth_of_isIntegral/formal-standard-leansearch.json) |
| standard | loogle | [formal-standard-loogle.json](../evidence/Roth.roth_of_isIntegral/formal-standard-loogle.json) |
| standard | rg | [formal-standard-rg.json](../evidence/Roth.roth_of_isIntegral/formal-standard-rg.json) |
| standard | local | [formal-standard-local.json](../evidence/Roth.roth_of_isIntegral/formal-standard-local.json) |
| abstract | leanfinder | [formal-abstract-leanfinder.json](../evidence/Roth.roth_of_isIntegral/formal-abstract-leanfinder.json) |
| abstract | leansearch | [formal-abstract-leansearch.json](../evidence/Roth.roth_of_isIntegral/formal-abstract-leansearch.json) |
| abstract | loogle | [formal-abstract-loogle.json](../evidence/Roth.roth_of_isIntegral/formal-abstract-loogle.json) |
| abstract | rg | [formal-abstract-rg.json](../evidence/Roth.roth_of_isIntegral/formal-abstract-rg.json) |
| abstract | local | [formal-abstract-local.json](../evidence/Roth.roth_of_isIntegral/formal-abstract-local.json) |

All methods actually executed. Finder’s external defaultv4.28.0 index and current web docs may
differ from the pin. Root local search returned index:error for all three queries; names returned
were retained and source-checked, but no local absence conclusion is made. Untruncated whole-tree
full-name search additionally excludes confusing this theorem with additive-combinatorics Roth
or Lüroth. Negative exact?/aesop probes are compile-checked search outcomes, not an absolute proof
that no possible mathlib derivation exists.

Closest pinned candidates: Liouville.exists_pos_real_of_irrational_root supplies a bound depending
on polynomial degree, insufficient for universal threshold2. LiouvilleWith.irrational only excludes
rationals above exponent1; mono/exponent-loss/affine invariance transport existing approximation
information. Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational is the opposite-direction
Dirichlet optimality statement. ae_not_liouvilleWith is almost-everywhere, not pointwise on every
algebraic irrational. None is a full Roth replacement. Pinned LiouvilleWith module introduction
explicitly names the missing p>2 algebraic-transcendence implication.

[Whole-tree search](../evidence/Roth.roth_of_isIntegral/full-name-search.json); [LiouvilleWith](../evidence/Roth.roth_of_isIntegral/mathlib-source-0.lean.txt); [Liouville bound](../evidence/Roth.roth_of_isIntegral/mathlib-source-1.lean.txt); [Dirichlet API](../evidence/Roth.roth_of_isIntegral/mathlib-source-2.lean.txt).

## Phase5.5 — statement shape

| Check | Verdict | Reason |
|---|---|---|
| Normal form | RESTATE-BEFORE-SHIP | Offer LiouvilleWith exponent exclusion as primary public API and finite-pair/irrational classical corollaries. No existing pinned canonical Roth theorem found. |
| Syntactic generality | Verified | Finite-for-κ>2 ↔ infinite-implies-κ≤2; all-exponent classical property ↔ LiouvilleWith exponent bound for irrational α. New predicates/bridges distinguish exact pair and rational semantics. |
| Superfluous arguments | NONE in original | α, hα, hint, κ and hinf all mathematically used; no κ>0 binder to remove. In the modern statement irrationality is derived when needed, not deleted unsafely. |

The finite-for-κ>2 formulation and exact classical recovery were compiled. Uniform IsDiophantine
is a project predicate with a complete bridge in LeanEval, not an existing mathlib replacement.
The full LeanEval module was re-elaborated in the caller test rather than assuming those two
predicates coincide. The α=0 native counterexample confirms why the old irrationality hypothesis
cannot simply be removed from the pair theorem. The p=1 rational LiouvilleWith guard prevents
inferring irrationality without its actual p>1 hypothesis.

## Phase6.0 — complete callers, inlining and duplications

One direct proof call: Roth.roth, Main577. No external-to-file direct proof calls; documentary
Main21 and declaration Main547 excluded. Canonical293 kernel-value audit independently finds
only Roth.roth, and no direct kernel-type consumer. Transitive users include roth_rat and the
LeanEval endpoint. Arbitrary simp closure is not inferred from source or direct kernel counts.

The exact original five-helper closure and full Roth.roth proof were replayed with the target
body inserted as a local integral_inline; original signature agreement holds. Full roth_rat and
all LeanEval declarations were then replayed through that caller. Additional kernel assertions
show all three endpoint replay values contain no direct reference to the original target.
Inlining preserves correctness; it does not make the hard proof an existing mathlib composition.

| A | B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| Integral Roth | Roth.roth | Special case | No; algebraic reduction invokes integral result | Keep integral proof core; algebraic extension is downstream |
| Integral Roth | Roth.roth_rat | Different domain/premise | No; num/den injection transports existing result | Retain representation corollary as needed |
| Exponent bound | LeanEval IsDiophantine | Equivalent for irrational α | No; exponent-gap/minimum argument | Choose public API and bridge once |
| Integral Roth | Generic order contradiction | No | Only final closure resembles it | Do not classify full named result as generic order wrapper |
[Caller inventory](../evidence/Roth.roth_of_isIntegral/callers.json); [Tracked search](../evidence/Roth.roth_of_isIntegral/tracked-source-search.json); [Inline search](../evidence/Roth.roth_of_isIntegral/inline-search.json); [Actual full inline/downstream source](../evidence/Roth.roth_of_isIntegral/callers2-executed.lean.txt).

## Phase6 — actual composition attempts

1. Degree-dependent Liouville bound cannot replace degree by2 for arbitrary integral equations.
2. LiouvilleWith.irrational/mono/affine invariance and frequently_lt_rpow_neg transport hypotheses;
   they do not provide exponent2 exclusion. The isolated negative exact?/aesop probes confirm
   those generic routes did not close the supplied Roth goal in this context.
3. The finite-set equivalence is generic order/set logic, but consumes the full exponent theorem.
   It is not a proof of that theorem. The modern equivalence also takes Roth content explicitly.
4. Imported project main_lemma and five private helpers do assemble the result, but these are
   project arithmetic theorems, not existing mathlib building blocks.

NOT-COMPOSABLE from current mathlib in≤3 existing calls. No simp-only closure is being sold as
new Roth content. The independently written bridge is not counted as an existing building block.

## Phase7 — upstream action

**YES-but-generalise-first**, MODERN-IDIOM. Add the actual algebraic-integer exponent2 exclusion
using the existing LiouvilleWith predicate. This fills the concrete theorem identified by that
module’s p>2 documentation, beyond its present elementary/affine API and beyond Liouville’s
degree-dependent bound. Keep the proven classical pair/finite formulations as recovery corollaries.
The modern theorem drops the explicit irrationality argument safely, handles the existential
constant and composes directly with LiouvilleWith.mono, rational affine invariance and
frequently_lt_rpow_neg. It preserves the named theorem’s full mathematical content.

Proposed new home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean`.
Proposed PR title: `feat(NumberTheory/DiophantineApproximation): prove Roth's theorem for algebraic integers`.
Stage after prerequisites; group the terminal arithmetic theorem with **already accepted YES**
Roth.main_lemma (progress snapshot checked), while shipping foundational accepted Hasse derivative/
Taylor/index API in prior PRs. Roth.exists_degrees and Roth.one_le_prod_pow_mul_abs_eval are also
accepted YES-but-generalise-first dependencies, not assumed already present in mathlib. No future
unassessed algebraic extension is described as already accepted.

Reviewer candidates based on actual relevant recent file history: Jovan Gerbscheid, whose
[2025-11-19 filter-negation API commit](https://github.com/leanprover-community/mathlib4/commit/66b2a6571bcd28f2ab6cd8e15f195d394fc175bd)
touches LiouvilleWith; Marcelo Lynch’s2026-08-11 cleanup also touches that exact file. These are
reviewer candidates, not claims of acceptance or subject-specialist endorsement.

Pre-PR checklist: `/generalise Roth.roth_of_isIntegral` against the exact modern signature above;
`/cleanup Roth/Main.lean Roth.roth_of_isIntegral` and prerequisite import/naming staging;
request reviewer feedback on the new DiophantineApproximation home and LiouvilleWith API.
Cost is not a verdict factor. Number-field/place extensions are separate mathematics, not an
excuse to downgrade or a claimed mechanically verified generalization.

[Reviewer commit receipt](../evidence/Roth.roth_of_isIntegral/reviewer-specific-commits.json); [Accepted grouping snapshot](../evidence/Roth.roth_of_isIntegral/progress-snapshot.json).

## Phase8 — verification and portability

Accepted exact original replay/type agreement/canonical293, full caller inlining, finite/recovery/
rational guard, unelided constant inventory, and isolated modern equivalence/recovery are archived
with complete root requests/raw receipts and elapsed milliseconds. Standard axioms only:
propext, Classical.choice, Quot.sound. Failed shape01 and modern01 attempts (including recovered
sorryAx diagnostics) are rejected evidence, preserved separately, never counted as verification.
Original pp.all body printer elides101777characters; initial aggregate constant printer elides462.
The exact complete written proof and separate306-info constant inventory remain available;
a full unelided kernel-body pretty-print is not claimed.

Stable mathlib-only18 and disk9 prefixes are checked against fixed portable SHA constants.
Root freshly authorized only LiouvilleWith as the19th isolated import after pinned-header read;
that exact prefix SHA is effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc.
No project import appears in isolated proofs. No limit raises or new axioms were used.

Portable validator checks current manifest hashes/bytes, links, exact canonical/private order293,
all17 pins, actual native receipt success/nonpartial format, approved prefixes, widths and source
bytes. Draft completion remainsfalse until actual scratch/integrated-layout/secret gates pass;
then final completion istrue. Root mathematical acceptance remainspending until independent review.

[Verification ledger](../evidence/Roth.roth_of_isIntegral/verification.json); [Portable validator](../evidence/Roth.roth_of_isIntegral/validate.py); [Current manifest](../evidence/Roth.roth_of_isIntegral/copy-manifest.json).
