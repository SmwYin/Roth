# Native ownership from declaration270 onward

Root observed separate MCP/Lean process trees appearing with fresh reviewers and minute-long
first checks even for focused original replays. To reuse one compiler session, root is now the
exclusive executor of native Lean checks and local LSP search for270 onward. This overrides
all worker-exclusive native paragraphs for those future declarations only.269 keeps its current
exclusive ownership until completed freeze/release. All mathematical assessment gates remain.

Workers must not invoke lean_diagnostic_messages, lean_run_code, lean_local_search, hover/goal/
verify/build/profile or other project-LSP/native tools directly. Remote semantic tools
leanfinder, leansearch and loogle may still be called directly; plain file/rg searches are fine.
Read full source/callers and perform all skill phases as before. Prepare exact scratch source
archives under your own candidate directory, never change the persistent .lake document.

To request work, write candidate/root-requests/ID.json with:
{"id":"original01","operation":"diagnostics","source":"original-executed.lean.txt",
 "source_sha256":"ACTUAL_SHA","receipt":"original-receipt.json","original_audit":true,
 "arguments":{"file_path":".lake/roth-overview-session/GenWronskianChecks.lean","timeout_s":45}}

For mathlib-only snippets use operation run_code, source and hash, receipt, arguments:{}.
Root will insert the source as the exact code argument. Use stable18 imports by default;
ask root before a required extra import, exactly as before. For local search use operation
local_search, receipt and arguments:{query:...,project_root:"/Users/ramin/LEAN/Roth",limit:N};
no source is needed. Name the three local-search receipts consistently with the15-cell matrix.

Notify root of each prepared request (several independent local searches may be requested
in one message). Root validates the source/hash/frontier/pins/import controls, copies a disk
source only into the existing scratch document, invokes its persistent native tool, and saves
{request:ACTUAL_ARGUMENTS,result:ACTUAL_TOOL_RETURN,elapsed_ms:ACTUAL_TIME,executor:...}.
Root records partial/failed returns too. Read the complete raw receipt, diagnose/fix proofs,
and submit a NEW source/receipt/request ID for another execution. Never overwrite an earlier
executed source or raw response. A partial/warming result needs another request before PASS.
Report actual root-executed provenance; do not claim you directly ran a tool you did not run.

Root-owned native execution is verification, not mathematical acceptance. You still complete
all own reading, generic proofs/recovery/callers/search/literature/phases/report/currentmanifest/
portable validators/secretguard, then freeze and notify root. Root independently reviews,
integrates, commits and pushes as before. No worker subagents or production/Git changes.
Fullfile reading, focused exact-target original replay, complete actual caller verification,
exact293 audit,17 hashes, default limits, standard axioms and all build gates remain required.
