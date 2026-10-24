# Roth/LeanEval.lean cleanup

## Preparation and file audit

Entry: clean `ramin-cleanup`, `f83e3253b5c3aff98a6b308545035924c0a16c9d`; 60 lines, 3010 bytes, SHA256 `610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca`. This is a classic import file with three genuine original declarations: `IsDiophantine` (definition, lines 11–13), `isDiophantine_iff` (lines 16–49, 32 proof lines), and `thueSiegelRoth` (lines 54–58, two tactic lines excluding `by` (the earlier three-line estimate counted the wrapper)). The actual compiled entry inventory has five rows, including `IsDiophantine._proof_1` and `isDiophantine_iff._simp_1_1`; the latter has universe `u_1`. Generated families are inspected before guards.

The file translates the exact LeanEval approximation predicate to the unreduced-pair exponent bound of `Roth.roth`. For irrational points, finite exceptional pairs permit a positive lower constant; conversely a positive lower constant excludes infinitely many pairs at exponents above two. The headline then applies Roth to an algebraic irrational real. This mathematical contract is retained.

| Audit | Entry finding / action |
|---|---|
| A.1 copyright | Missing metadata; unchanged under explicit user preservation instruction. |
| A.2 module doc | Existing exact LeanEval statement/source citation is preserved; assess a concise title in independent file final. |
| A.3 imports | Sole `Roth.Main` supplies all required API; no import addition warranted. |
| A.4 section headers | None; no contentless section. |
| A.5 file length | 60, below all splitting thresholds. |
| A.6 options | None; no raised resource limits or disabled lint. |
| A.7 mechanical | No deprecated lambda, dollar application or `push_neg`. |
| B diagnostics | Accepted Main closing complete unfiltered Eval diagnostics were clean; reuse is explicitly qualified below/by declaration receipts. |
| C.1 definition | Meaningful external predicate with two theorem users; public, no rename; missing docstring is actionable. |
| C.2 equivalence | Public explanatory API; existing docstring preserved; 32-line proof and large branches require substantive golf/decomposition review. |
| C.3 headline | Public external LeanEval theorem; existing named theorem contract retained; direct proof can use term mode. |

## Baseline (Phase 0)

The accepted immediately preceding Main file-final checks are reused as the unchanged-source doctor: actual full `lake build` 33.967 s followed by separate `lake build Roth.LeanEval` 35.280 s, then native Eval 31.275 s/root 28.916 s and complete unfiltered LSP for Main/Eval/root. All passed; only Main’s existing header warning remained. This is qualified prior evidence, not a new owner invocation. Main bytes remain accepted-exact; the worker saved genuine/current Eval before its docstring edit. The owner observation binding occurred after that insertion, so is explicitly not a pre-edit Eval snapshot. Prior closing receipts and qualified current bindings live under `/private/tmp/roth-main-final/` and `/private/tmp/roth-eval-owner/entry-owner-binding.json`. Optional cache/linter executable skipped; Lean native diagnostics include available linters. Each changed executable source must receive current ordered build/caller gates before publication.

## Workflow

Full installed cleanup/cleanup-all and Lean/mathlib-quality references apply. Each original receives a fresh dedicated worker and its own validated publication before the next edit. A new independent whole-file reviewer is mandatory after all three originals; the unavailable Claude `Skill(simplify)` is replaced by that substantive independent review, never claimed as an actual invocation. The five global renames remain for the coordinator’s project pass. Declaration and file-final completion are separate.

Original1 `IsDiophantine` accepted: exact definition retained, precise two-line scaled-error docstring added. Dedicated [audit](LeanEval-IsDiophantine.md), strict actual family2/default proof gates, exact-prefix42.616ms and owner raw/canonical/source review pass. Broad ordered build/native/LSP evidence is qualified unchanged-executable-source reuse. No whole-file final credit yet. Owner receipt: `/private/tmp/roth-eval-owner/IsDiophantine-owner-accepted-v1.json`.


## Original2 joint result

`isDiophantine_iff` is accepted with its necessary arbitrary-exponent finite-exception helper. Original body32→13 lines, forward9/reverse3; helper17 tactic lines. The helper’s NEW fresh independent audit uses a separate finite-induction proof and fixes only the measured implicit-minimizer unification issue with `hmin (p,q)`. The SAME original author then resumed and completed all original2 gates; helper and parent publish jointly, with only one original credit.

Current source63/3343B SHAe4f3998fd64e5a3acc1ccd4bc6588537ebf0e43ceeb4642343dd2795be294d35. All public signatures/docstrings and unrelated code remain exact; actual inventory6 includes all old5 plus helper, with all old TYPE/universes raw-exact. Current target/caller/generated default opaque proof gates pass; predicate/helper passed inference is reused by exact source/TYPE/hashlen/deps, without fullraw VALUE identity claims. Independent accepted-entry proof recovery is explicitly distinct from the genuine d2eb source/API.

Current target321.509ms and accepted helper291.597ms pass; old failing profile contexts remain in their reports. Owner bound the complete raw canonical payloads, narrow printer-space pair, macro implementation, disjoint root sums/kernel families, metadata/DAG and all43 frozen current inputs. Final actual ordered FULL4.646s→separateEval2.954s→nativeEval29.317s and complete unfiltered LSP pass; all tasks/drivers drained and leases released. [Original2 audit](LeanEval-isDiophantine_iff.md), [helper audit](LeanEval-exists_pos_div_rpow_lt_aux.md). Owner receipts: `/private/tmp/roth-eval-owner/{iff-owner-accepted-v1,finite-helper-owner-accepted-v1}.json`. Fresh original3 and mandatory NEW independent file-final review remain.


## Original3 result

`thueSiegelRoth` is accepted after a fresh dedicated audit: direct `IsAlgebraic.extendScalars` transport, term proof and packed signature. The exact external name, public binders/order/TYPE/universes and docstring remain preserved; every non-target byte equals the original2 entry. Source63/3344B SHA4c77924b46d4b6559c8fc6118710e89c92fe07b0a49eaff90011e76edb2429d0. All old five TYPE/universes remain raw-exact; current headline opaque VALUE/default inference/closure/std axioms and an independent helper-plus-Roth recovery pass. VALUE hash/length receipts are not raw identity claims.

Actual ordered FULL5.474s→separateEval27.406s→nativeEval28.373s, complete unfiltered LSP and guards pass. Final disjoint timing65.449ms plus492 conservative detached Meta.whnf0.557ms gives66.006ms; entry53.814ms passes separately. Genuine source context fails at the historical eventual-bound API in the old equivalence; its headline trace is excluded from valid baselines, with failure retained. No cross-context speedup claim or unnecessary repeat. Owner independently binds full canonical payloads, roots/kernel/sums and all44 current frozen inputs; actual tasks/drivers/groups drained and END released. Narrow owner parsing assumptions were corrected without Lean/capture replay. [Original3 audit](LeanEval-thueSiegelRoth.md), owner receipt `/private/tmp/roth-eval-owner/thue-owner-accepted-v1.json`.

All three original audits are accepted; publication is pending this exact source/audit checkpoint. A NEW independent whole-file review, root file-final, five global renames and final project gates remain. This does not claim project completion.
