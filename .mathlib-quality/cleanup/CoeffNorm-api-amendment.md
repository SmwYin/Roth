# CoeffNorm approved API amendment — 2026-10-16

Scope: the user's explicit 2026-10-16 approval of the existing
[API proposal](CoeffNorm-api-proposal.md), applied after the completed
[whole-file cleanup](CoeffNorm-final.md). This is a targeted amendment, not a repeat of
the completed declaration audits or their 24/42-item workflows. The four affected reports
(`CoeffNorm-normOne_mul_le.md`, `CoeffNorm-normOne_prod_le.md`,
`CoeffNorm-normOne_det_le.md`, `CoeffNorm-abs_coeff_det_hasseDeriv_le.md`), both skills,
proposal, and final file report were consulted. Historical reports describe their own
checkpoints; this report records the later approved change.

## Applied change

- Removed unused `[DecidableEq σ]` from `normOne_mul_le`, `normOne_prod_le`,
  `normOne_det_le`, and `abs_coeff_det_hasseDeriv_le`.
- Removed unused explicit `(hC : 0 ≤ C)` from `normOne_det_le`.
- Added proof-local `classical` to multiplication and determinant bounds. The cleaned
  finite-product term already works without an additional classical scope.
- Removed the determinant caller's `(by positivity)` argument in
  `abs_coeff_det_hasseDeriv_le`. The proposal's older `hC0`/`hN0` locals had already
  disappeared during cleanup; neither was reintroduced.
- Repacked only the shortened affected signatures at width 100.

Names, conclusions, all remaining arguments (including `hB0`), imports, definitions,
comments and documentation are preserved. No new helper, axiom, sorry, option, suppression,
limit change, version change or caller-file edit. Project-wide `rg` found no external
uses of the three norm inequalities. The sole external use of the coefficient determinant
bound is `Roth/Theta.lean:440`, an ordinary inferred-instance application requiring no edit.

Final source SHA256:
`ee0b23cfee16cf674512a5c8f912a8030242e736db6e79fc1270be71675e67a9`.
Snapshot: `/private/tmp/roth-coeffnorm-amend-frozen.lean`.
Pinned Lean `leanprover/lean4:v4.34.0`, mathlib revision
`5ed2965256430c3649e86755f9576b54eca72435`; both untouched.

## Verification

Native Lean MCP tools were discovered through `ALL_TOOLS`; native diagnostics worked,
so no fallback was needed. Complete final `lean_diagnostic_messages` on the actual source:
`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, zero errors,
one warning (the user-preserved missing header metadata). The five approved unused-binder
warnings are gone. Evidence: `/private/tmp/roth-coeffnorm-amend-lsp.json`.

`/Users/ramin/.elan/bin/lake env lean Roth/CoeffNorm.lean`, session15145 exit0,
checked the amendment before the final whitespace-only signature packing;
`/private/tmp/roth-coeffnorm-amend-module.log`. Final packed source is checked again by
the integrity and actual-source profile compilations below.

`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-coeffnorm-amend-integrity.lean`,
session11836 exit0; log `/private/tmp/roth-coeffnorm-amend-integrity.log`:

- Includes the actual final source verbatim rather than importing a stale CoeffNorm olean.
- Independently reproves all four new statements. Every use of any affected theorem
  in this reproof chain is replaced by the corresponding independent reproof, so none
  of the four production target constants proves any of the four reproofs.
- Checks each exact fully elaborated new type by `rfl` equality with its independent
  theorem (proof irrelevance applies after the types agree).
- Compiles the historical original module under `Roth.CoeffNormBaseline`; all25 public
  original type/value comparisons pass. The21 unaffected constants compare directly
  by `rfl`, including both definition values. The four changed constants compare after
  lambda abstraction over precisely their removed original arguments. Thus each old
  statement is recovered, including arbitrary supplied decidability instances and hC.
- All33 printed axiom sets (25 production constants and eight affected/reproof checks)
  contain only `propext`, `Classical.choice`, `Quot.sound`.

An initial scratch-only oldtype lambda used unsupported instance-binder syntax and
failed with four parser errors. Ordinary typed lambda binders corrected the fixture;
the complete rerun above passed. No source edit followed that scratch correction. The
historical baseline's unused hC warning is expected scratch evidence, distinct from the
single warning in the production file.

All source lines are at most100 Unicode codepoints; no trailing whitespace or forbidden
sorry/admit/axiom/native_decide/options/limit scaffolding. Affected signature widths:
mul95; prod79/54; det86/81; coefficient bound86/91/58/82/83. No next complete binder
or conclusion fits the preceding line. No rename or inequality reorientation occurs.

## Actual final-source performance

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/CoeffNorm.lean`, session91480 exit0, compiled the
actual final packed source. Budget1000ms; all26 declaration anchors are present and all
conservative totals are below750ms, so no borderline repeat sweep is required. Maximum
625.993ms (`normOne_det_le`). No other compiler/build ran concurrently with this profile;
no source instrumentation or performance-driven source change.

| Affected declaration | Line | Command ms | Proof ms | Conservative total ms |
|---|---:|---:|---:|---:|
| normOne_mul_le | 90 | 4.78 | 134.37 | 149.17 |
| normOne_prod_le | 99 | 7.02 | 94.73 | 111.08 |
| normOne_det_le | 113 | 12.13 | 594.98 | 625.99 |
| abs_coeff_det_hasseDeriv_le | 252 | 50.13 | 202.20 | 263.07 |

Trace `/private/tmp/roth-coeffnorm-amend-profile-trace.log`; complete26-declaration
table `/private/tmp/roth-coeffnorm-amend-profile-table.json`; parser
`/private/tmp/roth-coeffnorm-amend-profile-parse.py`; updated source-line inventory
`/private/tmp/roth-coeffnorm-amend-inventory.json`. The previous completed cleanup parser
was reused with new paths and an actual final-source inventory. Conservative totals add
Elab.command and associated non-linter asynchronous tasks without double-counting nested
trace nodes; proof time is shown separately as a subset. The private Classical wrapper
uses its larger outer/inner command once and explicitly anchored proof tasks. The parser
asserts all26 source declarations were matched. All totals passed the1000ms budget and
the750ms repeat threshold. Source SHA256 remained unchanged after profiling.

## Handoff boundary

Source editing is finished at the hash above. The parent owns the subsequent full
`lake build`, separate `lake build Roth.LeanEval`, final diff review, commit and push.
Those downstream/publication gates are not claimed by this leaf report. This worker
edited only `Roth/CoeffNorm.lean` and this new report; all probes/logs remain in `/private/tmp`.


## Owner final gates and publication

Source ownership explicitly revoked after the leaf freeze, before owner validation.
Owner sequential full `/Users/ramin/.elan/bin/lake build`, session27622 exit0 (2465 jobs),
then separate `/Users/ramin/.elan/bin/lake build Roth.LeanEval`, session35871 exit0
(2464 jobs). Root Roth omits LeanEval. Logs:
`/private/tmp/roth-coeffnorm-api-amendment-full.log` and
`/private/tmp/roth-coeffnorm-api-amendment-leaneval.log`.
Frozen SHA256 unchanged after both. Full downstream build validates the unchanged Theta
caller and remaining project closure. `git diff --check` passes. Only this approved
CoeffNorm amendment and its reports/progress are staged for the dedicated checkpoint;
GenWronskian source editing begins only after successful branch publication.
Original tally remains130/264 and7/14 files complete; no new declaration audit counted.
