# Roth/LeanEval.lean cleanup

## Preparation and file audit

Entry: clean `ramin-cleanup`, `f83e3253b5c3aff98a6b308545035924c0a16c9d`; 60 lines, 3010 bytes, SHA256 `610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca`. This is a classic import file with three genuine original declarations: `IsDiophantine` (definition, lines 11–13), `isDiophantine_iff` (lines 16–49, 32 proof lines), and `thueSiegelRoth` (lines 54–58, three proof lines). The actual compiled entry inventory has five rows, including `IsDiophantine._proof_1` and `isDiophantine_iff._simp_1_1`; the latter has universe `u_1`. Generated families are inspected before guards.

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
