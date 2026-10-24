# LeanEval independent whole-file final review

Status: **PASS, file-local; owner acceptance/publication pending.** Fresh independent reviewer
after all three original declarations and the necessary private helper were accepted. This
does not certify root `Roth.lean`, the five project-wide renames, or final project completion.
No Git, central progress, aggregate report, or other source file was changed by this reviewer.

## Scope, reads, and baseline

Read both installed mathlib-quality/Lean4 skills, the FULL installed cleanup/cleanup-all
commands and Phase4 worker instructions, and the complete golfing-rules, proof-patterns,
mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions,
profiling, pr-feedback-examples, quality-principles and deep-golfer references. In particular,
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Read the complete current source, all five
LeanEval preparation/declaration reports, and bounded central Current status. More specific
current rules and user scope take precedence over older contradictory reference examples.

Entry source:63 lines/3344 bytes,
SHA256 `4c77924b46d4b6559c8fc6118710e89c92fe07b0a49eaff90011e76edb2429d0`.
Saved before changes as `/private/tmp/roth-eval-final/entry.lean`.

Phase0 doctor is **qualified reuse**, not a new build invocation: accepted latest ordered
`/Users/ramin/.elan/bin/lake build` exit0/5.474s, THEN separate
`lake build Roth.LeanEval` exit0/27.406s, THEN native full Eval exit0/28.373s and complete
unfiltered clean LSP. Actual launch/terminal/stream evidence lives under
`/private/tmp/roth-eval-thue/final-{build,eval-build,native}-*.json`. Those actual tool calls
were reviewed and accepted by the owner in `thue-owner-accepted-v1.json`. Optional cache and
standalone linter executable skipped; native/LSP includes available Lean linters. All prior44
frozen inputs remain byte-exact except the precisely invertible Eval documentation change.
Root's default build excludes Eval, so the separate Eval build is explicitly retained as a
required qualified gate, never inferred from the full build. No executable edit here requires
replaying those broad checks. Fresh final-source canonical compilation/LSP and fresh actual
metadata provide the additional final binding below.

## Audit and concrete file-level correction

| Audit | Independent finding/action |
|---|---|
| A.1 copyright | Missing identity metadata left unchanged under user preservation instruction; no guess. |
| A.2 module doc | Existing citation prose lacked a module heading. Inserted concise `# LeanEval Thue–Siegel–Roth theorem`; preserved the full original prose/citation byte-content. |
| A.3 imports | Sole `Roth.Main` is needed for `Roth.roth` and its approximation API. No additional or removable import. |
| A.4 sections | No section headers/contentless sections; no optional sections added. |
| A.5 length | Final66 lines, maximum99 codepoints; no file split. |
| A.6 options | No resource/debug options, disabled linters, or profiling scaffolding. |
| A.7 mechanical | No deprecated lambda/dollar/push_neg, trailing whitespace, haveI/letI, TODO/FIXME or admissions. |
| B diagnostics | Fresh complete unfiltered final-source LSP: success=true, partial=false, timed_out=false, items=[], failed_dependencies=[]. |
| C declarations | Four written declarations, three original public contracts plus one independently audited private helper; all documented/visible appropriately. |

Exact inverse of the single heading insertion recovers the entire entry file byte-for-byte;
all executable bytes, declaration docstrings, binders, imports and original prose remain
unchanged. Final66 lines/3385 bytes,
SHA256 `70a3808e57b5251e725dfe6a93fbb064a2fb1f88b0c5d68659be924447417b65`.
Evidence: `/private/tmp/roth-eval-final/source-binding.json`. No original narrative proof
comments existed; zero deleted or relocated. The original LeanEval source link and headline
Roth1955 attribution remain exact. No mathematical/public-name rename or copyright edit.

## Per-declaration acceptance and substantive holistic review

| Written declaration | Accepted proof/body | Independent final finding | Dedicated prior audit |
|---|---:|---|---|
| `IsDiophantine` | 2-line Prop body | Meaningful external predicate, not a junk wrapper. Its defining conjunction belongs to the existential constant. | [Original1](LeanEval-IsDiophantine.md) |
| `exists_pos_div_rpow_lt_aux` | 17 tactic lines | Coherent substantive finite-exception bound, private `_aux`, no docstring; membership branches2/2. | [Helper](LeanEval-exists_pos_div_rpow_lt_aux.md) |
| `isDiophantine_iff` | 32→13 tactic lines | Public adapter, forward9/reverse3; finite bound already factored at the mathematical boundary. | [Original2](LeanEval-isDiophantine_iff.md) |
| `thueSiegelRoth` | 2 term lines | Direct algebraicity transport and accepted iff compose into one term. Exact external name/binders preserved. | [Original3](LeanEval-thueSiegelRoth.md) |

Each prior audit has its own full24-item/42-rule, search/generalisation, semantic, build and
performance evidence and all required checklist rows accepted. These were separate dedicated
workers, not a batched replacement. This final review does not claim those experiments were
repeated. No defect justifies reopening accepted expensive probes or introducing more API.

Fresh mathematical review: for arbitrary real κ, the helper minimizes the positive scaled
error on the finite exceptional set enlarged by `(0,1)`. Irrationality makes each error
nonzero; the selected denominator is positive, hence its real power is positive even when
κ≤0. Half this minimum and1/2 give one positive C; outside the exceptional set the scaled
error is at least1. The lift from positive integer q to natural q preserves the actual
integer/real casts. No zero/negative-denominator case is silently used. In the forward iff
direction, κ>2 admits the intermediate exponent `2 + (κ-2)/2`, and an infinite approximation
set has a denominator beyond the finite bounded-denominator portion. Scaling the eventual
inequality by positive C contradicts its lower bound. The reverse direction applies the
helper to the finite set at `2+ε`. The headline transports ℤ-algebraicity to ℚ using the
injective scalar map and applies `Roth.roth`. No vacuity, weakened result or new axiom.

Reuse/efficiency review: the only shared substantial skeleton is already the extracted
finite-exception argument. No duplicated proof warrants another helper. All four `have`s
were inspected: helper `haq` supplies implicit positivity input; `hfa` supplies witness
positivity and half-bound; `hq'` is used twice in division comparisons; iff `hgap` contains
substantive scaling/simplification proof. No single-use trivial have to inline. Terminal
simpa calls stay unsqueezed; no nonterminal bare simp, unnecessary show/change, repeated
rewrites, redundant term wrapper, or new automation attribute. Prior exact?/apply?/automation
failures remain valid for unchanged proofs. Cross-type casts establish genuine ℤ/ℕ/ℝ
bridges; annotations constrain real powers/comparisons. No new identifier in executable code.

Generalisation review: x is already arbitrary real; κ in the helper is arbitrary real with
no positivity hypothesis. Concrete→abstract fields change the fixed real-rpow/benchmark
objects rather than mechanically weaken a typeclass. Finite approxSet can mathematically
force irrationality, but proving that adds an unrelated rational-multiple argument; retain
the intentionally accepted hx. Removing hx from the public iff likewise adds rational-case
mathematics and changes its accepted application contract. Both headline hypotheses are
used despite their underscore names. No unused section instance, decidability/universe
restriction, global regularity hypothesis or strict→weak candidate applies. No concrete
object is unfolded once and then forgotten; no inversion/generalisation API expansion is
recommended. Prior five-method/literature evidence supports the same formulation; no new
absence claim or new external-paper review is asserted here.

## Packing, structure and orientation

Every signature line was freshly measured (codepoints, not bytes). Full width100 check
references remain in the dedicated audits; fresh `Enumerate.lean` also prints the iff at
`format.width=100`. Break arithmetic uses complete binders/conclusions as semantic units.

| Declaration/signature line | Width | Next unit / arithmetic | Action |
|---|---:|---|---|
| predicate16 | 35 | none; term body next | ok |
| helper20 | 70 | hs binder34;70+1+34=105 | ok |
| helper21 | 40 | full existential conclusion79;40+1+79=120 | ok |
| helper22 | 83 | none | ok |
| iff42 | 55 | full Iff conclusion72;55+1+72=128 | ok |
| iff43 | 76 | none | ok |
| headline61 | 83 | conclusion18;83+1+18=102 | ok |
| headline62 | 22 | none | ok |

| Inequality scan | Occurrences / action |
|---|---|
| predicate | Four `<` in definition body; no reversed signature inequality. |
| helper | C positivity, q positivity and approximation bound all `<`; no ≥/>. |
| iff | κ≤2 in signature; internal typed comparisons all smaller-left. |
| headline | No signature/body inequality. |

`<;>` is tactic syntax. Imported `not_gt`/`lt_of_not_ge` names are existing APIs. Main result2
lines≤15, ordinary iff13/helper17≤30, branches≤10. The helper's existential positivity
conjunction expresses one witness; artificially splitting it would duplicate construction.
Phase5a non-rename refactoring: none further needed. Phase5b: no Eval rename queued; five
existing global renames are coordinator-owned. Externally required `thueSiegelRoth` remains
an explicit user-authorized naming exception; public binder names are unchanged.

## Current families, preservation and proof evidence

Fresh actual metadata compile `lake env lean /private/tmp/roth-eval-final/Enumerate.lean`
exited0/27.868s. It printed actual families BEFORE comparisons, then saved full raw TYPE,
universe representations, actual opaque `value! true` VALUE hash/length and dependencies.
No raw VALUE dump. The imported olean is the accepted entry executable source; the sole
doc insertion is explicitly qualified by exact inverse, while fresh canonical profiling
and LSP check the actual final source. No claim of newly refreshed documentation in that
olean or fresh costly VALUE inference is made.

| Actual family (public prefix `LeanEval.NumberTheory.ThueSiegelRothProblem.`) | Universes | TYPE bytes | VALUE bytes |
|---|---|---:|---:|
| `IsDiophantine` | [] |108|5901|
| `IsDiophantine._proof_1` | [] |950|644|
| `isDiophantine_iff` | [] |2087|2585150|
| `isDiophantine_iff._simp_1_1` | [u_1] |2777|3006|
| `thueSiegelRoth` | [] |823|9234|
| `_private.Roth.LeanEval.0.LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux` | [] |4943|418547|

All6 full raw TYPE/universes match accepted metadata exactly; the old5 original families
retain their exact contracts. Five nonheadline complete metadata rows match the accepted iff
inventory, and headline VALUE9234/hash6990197182669633896/dependencies match its latest
accepted guard. These hashes/lengths are **not fullraw VALUE identity claims**. Prior strict
recursive Expr comparisons (Names/BinderInfo/Levels/metadata included), per-costly-check
default200000/20000/512 opaque inference, closure/no-sorry and standard-axiom checks are
reused with unchanged source/TYPE/hashlen/dependency bindings. No ExprBEq/defeq-only contract
substitute, broad normalization, raised limit or guessed universe is used.

Fresh actual same-file DAG is acyclic: predicate→its proof; iff→predicate/proof/private
helper; headline→predicate/iff; helper/generated simplifier have no Eval dependencies.
Accepted upstream-origin/no-self checks and independent finite-induction helper proof,
accepted-entry iff recovery, and helper-plus-Roth headline recovery remain valid unchanged
evidence. Lower accepted helper dependencies are allowed; target/generated/caller/circular
routes are excluded as specified in those audits. Evidence: `current-inventory.json` and
`metadata-binding.json`. No unrelated Main proof was reopened.

## Fresh canonical whole-file performance

Outcome **FAST-BOARD**. Actual command from project root:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/LeanEval.lean`.
This compiles the canonical WHOLE final file, not a prefix. Exit0/28.760s; stdout10198226B
and stderr556B retained separately. Import11.5s and cumulative profiler category totals are
not declaration costs. All4 written rows/all6 actual kernel families are covered.

| Written row | Outer command | Async proof | Kernel parents | Compiler | Lint parent | Detached Meta.whnf conservative charge | Complete total ms |
|---|---:|---:|---:|---:|---:|---:|---:|
| predicate |50.106|0|0.651|0.966|17.277|0.029|**69.029**|
| helper |10.649|222.811|8.113|0|17.250|0.969|**259.792**|
| iff |3.477|274.536|9.159|0|8.988|0.937|**297.097**|
| headline |5.880|33.258|6.965|0|2.487|0.382|**48.972**|

Complete full canonical docstring/signature/proof payloads match source after stripping
whitespace only. For helper, both full source-lemma wrapper and full expanded-theorem
payload match under the sole `lemma`→`theorem` token substitution. The pinned actual
`Mathlib/Tactic/Lemma.lean` implementation modifies that atom and corresponding syntax
kinds while preserving the full remaining AST; implementation path/hash/length bound in
`timing.json`. Expanded theorem trace appears before its enclosing source-wrapper trace;
its10.381ms is nested and excluded from addition. The disjoint wrapper carries that cost.
No nested header/value/addDecl/Kernel/Compiler/linter-child double counting. All actual
Kernel child names are enumerated and charged via their parents, including both generated
families. All declaration-range depth0 roots are accounted for. There are zero actual DATA
tokens/lazy Kernel DATA roots. Detached Meta.whnf roots are separately and conservatively
charged as Meta work, never mislabeled DATA. Scope ends at the NEXT command exclusively;
namespace/end/linter commands outside declarations are excluded.

All rows<750ms and<1000ms; no same-freeze repeat or unchanged third sample warranted/run.
No new performance fix, optional probe, noise waiver or cross-runtime speedup ratio. Prior
failed helper implicit-minimizer samples2265/2289/2314ms, historical iff2571ms and genuine
old-headline-context exit1 remain preserved in their respective audits; none is erased or
promoted into a valid controlled baseline. This is a fresh final all-row board.

Owner explicit PROFILE HOLDACK preceded ALL new driver/env/freeze preparation. Owner idle
through actual task/driver drain.41 frozen inputs and full parent/lake-env byte strings
compare equal before/after; only safe hash/length/PATH/toolchain persisted. Task PID/PGID
48043 and driver PID/PGID48021 actually absent; terminal RAW UNPARSED sent before explicit
owner RELEASE, parsing only afterward. `profile-{launch,terminal,drain}.json` bind the
streams and actual lifecycle. Initial os.setsid attempt failed before env/freeze/compiler
launch, exit1; driver then retained/recorded its actual existing PGID. Retained narrow
prelaunch-failure.txt. First post-release parser uniqueness assertion matched doc references;
keyword-qualified matching fixed that assertion with no compiler/capture replay; retained
parser-erratum.txt. Neither failure is presented as a Lean/profile failure or a pass.

## Final cumulative gates, simplify and disposition

| Gate | Result/evidence |
|---|---|
| lake_build | Qualified reuse of actual accepted latest full build exit0/5.474s; exact prior input binding except doc-only inverse. |
| lake_build_file | Qualified reuse of actual subsequent separate Eval build exit0/27.406s; root build alone does not cover Eval. |
| native full Eval | Qualified reuse of actual exit0/28.373s, empty streams; PLUS new canonical final whole-file profile compile exit0. |
| complete final diagnostics | Fresh unfiltered LSP clean, nonpartial, no timeout/dependency failure; diagnostics.json. |
| actual family/TYPE/proof binding | Fresh actual6 metadata/raw TYPE/universes/hashlen/deps match; costly prior proof checks reused explicitly. |
| definition_protected | Exact original predicate/executable bytes and accepted current definition contract. |
| theorem_statement_protected | All public binders/names/order/types unchanged; all6 raw TYPE/universes exact. |
| structure/naming/packing/orientation | Full fresh tables/reasoning above; no deferred flag or hidden long branch. |
| cumulative callers/imports | Fresh repository search finds only same-file users, no external Eval importer/headline caller. Main/root sources and all prior dependency/artifact/runtime bindings exact. |
| comments/docs/paper references | All declaration docstrings and original citation prose byte-content preserved; zero narrative comments deleted. |
| static/diff | Width99; no admissions/newaxioms/limits/scaffolding; `git diff --check -- Roth/LeanEval.lean` exit0. |
| whole-file performance | All4 rows/all6 compiled families<750ms/<1000ms, canonical source-bound; no repeat needed. |

Claude's built-in `Skill(simplify)` is **unavailable** in this environment; it was **not
invoked**. This NEW fresh substantive independent holistic review is the authorized
substitute: reuse, mathematics, generalisation, assumptions, dependencies, proof structure,
efficiency, docs/imports/comments and final compiled behavior reviewed across the complete
file. Outcome **ISSUES-FOUND-AND-FIXED**: only missing module heading fixed. No proof/API
change, unresolved suggestion, deferral, new rename or optional expansion. Mathlib buzz
Skill invocation is likewise not claimed; its actual held whole-file profiling workflow
and required timing artifact are supplied directly above.

Phase checklist: P0 qualified doctor ✓; P1 full preparation ✓; P2 full audit ✓; P3 heading
fix ✓; P4 all4 dedicated accepted reports reviewed ✓; P5a none further ✓; P5b global queue
explicitly coordinator-owned ✓; P6 qualified cumulative gates plus fresh final binding ✓;
P6.5 unavailable Skill honestly labeled/independent substantive substitute ✓; P6.6 actual
canonical whole-file all-row profile ✓; P7 this consolidated report ✓.

Total file delta: preparation60→final66 (+6); this final review63→66 (+3 doc lines/+41bytes).
Original iff32→13 proof lines is offset by the separately audited17-line helper, so no false
whole-file reduction claim. Final source/report frozen before FINAL-END; all reviewer tool
calls returned, task/driver groups drained, no pending compiler/native/LSP/profile work.
Final small `/private/tmp/roth-eval-final/FINAL-END.json` records actual final drain/bindings.
All source/report/compiler/native/LSP/profile leases released to the owner at handoff.
File completion is counted only after owner acceptance and actual publication; no project
completion claim follows from263/263 originals or this local pass.
