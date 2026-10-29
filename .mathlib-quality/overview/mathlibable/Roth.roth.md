# `Roth.roth` — canonical288

Verdict: **YES-but-generalise-first**, reason **MODERN-IDIOM**. This is the named BIG Roth theorem
for irrational real algebraic numbers. Its short reduction proof does not make the full mathematical
content an existing mathlib composition. No parent verdict is inherited and cost is not a factor.

## Phase0 — baseline and scope

Fresh17 source/pin hashes match the tracked shared manifest; baseline build passed2467jobs.
The accepted file-end228 full build remains reusable; next literal file-end build is289.
Full Main588 and LeanEval66 were read, including algebraic-integral reduction and the entire
multivariate integral proof. Local paper§6 reduction and §7 conclusion were read. Production,
pins, Git, overview and progress remain unchanged. Root exclusively executed native/LSP requests.
Original replay contains exactly this target in a fresh namespace, with no helper closure needed;
public reduction and integral theorem remain imported. Full unrelated Main replay is not claimed.

[inputs.json](../evidence/Roth.roth/inputs.json); [baseline-build.txt](../evidence/Roth.roth/baseline-build.txt); [source-Main.lean.txt](../evidence/Roth.roth/source-Main.lean.txt); [source-LeanEval.lean.txt](../evidence/Roth.roth/source-LeanEval.lean.txt).

## Phase1 — exact statement and mathematics

```lean
∀ {α : ℝ}, Irrational α → IsAlgebraic ℚ α → ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite → κ ≤ 2
```

The pairs are unreduced; q is a positive natural denominator, h an integer, κ any real.
Assuming κ>2, choose positive M with Mα integral. Removing finitely many bounded-denominator
solutions preserves infinitude. Multiplication (h,q)↦(Mh,q) is injective. Choose κ′=(κ+2)/2;
eventually M/q^κ<1/q^κ′, so Mα has infinitely many κ′ approximants and remains irrational.
The integral theorem forces κ′≤2, a contradiction.

The integral theorem is the hard Roth mathematics: choose a monic integer equation and parameters
m,δ; select reduced approximants with rapidly growing denominators and balanced r_j log q_j.
The main lemma supplies a multivariate integer Q of high index at α, small Hasse derivatives and
nonzero value at the approximants. Clearing denominators bounds that value below; Taylor expansion
and the index bound estimate it above. Logarithmic comparison contradicts m(1+4δ)/(γ−η)<κ.
Generic order closure supplies only the final contradiction, not this polynomial theorem.

Direct canonical dependencies in the elaborated value: Roth.approxSet, Roth.reduction, Roth.roth_of_isIntegral.
Full kernel constant inventory and full type/axioms are retained. The pp.all proof-body printer
elides9674characters; no full kernel-body pretty-print is claimed. Exact complete original source
is retained and re-elaborated, with original/replay type agreement by proof irrelevance.

[original-executed.lean.txt](../evidence/Roth.roth/original-executed.lean.txt); [original-receipt.json](../evidence/Roth.roth/original-receipt.json); [local-section6.tex.txt](../evidence/Roth.roth/local-section6.tex.txt); [local-section7.tex.txt](../evidence/Roth.roth/local-section7.tex.txt).

## Phase2 — size and one-line check

BIG: named Roth theorem, main project endpoint, classical standard result. The four-line assembly
uses project Roth.reduction and Roth.roth_of_isIntegral, neither an existing mathlib replacement.
Definition-only one-line test: n/a theorem. All six infrastructure rows are n/a theorem; no new
instance, coercion, reducibility or diamond structure is introduced.

## Phase3 — exhaustive literature

| Channel | Exact actual query | Finding |
|---|---|---|
| web-specific | Roth theorem irrational algebraic numbers rational approximation finite exponent 2 original 1955 | Primary Roth1955 and author1958 search extract state the real algebraic irrational exponent bound and integral reduction. |
| web-general | Thue Siegel Roth theorem number field generalization irrationality measure | Classical number-field/finite-place and subspace extensions require heights and valuations, beyond mechanical field weakening. |
| web-alias | Roth theorem LiouvilleWith formalization Lean mathlib | Existing mathlib LiouvilleWith docs explicitly mention the Roth transcendence implication; searches locate no full endpoint. |
| nlab | site:ncatlab.org/nlab Roth theorem Diophantine approximation | Vojta page describes a broader arithmetic dictionary. Actual open fails unsupported XHTML; no direct usable generality result. |
| ncatlab | site:ncatlab.org/ncatlab Roth theorem algebraic approximation | Distinct namespace search issued, then retried with Diophantine approximation; returned /nlab results rather than matching /ncatlab theorem. |
| stacks | site:stacks.math.columbia.edu Roth theorem Diophantine approximation | Actual search and quoted Roth/approximation retry return no applicable Stacks statement; no absence inference. |
| mathoverflow | site:mathoverflow.net Roth theorem irrationality exponent generalizations | History149600 and variations459897 distinguish degree-dependent/ineffective bounds and stronger log refinements. Used for discovery, not authoritative replacements. |
| arxiv | site:arxiv.org Roth theorem Diophantine approximation algebraic after:2021-10-29 before:2026-10-30 | Initial broad query retrieved unrelated additive-combinatorics Roth results; targeted retry finds Goel–Lunia–Ray2502.00731v2 §3.2 and Hindes2209.09182 abstract. |

Local clean.tex§6/7 is available and read. Optional ask_chatgpt_math is unavailable, recorded n/a.
Every named channel was queried, including distinct /ncatlab and /nlab namespaces. Searches return
out-of-namespace results honestly; Stacks supplied no usable statement. The nLab Vojta open failed
unsupported XHTML; full ICM PDF open exceeded tool size, so only its returned primary search extract
is used. Web receipts retain exact requests, response hashes/bytes/status and clean locators,
with our concise summaries, and no full third-party article/search bodies. Signed or credential
query URLs are not retained. Initial recent query confused additive-combinatorics Roth; targeted
Diophantine retry found the relevant papers.

Standard name: Thue–Siegel–Roth theorem. Standard equivalent real forms are finite exceptions at
every exponent2+ε, infinite-implies-exponent≤2, and ε-dependent positive uniform error constants.
[Roth1955 original](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F), Mathematika2(1),1–20,
provides publication metadata and the degree-dependent Liouville precursor.
[Roth’s1958 lecture](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), opening§1–2 search extract,
states the exponent bound and integral reduction.
[Goel–Lunia–Ray2026](https://arxiv.org/html/2502.00731v2), §3.2 Theorems3.2–3.3,
gives number-field finite-place versions. These use heights/valuations and are not mechanical
weakenings of this real proof. [Hindes2022](https://arxiv.org/abs/2209.09182), abstract,
warns the characteristic-p analogue fails. We do not claim an arbitrary-field generalization.

[literature.json](../evidence/Roth.roth/literature.json); [web0](../evidence/Roth.roth/web-batch0.json), [web1](../evidence/Roth.roth/web-batch1.json), [web2](../evidence/Roth.roth/web-batch2.json), [web3](../evidence/Roth.roth/web-batch3.json), [web4](../evidence/Roth.roth/web-batch4.json), [web5](../evidence/Roth.roth/web-batch5.json), [web6](../evidence/Roth.roth/web-batch6.json).

## Phase4a–b — complete generality

| Parameter | Status | Reason |
|---|---|---|
| α : ℝ | Essential concrete arithmetic domain | Number-field/place versions exist, but are not a typeclass edit of this proof. No verified field weakening claimed. |
| Irrational α | Essential for current pair formulation | α=0 counterexample verified natively. Modern LiouvilleWith theorem can omit this binder because p>2 implies irrationality. |
| IsAlgebraic ℚ α | Essential semantic hypothesis | Reduction multiplies α by a nonzero integer to obtain an algebraic integer. General irrational reals admit exponent>2 approximations; no removal claimed. |
| κ : ℝ | Arbitrary real exponent | No missing positive κ binder: contradiction assumes 2<κ and hence supplies every positivity use. |
| approxSet Infinite | Infinitely many unreduced integer/natural pairs | Finite-for-κ>2 equivalent verified. Reduced rational formulation is separately derived, not definitionally the same set. |
| Fixed constant1 | Representational, not essential for exponent-bound family | LiouvilleWith existential C transported via q<p; equality at one fixed exponent is not asserted. |
| Threshold2 | Semantic sharp constant | Dirichlet gives infinite reduced approximations at exponent2; replacing2 by arbitrary threshold would lose the named theorem. |
| Positive natural denominators | Part of approximation domain | q=0 excluded explicitly; integer positive-denominator API in LeanEval is bridged by lift to ℕ, not arbitrary sign removal. |

Classical form: MAXIMALLY GENERAL within real rational approximation; no original hypothesis
can simply be dropped. κ>0 is unnecessary and absent. Threshold2 is mathematical and sharp;
finite-for-κ>2 is equivalent, whereas finiteness atκ=2 is false for irrational reals by Dirichlet.
A generic threshold would only abstract an order tautology after assuming Roth content.

Verified modern restatement:
```lean
∀ {α p : ℝ}, IsAlgebraic ℚ α → LiouvilleWith p α → p ≤ 2
```
The isolated source reconstructs the exact pair predicate using mathlib operations and guards
Roth.roth/Roth.approxSet absence. It takes classical Roth as an explicit premise; it does not
pretend this premise is already mathlib. The all-exponent classical property for irrational α
is equivalent to the all-exponent LiouvilleWith upper bound. One direction uses bounded-denominator
finiteness to produce frequent denominators with C=1. Conversely, LiouvilleWith p α supplies
constant1 approximants at the smaller exponent (p+2)/2 through frequently_lt_rpow_neg.
The modern algebraic theorem needs no explicit irrationality binder: split p≤2 first, and when
p>2 use LiouvilleWith.irrational with 1<p. The original theorem is recovered using irrationality.
This is NOT a fixed-exponent equivalence between constant1 pair membership and existential C.
The bridge is new conditional proof, adapted from accepted287 syntax and independently compiled
with algebraicity premises; no prior verdict or unverified proof is inherited.

## Phase4c — modern idioms

| Question | Applies | Concrete consequence |
|---|---|---|
| Typeclasses | No | Irrationality/algebraicity are point properties, not competing algebra structures; retain proposition hypotheses. |
| Filters | Yes | LiouvilleWith uses frequently atTop denominators and an existential multiplicative constant. The verified all-exponent bridge absorbs that constant by a strict exponent gap. |
| Universal property | No | No constructed object is characterized by a universal property. |
| Bundled substructures | No | The approximation set is not closed under algebraic operations; no Submodule/Subring replacement. |
| Hierarchy weakening | No | The complete proof needs real absolute value, logarithms, rpow, and integer denominator arithmetic; arbitrary ordered fields are not mechanically supported. |
| Higher categories | No | No categorical content. |
| Concrete indices | No | Integer numerators/natural positive denominators encode rational approximation. Arbitrary monoids would change the theorem; number-field heights require a separate arithmetic development. |
| Concrete-via-abstract diagnostic | No; abstraction rejected | The body forwards hα and halg to reduction and invokes roth_of_isIntegral. There is no named fixed α or initial unfolding rewrite. Generic contradiction after supplying the integral Roth theorem is abstraction of the full hard premise, not new Roth mathematics. A generic order contradiction replaces the hypotheses by the entire hard theorem and supplies no Roth content. |
| False-generalization guard | PASS | Do not drop Irrational from unreduced pairs: α=0 supplies infinitely many (0,q) for every κ. LiouvilleWith excludes exact equality and infers irrationality only above exponent1; our modern theorem splits p≤2 first. |

Modern-idiom verdict: verified and a real organizational improvement. Existing mono, exponent-loss,
rational/integer/natural scaling and rational-translation API accepts LiouvilleWith directly.
This meets the pinned module’s explicit missing p>2 transcendence implication. The original pair
corollary stays useful; no whole development need be generalized to heights or arbitrary fields.

## Phase4.5 — six infrastructure risks

| Risk | Status | Reason |
|---|---|---|
| diamond | n/a | Theorem; introduces no definition, instance or coercion |
| reducibility | n/a | Theorem; introduces no definition, instance or coercion |
| unfolding | n/a | Theorem; introduces no definition, instance or coercion |
| priority | n/a | Theorem; introduces no definition, instance or coercion |
| universe | n/a | Theorem; introduces no definition, instance or coercion |
| coercion | n/a | Theorem; introduces no definition, instance or coercion |

## Phase4.6 — proof strategy

| Question | Applies | Alternative |
|---|---|---|
| Topology εδ | No global replacement | Parameter continuity already uses ContinuousAt; the decisive theorem is arithmetic, not an εδ topology lemma. |
| Algebra elements vs subobjects | No | Integer monomials and denominator divisibility are the substantive content; subobject inclusion does not prove nonvanishing/size bounds. |
| Sequences vs filters | Yes for public API | State exponent exclusion with LiouvilleWith, retaining finite selection of rapidly increasing approximants for the proof. |
| Category universal property | No | No categorical construction. |
| Missing helpers mathlib should have | Yes | Upstream Hasse/Taylor/index/main-lemma dependencies in staged PRs; the new bridge from bounded-denominator pair sets to frequently-atTop and the exponent-family equivalence are new scratch proofs, not current API replacements. |

REFACTOR-RECOMMENDED for public API: preserve integral auxiliary-polynomial proof and reduction,
expose LiouvilleWith exponent exclusion; stage reusable Hasse/Taylor/index/main-lemma prerequisites.
No alternative generic filter/order theorem supplies the Roth arithmetic.

## Phase5 — all fifteen formal cells

| Form | Method | Receipt |
|---|---|---|
| current | leanfinder | [formal-current-leanfinder.json](../evidence/Roth.roth/formal-current-leanfinder.json) |
| current | leansearch | [formal-current-leansearch.json](../evidence/Roth.roth/formal-current-leansearch.json) |
| current | loogle | [formal-current-loogle.json](../evidence/Roth.roth/formal-current-loogle.json) |
| current | rg | [formal-current-rg.json](../evidence/Roth.roth/formal-current-rg.json) |
| current | local | [formal-current-local.json](../evidence/Roth.roth/formal-current-local.json) |
| standard | leanfinder | [formal-standard-leanfinder.json](../evidence/Roth.roth/formal-standard-leanfinder.json) |
| standard | leansearch | [formal-standard-leansearch.json](../evidence/Roth.roth/formal-standard-leansearch.json) |
| standard | loogle | [formal-standard-loogle.json](../evidence/Roth.roth/formal-standard-loogle.json) |
| standard | rg | [formal-standard-rg.json](../evidence/Roth.roth/formal-standard-rg.json) |
| standard | local | [formal-standard-local.json](../evidence/Roth.roth/formal-standard-local.json) |
| abstract | leanfinder | [formal-abstract-leanfinder.json](../evidence/Roth.roth/formal-abstract-leanfinder.json) |
| abstract | leansearch | [formal-abstract-leansearch.json](../evidence/Roth.roth/formal-abstract-leansearch.json) |
| abstract | loogle | [formal-abstract-loogle.json](../evidence/Roth.roth/formal-abstract-loogle.json) |
| abstract | rg | [formal-abstract-rg.json](../evidence/Roth.roth/formal-abstract-rg.json) |
| abstract | local | [formal-abstract-local.json](../evidence/Roth.roth/formal-abstract-local.json) |

All methods were actually executed. Finder uses externalv4.28 index; external search versions can
differ from the pin. Actual local current/standard returned index:error and abstract warming;
no absence conclusion is drawn. The untruncated source search additionally checks full name and
statement variants; no truncation hides additive-combinatorics Roth or Lüroth collisions.

Positive candidates read from the pin and checked natively: Liouville.exists_pos_real_of_irrational_root
has polynomial-degree exponent, insufficient for sharp2 in all degrees. LiouvilleWith.irrational
excludes rationals above1, while mono/frequently_lt_rpow_neg/affine invariance transport approximation
information. Dirichlet’s infinite rational exponent2 theorem is a lower-side optimality statement.
The almost-everywhere ae_not_liouvilleWith theorem cannot specialize to every algebraic irrational.
Pinned LiouvilleWith introduction explicitly identifies the unproved Roth implication. Existing
Liouville.transcendental assumes approximations of every natural order, far stronger than one p>2.
Negative exact?/aesop probes compile, recording failure of those generic routes, not a universal
proof of absence. New scratch bridges never count as existing mathlib replacement theorems.

[mathlib-source-0.lean.txt](../evidence/Roth.roth/mathlib-source-0.lean.txt); [mathlib-source-1.lean.txt](../evidence/Roth.roth/mathlib-source-1.lean.txt); [mathlib-source-2.lean.txt](../evidence/Roth.roth/mathlib-source-2.lean.txt); [modern2-executed.lean.txt](../evidence/Roth.roth/modern2-executed.lean.txt).

## Phase5.5 — statement shape

| Check | Verdict | Reason |
|---|---|---|
| Normal form | RESTATE-BEFORE-SHIP | Offer LiouvilleWith exponent exclusion as primary public API and finite-pair/irrational classical corollaries. No existing pinned canonical Roth theorem found. |
| Syntactic generality | Verified | Finite-for-κ>2 ↔ infinite-implies-κ≤2; all-exponent classical property ↔ LiouvilleWith exponent bound for irrational α. New predicates/bridges distinguish exact pair and rational semantics. |
| Superfluous arguments | NONE in original | α, hα, halg, κ and hinf all mathematically used; no κ>0 binder to remove. In the modern statement irrationality is derived when needed, not deleted unsafely. |

Finite-for-κ>2 equivalence and original recovery are native verified. The α=0 infinite unreduced
pair counterexample for every κ confirms irrationality is essential in the original. LiouvilleWith1
holds even for0, so irrationality is inferred only with p>1. The full LeanEval bridge proves the
uniform lower-bound equivalence for irrational α; no equivalence on all reals is asserted.

## Phase6.0 — actual callers, inline audit and duplications

| Caller | Location | Uses | Inlining |
|---|---|---|---|
| Roth.roth_rat | Roth/Main.lean:583 | 1 | Full original body, original signature, exact target proof inlined |
| LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth | Roth/LeanEval.lean:64 | 1 | Full original body, original signature, exact target proof inlined |

One same-file and one external-file direct proof call. Documentation is excluded from the count.
Canonical293 audit independently finds exactly these two direct body consumers and no type consumer;
requested/unique/present/values are each293. No simp attribute and no arbitrary simp/transitive
closure claim. Both complete caller bodies, and the whole LeanEval module, were re-elaborated.
Kernel assertions confirm both endpoint proof values contain no direct target reference.

Integral Roth is the proof core; algebraic Roth adds integer scaling and exponent loss. roth_rat
maps rational values injectively to reduced numerator/denominator pairs. LeanEval minimizes the
weighted error on finitely many exceptions and handles the remaining pairs. Their mathematical
content is equivalent under irrationality, but these are actual representation bridges, not
identical proof copies. No independent full Roth theorem is silently rederived inline elsewhere.
Inlining succeeds, but does not make Roth junk or a composition from existing mathlib.

[callers.json](../evidence/Roth.roth/callers.json); [source-search.json](../evidence/Roth.roth/source-search.json); [tracked-source-search.json](../evidence/Roth.roth/tracked-source-search.json); [inline-search.json](../evidence/Roth.roth/inline-search.json); [callers2-executed.lean.txt](../evidence/Roth.roth/callers2-executed.lean.txt).

## Phase6 — actual composition experiments

NOT-COMPOSABLE from≤3 existing mathlib calls. Degree-dependent Liouville cannot give2 in arbitrary
degree. Irrationality/affine/mono/exponent-loss lemmas do not exclude LiouvilleWith p above2.
Native exact?/aesop attempts fail to derive the bound. Set/order finiteness equivalences consume
Roth content. The short original invokes project reduction and integral Roth, not mathlib Roth.
No simp-only closure is promoted as new arithmetic. The independently adapted exponent-family
bridge is new conditional mathematics, separate from existing pinned API.

## Phase7 — verdict and concrete upstream plan

**YES-but-generalise-first**, MODERN-IDIOM: expose the verified algebraic LiouvilleWith exponent
bound and recover classical finite/pair corollaries. This fills the explicit p>2 transcendence gap
named in the pinned LiouvilleWith introduction, beyond elementary irrationality, affine invariance
and degree-dependent Liouville. It is a terminal addition to the staged Roth proof, not a request
to mechanically port the entire proof to number-field heights. Irrationality is safely removed
only in the modern theorem, whose approximation premise excludes exact equality.

Exact proposed new home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean`.
Proposed PR title: `feat(NumberTheory/DiophantineApproximation): prove Roth's theorem for algebraic reals`.
Group the endpoint with already accepted YES Roth.roth_of_isIntegral and Roth.main_lemma; ship accepted
Hasse/Taylor/index prerequisites earlier. The progress snapshot actually confirms these assessments;
accepted assessment does not mean the theorem already exists in mathlib. Avoid import cycles:
prove the integral core first, then scaling/algebraic endpoint; do not use Roth.roth to prove its
own upstream integral premise.

Reviewer candidates from actual relevant recent history: Jovan Gerbscheid’s
[filter-negation change2025-11-19](https://github.com/leanprover-community/mathlib4/commit/66b2a6571bcd28f2ab6cd8e15f195d394fc175bd)
touches LiouvilleWith; Marcelo Lynch’s2026-08-11 exact-file cleanup also supplies a recent reviewer
candidate. This is history-based selection, not an endorsement or claim they accepted the proposal.
Pre-PR: `/generalise Roth.roth` against the exact modern signature, then
`/cleanup Roth/Main.lean Roth.roth`; stage prerequisite imports, names and documentation before PR.

[reviewer-specific-commits.json](../evidence/Roth.roth/reviewer-specific-commits.json); [progress-snapshot.json](../evidence/Roth.roth/progress-snapshot.json).

## Phase8 — actual verification and portability

Five accepted executions: original exact replay/type/axioms/canonical293; complete caller inlining;
clean finite/recovery/rational guard; caller target-free assertions; isolated modern bridge/recovery.
All actual root receipts and source hashes/timings are retained. Only propext, Classical.choice,
Quot.sound occur in accepted proofs. Failed shape01 and modern01, with recovered sorryAx, remain
separately rejected and never count as verification. Original #print elision is disclosed above;
full unelided constant/type messages and exact written source remain available.

Stable mathlib18 and disk9 hashes remain fixed. Root freshly authorized precisely LiouvilleWith as
isolated19 after pinned-header read; prefixSHA effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc.
No project import in isolated probes; no new axioms, unsafe/native_decide or raised limits.
The portable read-only validator checks current manifest/hash/bytes/links, both layouts, actual
native complete success and all source/pin controls. Completion remainsfalse/phase8pending until
actual draft scratch/integrated-layout/secret gates pass; final completion is settrue only afterward.
Root acceptance stayspending for independent review. Native execution requests are released.
Initial packaging-only draft validation rejected a normalized copy of the disk prefix; exact control
bytes were restored before the successful draft gates. Both rejected packaging receipts remain.
No executed Lean source or raw receipt changed. Copied prefixes retain their exact EOF whitespace;
only authored report/preparation scripts are normalized, and generators do not normalize prefixes.

[verification.json](../evidence/Roth.roth/verification.json); [validate.py](../evidence/Roth.roth/validate.py); [copy-manifest.json](../evidence/Roth.roth/copy-manifest.json).
