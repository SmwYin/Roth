# Roth cleanup progress

Started: 2026-10-14 (America/Chicago).

## Scope and preservation

- Work in the existing checkout, on `ramin-cleanup`, created from local `main` at
  `d2eb5e9a1806e12e66db25d15d8954ade4be9874`.
- The working tree was clean at entry; the previous branch, `ramin-edits`, remains intact.
- Preserve mathematical meaning, theorem contracts, and the pinned Lean/mathlib versions.
- Validate, commit, and push each completed declaration cleanup before proceeding.
- No pushes to `main`, force pushes, or merges.
- Approval policy updated 2026-10-15 after phone resumption: surface concrete,
  warranted changes needing user input promptly for a decision rather than
  automatically deferring them. Prepare reviewable evidence and continue independent
  authorized cleanup while an answer is pending. Substantial definition, statement,
  or project-structure changes still need explicit approval before application.
  Earlier deferred proposals will be reconsidered during the relevant file review;
  speculative future APIs do not become blockers. Required system approvals remain mandatory.

## Current status

Build/tool setup completed; GitHub browser authentication and branch publication succeeded. The first file audit
(`Roth/HasseDeriv.lean`, 26 declarations) is in progress. The first twenty declarations,
through `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, have completed their audits and
validation; 20 of 264 declarations reviewed. Optional API proposals are recorded
below and remain unapplied. File-level final
review and profiling remain pending.

Cleanup resumed: the user revoked the controlling-session handover hold. The
fully validated twentieth checkpoint is complete; next is
private `hasseDeriv_monomial_mul` (declaration 21) in `Roth/HasseDeriv.lean`.
Continue sequential declaration validation, commit, and push through
every remaining file in the inventory order, without waiting at file boundaries.
Each file still requires final independent review, profiling, and a full build.
The file and project cleanup remain incomplete; substantive proposals remain unapplied.

The first `lake build` installed Lean v4.34.0 and fetched the pinned dependencies.
It was deliberately interrupted during dependency compilation to fetch mathlib's
precompiled cache. After cache installation, `lake build` passed with exit code 0 (2,586 jobs).
`lake build Roth.LeanEval` also passed with exit code 0 (2,585 jobs), covering the
verification module absent from root imports.

GitHub CLI 2.102.0 is installed at `~/.local/bin/gh` (official macOS arm64 release,
SHA-256 verified). Browser authentication succeeded as `rtakloo`; Git uses HTTPS credentials
managed by GitHub CLI. Initial setup commit `0d7c74c` was pushed successfully to
[`ramin-cleanup`](https://github.com/SmwYin/Roth/tree/ramin-cleanup).
The earlier HTTPS credential failure and connected-app HTTP 403 are resolved by this local
CLI authentication. No token is stored in this repository.

The active file audit and declaration results are recorded in
[`cleanup/HasseDeriv.md`](cleanup/HasseDeriv.md). Each completed declaration's report and
source change are committed and pushed together after validation.

## Installed tooling and verification

| Component | Installed location/version | Verification |
| --- | --- | --- |
| mathlib-quality skill | `~/.codex/skills/mathlib-quality` | Instructions and references readable |
| mathlib-quality full workflow | `~/.local/share/roth-mathlib-quality`, commit `d927d3cacf78a74a80bb3ba044d2352a1c5a447e` | Cleanup command and dependency instructions inspected |
| lean4 skill | `~/.codex/skills/lean4` | Instructions and references readable |
| lean4 helper runtime | `~/.local/share/roth-lean4-skills`, commit `b6243b85b9b0a0ddff5bb6773889044daf687f8e` | Sorry analyzer ran: 14 files scanned, zero sorries |
| Lean | `leanprover/lean4:v4.34.0` | Installed by elan; Lake compiled dependency modules |
| uv | 0.13.1 | Installed; successfully installed the LSP tool and Python runtime |
| Python for LSP | 3.12.15, uv-managed | MCP client probe runs |
| lean-lsp-mcp | 0.31.0 | 22 native tools are registered. Native Loogle/Finder and source-search fallback succeeded; LeanSearch returned HTTP 500. Native code execution could not start its server because `lake` was missing from that server's PATH. Direct-client local search, goal inspection, complete diagnostics, and code execution succeeded. Not all 22 tools have been individually tested. |
| GitHub CLI | 2.102.0 | Browser authentication and branch push succeeded |
| ask_chatgpt_math | Skipped | Optional, as authorized |

The Lean LSP server is configured in `~/.codex/config.toml` using its absolute executable
path. Native tools became registered during this session and native remote search was
verified successfully. A later worker had native tools but native `lean_run_code`
failed to start the server because it could not find `lake`; native local search
returned source matches with `index=unavailable`. Registration alone therefore does
not establish working native proof execution. The tested direct stdio MCP client
continues to supply complete diagnostics and code execution successfully. No repair
or restart of the native session is claimed. The first 45-second diagnostic request timed out; a retry with
a 180-second limit completed successfully. A shutdown event-loop warning was emitted after
the successful response and did not invalidate the diagnostics. The `lean4` and
`mathlib-quality` skills are now discoverable. The installed workflow repositories contain
24 mathlib-quality command files, 12 lean4 command files, and 21 lean4 helper wrappers.
These counts describe installed files, not individually tested functions. Claude-specific
slash commands and hooks are adapted manually rather than registered as native commands.
The built-in Claude `/simplify` pass will be adapted to an independent review with the same
reuse, quality, and efficiency checks; unavailable capabilities will be recorded explicitly.

## File queue

The initial source inventory contains 264 declarations across 14 files (5,132 lines).
Files will be processed in dependency order; declarations within each file are sequential.

| File | Initial lines | Status |
| --- | ---: | --- |
| `Roth/HasseDeriv.lean` | 329 | In progress: 20/26 declarations reviewed; next private `hasseDeriv_monomial_mul` |
| `Roth/Box.lean` | 128 | Awaiting cleanup |
| `Roth/Wronskian.lean` | 271 | Awaiting cleanup |
| `Roth/Taylor.lean` | 239 | Awaiting cleanup |
| `Roth/CoeffNorm.lean` | 320 | Awaiting cleanup |
| `Roth/GenWronskian.lean` | 292 | Awaiting cleanup |
| `Roth/Lattice.lean` | 217 | Awaiting cleanup |
| `Roth/Index.lean` | 275 | Awaiting cleanup |
| `Roth/Separation.lean` | 618 | Awaiting cleanup |
| `Roth/Theta.lean` | 981 | Awaiting cleanup |
| `Roth/MainLemma.lean` | 704 | Awaiting cleanup |
| `Roth/Main.lean` | 684 | Awaiting cleanup |
| `Roth/LeanEval.lean` | 60 | Awaiting cleanup |
| `Roth.lean` | 14 | Awaiting cleanup |

## Completed declarations

| Declaration | Change | Validation | Report |
| --- | --- | --- | --- |
| `MvPolynomial.hasseCoeff` (reviewed with deferral) | Eta-reduced the defining function; unchanged signature and mathematical meaning. Optional argument-type generalization deferred for approval | Definitional equality by `rfl`; complete LSP diagnostics, zero errors; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseCoeff.md) |
| `MvPolynomial.hasseDeriv` | Used `↦` for the mathematical lambda; unchanged construction and signature | Definitional equality by `rfl`; module build and complete LSP diagnostics passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv.md) |
| `MvPolynomial.hasseDeriv_monomial` | Replaced the transitivity proof with `simp [hasseDeriv]`; unchanged statement | Independent isolated proof probe, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_monomial.md) |
| `MvPolynomial.hasseDeriv_apply` | Replaced conversion/rewrite and simp with `simp [hasseDeriv, sum_def]`; unchanged statement | Independent isolated proof probe, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_apply.md) |
| `MvPolynomial.hasseCoeff_eq_zero_iff` (reviewed with deferral) | Unsqueezed terminal simp; removed two redundant explicit lemmas. Related argument-type generalization deferred | Independent proof and standard-axiom probe, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseCoeff_eq_zero_iff.md) |
| `MvPolynomial.coeff_hasseDeriv` (reviewed with deferral) | Replaced an inline subtraction contradiction with `tsub_eq_iff_eq_add_of_le`; broader coefficient-type API exploration deferred | Independent proof and standard-axiom probe, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-coeff_hasseDeriv.md) |
| `MvPolynomial.hasseCoeff_eq_prod` (reviewed with inherited deferral) | Packed the 99-column signature; used dot notation and `↦`; earlier coefficient-domain proposal remains deferred | Independent proof and standard-axiom probe, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseCoeff_eq_prod.md) |
| `MvPolynomial.hasseDeriv_zero_apply` | Reviewed; existing short coefficient proof retained, no source change justified | Standard-axiom inspection, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_zero_apply.md) |
| `MvPolynomial.hasseDeriv_zero` | Reviewed; existing `LinearMap.ext` proof retained, no source change justified | Standard-axiom/type inspection, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_zero.md) |
| `MvPolynomial.hasseDeriv_C` (reviewed with optional deferral) | Existing clear rw/simp proof retained; a broader public vanishing lemma is an unnecessary, unimplemented API idea | Isolated original-proof and standard-axiom checks, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_C.md) |
| `MvPolynomial.hasseDeriv_map` (reviewed with optional deferral) | Existing ext/simp proof retained; optional additive coefficient-map API deferred | Isolated original proof/type/axioms, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_map.md) |
| `MvPolynomial.hasseDeriv_rename` (reviewed with optional deferral) | Inlined single-use coefficient transport, removing two proof lines; support-specific API variant deferred | Isolated proof/type/axioms, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_rename.md) |
| Private `choose_mul_choose_eq` | Replaced four-line arithmetic proof with two-line library specialization; removed three `omega` calls | Isolated proof/type/axioms, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-choose_mul_choose_eq.md) |
| Private `hasseCoeff_mul_hasseCoeff` (reviewed with inherited deferral) | Standardized lambda arrows and simplified terminal `simpa`; existing function-domain proposal remains unapplied | Isolated proof/type/axioms, module build and complete LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseCoeff_mul_hasseCoeff.md) |
| `MvPolynomial.hasseDeriv_hasseDeriv` | Reviewed; original ordered coefficient/cast rewrites retained | Isolated original proof/type/axioms, module build and complete direct-client LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_hasseDeriv.md) |
| `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | Inlined the single-use coefficient-equals-one fact in the composition rewrite | Isolated proof/type/axioms, module build and complete direct-client LSP passed; full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_hasseDeriv_of_disjoint.md) |

| Private `hasseCoeff_mul_succ` | Replaced 22 proof lines with a two-line specialization of the coefficient composition identity | Independent original/final proof, type and standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseCoeff_mul_succ.md) |

| `MvPolynomial.pderiv_hasseDeriv` (reviewed with optional API deferral) | Replaced cast bookkeeping and arithmetic normalization with direct ordered rewrites, reducing seven proof lines to four | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-pderiv_hasseDeriv.md) |

| `MvPolynomial.degreeOf_hasseDeriv_le` | Standardized lambda arrow and used `.trans'` for the degree comparison; unchanged statement | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-degreeOf_hasseDeriv_le.md) |

| `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | Used mathlib support exclusion directly, removing the single-use local contradiction | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_eq_zero_of_degreeOf_lt.md) |

## Validation and deferrals

- Remote CI diagnosis supplied by the controlling agent: [run 38788900661](https://github.com/SmwYin/Roth/actions/runs/38788900661)
  at `170ea7b` passed the Lean action. Docgen built and uploaded the documentation,
  but GitHub Pages deployment returned HTTP 400 because the previous `d20b6d5`
  deployment was still in progress. This was a publication-concurrency failure,
  not a Lean compilation failure. No old deployment was rerun and no workflow was
  changed by this cleanup worker; the controlling agent is handling publication separately.
- `lake exe cache get`: exit 0; 8,908 cached dependency files downloaded/decompressed.
- Baseline `lake build`: exit 0; 2,586 jobs. Full compiler output: `cleanup-baseline.log`.
- `lake build Roth.LeanEval`: exit 0; 2,585 jobs (separate verification module).
- Lean LSP diagnostics on `Roth/Box.lean`: complete, 0 errors, 21 existing warnings.
- Source `sorry` scan: passed (14 files, zero findings).
- First declaration: post-edit LSP diagnostics completed, zero errors and the existing header warning. Full downstream builds passed (2,586 jobs and 2,585 jobs respectively). Its equivalence and axiom probes passed; see the declaration audit.
- Second declaration: module build, fresh complete LSP diagnostics, equivalence/axiom
  probes, and both downstream builds passed. The existing header warning remains.
  Local searches and literature lookup succeeded; remote MCP searches failed DNS and
  their permission-dependent retry was interrupted. No remote absence claim is made.
- Deferred: a possible generalization of `hasseCoeff` from finitely supported `k` to an arbitrary function was tested but not applied because it changes the public definition signature.
- Third declaration: module build, complete LSP diagnostics, and both downstream
  builds passed (2,586 and 2,585 jobs). Native Loogle and LeanFinder succeeded;
  LeanSearch returned HTTP 500. Alternative automation probes timed out; the chosen
  simp proof was independently verified and compiled in the project.
- Seventeenth declaration: all audit and worker gates passed; full `lake build`
  (2,586 jobs) and separate `lake build Roth.LeanEval` (2,585 jobs) exited 0.
  The exact statement is preserved and no new proposal or rename is deferred.
- Eighteenth declaration: module, complete LSP, proof/type/axioms and both full
  dependent builds passed (2586 and 2585 jobs). Optional bundled/abstract Hasse API
  suggestions remain unapplied; no statement or definition changed.
- Nineteenth declaration: all required declaration and dependent gates passed.
  A separate stronger bound, `degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j`,
  compiled in a scratch proof and was surfaced for user decision. It has not been added.
- File-level profiling and final project verification remain pending.
- Sixteenth declaration: proof/type/axioms, module/direct-client LSP, full build
  (2,586 jobs), and separate LeanEval build (2,585 jobs) passed. The three-line proof
  retains its exact statement and documentation. This is the clean handover checkpoint;
  declaration 17 has not been started.
- Fifteenth declaration: original proof/type/axioms, module/direct-client LSP, full
  build (2,586 jobs), and separate LeanEval build (2,585 jobs) passed. A combined simp
  trial failed from rewrite ordering and was not adopted. Native run-code PATH
  limitation is documented above; the verified direct client supplies the fallback.
- Fourteenth declaration: proof/type/axioms, module/LSP, full build (2,586 jobs), and
  separate LeanEval build (2,585 jobs) passed. The twice-used support inclusion was
  retained; only notation and terminal simplification changed. Allowing an arbitrary
  function in the remaining multi-index would depend on the earlier deferred
  coefficient-domain redesign; no such API change was applied.
- Thirteenth declaration: proof/type/axioms, module/LSP, full build (2,586 jobs), and
  separate LeanEval build (2,585 jobs) passed. Removing the now-small private wrapper
  is a file-level review candidate; no user-approval requirement is inferred solely
  from this minor structural possibility. Its name may aid the following proof.
- Twelfth declaration: proof/type/axioms, module/LSP, full build (2,586 jobs), and
  separate LeanEval build (2,585 jobs) passed. Global injectivity is necessary for
  the stated theorem; a support-specific variant would need a different public
  hypothesis/transport API and remains optional and unapplied.
- Eleventh declaration: original proof/type/axioms, module/LSP, full build (2,586 jobs),
  and separate LeanEval build (2,585 jobs) passed. Removing `coeff_map` left an unsolved
  goal in isolation, so the original proof was retained. An additive coefficient-map
  formulation would require a different map operation/public statement and remains
  an optional unapplied API proposal, not a blocker.
- Tenth declaration: original proof, module/LSP, full build (2,586 jobs), and separate
  LeanEval build (2,585 jobs) passed. A direct simp trial looped; excluding a simp
  rule compiled but was less clear than the retained proof. A broader public
  monomial-vanishing lemma remains an optional unimplemented API idea, not a blocker.
- Ninth declaration: retained identity-map proof verified by module/LSP checks,
  standard-axiom/type inspection, full build (2,586 jobs), and separate LeanEval
  build (2,585 jobs). Report-only checkpoint; next declaration is `hasseDeriv_C`.
- Eighth declaration: retained proof verified by module/LSP checks, standard-axiom
  inspection, full build (2,586 jobs), and separate LeanEval build (2,585 jobs).
  A direct unfolding alternative failed in an isolated probe and was not adopted.
- Seventh declaration: module/LSP/isolated proof checks and both dependent builds
  passed (2,586 and 2,585 jobs). Native Loogle/Finder confirmed the generic product
  lemma already used; LeanSearch returned HTTP 500. No new API proposal was added.
- Sixth declaration: all module/LSP/dependent gates passed (2,586 full-build jobs and
  2,585 separate LeanEval jobs). A noncommutative-semiring or module-valued formulation
  would require reviewing and changing the public derivative construction and theorem
  interface. This is an unproved optional API exploration, deferred for approval;
  no broader result has been implemented or claimed.
- Fifth declaration: module build, complete LSP diagnostics, full build (2,586 jobs),
  and separate LeanEval build (2,585 jobs) passed. The earlier optional generalization
  of `hasseCoeff` would also require changing this theorem's public statement; this
  remains unapplied pending approval, while independent cleanup continues.
- Fourth declaration: module build, complete LSP diagnostics, full build (2,586 jobs),
  and separate LeanEval build (2,585 jobs) passed. Finder/Loogle succeeded through the
  approved direct MCP client; LeanSearch returned HTTP 500.
