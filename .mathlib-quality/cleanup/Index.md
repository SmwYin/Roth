# Index cleanup — file owner record

Baseline: `e557886`, `ramin-cleanup`, 2026-10-16. Original snapshot:
`/private/tmp/roth-index-original.lean`. Scope: `Roth/Index.lean`, 275 lines,
21 original declarations (one public definition, 17 public theorems, three private lemmas).
Public mathematics, definition values, documentation and pinned versions are protected.
No other file's earlier API approval authorizes an Index API change.

## Phase 0 — Doctor

- Optional cache fetch skipped: dependencies already installed and built.
- Actual `/Users/ramin/.elan/bin/lake build`, session28852, exited0;
  `/private/tmp/roth-index-baseline-build.log` ends in successful2465-job build.
- Complete native `lean_diagnostic_messages` returned success=true, partial=false,
  timed_out=false, zero errors. Header metadata, unused decidability binders,
  and unused `index_le_card.hr` warnings feed the audit below.
- Standalone runLinter executable absent; configured project style/unused linters
  run during module elaboration.

## Phase 1 — Preparation and original inventory

Dialect: classic (no leading module/public-import commands). Full source read.
Dedicated fresh workers process one declaration at a time; added private helpers
receive separate fresh audits and never increment the original-declaration tally.

| # | Original declaration | Start | Declaration lines |
|---|---|---|---|
| 1 | index | 50 | 2 |
| 2 | mem_support_taylor_iff | 54 | 3 |
| 3 | weightSet_finite | 59 | 3 |
| 4 | weightSet_nonempty | 64 | 4 |
| 5 | index_le_weight | 72 | 5 |
| 6 | exists_weight_eq_index | 79 | 5 |
| 7 | le_index_iff | 86 | 7 |
| 8 | index_nonneg | 94 | 4 |
| 9 | index_eq_zero_iff | 101 | 9 |
| 10 | index_hasseDeriv_ge | 112 | 8 |
| 11 | le_index_sum | 122 | 10 |
| 12 | weight_eq_finsuppWeight_div | 134 | 11 |
| 13 | index_eq_weightedOrder_div | 149 | 21 |
| 14 | index_mul | 173 | 13 |
| 15 | index_prod | 190 | 13 |
| 16 | index_neg | 205 | 3 |
| 17 | index_C_mul | 210 | 3 |
| 18 | index_mul_left_weights | 215 | 9 |
| 19 | index_rename | 227 | 7 |
| 20 | index_le_card | 238 | 7 |
| 21 | index_unique | 248 | 26 |

## Phase 2 — Audit punch-list (before fixes)

| Tag | Finding and concrete action |
|---|---|
| A.1 copyright | Missing; user explicitly requires preserving unconfirmed metadata. Leave unchanged and disclose inherited warning. |
| A.2 module docstring | Present after imports; preserve all existing documentation. |
| A.3 imports | Alphabetical within Mathlib/project groups; missing group separator. Add blank separator after source ownership is released. Audit redundancy in independent simplify review. |
| A.4 headings | No contentless section headings. Preserve module headings. |
| A.5 length | 275 lines, no split required. |
| A.6 options | No heartbeat/recursion/debug options. |
| A.7 mechanical | No lambda glyph, dollar operator, or push_neg. Mathematical `fun … =>` arrows need per-declaration normalization. |
| B.1 metadata | Complete native LSP reports inherited header warning; user-preserved. |
| B.2 decidability | Public theorem `[DecidableEq σ]` warnings and rename theorem `[DecidableEq τ]` warning. Compile concrete isolated removal proposal; obtain scoped user decision before applying. |
| B.3 positivity | `index_le_card.hr` unused. Compile stronger result and exact two Theta caller repairs; obtain user decision before applying. |
| C.1 naming | Descriptive index API names; private weightSet lemmas have camel component in theorem names and derivative theorem `_ge` suffix warrants rename queue consideration. Central project-end rename pass only. |
| C.2 visibility | Three existing private helpers have no docs; public API retained unless concrete approved removal. |
| C.3 docs | All18 public declarations documented; preserve existing docstrings. |
| C.4 structure | Headline weighted-order bridge and unique-variable identity exceed15body lines; workers must simplify/extract substantive private helpers or give explicit supported decomposition flag. |
| C.5 junk | index names the mathematical index and has17 public API results and downstream users; retain. No trivial private existential helper. |

## Phase 3 — File-level work

Metadata remains unchanged by user instruction. No limit options or deprecated
mechanical syntax require removal. After explicitly revoking the first worker's
source-edit authority, owner inserted the missing import-group blank separator.
All remaining declaration-level findings go to dedicated fresh workers.

## Ongoing work

Phase4 active. No final-file gates or completion claimed by this preparation record.

### Declaration1 — index

[Fresh dedicated audit](Index-index.md): definition retained unchanged, 2→2 lines.
All24 audit items,42 rule slots, five actual searches, every-binder mechanical tests,
public literature, signature/inequality tables and11 checked steps are present.
Target original type/value independently reconstructed and checked; actual target
standard axioms verified. Optional generic-coefficient observation is report-only,
not a required cleanup change. Earlier aggregate profiler observation is preliminary;
the file owner's final actual per-declaration sweep will supersede it.

Owner added only the import separator. Current frozen SHA256:
`9ea21436746c9e155e485b0ae6ef6deb884e4391417044407c717cb2f6206f64`.
Actual owner `lake build Roth.Index`80771 exits0; complete native LSP success=true,
partial=false, zero errors,27 inherited warnings. Public unused-argument warnings
are covered by [compiled proposal](Index-api-proposal.md), awaiting scoped decision;
metadata warning is explicitly user-preserved. No linter suppression added.

Sequential owner full `lake build` followed by separate `lake build Roth.LeanEval`,
session24111, both exit0 (170.57s/39.02s), frozen hash stable throughout.
Logs `/private/tmp/roth-index-d01-{full,leaneval}.log`; command/exit/hash evidence
`/private/tmp/roth-index-d01-builds.json`. No public declaration or mathematical
definition changed; all block docs preserved. Exact-path publication follows before
the next declaration's source edit. Original tally131/264; Index1/21, file incomplete.
