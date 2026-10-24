# Phase 4 — `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`

Fresh single-declaration worker; source scope is `Roth/LeanEval.lean:58–61` only.
The mathematical result, public name, binder names/order/explicitness, and docstring remain intact.
The external LeanEval benchmark contract expressly requires `thueSiegelRoth`; this is the
authorized external-name exception, not an unprocessed rename. No rename was queued.

## References and snapshots

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read both installed
mathlib-quality/Lean4 SKILL.md files, both full cleanup/cleanup-all commands, and the full
style-rules, naming-conventions, profiling, and pr-feedback-examples references. Large documents
were read in contiguous, nontruncated chunks. No unavailable Skill invocation is claimed.

Before any Lean experiment or golf, saved genuine and entry files in
`/private/tmp/roth-eval-thue/{original,entry}.lean`:

| Snapshot | Bytes | SHA256 |
|---|---:|---|
| Genuine d2eb5e9a source | 3018 | e95c44ae19345ef1514a59ca5e8b182247e9a32aaf4b7d39f0ce57ae5ed27f56 |
| Actual worker entry | 3343 | e4f3998fd64e5a3acc1ccd4bc6588537ebf0e43ceeb4642343dd2795be294d35 |
| Final | 3344 | 4c77924b46d4b6559c8fc6118710e89c92fe07b0a49eaff90011e76edb2429d0 |

The genuine and entry headline declarations are byte-identical (direct comparison); the
surrounding equivalence proof differs. No baseline-context identity is inferred from this.
All final bytes preceding and following the headline declaration equal the entry file.
The accepted predicate, equivalence, private helper, Main, root, and their reports are frozen.

## Mathematics and action

Roth.roth bounds the exponents admitting infinitely many rational approximants. The accepted
equivalence converts that bound to the benchmark's positive uniform lower bound. Algebraicity
over ℤ transports to ℚ by injectivity of the algebra map. Replaced the fraction-ring
equivalence projection by the directly applicable `IsAlgebraic.extendScalars`, with
`FaithfulSMul.algebraMap_injective ℤ ℚ`; removed the `by exact` wrapper and packed the signature.
The two proof-body lines stay two term-body lines; the whole declaration stays four lines.

## Full audit (24 items)

| # | Item | Specific resolution |
|---|---|---|
| 1 | LINT | Entry and final complete unfiltered LSP diagnostics: no messages, no timeout, no partial results. |
| 2 | HAVE SCAN | No `have` in the target; zero use-count rows. No helper inlining opportunity. |
| 3 | SET_OPTION | No target resource/debug option; none added. |
| 4 | SIMP SQUEEZE | No simp call in the target. |
| 5 | NAMING | Exact externally requested benchmark name exception; no forbidden numeric/scheme/abbreviation pattern. Public binder names protected and retained. |
| 6 | LINE PACKING | Initial 54+1+26=81 permitted moving the last binder; final complete width table below. |
| 7 | BY PLACEMENT | Removed redundant `by`; final is a term proof. |
| 8 | FORMAT | Two-space term indentation and four-space signature continuation; no empty body lines, semicolons, `haveI`, or `letI`. |
| 9 | COMMENTS | No inline proof comments present; none removed. |
| 10 | DOCSTRING | Existing public theorem docstring retained byte-for-byte as API; mathematically accurate and contains no proof strategy. |
| 11 | VISIBILITY | Public headline is the requested external theorem, so remains public regardless of internal caller count. |
| 12 | STRUCTURE | Two body lines, no conjunction, no branches; below headline ≤15 bound. No new helper needed. |
| 13 | MATHLIB | Five bounded methods below; direct algebraicity transport found and used. External adapter retained under explicit contract. |
| 14 | JUNK DEF | n/a: target is a theorem. |
| 15 | EXISTS LEMMA | n/a: target is public and concludes the benchmark predicate, not a private trivial witness lemma. |
| 16 | SHOW/CHANGE | Neither appears. |
| 17 | PUSH_NEG | No `push_neg` or negation tactic appears. |
| 18 | GENERALISE | Every binder audited below; actual drop probes for both proof hypotheses fail; no public restatement warranted. |
| 19 | INEQUALITY | Explicit zero-occurrence scan below; no ≥/> in signature or body. |
| 20 | NORMAL FORM | Existing `isDiophantine_iff` is exactly the bridge to canonical exponent-bound form; no additional equivalence generated. |
| 21 | SYNTAX-GEN | External explicit-x/irrational/algebraic application contract retained; accepted iff already supplies alternate usable form. |
| 22 | IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 | CASTS | 0 dropped / 0 cross-type casts / 0 load-bearing casts introduced in the diff; binder types are not casts. |
| 24 | INSTANCE-NAME | n/a: no instance declaration in target or diff. |

Issues fixed: redundant tactic wrapper; underpacked signature; indirect bidirectional algebraicity
transport where a direct theorem applies. Refactoring needed: none. No helper/API expansion.

## Line packing — every signature line

Actual `#check @...thueSiegelRoth` with `format.width := 100`:

```text
LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth : ∀ (x : ℝ),
  Irrational x → IsAlgebraic ℤ x → LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x
```

| Entry line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 58 | 54 | `(_h_alg : IsAlgebraic ℤ x)` (26) | 54+1+26=81 ≤100 | repacked |
| 59 | 54 | no next signature line | n/a | superseded by packing |

| Final line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 58 | 83 | `IsDiophantine x :=` (18) | 83+1+18=102 >100 | ok |
| 59 | 22 | no next signature line; term body follows | n/a | ok |

The widths count Unicode codepoints, including indentation, not UTF-8 bytes. All target lines ≤100.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | Complete signature, all hypotheses, and body | no ≥/> occurrences | none | no `_ge_`/`_gt_` name |

## Five-method mathlib search

| Method | Actual bounded query | Result |
|---|---|---|
| A Lean-Finder | `IsAlgebraic ℤ x to IsAlgebraic ℚ x`, 3 results | isAlgebraic_rat/int and NumberField.isAlgebraic; none a better transport. Remote index is older than pinned mathlib. |
| B Loogle | `IsAlgebraic ℤ _ → IsAlgebraic ℚ _`, 3-result bound | empty successful response; not an absence proof. |
| C LeanSearch | `algebraic over integers implies algebraic over rationals`, 3 results | integral/Niven results; no direct matching transport. |
| D source | Algebraic Basic/Integral declaration search; DiophantineApproximation and Transcendental Roth/Thue/Siegel search | `IsAlgebraic.extendScalars` at Basic:413; field-only tower_top at462; Liouville documentation mentions Roth but supplies no replacement proof. |
| E name-pattern | `IsAlgebraic.extendScalars`, local search | exact theorem and Algebra.IsAlgebraic variant found; index reported unavailable, so positive source hit verified by source and clean full-body compile. |

Auxiliary variants checked: `extendScalars`, `tower_top`, `tower_top_of_subalgebra_le`, and
algebraMap injectivity. `tower_top` requires a field base and cannot use ℤ. The first live probe
using `(algebraMap ℤ ℚ).injective` fails demanding `IsSimpleRing ℤ`; the verified FaithfulSMul
injectivity route succeeds. Common-equivalents table: no matching discrete/finite/bornology
bucket for this headline. Conclusion: partial mathlib match for transport; use it directly.
No claim that exhaustive search proves mathematical/API absence. The public adapter is retained
by the explicit external benchmark contract, with underlying Roth.roth used directly.

New identifiers are real pinned-source declarations and compile-checked in the complete proof:

| Identifier | Evidence |
|---|---|
| `IsAlgebraic.extendScalars` | pinned Algebraic/Basic.lean:413; positive local search; complete scratch and final native compile |
| `FaithfulSMul.algebraMap_injective` | pinned Algebra/Algebra/Basic.lean:336; complete scratch and final native compile |

## Generalisation — every binder

| Binder | Classification/use | Candidates and actual test | Result |
|---|---|---|---|
| `(x : ℝ)` | structure value; appears in both hypotheses and conclusion | Drop is structurally unavailable: both following hypotheses and conclusion depend on x. No abstract type binder/universe/class parent exists. ℝ→ordered field would restate the analytic rpow/absolute-value benchmark and Roth.roth. | retain; no meaningless type-only widening |
| `(_h_irr : Irrational x)` | proposition; used by iff and Roth.roth | Actual clean scratch `clear _h_irr; exact <entry proof>` cannot close (identifier is required), checked inside fail_if_success/solve. Not a strict order, global pointwise, bundled bijectivity, or typeclass hypothesis. | retain, despite underscore it is used |
| `(_h_alg : IsAlgebraic ℤ x)` | proposition; transported to ℚ for Roth.roth | Actual clean scratch `clear _h_alg; exact <entry proof>` cannot close, checked inside fail_if_success/solve. No class-parent, pointwise, strict→weak, or universe weakening applies. ℚ algebraicity is equivalent here, not a weaker result. | retain, used once in transport |

No implicit universes, explicit type variables, section instances, or decidability binders.
The drop probes establish necessity for the current proof, not universal nonexistence of another
proof. Inversion check: no concrete named witness in the statement, no initial unfolding phase,
and the proof uses Roth.roth on the actual x/hypotheses; no proof-abstract-after-unfolding signal.
Big-change candidates: none recommended for this fixed benchmark adapter.

Public literature search: one bounded WebSearch query `Roth theorem algebraic irrational
rational approximation generalization Schmidt subspace theorem`. Top three results: Evertse–
Ferretti [Quantitative versions](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.749.pdf),
[The subspace theorem](https://algant.eu/documents/theses/zerbini.pdf), and Evertse's
[Subspace theorem notes](https://www.math.leidenuniv.nl/~evertsejh/dio2011-subspace.pdf).
The first/third describe Roth's irrational algebraic hypothesis and higher-dimensional Subspace
Theorem extension. That extension changes mathematical setting/conclusion; it is not an inline
assumption weakening of this adapter. No algebraicity/irrationality drop is justified.
ChatGPT math MCP: unavailable (no matching callable tool); no invocation claimed.

## Golfing rule pass — all 42 slots

| Rule | Actual result |
|---|---|
| 1.1 by-exact wrapper | applied: direct composed term |
| 1.2 by-rfl | n/a: no rfl wrapper |
| 1.3 rw+exact | n/a: no rw |
| 1.4 simp+exact | n/a: no simp |
| 1.5 trailing rfl | n/a: no simp/rfl pair |
| 1.6 constructor pair | n/a: no constructor |
| 1.7 apply+exact | n/a: no apply chain in shipped proof |
| 1.8 by_contra+push_neg | n/a: no contradiction block |
| 1.9 eta reduction | n/a: no lambda |
| 1.10 single-use have | n/a: zero have binders |
| 1.11 apply+intro | n/a: no introductions |
| 1.12 redundant show | n/a: no show |
| 1.13 have projections | n/a: no have/projection destruction |
| 1.14 merge rw | n/a: no rewrites |
| 1.15 unsqueeze terminal simp | n/a: no simp only |
| 1.16 squeeze nonterminal simp | n/a: no simp |
| 1.17 dot notation | direct `_h_alg.extendScalars` uses found API; iff.mpr retained |
| 1.18 less parentheses | n/a: no by/lambda argument or `$`; ordinary composed term arguments already fit, no useful compression |
| 1.19 push_neg | n/a: absent |
| 1.20 trivial existential helper | n/a: public headline, no witness helper added |
| 2.1 whole grind | clean complete-body scratch fail_if_success/solve confirms failure to close |
| 2.2 delete before grind | n/a: no grind in shipped proof |
| 2.3 simpa consolidation | n/a: no simplification chain |
| 2.4 fun_prop | n/a: not a continuity/differentiability/measurability goal |
| 2.5 positivity | n/a: headline is not a positivity/nonzero goal |
| 2.6 gcongr | n/a: no monotonicity calc |
| 2.7 lia/omega | n/a: not a Nat/Int linear arithmetic goal |
| 2.8 aesop | clean complete-body scratch fail_if_success/solve confirms failure to close |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast normalization goal |
| 2.10 decide | n/a: infinite real/integer quantified analytic proposition, no finite decision computation |
| 2.11 field_simp/ring | n/a: no algebraic equality goal |
| 2.12 linear_combination | n/a: no ring-ending block or polynomial identity |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 calc composition | n/a: no calc |
| 2.15 shared goal closer | n/a: no multiple subgoals in final term |
| 3.1 erw→rw | n/a: neither appears |
| 3.2 legacy function tactics | n/a: none |
| 3.3 omega→lia | n/a: neither appears |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | n/a: external theorem, not an API rewrite rule; no new attributes |
| 3.6 simp_all | n/a: neither form appears |
| 3.7 remove limits | n/a: no limits present or introduced |

Step-back checks: clean scratch whole-body `simp` and `exact?` also fail to close. `apply?`
suggests only `(isDiophantine_iff _h_irr).mpr ?_`, leaving the exponent-bound goal; it is not
a closed proof. The initial live multi_attempt leaves the original continuation line behind;
its errors/empty goals are contaminated and are not treated as proof success. A first scratch
run additionally exposed that `apply?` can report tactic success while offering remaining
goals; that run exited1 and was retained. After removing that partial-search assertion, the
complete scratch file exited0 (30.680s), including negative closed-proof automation/drop checks
and the full positive direct-transport proof. No unresolved goals/sorry result accepted.
The body is one composed expression, so no proper 3–5-line chunk remains to automate.
Alternative recovery through accepted finite helper + Roth.roth is longer (5 body lines);
it is checked independently below, while the accepted iff route remains the clearer headline.

## Semantic and build gates

Actual final family enumeration precedes all current guards: IsDiophantine[],
IsDiophantine._proof_1[], isDiophantine_iff[], isDiophantine_iff._simp_1_1[u_1],
thueSiegelRoth[], and the private finite helper[]. No guessed generated suffixes/universes.

`LiveGuard.lean` checks exact old five TYPE/universe representations and an explicit
constructor-by-constructor strict Expr comparison for headline TYPE (Name, levels, BinderInfo,
literal, metadata/Syntax/source information covered). Final headline TYPE823B is unchanged.
The genuine/entry headline source equality plus original2 accepted strict TYPE receipts bind
the genuine contract; no hygiene exception is used. Accepted helper is not re-inferred.

Target opaque `value! true` is independently inferred with default maxHeartbeats200000,
synthInstance20000, maxRecDepth512, compared with the strict stored TYPE; no MVar, levelMVar,
FVar, loose bvar, or sorryAx. Final VALUE9234B/hash6990197182669633896; entry VALUE10510B/
hash13987190834422677417. Hash/length are receipts, not a claim of full raw VALUE identity.
Axioms exactly propext, Classical.choice, Quot.sound. Target direct dependencies have upstream
module indices and exclude self; there is no target-generated family or caller. Local lower
dependencies are accepted iff/predicate; Roth.roth is lower imported Main. Lean's ordered
declarations and the upstream dependency checks exclude forward/circular alias construction.
Repository search finds no headline callers; no caller proof is copied.

Independent recovery bypasses iff and the target, using the accepted finite-bound helper and
Roth.roth with the original fraction-ring transport. It has exactly the target TYPE/universes,
default opaque-value inference, closure and standard axioms, with no target/iff/generated/caller
dependency. Recovery VALUE333110B/hash6315586318359309444. This is genuine independent recovery,
not a proof copied from a caller; helper source is unchanged and no helper re-audit is claimed.

| Gate | Actual evidence/result |
|---|---|
| Ordered full build | `/Users/ramin/.elan/bin/lake build`, exit0, 5.474s; final-build-terminal.json |
| Separate file build | subsequent `lake build Roth.LeanEval`, exit0, 27.406s; final-eval-build-terminal.json |
| Full final file native | subsequent `lake env lean Roth/LeanEval.lean`, exit0, 28.373s; final-native-terminal.json |
| Semantic/strict guards | `lake env lean /private/tmp/roth-eval-thue/LiveGuard.lean`, exit0, 46.988s |
| Independent recovery | `lake env lean /private/tmp/roth-eval-thue/Independent.lean`, exit0, 36.070s |
| Final unfiltered LSP | success true; partial false; timed_out false; items[]; dependencies[] |
| definition_protected | no def/abbrev edits; all non-target bytes equal entry |
| theorem_statement_protected | source signature repack only; exact TYPE, universes, public binder names/order preserved |
| structure_gate | two body lines ≤15, no conjunction/branch |
| naming_gate | explicit external-name exception; no forbidden patterns; no new rename |
| line_packing_gate | both final signature rows measured, no repack remains |
| inequality_orientation_gate | explicit zero-occurrence table |
| caller preservation | no headline callers; whole project and separate file builds pass |

All compiler/native/LSP calls serialized under the owner's exclusive lease. All corresponding
launch PID/PGID and driver PID/PGID actually absent in preprofile-drain.json. Scratch raw outputs
and failures retained; no Main/root native or LSP replay, and no accepted helper re-certification.

## Performance pass

Outcome: FAST-BOARD for the scoped headline, no deferral, no limit raise, no scaffolding in source.
Owner explicitly granted PROFILE HOLDACK before any prefix/driver/map/freeze/env preparation;
owner held writes/reviews/compiler/native/LSP/raw parsing until actual terminal and drain. Three
serial full-prefix captures used exactly `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 <prefix>`, separate stdout/stderr. Genuine/entry/final prefix files
are byte-exact snapshots through the final headline (including the namespace close). Existing
lower helper elaboration in entry/final captures is incidental, not helper recertification or
headline charge. No Main/root profiling or broad verification replay.

Capture terminal: genuine exit1/105.748s, entry exit0/34.139s, final exit0/35.729s. All44 frozen
inputs (prior40 canonical source/config/artifact/tool inputs +3 prefixes+driver) equal before/after.
Full parent environment (2814 bytes) and lake-env environment (6212 bytes) compare equal in
memory; only hash/length and safe PATH/toolchain persisted. No full environment or unrelated
process argument capture. Before profile, one ordinary `ps -p 46861,46864 -o
pid=,pgid=,etime=,comm=` was sandbox-denied, exit127, no process data obtained. Scoped
os.kill/os.killpg zero-signal observations of known IDs supplied actual task/driver/group drain;
no permission workaround or fabricated process record.

All task47272/47310/47335 PID/PGIDs and driver47250 PID/PGID absent in profile-drain.json.
Sent terminal RAW UNPARSED evidence and drain to owner; owner granted explicit PROFILE RELEASE
before any raw-content parsing. Raw failures and all valid rows retained. Source/environment
freeze and raw stream hashes/lengths are in profile-terminal.json, with raw_parsed:false at
the release boundary.

The genuine capture fails in the old equivalence at source L22: its call to
`Roth.eventually_div_rpow_lt (one_div_pos.mpr hC) ...` does not match the now-accepted lower Main
API. This is a genuine historical source/current-dependency incompatibility, not a final-source
error or heartbeat failure. Its headline trace is preserved (77.638ms conservative) but is
**excluded as a valid timing baseline**, since earlier elaboration failed. It was not rewritten,
rerun, or silently promoted to a pass. Valid entry/final captures stand independently. No timing
ratio, speedup claim, or noise waiver is made across these contexts.

Every full canonical target command payload (docstring+complete signature+complete proof)
matches its actual source after whitespace normalization; timing.json stores the boolean and
canonical payload hash/length. No one-line substring matching. Actual target family has no
generated declarations; its single Kernel child is charged through its disjoint addDeclCore
parent. All target-range depth0 nodes are accounted for:

| Disjoint target root/category | Entry ms | Final ms |
|---|---:|---:|
| Complete declaration command (includes header child) | 7.105 | 9.859 |
| Async proof elaboration (includes value/addDecl children) | 35.325 | 44.757 |
| Kernel parent (Kernel child itself 8.121/8.086ms, not added twice) | 8.153 | 8.126 |
| Async linters | 2.873 | 2.707 |
| Canonical non-Meta total | 53.456 | 65.449 |
| Detached Meta.whnf, conservatively charged separately | 0.358 (482 roots) | 0.557 (492 roots) |
| Actual lazy DATA roots / compilation roots | 0 / 0 | 0 / 0 |
| Conservative disjoint total | **53.814** | **66.006** |

Meta.whnf is not DATA; nested header/value/kernel/lint children are not double-counted. Final
66.006ms is below750ms and1000ms; the ≥750ms same-freeze repeat rule does not trigger, so no
unchanged second/third capture was made. The term is small and below budget despite slightly
higher measured wall time than entry; direct transport reduces the opaque VALUE receipt from
10510 to9234 bytes, but no causal performance improvement is asserted. Fresh independent file
review remains responsible for the final whole-file board.

## Phase checklist and handoff

| Required step | Status |
|---|---|
| Step1 reference reads | ✓ full required reads |
| Step2 full audit | ✓ all24 slots specific |
| Step2.5 mathlib search | ✓ all5 actual methods |
| Step2.6 generalisation | ✓ all3 binders, drop/inversion/public literature |
| Step2.7 line packing | ✓ every signature line measured |
| Step2.8 inequality table | ✓ explicit zero occurrence row |
| Step3 golfing | ✓ all42 slots specific |
| Step4 reflection | ✓ closed automation checks and distinct recovery route |
| Step5a LSP | ✓ complete unfiltered clean |
| Step5b gates | ✓ strict/default semantic guards and cited build exits |
| Step6a renames | ✓ none; explicit benchmark-name exception |
| Scoped Buzz | ✓ 66.006ms conservative, held capture/drain/release complete |

Full/branch/headline limits
are satisfied; declaration4→4 lines, body2→2 lines, zero syntactic wrapper tactics remain.
No suggested change is left undecided or omitted. Final semantic/native/LSP/build evidence
binds source4c77924b; no executable source change followed those gates.
Renames queued: none. Comments preserved: none present, none removed. Refactoring needed: none.
Built-in simplify is unavailable; no invocation claimed. The mandatory NEW independent full-file
review after owner acceptance/publication supplies the separate holistic review. That review,
root file-final, five global renames and final project checks remain outstanding beyond this worker.
263/263 originals alone will not imply project completion.

Final-END.json and final-drain.json are the terminal handoff receipts. The worker releases all
compiler/native/LSP/source leases to the owner only after writing these actual drain records.
Owner acceptance/publication is still required before dispatching the fresh independent file review.
