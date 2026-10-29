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

For isolated mathlib-only probes, prefer the native `lean_run_code` serial virtual
scratch pool with a stable minimal import prefix. The installed connector conservatively
marks other disk documents stale after disk edits; its virtual pool avoids that cross-file
invalidation. Keep target checks in one disk document and isolated probes in the virtual
pool. Never add a Roth import to an isolated probe; expected name-resolution failure is a
useful control, not a mathematical absence proof. Warmup may still be needed after restart.
The actual controls in evidence/shared/virtual-session-{prime,repeat}.json passed:
first load 55,478 ms, same-prefix additional inspection 995 ms. These are session controls,
not a promised duration for arbitrary proofs. Save each executed code string and raw
complete native response as that declaration's evidence.

Current structural inventory has 293 written declarations (215 public, 78 private),
28 definitions,191 theorems,74 lemmas across14 production files. Source signatures and direct
references were manually reviewed; an independent parser review repaired named-assignment/
statement-let delimiter errors. The broader structural drafts stay scratch-only until
associated declaration assessments are complete, respecting completed-only publication.
The initial fresh Lean.Meta metadata extraction timed out; that historical limitation is
retained in the earlier evidence. Later successful native audits enumerated the exact293
canonical declarations with correct private modules, and extracted direct references from
both types and opaque theorem values. The final evidence preserves the raw receipt and exact
executed source alongside the canonical graph. This is a direct expression audit; it does not
expand the full auxiliary/simp/generated/transitive dependency closure or establish external
deadness. Per-declaration generated-proof investigations retain their own narrower scopes.

Final inventory signatures reproduce complete native binder types. Fourteen older kind-only
inventory fields were repaired from separately verified native type/binder receipts; original
accepted packages remain immutable. The final aggregate records the repair and dependency-
metadata normalization provenance separately from those historical packages.

The default Roth library root does not import Roth.LeanEval. Final build evidence must include
both `lake build` and `lake build Roth.LeanEval`, with actual exit statuses and log hashes;
one command alone does not establish full source coverage.

Final supporting evidence: [native dependency graph](evidence/final/final-kernel-graph.json), [canonical direct dependencies](evidence/final/final-canonical-direct-dependencies.json), [native binder repairs](evidence/final/final-inventory-type-repair-plan.json), [historical metadata resolutions](evidence/final/final-project-dependency-reviewed-resolutions.json), [full pairwise comparison index](evidence/final/pairwise/README.md), [both actual final builds](evidence/final/final-build-verification.json), and [copied evidence manifest](evidence/final/copy-manifest.json).

Before publishing evidence, run `python3 .mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py <incoming-package-directory>`. Returned signed or credential-bearing URLs must have their query removed and the redaction documented. [Correction record](evidence/shared/web-evidence-redaction-2026-10-26.md).

## Canonical audit integrity

All full-repository native caller audits must build the exact names array from
`declaration-order.json`, preserve private-name construction, and check both
293 entries and 293 unique names. Count alone is insufficient. Declarations 82
and 83 had an enumerator substitution defect; fresh corrected audits match the
exact order and find unchanged callers. Their reports and `audit-correction.json`
records retain the history and supersede the earlier coverage claims.
The shared `validate_canonical_audit.py` checks corrected evidence independently.
