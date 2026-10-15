# HasseDeriv cleanup audit

Status: all 26 original declarations audited and validated; all final cleanup phases complete.
The source retains 25 declarations after the single-use private wrapper was removed.
Independent review passed without changes; actual profiling puts every retained
declaration under 1000ms (maximum 597.68ms). Public API preserved. The two optional
companion bounds were declined by the user; other speculative API explorations were
closed without implementation in final review. Unconfirmed copyright/license
metadata remains an external limitation; warning-free status is not claimed.
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
| C.12 | `hasseDeriv_rename` (theorem) | 139–149 | 9 | Reviewed with optional support-specific API deferred; inlined single-use coefficient transport and removed two proof lines |
| C.13 | `choose_mul_choose_eq` (lemma) | 151–156 | 5 | Full audit complete; two-line library specialization replaces four-line proof and all omega calls; helper retention queued for final review |
| C.14 | `hasseCoeff_mul_hasseCoeff` (lemma) | 158–171 | 12 | Reviewed with inherited coefficient-domain proposal deferred; lambda notation and terminal simpa simplified; twice-used support fact retained |
| C.15 | `hasseDeriv_hasseDeriv` (theorem) | 178–182 | 4 | Full audit complete; original ordered coefficient/cast rewrite proof retained |
| C.16 | `hasseDeriv_hasseDeriv_of_disjoint` (theorem) | 188–192 | 4 | Full audit complete; single-use coefficient-equals-one fact inlined in composition rewrite; exact statement retained |
| C.17 | `hasseCoeff_mul_succ` (lemma) | 194–218 | 23 | Full audit complete; two-line coefficient-composition specialization replaces 22-line product-erasure proof; exact statement preserved |
| C.18 | `pderiv_hasseDeriv` (theorem) | 223–231 | 8 | Reviewed with optional API deferral; direct ordered coefficient/cast rewrites remove local cast identity and arithmetic normalization |
| C.19 | `degreeOf_hasseDeriv_le` (theorem) | 236–240 | 4 | Full original-theorem cleanup complete; lambda arrow and dot notation improved; separate stronger-bound proposal surfaced for user decision |
| C.20 | `hasseDeriv_eq_zero_of_degreeOf_lt` (theorem) | 245–250 | 5 | Full audit complete; mathlib support-exclusion API replaces local contradiction, removing one proof line |
| C.21 | `hasseDeriv_monomial_mul` (lemma) | 252–266 | 14 | Full audit complete; inlined coefficient identity, compact support cases, terminal simp replaces ring_nf; two lines removed |
| C.22 | `hasseDeriv_mul_of_degreeOf_eq_zero` (theorem) | 272–277 | 5 | Full audit complete; inlined support-degree fact, standardized lambdas; one proof line removed |
| C.23 | `hasseDeriv_single_aeval_X` (theorem) | 283–292 | 8 | Full audit complete; removed hc and unsqueezed terminal simp, with local map_natCast exclusion; two proof lines removed |
| C.24 | `uniqueAlgEquiv_hasseDeriv` (theorem) | 298–304 | 6 | Full audit complete; three-line coefficient proof eliminates conversion helper, lambda, and semicolon |
| C.25 | `hasseCoeff_le_two_pow` (theorem) | 309–313 | 4 | Full audit complete; existing proof retained, lambda standardized; optional summed-bound companion compiled and declined by user |
| C.26 | `factorial_smul_hasseDeriv_single` (theorem) | 319–327 | 8 | Full audit complete; direct cast-product and commutativity rewrites replace push_cast and ring_nf; two proof lines removed |

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

    Publication: committed and pushed to `ramin-cleanup` as `4a32dea`.

12. `MvPolynomial.hasseDeriv_rename`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_rename.md). Inlined the
    single-use coefficient-transport fact into the monomial-case simp call, removing
    two proof lines. Statement and induction structure are unchanged. Isolated
    proof/type/standard-axiom checks, module build (1430 jobs), and complete LSP passed.
    Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs)
    both exited 0. Logs `/private/tmp/roth-hasseDeriv_rename-build.log` and
    `/private/tmp/roth-hasseDeriv_rename-leaneval.log`.
    Injectivity is necessary in general; a support-specific variant would require
    different public hypotheses and transport API, so it remains optional and deferred.

    Publication: committed and pushed to `ramin-cleanup` as `a8cd173`.

13. Private `choose_mul_choose_eq`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-choose_mul_choose_eq.md). Replaced four
    proof lines with a two-line `simpa` specialization of `Nat.choose_mul` and
    binomial symmetry, removing all three `omega` calls. The statement is unchanged.
    Isolated proof/type/standard-axiom checks, module build (1430 jobs), and complete
    LSP passed. Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval`
    (2585 jobs) both exited 0. Logs `/private/tmp/roth-choose_mul_choose_eq-build.log`
    and `/private/tmp/roth-choose_mul_choose_eq-leaneval.log`.
    File-level review candidate: retain this short named identity for clarity or
    inline its library specialization into the following proof. This is a scope
    deferral for final review, not an automatic requirement for user approval.

    Publication: committed and pushed to `ramin-cleanup` as `d7575e6`.

14. Private `hasseCoeff_mul_hasseCoeff`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseCoeff_mul_hasseCoeff.md). Standardized
    five lambda arrows and simplified terminal `simpa`, retaining the support fact
    used twice. Statement and proof structure are unchanged. Isolated proof/type/axiom
    checks, module build (1430 jobs), and complete LSP passed. Full `lake build`
    (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs) both exited 0.
    Logs `/private/tmp/roth-hasseCoeff_mul_hasseCoeff-build.log` and
    `/private/tmp/roth-hasseCoeff_mul_hasseCoeff-leaneval.log`.
    The inherited coefficient-domain generalization remains unapplied; this checkpoint
    makes no substantive definition or statement change.

    Publication: committed and pushed to `ramin-cleanup` as `7df4a50`.

15. `MvPolynomial.hasseDeriv_hasseDeriv`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_hasseDeriv.md). Retained the
    ordered rewrite proof; a combined simp trial normalized an index too early and
    was not adopted. Original proof/type/standard-axiom checks, module build (1430 jobs),
    and complete direct-client LSP passed. Full `lake build` (2586 jobs) and separate
    `lake build Roth.LeanEval` (2585 jobs) both exited 0. Logs:
    `/private/tmp/roth-hasseDeriv_hasseDeriv-build.log` and
    `/private/tmp/roth-hasseDeriv_hasseDeriv-leaneval.log`.
    Native run-code failed because its server could not find `lake`; the direct-client
    fallback succeeded. The shared tooling report records this verified limitation.

    Publication: committed and pushed to `ramin-cleanup` as `d20b6d5`.

16. `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_hasseDeriv_of_disjoint.md).
    Inlined the single-use coefficient-equals-one fact into the composition rewrite
    and standardized its lambda arrow. The exact statement and documentation remain.
    Isolated proof/type/standard-axiom checks, module build (1430 jobs), and complete
    direct-client LSP passed. Full `lake build` (2586 jobs) and separate
    `lake build Roth.LeanEval` (2585 jobs) both exited 0. Logs:
    `/private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-build.log` and
    `/private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-leaneval.log`.
    All tracked builds and probes completed before this handover checkpoint.
    Resume at private `hasseCoeff_mul_succ`; it has not been started.

17. Private `hasseCoeff_mul_succ`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseCoeff_mul_succ.md). Reused
    `hasseCoeff_mul_hasseCoeff` with a singleton order, replacing 22 proof lines
    with two and removing the separate product-erasure argument. The exact statement
    is unchanged. Original/final isolated proof, type and standard-axiom probes,
    module build, and complete LSP passed; only the existing header warning remains.
    Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs)
    both exited 0. Logs `/private/tmp/roth-hasseCoeff_mul_succ-build.log` and
    `/private/tmp/roth-hasseCoeff_mul_succ-leaneval.log`.
    No new substantial proposal or rename is deferred.

18. `MvPolynomial.pderiv_hasseDeriv`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-pderiv_hasseDeriv.md). Direct coefficient
    and natural-cast rewrites replace the local cast identity, `push_cast`, `abel`,
    and `ring`, reducing seven proof lines to four. Statement and docstring remain
    byte-identical. Isolated proof/type/standard-axiom checks, module build and
    complete LSP passed. Full `lake build` (2586 jobs) and separate
    `lake build Roth.LeanEval` (2585 jobs) exited 0; logs
    `/private/tmp/roth-pderiv_hasseDeriv-build.log` and
    `/private/tmp/roth-pderiv_hasseDeriv-leaneval.log`.
    Optional abstract Hasse–Schmidt or bundled composition APIs would change the
    interface; they remain proposals, not applied changes or blockers.

19. `MvPolynomial.degreeOf_hasseDeriv_le`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-degreeOf_hasseDeriv_le.md). Standardized
    the lambda arrow and expressed the same degree comparison with `.trans'`.
    Signature and documentation are unchanged. Isolated proof/type/standard-axiom
    checks, module build, and complete LSP passed. Full `lake build` (2586 jobs)
    and separate `lake build Roth.LeanEval` (2585 jobs) exited 0; logs
    `/private/tmp/roth-degreeOf_hasseDeriv_le-build.log` and
    `/private/tmp/roth-degreeOf_hasseDeriv_le-leaneval.log`.
    A scratch proof verifies the stronger subtraction bound as a potential separate
    `degreeOf_hasseDeriv_le_sub` theorem. It was surfaced for user decision; the
    user declined the addition and chose the current API. Existing theorem and four
    callers remain unchanged, with no pending decision for this proposal.

20. `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: dedicated worker complete;
    see [the full declaration audit](HasseDeriv-hasseDeriv_eq_zero_of_degreeOf_lt.md).
    Used `notMem_support_of_degreeOf_lt` directly, replacing the single-use `hP`
    contradiction and removing one proof line. Exact signature/docs preserved.
    Isolated proof/type/standard-axiom checks, module build, complete LSP and final
    proof-state check passed. Full `lake build` (2586 jobs) and separate
    `lake build Roth.LeanEval` (2585 jobs) exited 0; logs
    `/private/tmp/roth-hasseDeriv_eq_zero_of_degreeOf_lt-build.log` and
    `/private/tmp/roth-hasseDeriv_eq_zero_of_degreeOf_lt-leaneval.log`.
    No new proposal, rename, or unresolved worker item.

21. Private `hasseDeriv_monomial_mul`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_monomial_mul.md). Inlined
    the single-use coefficient identity, simplified the support split and replaced
    `ring_nf` with terminal `simp`, reducing fifteen declaration lines to thirteen.
    Exact signature preserved; no new helper/import/API. Isolated proof/type/axiom,
    module build and complete native LSP checks passed. Full `lake build` (2586 jobs)
    and separate `lake build Roth.LeanEval` (2585 jobs) exited 0; logs
    `/private/tmp/roth-hasseDeriv_monomial_mul-build.log` and
    `/private/tmp/roth-hasseDeriv_monomial_mul-leaneval.log`.
    No new proposal, rename, or unresolved worker item.

22. `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: dedicated worker complete;
    see [the full declaration audit](HasseDeriv-hasseDeriv_mul_of_degreeOf_eq_zero.md).
    Inlined `ha` at its sole call and standardized mathematical lambda arrows;
    four proof lines become three. Exact signature/docs preserved. Isolated
    proof/type/standard-axiom, module and complete native LSP checks passed.
    Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval`
    (2585 jobs) exited 0; logs
    `/private/tmp/roth-hasseDeriv_mul_of_degreeOf_eq_zero-build.log` and
    `/private/tmp/roth-hasseDeriv_mul_of_degreeOf_eq_zero-leaneval.log`.
    No new proposal, rename, or unresolved worker item.

23. `MvPolynomial.hasseDeriv_single_aeval_X`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseDeriv_single_aeval_X.md).
    Removed the local coefficient fact and unsqueezed both terminal simp calls,
    using a local `-map_natCast` exclusion to preserve the coefficient form needed
    by `C_mul_monomial`. Seven proof lines become five, with exact signature/docs.
    Isolated proof/type/standard-axiom, module and complete LSP checks passed.
    Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval`
    (2585 jobs) exited 0; logs `/private/tmp/roth-hasseDeriv_single_aeval_X-build.log`
    and `/private/tmp/roth-hasseDeriv_single_aeval_X-leaneval.log`.
    No new proposal, rename, or unresolved worker item.

24. `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-uniqueAlgEquiv_hasseDeriv.md).
    Replaced the conversion helper with a direct coefficient-extensionality proof;
    four proof lines become three. Signature/docs preserved. Isolated proof/type/
    standard-axiom, module and complete LSP checks passed. Full `lake build`
    (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs) exited 0;
    logs `/private/tmp/roth-uniqueAlgEquiv_hasseDeriv-build.log` and
    `/private/tmp/roth-uniqueAlgEquiv_hasseDeriv-leaneval.log`.
    No new proposal, rename, or unresolved worker item.

25. `MvPolynomial.hasseCoeff_le_two_pow`: dedicated worker complete; see
    [the full declaration audit](HasseDeriv-hasseCoeff_le_two_pow.md). Retained
    the existing concise product proof and standardized its mathematical lambda.
    Statement/docs unchanged. Isolated proof/type/standard-axiom, module and complete
    LSP checks passed. Full `lake build` (2586 jobs) and separate
    `lake build Roth.LeanEval` (2585 jobs) exited 0; logs
    `/private/tmp/roth-hasseCoeff_le_two_pow-build.log` and
    `/private/tmp/roth-hasseCoeff_le_two_pow-leaneval.log`.
    The optional sum-bound companion was compiled in scratch and considered together
    with the stronger degree bound. User decision: keep the current API; both additions
    declined, neither applied, no pending decision for these proposals.

26. `MvPolynomial.factorial_smul_hasseDeriv_single`: dedicated worker complete;
    see [the full declaration audit](HasseDeriv-factorial_smul_hasseDeriv_single.md).
    Extended the final rewrite chain with `Nat.cast_mul` and `mul_comm`, replacing
    `push_cast` and `ring_nf` and saving two lines. Exact signature/docs preserved.
    Isolated proof/type/standard-axiom, module and complete LSP checks passed.
    Full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval`
    (2585 jobs) exited 0; logs
    `/private/tmp/roth-factorial_smul_hasseDeriv_single-build.log` and
    `/private/tmp/roth-factorial_smul_hasseDeriv_single-leaneval.log`.
    No new proposal, rename, or unresolved worker item.

## Final-phase checkpoint

Phase 5a removed the single-use private `choose_mul_choose_eq` wrapper and used
`Nat.choose_mul` directly at its sole caller, saving three lines. The original
26-declaration audit trail remains intact; 25 declarations remain in the source.
Complete LSP, module build, full `lake build` (2586 jobs) and separate
`lake build Roth.LeanEval` (2585 jobs) all passed. Retained signatures and all
documentation are preserved. See [the final-phase report](HasseDeriv-final.md).

The rename queue is empty; project-wide Phase 5b will run after all files.
Phase 6 cumulative code/build gates pass with the known copyright metadata warning.
Phase 6.5 independent review completed with PASS-THROUGH. Phase 6.6 actual profiling
completed with FAST-BOARD: all 25 retained declarations below 1000ms, maximum
597.68ms. Phase 7 comprehensive report is complete. Source: 329 → 288 lines (−41).
All source cleanup and verification phases are complete, with the unconfirmed
copyright/license metadata limitation remaining explicit.
