# HasseDeriv cleanup audit

Status: 11 of 26 declarations audited and validated.
User resumed active cleanup after the ninth checkpoint. Next declaration:
`hasseDeriv_rename` (twelfth); continue sequentially through the full project.
`hasseCoeff`, `hasseCoeff_eq_zero_iff`, and `hasseCoeff_eq_prod` are reviewed with their related optional
argument-type generalization deferred for approval.
`coeff_hasseDeriv` is reviewed with a broader coefficient-type API exploration deferred.
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
| C.1 | `hasseCoeff` (def) | 44–44 | 1 | Reviewed with deferral: eta reduction validated; optional argument-type generalization deferred |
| C.2 | `hasseDeriv` (def) | 51–54 | 4 | Full audit complete; lambda notation updated with definitional equivalence validated |
| C.3 | `hasseDeriv_monomial` (theorem) | 60–62 | 2 | Full audit complete; replaced transitivity proof with terminal `simp [hasseDeriv]`; unchanged statement |
| C.4 | `hasseDeriv_apply` (theorem) | 67–70 | 3 | Full audit complete; direct `simp [hasseDeriv, sum_def]` replaces two-tactic proof; unchanged statement |
| C.5 | `hasseCoeff_eq_zero_iff` (theorem) | 75–77 | 3 | Reviewed with deferral: terminal simp unsqueezed and validated; related argument-type generalization deferred |
| C.6 | `coeff_hasseDeriv` (theorem) | 84–95 | 11 | Reviewed with deferral: reused standard subtraction equivalence; broader coefficient-type API exploration deferred |
| C.7 | `hasseCoeff_eq_prod` (theorem) | 101–103 | 2 | Reviewed with inherited deferral: signature packed to 99 columns; dot notation and lambda arrow updated; existing coefficient-domain proposal deferred |
| C.8 | `hasseDeriv_zero_apply` (theorem) | 108–110 | 3 | Full audit complete; existing short coefficient proof retained; no source change justified |
| C.9 | `hasseDeriv_zero` (theorem) | 116–117 | 2 | Full audit complete; existing minimal LinearMap.ext proof retained; no source change justified |
| C.10 | `hasseDeriv_C` (theorem) | 122–124 | 3 | Reviewed with optional API idea deferred; existing clear rw/simp proof retained |
| C.11 | `hasseDeriv_map` (theorem) | 130–133 | 3 | Reviewed with optional additive-map API deferred; original concise proof retained and validated |
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

   Publication: committed and pushed to `ramin-cleanup` as `59d451d`.

3. `MvPolynomial.hasseDeriv_monomial`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseDeriv_monomial.md). The proof is now
   `by simp [hasseDeriv]`, preserving its statement and simp attribute. An isolated
   copied-definition probe verified the proof independently of this theorem.
   Module build passed (1430 jobs); complete LSP diagnostics found no errors and only
   the existing header warning. Full `lake build` passed (2586 jobs) and separate
   `lake build Roth.LeanEval` passed (2585 jobs), both exit 0. Logs:
   `/private/tmp/roth-hasseDeriv_monomial-build.log` and
   `/private/tmp/roth-hasseDeriv_monomial-leaneval.log`.
   Native Loogle and LeanFinder succeeded; LeanSearch returned HTTP 500. Read-only
   alternative automation probes timed out; no success or failure of individual
   alternatives is inferred. The chosen proof passed all compilation gates.

   Publication: committed and pushed to `ramin-cleanup` as `1bfa9f3`.

4. `MvPolynomial.hasseDeriv_apply`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseDeriv_apply.md). Direct simplification
   with `hasseDeriv` and `sum_def` replaces conversion and rewriting, removing one
   line while preserving the statement. The independent probe excludes the target
   and later theorems. Module build passed (1430 jobs); complete LSP found no errors
   and only the existing header warning. Full `lake build` (2586 jobs) and separate
   `lake build Roth.LeanEval` (2585 jobs) both exited 0. Logs:
   `/private/tmp/roth-hasseDeriv_apply-build.log` and
   `/private/tmp/roth-hasseDeriv_apply-leaneval.log`.
   Finder/Loogle succeeded through the approved direct client; LeanSearch returned
   HTTP 500. No substantive change is queued.

   Publication: committed and pushed to `ramin-cleanup` as `373ec6d`.

5. `MvPolynomial.hasseCoeff_eq_zero_iff`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseCoeff_eq_zero_iff.md). Replaced
   terminal `simp only` by `simp` and removed explicit `not_le`/`exists_prop`, preserving
   the exact statement. Independent proof and standard-axiom probes passed.
   Module build passed (1430 jobs); complete LSP found no errors and only the existing
   header warning. Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval`
   (2585 jobs) both exited 0. Logs:
   `/private/tmp/roth-hasseCoeff_eq_zero_iff-build.log` and
   `/private/tmp/roth-hasseCoeff_eq_zero_iff-leaneval.log`.
   Finder/Loogle succeeded, LeanSearch returned HTTP 500. Reviewed with deferral:
   the previously proposed broader `hasseCoeff` argument would also change this
   theorem's public statement, requiring approval. It remains unapplied.

   Publication: committed and pushed to `ramin-cleanup` as `2d62138`.

6. `MvPolynomial.coeff_hasseDeriv`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-coeff_hasseDeriv.md). Replaced an inline
   subtraction contradiction with `tsub_eq_iff_eq_add_of_le hdk` in the existing
   simp proof. The coefficient formula and documentation are unchanged. Independent
   proof/standard-axiom probe, module build (1430 jobs), and complete LSP passed;
   only the existing header warning remains. Full `lake build` (2586 jobs) and
   separate `lake build Roth.LeanEval` (2585 jobs) both exited 0. Logs:
   `/private/tmp/roth-coeff_hasseDeriv-build.log` and
   `/private/tmp/roth-coeff_hasseDeriv-leaneval.log`.
   Native Loogle/Finder searches succeeded; LeanSearch returned HTTP 500.
   Reviewed with deferral: broader noncommutative-semiring or module-valued operator
   formulations would require substantive construction/interface changes. This is
   an unproved optional exploration, left unapplied pending approval.

   Publication: committed and pushed to `ramin-cleanup` as `b37a775`.

7. `MvPolynomial.hasseCoeff_eq_prod`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseCoeff_eq_prod.md). Packed the unchanged
   signature onto one 99-column line and expressed the same `Finsupp.prod_fintype`
   proof using dot notation and `↦`. Independent proof/standard-axiom probe, module
   build (1430 jobs), and complete LSP passed; only the existing header warning remains.
   Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs)
   both exited 0. Logs `/private/tmp/roth-hasseCoeff_eq_prod-build.log` and
   `/private/tmp/roth-hasseCoeff_eq_prod-leaneval.log`.
   Native Loogle/Finder confirmed existing generic product infrastructure; LeanSearch
   returned HTTP 500. The earlier coefficient-domain proposal remains deferred;
   no new substantial change is proposed.

   Publication: committed and pushed to `ramin-cleanup` as `6ab3654`.

8. `MvPolynomial.hasseDeriv_zero_apply`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseDeriv_zero_apply.md). Retained the
   existing coefficient-extensionality proof. Direct unfolding left a residual sum
   identity in an isolated experiment; no failed experiment was adopted. Module
   build (1430 jobs), complete LSP, and standard-axiom/type inspection passed;
   only the existing header warning remains. Full `lake build` (2586 jobs) and
   separate `lake build Roth.LeanEval` (2585 jobs) both exited 0. Logs:
   `/private/tmp/roth-hasseDeriv_zero_apply-build.log` and
   `/private/tmp/roth-hasseDeriv_zero_apply-leaneval.log`.
   Source is byte-identical; this checkpoint records the completed review.

   Publication: committed and pushed to `ramin-cleanup` as `f9f649f`.

9. `MvPolynomial.hasseDeriv_zero`: dedicated worker complete; see
   [the full declaration audit](HasseDeriv-hasseDeriv_zero.md). Retained the existing
   minimal `LinearMap.ext` proof, matching the analogous library packaging.
   Module build (1430 jobs), complete LSP, and standard-axiom/type inspection passed;
   only the existing header warning remains. Full `lake build` (2586 jobs) and
   separate `lake build Roth.LeanEval` (2585 jobs) both exited 0. Logs:
   `/private/tmp/roth-hasseDeriv_zero-build.log` and
   `/private/tmp/roth-hasseDeriv_zero-leaneval.log`.
   Source is byte-identical; this checkpoint records the completed review and the
   resumption point for controlling-session handover.

   Publication: committed and pushed to `ramin-cleanup` as `667acf6`.

10. `MvPolynomial.hasseDeriv_C`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_C.md). Retained the original
    rw/simp proof. Direct simp consolidation looped; excluding a simp rule compiled
    but added an exception without a useful clarity benefit. The original target
    compiled independently with only standard axioms. Module build (1430 jobs),
    complete LSP, full `lake build` (2586 jobs), and separate `lake build Roth.LeanEval`
    (2585 jobs) all passed; only the existing header warning remains in this file.
    Logs `/private/tmp/roth-hasseDeriv_C-build.log` and
    `/private/tmp/roth-hasseDeriv_C-leaneval.log`.
    A broader public monomial-vanishing lemma is an optional unimplemented API idea;
    no current cleanup need was established, and it does not block continued work.

    Publication: committed and pushed to `ramin-cleanup` as `733ed99`.

11. `MvPolynomial.hasseDeriv_map`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_map.md). Retained its concise
    coefficient-extensionality proof. Removing `coeff_map` failed in an isolated
    probe; the original proof/type/standard-axiom probe passed. Module build
    (1430 jobs), complete LSP, full `lake build` (2586 jobs), and separate
    `lake build Roth.LeanEval` (2585 jobs) all passed. Logs:
    `/private/tmp/roth-hasseDeriv_map-build.log` and
    `/private/tmp/roth-hasseDeriv_map-leaneval.log`.
    An optional additive coefficient-map formulation would change the public map
    operation and statement; it remains unapplied and does not block cleanup.

Phases 5a, 5b, 6, 6.5 (independent simplify review), 6.6 (buzz profiling), and 7 remain pending until every declaration is processed. No claim of file completion is made.
