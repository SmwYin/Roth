# Roth.exists_approximants — canonical277

**Verdict: BORDERLINE-needs-human.** Keep the arithmetic packaging local while deciding whether
cofinal-height recursive selection deserves a public API. All final package gates passed; this is a completed mathematical
assessment; the three upstream design questions are not a user
blocker. No verdict is inherited from the reduced-approximation selector or another declaration.
Cost is not a verdict factor.

## Phase0 — baseline and provenance

The unchanged production statement resolves at Roth/Main.lean256. Kind: theorem; no sorry in
original source. Main proves Roth's theorem by reduction, parameter and approximant selection,
polynomial construction, and a logarithmic contradiction. The shared baseline succeeded with2467
jobs; all17 current production-source/pin hashes freshly match its tracked manifest. The accepted
Theta228 file-boundary build remains applicable; the next requested literal build is289.
No build was required at277. Root exclusively executed native/project-LSP operations; this worker
prepared immutable source/request archives and inspected the complete raw returned diagnostics.

[baseline-build.txt](../evidence/Roth.exists_approximants/baseline-build.txt), [inputs.json](../evidence/Roth.exists_approximants/inputs.json), [fresh-final-inputs.json](../evidence/Roth.exists_approximants/fresh-final-inputs.json).
Original re-elaboration scope is exactly the target theorem, renamed `replay` in a fresh namespace
with public project ingredients imported. There is no private helper closure to copy. Native
proof-irrelevance equality verifies the exact original/replay type; it does not identify proof
construction. The293-name audit derives directly from tracked declaration order, preserving
private modules, and verifies exact order/uniqueness/presence/values. Native full type and axioms
were captured via `Lean.getConstInfo` and tagged `pp.funBinderTypes`. Both original and scope executions request the original `pp.all #print`; each
contains the same79277-character printer elision; a full kernel-body dump is not claimed.

[original-executed.lean.txt](../evidence/Roth.exists_approximants/original-executed.lean.txt), [original-receipt.json](../evidence/Roth.exists_approximants/original-receipt.json), [native-type.json](../evidence/Roth.exists_approximants/native-type.json).

## Phase1 — mathematical content

From infinitely many fixed-constant approximating pairs for an irrational real number, select any
nonzero finite number of reduced pairs. Every denominator exceeds1, the first logarithm strictly
exceeds an arbitrary real L, and each adjacent logarithm strictly exceeds2/δ times its predecessor.
The actual δ parameter is arbitrary real. For δ≤0 the inequality does not assert an increasing
sequence: at δ=0 totalized division makes its left factor0. No hidden positivity assumption is
added.

The proof calls `Roth.exists_reduced_approx` for an unbounded-denominator selector, recursively
chooses above natural ceilings of exp(L) and powered previous denominators, and applies
`Real.lt_log_of_rpow_lt`. Coprimality and q>1 are carried at every recursive step.

Full native type:

```lean
∀ {α : ℝ},
  Irrational α →
    ∀ {κ : ℝ},
      0 < κ →
        (Roth.approxSet α κ).Infinite →
          ∀ (m : ℕ) [inst : NeZero m] {δ : ℝ} (L : ℝ),
            ∃ (h : Fin m → ℤ) (q : Fin m → ℕ),
              (∀ (j : Fin m), (h j, q j) ∈ Roth.approxSet α κ) ∧
                (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) ∧
                  (∀ (j : Fin m), 1 < q j) ∧
                    L < Real.log ↑(q 0) ∧ ∀ (i j : Fin m), ↑i + 1 = ↑j → 2 / δ * Real.log ↑(q i) < Real.log ↑(q j)
```

Parameters/hypotheses and every generality finding appear in Phase4. Written project dependencies
in tracked canonical order are exactly `Roth.approxSet`, `Roth.exists_reduced_approx`.
Generated kernel constants, lexical occurrences, direct type/value consumers, and transitive
consumers are distinct scopes.

## Phase2 — size and definition-only checks

SMALL: auxiliary selection theorem, neither a new structure nor a named main result.
One-line definition test: n/a, theorem. All six infrastructure risks are n/a for a theorem:
no instance diamond, reducibility leak, noncanonical data unfolding, priority registration,
universe-constrained data instance, or new coercion. Detailed reasons: [phase-checks.json](../evidence/Roth.exists_approximants/phase-checks.json).

## Phase3 — exhaustive literature

Every named channel was attempted, including the distinct /ncatlab namespace and a dated recent
arXiv query. General queries differ in specific, abstract, and alias formulations. Only exact
requests, response SHA/byte/status, titles/URLs/locators, and original concise summaries are
persisted; no third-party article or search-response bodies are archived.

| Channel | Actual query | Finding and source locator |
|---|---|---|
| web-specific | Roth theorem proof choose reduced approximations denominators q j rapidly increasing logarithms | Author exposition explicitly chooses a finite list with rapidly increasing denominators; not a named general finite-chain theorem. [An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf); §2, page3 and §6. [request/fingerprint](../evidence/Roth.exists_approximants/web-specific.json) |
| web-general | unbounded set real numbers recursively choose sequence prescribed growth dependent choice | Recursive witness selection is a dependent-choice pattern. Exact arithmetic approximation is additional input. [Axiom of Choice, Eric Schechter](https://math.vanderbilt.edu/schectex/ccc/choice.html); Choice variants. [request/fingerprint](../evidence/Roth.exists_approximants/web-general.json) |
| web-alias | Roth theorem gap principle rational approximations lacunary denominators | Gap principles constrain all sufficiently good reduced approximants; our theorem instead selects a sparse finite subsequence. Do not identify these statements. [Geometric Number Theory](https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf); §4.5, Lemma4.5.3. [request/fingerprint](../evidence/Roth.exists_approximants/web-alias.json) |
| nlab | site:ncatlab.org/nlab axiom dependent choice sequence | Serial relations admit recursively linked countable choices. Direct opening returned unsupported application/xhtml+xml; search evidence alone retained. [dependent choice in nLab](https://ncatlab.org/nlab/show/dependent%20choice); search result; direct fetch unsupported XHTML. [request/fingerprint](../evidence/Roth.exists_approximants/nlab.json) |
| ncatlab | site:ncatlab.org/ncatlab cofinal sequence dependent choice | Returned /nlab and other out-of-namespace results. No exact namespace hit; no categorical generalization claimed. No exact /ncatlab namespace result; actual site:ncatlab.org/ncatlab query. [request/fingerprint](../evidence/Roth.exists_approximants/ncatlab.json) |
| stacks | site:stacks.math.columbia.edu dependent choice cofinal sequence | A countable directed inverse-system proof constructs a cofinal sequence by induction. Useful structural analogy, not a Diophantine chain statement. [Lemma10.86.3 (0597)](https://stacks.math.columbia.edu/tag/0597); proof, cofinal sequence and choice. [request/fingerprint](../evidence/Roth.exists_approximants/stacks.json) |
| mathoverflow | site:mathoverflow.net Roth theorem gap principle denominators | Search finds quantitative finiteness/gap questions, not exact arbitrary-cofinal-height finite selection API. [Estimate number of solutions in the Roth’s theorem](https://mathoverflow.net/questions/249176/estimate-number-of-solutions-in-the-roths-theorem/249191); discussion of quantitative Roth. [request/fingerprint](../evidence/Roth.exists_approximants/mathoverflow.json) |
| arxiv | site:arxiv.org Roth theorem gap principle rational approximations after:2021-10-29 before:2026-10-30 | Function-field transcendence analogue appeared in the dated query. Other hits were additive Roth/irrelevant approximation papers; no exact finite-selection result found. Refined dated Diophantine gap query returned empty. [Transcendence of continued fractions over function fields and a quantitative version of Uchiyama’s theorem](https://arxiv.org/abs/2608.15119); 2026 search result. [request/fingerprint](../evidence/Roth.exists_approximants/arxiv.json) |
| Local | reduced solutions / choose solutions / eq50 | clean.tex1572–1613, §7: unbounded reduced denominators and successive strict log ratios. [literature-local.json](../evidence/Roth.exists_approximants/literature-local.json), [local-excerpt.tex.txt](../evidence/Roth.exists_approximants/local-excerpt.tex.txt) |
| Optional ChatGPT math | n/a | ask_chatgpt_math unavailable; all other channels still executed. |

The author's [elementary Roth exposition](https://aleksa-milojevic.github.io/expository/roth.pdf)
explicitly chooses rapidly increasing denominators in §2 page3; it dates itself January2022.
The literature distinguishes this freedom to choose a sparse subsequence from the gap principle,
which constrains all sufficiently good approximants. The [Stacks proof0597](https://stacks.math.columbia.edu/tag/0597)
constructs a cofinal sequence inductively in a different setting; it is an analogy, not the same
arithmetic theorem. nLab direct opening failed on unsupported XHTML; the distinct /ncatlab query
returned only out-of-namespace hits. The refined dated arXiv Diophantine gap query returned empty;
the first dated query also returned additive-Roth and irrelevant approximation papers, retained
honestly as search noise. [primary.json](../evidence/Roth.exists_approximants/primary.json), [literature.json](../evidence/Roth.exists_approximants/literature.json).

Standard mechanism: recursively select from a cofinal set, with arbitrary starting bound and
prescribed growth. The factor2/δ is downstream parameter bookkeeping. Reducedness and fixed1
approximation membership remain substantive arithmetic input; a generic recursion does not
prove them.

## Phase4a–4b — parameter-by-parameter generality

| Parameter/hypothesis | Finding |
|---|---|
| α : ℝ | Concrete Diophantine approximation content retained; abstract arbitrary A height construction independently verified. |
| Irrational α | Essential to arbitrary unreduced-infinitude formulation: α0 κ3 yields no reduced q>1 chain despite infinitely many exact pairs. |
| κ : ℝ | Arbitrary real κ valid after removing positivity. New signed selector proof combines original positive fiber proof with Dirichlet for nonpositiveκ. |
| 0<κ | Verified removable: signed01 unrestricted and edges02 exact original signature through unrestricted theorem. |
| hinf | Required input of high-exponent branch; κ≤2 branch independently obtains reduced approximants without it. No claim that it is universally redundant. |
| m : ℕ, NeZero m | Every nonzero length permitted; first q0 needs nonzero instance. Empty form separately compiled without start bound. |
| δ : ℝ | Already completely unrestricted; zero/negative cases totalized division. Edges02 tests0,-1; never add δ>0. |
| L : ℝ | Arbitrary strict initial log threshold retained. Generic cofinal height transport uses exp L and Nat.ceil. |
| 2/δ | Representation of arbitrary real multiplier c; stronger arbitrary recursive F tested. No positivity needed for construction. |
| h,q output | Full Fin m→ℤ / Fin m→ℕ coordinates, coprimality, q>1 and adjacency retained. Rat is a possible semantic representation; no definitional equality asserted without bridge. |

**Verified weakening:** κ positivity is unnecessary for the complete original conclusion.
For κ>0 the finite-fiber reduction proof supplies unbounded reduced approximants. For κ≤0,
Dirichlet's existing exponent2 rational approximation theorem supplies infinitely many reduced
rationals; bounded-denominator finiteness and monotonicity in the exponent provide the needed
selector. More generally κ≤2 needs no supplied infinitude. These selector proofs are newly
written scratch mathematics, credited to prior274 as proof templates and independently rechecked
here. They are not existing mathlib theorems and are not inherited assessment evidence.

[signed-executed.lean.txt](../evidence/Roth.exists_approximants/signed-executed.lean.txt), [signed01-receipt.json](../evidence/Roth.exists_approximants/signed01-receipt.json).
Full original positive-κ signature is recovered specifically through the unrestricted theorem;
δ=0 and δ=−1 full-output specializations also compile. [edges2-executed.lean.txt](../evidence/Roth.exists_approximants/edges2-executed.lean.txt), [edges02-receipt.json](../evidence/Roth.exists_approximants/edges02-receipt.json).

Irrationality is protected by a checked counterexample: α=0, κ=3 has infinitely many exact
unreduced pairs, yet no coprime approximating pair with q>1 and hence no m=1 output chain.
This is a full-family obstruction, not merely failure of one proposed witness.
[counterexample2-executed.lean.txt](../evidence/Roth.exists_approximants/counterexample2-executed.lean.txt), [counterexample02-receipt.json](../evidence/Roth.exists_approximants/counterexample02-receipt.json).

Generality status: strictly narrower in κ, and abstractable in witness/height/growth semantics.
The finite-chain proof tested for arbitrary real c and arbitrary objects A has a stronger
infinite-sequence version with arbitrary time-dependent threshold F. Empty-chain restatement
requires omitting the nonexistent first entry; its separate no-start form is compiled.
No weakening of the real analytic approximation theory to arbitrary fields is claimed.

## Phase4c — nine modern-idiom checks

| Question | Answer and downstream consequence |
|---|---|
| Typeclasses | No: cofinality/admissibility is value data, not a canonical global instance. Do not introduce a custom typeclass for one chosen set. |
| Filters | Yes as input language: cofinality is ¬BddAbove(height image), equivalence compiled. Sequence output is needed for finite adjacent coordinates; a bare Tendsto is insufficient for the exact gaps. |
| Universal properties | No: existential selection has no uniqueness or universal mapping property. |
| Bundled structures | Possible subtype s carries reducedness and admissibility; no closure predicate making it a subring/submodule. New bundled structure unnecessary. |
| Hierarchy | Real log/rpow arithmetic belongs to the specialization. Generic recursion uses only height cofinality and threshold choice; broader ordered-height hierarchy is not claimed mechanically verified here. |
| Higher categories | No: no categorical construction or morphism occurs. |
| Concrete indices | Yes: arbitrary A and height A→ℝ, arbitrary F:ℕ→ℝ→ℝ, arbitrary multiplier c:ℝ verified. Natural time supplies recursion; empty finite form separately verified. |
| Concrete-via-abstract | Yes: α,κ and irrationality enter only via the reduced selector; generic cofinal-height finite-chain theorem and complete exact old recovery compiled. |
| False-generalization guard | Pass: exact recovery retains admissibility, coprimality, q>1, strict L bound, NeZero m, all real δ and adjacent strict gap. Generic construction is new proof, not an existing mathlib replacement. |

Concrete-via-abstract diagnostic: α and κ enter only through the initial selector and the
membership assertion. The remaining recursion constructs height-separated witnesses.
[concrete-diagnostic.json](../evidence/Roth.exists_approximants/concrete-diagnostic.json). Genuine organizational improvement: isolate selection from
integer/rational representation, permit arbitrary real growth factors, and use unbounded-image
API. The exact recovery still proves cofinal logarithmic height using exp/ceiling and preserves
all original output fields. It does not replace the theorem by a hypothesis supplying its conclusion.

Verified generic signature (new scratch proof):

```lean
∀ {A : Type*} (s : Set A) (height : A → ℝ), (∀ B : ℝ, ∃ a ∈ s, B < height a) → ∀ (F : ℕ → ℝ → ℝ) (L : ℝ), ∃ f : ℕ → A, (∀ k, f k ∈ s) ∧ (∀ k, 0 < height (f k)) ∧ L < height (f 0) ∧ ∀ k, F k (height (f k)) < height (f (k+1))
```

[generic-executed.lean.txt](../evidence/Roth.exists_approximants/generic-executed.lean.txt), [generic01-receipt.json](../evidence/Roth.exists_approximants/generic01-receipt.json).
The full old statement follows from the generic finite chain with A=ℤ×ℕ,
s={admissible coprime pairs with q>1}, height=log denominator, and c=2/δ. Exact original/recovered
type equality also compiles in the real project context.
[recovery-executed.lean.txt](../evidence/Roth.exists_approximants/recovery-executed.lean.txt), [recovery01-receipt.json](../evidence/Roth.exists_approximants/recovery01-receipt.json).

## Phase4.6 — five proof-strategy checks

| Question | Answer |
|---|---|
| Topology | No ε–δ argument. Log/exp inequality is a monotone height transport; no topology refactor needed. |
| Algebra | No ideal/submodule argument. Reducedness is supplied by an arithmetic selector; not replaceable by an abstract ring assumption. |
| Analysis sequences | Sequence is a witness constructor, not a convergence proof. Filters can express cofinality, but prescribed adjacent gaps still need selection. |
| Universal construction | No universal property to replace a recursive witness choice. |
| Missing helper | Potential reusable cofinal-height sequence with arbitrary recursive thresholds. New generic proof tested; existing Set.seq_of_forall_finite_exists is a broader selection primitive requiring additional finite-bound work. |

Strategy verdict: REFACTOR-RECOMMENDED if a general selection API is adopted; arithmetic
cofinality feeds generic recursive selection. Existing direct recursion is mathematically sound.
Neither cost nor brevity establishes the upstream verdict.

## Phase5 — fifteen actual formal-search cells

| Form | Lean-Finder | Loogle | LeanSearch | Source rg | Root local LSP |
|---|---|---|---|---|---|
| current | [leanfinder](../evidence/Roth.exists_approximants/formal-current-leanfinder.json) | [loogle](../evidence/Roth.exists_approximants/formal-current-loogle.json) | [leansearch](../evidence/Roth.exists_approximants/formal-current-leansearch.json) | [rg](../evidence/Roth.exists_approximants/formal-current-rg.json) | [local](../evidence/Roth.exists_approximants/formal-current-local.json) |
| standard | [leanfinder](../evidence/Roth.exists_approximants/formal-standard-leanfinder.json) | [loogle](../evidence/Roth.exists_approximants/formal-standard-loogle.json) | [leansearch](../evidence/Roth.exists_approximants/formal-standard-leansearch.json) | [rg](../evidence/Roth.exists_approximants/formal-standard-rg.json) | [local](../evidence/Roth.exists_approximants/formal-standard-local.json) |
| abstract | [leanfinder](../evidence/Roth.exists_approximants/formal-abstract-leanfinder.json) | [loogle](../evidence/Roth.exists_approximants/formal-abstract-loogle.json) | [leansearch](../evidence/Roth.exists_approximants/formal-abstract-leansearch.json) | [rg](../evidence/Roth.exists_approximants/formal-abstract-rg.json) | [local](../evidence/Roth.exists_approximants/formal-abstract-local.json) |

Current form finds Dirichlet and Liouville-family candidates, not the old output chain.
Standard form finds `Nat.exists_strictMono_subsequence` and
`Filter.extraction_forall_of_frequently`; abstract form finds
`Set.seq_of_forall_finite_exists` and cofinal constructions. All three local requests returned
`index:error` with1/2/3 hits respectively; this is degraded indexing, never absence evidence.
Remote indexes may differ from the pin. The finite-history, strict-monotone, frequent-extraction, unbounded-image and log
candidate signatures were checked natively; cofinal bundles and LiouvilleWith were inspected in
pinned source. Current pinned modules are archived with hashes. [formal-search-matrix.json](../evidence/Roth.exists_approximants/formal-search-matrix.json), [mathlib-inputs.json](../evidence/Roth.exists_approximants/mathlib-inputs.json).

`Set.seq_of_forall_finite_exists` relates the next element to its finite predecessor image;
applying it here requires proving a finite upper-bound selection premise and transporting its
outputs. Strictly increasing natural subsequences alone do not provide arbitrary adaptive
real-logarithmic growth. `Order.sequenceOfCofinals` supplies monotonicity and membership in fixed
countably indexed cofinal sets; the pinned source does not supply this exact recursive gap law.

The pinned `LiouvilleWith p x` has an existential approximation constantC, frequent natural
denominators, and excludes exact equality. Its `exists_pos` adds positive C and positive
denominators, `mono` weakens exponent, and `frequently_lt_rpow_neg` absorbs C only with a strict
exponent loss. It is not the fixed1 `approxSet α κ`, nor a reduced-pair set, nor the
uniform-for-every-ε lower-bound `IsDiophantine` API. For p≤1 it can hold for rational x. Its
pinned source is inspected, not claimed as a native exact equivalence or ≤3-call replacement.

## Phase5.5 — three statement-shape checks

| Check | Finding |
|---|---|
| Normal form | Pair coordinates with coprimality versus Rat normalized fractions; finite chain versus infinite sequence; log gap versus power gap. Keep original pair form at sole caller. Cofinal image normal form ¬BddAbove(height image) verified; no arbitrary pairwise equivalence rewrite loop. |
| Syntactic generality | Arbitrary real growth multiplier c, arbitrary recursive F, and exact original signature from generic chain compiled. Signedκ theorem and κ≤2 unconditional branch compiled; δ=0,-1 full-output instances compiled. |
| Superfluous arguments | Drop hκ:0<κ with newly proved signed selector/Dirichlet branch. For κ≤2 also drop hinf. Keep irrationality: α0κ3 counterexample has infinite unreduced pairs and no reduced m1 chain. Keep NeZero m for first entry; empty chain changes signature. |

Normal form: OK for the local arithmetic caller; upstream recursive selection would use
cofinal-height semantics. Syntactic generality: RESTATE for public generic API. Superfluous
arguments: hκ positivity verified removable; hinf removable only in verified κ≤2 branch.
No reversed simp-normal-form equivalence or new global instances are proposed.

## Phase6.0 — complete callers, inline audit, dependency scopes

Fresh scoped `rg --no-ignore` and tracked `git grep` agree: one actual source caller,
`Roth.exists_roth_approximants_aux` at Main438, inside its full declaration Main429–450.
There are zero external-to-file source callers. Main's docstring occurrence is not a caller.
The entire Main file and LeanEval wrapper were read. No separate inline rederivation was found.
[source-search.json](../evidence/Roth.exists_approximants/source-search.json), [tracked-source-search.json](../evidence/Roth.exists_approximants/tracked-source-search.json), [inline-search.json](../evidence/Roth.exists_approximants/inline-search.json), [callers.json](../evidence/Roth.exists_approximants/callers.json).

Both tests retain the actual caller's complete original signature and body: first literal
selection proof inlined at the actual application, then substitution by the generic recovered
theorem. They return all balanced degrees and subsequent bound obligations, not merely an
isolated prefix or a supplied desired conclusion. Only declaration visibility/name change.
[callers2-executed.lean.txt](../evidence/Roth.exists_approximants/callers2-executed.lean.txt), [callers02-receipt.json](../evidence/Roth.exists_approximants/callers02-receipt.json).

Native293 audit finds zero direct type consumers, one direct kernel-value consumer, and five
canonical transitive consumers: the private approximant/degree helper, roth_of_isIntegral,
roth, roth_rat, and LeanEval.thueSiegelRoth. This theorem has no simp attribute; lexical,
body/type, and canonical graph scopes are separately recorded.
[scope-executed.lean.txt](../evidence/Roth.exists_approximants/scope-executed.lean.txt), [scope01-receipt.json](../evidence/Roth.exists_approximants/scope01-receipt.json), [canonical-consumers.json](../evidence/Roth.exists_approximants/canonical-consumers.json).

Pairwise moral-duplication audit:

| A | B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| exists_approximants | exists_reduced_approx | No: unbounded one-witness selector versus finite recursive chain | Selector is initial arithmetic input | Keep scopes separate; do not count parent as mathlib |
| exists_approximants | exists_degrees | No: rational selection versus degree rounding/balancing | No | No unification |
| exists_approximants | Set.seq_of_forall_finite_exists | No: exact arithmetic/log outputs versus finite-history predicate | Shared choice/recursion mechanism | Investigate public generic selection API |

## Phase6 — actual composition experiments

Attempt1: strict-monotone subsequence/extraction primitives. Native signatures confirm their
shapes, but arbitrary recursive growth and reduced fixed-constant approximation membership are
missing; no1–3-call old-form proof was obtained.

Attempt2: finite-history sequence selection plus finite bounds. This is a possible proof
strategy, but the finite-bound premise and logarithmic/reduced-pair bridge require new proof;
it is not a1–3-call replacement. The new generic recursion proves the exact desired growth.

The accepted native probe places `fail_if_success solve | simp` and
`fail_if_success solve | exact?` inside the first own generic declaration, before any own
selection theorem is available. Neither closes. This is evidence about those routes, not an
absolute absence theorem. The cofinal-image normal-form equivalence does close by simp; that
small equivalence is not the full chain theorem. No ≤3-call mathlib-only old-signature
composition, and no full simp composition, has been demonstrated.
[composition2-executed.lean.txt](../evidence/Roth.exists_approximants/composition2-executed.lean.txt), [composition02-receipt.json](../evidence/Roth.exists_approximants/composition02-receipt.json).

## Phase7 — actionable verdict

**BORDERLINE-needs-human.** A useful local witness-construction theorem is established, but
whether its generic recursion packaging should become public API remains an audience/granularity
choice. The exact2/δ logarithmic formulation serves one Roth caller. A reusable cofinal-height
sequence exposes more mathematics and composes with unbounded-image predicates, but the
selection mechanism overlaps existing finite-history sequence primitives. This does not justify
calling the old theorem redundant, nor establish that its exact arithmetic spelling should ship.

Keep the current project theorem. A concrete local improvement is dropping κ positivity using
the verified signed selector, and supplying only the reduced cofinal-height premise to the
finite-chain theorem. The only actual caller can retain every output obligation with the tested
generic replacement. If public selection API is pursued, decide these future upstream questions:

1. Should cofinal-height selection with prescribed recursive growth be public API, or remain local to applications of existing sequence-selection primitives?
2. If public, should the primary API return an infinite sequence for arbitrary recursive threshold F, with the nonempty finite multiplier chain as a corollary?
3. Should the reduced rational/logarithmic specialization remain local to a future Roth development while only the general selection law is proposed upstream?

These are future upstream decisions, not missing mathematical proof or user blockers. No
production theorem, pin, Git state, overview, or progress entry was changed by this worker.

## Phase8 — native attempt ledger and final gates

| Accepted exact source | Raw root receipt | Elapsed ms |
|---|---|---|
| [original](../evidence/Roth.exists_approximants/original-executed.lean.txt) | [original-receipt.json](../evidence/Roth.exists_approximants/original-receipt.json) | 3018 |
| [generic](../evidence/Roth.exists_approximants/generic-executed.lean.txt) | [generic01-receipt.json](../evidence/Roth.exists_approximants/generic01-receipt.json) | 97623 |
| [recovery](../evidence/Roth.exists_approximants/recovery-executed.lean.txt) | [recovery01-receipt.json](../evidence/Roth.exists_approximants/recovery01-receipt.json) | 2352 |
| [callers](../evidence/Roth.exists_approximants/callers2-executed.lean.txt) | [callers02-receipt.json](../evidence/Roth.exists_approximants/callers02-receipt.json) | 1483 |
| [composition](../evidence/Roth.exists_approximants/composition2-executed.lean.txt) | [composition02-receipt.json](../evidence/Roth.exists_approximants/composition02-receipt.json) | 10054 |
| [scope](../evidence/Roth.exists_approximants/scope-executed.lean.txt) | [scope01-receipt.json](../evidence/Roth.exists_approximants/scope01-receipt.json) | 3901 |
| [counterexample](../evidence/Roth.exists_approximants/counterexample2-executed.lean.txt) | [counterexample02-receipt.json](../evidence/Roth.exists_approximants/counterexample02-receipt.json) | 2375 |
| [signed](../evidence/Roth.exists_approximants/signed-executed.lean.txt) | [signed01-receipt.json](../evidence/Roth.exists_approximants/signed01-receipt.json) | 68527 |
| [edges](../evidence/Roth.exists_approximants/edges2-executed.lean.txt) | [edges02-receipt.json](../evidence/Roth.exists_approximants/edges02-receipt.json) | 1162 |

All accepted proofs have clean complete diagnostics and only propext/Classical.choice/Quot.sound.
Disk results explicitly report partial=false; raw run_code format reports success/diagnostics
without a partial field. Nine accepted native executions; three other native executions are
separately retained: callers01 errors/recovered sorryAx rejected; counterexample01 clean but
missing target-isolation guard, superseded by guarded02; edges01 clean proof with two whitespace
warnings, superseded by warning-free02. Composition01 was never executed: the circular own-theorem
negative-probe mistake was caught in preparation and corrected in02. Exact executed sources and
hashes are immutable. No raised limits, new axioms, sorry/admit/unsafe/native_decide accepted.

Stable18 isolated prefix and disk9 prefix remain unchanged. Signed and edge probes alone use the
fresh root-approved19th import, DiophantineApproximation.Basic. [native-prefix-authorization.json](../evidence/Roth.exists_approximants/native-prefix-authorization.json).
Portable validator checks current manifest hashes/bytes,17 fresh source/pin hashes, exact293 array,
all native receipts and imported prefixes, standard axioms, literal replay/complete caller
scope,15 formal cells, named literature requests, required overview keys and report links in
both scratch and integrated layouts. [verification.json](../evidence/Roth.exists_approximants/verification.json), [validate.py](../evidence/Roth.exists_approximants/validate.py).

Final gates: [scratch validation](../evidence/Roth.exists_approximants/validation-scratch.json), [integrated validation](../evidence/Roth.exists_approximants/validation-integrated.json), [secret scan](../evidence/Roth.exists_approximants/secret-scan.json). All passed; completed=true, unresolved[], root acceptance pending.
