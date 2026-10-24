# Roth/Main.lean — independent whole-file final review

This is a fresh holistic file review after the 17 published original-declaration audits. Actual `Skill(simplify)` was unavailable; I used an independent manual mathematical and source review, with the installed Lean/mathlib-quality instructions and mandatory cleanup, review, style, search, generalisation, proof and profiling references. I read the complete entry file and genuine 684-line project-original file. No original audit was restarted, no original credit is added or removed, and this report does not assert project completion.

## Findings and applied changes

The unreduced-pair definition of `approxSet` needs the bounded-denominator/fiber argument: finiteness of reduced rational values alone would not prove the integer-pair conclusion. The current reduction and rational endpoint handle this correctly. The five headline helpers represent coherent correlated choices and estimates, with live consumers; no extra wrapper, tuple or extraction is warranted. The integral-normalization, approximation-weight and all five headline helpers are live in actual TYPE/opaque-VALUE dependency metadata.

Actual metadata for every initial Main/Eval declaration found no TYPE or opaque-VALUE consumer of private `eta_lt_of_lt`. I removed its seven-line isolated block, including prose that described only that obsolete proof. Original audit 9 remains historical credit. Other ordinary signposts, public/module documentation and paper citations are preserved.

The mandatory production-file timing sweep found concrete failures. Bounded trace-guided proof changes replaced a broad square simplification, continuity automation, denominator clearing and large arithmetic searches with specific rewrites, continuity constructors, cancellation, explicit order bounds and smaller certificates. The five changed mathematical roots are `exists_m`, `exists_delta`, `exists_degrees`, `one_le_prod_pow_mul_abs_eval`, and `roth_log_bound_aux`. Later edits were restricted to actually failing roots. Four changed roots are original public proofs (`exists_m`, `exists_delta`, `exists_degrees`, integer lower bound); the fifth is the introduced private logarithm helper. Of the seven introduced private helpers, the other six remain entry-exact. Original 9's private eta lemma is retired. The earlier logarithm-helper report and its declaration hash are historical accepted source, not the current source freeze; its contract and independent proof are reused alongside fresh changed-VALUE/current file-final evidence. Historical helper reports are unchanged. No signature, conclusion, resource budget, helper interface or accepted mathematical choice changed in this batch. Failed timing samples remain evidence; no unchanged third capture or noise waiver was used.

## Public contracts and source checks

Every retained written signature matches the saved entry exactly. Fresh actual full TYPE and universe comparisons additionally cover every retained public, private, generated and Eval declaration. There is no current-versus-entry hygiene exception. Historical project-original weakenings remain those accepted by the individual audits:

| Public declaration | Contract relative to the genuine project original |
|---|---|
| `approxSet` | Preserved unreduced-pair definition |
| `exists_nat_mul_isIntegral` | Preserved |
| `approxSet_den_le_finite` | Preserved |
| `eventually_div_rpow_lt` | Removed positivity assumption on `M` |
| `reduction` | Preserved |
| `exists_monic_aeval_eq_zero` | Removed irrationality; multiplication by `X²` covers the small-degree case |
| `exists_reduced_approx` | Preserved |
| `exists_m` | Removed positivity assumption on `n` |
| `exists_delta` | Removed positivity of `n` and redundant inequality (47) |
| `exists_approximants` | Removed unused positivity of `δ` |
| `exists_degrees` | Accepts `δ ≤ 1` and non-strict adjacent logarithm bounds |
| `one_le_prod_pow_mul_abs_eval` | Preserved |
| `abs_eval_lt_of_le_index` | Removed nonzero-polynomial and strict positivity assumptions on `r,c`; accepts `κ ≥ 0` and non-strict approximation bounds |
| `roth_of_isIntegral` | Preserved |
| `roth` | Preserved |
| `roth_rat` | Preserved bounded accepted API, including its irrationality assumption |

The three imports remain justified: irrationality supplies rational non-equality and scaling facts; integral algebraicity supplies the integral multiple; `Roth.MainLemma` supplies the polynomial argument. Mathlib imports precede the project import in alphabetical order. I found no concrete redundant import warranting deletion. Unknown copyright metadata remains unchanged; the existing line-1 header warning is the only diagnostic. All ordinary proofs have at most 30 non-comment body lines, the headline has 15, branches have at most 10 and width is at most 100. No scaffold, `sorry`, new axiom, resource raise or `native_decide` was introduced. The coordinator's five-name global rename queue is untouched.

## Semantic method and qualifications

The saved entry precedes all Lean/golf work. Fresh actual defining-module inventory initially found 49 rows (Main 44, Eval 5, root 0), including generated DATA, actual nonempty universes and opaque declarations whose ordinary `hasValue` flag is false. Dead-helper deletion left 48. Replacing denominator clearing retired seven generated integer-family simplification declarations. Inventories are discovered before individual guards; no suffix or empty-universe assumptions are used.

All TYPE checks use strict recursive Expr comparison, including Names, Levels, BinderInfo, literals, metadata, projections and remaining syntax, plus exact raw serialized TYPE/universe equality. They do not use Expr BEq shortcuts or definitional equality for TYPE preservation. Actual opaque VALUE inference is under per-command defaults 200000/20000/512, with closed expressions, no metavariables, level metavariables, free/loose variables or `sorryAx`, only `propext`, `Classical.choice`, `Quot.sound`, no self dependency, acyclic local graph and actual upstream origins. Definitional equality is used only to check an inferred VALUE type against its declaration TYPE.

The first 48-row guard run retained 36 valid rows despite scratch Name-quotation failures. A quoting-only supplement retained two more; the final outstanding-name supplement passed the remaining ten. Previously valid VALUE inferences were not repeated. Subsequent source changes rechecked the complete current TYPE inventory and VALUE fingerprints/dependencies, and freshly inferred only actually changed roots or generated families. Unchanged proof evidence is reused through exact retained source/TYPE binding and VALUE hash/byte-length/dependency comparison; this is explicitly **not** fullraw VALUE equality. VALUE serialization stayed in memory and was not dumped. An aggregate Python origin-index assumption was corrected to the actual observed module index without rerunning passed Lean checks. Candidate compile failures and their corrected successful runs are preserved in scratch.

Accepted independent proofs for the five changed roots are reused, with actual current production TYPE equality binding their unchanged contracts to prior accepted independent TYPE/VALUE/no-self/upstream checks. No helper or independent proof was reproved. `accepted-independent-reuse.json` identifies sources, oleans and owner acceptance receipts. For choose-m, delta-choice and integer-bound, compact historical source hashes were unavailable: artifact hashes there were observed now and are not backdated historical bindings; prior accepted proof/TYPE/DAG evidence and unchanged dedicated artifacts are the qualification. Degrees and logarithm artifacts also match their actual historical source/olean hashes. Historical finite hygienic binder exceptions in independent-proof comparisons remain limited to those prior accepted receipts; they are not a new current/entry exception.

## Production timing method

Each capture runs the actual complete `Roth/Main.lean` with `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0`, separate stdout/stderr, and no prefix substitute. All 23 written commands are matched to complete canonical printed payloads, using whitespace and standalone-comment normalization only. The source-backed Lemma-macro/recursive-command binding from `roth-main-eta-bound/final-profile/expanded-command-parent-binding.json` distinguishes nested expanded commands from the outer source command. Rows sum disjoint outer command, async proof, kernel parents, compiler parents and lint roots; nested timings are not added twice. Every actual generated family is kernel-covered. No Meta roots were excluded or cross-family lazy DATA roots encountered in either final sample. Each covers 36 kernel groups, one compiler group and 105 disjoint row roots; all 36 actual Main family Names are covered.

Each phase had an owner HOLD acknowledged before preparation, exact current 40-input source/tool/import/default/env freeze, safe full parent/Lake environment equality in memory only, and actual terminal-zero/drained/absent driver and process groups. Only allowlisted toolchain fields and hash/length evidence are persisted. Raw traces were unparsed until explicit owner RELEASE after drain. A row at least 750 ms causes exactly one same-freeze repeat; all actual samples must remain below 1000 ms. Historical helper-prefix log 962.731/852.705 and integer 923.777/917.011 are accepted separate contexts, not substitutes for these whole-file measurements. No historical ratio or causal performance claim is made.

## Final current gates and bindings

Final source: `6bc428c62fb96296fc155ece49cfa2c1929199f4582fae4c7ecc6c2223df83a8`, 581 lines, 35653 bytes (entry 582 lines, 35257 bytes). Eval source is entry-exact. The final degree argument chooses the scale above a finite supremum of pointwise ratios, derives the large-degree bound directly from the ceiling lower bound, and proves adjacency by scalar order and correctly oriented multiplication/division cancellation APIs. It contains no `linarith`, `nlinarith`, `convert` or `ring`. This substantive whole-proof reassessment followed valid failures of several marginal candidates; none was waived.

The coordinator explicitly approved reordering the last cycle: current Main module/target semantics → whole-source performance → all remaining broad gates. The preliminary candidate command did not refresh Main's olean; actual `lake build Roth.Main` did (43.564 s), then the combined actual 41-row inventory/strict metadata/degree-only VALUE gate passed (108.204 s). Broad caller gates were honestly pending during K/L. After both timing samples passed, final **FULL `lake build` 33.967 s → separate `lake build Roth.LeanEval` 35.280 s** passed. Closing combined actual 41-row metadata passed in 96.671 s: inventory, strict/raw TYPE/universes and VALUE hash/length/dependencies exactly match the current binding; no unchanged VALUE inference was repeated.

Serial native checks: actual same-source `lake env lean Roth/Main.lean` 30.691 s reused from the successful candidate; affected Eval 31.275 s and root 28.916 s freshly passed. Main's hash was observed after the ordered edit→compile→terminal sequence with no intervening source write, not described as a contemporaneous launch hash. Complete unfiltered LSP for all three current files returned success, nonpartial, nontimeout and no failed dependencies; only Main's unchanged line-1 header warning remains.

`closing-semantic-supplement.json` records broad closure separately: K/L frozen inventory, semantic receipt, driver and defaults were not overwritten. Actual comparison of every one of the 40 frozen inputs after broad builds, native checks and complete LSP gives **no delta**. No unused-caller artifact exception was needed; source/import/tool/default bindings remain exact for timing reuse.

Final 41 rows: Main 36, Eval 5, root 0. All retained TYPE/universes are strict/raw entry-exact. Final degree VALUE was freshly inferred; other 40 reuse passed checks through unchanged fields/dependencies/source bindings. Earlier five-root and subsequent two-/one-root updates are journaled in scoped receipts. Accepted independent proof bindings and their historical qualifications above remain applicable.

## Final whole-file timings

Milliseconds from disjoint actual roots. All 23 rows pass in **both** samples, maximum **916.000 ms**. The mandatory same-freeze repeat is complete; no unchanged third capture.

| Written declaration | K | L | Body lines |
|---|---:|---:|---:|
| `approxSet` | 64.279 | 45.244 | 0 |
| `exists_nat_mul_isIntegral` | 203.419 | 180.422 | 3 |
| `approxSet_den_le_finite` | 840.626 | 908.099 | 23 |
| `eventually_div_rpow_lt` | 116.587 | 123.251 | 6 |
| `reduction` | 578.686 | 614.548 | 14 |
| `exists_monic_aeval_eq_zero` | 125.139 | 133.190 | 4 |
| `approxSet_num_den_mem_aux` | 328.651 | 316.874 | 6 |
| `exists_reduced_approx` | 266.468 | 228.973 | 22 |
| `exists_m` | 681.648 | 714.332 | 21 |
| `exists_delta` | 535.689 | 593.627 | 19 |
| `exists_approximants` | 362.769 | 384.193 | 15 |
| `exists_degrees` | 794.850 | 791.624 | 30 |
| `one_le_prod_pow_mul_abs_eval` | 750.281 | 824.668 | 17 |
| `abs_prod_pow_le_rpow_of_le_weight` | 624.959 | 746.756 | 21 |
| `abs_eval_lt_of_le_index` | 483.311 | 616.787 | 19 |
| `exists_roth_parameters_aux` | 548.268 | 549.910 | 10 |
| `exists_roth_approximants_aux` | 359.877 | 406.934 | 13 |
| `one_lt_roth_eval_bound_aux` | 516.194 | 600.137 | 13 |
| `roth_product_bound_aux` | 532.084 | 670.198 | 15 |
| `roth_log_bound_aux` | 730.665 | 916.000 | 30 |
| `roth_of_isIntegral` | 518.275 | 674.969 | 15 |
| `roth` | 46.139 | 78.436 | 3 |
| `roth_rat` | 77.870 | 66.538 | 4 |

Body lines exclude opening `by` and ordinary comments; `approxSet` is a definition. Logarithm helper has one additional preserved comment line. Headline 15, ordinary maximum 30, branch maximum 10, width 100.

Earlier **valid** whole-file failures remain separate source contexts:

| Sample | Actual rows at or above 1000 ms |
|---|---|
| A | `exists_m` 1405.503, `exists_delta` 1350.057, `exists_degrees` 1183.412, `one_le_prod_pow_mul_abs_eval` 1445.133 |
| B | `exists_m` 1487.398, `exists_delta` 1358.966, `exists_degrees` 1209.937, `one_le_prod_pow_mul_abs_eval` 1528.892, `roth_log_bound_aux` 1095.459 |
| C | `exists_degrees` 1134.155 |
| D | `exists_degrees` 1065.124 |
| E | `exists_degrees` 1063.544 |
| F | `exists_m` 1046.241, `exists_degrees` 1119.127 |
| G | `exists_degrees` 1001.183 |
| H | `exists_degrees` 1011.813 |
| I | `exists_degrees` 1047.413 |
| J | `exists_degrees` 1052.943 |

A/B source `058f2108…`; C/D `8e1c8e6e…`; E/F `fd8fa077…`; G/H `3ed13163…`; I/J `6fed3641…`; final K/L `6bc428c6…`. Each pair is internally same-freeze. Candidate errors, including quoting, coercions and cancellation orientation, were corrected before successful gates. No sample was substituted, averaged away, rounded down or dismissed as noise. No optional edit was made to a passing root without a subsequent concrete failure.

## Evidence and handoff

Scratch: `/private/tmp/roth-main-final/`. Main receipts: `entry-inventory.json`, `dead-helper-confirmation.json`, `semantic-receipt.json`, `accepted-independent-reuse.json`, `current-semantic-receipt.json`, `closing-semantic-supplement.json`, `final-static-receipt.json`, `final-performance-receipt.json`; final `profile-{k,l}/allrows.json` plus raw stdout, terminal/default/env/freeze/drain/HOLD/release records. `closing-LSP-{Main,Eval,root}.json` contains complete diagnostics. Every all-row receipt identifies the macro parent-binding source. No VALUE dump or giant independent replay was created.

Only `Roth/Main.lean` and this report are source/report deliverables. Historical per-original/helper reports are unchanged. Git, shared progress, publication, file-final credit and coordinator handoff belong to the owner. `FINAL-END.json` records the final task-owned process drain and lease handoff after all known jobs/tool sessions finish.

Owner review: the actual frozen maps contain 40 paths; the declaration inventory has 41 rows. This corrects the input-count label in phase messages and the legacy static-receipt key without changing captured inputs or gates. Owner independently bound both final raw full canonical payloads, all disjoint roots/kernel/compiler parents/sums, all 40 current frozen paths, and all 12 expanded private-lemma theorem payloads across K/L to the actual macro implementation. The normalization helper is already a private theorem and has no lemma-macro expansion. Narrow owner guards initially assumed 41 paths and seven lemma macros; actual maps and declaration kinds corrected those assumptions before acceptance, with no Lean or capture replay. Receipt: `/private/tmp/roth-main-owner/main-final-profile-owner-review-v1.json`.
