# Overview workflow and restart contract

Work only on ramin-cleanup; push normally to origin HEAD:ramin-cleanup. Never merge,
force-push, or push main. Production Lean sources and pinned versions must stay unchanged.
Use scratch files for experiments. The initial source snapshot is recorded in
evidence/shared/input-manifest.json.

On restart, read progress.json and progress.md FIRST, verify the branch and all source/pin
hashes, then resume next_declaration (the first unfinished item in declaration-order.json).
A report file existing in scratch, an inventory entry, or a guessed verdict is not completion.

For each applicable declaration, follow the full installed mathlib-quality overview/mathlibable
workflow. The command sources in this session are
/Users/ramin/.local/share/roth-mathlib-quality/commands/overview.md and mathlibable.md;
references are /Users/ramin/.codex/skills/mathlib-quality/references/.
Use import-order files and definitions before dependent lemmas. Apply only documented
private/local/glue/collision prefilters; match full qualified names, never bare-name collisions.
A permitted SKIP needs its own completed applicable inventory/triage report and evidence.
No incomplete declaration assessment belongs in Git.

Complete literature/search/generality/modern-idiom/risk/proof-strategy/statement-shape/
composition/verdict checks and all required compiler verification before publishing a
report. Keep exact queries, result symbols and URLs, scratch proof code, actual raw logs,
command/exit receipts and source identities. Never infer absence from an unavailable index,
and never allow a mathlib-only composition/absence probe to see the project target itself.
Optional ask_chatgpt_math is unavailable and may be recorded n/a; other checks remain required.

Only after the declaration's acceptance gate passes: copy its complete report and supporting
evidence into the tracked overview tree, update PROJECT_OVERVIEW.md and both progress
records, check source hashes and links, commit that completed assessment, and push it.
Record every completed declaration and the exact next declaration. Do not publish partial
assessment checkpoints. The source-name roadmap contains no verdicts for unfinished items.

Keep one persistent Lean language-server session warm for repeated source inspections.
Batch compatible scratch checks, import only needed modules, and allow only one heavy
compiler process at a time. Use direct CLI as fallback with real command/log receipts.
Reuse a successful baseline only when all source/pin hashes match. Re-downloading the
already present cache is not a remedy for session startup/loading overhead.

Current structural inventory has 293 written declarations (215 public, 78 private),
28 definitions,191 theorems,74 lemmas across14 production files. Source signatures and direct
references were manually reviewed; an independent parser review repaired named-assignment/
statement-let delimiter errors. The broader structural drafts stay scratch-only until
associated declaration assessments are complete, respecting completed-only publication.
Full fresh Lean.Meta metadata extraction timed out; no opaque dependency audit is claimed.
