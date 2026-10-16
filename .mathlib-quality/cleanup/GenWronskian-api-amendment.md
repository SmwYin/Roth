# GenWronskian approved public-instance amendment

The user explicitly approved these two removals on 2026-10-16. This is a narrow amendment
to the completed whole-file audit, not a new declaration audit or a repeat of its 24-item,
42-rule workflow. The original19 declaration tally and21 dedicated reports do not change.
Both installed Lean/mathlib-quality skills, the proposal, final report and both affected
dedicated reports were read for this amendment.

## Exact scope and protection

Source before SHA256 `cc7b2786088d6c839d36a14d9b5b09a884eb1de1a0d521b3bc2b84c9772cbfcf`.
Final source SHA256 `5283b554baa1fcfce18f2298a0f5181cc58586f22b541dd2222745ef651b6e32`.

- Insert `omit [Fintype σ] in` before the unchanged dependent-family vanishing docstring.
  The theorem now quantifies over arbitrary variable types without a Fintype instance.
- Remove only `[DecidableEq ι]` from `det_sum_rows`. After removal the next complete
  `c` binder fits exactly:80+1+19=100 codepoints, so it moves to the first signature line;
  `N` remains on the following line. All remaining binder tokens and their order agree.

A scripted exact-transformation assertion against `/private/tmp/roth-gen-amend-before.lean`
passes. All original block comments/docstrings are byte-identical; every proof, definition,
import, name, conclusion and other binder remains unchanged. Maximum source width100.
No sorry/admit, custom axiom, native_decide, option/resource override or profiling scaffold
occurs in the source. No toolchain/dependency change or new Lean declaration.

The existence theorem's Fintype binder remains unchanged: its removal was not approved.
The earlier optional coefficient-ring and other mathematical generalizations remain closed.

## Actual verification

Native Lean MCP was discovered through `ALL_TOOLS`; fallback was unnecessary.
`/Users/ramin/.elan/bin/lake build Roth.GenWronskian` completed twice, sessions53662 and21414,
exit0. The second is the final packed source. Logs:
`/private/tmp/roth-gen-amend-{module,packed-module}.log`.

Complete native diagnostics on the final packed module:
`/private/tmp/roth-gen-amend-packed-lsp.json`, success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors. Warnings5→2: preserved missing
authoritative copyright metadata and the unapproved existence theorem's unused Fintype.
All three warnings associated with the two approved unused instances disappear.

Fresh independent new-type reproofs compile with exit0:
`/private/tmp/roth-gen-amend-newtype-{zero,det}.lean`, sessions35236/76425,
with corresponding `.log` files. They import only HasseDeriv/Wronskian, never GenWronskian;
the vanishing proof uses an independently copied exact definition, and neither proof calls
the target theorem. Their printed types omit the approved instances. Their only axioms are
`propext`, `Classical.choice`, `Quot.sound`.

`/private/tmp/roth-gen-amend-actual-types.lean`, session19888 exit0, applies both actual
built target theorems at the new types without the removed instances, prints their complete
types and checks their axioms: exactly the same three standard axioms. Corresponding log
contains no errors or sorry warnings.

Original API compatibility: `/private/tmp/roth-gen-amend-compatibility.lean`, session42174
exit0, compiles the complete original baseline module in its own namespace, checks all13
original public constants and all three public definition values by rfl. The two changed
theorems use eta adapters accepting and ignoring precisely the removed instance; all other
comparisons remain unchanged. The corresponding log prints all13 actual target axiom sets,
each standard only. This proves recoverability at the old quantified types, while explicitly
acknowledging that raw `@` application binder positions change for the two amendments.

Fresh project caller search finds no callers of dependent-family vanishing; `det_sum_rows`
has only the existing same-file private expansion helper, with inferred instance application.
That caller compiles unchanged in the actual module. No caller edit was needed.

## Isolated actual-source performance

Budget1000ms; mandatory repeated sweep for declarations at or above750ms. Every run uses
the pinned `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/GenWronskian.lean` on the final source hash above.
All verification compiler sessions finished before profiling; parent builds stayed idle and
no probes or compiler tasks ran concurrently with either sweep. The native diagnostic call
had completed before profiling. No performance proof edit was made.

The parser was adapted from the completed final audit with a fresh19-declaration line
inventory: `/private/tmp/roth-gen-amend-analysis.json` and
`/private/tmp/roth-gen-amend-profile-parse.py` and
`/private/tmp/roth-gen-amend-profile2-parse.py`. Complete trace/table pairs use
`/private/tmp/roth-gen-amend-profile{1,2}.log` and
`/private/tmp/roth-gen-amend-profile{1,2}-table.json`. An attempted parse while sweep1 was
still running correctly rejected its incomplete inventory; only completed traces count.

Both actual full-source sweeps exit0: sessions78404/92985. All19 declarations are below
1000ms in both sweeps; the mandatory borderline resweep is complete. No limit raise,
performance source change or deferral. Total elaboration times include command and async
elaboration, using the same accounting as the prior final audit.

| Declaration | Final line | Sweep1 ms | Sweep2 ms |
|---|---:|---:|---:|
| `genWronskian` | 26 | 30.63 | 36.30 |
| `genWronskian_eq_zero_of_not_linearIndependent` | 35 | 610.42 | 572.39 |
| `kronecker` | 47 | 24.45 | 25.03 |
| `kroneckerExp` | 51 | 10.80 | 10.39 |
| `kronecker_monomial` | 54 | 164.39 | 176.50 |
| `kroneckerExp_injOn` | 63 | 143.47 | 161.87 |
| `coeff_kronecker` | 82 | 101.98 | 111.80 |
| `kronecker_eq_zero_iff` | 100 | 102.36 | 97.96 |
| `linearIndependent_kronecker` | 111 | 427.41 | 422.66 |
| `derivative_aeval` | 127 | 929.00 | 829.00 |
| `kronHasse` | 139 | 32.65 | 24.23 |
| `kronSpan` | 143 | 23.05 | 19.62 |
| `derivative_kronHasse_aux` | 147 | 998.25 | 907.78 |
| `derivative_mem_kronSpan` | 156 | 332.31 | 332.80 |
| `hasseDeriv_kronecker_mem` | 184 | 469.83 | 451.56 |
| `exists_hasseDeriv_kronecker_eq_sum` | 208 | 189.23 | 184.86 |
| `det_sum_rows` | 222 | 195.64 | 178.76 |
| `wronskian_kronecker_eq_sum_aux` | 232 | 498.43 | 409.31 |
| `exists_genWronskian_ne_zero` | 247 | 412.92 | 348.84 |

## Handoff

SOURCEFINAL/FROZEN: `5283b554baa1fcfce18f2298a0f5181cc58586f22b541dd2222745ef651b6e32`.
All compiler/profiler sessions are finished. Leaf source edits end here; subsequent work
is report-only. Full project build, sequential separate `lake build Roth.LeanEval`, exact
staging, commit and push are parent-owned gates and are not claimed by this leaf.
No Git operation, full project build or shared-log edit was performed by the leaf.


## Owner final gates and publication

Source ownership explicitly revoked at the frozen hash before owner gates. Sequential
owner full `/Users/ramin/.elan/bin/lake build`, session15112 exit0 (2465 jobs), then
separate `/Users/ramin/.elan/bin/lake build Roth.LeanEval`, session83552 exit0 (2464 jobs).
Root Roth omits LeanEval. Logs `/private/tmp/roth-genwronskian-api-amendment-full.log`
and `/private/tmp/roth-genwronskian-api-amendment-leaneval.log`. These cover unchanged
callers and the full downstream closure. Both source hashes (CoeffNorm and GenWronskian)
remain frozen; final diff whitespace/protection checks pass.

The first separately validated amendment was committed and successfully pushed as
`9a9cc37bdf1671d83dc3fb5bef40af943666f8a4` before any GenWronskian source edit.
This second amendment is staged by exact paths with its own dedicated commit/push.
Original tally remains130/264,7/14 files complete. No Index work was begun.
After successful second publication all source/report/shared-progress/Git ownership
returns to the orchestrator; remaining file order starts with Index.
