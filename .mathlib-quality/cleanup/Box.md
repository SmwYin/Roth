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

Completed 1/14 dedicated declaration workers. Each completed declaration is fully validated,
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
