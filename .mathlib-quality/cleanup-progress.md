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

Build/tool setup completed; GitHub browser authentication and branch publication succeeded.
The first file, `Roth/HasseDeriv.lean`, has completed all declaration and final review,
build, and profiling phases, with unconfirmed copyright/license metadata remaining
as an external limitation. All 26 original declarations were audited and validated;
25 remain after removal of a single-use private wrapper. HasseDeriv accounts for 26 of 264 original
declarations reviewed. Source: 329 → 288 lines (−41). Independent simplify review:
PASS-THROUGH. Actual profiling: all 25 retained declarations under 1000ms, maximum
597.68ms. Module, complete LSP, full project and separate LeanEval builds passed.
See [final-phase report](cleanup/HasseDeriv-final.md) for evidence and limitations.

Cleanup is active. `Roth/Box.lean` has completed all declaration and final file-level phases.
All 14 declarations retained and reviewed; overall 40/264 original declarations reviewed.
Box source 128 → 126 lines; independent simplify finding fixed (two redundant imports),
final module/full/LeanEval and complete LSP gates pass. Actual profiling: all 14 below 1000ms,
maximum 196.39ms. See [Box final report](cleanup/Box-final.md).
`Roth/Wronskian.lean` has completed all 15 original declaration audits and final file-level phases.
13 declarations remain after two private Mathlib replacements; source271 → 218 lines after the approved hypothesis amendment.
Fresh independent simplify review found five redundant imports, removed and revalidated.
Final module/full/separate LeanEval, complete LSP, public-type/definition compatibility, and
axiom gates pass. Post-amendment actual profiling: all13 below1000ms, maximum586.13ms.
See [Wronskian final report](cleanup/Wronskian-final.md). Overall55/264 original declarations audited.
`Roth/Taylor.lean` has completed all20 original declaration audits, both new private-helper audits,
and every final file-level phase. Source239 → 218lines; original public API/docs preserved.
Independent simplify finding fixed and revalidated; actual profile all22 retained declarations
below750ms, maximum672.30ms. Overall75/264 original declarations audited.
See [Taylor final report](cleanup/Taylor-final.md). `Roth/CoeffNorm.lean` has completed all26 original declaration audits, its new private-helper audit and every final file phase. Source320→268; independent simplify fixes applied and revalidated. All26 retained declarations profile below750ms (maximum656.95ms); final module/full/separate LeanEval, complete module/caller LSP, all25 original-public type/value comparisons and standard axioms pass. Overall101/264 originals audited. See [CoeffNorm final report](cleanup/CoeffNorm-final.md). Compiled public-hypothesis proposal awaits scoped user decision; published public signatures remain unchanged. Header metadata warning remains user-preserved. GenWronskian has completed all19 original audits, both added-helper audits and every final file phase. Source292→263; independent simplify removed two redundant imports, measured digit-injection optimization applied. All19 retained declarations below1000ms, maximum921.00ms with required borderline repeat passed. Final complete module/caller diagnostics, all13 public type/three definition-value comparisons, standard axioms, full build and separate LeanEval pass. See [GenWronskian final report](cleanup/GenWronskian-final.md). Overall120/264 originals;6/14 files complete. Two compiled GenWronskian public-assumption proposals remain unapplied awaiting scoped decision; metadata remains user-preserved.
The user approved removing unused `hφ`/`hd` from the Wronskian coefficient identity;
the exact removal and sole-caller update are implemented and fully revalidated. Both unused
argument warnings are gone; header metadata remains unchanged.
Continue sequential declaration validation, commit, and push through every remaining
file in inventory order without waiting at file boundaries. Each file requires final
independent review, profiling, and a full build. The project remains incomplete.
The user declined the two optional companion bounds and chose to preserve the API;
other speculative API explorations were assessed and closed without implementation
at final file review. No warranted API change is awaiting approval for HasseDeriv.
The user chose unchanged copyright/license metadata without supplying authoritative facts;
the header warnings remain explicit, and no metadata was invented or suppressed.

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
[`cleanup/Taylor.md`](cleanup/Taylor.md), following the completed HasseDeriv, Box and Wronskian reports. Each completed declaration's report and
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
continues to supply complete diagnostics and code execution successfully. Native proof execution and complete diagnostics later succeeded for declaration 21;
this records that observed recovery without claiming a configuration repair or restart. The first 45-second diagnostic request timed out; a retry with
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
| `Roth/HasseDeriv.lean` | 329 | All cleanup phases complete; 26/26 original declarations reviewed; copyright/license metadata unresolved |
| `Roth/Box.lean` | 128 | All cleanup phases complete; 14/14 declarations reviewed; header warning retained by user decision |
| `Roth/Wronskian.lean` | 271 | All cleanup phases complete;15/15 original declarations audited; user-preserved metadata |
| `Roth/Taylor.lean` | 239 | All cleanup phases complete;20/20 originals and2 added helpers audited; user-preserved metadata |
| `Roth/CoeffNorm.lean` | 320 | All cleanup phases complete;26/26 originals and1 added helper audited; compiled public proposal pending |
| `Roth/GenWronskian.lean` | 292 | All cleanup phases complete;19/19 originals and2 added helpers audited; metadata/two compiled public proposals explicit |
| `Roth/Lattice.lean` | 217 | Active: original declarations 3/10 audited; final file phases pending |
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

| Private `hasseDeriv_monomial_mul` | Inlined coefficient identity, simplified support cases, and replaced ring normalization with simp; two lines removed | Isolated proof/type/standard-axiom checks, module build, complete native LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_monomial_mul.md) |

| `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | Inlined the support-degree fact and standardized lambdas; four proof lines reduced to three | Isolated proof/type/standard-axiom checks, module build, complete native LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_mul_of_degreeOf_eq_zero.md) |

| `MvPolynomial.hasseDeriv_single_aeval_X` | Removed local coefficient fact and unsqueezed terminal simp calls; seven proof lines reduced to five | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseDeriv_single_aeval_X.md) |

| `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | Replaced conversion helper with direct three-line coefficient proof | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-uniqueAlgEquiv_hasseDeriv.md) |

| `MvPolynomial.hasseCoeff_le_two_pow` | Retained existing product proof and standardized mathematical lambda arrow | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-hasseCoeff_le_two_pow.md) |

| `MvPolynomial.factorial_smul_hasseDeriv_single` | Replaced push_cast and ring_nf with explicit cast-product and commutativity rewrites, saving two lines | Isolated proof/type/standard-axiom checks, module build, complete LSP, full `lake build` and separate `lake build Roth.LeanEval` passed | [Declaration audit](cleanup/HasseDeriv-factorial_smul_hasseDeriv_single.md) |

## Validation and deferrals

- User decision (2026-10-15): “Keep the current API as you recommend.” The compiled
  optional stronger degree bound and total-exponent-sum coefficient-bound companion
  were considered and declined. Neither was added; no decision remains pending for them.

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
  compiled in a scratch proof and was surfaced for user decision. The user declined
  adding it, choosing to keep the current API.
- HasseDeriv file-level independent review and profiling completed; all 25 retained declarations are below budget. Final whole-project verification remains pending until the remaining files are cleaned.
- Sixteenth declaration: proof/type/axioms, module/direct-client LSP, full build
  (2,586 jobs), and separate LeanEval build (2,585 jobs) passed. The three-line proof
  retains its exact statement and documentation. This was the earlier handover checkpoint; declarations 17–26 and final file phases have since completed.
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

## HasseDeriv final checkpoint

Final source checkpoint `76f8c58` passed module, complete LSP, full `lake build`
and separate `lake build Roth.LeanEval`. Fresh independent simplify review found
no actionable issue. Supported Lean 4.34 profiling with trace anchors measured
all 25 retained declarations below 1000ms (maximum 597.68ms), with no performance
fix or source instrumentation needed. All 26 original declaration reports and
final audit gates are complete. Full evidence: [HasseDeriv-final.md](cleanup/HasseDeriv-final.md).
The absent confirmed copyright/license metadata remains explicit; warning-free
status is not claimed. The global rename pass remains for the project end.

## Box declaration 1 checkpoint

`Roth.box`: mathematical lambda normalized to `↦`; two body lines packed to one
97-codepoint line. Declaration 3 → 2 lines, file 128 → 127. Public signature and
existing docstring unchanged; isolated `rfl` verifies identical construction.
Complete LSP, module build, type/isolation/standard-axiom checks pass.
Declaration audit: [Box-box.md](cleanup/Box-box.md).

Publication verification for `Roth.box`: actual full `lake build` session 17861 exited 0
(2586 jobs; `/private/tmp/roth-box-box-build.log`); separate `lake build Roth.LeanEval`
session 96802 exited 0 (2585 jobs; `/private/tmp/roth-box-d01-leaneval.log`).
All dependent modules pass; remaining warnings are baseline warnings tracked for their own cleanup.

## Box declaration 2 checkpoint

`Roth.mem_box`: removed redundant `Finset.mem_map_equiv` from the terminal simp
argument list; statement and documentation unchanged. Complete per-declaration audit,
module build, native full LSP, isolated proof/type/standard-axiom checks pass.
Declaration audit: [Box-mem_box.md](cleanup/Box-mem_box.md).

Publication verification for `Roth.mem_box`: full `lake build` session 29589 exited 0
(2586 jobs; `/private/tmp/roth-box-d02-full.log`); separate `lake build Roth.LeanEval`
session 68459 exited 0 (2585 jobs; `/private/tmp/roth-box-d02-leaneval.log`).

## Box declaration 3 checkpoint

`Roth.card_box` reviewed unchanged: original `simp [box]` remains the direct minimal
proof after compiled alternatives and library searches. Module build/full LSP,
independent proof/type/standard-axiom gates pass. Full `lake build` session 4764
and separate `lake build Roth.LeanEval` session 20469 both exited 0 (2586/2585 jobs);
logs `/private/tmp/roth-box-d03-{full,leaneval}.log`.
Declaration audit: [Box-card_box.md](cleanup/Box-card_box.md).

## User decision on Box assumptions and metadata

The user approved the recommendation: “Follow your recommendation.” Authorized scope:
remove verified unused positivity hypotheses and DecidableEq arguments from Box theorems,
preserve their conclusions, and adjust the two affected Index callsites. Apply each
verified removal at its sequential declaration checkpoint, with complete dependent builds.
No broader API additions or generalisations are authorized by this decision.
Copyright/license metadata stays unchanged because authoritative facts were not supplied;
the remaining header warning must stay explicit rather than being invented or suppressed.
The card_le_card_box DecidableEq drop is compiler-verified and will be the first application.

## Box declaration 4 checkpoint

`Roth.card_le_card_box`: with explicit user approval, removed unused DecidableEq σ
from the elaborated theorem type and used local classical reasoning. Conclusion and
explicit parameters unchanged. Composed cardinality inequality with equality directly
using `trans_eq`, with mathematical lambda `↦`. Target unused-instance warning fixed.
Module/full LSP, isolated proof/type/standard-axiom gates pass.
Declaration audit: [Box-card_le_card_box.md](cleanup/Box-card_le_card_box.md).

Final approved-source publication verification: full `lake build` session 11996 exited 0
(2586 jobs; `/private/tmp/roth-box-d04-full-approved.log`), separate
`lake build Roth.LeanEval` session 35385 exited 0 (2585 jobs;
`/private/tmp/roth-box-d04-leaneval-approved.log`). These runs supersede the earlier
proof-only full build 90150 and verify the selected generalized signature plus all callers.

## Box declaration 5 checkpoint

`Roth.weight` reviewed unchanged: the one-line normalized sum and its actual signature
(no DecidableEq argument) are appropriate for the existing API. Module/full LSP,
independent rfl/type/standard-axiom checks pass. Full `lake build` session 76138
and separate `lake build Roth.LeanEval` session 34164 exited 0 (2586/2585 jobs).
[Declaration audit](cleanup/Box-weight.md).

## Box declaration 6 checkpoint

`Roth.weight_nonneg`: removed approved unused DecidableEq σ; replaced the general
Finset sum proof with `Fintype.sum_nonneg`, removing its unused membership binder.
Conclusion/docstring unchanged. Target lint resolved, all module/fullLSP/isolated
type/standard-axiom checks pass. [Declaration audit](cleanup/Box-weight_nonneg.md).

Publication verification: full `lake build` session 67516 exited 0 (2586 jobs;
`/private/tmp/roth-box-d06-full.log`); separate `lake build Roth.LeanEval` session 32007
exited 0 (2585 jobs; `/private/tmp/roth-box-d06-leaneval.log`). All affected dependents pass.

## Box declaration 7 checkpoint

`Roth.weight_zero`: approved unused DecidableEq removed with a scoped omission;
original proof, conclusion, docstring, and simp attribute preserved. Module, complete
LSP, independent proof/type and standard-axiom gates pass.
[Declaration audit](cleanup/Box-weight_zero.md).

Publication verification: full `lake build` session 79655 exited 0 (2586 jobs;
`/private/tmp/roth-box-d07-full.log`); separate `lake build Roth.LeanEval` session 57725
exited 0 (2585 jobs; `/private/tmp/roth-box-d07-leaneval.log`). All affected dependents pass.

## Box declaration 8 checkpoint

`Roth.weight_add`: approved unused DecidableEq removed; all three original simp
arguments remain necessary and the proof is retained. Module, complete LSP, independent
proof/type and standard-axiom gates pass. [Declaration audit](cleanup/Box-weight_add.md).

Publication verification: full `lake build` session 60506 exited 0 (2586 jobs;
`/private/tmp/roth-box-d08-full.log`); separate `lake build Roth.LeanEval` session 78621
exited 0 (2585 jobs; `/private/tmp/roth-box-d08-leaneval.log`). All affected dependents pass.

## Box declaration 9 checkpoint

`Roth.weight_eq_zero_iff`: approved unused DecidableEq removed; strict positivity
retained with a compiled zero-denominator counterexample to its removal. Original
proof/docstring/conclusion retained. All target gates pass.
[Declaration audit](cleanup/Box-weight_eq_zero_iff.md).

Publication verification: full `lake build` session 2639 exited 0 (2586 jobs;
`/private/tmp/roth-box-d09-full.log`); separate `lake build Roth.LeanEval` session 25122
exited 0 (2585 jobs; `/private/tmp/roth-box-d09-leaneval.log`). All affected dependents pass.

## Box declaration 10 checkpoint

`Roth.weight_single`: approved unused DecidableEq removed and classical reasoning
localized to the proof. Packed its signature to one 97-character line; original simp
proof retained. All target gates pass. [Declaration audit](cleanup/Box-weight_single.md).

Publication verification: full `lake build` session 41056 exited 0 (2586 jobs;
`/private/tmp/roth-box-d10-full.log`); separate `lake build Roth.LeanEval` session 58453
exited 0 (2585 jobs; `/private/tmp/roth-box-d10-leaneval.log`). All affected dependents pass.

## Box declaration 11 checkpoint

`Roth.weight_le_card`: removed approved unused positivity hr and DecidableEq;
conclusion retained, proof lambda normalized. Updated the sole Index call by removing
its obsolete hr argument. Complete Index LSP passes with no errors; Index.index_le_card
now has an exposed unused hr warning, retained for that file’s dedicated cleanup.
All Box target gates pass. [Declaration audit](cleanup/Box-weight_le_card.md).

Publication verification: full `lake build` session 7727 exited 0 (2586 jobs;
`/private/tmp/roth-box-d11-full.log`); separate `lake build Roth.LeanEval` session 44525
exited 0 (2585 jobs; `/private/tmp/roth-box-d11-leaneval.log`). All affected dependents pass.

## Box declaration 12 checkpoint

`Roth.weight_mul_left`: removed approved unused positivity hl and DecidableEq;
equality retained, lambda normalized. Updated the sole Index rewrite by deleting
its obsolete hl argument. Complete Index LSP passes with no errors; selected proof
and zero-scale probe compile. All target gates pass.
[Declaration audit](cleanup/Box-weight_mul_left.md).

Publication verification: full `lake build` session 84040 exited 0 (2586 jobs;
`/private/tmp/roth-box-d12-full.log`); separate `lake build Roth.LeanEval` session 7710
exited 0 (2585 jobs; `/private/tmp/roth-box-d12-leaneval.log`). All affected dependents pass.

## Box declaration 13 checkpoint

`Roth.weight_le_degree_div`: removed approved unused DecidableEq, packed the
signature, and replaced manual cast/positivity plumbing with gcongr and hr.
Necessary hm/hr retained with compiled counterexamples to their removal.
All target gates pass. [Declaration audit](cleanup/Box-weight_le_degree_div.md).

Publication verification: full `lake build` session 46898 exited 0 (2586 jobs;
`/private/tmp/roth-box-d13-full.log`); separate `lake build Roth.LeanEval` session 24692
exited 0 (2585 jobs; `/private/tmp/roth-box-d13-leaneval.log`). All affected dependents pass.

## Box declaration 14 checkpoint

`Roth.weight_mapDomain`: removed both approved unused DecidableEq assumptions;
replaced manual reindexing with Mathlib’s generic injective mapDomain sum theorem.
Declaration 6 → 4 lines; conclusion, injectivity and docs preserved. All target gates
pass; only the user-preserved Box header warning remains.
[Declaration audit](cleanup/Box-weight_mapDomain.md).

Publication verification: full `lake build` session 56521 exited 0 (2586 jobs;
`/private/tmp/roth-box-d14-full.log`); separate `lake build Roth.LeanEval` session 76596
exited 0 (2585 jobs; `/private/tmp/roth-box-d14-leaneval.log`). All affected dependents pass.


## Box final file-level checkpoint

All 14 dedicated declaration audits and sequential publications are complete. Final scope
consolidation preserves all 14 elaborated types/axioms byte-for-byte. Fresh independent
simplify review found two redundant direct imports; both removed and validated. Final
source 128 → 126 lines, declaration lines 41 → 39, all 14 declarations retained, all original
comments/docs preserved. Final module 91862/full 88871/LeanEval 70480 exited 0; complete LSP
has only the agreed metadata warning. Actual profiling 3955 passed all 14 declarations,
maximum 196.39ms, with no limit changes or source instrumentation. Project-wide rename
pass remains scheduled after all files; Box queues none. [Final report](cleanup/Box-final.md).

The Box worker stops at this file boundary and releases source/report/shared-log/Git
ownership to the orchestrator for dispatch of the next fresh Wronskian worker.

## Wronskian declaration 1 checkpoint

`Roth.wronskianMatrix`: Normalized lambda arrow and removed redundant explicit Fin-to-Nat ascription; original definition verified by rfl, API retained. [Full declaration audit](cleanup/Wronskian-wronskianMatrix.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session77119 exit0; separate `lake build Roth.LeanEval` session65973 exit0. Logs `/private/tmp/roth-wronskian-d1-full.log` and `...-leaneval.log`.

## Wronskian declaration 2 checkpoint

`Roth.wronskian`: Definition already minimal, retained unchanged; complete dedicated audit and definitional equality/type checks passed. [Full declaration audit](cleanup/Wronskian-wronskian.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session73364 exit0; separate `lake build Roth.LeanEval` session97956 exit0. Logs `/private/tmp/roth-wronskian-d2-full.log` and `...-leaneval.log`.

## Wronskian declaration 3 checkpoint

`Roth.wronskian_eq_zero_of_not_linearIndependent`: Packed signature, normalized two lambdas and removed redundant Nat ascription; direct determinant proof and contract preserved,8lines retained. [Full declaration audit](cleanup/Wronskian-wronskian_eq_zero_of_not_linearIndependent.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session22706 exit0; separate `lake build Roth.LeanEval` session1146 exit0. Logs `/private/tmp/roth-wronskian-d3-full.log` and `...-leaneval.log`.

## Wronskian declaration 4 checkpoint

`Roth.det_choose_eq`: Oriented the scaling equality toward the transposed evaluation matrix, removed redundant h2 and normalized lambdas; declaration16→13lines, statement preserved. [Full declaration audit](cleanup/Wronskian-det_choose_eq.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session6371 exit0; separate `lake build Roth.LeanEval` session37787 exit0. Logs `/private/tmp/roth-wronskian-d4-full.log` and `...-leaneval.log`.

## Wronskian declaration 5 checkpoint

`Roth.sum_range_card_le_sum`: Packed signature to100codepoints and normalized lambdas/ascription;11→10lines. Verified Mathlib replacement queued for Phase5a, public API unchanged. [Full declaration audit](cleanup/Wronskian-sum_range_card_le_sum.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session4157 exit0; separate `lake build Roth.LeanEval` session51137 exit0. Logs `/private/tmp/roth-wronskian-d5-full.log` and `...-leaneval.log`.

## Wronskian declaration 6 checkpoint

`Roth.coeff_prod_of_natDegree_le'`: Simplified the inserted-bound premise once and reused projections, eliminating repeated membership lambdas;12→11lines, exact signature preserved. [Full declaration audit](cleanup/Wronskian-coeff_prod_of_natDegree_le.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session84949 exit0; separate `lake build Roth.LeanEval` session56529 exit0. Logs `/private/tmp/roth-wronskian-d6-full.log` and `...-leaneval.log`.

## Wronskian declaration 7 checkpoint

`Roth.sum_range_le_sum_of_injective`: Replaced single-use h/rwa with direct simpa and hd.injOn, removed unnecessary classical;6→4lines with original contract retained. [Full declaration audit](cleanup/Wronskian-sum_range_le_sum_of_injective.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session28169 exit0; separate `lake build Roth.LeanEval` session83466 exit0. Logs `/private/tmp/roth-wronskian-d7-full.log` and `...-leaneval.log`.

## Wronskian declaration 8 checkpoint

`Roth.coeff_wronskian_of_natDegree_injective`: Eliminated hD through direct sum rewrites and replaced final simp-only/ring with terminal simp;29→22lines,18bodylines. Both unused hypotheses retained pending explicit user decision on compiled removal proposal and sole caller repair. [Full declaration audit](cleanup/Wronskian-coeff_wronskian_of_natDegree_injective.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session10237 exit0; separate `lake build Roth.LeanEval` session38808 exit0. Logs `/private/tmp/roth-wronskian-d8-full.log` and `...-leaneval.log`.

## Wronskian declaration 9 checkpoint

`Roth.wronskian_ne_zero_of_natDegree_injective`: Direct simpa from coefficient identity replaces h1/rewrite chain, signature packed and redundant cast removed;8→5lines. Final-source closure rerun after premature freeze, earlier full36477 not counted. [Full declaration audit](cleanup/Wronskian-wronskian_ne_zero_of_natDegree_injective.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session80038 exit0; separate `lake build Roth.LeanEval` session58989 exit0. Logs `/private/tmp/roth-wronskian-d9-full-final.log` and `...-leaneval.log`.

## Wronskian declaration 10 checkpoint

`Roth.wronskian_update_sub_smul`: Composed determinant congruence with Mathlib column-operation invariance and used one terminal conditional simp;10→7lines, signature/documentation unchanged. [Full declaration audit](cleanup/Wronskian-wronskian_update_sub_smul.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session21216 exit0; separate `lake build Roth.LeanEval` session9301 exit0. Logs `/private/tmp/roth-wronskian-d10-full.log` and `...-leaneval.log`.

## Wronskian declaration 11 checkpoint

`Roth.span_range_update_sub_le`: Reduced span-membership proof to structural rewrites and aesop;10→5lines, exact signature unchanged. Compiled Mathlib span-update equality replacement in sole caller queued for Phase5a helper deletion. [Full declaration audit](cleanup/Wronskian-span_range_update_sub_le.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session15006 exit0; separate `lake build Roth.LeanEval` session18366 exit0. Logs `/private/tmp/roth-wronskian-d11-full.log` and `...-leaneval.log`.

## Wronskian declaration 12 checkpoint

`Roth.linearIndependent_update_sub_smul`: Replaced inverse-update/span machinery with direct Mathlib span preservation,11→6lines and8→3bodylines; signature/docs unchanged. Private span helper now unused, scheduled for Phase5a deletion. [Full declaration audit](cleanup/Wronskian-linearIndependent_update_sub_smul.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session37876 exit0; separate `lake build Roth.LeanEval` session72281 exit0. Logs `/private/tmp/roth-wronskian-d12-full.log` and `...-leaneval.log`.

## Wronskian declaration 13 checkpoint

`Roth.sum_natDegree_update_lt`: Reused updated-family independence for nonzero cancellation, inlined scalar nonzero fact and simplified sum comparison;23→19lines, original statement/docs retained. [Full declaration audit](cleanup/Wronskian-sum_natDegree_update_lt.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session18116 exit0; separate `lake build Roth.LeanEval` session13785 exit0. Logs `/private/tmp/roth-wronskian-d13-full.log` and `...-leaneval.log`.

## Wronskian declaration 14 checkpoint

`Roth.wronskian_ne_zero_of_linearIndependent`: Packed induction branch heading and normalized lambda;11→10lines, original signature/docs and degree-descent strategy preserved. [Full declaration audit](cleanup/Wronskian-wronskian_ne_zero_of_linearIndependent.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session41757 exit0; separate `lake build Roth.LeanEval` session34353 exit0. Logs `/private/tmp/roth-wronskian-d14-full.log` and `...-leaneval.log`.

## Wronskian declaration 15 checkpoint

`Roth.wronskian_eq_zero_iff`: Replaced manual implication lambda with imp_not_comm.mp;4lines retained, exact theorem type/docs unchanged. All15 original declaration audits complete; final file phases pending. [Full declaration audit](cleanup/Wronskian-wronskian_eq_zero_iff.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session76389 exit0; separate `lake build Roth.LeanEval` session69359 exit0. Logs `/private/tmp/roth-wronskian-d15-full.log` and `...-leaneval.log`.


## Wronskian final file checkpoint

Completed all15 original audits and final phases; two private wrappers replaced with Mathlib,
five redundant imports removed by independent review, source271→219 lines. Final gates:
module76381, full10167, LeanEval82516, compatibility62603 all exit0; complete LSP zero errors,
three explicit existing warnings. Actual profiling16927 exit0: maximum647.20ms, all13 retained
declarations below1000ms. No pending source edit; coefficient-hypothesis proposal still awaiting
user decision. Final reports prepared; Taylor next. Overall55/264 original declarations audited.

## Taylor declaration 1 checkpoint

`MvPolynomial.taylor`: Normalized the mathematical lambda arrow; original definition verified by rfl, exact public API/docstring preserved. File-level project imports alphabetized. [Dedicated audit](cleanup/Taylor-taylor.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session54303 exit0; separate `lake build Roth.LeanEval` session6076 exit0. Frozen source SHA256 `91e0b1f92db86dacca1c06b0ae8c3e87793d5a27ffafc3070db8074caa2d40ae`. Logs `/private/tmp/roth-taylor-d01-full.log` and `...-leaneval.log`.

## Taylor declaration 2 checkpoint

`MvPolynomial.taylor_apply`: Normalized the mathematical lambda arrow; retained the minimal rfl proof, original elaborated type and docstring. [Dedicated audit](cleanup/Taylor-taylor_apply.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session35545 exit0; separate `lake build Roth.LeanEval` session40919 exit0. Frozen source SHA256 `b09b1665ded220e46380fb7174a024f0f5d12144caafdb60a25f107d0488f56a`. Logs `/private/tmp/roth-taylor-d02-full.log` and `...-leaneval.log`.

## Taylor declaration 3 checkpoint

`MvPolynomial.taylor_X`: Replaced simplification with direct Mathlib aeval_X term,2 to1lines; original statement, simp attribute and docstring preserved. [Dedicated audit](cleanup/Taylor-taylor_X.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session74936 exit0; separate `lake build Roth.LeanEval` session95276 exit0. Frozen source SHA256 `79a3459730c972e438301e511ded297cad4e10edcef816302ad1dc21cfbb5ad1`. Logs `/private/tmp/roth-taylor-d03-full.log` and `...-leaneval.log`.

## Taylor declaration 4 checkpoint

`MvPolynomial.taylor_C`: Replaced definition-unfolding simp with direct Mathlib algHom_C term,2 to1lines; original statement, simp attribute and docstring preserved. [Dedicated audit](cleanup/Taylor-taylor_C.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session4113 exit0; separate `lake build Roth.LeanEval` session18089 exit0. Frozen source SHA256 `57ed0bd46f1e97a504e63e53fb570c98045df68530f25bd8f48287ed2604ff6a`. Logs `/private/tmp/roth-taylor-d04-full.log` and `...-leaneval.log`.

## Taylor declaration 5 checkpoint

`MvPolynomial.taylor_monomial`: Replaced simp and definition unfolding with direct Mathlib aeval_monomial term; mathematical lambda normalized,3lines retained, original contract/docstring preserved. [Dedicated audit](cleanup/Taylor-taylor_monomial.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session63285 exit0; separate `lake build Roth.LeanEval` session31201 exit0. Frozen source SHA256 `a913c9258bdcb0630d0d3398f34626f52c2d9f9504a7077e443ef2f24f1090a4`. Logs `/private/tmp/roth-taylor-d05-full.log` and `...-leaneval.log`.

## Taylor declaration 6 checkpoint

`MvPolynomial.coeff_aeval_X_mul`: Direct evaluation expansion and Finsupp erase cancellation replace two intermediate proofs; single-use inequality inlined,24 to18lines, exact statement retained. [Dedicated audit](cleanup/Taylor-coeff_aeval_X_mul.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session53572 exit0; separate `lake build Roth.LeanEval` session61138 exit0. Frozen source SHA256 `f4a686acc2e188a3bea162eb6bff0afd5079cd162d2297afbe1ce2b0d830529a`. Logs `/private/tmp/roth-taylor-d06-full.log` and `...-leaneval.log`.

## User-approved hypothesis amendment (2026-10-15)

The user approved removal of both unused `hφ`/`hd` arguments from
`coeff_wronskian_of_natDegree_injective`, preserving its name and conclusion,
and the minimal sole-caller update to `(φ := φ)`. A fresh narrow worker applied exactly
those two replacements. All other source, definitions, proof, documentation and the
nonvanishing caller's hypotheses remain byte-identical. Earlier pending-proposal
statements in historical checkpoints are superseded by this approval and implementation.

Wronskian source is now271→218lines,13retained declarations; the original audit count
remains15. Module28780 exit0, complete LSP zeroerrors and only the user-preserved header
warning, independent pre-target theorem/caller compilation and standard-axiom checks pass.
Actual profiling5470 exit0: all13 below750ms, maximum586.13ms; caller457.33ms.
Full `lake build` session30588 exit0 (2587jobs), followed by separate
`lake build Roth.LeanEval` session6721 exit0 (2586jobs). The full result was recovered
successfully after a usage interruption; both source hashes stayed unchanged.
Logs `/private/tmp/roth-wronskian-approved-{full,leaneval}.log`.
Frozen Wronskian SHA256 `b4f0c0db36bcbd81983f5a38c137dcefdf57bce18e12445e8241689a8abf888e`.
[Full amendment evidence](cleanup/Wronskian-approved-hypotheses.md). No API proposal remains pending.
This amendment does not increment the264original-declaration tally; Taylor remains6/20,
overall61/264. Taylor7 resumes after this separate publication checkpoint.

## Taylor declaration 7 checkpoint

`MvPolynomial.hasseCoeff_single_add_eq`: Used Mathlib mul_prod_erase and support_erase to remove explicit disjointness and case splitting; packed unchanged signature,16 to9lines. [Dedicated audit](cleanup/Taylor-hasseCoeff_single_add_eq.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session6797 exit0; separate `lake build Roth.LeanEval` session18199 exit0. Frozen source SHA256 `72a52b08db494fd445a13c5716fc1afd32fbf315b1e41dccffe81f230ef1f7bd`. Logs `/private/tmp/roth-taylor-d07-full.log` and `...-leaneval.log`.

## Taylor declaration 8 checkpoint

`MvPolynomial.prod_pow_single_add_tsub`: Terminal simp replaces rewrite/congr/exact assembly with local single_tsub exclusion; lambda syntax and signature packed,11 to8lines, original contract preserved. [Dedicated audit](cleanup/Taylor-prod_pow_single_add_tsub.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session26690 exit0; separate `lake build Roth.LeanEval` session78586 exit0. Frozen source SHA256 `58a982948ba48df089ea5e4a00e8050fb00566e381e9a942279484ac88e0818e`. Logs `/private/tmp/roth-taylor-d08-full.log` and `...-leaneval.log`.

## Taylor declaration 9 checkpoint

`MvPolynomial.coeff_taylor`: Separated monomial expansion into two private helpers; headline33 to3bodylines, original public contract/docs preserved, source net+2lines. New helpers await fresh dedicated audits. [Dedicated audit](cleanup/Taylor-coeff_taylor.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session19265 exit0; separate `lake build Roth.LeanEval` session62727 exit0. Frozen source SHA256 `339ca8621ef76a233dab2c5f86002e6a1016b9116616266e78b9a5d311177b39`. Logs `/private/tmp/roth-taylor-d09-full.log` and `...-leaneval.log`.

## Added helper1 checkpoint

Fresh GPT-6 Astra Medium worker independently audited `coeff_taylor_monomial_single_add_aux`
under the user-requested model setting. Removed redundant classical and a redundant terminal
simp argument;19→18declarationlines, exact signature retained. All24audit/42rules/search/
generalisation/width/inequality/checklist artifacts and module/completeLSP/isolatedproof/type/
standardaxiom gates pass. [Dedicated audit](cleanup/Taylor-coeff_taylor_monomial_single_add_aux.md).
Full `lake build` session38813 and separate `lake build Roth.LeanEval` session94812 exit0
(2587/2586jobs); `/private/tmp/roth-taylor-newhelper01-{full,leaneval}.log`.
Frozen source SHA256 `9a4189e83c942dbf021d9c6f831a4d4a17384e5b7ad8a88e1ded62dbba73cdd8`.
Original tally unchanged: Taylor9/20, overall64/264. Second new helper audit remains pending.

## Added helper2 checkpoint

Fresh GPT-6 Astra Medium worker independently audited `coeff_taylor_monomial_aux`.
Existing hasseDeriv_C replaces manual constant-case coefficient expansion and vanishing;
11→10declarationlines, exact signature retained. All24audit/42rules/search/generalisation/
width/inequality/checklist artifacts and module/completeLSP/isolatedproof/type/standardaxiom
gates pass. [Dedicated audit](cleanup/Taylor-coeff_taylor_monomial_aux.md).
Full `lake build` session74901 and separate `lake build Roth.LeanEval` session24217 exit0
(2587/2586jobs); `/private/tmp/roth-taylor-newhelper02-{full,leaneval}.log`.
Frozen source SHA256 `61807d7fe836eb95dbcea48055b0c9a5f5747d3c98b8d15f0d82fe33aee3f81d`.
Both added helpers now have fresh dedicated audits/publication gates; original tally remains
Taylor9/20, overall64/264. Original declaration10 resumes next.
LeanSearch recovered in this audit and returned a verified univariate partial match; this
supersedes the earlier service-unavailable status for future searches without claiming an
environment repair.

## Taylor declaration 10 checkpoint

`MvPolynomial.eval_taylor`: Direct Mathlib evaluation composition replaces induction; lambda arrow normalized,3 declaration lines retained, exact public contract and docstring preserved. [Dedicated audit](cleanup/Taylor-eval_taylor.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session26144 exit0; separate `lake build Roth.LeanEval` session9704 exit0. Frozen source SHA256 `fbd691573b1e1fa3dd2c4f33449095583791028ee6cbd25a8d92df2175e9ab39`. Logs `/private/tmp/roth-taylor-d10-full.log` and `...-leaneval.log`.

## Taylor declaration 11 checkpoint

`MvPolynomial.taylor_taylor`: Direct Mathlib algebra evaluation composition replaces induction; lambda normalized, exact public contract and documentation retained. [Dedicated audit](cleanup/Taylor-taylor_taylor.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session87659 exit0; separate `lake build Roth.LeanEval` session70984 exit0. Frozen source SHA256 `c3b13e052d8ffa6af70404bf29d2853cce67a99b36cd0dc4a8584f5bfbf23020`. Logs `/private/tmp/roth-taylor-d11-full.log` and `...-leaneval.log`.

## Taylor declaration 12 checkpoint

`MvPolynomial.taylor_zero`: Direct Mathlib identity-evaluation simplification replaces induction; equivalent lambda notation normalized, original public API and docstring preserved. [Dedicated audit](cleanup/Taylor-taylor_zero.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session11614 exit0; separate `lake build Roth.LeanEval` session44120 exit0. Frozen source SHA256 `a2f43a6a92cc7e8cee595b4fdb1047638cc7f8a9d1d031e050f72a95f086a6af`. Logs `/private/tmp/roth-taylor-d12-full.log` and `...-leaneval.log`.

CI follow-up: the root agent inspected [run 38848241891](https://github.com/SmwYin/Roth/actions/runs/38848241891) at `5496d75`: Lean action succeeded; the Pages deployment failed with HTTP400 because it overlapped the newer `2c552b3` deployment. [Newer run 38849121428](https://github.com/SmwYin/Roth/actions/runs/38849121428) completed successfully. This was a deployment overlap, not a Lean regression; no rerun or workflow change was needed.

## Taylor declaration 13 checkpoint

`MvPolynomial.taylor_map`: Evaluation-map naturality replaces polynomial induction; equivalent lambda notation normalized, exact public API and docs retained. [Dedicated audit](cleanup/Taylor-taylor_map.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session53057 exit0; separate `lake build Roth.LeanEval` session18619 exit0. Frozen source SHA256 `d4a821b4ee428a5e8b052cb7a6cd0a62a9830b3fdb5a3d78557b86bd29d2dd74`. Logs `/private/tmp/roth-taylor-d13-full.log` and `...-leaneval.log`.

User model preference update: all new declaration/helper/review workers now use GPT-6.1 Sol Medium with fresh context. The already-running Taylor13 Astra Medium worker finished its existing audit; no model switch is claimed for that worker. Required gates remain unchanged, with concise output and no unchanged status updates.

## Taylor declaration 14 checkpoint

`MvPolynomial.taylor_rename`: Direct substitution composition replaces induction; exact public signature and documentation unchanged. [Dedicated audit](cleanup/Taylor-taylor_rename.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session21806 exit0; separate `lake build Roth.LeanEval` session71085 exit0. Frozen source SHA256 `4cd871acc4a0ad26ceba2c01bef9ee5c88e0f5117254a50d24a895b56af32f7a`. Logs `/private/tmp/roth-taylor-d14-full.log` and `...-leaneval.log`.

## Taylor declaration 15 checkpoint

`MvPolynomial.degreeOf_taylor_le`: Retained direct coefficient-vanishing degree proof after search; normalized two mathematical lambda arrows, exact signature and docs preserved. [Dedicated audit](cleanup/Taylor-degreeOf_taylor_le.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session9544 exit0; separate `lake build Roth.LeanEval` session22563 exit0. Frozen source SHA256 `1f69c55d06c8b562930bb9bbc90e9ab3a676f2491d6ddbf4f8dd4c08b8fe3de8`. Logs `/private/tmp/roth-taylor-d15-full.log` and `...-leaneval.log`.

## Taylor declaration 16 checkpoint

`MvPolynomial.taylor_neg_taylor`: Retained minimal composition-cancellation simp; normalized lambda and packed signature, exact mathematical type and docstring preserved. [Dedicated audit](cleanup/Taylor-taylor_neg_taylor.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session58028 exit0; separate `lake build Roth.LeanEval` session88498 exit0. Frozen source SHA256 `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`. Logs `/private/tmp/roth-taylor-d16-full.log` and `...-leaneval.log`.

## Taylor declaration 17 checkpoint

`MvPolynomial.taylor_injective`: Retained direct LeftInverse.injective proof after tested alternatives; no source change, complete dedicated audit and exact API verification. [Dedicated audit](cleanup/Taylor-taylor_injective.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session30998 exit0; separate `lake build Roth.LeanEval` session69947 exit0. Frozen source SHA256 `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`. Logs `/private/tmp/roth-taylor-d17-full.log` and `...-leaneval.log`.

## Taylor declaration 18 checkpoint

`MvPolynomial.taylor_eq_zero_iff`: Retained minimal injectivity eq_iff term after compiled alternatives; no source change, exact public simp API and docs verified. [Dedicated audit](cleanup/Taylor-taylor_eq_zero_iff.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session21654 exit0; separate `lake build Roth.LeanEval` session88267 exit0. Frozen source SHA256 `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`. Logs `/private/tmp/roth-taylor-d18-full.log` and `...-leaneval.log`.

## Taylor declaration 19 checkpoint

`MvPolynomial.eq_sum_box_hasseDeriv`: Consolidated coefficient rewriting into one squeezed simp, reducing headline proof16 to15 lines including by; lambdas normalized, no helper or public contract change. [Dedicated audit](cleanup/Taylor-eq_sum_box_hasseDeriv.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session8153 exit0; separate `lake build Roth.LeanEval` session30826 exit0. Frozen source SHA256 `eda896cd346e776d923237cdc4235045d1dd2e4fe32a8d039f561ca6068221a6`. Logs `/private/tmp/roth-taylor-d19-full.log` and `...-leaneval.log`.

## Taylor declaration 20 checkpoint

`MvPolynomial.eval_eq_sum_box`: Applied evaluation congruence directly with simpa; body2 to1lines and signature packed, exact public type/docs preserved. [Dedicated audit](cleanup/Taylor-eval_eq_sum_box.md). Module, complete LSP, isolated type/axiom and diff gates pass. Publication validation: full `lake build` session80735 exit0; separate `lake build Roth.LeanEval` session37852 exit0. Frozen source SHA256 `4878106187d61fe102f4f1b52582772cbc6938085e3e1e1845843279cfd356de`. Logs `/private/tmp/roth-taylor-d20-full.log` and `...-leaneval.log`.

## Taylor independent simplify checkpoint

Fresh GPT-6.1 Sol Medium review found one compiled degree-bound proof improvement, now applied: terminal simp replaces rw/contradiction,3→2bodylines. [Review](cleanup/Taylor-simplify.md). Final source218lines, original20/20 and overall75/264 unchanged. Module87739/full91300/separateLeanEval69418 exit0, complete LSP only preserved header warning, exact17publicconstant compatibility session7752 exit0. Frozen SHA256 `31af75afd28f840ddee51978509ba63b28536aa84bba56dc047df2aa4b23fbdc`. Profiling and final report remain pending.

## Taylor final phases complete

All20 originals and2 added helpers complete; overall75/264. [Final report](cleanup/Taylor-final.md) contains cumulative gates, exact original-public compatibility, all22 profiling timings, independent review and artifact sweep. Final source SHA256 `31af75afd28f840ddee51978509ba63b28536aa84bba56dc047df2aa4b23fbdc`;218lines. Post-review full91300 and separateLeanEval69418 exit0, complete source/caller diagnostics no errors, profile24788 exit0 maximum672.30ms, post-profile module42517 exit0. Header metadata remains the explicit user-preserved limitation. No Taylor proposal/rename/refactor remains pending. Prior pending final-phase notes above are historical and superseded. Worker releases Taylor/shared-log/Git ownership after final publication; no CoeffNorm work started.

## CoeffNorm declaration1 checkpoint

`Roth.normOne`: retained the one-line coefficient norm definition unchanged after full dedicated audit; file-level imports alphabetized. [Dedicated audit](cleanup/CoeffNorm-normOne.md), [initial file audit](cleanup/CoeffNorm.md). Module89974 exit0, complete LSP noerrors, independent originaltype/value and standardaxiom gates pass. Frozen source SHA256 `1290a45f7dbbe5f2a37df1dfd7cb9718884fad6f1d6ae903c0afcf7dbbee9c5b`; source320→321lines from import grouping. Full `lake build` session25646 exit0,2587jobs; separate `lake build Roth.LeanEval` session18016 exit0,2586jobs. Logs `/private/tmp/roth-coeffnorm-d01-{full,leaneval}.log`. [Concrete API proposal](cleanup/CoeffNorm-api-proposal.md) compiled46719 exit0: four unused publicDecidableEq removals and unused hC removal await userdecision, not applied. Overall76/264original declarations audited; CoeffNorm1/26.

## CoeffNorm declaration2 checkpoint

`Roth.normOne_nonneg`: normalized mathematical lambda; retained direct sum_nonneg term and exact publictype/docstring,2→2lines. [Dedicated audit](cleanup/CoeffNorm-normOne_nonneg.md). Module1883 exit0; complete finalLSP noerrors; independent CLI originaltype/reproof/standardaxioms session88771 exit0. Full `lake build` then separate `lake build Roth.LeanEval` both exit0 in sequential publication session18176, frozen SHA256 `602e34191b8255ce65c19e1217e7cfe653f3516fd4a439371f60b771f45c2a57` unchanged through both. Logs `/private/tmp/roth-coeffnorm-d02-{full,leaneval}.log`. All24audit/42rules/5search/11checks complete. CoeffNorm2/26,overall77/264; existing APIproposal remains pending, source signatures unchanged.

## CoeffNorm declaration3 checkpoint

`Roth.normOne_eq_sum_of_support_subset`: normalized lambda; retained direct Finset.sum_subset proof, exact publictype/docstring,3→3lines. [Dedicated audit](cleanup/CoeffNorm-normOne_eq_sum_of_support_subset.md). Module exit0, complete finalLSP noerrors, independent CLI originaltype/reproof/standardaxioms exit0; all24audit/42rules/5search/11checks pass. Full `lake build` followed by separate `lake build Roth.LeanEval` both exit0 in session89274, source SHA256 `d6d990fb089ca49ae94d876a531e7b2237d84b3fb83400f815effd77571ef538` unchanged. Logs `/private/tmp/roth-coeffnorm-d03-{full,leaneval}.log`. CoeffNorm3/26,overall78/264.

## CoeffNorm declaration4 checkpoint

`Roth.normOne_monomial`: removed33redundant proof-ascription characters;4→4declarationlines excluding preserved docstring, exact publictype retained. [Dedicated audit](cleanup/CoeffNorm-normOne_monomial.md). Module84288 exit0, completefinalLSP noerrors; independent CLI originaltype/reproof/standardaxioms91378 exit0. All24audit/42rules/5search/11checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session36875 exit0; source SHA256 `62cc00913634a7662c2313a3c36a98f0891f663db3577869a49ff676bbd4e1e5` unchanged. Logs `/private/tmp/roth-coeffnorm-d04-{full,leaneval}.log`. CoeffNorm4/26,overall79/264.

## CoeffNorm declaration5 checkpoint

`Roth.normOne_zero`: retained standard one-tactic simp proof,2→2lines, originalsignature/simpattribute/docstring unchanged after compiledalternatives. [Dedicated audit](cleanup/CoeffNorm-normOne_zero.md). Actualmodulebuild exit0, completefinalLSP noerrors; independent originaltype/non-selfreproof/simpbehavior/standardaxioms pass. All24audit/42rules/5search/11checks complete. Full `lake build` then separate `lake build Roth.LeanEval` session67751 exit0, SHA256 `62cc00913634a7662c2313a3c36a98f0891f663db3577869a49ff676bbd4e1e5` unchanged. Logs `/private/tmp/roth-coeffnorm-d05-{full,leaneval}.log`. CoeffNorm5/26,overall80/264.

## CoeffNorm declaration6 checkpoint

`Roth.abs_coeff_le_normOne`: direct Mathlib Finsupp.single_eval_le_sum replaces supportcases,6→3declarationlines; exact publictype/docs preserved. [Dedicated audit](cleanup/CoeffNorm-abs_coeff_le_normOne.md). Module71860 exit0; completefinalLSP noerrors; fresh CLI originaltype/independentnonselfreproof/standardaxioms33658 exit0. All24audit/42rules/5search/11checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session9002 exit0; source SHA256 `29e747bec2da1d802c9dea2a034b17dfe1db36b793f966b7007c46c3529e93bc` unchanged. Logs `/private/tmp/roth-coeffnorm-d06-{full,leaneval}.log`. CoeffNorm6/26,overall81/264.

## CoeffNorm declaration7 checkpoint

`Roth.normOne_add_le`: normalized mathematical lambda and retained direct supportunion triangleinequality proof,7→7declarationlines, exact publictype/docs preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_add_le.md). Module10663 exit0, completefinalLSP noerrors, fresh CLI originaltype/nonselfreproof/standardaxioms36739 exit0. All24audit/42rules/5search/11checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session55968 exit0; SHA256 `1c67627438e2ed4ecec1e2024e1d517b23c235fc3b3f44d409394477fc5a818c` unchanged. Logs `/private/tmp/roth-coeffnorm-d07-{full,leaneval}.log`. CoeffNorm7/26,overall82/264.

## CoeffNorm declaration 8 checkpoint

`Roth.normOne_neg`: removed redundant support_neg simp argument; 2→2 declaration lines, exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_neg.md). Module62505 exit0, complete final LSP no errors, fresh CLI original type/nonself reproof/standard axioms75775 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session54826 exit0; SHA256 `12422f3bbb5a494633eede6148bc384c1c3eff739be1aa3c00181dabea5d7423` unchanged. Logs `/private/tmp/roth-coeffnorm-d08-{full,leaneval}.log`. CoeffNorm8/26, overall83/264.

## CoeffNorm declaration 9 checkpoint

`Roth.normOne_sum_le`: retained direct Mathlib subadditivity term, 3→3 declaration lines, exact public API/docs preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_sum_le.md). Module73402 exit0, complete final LSP no errors, fresh CLI original-type assignment/independent induction reproof/standard axioms62550 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session90598 exit0; frozen SHA256 `12422f3bbb5a494633eede6148bc384c1c3eff739be1aa3c00181dabea5d7423` unchanged. Logs `/private/tmp/roth-coeffnorm-d09-{full,leaneval}.log`. The leaf's optional wrapper-deletion idea is closed under the explicit public-API preservation policy; no required caller benefit or requested deletion warrants another approval question. CoeffNorm9/26, overall84/264.

## CoeffNorm declaration 10 checkpoint

`Roth.normOne_mul_le`: Mathlib MvPolynomial.mul_def replaces manual monomial-product expansion; body10→5 and declaration12→7 lines. Public signature (including pending DecidableEq), docs and mathematical result preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_mul_le.md). Module28226 exit0; complete final LSP no errors, six explicit existing warnings. Fresh CLI original-type assignment/nonself reproof/standard axioms30038 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session67825 exit0; SHA256 `7e5a4e7491daccb1e05fc20d375fc5bc64f27abc581fbb79cf97595b491e589a` unchanged. Logs `/private/tmp/roth-coeffnorm-d10-{full,leaneval}.log`. CoeffNorm10/26, overall85/264.

## CoeffNorm declaration 11 checkpoint

`Roth.normOne_prod_le`: direct Finset.le_prod_of_submultiplicative_of_nonneg replaces induction; declaration8→4 lines. Original public type (including pending DecidableEq) and docstring preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_prod_le.md). Module80686 exit0; complete final LSP no errors; native exact original-type assignment/independent induction reproof/standard axioms pass without stale imports. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session31438 exit0; SHA256 `76c5827a7b9a0b520e09b1012d73021c26b4a68d2c1d9d749e36b5712989b13a` unchanged. Logs `/private/tmp/roth-coeffnorm-d11-{full,leaneval}.log`. CoeffNorm11/26, overall86/264.

## CoeffNorm declaration 12 checkpoint

`Roth.normOne_le_card_mul`: terminal simpa consolidates rewrite/term proof; declaration4→3 lines, original public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_le_card_mul.md). Module81998 exit0, complete final LSP no errors, fresh CLI original-type assignment/nonself reproof/standard axioms54979 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session61558 exit0; SHA256 `3d35d122b0dd0a330e7a1f78a76ed60d992234ced16013aaeb34c249f87f392c` unchanged. Logs `/private/tmp/roth-coeffnorm-d12-{full,leaneval}.log`. Optional support-local hB restatement closed under public-API preservation, no required pending action. CoeffNorm12/26, overall87/264.

## CoeffNorm declaration 13 checkpoint

`Roth.normOne_det_le`: direct sign-case simpa removes intermediate show/rw equality; declaration11→10 and body8→7 lines. Exact public signature/docs preserved; unused DecidableEq and hC remain pending scoped approval. [Dedicated audit](cleanup/CoeffNorm-normOne_det_le.md). Module95270 exit0, complete frozen-source LSP no errors, fresh CLI original-type assignment/nonself reproof/standard axioms exit0. All24 audit/42 rules/5 searches/11 checks pass; all stalled probes terminated, no orphan process. Sequential full `lake build` and separate `lake build Roth.LeanEval` session12002 exit0; SHA256 `539842bb50df433db0d3ee8d8f366892b352427103407526700baa23ae5cd33f` unchanged. Logs `/private/tmp/roth-coeffnorm-d13-{full,leaneval}.log`. CoeffNorm13/26, overall88/264.

## CoeffNorm declaration 14 checkpoint

`Roth.abs_coeff_hasseDeriv_le`: explicit cast rewrite chain replaces separate rewrite/push_cast/rewrite; declaration12→10, body9→7 lines, exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-abs_coeff_hasseDeriv_le.md). Module31196 exit0; complete final LSP no errors, fresh CLI original-type assignment/nonself reproof/standard axioms30662 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session24717 exit0; SHA256 `e69bf642ea61b7df2ae8ea75e5b379a66aa58a3da95b0a9b8ea4c9bc21231b47` unchanged. Logs `/private/tmp/roth-coeffnorm-d14-{full,leaneval}.log`. An unnecessary repeated leaf baseline build and incorrectly named LeanEval target are disclosed in its report; publication used the correct Roth.LeanEval target successfully. Optional public hB localization closed under API preservation. CoeffNorm14/26, overall89/264.

## CoeffNorm declaration 15 checkpoint

`Roth.normOne_hasseDeriv_le`: direct hasseDeriv_apply expansion removes output-support image bookkeeping; declaration23→10, body21→8 lines with no helpers. Exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-normOne_hasseDeriv_le.md). Module14800 exit0; complete final LSP no errors, fresh CLI original-type assignment/nonself reproof/standard axioms10408 exit0. All24 audit/42 rules/5 searches/11 checks and headline structure gate pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session76914 exit0; SHA256 `05f9128d32dfec65f7c590be5f25b23b2e817269ea2e042f38c68e29ffdcaf15` unchanged. Logs `/private/tmp/roth-coeffnorm-d15-{full,leaneval}.log`. Optional support-local public restatement closed under API preservation. CoeffNorm15/26, overall90/264.

## CoeffNorm declaration 16 checkpoint

`Roth.diag`: normalized ordinary lambda arrow, one-line definition retained; exact original public type/value/docstring verified by full-function and pointwise rfl probes. [Dedicated audit](cleanup/CoeffNorm-diag.md). Module93460 exit0; complete final LSP no errors, fresh CLI original-type/value/construction/standard-axiom checks56394 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session37370 exit0; SHA256 `af400c5f5c9179a854279959ce8050ed9f68d7acb5888ae7b2e5b52b736588d8` unchanged. Logs `/private/tmp/roth-coeffnorm-d16-{full,leaneval}.log`. Optional generic-coefficient construction closed under current API/value preservation. CoeffNorm16/26, overall91/264.

## CoeffNorm declaration 17 checkpoint

`Roth.diag_eq_sum`: direct eval₂_eq expansion removes explicit monomial-sum congruence; proof5→3, declaration7→5 lines, exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-diag_eq_sum.md). Module48754 exit0, complete final LSP no errors, fresh CLI original-type assignment/independent monomial-sum reproof/standard axioms20109 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session39188 exit0; SHA256 `f3e745f4aab0b8c61c9ee4196bf8267aa97138ac57cada23aae913b0a79d31c0` unchanged. Logs `/private/tmp/roth-coeffnorm-d17-{full,leaneval}.log`. CoeffNorm17/26, overall92/264.

## CoeffNorm declaration 18 checkpoint

`Roth.abs_coeff_diag_le`: consolidated coefficient-monomial cases with split_ifs/grind; body6→4, declaration8→6 lines. Exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-abs_coeff_diag_le.md). Module37835 exit0; complete frozen-source LSP no errors or target warnings; fresh CLI original-type assignment/independent explicit-branch reproof/standard axioms38036 exit0. All24 audit/42 rules/5 searches/11 checks pass. Scratch timing compares both proofs below100ms; production profiling remains final-phase work. Sequential full `lake build` and separate `lake build Roth.LeanEval` session47381 exit0; SHA256 `e8cec540e872c07592442cd4c2a9cf8bbaec03e0ee89ab0ebe9814295cb79d2c` unchanged. Logs `/private/tmp/roth-coeffnorm-d18-{full,leaneval}.log`. All stalled sessions finished; optional public variants closed. CoeffNorm18/26, overall93/264.

## CoeffNorm declaration 19 checkpoint

`Roth.natDegree_diag_le`: normalized two ordinary lambda arrows; retained direct degree/sum proof after compiled alternatives,7→7 declaration lines. Exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-natDegree_diag_le.md). Module84593 exit0; complete final LSP no errors, fresh CLI exact original-type assignment/nonself reproof/standard axioms32340 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session47412 exit0; SHA256 `71a51cfdf91108c0cf3983c4718bfc70d51001ed9e2d8c45573a77220764e366` unchanged. Logs `/private/tmp/roth-coeffnorm-d19-{full,leaneval}.log`. CoeffNorm19/26, overall94/264.

## CoeffNorm declaration 20 checkpoint

`Roth.eval_diag`: normalized constant-lambda arrow in the statement, retained one-line structural induction after compiled composition alternatives;4→4 declaration lines. Exact elaborated public type and docs preserved. [Dedicated audit](cleanup/CoeffNorm-eval_diag.md). Module1379 exit0, complete final LSP no errors, fresh CLI exact original-type assignment/independent composition reproof/standard axioms34678 exit0. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session32277 exit0; SHA256 `815a7a525d0a6ec34149da5b5d141cf978321d242abbefb9eb50bbcad4fe2cd8` unchanged. Logs `/private/tmp/roth-coeffnorm-d20-{full,leaneval}.log`. Optional abstract-target variant closed under API preservation. CoeffNorm20/26, overall95/264.

## CoeffNorm declaration 21 checkpoint

`Roth.diag_sub`: retained direct map_sub term unchanged after compiled alternatives;2→2 declaration lines, exact public API/docs preserved. [Dedicated audit](cleanup/CoeffNorm-diag_sub.md). Module57811 exit0; complete final LSP no errors, independent exact original-type assignment/nonself simp reproof/standard axioms pass. All24 audit/42 rules/5 searches/11 checks complete. Sequential full `lake build` and separate `lake build Roth.LeanEval` session89064 exit0; frozen SHA256 `815a7a525d0a6ec34149da5b5d141cf978321d242abbefb9eb50bbcad4fe2cd8` unchanged. Logs `/private/tmp/roth-coeffnorm-d21-{full,leaneval}.log`. CoeffNorm21/26, overall96/264.

## CoeffNorm declaration 22 checkpoint

`Roth.geom_sum_le_one_add_pow`: direct range-succ membership lemma replaces two-step conversion; lambda normalized,7→7 declaration lines. Exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-geom_sum_le_one_add_pow.md). Module83702 exit0, complete final LSP no errors, fresh CLI original-type assignment/nonself reproof/standard axioms52207 exit0; missing-nonnegativity counterexample confirmed. All24 audit/42 rules/5 searches/11 checks pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session84781 exit0; SHA256 `0aaf92ee5addd94f9c952317d166f8e29d4247d4f2412ac312bee11ca2d448e1` unchanged. Logs `/private/tmp/roth-coeffnorm-d22-{full,leaneval}.log`. CoeffNorm22/26, overall97/264.

## CoeffNorm declaration 23 checkpoint

Private `Roth.sum_box_prod_pow`: removed four-line wrapper and separator; sole abs_eval_le equality step now uses direct terminal simp with Mathlib finite-product/sum APIs. Public caller type/docs unchanged. [Dedicated audit](cleanup/CoeffNorm-sum_box_prod_pow.md). Module79122 exit0, complete final LSP no errors, fresh CLI original private-statement reproof/caller original-type/standard axioms16772 exit0. All24 audit/42 rules/5 searches/11 checks pass; private literature exemption explicit. Sequential full `lake build` and separate `lake build Roth.LeanEval` session8381 exit0; SHA256 `15d3ac71121de58374fd6d7bce63a35c7a25e81b1bf4bae306a12a3809277a5b` unchanged. Logs `/private/tmp/roth-coeffnorm-d23-{full,leaneval}.log`. CoeffNorm23/26 originals audited;25 declarations retained, overall98/264.

## CoeffNorm declaration 24 checkpoint

`Roth.abs_eval_le`: reduced proof25→14 lines through direct eval₂ expansion and a private geometric-box bound; exact public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-abs_eval_le.md). Module24551 exit0, complete final LSP no errors, fresh CLI original-type assignment/nonself reproof/standard axioms90708 exit0. All24 audit/42 rules/5 searches/11 checks pass. New private `sum_box_prod_pow_le_aux` awaits a fresh dedicated audit before declaration25. Sequential full `lake build` and separate `lake build Roth.LeanEval` session29495 exit0; SHA256 `f3bf41ffebbac5dab7b9fd600a154957131ae7b259e6281c4bc48f879004a2ad` unchanged. Logs `/private/tmp/roth-coeffnorm-d24-{full,leaneval}.log`. CoeffNorm24/26 originals audited, overall99/264.

## CoeffNorm added private helper checkpoint

Fresh independent dedicated audit of `sum_box_prod_pow_le_aux` completed: direct simpa composition reduces body8→4 lines; private unused DecidableEq removed with declaration-local Classical scope. All public signatures/docs preserved; old private statement transported across subsingleton instances in compiled scratch, independent binomial-expansion reproof and live-helper axioms standard. [Dedicated audit](cleanup/CoeffNorm-sum_box_prod_pow_le_aux.md) contains all24 audit/42 rules/5 actual searches/11 checks. Module and complete final LSP pass. Sequential full `lake build` and separate `lake build Roth.LeanEval` session13387 exit0, frozen SHA256 `7270e6f1cb84f697ca7016758951801f6805d2867ca2a1ad0597f6bc7be8ca68` unchanged; logs `/private/tmp/roth-coeffnorm-helper-box-{full,leaneval}.log`. Original tally remains CoeffNorm24/26, overall99/264; added helper1/1 audited.

## CoeffNorm declaration 25 checkpoint

`degreeOf_det_hasseDeriv_le`: direct degreeOf_C_mul_le replaces sign-cast casework; terminal simpa closes finite-sum arithmetic. Declaration14→9, body11→6, original public type/docs preserved. [Dedicated audit](cleanup/CoeffNorm-degreeOf_det_hasseDeriv_le.md) completes all24 audit/42 rules/5 actual searches/11 checks. Module exit0, complete final native LSP no errors/targetwarnings, original-type assignment/nonself prerequisite reproof/standard axioms pass. Optional public generalizations closed under API preservation; no new question. Sequential full `lake build` then separate `lake build Roth.LeanEval` session24977 both exit0, frozen SHA256 `dbbbeba0c96895502c9830ac2bca3fe8fb952028582f53e76e49964d6f9cc63a` unchanged; logs `/private/tmp/roth-coeffnorm-d25-{full,leaneval}.log`. Actual file-level profiling remains final-phase work. CoeffNorm25/26 originals plus1/1 new helper complete, overall100/264.

## CoeffNorm declaration 26 checkpoint

`abs_coeff_det_hasseDeriv_le`: inlined single-use entry/positivity witnesses and removed redundant pow rewrite; declaration20→15, body14→10, exact original public API/docs preserved. [Dedicated audit](cleanup/CoeffNorm-abs_coeff_det_hasseDeriv_le.md) completes all24 audit/42 rules/5 actual searches/11 checks. Final packed-source module70334 exit0, complete native diagnostics zero errors/six inherited warnings; fresh original-type assignment/nonself reproof/standard axioms3207 exit0. Packing issue caught before publication; earlier validation hash425cc67 invalidated and rerun. Final sequential full `lake build` then separate `lake build Roth.LeanEval` session2725 exit0 at frozen SHA256 `6bd90da3a6a467e166523e006f4911384e2d3ffd7c277b40d8a660c39d9aa738`, unchanged. Logs `/private/tmp/roth-coeffnorm-d26-packed-{full,leaneval}.log`. All25 public original constants additionally compare by rfl against compiled original-module baseline, final compatibility62691 exit0. CoeffNorm26/26 originals plus1/1 new helper audited, overall101/264; final holistic review/performance/file gates remain.

## CoeffNorm independent simplify checkpoint

Fresh independent holistic reviewer found two compiled minor simplifications: remove unused Mathlib.Algebra.MvPolynomial.Polynomial import and redundant helper classical tactic under declaration-local Classical scope. Both applied; [review](cleanup/CoeffNorm-simplify.md). Source320→268 lines (corrected count: declaration26 checkpoint was270, not the269 stated in a progress message). New source frozen SHA256 `7165f8d8bacbd22a337d00a95133d3b1264c5e2a972e7e2ee6ec9ddcc6517d5c`. Module96881 exit0, complete final CoeffNorm and all three direct-caller diagnostics no errors; fresh public original-type/value comparison76428 and identifier batch41147 exit0. Sequential full/separate Roth.LeanEval94127 exit0, source unchanged. Logs `/private/tmp/roth-coeffnorm-simplify-{module,compatibility,identifiers,full,leaneval}.log` and simplify LSP JSON artifacts. All27 dedicated reports complete; all final gates pass apart from actual performance sweep still pending. Overall101/264 originals audited.

## CoeffNorm final file checkpoint

All26 original declarations and1 added private helper audited; all27 reports pass42-rule/11-check artifact sweep. Independent simplify's two fixes published72871a7 and revalidated. Actual final-source profiling70638 exit0 anchors all26 retained declarations; maximum656.95ms normOne_det_le, all below750ms so no borderline resweep/slow-proof remediation needed. Parser accounts for wrapped private-helper command and explicit async proof; no profiling scaffolding or source drift. Post-profile module37614 exit0. Final SHA256 `7165f8d8bacbd22a337d00a95133d3b1264c5e2a972e7e2ee6ec9ddcc6517d5c`, source320→268, declaration lines202→149. All25 public baseline types/values compare by rfl with standard axioms; docs/comments preserved, no overwidth or trust changes. Full then separate Roth.LeanEval94127 exit0; complete CoeffNorm/Separation/Theta/MainLemma diagnostics no errors. [Final report](cleanup/CoeffNorm-final.md) includes complete artifacts, profiling table, cumulative gates and explicit limitations. Three Mathlib discoveries recorded in learnings.jsonl. Original project tally101/264. Compiled public DecidableEq/hC proposal remains unapplied/pending scoped decision and existing metadata warning remains unchanged. File/shared-progress/Git ownership released after successful final report push; fresh owner required for GenWronskian.


## GenWronskian declaration 1 checkpoint

`genWronskian`: redundant arrow-codomain parentheses removed and ordinary lambda arrow normalized;3→3 declaration lines, public type/value/docs preserved. [Dedicated audit](cleanup/GenWronskian-genWronskian.md) completes all24 audit/42 rules/5 actual searches/generalisation/public literature/width/inequality/11 checklist steps. Module74305 exit0, complete final LSP no errors/five inherited warnings, original type/value and independent determinant construction76861 exit0 with standard axioms. Optional CommRing extension compiled and closed under preserved API. Source ownership explicitly revoked at frozen SHA256 `c77ff48271a96da7c0f4fe4e4f40d394f94288e6765719929c9ac6297d510f70`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session18223, both exit0; hash unchanged. Logs `/private/tmp/roth-genwronskian-d01-{full,leaneval}.log`. Initial file audit records baseline and import-group separator. GenWronskian1/19 originals, overall102/264.


## GenWronskian declaration 2 checkpoint

`genWronskian_eq_zero_of_not_linearIndependent`: terminal simpa absorbs derivative normalization and a single-use congrArg witness; two lambda arrows normalized,10→9 declaration lines. Exact public signature/docs preserved. [Dedicated audit](cleanup/GenWronskian-genWronskian_eq_zero_of_not_linearIndependent.md) completes all24 audit/42 rules/5 searches/11 checklist steps. Module exit0, complete final LSP zero errors/five inherited warnings, fully quantified original-type and independently constructed nonself proof exit0 with standard axioms. [Compiled public Fintype omission proposal](cleanup/GenWronskian-api-proposal.md) forwarded for scoped decision and remains unapplied. Source freeze/explicit ownership revocation at SHA256 `612dec221169e15882ba06cd07f3cd99fa7fa7e1dd751f38705e5ba30b065418`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session93345, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d02-{full,leaneval}.log`. GenWronskian2/19 originals, overall103/264.


## GenWronskian declaration 3 checkpoint

`kronecker`: ordinary lambda arrow normalized and redundant exponent parentheses removed;2→2 declaration lines, exact original public type/value/docs preserved. [Dedicated audit](cleanup/GenWronskian-kronecker.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps. Module74890 exit0, complete final LSP zero errors/five inherited warnings; original whole-function value and independent eval₂Hom algebra-hom construction94911 exit0, standard axioms. Optional coefficient generalization closed under preservation; Fin→Nat coercion removal tested and rejected. Explicit ownership revocation at frozen SHA256 `0def23fb49d7e7ceab911c7637391c7e343b5f71307b503855950a1757d14fe2`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session47178, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d03-{full,leaneval}.log`. GenWronskian3/19 originals, overall104/264.


## GenWronskian declaration 4 checkpoint

`kroneckerExp`: unchanged1→1 line after full dedicated audit; existing100-codepoint term and necessary Fin→Nat bridge retained. [Dedicated audit](cleanup/GenWronskian-kroneckerExp.md) completes all24 audit/42 rules/5 actual search attempts/11 checklist steps; bounded Finder timeouts explicitly disclosed, no false absence claim. Module45882 exit0, complete final native LSP zero errors/five inherited warnings; exact original function rfl and independent reindexed Fin-sum reconstruction compile with standard axioms. Explicit ownership revocation at frozen SHA256 `0def23fb49d7e7ceab911c7637391c7e343b5f71307b503855950a1757d14fe2`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session44007, both exit0, source unchanged; logs `/private/tmp/roth-genwronskian-d04-{full,leaneval}.log`. GenWronskian4/19 originals, overall105/264.


## GenWronskian declaration 5 checkpoint

`kronecker_monomial`: direct terminal simp replaces rewrite/congruence/product bookkeeping;6→4 declaration lines,2 proof lines, exact public signature/docs preserved. [Dedicated audit](cleanup/GenWronskian-kronecker_monomial.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps; Finder and native-probe timeouts disclosed with successful direct fallback/CLI evidence. Module exit0, complete final LSP zero errors/five inherited warnings; exact original type and independent nonself reproof freshly compile with standard axioms. No new helper/rename/extension. Explicit ownership revocation at frozen SHA256 `8145a47137b5aec96742b4f5a429393b77e00e345799fda13fd6d658bbb704cb`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session21731, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d05-{full,leaneval}.log`. GenWronskian5/19 originals, overall106/264.


## GenWronskian declaration 6 checkpoint

Private `digits_unique`: deleted5-line Mathlib wrapper; sole kroneckerExp_injOn callsite uses Nat.ofDigits/List.ofFn APIs directly, net3 source lines removed. Caller public type/docs and all definitions preserved; caller receives its own subsequent audit. [Dedicated audit](cleanup/GenWronskian-digits_unique.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps. Module82420 exit0, complete final LSP zero errors/five inherited warnings; exact original private statement and caller original type independently re-proved, standard axioms only. No new helper/rename; optional private hk weakening superseded by deletion. Explicit ownership revocation at frozen SHA256 `dff932bf70cdff2d9d0c8160f0f752cd1cdf13ba8dbdf932d375bffd81bc4a10`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session6396, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d06-{full,leaneval}.log`. GenWronskian6/19 originals audited,18 declarations retained, overall107/264.


## GenWronskian declaration 7 checkpoint

`kroneckerExp_injOn`: combined digit expansion/reindexing and cancelled function precomposition through existing injectivity APIs;14→11 checkpoint declaration lines (same11 as original baseline), exact original public signature/docs preserved. [Dedicated audit](cleanup/GenWronskian-kroneckerExp_injOn.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps. Behrend.map_injOn found but unrelated analysis import fanout avoided; no new imports/helper. Optional hk removal compiled and closed under API preservation. Module96637 exit0, complete native LSP zero errors/five inherited warnings, exact original-type22743 and nonself proof78416 exit0 with standard axioms. Explicit ownership revocation at frozen SHA256 `71987145fa101e7d90eb961eb3f939babce38d9ae9c33d33864ced02969c4f1d`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session21700, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d07-{full,leaneval}.log`. GenWronskian7/19 originals, overall108/264.


## GenWronskian declaration 8 checkpoint

`coeff_kronecker`: unified finite-sum single-index obligations remove separate support cases and inline the remaining degree bound;14→13 declaration lines, public signature/docs preserved. [Dedicated audit](cleanup/GenWronskian-coeff_kronecker.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps; Finder normal search recovered. Module exit0, complete final LSP zero errors/five inherited warnings; exact original-type and independent prefix-only nonself reproof45952 exit0 with standard axioms. Failed automation/suggestion probes distinguished from accepted proofs; prebuild scratch import race corrected. No helper/rename/pending extension. Explicit ownership revocation at frozen SHA256 `10694e44ecbeeafffa6e844498c585d636dbc8456c53ba2b6f2ac5b41a76ce66`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session50338, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d08-{full,leaneval}.log`. GenWronskian8/19 originals, overall109/264.


## GenWronskian declaration 9 checkpoint

`kronecker_eq_zero_iff`: direct support-empty criterion removes arbitrary-exponent case split;8→6 declaration lines, exact public signature/docs preserved. [Dedicated audit](cleanup/GenWronskian-kronecker_eq_zero_iff.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps, with parameter probes separated from semantic necessity/counterexample analysis. Module43456 exit0, complete final native LSP zero errors/five inherited warnings; original-type and independent nonself proof63028 exit0 with standard axioms. Optional ring/radix broadening closed; no new helper/rename. Explicit ownership revocation at frozen SHA256 `a17695405eb4047be5fa1470a670fd6b55a9a242b2b82357f5c37a0fc56ef5df`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session17342, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d09-{full,leaneval}.log`. GenWronskian9/19 originals, overall110/264.


## GenWronskian declaration 10 checkpoint

`linearIndependent_kronecker`: inline the single-use finite-combination degree bound and consolidate map_sum/map_smul into terminal simpa;13→11 declaration lines,10→8 body lines, original public type/docs preserved. [Dedicated audit](cleanup/GenWronskian-linearIndependent_kronecker.md) completes all24 audit/42 rules/5 searches/11 checklist steps. Module95684 exit0, complete final native LSP zero errors/five inherited warnings; exact original public type and independent original proof freshly compile with standard axioms. Optional generalizations closed under preservation; failed automation/weakening probes explicitly distinguished from necessity/absence. No helper/rename. Explicit ownership revocation at frozen SHA256 `66842fe6298588547e6abd33d06e4354e763637f48490d0410d75c0d1294f1de`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session37753, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d10-{full,leaneval}.log`. GenWronskian10/19 originals, overall111/264.


## GenWronskian declaration 11 checkpoint

`derivative_aeval`: terminal multiplication-case simp replaces expansion/congruence/ring chain;14→10 declaration lines,11→7 proof lines. Exact public type/docs preserved; no helper. [Dedicated audit](cleanup/GenWronskian-derivative_aeval.md) completes all24 audit/42 rules/5 searches/11 checklist steps. Module75879 exit0, complete final LSP zero errors/five inherited warnings; original-type assignment and independent original proof98233 exit0 with standard axioms. Full CommSemiring scratch10191 also compiled; optional widening closed under preserved API. Explicit ownership revocation at frozen SHA256 `2d8077043642a40c4a55a8d438157c5234fa7c35c04d38567839fe1028249f32`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session8210, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d11-{full,leaneval}.log`. GenWronskian11/19 originals, overall112/264.


## GenWronskian declaration 12 checkpoint

Private `kronHasse`: normalized ordinary lambda arrow,2→2 lines, exact private type/value and protected existing docstring preserved. [Dedicated audit](cleanup/GenWronskian-kronHasse.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps. Module80469 exit0, complete final native LSP zero errors/five inherited warnings; exact-source private clone73690 checks original polymorphic type/value rfl and independent aeval/Hasse-sum reconstruction with standard axioms. Shared span/derivative uses justify retaining this operator; optional representation redesign closed. Explicit ownership revocation at frozen SHA256 `8489cadc516e917c45f5d291d766f7a7af7267cd0e30573df88804ceadf0e557`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session85551, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d12-{full,leaneval}.log`. GenWronskian12/19 originals, overall113/264.


## GenWronskian declaration 13 checkpoint

Private `kronSpan`: packed Submodule scalar argument onto declaration line;3→3 lines, exact original type/value/protected docstring preserved. [Dedicated audit](cleanup/GenWronskian-kronSpan.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps. Module53968 exit0, complete final LSP zero errors/five inherited warnings; isolated exact-source clone42351 checks original private type/value rfl and independent expanded sInf/aeval reconstruction with standard axioms. No redesign/helper/rename. Explicit ownership revocation at frozen SHA256 `783c291cbae82149741146cdf964f79d1b26b84cc23c7191613fef88bb984a75`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session40348, both exit0, source unchanged; logs `/private/tmp/roth-genwronskian-d13-{full,leaneval}.log`. GenWronskian13/19 originals, overall114/264.


## GenWronskian declaration 14 checkpoint

Private `kronSpan_mono`: deleted3-line span/image monotonicity wrapper; sole derivative_mem_kronSpan caller uses Mathlib directly, net3 source lines removed and17 declarations retained. Caller receives its own subsequent audit. [Dedicated audit](cleanup/GenWronskian-kronSpan_mono.md) completes all24 audit/42 rules/5 searches/11 checklist steps. Module64120 exit0, complete final LSP zero errors/five inherited warnings; original private statement97232 and before/after caller type/axioms81073/64659 compile with standard axioms. Public signatures/definitions/docs preserved. Explicit ownership revocation at frozen SHA256 `cb4e0d6efa8a7e2b8a270914c87db5d1882b31bc5f7d205c97853a2826d56847`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session85339, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d14-{full,leaneval}.log`. GenWronskian14/19 originals, overall115/264.


## GenWronskian declaration 15 checkpoint

Private `derivative_mem_kronSpan`: extract chain-rule generator identity and remove scalar-case single-use equality;36→27 declaration lines, longest branch under10. New private `derivative_kronHasse_aux` has9 lines and awaits fresh dedicated audit before declaration16; no helper audit credit yet. Total declaration content36→36, separating blank adds1 source line. Omega replaced by direct Nat.add_le_add_right; public API/docs preserved. [Dedicated audit](cleanup/GenWronskian-derivative_mem_kronSpan.md) completes all24 audit/42 rules/5 actual search attempts/11 checklist steps; three remote DNS failures disclosed and local/compiled generic probes supply positive evidence. Module31828 exit0, complete final LSP zero errors/five inherited warnings; exact original-type nonself reproof, actual built target/helper standard axioms and independent hF-drop counterexample pass. Explicit ownership revocation at frozen SHA256 `ca4b042b39f51080139eda0a986c5be683cb78f101f22c14934351295817c39b`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session71441, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d15-{full,leaneval}.log`. GenWronskian15/19 originals, overall116/264.


## GenWronskian extracted-helper checkpoint

Private `derivative_kronHasse_aux`: fresh separate audit of the declaration extracted in original15; terminal simp replaces per-summand ring,9→8 lines. [Dedicated audit](cleanup/GenWronskian-derivative_kronHasse_aux.md) records all24 audit/42 rules/5 actual searches/11 checklist steps, independent original-type reproof and actual built helper standard axioms. Module17564 exit0, complete final LSP zero errors/five inherited warnings. Explicit ownership revocation at frozen SHA256 `3e6cfc0362faa15037b2a786465a581c24c8a1c282a3ef322c974e0553e44a2c`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session68363, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-helper-derivative-{full,leaneval}.log`. GenWronskian15/19 originals plus1/1 added helper audited, overall116/264 originals unchanged.


## GenWronskian declaration 16 checkpoint

Private `hasseDeriv_kronecker_mem`: restricted-scalar submodule cancellation replaces the reciprocal-polynomial identity and cast/multiplication rewrite chain;20→16 declaration lines,18→14 body lines, longest branch8. Exact private mathematical type preserved; no helper. [Dedicated audit](cleanup/GenWronskian-hasseDeriv_kronecker_mem.md) completes all24 audit/42 rules/5 actual searches/11 checklist steps. Module6284 exit0, complete native LSP zero errors/five inherited warnings; independent exact original-type proof54709 and actual built private axiom check38591 exit0 with standard axioms. Optional characteristic-free restatement closed under API preservation, with proof limitation distinguished from semantic necessity. Explicit ownership revocation at frozen SHA256 `e71820d474dea9551ec7812650dbabd66ec497358a57dbe1a0a001589f4877bd`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session42399, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d16-{full,leaneval}.log`. GenWronskian16/19 originals plus1/1 added helper audited, overall117/264.


## GenWronskian declaration 17 checkpoint

`exists_hasseDeriv_kronecker_eq_sum`: terminal simpa and direct certificate remove manual rewrite/reflexivity and eta expansion; signature packed,10→8 declaration lines,6→5 proof lines. Exact public signature/docs, uniform existential coefficients/support and degree conjunction preserved. [Dedicated audit](cleanup/GenWronskian-exists_hasseDeriv_kronecker_eq_sum.md) completes all24 audit/42 rules/5 actual searches/public literature/11 checklist steps. Module88422 exit0, complete native LSP zero errors/five inherited warnings; exact original-type assignment and independent original proof51945 exit0 with standard axioms. No helper/rename/pending generalisation. Explicit ownership revocation at frozen SHA256 `c99367130f26ea52ba6f1a375afba046a79d3231c4f66722875209be3fbf0a8c`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session62892, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d17-{full,leaneval}.log`. GenWronskian17/19 originals plus1/1 added helper audited, overall118/264.


## GenWronskian declaration 18 checkpoint

`det_sum_rows`: direct multilinear finite-sum/scalar expansion and Finset.sum_fn remove the local matrix identity and summand-congruence block;12→9 declaration lines,8→5 proof lines. Exact public formula/instances/docs preserved. [Dedicated audit](cleanup/GenWronskian-det_sum_rows.md) completes all24 audit/42 rules/5 actual searches/public literature/11 checklist steps; attempted simpa normalization failures and native isolated-profiler parser failure explicitly disclosed. Module60607 exit0, complete native LSP zero errors/five inherited warnings; independent stronger no-DecidableEq proof95815 and exact original-type/built standard-axiom check60951 exit0. [Compiled public proposal](cleanup/GenWronskian-api-proposal.md) records unused DecidableEq removal with its sole implicit same-file caller; unapplied pending scoped decision. No helper/rename/pending routine change. Explicit ownership revocation at frozen SHA256 `9de4ad38403b6b44012fb4619cc58aeed78981be6ca1d7b434c98d49224fff06`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, session96489, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d18-{full,leaneval}.log`. GenWronskian18/19 originals plus1/1 added helper audited, overall119/264.


## GenWronskian declaration 19 checkpoint

`exists_genWronskian_ne_zero`: meaningful private determinant/substitution expansion extracted, both omega calls replaced with direct Nat bounds, single-use aliases inlined;26→16 headline declaration lines,23→13 body lines. New private `wronskian_kronecker_eq_sum_aux`15 declaration/9 proof lines awaits its fresh dedicated audit; total source grows6 lines for honest decomposition. Exact original public signature/docs and three public definitions preserved. [Dedicated audit](cleanup/GenWronskian-exists_genWronskian_ne_zero.md) completes all24 audit/42 rules/5 actual searches/public literature/11 checklist steps. Owner caught the worker's invalid readability exemption for a no-by single-use hdeg and applied its separately compiled inlining candidate; all final checks rerun on corrected source, historical d2ae601 evidence explicitly superseded. Corrected module81592 exit0, complete native LSP cell213 zero errors/five inherited warnings; independent original proof and renewed exact original-type/headline/helper actual built axiom sessions71534/91985 exit0 with standard axioms. Optional Finite widening closed: sole Separation caller already supplies Fintype; no additional pending proposal. Explicit source ownership revocation continued at frozen SHA256 `cbd1564dda27d17e67feacd0712e035fdfd0feeeefe920d6f7603cee970bade8`. Sequential full `lake build` then separate `lake build Roth.LeanEval`, corrected session22282, both exit0, hash unchanged; logs `/private/tmp/roth-genwronskian-d19-inline-{full,leaneval}.log`. GenWronskian19/19 originals plus1/2 added helpers audited, overall120/264 originals. Fresh second-helper audit and all final file phases remain.


## GenWronskian second extracted-helper checkpoint

Private `wronskian_kronecker_eq_sum_aux`: fresh separate audit reduces15→8 declaration lines and9→3 proof lines using direct algebra-hom determinant transport and terminal simpa over det_sum_rows; private expansion hypothesis localized to the supplied family, sole headline proof caller adapted. All public signatures/docs/definition values preserved, headline remains13 proof lines. [Dedicated audit](cleanup/GenWronskian-wronskian_kronecker_eq_sum_aux.md) completes all24 audit/42 rules/5 searches/11 checklist steps; independent initial uniform-hypothesis type reproof and actual built helper standard axioms pass. Owner applied the required signature repack only after earlier gates finished, then reran checks on final SHA256 `175ce6a3ece377484ccf54ad54479d3f79e425080364fbbcbe635484a9d482c9`; source ownership explicitly revoked for helper/caller at this freeze. Packed module20165 exit0, complete module/caller diagnostics zero errors (5/32 inherited warnings). Sequential full `lake build` then separate `lake build Roth.LeanEval`, session26252, both exit0; logs `/private/tmp/roth-genwronskian-helper-wronskian-packed-{full,leaneval}.log`. Cumulative isolated checks51509 also exit0: all13 original public types/three definition values compare by rfl; introduced identifiers compile; all6 current private declarations use only standard axioms. Source hash stable throughout. All21 dedicated reports contain42 rules/11 checked steps; source262 lines, no overwidth/banned constructs, original block comments byte-identical. GenWronskian19/19 originals plus2/2 added helpers audited, overall120/264 originals unchanged. Fresh independent simplify review and actual per-declaration profiling/final report remain.


## GenWronskian final file checkpoint

All19 original declarations plus2 added private helpers have fresh dedicated audits; all21 canonical reports contain42 rule labels/11 checked steps. Cumulative public API/three original definition values/docs/toolchain preserved. Source292→263 lines, declaration content198→170; two redundant private wrappers removed, two meaningful private identities audited. Fresh independent [simplify review](cleanup/GenWronskian-simplify.md) compiled removal of two redundant imports; owner applied and revalidated. Actual profiling found a slow digit-injection proof; a fresh dedicated [performance worker](cleanup/GenWronskian-performance-kroneckerExp_injOn.md) removed expensive failed Nonempty simp searches through direct ofFn APIs/restricted rewrites. Actual full-source timing1311.73→164.75ms, default-budget heartbeats6773→643; the deliberate three-line increase is documented. No other declaration change was needed after measured resweeps. All19 below1000ms in both final complete-source sweeps: maximum921.00ms, derivative_aeval842.94/841.02 and generator helper917.18/921.00; owner resweep11124 exit0 isolated from other compilers. No deferral/limit raise/profiler scaffolding.

Final SHA256 `cc7b2786088d6c839d36a14d9b5b09a884eb1de1a0d521b3bc2b84c9772cbfcf`, all leaf/reviewer source ownership explicitly revoked before owner gates. Module31484 exit0; complete module/Separation diagnostics zero errors,5/32 inherited warnings, no partial/timeouts/failed dependencies. Fresh all13 public type/value rfl comparisons,31-identifier batch and all6 private standard-axiom checks14185 exit0. Actual full `lake build` then separate `lake build Roth.LeanEval`, session90179, both exit0 (196.18s/32.16s), frozen hash stable; logs `/private/tmp/roth-genwronskian-performance-final-{full,leaneval}.log`. Final source/comments/width/trust sweep and git diff --check pass. Five meaningful learnings recorded. [Final report](cleanup/GenWronskian-final.md) contains every phase, full declaration/profile tables and exact cumulative gate evidence.

Project original tally120/264,6/14 files complete. Metadata remains user-preserved; two independently compiled public proposals remain unapplied. Final caller search refreshed: dependent-zero theorem has no project caller; det_sum_rows now has only the private expansion helper's implicit-instance call (the original headline call moved there during decomposition). Other pending CoeffNorm proposals unchanged. No routine GenWronskian work remains. Ownership of file/reports/shared-progress/Git transfers back to the project orchestrator on successful final report push; next Lattice requires its fresh file owner.


## Lattice declaration 1 checkpoint

`sqrt_one_sub_inv_lt`: inlined two single-use local facts and replaced typed positivity
with `Nat.cast_nonneg`;11→10 declaration lines, exact original public signature/docs
preserved. Added authorized import-group separator. [Dedicated audit](cleanup/Lattice-sqrt_one_sub_inv_lt.md)
records24 audit items/42 golfing rules/five actual searches/public literature/hypothesis
probes/11 checked steps. Module build exit0, complete native diagnostics zero errors/one
user-preserved header warning; independent original-type proof and actual target standard
axioms pass. Optional compiled hm1 weakening closed by project owner as unnecessary with
no current caller benefit; no pending decision. Explicit leaf source-ownership revocation
at SHA256 `9d5a4630daf715a8a7c8248c41046c74276421ccc603c004d020e129d049c53c`.
Owner sequential full `lake build` then separate `lake build Roth.LeanEval`, session61721,
both exit0 (114.13s/37.98s), frozen source hash unchanged; logs
`/private/tmp/roth-lattice-d01-{full,leaneval}.log`.
Lattice1/10 originals, overall121/264; final file phases remain.


## Lattice declaration 2 checkpoint

Private `inv_add_inv_le`: exhaustive audit retains existing6 declaration/4 proof lines;
positive denominators and polynomial bound already direct. [Dedicated audit](cleanup/Lattice-inv_add_inv_le.md)
records all24/42/five actual searches/all11 checked steps, every parameter probe and
compiled counterexamples. Optional private bound weakening closed without current caller
benefit. Module19043 exit0, complete native LSP zeroerrors/headeronly; independent exact
original-type proof and actual imported built private constant standard axioms pass.
Explicit owner source-ownership revocation at unchanged SHA256
`9d5a4630daf715a8a7c8248c41046c74276421ccc603c004d020e129d049c53c`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session74194, both
exit0 (6.14s/2.86s), hash stable; logs `/private/tmp/roth-lattice-d02-{full,leaneval}.log`.
Lattice2/10 originals audited, overall122/264; final file phases remain.


## Lattice declaration 3 checkpoint

Private `sum_inv_le`: inlined single-use reciprocal estimate, used cast-aware `gcongr`,
normalized two lambda arrows and separated chained tactics;15→15 declaration lines.
Exact private signature retained. [Dedicated audit](cleanup/Lattice-sum_inv_le.md) records
all24/42/five actual searches/all11 checks; native unsqueezed terminal simpa fails the
subsequent reflection rewrite by changing the inferred index, so restricted simpa retains
that required normal form. Module69913 exit0, complete LSP zeroerrors/headeronly; independent
original-type nonself proof and actual built private target standard axioms pass.
Explicit owner source-ownership revocation at frozen SHA256
`f94e0e1dcdc5dc0fc14ca4c9940b57963f59d44c60361a4724d50604b501251d`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session38839,
both exit0 (104.70s/35.53s), hash stable; logs `/private/tmp/roth-lattice-d03-{full,leaneval}.log`.
Lattice3/10 originals audited, overall123/264; final file phases remain.
