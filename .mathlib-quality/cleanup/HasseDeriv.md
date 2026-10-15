# HasseDeriv cleanup audit

Status: 2 of 26 declarations audited and validated; second checkpoint ready for publication.
The file has **not** completed all cleanup phases.
Source: `Roth/HasseDeriv.lean`; dialect: classic imports (no `module`).

## Phase 0 — Baseline

- `lake exe cache get`: skipped; existing cached imports suffice.
- Full `lake build`: passed in orchestrator, exit 0, 2586 jobs; evidence `.mathlib-quality/cleanup-baseline.log`.
- Direct `lean-lsp-mcp` v0.31.0 `lean_diagnostic_messages` with `timeout_s=180`: success, complete, no failed dependencies, no errors.
- Diagnostic: line 1, column 2, header linter warning `Copyright too short!`.
- Standalone runLinter: optional, not invoked; standard mathlib linters enabled in lakefile and LSP diagnostics collected.

## Phase 1 — Context

Entire 329-line file read. Installed cleanup command and style, naming, golfing, and proof-pattern references read in full using bounded reads. Existing source citations and proof comments will be preserved. The file has 26 declarations. Definitions and theorem statement semantics remain protected; substantive API/generalization changes require approval.

Direct importers: `Roth`, `Roth.CoeffNorm`, `Roth.GenWronskian`, `Roth.Taylor`.
Transitive dependent modules also include `Roth.Index`, `Roth.LeanEval`, `Roth.Main`,
`Roth.MainLemma`, `Roth.Separation`, and `Roth.Theta`. The checkpoint build will run
`lake build` and the separately required `lake build Roth.LeanEval` to cover this closure.

## Phase 2 — Audit punch-list

### File-level items

- A.1 COPYRIGHT: absent. Deferred pending confirmed ownership/licensing; cleanup will not invent an author or license.
- A.2 MODULE DOCSTRING: present after imports with definitions, results, and source reference; preserve.
- A.3 IMPORTS: eight Mathlib imports, alphabetical; no new import needed. No speculative deletion.
- A.4 SECTION HEADERS: no contentless section header; module headings preserved.
- A.5 FILE LENGTH: 329 lines, below 1000; no split needed.
- A.6 FILE-LEVEL SET_OPTION: none.
- A.7 MECHANICAL: no λ, $, or push_neg; ordinary `fun … =>` occurrences will be fixed with their declaration checkpoints.

### Linter findings

- B.1 L1: `linter.style.header` reports `Copyright too short!`; disposition A.1. No other LSP warnings/errors.

### Per-declaration scan and inventory

Body line counts include a same-line term after `:=`; names using existing camelCase definition names within theorem names follow those subjects. Every public declaration has a docstring; private declarations have none. No proof exceeds 30 lines and no private single-use existential witness lemma occurs. Both definitions have substantive surrounding API and repeated uses (not junk definitions).

| Item | Declaration | Lines | Body lines | Audit |
|---|---|---|---|---|
| C.1 | `hasseCoeff` (def) | 44–44 | 1 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦ |
| C.2 | `hasseDeriv` (def) | 51–54 | 4 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦ |
| C.3 | `hasseDeriv_monomial` (theorem) | 60–62 | 2 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); deep audit pending |
| C.4 | `hasseDeriv_apply` (theorem) | 67–70 | 3 | naming: descriptive, no forbidden pattern; public docstring present (OK); public API; inspect reuse in worker; deep audit pending |
| C.5 | `hasseCoeff_eq_zero_iff` (theorem) | 75–77 | 3 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); inspect terminal simp only |
| C.6 | `coeff_hasseDeriv` (theorem) | 84–95 | 11 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); split tactic chains |
| C.7 | `hasseCoeff_eq_prod` (theorem) | 101–103 | 2 | naming: descriptive, no forbidden pattern; public docstring present (OK); public API; inspect reuse in worker; lambda arrows → ↦ |
| C.8 | `hasseDeriv_zero_apply` (theorem) | 108–110 | 3 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); deep audit pending |
| C.9 | `hasseDeriv_zero` (theorem) | 116–117 | 2 | naming: descriptive, no forbidden pattern; public docstring present (OK); public API; inspect reuse in worker; deep audit pending |
| C.10 | `hasseDeriv_C` (theorem) | 122–124 | 3 | naming: descriptive, no forbidden pattern; public docstring present (OK); public API; inspect reuse in worker; deep audit pending |
| C.11 | `hasseDeriv_map` (theorem) | 130–133 | 3 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); deep audit pending |
| C.12 | `hasseDeriv_rename` (theorem) | 139–149 | 9 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); scan single-use have |
| C.13 | `choose_mul_choose_eq` (lemma) | 151–156 | 5 | naming: descriptive, no forbidden pattern; private: no docstring (OK); private (OK); scan single-use have; test available arithmetic tactic alternatives; assess descriptive helper naming |
| C.14 | `hasseCoeff_mul_hasseCoeff` (lemma) | 158–171 | 12 | naming: descriptive, no forbidden pattern; private: no docstring (OK); private (OK); lambda arrows → ↦; inspect terminal simp only; scan single-use have; assess descriptive helper naming |
| C.15 | `hasseDeriv_hasseDeriv` (theorem) | 178–182 | 4 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); deep audit pending |
| C.16 | `hasseDeriv_hasseDeriv_of_disjoint` (theorem) | 188–192 | 4 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦; scan single-use have |
| C.17 | `hasseCoeff_mul_succ` (lemma) | 194–218 | 23 | naming: descriptive, no forbidden pattern; private: no docstring (OK); private (OK); lambda arrows → ↦; inspect terminal simp only; scan single-use have; assess descriptive helper naming |
| C.18 | `pderiv_hasseDeriv` (theorem) | 223–231 | 8 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); scan single-use have |
| C.19 | `degreeOf_hasseDeriv_le` (theorem) | 236–240 | 4 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦ |
| C.20 | `hasseDeriv_eq_zero_of_degreeOf_lt` (theorem) | 245–250 | 5 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦; scan single-use have |
| C.21 | `hasseDeriv_monomial_mul` (lemma) | 252–266 | 14 | naming: descriptive, no forbidden pattern; private: no docstring (OK); private (OK); lambda arrows → ↦; inspect terminal simp only; scan single-use have; assess descriptive helper naming |
| C.22 | `hasseDeriv_mul_of_degreeOf_eq_zero` (theorem) | 272–277 | 5 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦; scan single-use have |
| C.23 | `hasseDeriv_single_aeval_X` (theorem) | 283–292 | 8 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); inspect terminal simp only; scan single-use have |
| C.24 | `uniqueAlgEquiv_hasseDeriv` (theorem) | 298–304 | 6 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦; scan single-use have; split tactic chains |
| C.25 | `hasseCoeff_le_two_pow` (theorem) | 309–313 | 4 | naming: descriptive, no forbidden pattern; public docstring present (OK); public: downstream users (OK); lambda arrows → ↦ |
| C.26 | `factorial_smul_hasseDeriv_single` (theorem) | 319–327 | 8 | naming: descriptive, no forbidden pattern; public docstring present (OK); public API; inspect reuse in worker; deep audit pending |

## Phase 3 — File-level fixes

No file-level edits needed beyond A.1, deferred because ownership/licensing is unconfirmed. No contentless headers, import-order defects, override options, or batch replacements. Full-file LSP remains successful with the baseline header warning only.

## Phase 4 — Declaration checkpoints

1. `MvPolynomial.hasseCoeff`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseCoeff.md). Eta-reduced the inner lambda
   and used `↦`, with a compiled `rfl` equivalence check. Name, type, visibility,
   documentation, and mathematical value preserved. All audit/golf/checklist artifacts
   pass with the explicitly recorded unavailable LeanSearch service. Post-edit complete
   LSP diagnostics report no errors and only the existing header warning. Root's
   `lake build` (2586 jobs) and `lake build Roth.LeanEval` (2585 jobs) both exited 0;
   logs: `/private/tmp/roth-hasseCoeff-build.log`,
   `/private/tmp/roth-hasseCoeff-leaneval.log`; diagnostics:
   `/private/tmp/roth-hasseCoeff-diagnostics.json`.

   Optional substantial change deferred: allow arbitrary function `k : σ → ℕ`.
   A scratch probe compiled, but this would change the public argument type and is not
   needed for the current cleanup. No such change was applied.

   Publication: committed and pushed to `ramin-cleanup` as `f234f0e`.

2. `MvPolynomial.hasseDeriv`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseDeriv.md). Changed only the lambda arrow
   `=>` to `↦`, with compiled `rfl` equivalence and unchanged name, signature, and
   construction. Module build passed (1430 jobs); fresh LSP completed with no errors
   and only the existing header warning. Full `lake build` passed (2586 jobs), as did
   `lake build Roth.LeanEval` (2585 jobs); logs:
   `/private/tmp/roth-hasseDeriv-build.log`, `/private/tmp/roth-hasseDeriv-leaneval.log`.
   Local search and literature lookup succeeded. Remote MCP searches failed DNS and
   the escalated retry was interrupted while awaiting approval; their unavailability
   is recorded without claiming mathematical absence. No substantive refactor proposed.

Phases 5a, 5b, 6, 6.5 (independent simplify review), 6.6 (buzz profiling), and 7 remain pending until every declaration is processed. No claim of file completion is made.
