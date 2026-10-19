# Performance revisit: `sum_max_sub_le_index_det`

Proof-only repair of original27. Counts remain 216/264 originals, Theta 35/35,
9/14 completed files; revisits add zero originals. No Git, shared-log, rename-queue,
or unrelated source writes. Public wrappers/domains, hq, Θ hypotheses, header and all
preceding helper/deletion/FIRST audits are preserved. No new helper or API recommendation.

Baseline release: HEAD/origin `c2e9ed63827828433a42cd7c63406877ace43d29`;
source/audit commit `305442a9a0daef17dcfc800333a63a669ad5cc21`.
Baseline Theta SHA256 `f458cf85b2746b8d155074c3aaaccd8e8c0708bd2d7fa78787184d76ae008875`.
Owner's inherited baseline full build 87.943s then separate LeanEval 35.135s passed;
complete native baseline diagnostics in `/private/tmp/theta-numeric-performance/`
are reused against the identical baseline source, with fresh final gates required below.
No cache operation was needed. Classic Lean dialect. Final owner cumulative/full build,
then separate LeanEval/publication remain owner work after terminal freeze.

## Diagnosis and measured repair

Latest inherited failing actual target total **1333.349ms** is preserved in
`inherited-target-row.json`, its strict UTF-8 raw slice, and the original complete raw
log/source/status/table referenced with byte hashes in `preserved-failing-history.json`.
Earlier failures (1233.766, 1411.317, 1420.445, 1351.681, 1698.334ms and other retained
samples) remain failed history; a later unchanged-source pass cannot erase them.
This repair began from the real failed source and trace, not an uncompiled hint.

Nested diagnostic hotspots are overlapping and **never added to the disjoint total**:
hidx 405.836ms, its two broad simps 152.156/206.195ms, hterm 204.985ms with restricted
linarith 125.020ms. The repair uses existing `index_C_mul` with the generic integer
map bridge and unit nonzero proof; no ±1 split remains. It rewrites the derivative loss
as successive subtraction and applies `sub_le_sub_left` followed by transitivity.
The candidate compiled before the narrowly scoped production replacement. Deterministic
count_heartbeats checks passed at unchanged default 200000: 4759 before → 3263 after
(31.44% fewer), with no production instrumentation.

| Eight-cause taxonomy | Actual assessment |
|---|---|
| 1 instance synthesis | Not the dominant failed node; no instance workaround introduced. |
| 2 fat simp | Confirmed in hidx; broad two-branch simp removed. |
| 3 unification/defeq | Final sum/E normalization still contributes; preserved pending final measurement, no unsupported diagnosis of a new root cause. |
| 4 heavy automation | Confirmed hterm linarith normalization/certificate cost; replaced with direct order transport. |
| 5 metavariable churn | Existing explicit E/hterm/hidx types retained; no evidence of a dominant separate cause. |
| 6 coercion churn | Integer sign bridge crossed once with map_intCast; no repeated sign-case cast normalization. |
| 7 duplicated subterms | Existing local E retained, no duplicated helper or source matrix expansion introduced. |
| 8 kernel/compiler | Count actual disjoint addDecl including kernel below; no independent executable theorem compiler cost or nested kernel double-count. |

Scope propagation: the direct index29 caller is measured with the target. Separate
lem7_Φ_bound/lem7_numeric/prefix repair queue remains mandatory; no out-of-scope edits.

## Fresh 24-item audit

| # | Item | Result/action |
|---|---|---|
| 1 | LINT | No target warning in inherited complete native diagnostics; fresh final native gates below preserve every warning. |
| 2 | HAVE SCAN | hterm: substantive 9-line derivative estimate. h1: rewritten derivative bound. h2: used twice. hprod: used twice for nonzero entries. hidx: exact scalar-index transport. hlδ: terminal simp identifies the repeated constant sum. No trivial existential helper or one-use alias added. |
| 3 | SET_OPTION | No production options or profiling scaffolding. |
| 4 | SIMP SQUEEZE | Removed both broad sign-case simps. The single-lemma simpa only [map_intCast] is the targeted performance exception; hlδ remains terminal unsqueezed simp. |
| 5 | NAMING | sum_max_sub_le_index_det describes the sum/max/subtraction determinant-index inequality, snake_case, no forbidden abbreviation or scheme. No rename. Index rename remains owner project-end work. |
| 6 | LINE PACKING | All eight signature lines measured in packing.json and table below; byte-identical to release. |
| 7 | BY PLACEMENT | Every by remains at end of its declaration/assignment line. |
| 8 | FORMAT | Two-space indentation; no semicolon, haveI, letI, empty proof line or long line; new scalar transport wrapped at ≤100 codepoints. |
| 9 | COMMENTS | Protected source docstring and attribution preserved byte-for-byte; no original proof comment removed. |
| 10 | DOCSTRING | Existing mathematical determinant and loss description retained. |
| 11 | VISIBILITY | Public contract retained; publication visibility is not reopened during this performance revisit. |
| 12 | STRUCTURE | 27 lines after := by (28 including its line) ≤30; target is not a module Main results headline. Largest local subproof 9 ≤10. No conjunction result, new helper, or arbitrary 15-line cap. |
| 13 | MATHLIB | Five actual methods attempted below. Existing index_C_mul and generic map_intCast replace the costly sign normalization; no replacement theorem found by the bounded clean literal goal probes, no global absence claim. |
| 14 | JUNK DEF | Not a def; local set E names the repeated derivative matrix and avoids duplicated elaboration. |
| 15 | EXISTS LEMMA | No existential lemma or witness duplication. |
| 16 | SHOW vs CHANGE | Neither occurs in changed production proof. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every effective binder probed/reviewed below, two positive variants compiled, unchanged intended contract. |
| 19 | INEQUALITY | All five statement inequalities oriented ≤/<; scan below. |
| 20 | NORMAL-FORM | The finite range/max sum is the concrete source and caller normal form. Scalar sign invariance now uses the nonzero-constant API directly. |
| 21 | SYNTAX-GEN | Current caller directly supplies D/hD/hdet/hr/global hδ; replacing hD/hδ with family-local weights would move useful routine specialization into that caller. No recommended contract change. |
| 22 | IMPORT-FANOUT | No new imports or file-level changes. |
| 23 | CASTS | No cast removed: Fin→Nat, Nat→Real, unit→Int→polynomial and the scalar bridge are genuine cross-type/load-bearing. No new redundant explicit cast in the diff. |
| 24 | INSTANCE-NAME | No instance declaration added or named; DecidableEq τ remains omitted as previously approved. |

## Five actual searches and clean current goal exploration

| Method | Fresh evidence/result |
|---|---|
| A Lean-Finder | `lean_leanfinder.json`: determinant derivative weighted-index query; actual DNS failure, no absence claim. |
| B Loogle | `lean_loogle.json`: subtraction-order type pattern; actual DNS failure. |
| C LeanSearch | `lean_leansearch.json`: index/determinant/Hasse derivative query; actual DNS failure. |
| D full source/name search | `full-name-search.log`, local Index.lean:187 and mathlib integer-map/Units/order sources inspected; generic building blocks present. |
| E local name pattern | `lean_local_search.json` map_intCast; source hits may appear but index unavailable, not an absence proof. Positive #check compilation verifies names. |

Auxiliary routes: index_C_mul/index_neg, map_intCast, Units.ne_zero, Int.cast_ne_zero,
sub_le_sub_left/sub_right_comm/sub_le_iff_le_add. Common-equivalents table has no matching
analytic/topological bucket. We use the already-existing scalar API directly. No claim
of exhaustive global theorem absence follows from unavailable remote/index services.

`PrefixAbsence.lean` is the exact current pre-target source, without importing Theta;
the corrected positive run succeeds separately, checks that preceding min_le_sum_max is
present, and asserts both target and index29 caller absent using correctly qualified
name literals. The initial positive run used Name.mkSimple on dotted strings, which
encodes one atomic component and cannot certify the intended names; its exact source
and output are retained as unaccepted evidence. This review correction was found
during the first full trace capture and compiled only after that capture drained;
any required same-source repeat follows the corrected gate with no overlapping requests.
The scratch correction alone does not trigger a repeat and does not invalidate the
uncontended first trace on identical production bytes.
`Automation.lean` contains anonymous literal current-header goals, correctly omitting
DecidableEq τ, never named failed theorems. grind/aesop/simp_all/exact? fail; bounded
apply? gives partial index lower-bound/generic order suggestions then reaches the lower
10,000-heartbeat scratch budget. All errors and suggestions are preserved; maxErrors
is unchanged. This is exploration, never a positive proof/axiom certificate. No import-self
or failed-declaration contamination. `LocalAutomation.lean` exits 1 only for the attempted positivity and degree-lia goals;
the finite-sum gcongr, scalar norm_cast and direct order examples have no diagnostics.
The lia goal needs the specialized hD μ and Fin bound available to arithmetic search;
the selected explicit Nat transitivity proof already supplies them without search.
These failed alternatives are not positive certificates.

## Every effective parameter and generality

`BindersNegative.lean` and range/result JSON record each drop test with autoImplicit false.
Data/type binders occurring in dependent types cannot be dropped meaningfully: τ, R, l,
D, α, r, δ produce unknown/type-dependency errors. Fintype τ removal fails index's required
instance. hD, hdet, hr removal fails their substantive proof uses. The first hδ drop scratch
had a missing-colon parse error; it is retained as failed exploration and replaced by the
separate syntactically correct `DropHdelta.lean`, which fails at the actual missing hδ use.
No parse error is presented as mathematical necessity. DecidableEq τ is already omitted;
there is no effective σ/Fintype σ/DecidableEq σ in this target's telescope.

| Effective binder | Action/evidence |
|---|---|
| τ : Type* | Already universe polymorphic; structural dependency probe fails on unbound type. |
| Fintype τ | Compiled omission fails required Option τ finite-index operations. |
| R | Structural polynomial in statement/proof; drop produces unknown R. |
| l | Controls matrix, Fin/range and cutoff; drop produces unknown l. |
| D | Correlated derivative family shared with hdet/conclusion; drop produces unknown D. |
| hD | Drop fails at bound use. Uniform degree <l variant freshly compiles. |
| hdet | Drop fails at determinant expansion/nonzero sum use. Dropping correlated nonzero information is not supported by index's zero convention. |
| α | Arbitrary point, structurally used throughout; drop fails. |
| r | Arbitrary natural weights, structurally used; drop fails. |
| hr | Drop fails index_prod positivity premise. No coefficient/index API abstraction change. |
| δ | Arbitrary real loss, structurally used; drop fails. |
| hδ | Corrected drop fails actual use. Family-local weight variant compiles and removes hD. |

The family-local weights and uniform degree variants are concrete assessed alternatives,
not recommended API churn. The first inversion scratch imported Index without the matrix determinant module and
failed at unknown Matrix; exact failed source/raw log are retained. `Inversion.lean`
adds only the required scratch determinant import and is recompiled separately.
The whole index29 caller already derives the existing global
cutoff/degree hypotheses. Correlated matrix nonzero and permutation-product information
remains shared. Abstracting ℝ or index's coefficient API would exceed this scoped proof
repair; no unused new hypothesis, weaker conclusion or theorem visibility change.

Fresh literature queries and fetched primary source text are preserved in
`literature-results.json`. [Min Ru's notes](https://www.math.uh.edu/~minru/fields/roth.pdf)
state the same index product and sum principles (p.3); the [UCL notes](https://www.ucl.ac.uk/~ucahpet/TransNotes.pdf)
were search hits but the fresh fetch returned 404, so no new content claim is based on
that fetch. Local authoritative `.mathlib-quality/references/clean.tex:815–840` supplies
the exact determinant expansion and derivative-loss argument. No ChatGPT math MCP is
available; no external second opinion is claimed.

Inversion fires in the determinant-expansion suffix: `Inversion.lean` freshly tests a
complete abstract arbitrary-matrix/column-bound argument, using the same scalar-index
API. It is a real abstraction option, not a user veto or an impossible generalization.
The concrete theorem still has substantive Hasse-derivative weight content; a one-use
wrapper is unnecessary for this performance repair and is not recommended here.

## Measured signature packing and inequality scan

Widths below are codepoints, not UTF-8 bytes. Next group is the next complete legal
binder/application segment. All eight signature lines remain byte-identical.

| Line | Width | Next group width | Arithmetic | Action |
|---|---:|---:|---|---|
| 371 | 95 | 28 | 95 + 1 + 28 = 124 >100 | ok |
| 372 | 69 | 75 | 69 + 1 + 75 = 145 >100 | ok |
| 373 | 100 | 18 | 100 + 1 + 18 = 119 >100 | ok |
| 374 | 50 | 63 | 50 + 1 + 63 = 114 >100 | ok |
| 375 | 69 | 64 | 69 + 1 + 64 = 134 >100 | ok |
| 376 | 68 | 34 | 68 + 1 + 34 = 103 >100 | ok |
| 377 | 40 | 80 | 40 + 1 + 80 = 121 >100 | ok |
| 378 | 88 | — | final signature line | ok |

| Occurrence | Final orientation | Decision |
|---|---|---|
| hD | degree ≤ μ | already ≤ |
| hr | 0 < r j | already < |
| hδ premise | degree ≤ l−1 | already ≤ |
| hδ result | weight ≤ δ | already ≤ |
| conclusion | sum − lδ ≤ determinant index | already ≤ |

No ≥/> in code signature, no renamed inequality theorem. Protected mathematical prose unchanged.

## All 42 golfing rules

| Rule | Fresh assessment |
|---|---|
| 1.1 | No by-exact wrapper. |
| 1.2 | No by-rfl wrapper. |
| 1.3 | No rw then exact on the same closing fact; h1 rewrites precede the h2/max estimate. |
| 1.4 | Scalar normalization uses simpa using directly. |
| 1.5 | No trailing rfl. |
| 1.6 | No constructor. |
| 1.7 | Direct exact/refine used. |
| 1.8 | No contradiction. |
| 1.9 | Dependent membership lambdas cannot eta-reduce; no trivial lambda wrapper. |
| 1.10 | h2 and hprod used twice; h1 is rewritten, hidx/hlδ each encode a nontrivial normalization, hterm supplies the repeated estimate. |
| 1.11 | le_index_sum uses refine with a function. |
| 1.12 | No redundant show. |
| 1.13 | Nonzero product gives an entry-indexed family, not a fixed conjunction destructuring. |
| 1.14 | Existing final rewrites combined. New h1 rewrite is before goal rewrite and could be combined as `rw ... at h1` only with a different location, so retained separately. |
| 1.15 | hlδ terminal simp remains. Scalar simpa-only is the measured performance exception, not cosmetic squeezing. |
| 1.16 | No nonterminal bare simp. |
| 1.17 | Order transport uses .trans and standard projection forms. |
| 1.18 | No trailing by block or parenthesized lambda improved by <|. |
| 1.19 | No push_neg. |
| 1.20 | No existential helper. |
| 2.1 | Fresh anonymous whole-goal grind fails; raw log retained. |
| 2.2 | Whole-goal grind already deletes all setup; no production grind. |
| 2.3 | Implemented scalar simpa consolidation. |
| 2.4 | No analytic function predicate, not applicable to algebraic Hasse derivatives. |
| 2.5 | Fresh local nonnegativity positivity trial recorded; direct add_nonneg remains controlled. |
| 2.6 | Fresh finite-sum gcongr probe recorded; sum_le_sum is direct and expected-type-guided. |
| 2.7 | Fresh degree lia probe recorded; current Nat.le_sub_one_of_lt term avoids proof search. |
| 2.8 | Fresh anonymous whole-goal aesop fails. |
| 2.9 | Fresh scalar cast norm_cast probe recorded; selected Int.cast_ne_zero is direct. |
| 2.10 | Arbitrary polynomial inequality is not closed decidable computation; no decide/native_decide. |
| 2.11 | No denominator identity goal; no field_simp/ring endpoint. |
| 2.12 | No ring/ring_nf endpoint. Replaced restricted linear arithmetic with a direct order lemma. |
| 2.13 | Eliminated both sign cases using arbitrary nonzero scalar invariance; no wlog needed. |
| 2.14 | No two-step calc; direct transitivity used. |
| 2.15 | No repeated goals remain after removing sign case split. |
| 3.1 | Only rw, no erw. |
| 3.2 | No legacy continuity/measurability. |
| 3.3 | No omega; local integer arithmetic probe uses lia. |
| 3.4 | Sign equality rcases removed entirely. |
| 3.5 | Specialized determinant derivative estimate does not need global simp/grind registration. |
| 3.6 | Fresh anonymous simp_all whole-goal fails; no production simp_all. |
| 3.7 | No limit raises present or introduced. |

## Step-back and simplify review

No built-in simplify callable exists in this host; its reuse/quality/efficiency review
was executed directly. Outcome ISSUES-FOUND-AND-FIXED: the existing scalar-index API
removes duplicated sign branches, order transport removes unnecessary arithmetic search.
No further supported source recommendation remains unapplied. No helper is extracted
merely to impose an invented headline cap. New production helpers: zero.

## Frozen semantic, native and actual performance gates

The final production proof is frozen at SHA256
`c0e8edc37192227f56814c674480b56143e2923e588a750dca5d7f3ecf03c2a8`. The complete 17-path source/pin map is
`source-hashes.json`; inherited release pins are kept separately in
`release-source-pin-hashes.json`. All 74 preceding Theta reports and all 16 inherited
FIRST-related files retain their exact hashes. The numeric helper's immutable FIRST
source/fragment are additionally recorded in `supplemental-numeric-FIRST-hashes.json`.
No original/helper audit is replaced, recounted, or silently waived.

| Actual command/gate | Exit | Seconds | Positive markers/result |
|---|---:|---:|---|
| lake build Roth.Theta | 0 | 31.635 | 0 PASS markers |
| then lake build Roth.MainLemma | 0 | 35.694 | 0 PASS markers |
| lake env lean Independent.lean | 0 | 28.038 | 40 PASS markers |
| lake env lean ActualSemanticsAugmented.lean | 0 | 190.828 | 553 PASS markers |

The independent file re-elaborates the complete original27 proof in its exact preceding
original Index/Theta context and the complete preceding current source through the
entire public index29 caller in a separate namespace. It verifies actual full effective
current target/caller types, retained user names/order/BinderInfo, universe parameters,
conclusions, actual opaque values with `value! true`, standard axioms only, nonself
proofs and positive current/actual direct-caller dependencies. The original full telescope
is recovered by the unchanged all29 adapter map with only the previously approved
DecidableEq/hR removals for this target; no map edits were needed.

The augmented run preserves the entire preceding scaffold byte-for-byte (SHA256
`dead52ef35a112373ecf1c77d0b899ab8fe657c440157a2a15a1f19fef62a65c`) and
passes **553** markers = all **513** prior checks plus **40** fresh checks. The standalone
independent file passes the same 40 new checks. Whole original/current MainLemma proofs,
all29 original public recoveries, five public definition values, all11 original35
introduced-helper retention/deletion audits, other helper FIRST proofs, all previous
performance repairs, actual updated RootTheta/MainLemma opaque values/types/standard
axioms/dependencies are freshly executed. Every old marker category is checked against
the preceding successful log. All four canonical full proof blocks retain exact bytes:

| Full canonical block | SHA256 |
|---|---|
| raw bytes 1414–15125 | `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f` |
| raw bytes 16628–68797 | `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da` |
| raw bytes 70475–105941 | `96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a` |
| raw bytes 117380–152930 | `859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41` |

Complete, unfiltered native diagnostics were requested on the two absolute live paths,
without declaration/range/severity/timeout filters, after the builds and semantic runs:

| Module | success | partial | timed_out | Errors | Warnings |
|---|---|---|---|---:|---:|
| theta | true | false | false | 0 | 8 |
| mainlemma | true | false | false | 0 | 3 |

All warnings are preserved in raw native JSON. Theta warnings: protected header; retained
hr at93, hB/hr at101, hB109, hr129, hr252, hq554. MainLemma: protected header and
hδ0/hr₁ at149. No target warning, filtering, suppression or error. Positive compiler logs
contain no PANIC, error or sorryAx. No sorry/new axiom/native_decide/limit raise appears
in the source diff. New identifiers are certified by positive prefix #check and actual
candidate/module compilation; no hallucinated name is accepted.

## Actual final whole-Theta trace, scoped acceptance

Exact command, after all ordinary/native requests drained:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean
```

Each complete run uses a sufficient 420-second external capture window, unchanged Lean
limits, exact final source snapshot, strict UTF-8 raw bytes, SHA256s and byte offsets.
Inventory is **50/50** current declarations, every theorem/lemma with exactly one actual
proof anchor. The table counts disjoint outer command + async proof + addDecl (including
kernel) + compiler/linter rows. Nested macro/header and nested kernel rows are excluded
from additional sums; full per-row anchors are in strict slice JSON/table artifacts.

| Sample | Declaration | Command ms | Async proof ms | AddDecl ms | Linter/other ms | Total ms |
|---|---|---:|---:|---:|---:|---:|
| final-first | sum_max_sub_le_index_det | 123.338 | 740.062 | 20.246 | 64.533 | **948.179** |
| final-first | index_le_lem6 | 53.205 | 418.357 | 28.999 | 49.409 | **549.970** |
| final-first | Θ_option_le | 111.403 | 59.300 | 11.189 | 41.976 | **223.868** |
| final-repeat | sum_max_sub_le_index_det | 131.535 | 711.614 | 20.579 | 51.200 | **914.928** |
| final-repeat | index_le_lem6 | 54.620 | 431.016 | 17.588 | 49.978 | **553.202** |
| final-repeat | Θ_option_le | 92.720 | 56.601 | 3.921 | 15.437 | **168.679** |

Scoped budget is 1000ms. A ≥750ms scoped first sample requires exactly one same-source
repeat. Any repeat is recorded above; no third unchanged-source sample is used to choose
favorable acceptance. Unrelated rows alone never trigger a scoped repeat. The inherited
1333.349ms actual failure remains preserved; this measured proof repair, rather than an
unchanged-source rerun, supplies the new accepted evidence. Heartbeats: 4759 →3263. Nested first-final diagnostic nodes (not additive):
hterm204.985→103.967ms, hidx405.836→104.353ms; exact saved rows in
`final-first-nested-hotspots.json`.
Buzz outcome: **FIXED for summax/direct-index29 scope**. No new helper, no limit raise
removed/added (0/0), no profiling scaffolding in production.

**No whole-file or MainLemma caller timing PASS is claimed.** The actual complete trace
is inventoried, with all failing rows/slices retained. Mandatory separate lem7_Φ_bound,
lem7_numeric and the previously failed second-prefix queue remain, even if an incidental
sample falls below budget. MainLemma actual caller timing remains unmeasured after its
historical bounded cutoff before main_lemma; ordinary builds/semantics/native success do
not substitute for that timing. Newly over-budget unrelated rows, if any, are concrete
queue additions in `profile-*-remaining-queue.json` and strict failure slice artifacts.

## Gates and eleven-step checklist

| Gate | Result |
|---|---|
| lake_build_file | PASS, actual Theta then MainLemma commands/times above |
| definition/public statement/visibility protection | PASS, only target proof changed; exact header and entire prefix/suffix/caller text preserved |
| structure | PASS, 24→27 lines after := by (25→28 counting that line), largest local subproof9≤10, ordinary cap30 |
| naming/packing/inequality | PASS, fresh measured tables above, no rename |
| original/current proof/type/opaque/stdaxiom/nonself | PASS, standalone and entire augmented positive runs |
| all prior semantic/helper/deletion/FIRST gates | PASS, entire513 prefix and four canonical blocks unchanged/reexecuted |
| complete unfiltered native | PASS, 0 errors, 8/3 warnings preserved |
| scoped actual performance | PASS, fresh whole-trace anchored rows above, repeat policy honored |
| owner cumulative/full build then separate LeanEval/publication | PENDING OWNER, not claimed by this leaf |

- [✓] 1. Required cleanup/buzz/golf/proof/search/generality/gates/style/naming/profiling references consulted.
- [✓] 2. All24 audit items and every have reviewed.
- [✓] 3. Five actual searches and clean literal pre-target anonymous automation/positive absence gate.
- [✓] 4. Every effective parameter drop/weakening, literature and concrete inversion probe.
- [✓] 5. Every signature line measured; all five inequalities scanned.
- [✓] 6. All42 golf rules answered with concrete results.
- [✓] 7. Step-back/direct simplify review; supported improvements implemented, no speculative API churn.
- [✓] 8. Actual Theta then MainLemma builds; full old/current independent/caller/opaque/stdaxiom gates.
- [✓] 9. Entire513 scaffold, original/current MainLemma/all29/five-values/all-helper-FIRST audits preserved and freshly executed.
- [✓] 10. Complete unfiltered native, drained requests, actual whole-Theta profiles and strict failure history.
- [✓] 11. Terminal hash/manifest/process freeze; owner cumulative publication gates explicitly separate.

## Concrete artifact map and terminal freeze

All fresh artifacts are under `/private/tmp/theta-summax-performance/`:

| Artifact(s) | Purpose |
|---|---|
| baseline-Theta.lean, final-Theta.lean, candidate-declaration.lean, original-declaration.lean, owned-proof.diff | Exact before/after sources and scoped diff |
| inherited-target-row.json, inherited-target-strict-slice.log, inherited-nested-hotspots.json, preserved-failing-history.json | Actual failed diagnosis/history, immutable prior raw/source/status/table references |
| lean_leanfinder/lean_loogle/lean_leansearch/lean_local_search.json + stderr, search.py, full-name-search.log, literature-results.json | Actual five-method/literature search evidence, including failures |
| PrefixAbsence.lean, prefix-absence.*, Automation.lean, automation-*json/log | Positive clean absence and bounded anonymous literal-current-goal searches |
| BindersNegative.lean, binder-*json, binders.*, DropHdelta.lean, drop-hdelta.* | Every binder drop, preserved initial parse error and corrected hδ use failure |
| Generality.lean, GeneralityMore.lean, generality*json/log | Concrete family-local and uniform-degree positive variants |
| failed-import-Inversion.lean, inversion.*, Inversion.lean, inversion-corrected.* | Preserved failed import context and successful full abstract matrix argument |
| LocalAutomation.lean, local-automation.*, Heartbeats-before/after.lean, heartbeats-* | Honest auxiliary failures/successes and deterministic before/after measures |
| packing.json, static-gates.json, frozen-source-static-metadata.json | Exact structure/packing/signature/scoped-source decisions |
| Independent.lean, independent-original-context.lean, original27-proof-fragment.lean, independent-proof-blocks.json, independent-final.* | Complete independent original/current/whole-caller source and opaque/type/metadata diagnostics |
| ActualSemanticsAugmented.lean, immutable-scaffold-and-blocks.json, actual-semantics-final.*, semantic-marker-summary-final.json | Entire513+40 semantic proof scaffold and every positive marker |
| build-theta-final.*, build-mainlemma-final.*, native-theta-final.json, native-mainlemma-final.json | Actual builds and complete unfiltered native diagnostics |
| actual-profile-final-*.log/json, actual-profile-final-*-table.json, profile-*-strict-slices.json, final-*-strict-slice.log | Actual complete traces/statuses, all50 inventory, exact scope offsets/anchors/hashes |
| profile-*-remaining-queue.json, profile-*-new-actionable-strict-slices.json | Separate mandatory queue and new actionable failures |
| source-hashes.json, release-source-pin-hashes.json, all-FIRST-immutable-hashes.json, supplemental-numeric-FIRST-hashes.json, protected-report-hashes.json | Exact17 source/pins,16 inherited FIRST plus numeric originals,74 protected reports |
| pre-profile-drain.json, pre-repeat-drain.json (if repeat), final-process-drain.json | Completed request and dead process-group evidence |
| evidence-manifest.json, final-freeze.json | Full artifact byte-size/SHA256 map and terminal authority revocation |

The machine `evidence-manifest.json` gives exact existing paths/hashes (the tables use
families where several raw/status/PID files share a basename). All failed exploration
sources/raw diagnostics are retained. No pending leaf request, compiler or native work
remains. Source, scratch, report, compiler and native authority are explicitly **REVOKED**;
the compiler/native window is **RELEASED** to the owner. No source/report/scratch writes
are authorized after this terminal record. Counts stay216/264,Theta35/35,files9/14.
Owner alone performs final cumulative/allactual checks, full build THEN separate LeanEval,
exact-path stage/commit/push/clean before the next repair source edit.


## Owner evidence qualifications

Owner source-free review independently checked all15 supplied historical whole-source captures
for this theorem, including1351.681/1698.334ms and the immediately preceding1333.349ms:
full raw/source/table hashes, disjoint totals, exact byte offsets and strict UTF8 slices.
Supplemental manifest: `/private/tmp/theta-summax-performance/owner-supplied-failure-history.json`.
This supplements the leaf history map, which directly hashes the latest shared capture and the
preceding numeric history manifest. No new timing run or source edit occurred.

The bounded apply? exploration produced partial suggestions and a10000-heartbeat whnf timeout
reported at line1, outside its example range; owner therefore records an honest bounded outcome,
not a span-verified error for that trial. Four other whole-goal trial errors are in range.
Eleven well-formed binder-drop trials have located errors; the initially malformed hδ trial
is superseded by its separate corrected missing-hδ-use diagnostic. Corrected positive absence
uses qualified target/caller names and a present preceding control; the atomic-name scratch
is unaccepted. Remote search methods were attempted but returned DNS failures; local source
and name evidence support used identifiers, without a claim of global theorem absence.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 72.029 s and 53.706 s.
Theta SHA256 `c0e8edc37192227f56814c674480b56143e2923e588a750dca5d7f3ecf03c2a8` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p06-full.log` and `/private/tmp/roth-theta-p06-leaneval.log`; machine record
`/private/tmp/roth-theta-p06-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 27 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
