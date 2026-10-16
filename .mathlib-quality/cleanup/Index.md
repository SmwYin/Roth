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
| 5 | index_le_weight | 72 | 4 |
| 6 | exists_weight_eq_index | 79 | 4 |
| 7 | le_index_iff | 86 | 6 |
| 8 | index_nonneg | 94 | 4 |
| 9 | index_eq_zero_iff | 101 | 8 |
| 10 | index_hasseDeriv_ge | 112 | 7 |
| 11 | le_index_sum | 122 | 8 |
| 12 | weight_eq_finsuppWeight_div | 134 | 10 |
| 13 | index_eq_weightedOrder_div | 149 | 21 |
| 14 | index_mul | 173 | 13 |
| 15 | index_prod | 190 | 13 |
| 16 | index_neg | 205 | 3 |
| 17 | index_C_mul | 210 | 3 |
| 18 | index_mul_left_weights | 215 | 8 |
| 19 | index_rename | 227 | 7 |
| 20 | index_le_card | 238 | 6 |
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

Original-declaration light scan (all widths/proof measurements are subsequently
checked by the dedicated worker; names here identify the original API). The three
private lemmas have no docstrings; all18 public declarations have docstrings.
All public visibility decisions preserve the established API pending a concrete
approved change. No private single-use trivial existential wrapper was found.

| Declaration | Naming | Visibility/docs | Length/structure and junk scan |
|---|---|---|---|
| index | lowerCamelCase data, descriptive | public/doc present | 1term line; nontrivial mathematical concept and extensive API, retain |
| mem_support_taylor_iff | snake_case, describes iff | private/no doc | 1proof line, repeated support API, not existential |
| weightSet_finite | mixed camel prefix needs dedicated naming check | private/no doc | 1term line; repeated finite-set support infrastructure |
| weightSet_nonempty | mixed camel prefix needs dedicated naming check | private/no doc | 2proof lines; repeated nonempty-set infrastructure |
| index_le_weight | descriptive snake_case | public/doc present | 2term lines; no long branch |
| exists_weight_eq_index | descriptive snake_case | public/doc present | 2proof lines; existential witness pairs nonvanishing/equality, no top-level conjunction to split |
| le_index_iff | descriptive snake_case | public/doc present | 4proof lines; headline below15 |
| index_nonneg | descriptive snake_case | public/doc present | 3proof lines |
| index_eq_zero_iff | descriptive snake_case | public/doc present | 6proof lines; short iff branches |
| index_hasseDeriv_ge | final_ge suffix needs orientation rename consideration | public/doc present | 5proof lines; headline below15 |
| le_index_sum | descriptive snake_case | public/doc present | 5proof lines; headline below15 |
| weight_eq_finsuppWeight_div | camel component refers to Finsupp weight API | public/doc present | 8proof lines; audit casts and hD usage |
| index_eq_weightedOrder_div | camel component names weightedOrder | public/doc present | 14proof lines; headline bound and largest branch need precise worker count |
| index_mul | descriptive snake_case | public/doc present | 11proof lines; headline below15 |
| index_prod | descriptive snake_case | public/doc present | 10proof lines; induction branches below10 |
| index_neg | descriptive snake_case | public/doc present | 1proof line |
| index_C_mul | C refers to polynomial constant map | public/doc present | 1proof line |
| index_mul_left_weights | descriptive snake_case | public/doc present | 6proof lines; local image-equality proof |
| index_rename | descriptive snake_case | public/doc present | 4proof lines; headline below15 |
| index_le_card | descriptive snake_case | public/doc present | 4proof lines; positivity candidate in B.3 |
| index_unique | descriptive snake_case | public/doc present | 23proof lines; headline needs substantive simplification/extraction |

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

### Declaration2 — mem_support_taylor_iff

[Fresh dedicated audit](Index-mem_support_taylor_iff.md): private support/Taylor iff
retained unchanged,3→3 lines. All24audit/42rules/five actual searches/every binder
probe/signature+inequality tables/11checked steps inspected. No helper/rename/required
refactor. Generic coefficient observation remains optional/report-only. Actual module
47848 exit0; complete native LSP success=true,partial=false, zero target diagnostics;
independent original-type nonself proof and actual imported private constant axiom
checks pass. Isolated166heartbeats preliminary; actual anchored file profiling remains
for final buzz. All leaf processes complete, source/report editing released.

Frozen source unchanged9ea214…; owner sequential full then separate LeanEval64010,
both exit0(5.12s/3.05s), `/private/tmp/roth-index-d02-{full,leaneval}.log`, frozen hash
stable. Exact-path publication precedes next edit. Index2/21; overall132/264 originals.

### Declaration3 — weightSet_finite

[Fresh dedicated audit](Index-weightSet_finite.md): generic finite-image wrapper
selected for deletion; all24audit/42rules/five actual searches/all binder probes/
packing+inequality tables/11checks inspected. Worker independently compiled original
private type/proof, actual private standard axioms and both concrete caller repairs;
module63141/complete pre-deletion diagnostics pass. Worker explicitly released source,
then owner removed private declaration+omit command and specialized Mathlib's existing
finite-image API directly at both callers. Public types/docs/definition unchanged.

Source276→272 lines,20 retained declarations. Frozen SHA256
`6897edb8955031680fa67e41007292a74287c1f0737f9dbcd5b44ca42e471ef7`.
Actual owner module45739 exit0, complete native LSP zero errors27 inherited warnings;
fresh whole ORIGINAL independent reproof/all18 public type+value equalities/all20
actual retained standard-axiom checks90385 exit0. All block docs identical, widths≤100,
no new external identifier beyond existing finite-image API, diff check clean.
Sequential owner full then separate LeanEval7465 both exit0(143.50s/32.05s), hash stable;
logs `/private/tmp/roth-index-d03-{full,leaneval}.log`. No helper or rename added.
Index3/21 originals audited, overall133/264; exact-path publication before next edit.

Scoped user approval arrived via root/parent2026-10-16 for API groups1+2 only.
Approved removals will occur at each corresponding fresh public-declaration audit;
none is applied in this private-wrapper checkpoint. Group3 scaling positivity remains
unapproved/unapplied. See [current proposal/decision record](Index-api-proposal.md).

### Declaration4 — weightSet_nonempty

[Fresh dedicated audit](Index-weightSet_nonempty.md): original4lines→3 via terminal
simpa, then owner accepted its compiled Phase5a wrapper-deletion proposal and removed
the helper/omit command. Both callers now directly simplify nonemptiness from hP;
attained-minimum receiver has a load-bearing term-mode type annotation. All24audit/
42rules/five actual searches/every binder probe/width+inequality tables/11steps inspected.
Worker module99920, complete LSP, independent exact original-type proof and actual
private standard axioms18097 passed; all worker processes complete before handoff.
Owner explicitly revoked source authority before applying caller edits/deletion.

Source272→267lines,19 retained declarations. Frozen SHA256
`531003ff42de90398daad179eb7b7006cc520efea475de29274078cad567bf9a`.
Owner module2756 exit0; complete native LSP zero errors27 inherited warnings;
fresh whole ORIGINAL nonself reproof/all18 original public type+value equalities/
all19 actual standard-axiom checks58412 exit0. Docs byte-identical, widths≤100,
diff clean. Sequential full then separate LeanEval47084 both exit0(137.39s/33.18s),
Index+Theta hashes stable; logs `/private/tmp/roth-index-d04-{full,leaneval}.log`.
No new helper/rename/public API change. Index4/21 originals, overall134/264.
Exact-path publication precedes first approved public-instance removal audit.

### Declaration5 — index_le_weight; first approved API omission

[Fresh dedicated audit](Index-index_le_weight.md): public4→4 declaration lines;
one scoped `omit [DecidableEq σ] in` added before the byte-identical docstring,
as expressly approved in groups1+2. No proof/conclusion/other argument change.
All24/42/five actual searches/public literature/every binder probe/packing+inequality
tables/11steps inspected. Actual worker module92257 exit0; complete native LSP
zero errors/zero target diagnostics/26 remaining outside warnings. Fresh54440
actual no-DecEq signature/standard axioms/nonself stronger proof/original-type
adapter pass. Stale native scratch and corrected scratch heartbeat failure disclosed.

Explicit source editing revoked; frozen SHA256
`2bf2b502f4e95caf1b28cdc247ccd4a26cc9f1c60c747d8e7c388cf9035234cb`.
Owner whole ORIGINAL independent reproof/all18 public type+value recoveries/all19
actual standard-axiom checks55805 exit0; actual new type also inspected by Expr.find?
and has no DecidableEq constant. Sequential full then separate LeanEval89783 both
exit0(144.71s/36.17s), Index+Theta hashes stable. Native Main caller cell118 complete,
zero errors/four existing warnings; JSON `/private/tmp/roth-index-d05-main-lsp.json`.
Docs identical, widths≤100, canonical first5reports each42rules/11checked steps.
No helper/rename. Source267→268 from omit command. Index5/21 originals, overall135/264;
publication precedes next edit. Group1 application1/17 σ-omissions; group2/card and
rename τ still future targets. Group3 hl unapproved, untouched.


### Checkpoint d06 — exists_weight_eq_index

Applied the explicitly approved unused σ-DecidableEq omission only; all proof, docs and mathematical binders retained.

[Dedicated audit](Index-exists_weight_eq_index.md) inspected:24 audit items,42rules,five actual searches,
binder probes,literature/exemption,complete packing+inequality tables,all11steps.
Frozen SHA256 `a872711cb58cfec0e2bb6b24ba400001fb4f3d3e6518276b3f6f47f46f25352b`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session35801 exit0, `/private/tmp/roth-index-d06-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval56008 both exit0(147.16s/34.47s),
Index+Theta hashes stable; `/private/tmp/roth-index-d06-{full,leaneval}.log`.
Worker complete Index LSP: success=true partial=false timed_out=false, 0target diagnostics/26unrelated warnings. External MainLemma complete native LSP functions cell146: success=true partial=false timed_out=false, 0errors/3inherited warnings, noinfos, no faileddependencies. MainLemma:522 caller accepted; raw /private/tmp/roth-index-d06-mainlemma-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Source269lines/19retained. Index6/21 originals,overall136/264;
no file-final completion claimed. Leaf source/Lean requests finished before owner gates.
