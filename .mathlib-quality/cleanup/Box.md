# Box cleanup audit

Baseline commit: `62e7b29`. File: `Roth/Box.lean`. Initial size: 128 lines, 14 declarations.
Dialect: classic imports, no `module`/`public section`. No existing inline proof comments.
Scope: preserve mathematical objects and public API; concrete warranted signature changes need a user decision.

## Phase 0 — baseline

- Cache fetch skipped: pinned dependencies already cached/built.
- `/Users/ramin/.elan/bin/lake build` completed successfully (2586 jobs); log `/private/tmp/roth-box-baseline-build.log`.
- Native complete `lean_diagnostic_messages` returned success, partial=false, zero errors and 21 warnings.
- Separate `runLinter` target is not configured in lakefile.toml; standard linters run during compilation/LSP.

## Phase 1 — preparation

Full source, lean4/mathlib-quality skills, cleanup/cleanup-all workflows, style, naming, golf,
proof-pattern and gate references read. Original source snapshot: `/private/tmp/roth-box-baseline.lean`.

## Phase 2 — punch-list before edits

| Tag | Finding | Disposition |
| --- | --- | --- |
| A.1 | Copyright/license header absent | Parent owns factual metadata clarification; do not invent |
| A.2 | Module docstring present after imports, with definitions/results/references | Preserve |
| A.3 | Eight Mathlib imports alphabetized; no project imports | Preserve; no speculative pruning |
| A.4 | No contentless section headers | No change |
| A.5 | 128 lines | No split needed |
| A.6 | No set_option | No removal needed |
| A.7 | No λ, $, push_neg; mathematical `=>` lambdas in seven declarations | Per-declaration arrow normalization |

### B — authoritative diagnostics

- Line 1: copyright header too short/absent.
- `card_le_card_box`: unused DecidableEq in type.
- `weight_nonneg`, `weight_zero`, `weight_add`, `weight_eq_zero_iff`, `weight_le_card`,
  `weight_mul_left`, `weight_le_degree_div`, `weight_mapDomain`: unused section DecidableEq σ
  plus unused decidability in the theorem type (two warnings each).
- `weight_single`: unused DecidableEq σ in theorem type.
- `weight_mapDomain`: its unused-decidability warning also names DecidableEq τ.
- `weight_le_card`: hr is unused; `weight_mul_left`: hl is unused.
- Total 21 warnings, zero errors. Each declaration worker receives the applicable findings.

### C — declaration inventory and light scan

All declarations have existing docstrings, public names follow their mathematical subjects,
no proof is longer than four lines, no private existential wrapper or long branch exists.
`box` and `weight` have multiple API lemmas and downstream uses; their necessity will be searched.
Public visibility remains pending each worker's usage audit; no blanket privatization.

| # | Declaration | Original lines | Decl lines | Scan |
| --- | --- | --- | --- | --- |
| 1 | `box` | 43–45 | 3 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 2 | `mem_box` | 48–49 | 2 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 3 | `card_box` | 54–55 | 2 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 4 | `card_le_card_box` | 60–62 | 3 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 5 | `weight` | 65–65 | 1 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 6 | `weight_nonneg` | 69–70 | 2 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 7 | `weight_zero` | 74–75 | 2 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 8 | `weight_add` | 79–80 | 2 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 9 | `weight_eq_zero_iff` | 85–87 | 3 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 10 | `weight_single` | 90–92 | 3 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 11 | `weight_le_card` | 97–100 | 4 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 12 | `weight_mul_left` | 104–106 | 3 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 13 | `weight_le_degree_div` | 112–116 | 5 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |
| 14 | `weight_mapDomain` | 121–126 | 6 | Documented public API; descriptive name; short body; inspect hypothesis lint and packing |

## Phase 3 — file-level fixes

No source edits needed: imports/docstring/layout already conform; no options or obsolete
mechanical tokens. Missing header metadata remains an explicit external limitation.
Proof-lambda arrows and packing are handled at the corresponding sequential declaration checkpoint.

## Phase 4 — sequential declaration results

Completed 14/14 dedicated declaration workers. Each completed declaration is fully validated,
committed and pushed before the next source edit.

## Concrete API proposal prepared for user decision

Native `lean_run_code` compiled isolated original proofs of `weight_le_card` without
`hr : ∀ j, 0 < r j` and `weight_mul_left` without `hl : 0 < l` (success=true,
timed_out=false, zero errors). Both also compiled without `[DecidableEq σ]`.
These positivity hypotheses are unnecessary because division is total at zero in Lean.
Exactly one current call each in `Roth/Index.lean` (original lines 241 and 221) would
remove the supplied proof argument. The parent was notified immediately; no signature
or caller change has been applied. This is a concrete lint/API cleanup proposal,
not a prerequisite for independent proof/style cleanup.

| Declaration | Before | After | Change | Declaration gates | Report |
| --- | ---: | ---: | --- | --- | --- |
| `Roth.box` | 3 | 2 | `↦`; body packing | Module/LSP/rfl/isolation/type/axioms pass; full build passed | [Audit](Box-box.md) |

Publication verification for `Roth.box`: actual full `lake build` session 17861 exited 0
(2586 jobs; `/private/tmp/roth-box-box-build.log`); separate `lake build Roth.LeanEval`
session 96802 exited 0 (2585 jobs; `/private/tmp/roth-box-d01-leaneval.log`).
All dependent modules pass; remaining warnings are baseline warnings tracked for their own cleanup.

Declaration 2: `Roth.mem_box`, 2 → 2 lines (−22 characters), redundant simp argument
removed. Full declaration gates pass; [audit](Box-mem_box.md).

Publication verification for `Roth.mem_box`: full `lake build` session 29589 exited 0
(2586 jobs; `/private/tmp/roth-box-d02-full.log`); separate `lake build Roth.LeanEval`
session 68459 exited 0 (2585 jobs; `/private/tmp/roth-box-d02-leaneval.log`).

Declaration 3: `Roth.card_box`, 2 → 2 lines, reviewed unchanged; all declaration
gates pass. Full build session 4764 and separate LeanEval 20469 exited 0
(2586/2585 jobs). [Audit](Box-card_box.md).

## User decision on Box assumptions and metadata

The user approved the recommendation: “Follow your recommendation.” Authorized scope:
remove verified unused positivity hypotheses and DecidableEq arguments from Box theorems,
preserve their conclusions, and adjust the two affected Index callsites. Apply each
verified removal at its sequential declaration checkpoint, with complete dependent builds.
No broader API additions or generalisations are authorized by this decision.
Copyright/license metadata stays unchanged because authoritative facts were not supplied;
the remaining header warning must stay explicit rather than being invented or suppressed.
The card_le_card_box DecidableEq drop is compiler-verified and will be the first application.

Declaration 4: `Roth.card_le_card_box`, 3 → 4 declaration lines plus scoped omission
(net +2 source lines), approved unused DecidableEq removed; `trans_eq` composition
and `↦`. All target gates pass; [audit](Box-card_le_card_box.md).

Final approved-source publication verification: full `lake build` session 11996 exited 0
(2586 jobs; `/private/tmp/roth-box-d04-full-approved.log`), separate
`lake build Roth.LeanEval` session 35385 exited 0 (2585 jobs;
`/private/tmp/roth-box-d04-leaneval-approved.log`). These runs supersede the earlier
proof-only full build 90150 and verify the selected generalized signature plus all callers.

Declaration 5: `Roth.weight`, 1 → 1 line, retained unchanged after generic weight
comparison and definitional/type checks. All target gates and fullbuild76138/LeanEval34164
pass. [Audit](Box-weight.md).

Declaration 6: `Roth.weight_nonneg`, 2 → 2 declaration lines plus scoped omission
(+1 source line); approved unused instance removed and Fintype sum lemma used.
All target gates pass; [audit](Box-weight_nonneg.md).

Publication verification: full `lake build` session 67516 exited 0 (2586 jobs;
`/private/tmp/roth-box-d06-full.log`); separate `lake build Roth.LeanEval` session 32007
exited 0 (2585 jobs; `/private/tmp/roth-box-d06-leaneval.log`). All affected dependents pass.

Declaration 7: `Roth.weight_zero`, 2 → 2 declaration lines plus one scoped omission.
Approved unused instance removed; original proof retained. All target gates pass;
[audit](Box-weight_zero.md).

Publication verification: full `lake build` session 79655 exited 0 (2586 jobs;
`/private/tmp/roth-box-d07-full.log`); separate `lake build Roth.LeanEval` session 57725
exited 0 (2585 jobs; `/private/tmp/roth-box-d07-leaneval.log`). All affected dependents pass.

Declaration 8: `Roth.weight_add`, 2 → 2 declaration lines plus one scoped omission.
Approved unused instance removed; original proof retained after live alternatives.
All target gates pass; [audit](Box-weight_add.md).

Publication verification: full `lake build` session 60506 exited 0 (2586 jobs;
`/private/tmp/roth-box-d08-full.log`); separate `lake build Roth.LeanEval` session 78621
exited 0 (2585 jobs; `/private/tmp/roth-box-d08-leaneval.log`). All affected dependents pass.

Declaration 9: `Roth.weight_eq_zero_iff`, 3 → 3 declaration lines plus one scoped
omission. Approved unused instance removed; positivity and proof retained.
All target gates pass; [audit](Box-weight_eq_zero_iff.md).

Publication verification: full `lake build` session 2639 exited 0 (2586 jobs;
`/private/tmp/roth-box-d09-full.log`); separate `lake build Roth.LeanEval` session 25122
exited 0 (2585 jobs; `/private/tmp/roth-box-d09-leaneval.log`). All affected dependents pass.

Declaration 10: `Roth.weight_single`, 3 → 3 declaration lines plus one scoped omission.
Approved unused instance removed, proof-local classical, signature packed to97characters.
All target gates pass; [audit](Box-weight_single.md).

Publication verification: full `lake build` session 41056 exited 0 (2586 jobs;
`/private/tmp/roth-box-d10-full.log`); separate `lake build Roth.LeanEval` session 58453
exited 0 (2585 jobs; `/private/tmp/roth-box-d10-leaneval.log`). All affected dependents pass.

Declaration 11: `Roth.weight_le_card`, 4 → 4 declaration lines plus one scoped omission.
Approved positivity/instance removed, lambda normalized, sole Index caller adjusted.
Complete Index LSP passes; its newly exposed unused hr is left for Index cleanup.
All target gates pass; [audit](Box-weight_le_card.md).

Publication verification: full `lake build` session 7727 exited 0 (2586 jobs;
`/private/tmp/roth-box-d11-full.log`); separate `lake build Roth.LeanEval` session 44525
exited 0 (2585 jobs; `/private/tmp/roth-box-d11-leaneval.log`). All affected dependents pass.

Declaration 12: `Roth.weight_mul_left`, 3 → 3 declaration lines plus one scoped omission.
Approved positivity/instance removed, lambda normalized, sole Index rewrite adjusted.
Complete Index LSP passes. All target gates pass; [audit](Box-weight_mul_left.md).

Publication verification: full `lake build` session 84040 exited 0 (2586 jobs;
`/private/tmp/roth-box-d12-full.log`); separate `lake build Roth.LeanEval` session 7710
exited 0 (2585 jobs; `/private/tmp/roth-box-d12-leaneval.log`). All affected dependents pass.

Declaration 13: `Roth.weight_le_degree_div`, 5 → 5 declaration lines plus scoped omission,
94 fewer codepoints. Unused instance removed, signature packed, gcongr proof simplified.
All target gates pass; [audit](Box-weight_le_degree_div.md).

Publication verification: full `lake build` session 46898 exited 0 (2586 jobs;
`/private/tmp/roth-box-d13-full.log`); separate `lake build Roth.LeanEval` session 24692
exited 0 (2585 jobs; `/private/tmp/roth-box-d13-leaneval.log`). All affected dependents pass.

Declaration 14: `Roth.weight_mapDomain`, 6 → 4 declaration lines plus scoped omission.
Both unused instances removed; generic Mathlib sum theorem replaces manual reindexing.
All target gates pass; [audit](Box-weight_mapDomain.md). Only header warning remains.

Publication verification: full `lake build` session 56521 exited 0 (2586 jobs;
`/private/tmp/roth-box-d14-full.log`); separate `lake build Roth.LeanEval` session 76596
exited 0 (2585 jobs; `/private/tmp/roth-box-d14-leaneval.log`). All affected dependents pass.
