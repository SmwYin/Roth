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
- Standing approval updated 2026-10-18: the user says, “From now on implement all changes
  that you recommend. Only ask me if you can't decide.” This supersedes the earlier
  per-change approval policy above. Well-supported recommendations still require concrete
  compiled evidence and all sequential validation/publication gates. Earlier explicit
  preservation choices remain in force; platform escalation requirements are unchanged.

## Current status

MainLemma is active:6/27originals complete at the latest published checkpoint;
overall222/264originals,10/14fullycompletedfiles. Latest:`eta_lt_gam_iff` after fresh full
24-item/42-rule/5-method/11-step audit,independent original/type/binder/value/standard-axiom
checks,complete unfiltered affected diagnostics and actual anchored profile208.229ms.
Owner fullbuild55.789s THEN separateLeanEval43.154s,both exit0 on immutable17pins.
Packed signature93/29chars and replaced two-line proof with one grind[gam,lam]; added application guidance,preserved source quote. Exact API/three effective binders/imports/callers unchanged;0helpers. Profile281.175→208.229ms;heartbeats1588→1055. Actual rebuilt-module opaque body/full independent original/type AST/universe/binder/standard-axiom gates pass. Owner independently froze/rehashed54UTF8 artifacts and verified exact prefixes/root timings;fresh full root/LeanEval native closure returns zero messages/errors. Entry708→current695lines. Next:sqrt_lt_floor. MainLemma filewide final,
independent simplify and complete performance phases remain pending. See
[MainLemma ledger](cleanup/MainLemma.md) and [latest audit](cleanup/MainLemma-eta_lt_gam_iff.md).
The exact source/audit commit is recorded in appended checkpoint history by its metadata
child. Prior fullycompleted-file handoff is preserved below.

### Previous completed-file handoff (Theta)

Latest completed file after successful final publication: Theta. All 35/35 Theta originals
are complete; overall 216/264 original declarations and 10/14 files. The 50 retained
declarations comprise 32 originals and 18 new private helpers; all 22 introduced helper
histories received separate fresh audits. The final independent review is PASS-THROUGH.
Fresh owner gates pass all 1,223 cumulative semantic checks, all 29 original public
contracts, five definition values, whole original/current caller proofs, and all 50 actual
opaque proof-body/type/standard-axiom checks. Complete unfiltered diagnostics have zero
errors; Theta/MainLemma/Main/LeanEval/root warnings are 6/3/4/0/0.
Affected-module build 4.802 s, full build 6.695 s THEN separate
LeanEval 3.353 s all exit 0, with all 17 source/configuration pins unchanged.
Final actual profiling covers all 50 declarations, every sample below 1,000 ms; maxima
778.325, 907.046 ms. The required repeat on identical source also passed.
All historical failures remain preserved. [Final report](cleanup/Theta-final.md),
[independent review](cleanup/Theta-final-simplify-final.md), and
[contract ledger](cleanup/Theta-contract-proposal.md) provide the evidence.
Both technical hr findings have separate validated checkpoints. Explicit choices about
Theta hB/hr, hq, headers, wrappers and domains remain preserved. Next: MainLemma, then
Main, LeanEval and Roth.lean. MainLemma actual caller timing remains unavailable after the
bounded 60 s cutoff before its target (5/27); no whole-project performance pass is claimed.
The authorized Index rename remains queued for the project-end global pass. The final audit
publication hash is recorded in the appended history below.

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
See [Taylor final report](cleanup/Taylor-final.md). `Roth/CoeffNorm.lean` has completed all26 original declaration audits, its new private-helper audit and every final file phase. Source320→268; independent simplify fixes applied and revalidated. All26 retained declarations profile below750ms (maximum656.95ms); final module/full/separate LeanEval, complete module/caller LSP, all25 original-public type/value comparisons and standard axioms pass. Overall101/264 originals audited. See [CoeffNorm final report](cleanup/CoeffNorm-final.md). The explicitly user-approved public-hypothesis removals are applied and validated; current complete LSP has one preserved metadata warning, all26 declarations profile below750ms (maximum625.993ms), stronger independent reproofs/original-type recovery and full/separate LeanEval builds pass. See [approved amendment audit](cleanup/CoeffNorm-api-amendment.md). Earlier evidence in this status paragraph describes the pre-amendment checkpoint. Header metadata warning remains user-preserved. GenWronskian has completed all19 original audits, both added-helper audits and every final file phase. Source292→263; independent simplify removed two redundant imports, measured digit-injection optimization applied. All19 retained declarations below1000ms, maximum921.00ms with required borderline repeat passed. Final complete module/caller diagnostics, all13 public type/three definition-value comparisons, standard axioms, full build and separate LeanEval pass. See [GenWronskian final report](cleanup/GenWronskian-final.md). Overall120/264 originals;6/14 files complete. Both explicitly user-approved GenWronskian public-assumption removals are applied and independently checked. Current source264 lines, complete LSP zero errors/two warnings, actual profiles all19 below1000ms with required repeat passed (maxima998.25/907.78ms). See [approved amendment audit](cleanup/GenWronskian-api-amendment.md) for current type/proof/axiom/build evidence. Earlier profile/type-preservation figures in this paragraph describe the pre-amendment checkpoint; metadata and the unapproved existence-theorem Fintype remain explicit.
`Roth/Lattice.lean` has completed all10 original audits, all3 added private-helper audits and every final file phase. Source217→214; headline proof43→14 body lines, all4 original public types/docs preserved. Independent simplify import finding fixed and revalidated. All13 declarations below1000ms in both final complete profiling sweeps, maximum994.79ms; initial square-root1034.98ms sample explicitly recorded with required959.56/994.79ms repeats. Final module/full/separate LeanEval, complete module/caller diagnostics, independent original proofs/public-type equalities and actual standard axioms pass. See [Lattice final report](cleanup/Lattice-final.md). Overall130/264 originals audited;7/14 files complete. Header metadata remains user-preserved.

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

The latest completed file audit and declaration results are recorded in
[`cleanup/Separation.md`](cleanup/Separation.md) and [its final report](cleanup/Separation-final.md),
following the eight earlier completed files. Each completed declaration's report and
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
| `Roth/CoeffNorm.lean` | 320 | All cleanup phases complete;26/26 originals and1 added helper audited; user-approved public amendment applied and validated |
| `Roth/GenWronskian.lean` | 292 | All cleanup phases complete;19/19 originals and2 added helpers audited; both user-approved public amendments applied;2 preserved warnings |
| `Roth/Lattice.lean` | 217 | All cleanup phases complete;10/10 originals and3/3 added helpers audited; user-preserved metadata |
| `Roth/Index.lean` | 275 | All cleanup phases complete;21/21 originals audited; user-approved hypothesis groups applied and validated |
| `Roth/Separation.lean` | 618 | Complete;30/30 originals and all final phases;source556lines27retained;all12 approved instance amendments validated |
| `Roth/Theta.lean` | 981 | Complete;35/35 originals and all final file phases;source991lines,50retained |
| `Roth/MainLemma.lean` | 704 | Active;6/27 originals audited/published;final file phases pending |
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


## Lattice declaration 4 checkpoint

`sum_inv_lt`: inlined one single-use square-root fact, separated positivity proof tactics,
used `Nat.cast_nonneg` and direct `gcongr` comparison;24→23 declaration/21→20 bodylines.
Exact publictype/docs preserved. [Dedicated audit](cleanup/Lattice-sum_inv_lt.md) records all24
audititems/42rules/fiveactualsearches/publicliterature/everyparameterprobe/all11checks.
Actual modulebuild exit0(26s), complete nativeLSP zeroerrors/headeronly; independent
original-type nonself proof and actual public target standardaxioms pass. Nohelper/rename/API
proposal. Explicit owner source-ownership revocation at frozen SHA256
`ee64506a923d08cf5a57871b5f670a67f6f4509e924c56feac07e27909366d42`.
Sequential owner full `lake build` then separate `lake build Roth.LeanEval`, session36147,
both exit0 (108.79s/34.18s), hash stable; logs `/private/tmp/roth-lattice-d04-{full,leaneval}.log`.
Lattice4/10 originals audited, overall124/264; final filephases remain.


## Lattice declaration 5 checkpoint

Private `extend_apply_castSucc`: removed redundant singleton-zero simplification hint;
4→3 declaration lines, exact private type and four local rewrite sites preserved.
[Dedicated audit](cleanup/Lattice-extend_apply_castSucc.md) records all24 audit items,42 rules,
five actual searches, parameter probes and all11 checks. Actual module13844 exits0; complete
native LSP zero errors/header only. Independent exact original-type proof and actual built
private constant check31949 pass with standard axioms. No helper or rename.
Explicit owner source-ownership revocation at frozen SHA256
`7e42ef79b31d4fe9dcd627cc064dc656732639564afbf968f10a91ae38d56aa0`.
Owner sequential full `lake build` then separate `lake build Roth.LeanEval`, session5569,
both exit0(104.10s/35.13s), frozen hash stable; logs `/private/tmp/roth-lattice-d05-{full,leaneval}.log`.
Lattice5/10 originals audited, overall125/264; final file phases remain.


## Lattice declaration 6 checkpoint

Private `extend_apply_last`: targeted terminal simp subsumes the explicit range contradiction;
6→3 declaration lines, exact private type and four local rewrite sites preserved.
[Dedicated audit](cleanup/Lattice-extend_apply_last.md) records24 audit items/42 rules/five actual
searches/every parameter probe/all11 checks. Actual module build exits0 (31s); complete
LSP zero errors/header only. Independent exact original-type proof and actual imported
private #check/axiom probe exit0 with standard axioms. No probes remain running.
Explicit owner source edit revocation at frozen SHA256
`4e1844b749055743bc6aad96f85057664c5376d91e37e95ef53fa729a96de689`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session51672,
both exit0 (96.32s/34.26s), hash stable; logs `/private/tmp/roth-lattice-d06-{full,leaneval}.log`.
Lattice6/10 originals audited, overall126/264; final file phases remain.


## Lattice declaration 7 checkpoint

`card_filter_box_last`: extracted substantive private fibre-bijection identity, shared one
reconstruction proof across two obligations; public43→11 declaration lines/7 proof lines,
new `card_filter_box_fiber_aux`25 declaration/20 proof lines (largest branch9). Exact
public mathematical type and existing docs preserved, with signature packing/lambda style
normalized. [Dedicated audit](cleanup/Lattice-card_filter_box_last.md) records all24/42/five
actual searches/public literature/four binder probes/all11 checks. Finder timeout and native
standalone profiler limitation are explicit; aggregate profiling does not claim per-declaration
measurement. Actual module build exit0(34s), complete LSP zero errors/header only; exact
original-type assignment and independent original nonself proof exit0. Actual public/new
private helper standard axioms verified. Explicit owner source edit revocation at SHA256
`d3a5301ef1c44bf385b8918923fe31d25d013840fefa4fc5764a3dbf903386a5`.
Owner sequential full `lake build` then separate `lake build Roth.LeanEval`, session33681,
both exit0(102.58s/38.00s), frozen hash stable; logs `/private/tmp/roth-lattice-d07-{full,leaneval}.log`.
Lattice7/10 originals audited, overall127/264; helper fresh audit and final file phases remain.


## Lattice extracted fibre-helper checkpoint

Fresh dedicated `card_filter_box_fiber_aux` audit unsqueezes terminal obtain simplification
and replaces final explicit conjunction with direct simp;25→25 declaration/20 proof lines.
Exact helper type/public API/docs retained. [Dedicated audit](cleanup/Lattice-card_filter_box_fiber_aux.md)
records all24/42/five actual searches/six binder probes/all11 checks. Module65137 exit0;
complete LSP zero errors/header only. Independent exact initial-type nonself proof50270
and actual imported private environment probe81255 exit0 with standard axioms. Explicit
owner source edit revocation at frozen SHA256
`eabdd704d625fcba80e9529642866d57f0cd6e0274746224209ed37074981414`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session46779,
both exit0(84.53s/29.47s), frozen hash stable; logs
`/private/tmp/roth-lattice-helper-fiber-{full,leaneval}.log`.
Lattice7/10 originals plus1/1 added helper audited; overall127/264 unchanged.


## Lattice declaration 8 checkpoint

Private `filter_weight_le_eq_empty`: normalized two mathematical lambda arrows;3→3 lines,
exact mathematical type/proof strategy preserved. [Dedicated audit](cleanup/Lattice-filter_weight_le_eq_empty.md)
records24 audit items/42 rules/five actual search attempts/four binder drop probes/strict
weakening refuted by compiled zero-dimensional counterexample/all11 checks. Finder timeout
is explicit; no absence claim. Module build exit0(35s), complete LSP zero errors/header only;
independent original-type nonself clone and actual private theorem standard axioms pass.
Explicit owner source edit revocation at SHA256
`ff720f72959dc95143cec984113dd0fe3fef768e5757b8854a2eedbc90602dc7`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session67566,
both exit0(109.71s/40.64s), frozen hash stable; logs `/private/tmp/roth-lattice-d08-{full,leaneval}.log`.
Lattice8/10 originals plus1/1 helper audited, overall128/264.


## Lattice declaration 9 checkpoint

Private `card_filter_fiber_eq`: terminal grind replaces push_cast and two-direction arithmetic;
lambdas/continuation style normalized,11→10 declaration/5→4 proof lines. Exact mathematical
type preserved. [Dedicated audit](cleanup/Lattice-card_filter_fiber_eq.md) records all24/42/five
actual searches/four parameter probes/all11 checks. Stalled native tactic query bounded;
complete persistent direct LSP42366 passes (partial=false, zero errors/header only), earlier
partial calls not counted. Actual module85742 exit0(58s), independent exact original-type
nonself proof exits0 with standard axioms; actual private target verification standard.
Explicit owner source edit revocation at SHA256
`00bedd0a4607a8fa4017206e750d8827f2b5c672ec116b8664093d1b386bfbea`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session72585,
both exit0(70.69s/28.67s), frozen hash stable; logs `/private/tmp/roth-lattice-d09-{full,leaneval}.log`.
Lattice9/10 originals plus1/1 helper audited, overall129/264.


## Lattice declaration 10 checkpoint

Headline `card_filter_weight_le`: extracted two substantive private easy-range and successor
estimates; public47→17 declaration/43→14 body lines, largest branch9. Exact public type/docs
preserved. New private helpers `card_filter_weight_le_of_le_sqrt_aux`8 declaration/4 body
lines and `card_filter_weight_le_succ_aux`33 declaration/25 body lines await separate fresh
audits. [Dedicated audit](cleanup/Lattice-card_filter_weight_le.md) records all24/42/five actual
searches/public literature/five parameter probes/all11 checks. Original no-by aliases and
omega removed. Worker caught a final binder packing defect during report-only phase; owner
let historical786d2720 full/separate60475 finish, applied the exact packing correction, then
renewed all affected gates. No earlier hash's gates certify the corrected source.

Corrected source freeze SHA256 `97697192cf943554cec6fbc3735d556e63eb441571c2f30b39ff2f7b6e73883e`,
all leaf source ownership explicitly revoked. Module73103 exit0(30s), complete native LSP
cell98 success/partial=false/zero errors/header only. Independent ORIGINAL entire source
reproof and all4 original public proof-function equality comparisons29613 exit0; actual
all13 imported public/private declarations axiom scan68502 exits0, standard axioms only.
Logs `/private/tmp/roth-lattice-d10-packed-{module,compatibility,axioms}.log`. Sequential full
`lake build` then separate `lake build Roth.LeanEval`, corrected session16889, both exit0
(6.37s/3.15s), frozen hash stable; logs `/private/tmp/roth-lattice-d10-packed-{full,leaneval}.log`.
Lattice10/10 originals plus1/3 helpers audited, overall130/264; helper audits and final file
phases remain before Lattice completion.


## Lattice extracted easy-range helper checkpoint

Fresh dedicated `card_filter_weight_le_of_le_sqrt_aux` audit replaces chained cast rewrites
with terminal `simp [card_box]` and packs the signature;8→7 declaration/4 body lines.
[Dedicated audit](cleanup/Lattice-card_filter_weight_le_of_le_sqrt_aux.md) records all24/42/five
actual searches/five binder probes/all11 checks. Module build exit0(61s), complete native
LSP zero errors/header only; independent INITIAL exact-type nonself proof and actual private
standard-axiom verification pass. Public API/docs unchanged. Explicit owner source edit
revocation at SHA256 `c4001f0b35048a95614d8a819471d639a1d9f66dcfbf41633728f2a290ffb73e`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session37542,
both exit0(115.31s/45.69s), frozen hash stable; logs
`/private/tmp/roth-lattice-helper-easy-{full,leaneval}.log`.
Lattice10/10 originals plus2/3 helpers audited, overall130/264 unchanged.


## Lattice extracted successor-helper checkpoint

Fresh dedicated `card_filter_weight_le_succ_aux` audit localizes private positivity to the
last coordinate, adapts sole headline argument, removes unused classical and grouping
parentheses, packs signature;33→30 declaration/25→24 body lines. Headline remains14body
lines; all public types/docs preserved. [Dedicated audit](cleanup/Lattice-card_filter_weight_le_succ_aux.md)
records all24/42/five actual searches/all binder probes/11 checks; failed weakenings explicitly
concern the proof, not logical necessity. Actual module exit0(26s), complete nativeLSP zero
errors/header only; independent INITIAL exact-type nonself reproof/recovery and actual imported
private/headline standard-axiom checks exit0. All worker compiler processes finished.
Explicit owner source edit revocation at SHA256
`be707274cdc77d8e31a73497e8392e8a556f8d13af1e3c190e32ad9c9496a2b3`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session96137,
both exit0(144.68s/36.29s), frozen hash stable; logs
`/private/tmp/roth-lattice-helper-succ-{full,leaneval}.log`.
Owner inventory parser confirms all13 canonical dedicated reports each contain42 rule labels,
11 checked steps and zero unchecked items; all original block comments identical, no overwidth
source line. Source217→214, declaration content170→163. Lattice10/10 originals plus3/3 helpers
audited, overall130/264; fresh independent simplify, actual profiling and final gates/report remain.


## Lattice independent simplify checkpoint

Fresh [independent review](cleanup/Lattice-simplify.md) compiled a narrower two-import
proposal, applied by owner; unnecessary real/complex powers and square-root smoothness
imports replaced with the actual elementary sqrt/finite-product defining modules. No proof
or public contract change. Frozen sourcea363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8,
all worker/reviewer source ownership revoked. Actual module5997 exit0, complete module/caller
LSP132 zero errors/1+3 inherited warnings; fresh original-source independent proof/all4public
typeequalities/4 external#checks/all13actual standardaxioms46950 exit0. Sequential full/separate
93589 both exit0(82.60s/23.98s), frozen hash stable. Logs
`/private/tmp/roth-lattice-simplify-{module,compatibility,identifiers,axioms,full,leaneval}.log`.
All13 canonical audits verified42rule labels/11checked steps; no source overwidth or comment
drift. Source214lines. Original130/264, all10Lattice originals+3helpers audited; actual
per-declaration profiling and final file report remain before7/14file completion.


## Lattice final publication and handoff

All final file phases complete: [final report](cleanup/Lattice-final.md), all13 canonical
declaration reports and fresh independent simplify report present. Source217→214 lines,
declaration content170→163; headline43→14 body lines, largest branch9. All4 original public
types, mathematical conclusions, existing block docs and pinned versions preserved.
Source freeze SHA256 `a363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8`;
all worker/reviewer source ownership explicitly revoked. Import-only simplify fix published
as `b34d56d`; source unchanged throughout subsequent final profiling/build/report gates.

Actual isolated full-source profiler sessions3913/82130/19793 all exit0. Initial square-root
1034.98ms required repeated complete sweeps;959.56/994.79ms pass, all13 below1000ms in both
final sweeps. sum_inv_lt774.15/790.97ms; remaining11 below750ms. Final maximum994.79ms.
Actual per-declaration totals include elaboration and associated async proof/kernel/compiler
tasks without nested double counting; no aggregate-only inference or performance patch.
Trace/table evidence `/private/tmp/roth-lattice-profile-passN-{trace.log,table.json}` N=1,2,3;
final copies `/private/tmp/roth-lattice-final-profile-{trace.log,table.json}`.

Fresh final sequential full `lake build` then separate `lake build Roth.LeanEval`, session6730,
both exit0(6.36s/3.23s), frozen source hash stable; logs
`/private/tmp/roth-lattice-final-{full,leaneval}.log`. Current source also has module5997,
complete module/caller LSP132 zero errors, independent original whole-file reproof/all4
public equalities/all4 external identifiers/all13 actual standard axioms46950 exit0.
All13 audit reports42 rule labels/11 checked steps/no unchecked entries; original block
comments identical, no source overwidth, final diff check passes. Three meaningful learnings
recorded. No pending Lattice rename, public proposal, decomposition or routine follow-up;
header metadata warning explicitly preserved by user decision.

Project tally130/264 original declarations,7/14 files complete; private helpers do not
increment the original count. Following successful final report push, file/report/shared
progress/Git ownership is released to the project orchestrator. Newly approved CoeffNorm
and GenWronskian API removals remain unapplied and belong to the fresh amendment owner
before Index; no prior Lean source or report changed during Lattice ownership.


## Approved CoeffNorm API amendment — 2026-10-16

Explicit user approval covers removal of four unused public `[DecidableEq σ]` binders
and unused `normOne_det_le.hC`. Applied by a fresh Sol Medium narrow leaf; only the cleaned
same-file caller's positivity argument needed removal (older hC0/hN0 already absent).
Names, conclusions, other binders/docs/definitions/versions preserved. Source frozen and
leaf editing revoked at SHA256
`ee0b23cfee16cf674512a5c8f912a8030242e736db6e79fc1270be71675e67a9`.
[Amendment audit](cleanup/CoeffNorm-api-amendment.md): actual final complete native LSP
zero errors/header-only warning, four independent stronger reproofs, all25 original public
type/value recoveries and33 standard-axiom checks. Actual isolated final-source profiler
91480 exit0, all26 declarations below750ms, maximum625.993ms; no repeat needed.
Sequential owner full27622 then separate LeanEval35871 both exit0, frozen hash stable;
logs `/private/tmp/roth-coeffnorm-api-amendment-{full,leaneval}.log`. Theta and other downstream
sources unchanged; full build covers callers. Dedicated exact-path publication precedes
any GenWronskian source edit. Original count remains130/264,7/14 files complete.


## Both approved API amendments complete — 2026-10-16

CoeffNorm's dedicated checkpoint `9a9cc37bdf1671d83dc3fb5bef40af943666f8a4` was
successfully pushed before the second group began. GenWronskian's explicit approval covers
only the dependent-zero theorem's unused Fintype and `det_sum_rows`' unused DecidableEq.
A fresh Sol Medium narrow leaf applied exactly these and packed the shortened signature;
no other binder/proof/import/docs/definition/version changed. The existence theorem's
Fintype remains. Frozen source/explicit leaf edit revocation SHA256
`5283b554baa1fcfce18f2298a0f5181cc58586f22b541dd2222745ef651b6e32`.
[Amendment audit](cleanup/GenWronskian-api-amendment.md): packed module21414 exit0,
complete native LSP zero errors/two preserved warnings (previously five), independent
stronger nonself reproofs, actual new-type applications, all13 historical public
recoveries/three definition values and standard axioms pass. Actual isolated full-source
profiles78404/92985 both exit0; all19 below1000ms, required borderline repeats
929.00→829.00ms and998.25→907.78ms. No performance source edit required.
Sequential owner full15112 then separate LeanEval83552 both exit0, hashes stable;
logs `/private/tmp/roth-genwronskian-api-amendment-{full,leaneval}.log`. Source263→264
from the omit command. Current proposals/final reports and affected historical reports
link these amendments; earlier awaiting-decision statements are superseded.

Both approved groups now have their own validation/build/publication checkpoints.
Overall130/264 original declarations and7/14 files remain complete; amendments do not
increment this tally. No pending decision remains for these approved removals. Header
metadata remains user-preserved. After the second successful push, all amendment source,
report, shared-progress and Git ownership is released to the orchestrator; next Index
requires a fresh file owner. This amendment owner does not start Index.


## Index declaration1 checkpoint — 2026-10-16

Fresh Index file owner starts from `e557886`, source275lines/21original declarations.
Actual baseline full build28852 exits0; complete native LSP has zero errors/27 inherited
warnings. [File audit](cleanup/Index.md) records phases0–3 and complete original inventory.
Fresh dedicated [index audit](cleanup/Index-index.md) retains the 2line public definition:
all24audit items/42golf slots/five actual searches/every binder probe/literature/11checks,
module build, complete LSP, independent original type/value and standardaxioms pass.
Optional generic-coefficient observation remains report-only, not a required change.

Owner explicitly revoked leaf source editing and added the missing Mathlib/project
import separator. Frozen SHA256
`9ea21436746c9e155e485b0ae6ef6deb884e4391417044407c717cb2f6206f64`.
Owner module80771 exit0 and complete native LSP zero errors/27 inherited warnings.
Sequential full then separate LeanEval24111 both exit0 (170.57s/39.02s), hash stable;
logs `/private/tmp/roth-index-d01-{full,leaneval}.log`. Exact-path commit/push precedes
the next declaration edit. Index1/21 originals audited, overall131/264; final file phases
remain. [Compiled API proposal](cleanup/Index-api-proposal.md) awaits scoped decision:
18 unused public decidability binders, index_le_card.hr, exactly2Theta caller repairs;
none applied. No previous other-file approval was reused. Header remains user-preserved.


## Index declaration2 checkpoint

Private `mem_support_taylor_iff` retained unchanged,3→3lines. [Dedicated audit](cleanup/Index-mem_support_taylor_iff.md)
records all24audit/42rules/five actual searches/every binder probe/11checked steps.
Actual module47848 exit0; complete native LSP zero errors/zero target diagnostics,
27 inherited other warnings; independent exact original-type nonself proof and actual
imported private constant standardaxioms pass. Isolated166heartbeats is preliminary;
owner final anchored file profiling remains. No newhelper/rename/required refactor.
All leaf compiler processes complete; source/report ownership released. Source freeze
unchanged9ea21436746c9e155e485b0ae6ef6deb884e4391417044407c717cb2f6206f64.
Owner sequential full then separate LeanEval64010 both exit0(5.12s/3.05s), hash stable;
logs `/private/tmp/roth-index-d02-{full,leaneval}.log`. Exact-path publication precedes
nextedit. Index2/21 originals, overall132/264; API proposal still unapplied.


## Index declaration3 checkpoint and scoped API approval

Private `weightSet_finite` generic two-call Mathlib wrapper removed; both callers use
finite-image API directly. [Dedicated audit](cleanup/Index-weightSet_finite.md) records
all24/42/five actual searches/every binder probe/11checks, independent original proof,
actual built private standard axioms and compiled caller proposals. Worker source editing
explicitly revoked before owner deletion. Source276→272lines,20retained declarations;
all original public types, definition and block docs preserved.
Frozen SHA2566897edb8955031680fa67e41007292a74287c1f0737f9dbcd5b44ca42e471ef7.
Owner module45739 exit0, complete native LSP zero errors27 inherited warnings;
fresh whole ORIGINAL reproof/all18 public type+value equalities/all20actual standard
axiom checks90385 exit0. Sequential owner full then separate LeanEval7465 both
exit0(143.50s/32.05s), hash stable; logs `/private/tmp/roth-index-d03-{full,leaneval}.log`.
Index3/21 originals audited, overall133/264; publication precedes next edit.

Explicit USER approval via root/parent now covers only [API proposal](cleanup/Index-api-proposal.md)
groups1+2: remove σ-DecEq from17 public Index theorems plus τ-DecEq in index_rename,
remove index_le_card.hr and repair precisely2Theta callers preserving Theta contracts.
These will apply during corresponding fresh declaration checkpoints, not prematurely
across unaudited declarations. Group3 index_mul_left_weights.hl remains unapproved and
unchanged pending separate user decision. No broader approval inferred.


## Index declaration4 checkpoint

Private `weightSet_nonempty` golfed4→3 and removed as a thin support/image simp wrapper;
two callers now simplify nonemptiness directly from hP. [Dedicated audit](cleanup/Index-weightSet_nonempty.md)
records all24/42/five actual searches/every binder probe/11steps, module/complete LSP,
independent original proof and actual private standardaxioms. Owner explicitly revoked
leaf source edits before applying compiled caller-deletion proposal. Source272→267,
19retained declarations; public types, definition and block docs unchanged.
Frozen SHA256531003ff42de90398daad179eb7b7006cc520efea475de29274078cad567bf9a.
Owner module2756 exit0, complete native LSP zero errors27 inherited warnings;
fresh whole ORIGINAL nonself reproof/all18 public type+value equalities/all19 actual
standardaxiom checks58412 exit0. Sequential full then separate LeanEval47084 both
exit0(137.39s/33.18s), Index+Theta hashes stable; logs
`/private/tmp/roth-index-d04-{full,leaneval}.log`. No addedhelper/rename/API change.
Index4/21 originals audited, overall134/264. Exact-path push precedes declaration5,
the first fresh public audit where the scoped approved instance removal will apply.


## Index declaration5 checkpoint — first approved public instance removal

`index_le_weight` now omits unused σ-DecidableEq, specifically covered by user group1
approval; mathematical statement/proof/name/docs/other arguments unchanged.
[Dedicated audit](cleanup/Index-index_le_weight.md): all24/42/five actual searches/public
literature/every binder probe/11checks, worker module92257, complete native target-clean
LSP and fresh54440 actual new-type/nonself stronger proof/original-type adapter/standard
axioms pass. All leaf Lean calls finished and source editing explicitly revoked.
Frozen SHA2562bf2b502f4e95caf1b28cdc247ccd4a26cc9f1c60c747d8e7c388cf9035234cb.
Owner entire ORIGINAL independent reproof/all18 public recoveries/all19 actual standard
axioms55805 exit0; actual type Expr scan confirms no DecidableEq. Sequential full then
separate LeanEval89783 both exit0(144.71s/36.17s), Index+Theta hashes stable;
logs `/private/tmp/roth-index-d05-{full,leaneval}.log`. External Main native diagnostics
cell118 complete, zero errors/four inherited warnings; saved JSON. Current Index26
remaining warnings concern metadata/remaining approved omissions, no target warning.
Source267→268 from scoped omit command; all block docs preserved. First5canonical
reports each42rule labels/11checked steps. Index5/21, overall135/264 originals.
Exact-path publication precedes next edit. Group1 applied1/17 σ-removals; group2/card
and renameτ remain scheduled. Group3 scalinghl still unapproved/unapplied.


## Index d06 checkpoint — exists_weight_eq_index

Applied the explicitly approved unused σ-DecidableEq omission only; all proof, docs and mathematical binders retained.

[Dedicated audit](cleanup/Index-exists_weight_eq_index.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `a872711cb58cfec0e2bb6b24ba400001fb4f3d3e6518276b3f6f47f46f25352b`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session35801 exit0, `/private/tmp/roth-index-d06-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval56008 both exit0(147.16s/34.47s),
Index+Theta hashes stable; `/private/tmp/roth-index-d06-{full,leaneval}.log`.
Worker complete Index LSP: success=true partial=false timed_out=false, 0target diagnostics/26unrelated warnings. External MainLemma complete native LSP functions cell146: success=true partial=false timed_out=false, 0errors/3inherited warnings, noinfos, no faileddependencies. MainLemma:522 caller accepted; raw /private/tmp/roth-index-d06-mainlemma-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index6/21 originals,overall136/264; source269lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d07 checkpoint — le_index_iff

Applied the explicitly approved unused σ-DecidableEq omission and two Unicode lambda arrows; retained the explicit proof after shorter generic candidate measured 443.491ms versus original95.231ms; final162.62ms. Mathematical arguments, conclusion and docs retained.

[Dedicated audit](cleanup/Index-le_index_iff.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `35ec8776ff8a9da254b521bc6e651b013c8c87b769931bfc37646bf3ee3411d9`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session53801 exit0, `/private/tmp/roth-index-d07-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval93535 both exit0(145.71s/40.38s),
Index+Theta hashes stable; `/private/tmp/roth-index-d07-{full,leaneval}.log`.
Worker complete Index LSP: success=true partial=false timed_out=false, 0target diagnostics/26unrelated warnings. External MainLemma complete native LSP functions cell172: success=true partial=false timed_out=false, 0errors/3inherited warnings, noinfos, no faileddependencies. MainLemma:477 caller accepted; raw /private/tmp/roth-index-d07-mainlemma-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index7/21 originals,overall137/264; source270lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d08 checkpoint — index_nonneg

Applied approved unused σ-DecidableEq omission and direct nonnegative-infimum/image-transport term; proof3→1 lines, measured18.34→4.37ms, file270→269. Definitions, mathematical binders/conclusion and docs retained.

[Dedicated audit](cleanup/Index-index_nonneg.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `2497bbf3fc19aa862b47a5c66474cc336a2e04b745cd9f74f424c7ae05913755`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session55139 exit0, `/private/tmp/roth-index-d08-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval87007 both exit0(153.09s/35.49s),
Index+Theta hashes stable; `/private/tmp/roth-index-d08-{full,leaneval}.log`.
Worker complete Index LSP success=true partial=false timed_out=false, 0target diagnostics/25unrelated warnings. External Theta complete native LSP after one45second partial timeout and immediate complete retry: success=true partial=false timed_out=false, 0errors/23inherited warnings, noinfos/no faileddependencies. All3 index_nonneg callers accepted; raw /private/tmp/roth-index-d08-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index8/21 originals,overall138/264; source269lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d09 checkpoint — index_eq_zero_iff

Applied explicitly approved unused σ-DecidableEq omission and two Unicode lambda arrows. Independent counterexamples validate retained nonzero-polynomial and positive-weight assumptions; no broader API/proof change, docs preserved. Target measured154.51ms.

[Dedicated audit](cleanup/Index-index_eq_zero_iff.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `089b92ef70eee154e17169baf76710e227ed3dc3f8f1894496a006eca0fd86b5`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session76431 exit0, `/private/tmp/roth-index-d09-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval20223 both exit0(164.93s/36.44s),
Index+Theta hashes stable; `/private/tmp/roth-index-d09-{full,leaneval}.log`.
Worker final target-filtered diagnostics clean; owner unfiltered COMPLETE Index native diagnostics after fullbuild success=true partial=false timed_out=false, no faileddependencies, 0errors/23unrelated warnings, targetlines93–104 empty. Raw /private/tmp/roth-index-d09-index-lsp.json. Source rg finds only internal index_prod caller, accepted by module/fullbuild; no external caller to query.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index9/21 originals,overall139/264; source270lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d10 checkpoint — index_hasseDeriv_ge

Applied approved unused σ-DecidableEq omission and direct sub_le_iff_le_add/simpa proof, removing have/rewrite/linarith; proof5→3 lines, measured289.94→192.16ms. Appended public project-end rename request index_hasseDeriv_ge→index_sub_weight_le_index_hasseDeriv; no source rename.

[Dedicated audit](cleanup/Index-index_hasseDeriv_ge.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `e5f65f41f0054212ead03ba47fb84d660a1fbe451c7918ee83df9fb9325d4174`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session71946 exit0, `/private/tmp/roth-index-d10-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval62194 both exit0(176.89s/40.45s),
Index+Theta hashes stable; `/private/tmp/roth-index-d10-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, 0target items/21other warnings. External MainLemma and Theta complete native LSP0errors/3and23inherited warnings, noinfos/no faileddependencies; Theta one45second partial followed complete retry. Both external callers accepted; raw /private/tmp/roth-index-d10-callers-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index10/21 originals,overall140/264; source269lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d11 checkpoint — le_index_sum

Applied approved unused σ-DecidableEq omission and two Unicode lambda arrows only; retained explicit5-line coefficient argument after exhaustive probes. Updated proposal record for separately user-approved group3 scaling-hl removal and2minimalTheta rewrite arguments, scheduled at target18; no scaling change yet. Target394.921ms.

[Dedicated audit](cleanup/Index-le_index_sum.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `ca55d5c8adada4876194803c57bc4ab41cad3f30c13f17d414827852de268aeb`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session73801 exit0, `/private/tmp/roth-index-d11-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval86657 both exit0(150.60s/35.53s),
Index+Theta hashes stable; `/private/tmp/roth-index-d11-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, 0target diagnostics/19other warnings. External Theta complete native LSP0errors/23inheritedwarnings, noinfos/no faileddependencies after one45second partial request followed complete retry; sole le_index_sum callerTheta:394 accepted. Raw /private/tmp/roth-index-d11-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index11/21 originals,overall141/264; source270lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d12 checkpoint — weight_eq_finsuppWeight_div

Applied approved σ-DecidableEq omission; reused weight_eq_sum/cast_div_charZero and direct cancellation to remove manual support plumbing, hrj and field_simp. Proof8→6 lines,file270→269; measured439.849→212.334ms, standalone heartbeats1501→583. Preserved hr and formula; compiled mixed-zero counterexample validates global positivity.

[Dedicated audit](cleanup/Index-weight_eq_finsuppWeight_div.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `a57e50381e101099bf444b7e5feeb9af2e35d4f3908d8f21a7c93009e72b7374`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session23587 exit0, `/private/tmp/roth-index-d12-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval33771 both exit0(152.33s/36.29s),
Index+Theta hashes stable; `/private/tmp/roth-index-d12-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index native LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/18other warnings; /private/tmp/roth-weight-div-native-final.json. Owner rg finds only2internal bridge uses; both accepted by module/full builds, no external caller to query.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index12/21 originals,overall142/264; source269lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d13 checkpoint — index_eq_weightedOrder_div

Applied approved σ-DecidableEq omission, packed signature and reduced headline bridge16→12bodylines using one attained coefficient plus le_index_iff/ENat.toNat_le_toNat; no helper added. Preserved hP/hr/math/docs. Final241.789ms, source269→265. Recovered completed frozen full/separate build session after usage reset; no duplicate work.

[Dedicated audit](cleanup/Index-index_eq_weightedOrder_div.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `5f04282b1750289a3a79d03b8a282620d4af9a4f14c3845bde6100ee3f43f770`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session48345 exit0, `/private/tmp/roth-index-d13-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval45205 both exit0(170.63s/39.73s),
Index+Theta hashes stable; `/private/tmp/roth-index-d13-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/17other warnings; /private/tmp/roth-index-weighted-final2-lsp.json. Owner rg finds onlyinternal index_mul uses; all accepted by module/full builds, no external caller to query.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index13/21 originals,overall143/264; source265lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d14 checkpoint — index_mul

Applied approved σ-DecidableEq omission; inlined hPQ and simplified shared finite-order certificate with terminal simp. Selected7body versus original11, rejected fully inlined5body after actual-module regression; finalrepeat209.54ms. Definitions, hP/hQ/hr, formula/docs preserved; file265→262.

[Dedicated audit](cleanup/Index-index_mul.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `975ba0a5f5fc234c48bdf161c0bb178cff8c1bab7ac40d4f876dc8bcc2453e25`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session16109 exit0, `/private/tmp/roth-index-d14-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval41871 both exit0(122.00s/41.50s),
Index+Theta hashes stable; `/private/tmp/roth-index-d14-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/16other warnings; /private/tmp/roth-index-mul-selected-lsp.json. External Theta complete native LSP0errors/23inheritedwarnings/noinfos after one45second partial and complete retry, caller493 accepted; raw /private/tmp/roth-index-d14-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index14/21 originals,overall144/264; source262lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d15 checkpoint — index_prod

Applied approved σ-DecidableEq omission and two Unicode lambda arrows only; retained readable induction after one-line base alternative cost922vs900heartbeats. Independent direct weightedOrder_prod proof validates original type; target433.14ms, source262→263.

[Dedicated audit](cleanup/Index-index_prod.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `568dc824159ae7476977806bf4eff276e9d175d5317c5381aee0c57a72d2e232`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session51247 exit0, `/private/tmp/roth-index-d15-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval1153 both exit0(86.70s/23.18s),
Index+Theta hashes stable; `/private/tmp/roth-index-d15-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/14other warnings; /private/tmp/roth-index-prod-after-lsp.json. External Theta COMPLETE native LSP0errors/23inheritedwarnings/noinfos, caller399 accepted; raw /private/tmp/roth-index-d15-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index15/21 originals,overall145/264; source263lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d16 checkpoint — index_neg

Applied approved σ-DecidableEq omission only; unchanged one-tactic support-negation proof. Actual target250.05ms; original independent literal-index proof/recovery/axioms pass; source263→264. Caller Theta retains its section instances; stronger Index API exposes one additional unused-section warning there, reserved for Theta audit.

[Dedicated audit](cleanup/Index-index_neg.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `4117b5c634957e30e7df55bdc5a43b0c98d1b5a12dec1343fdc662155f7975b1`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session49904 exit0, `/private/tmp/roth-index-d16-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval13150 both exit0(101.62s/26.94s),
Index+Theta hashes stable; `/private/tmp/roth-index-d16-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/12other warnings; /private/tmp/roth-index-neg-after-lsp.json. External Theta COMPLETE native LSP0errors/24warnings after bounded partial+complete retry:23previous plus newly exposed unused-section instance in sum_max_sub_le_index_det at371; original section instance retained, no warning suppression or Theta edit. Caller398 accepted; raw /private/tmp/roth-index-d16-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index16/21 originals,overall146/264; source264lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d17 checkpoint — index_C_mul

Applied approved σ-DecidableEq omission only; original one-rewrite support-scaling proof, hc/data/formula/docs preserved. Independent coefficientwise-support proof validates original type. Target102.65ms; file264→265.

[Dedicated audit](cleanup/Index-index_C_mul.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `580afc142903ea2171cb7e4411d681524fd1fbdaedef33611af5d7c50fef24c1`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session21635 exit0, `/private/tmp/roth-index-d17-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval88853 both exit0(163.72s/39.89s),
Index+Theta hashes stable; `/private/tmp/roth-index-d17-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/10other warnings; /private/tmp/roth-index-cmul-diagnostics.json. Owner rg finds no project callers; no external caller query needed.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index17/21 originals,overall147/264; source265lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d18 checkpoint — index_mul_left_weights

Applied separately approved σ-DecidableEq and unused hl removals; original literal-index/stronger/zero proofs pass; target205.02ms. Exactly2Theta rewrite-argument deletions, all contracts/instances/positive facts preserved. Theta module97645exit0; independent ORIGINAL Index+Theta prefix86171exit0 with all6 original public type/value recoveries and standard actual axioms, including index_det_le with DecidableEqτ. Logs /private/tmp/roth-index-d18-theta-{module,scaling-compatibility}.log. Group3 validated/closed; no broader API change.

[Dedicated audit](cleanup/Index-index_mul_left_weights.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `c7ecc3d5d361a6f72515e0b4b400045466f6b79da07159eb003eca394addc402`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session37175 exit0, `/private/tmp/roth-index-d18-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval97631 both exit0(101.23s/35.65s),
Index+Theta hashes stable; `/private/tmp/roth-index-d18-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/8other warnings; /private/tmp/roth-index-scale-lsp.json. Owner COMPLETE Theta native LSP0errors/24warnings/noinfos after bounded partial+complete retry; both repaired callers accepted. Raw /private/tmp/roth-index-d18-theta-lsp.json. Theta docs/definition/theorem signatures untouched; only2exact rewrite argument deletions.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index18/21 originals,overall148/264; source266lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d19 checkpoint — index_rename

Applied approved σ/τ-DecidableEq removals; local classical, packed signature and Unicode lambda. Original and no-instance independent literal-index proofs pass; actual Expr9binders versus old11, noDecEq. Explicit proof retained after slower simp alternative; target105.050ms, source266→268. No Theta source edit.

[Dedicated audit](cleanup/Index-index_rename.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `8b24b3d3662da1a203889b8987874a03d11038f39578339564209e7e6b0d6718`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session74452 exit0, `/private/tmp/roth-index-d19-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval43968 both exit0(149.84s/37.90s),
Index+Theta hashes stable; `/private/tmp/roth-index-d19-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/6other warnings; /private/tmp/roth-index-rename-lsp.json. Owner COMPLETE Theta native LSP0errors/25warnings after bounded partial+complete retry:24previous plus newly exposed unused-section σ-DecEq on private indexSet_comp_subset:134; Θinstances retained for its later audit. Callers148/495 accepted; raw /private/tmp/roth-index-d19-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index19/21 originals,overall149/264; source268lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d20 checkpoint — index_le_card

Applied approved σ-DecidableEq and unused hr removals, packed signature and Unicode lambda; hP retained. Exactly2Theta hr call-argument deletions preserve everyΘcontract/instance/positivity premise. Θmodule21251exit0; independent ORIGINAL Index+Θprefix14771exit0/all9 original public type/value recoveries+standard actual axioms, including indexSet_bddAbove and Θ_le_card. Evidence /private/tmp/roth-index-d20-theta-{module,prefix-compatibility}.log. Group2 validated/CLOSED; optional hP-free zero-case extension not applied. Target38.970ms, source268→269.

[Dedicated audit](cleanup/Index-index_le_card.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `e05d2a8a8a08c937ab43f96999efb4e9476b9a8ce47c08f9e6267459b236f190`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session27382 exit0, `/private/tmp/roth-index-d20-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval93853 both exit0(97.14s/39.29s),
Index+Theta hashes stable; `/private/tmp/roth-index-d20-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/3other warnings; /private/tmp/roth-index-card-final-lsp.json. Owner COMPLETE Theta LSP0errors/28warnings after bounded partial+complete retry:25previous +3new preserved-contract warnings (unused section instance and hr at86, hr at109). Exactly2caller repairs accepted; no suppression/Theta contract removal. Raw /private/tmp/roth-index-d20-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index20/21 originals,overall150/264; source269lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index d21 checkpoint — index_unique

Approved final σ-DecidableEq omission; all17 public theorem omissions now applied. Genuine proof23→15lines by direct Taylor-coefficient bounds and alias removal; all hP/Fintype/Unique/data/docs preserved, no helper. Group1 target applications validated.

[Dedicated audit](cleanup/Index-index_unique.md): all24/42/five searches/binder probes/11checks;
worker module/complete LSP/independent proof/type/actual standard-axiom gates passed.
Frozen SHA256 `f706f41e57e50a6449b372c7ed36bc37cac254d6e52b21b94af1b03bdc5e0ee7`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session27558 exit0, `/private/tmp/roth-index-d21-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval99632 both exit0(169.65s/41.84s),
Index+Theta hashes stable; `/private/tmp/roth-index-d21-{full,leaneval}.log`.
Complete unfiltered native Index diagnostics: header warning only; Theta caller254 checked, success=true/partial=false/timed_out=false,0errors/28warnings, unchanged from d20. Evidence /private/tmp/roth-index-d21-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Index21/21 originals,overall151/264; source262lines,
19retained declarations. Exact-path commit and successful cleanup-branch push
precede the next edit. Header remains explicitly user-preserved.


## Index final completion — 8/14files,151/264 originals

[Final report](cleanup/Index-final.md). All21 originals audited by fresh dedicated workers;
19retained,two trivial private wrappers removed,no added helpers. Source275→245lines.
All3 scoped approved hypothesis groups CLOSED; four minimal Theta argument deletions
preserve all29 Theta original public contracts. No broader API change.
Final SHA256 `30e6f151ddd2d9c344b9537d1bef87124e3f5814d2e58f3cba499a7e1ea6c939`. Actual Index module62865,
independent original18recoveries/all19actualaxioms3443,identifiers72331,whole original
Index+Theta29contracts/actualaxioms54584 all exit0. Complete native Index/Theta/MainLemma/
Main LSP0errors,1/28/3/4warnings; Indexheader user-preserved,Theta five newly exposed
unused-contract warnings retained for its own fresh audit. Full/separateLeanEval35061
both exit0(87.99s/40.00s),stable hashes. Fresh independent simplify PASS-THROUGH;
actual two complete19-declaration finalprofile sweeps98346/75637 exit0,max374.66/341.66ms,
allbelow750borderline/1000budget,no limitraises/deferrals. All21 reports42rules/11checks.
One rename remains in shared queue for parent project-end drain. Final exact-path commit
and successful push precede release; nextfresh owner is Separation.


## Separation d01 checkpoint — mapDomain_some_none

[Dedicated audit](cleanup/Separation-mapDomain_some_none.md): all24 audit items,42golf rules,five actual searches,binder/generalisation/inequality/width tables and11steps. Private redundant wrapper removed; four calls directly specialise existing Mathlib off-range API. Import groups separated. Source618→616;29 retained declarations; all20public contracts/docs/definition unchanged. No added helper or rename.

Source FROZEN SHA256 `8de29f33439259fa33927a72c7411dbd40ff2a3afacfeb97d8ea4a14bf0f3646`; leaf source ownership revoked before owner builds. Actual module25817 exit0; COMPLETE unfiltered native LSP success=true,partial=false,timed_out=false,no faileddependencies,0errors/32baselinewarnings. `/private/tmp/roth-separation-d01-lsp.json`. Exact ORIGINAL isolated proof and generic existing-library proof compile standard-only. Before actual anchored target profile103.002ms; removed target has no final elaboration cost.

Owner73355exit0: whole ORIGINAL30 independently re-proved in isolated namespace,all20 original public type/value recoveries by rfl,and ALL29 actual retained standard-axiom checks. `/private/tmp/roth-separation-d01-compatibility.{lean,log}`. Owner sequential full then separateLeanEval39911 both exit0(127.65s/32.76s),stable frozen hashes; `/private/tmp/roth-separation-d01-{full,leaneval}.log` and `...-builds.json`. Original block docs byte-identical; focused diff checked.

Separation1/30,overall152/264 original audits after this checkpoint's exact-path commit and successful cleanup-branch push;8/14files complete. Public scoped12-theorem instance proposal compiled but NOT applied; see [proposal](cleanup/Separation-instance-proposal.md). Header remains user-preserved. Next original eq_mapDomain_some_add_single starts only after successful publication.


## Separation d02 checkpoint — eq_mapDomain_some_add_single

[Dedicated audit](cleanup/Separation-eq_mapDomain_some_add_single.md): all24/42/five actual searches,every effective binder/public literature,inequality/width tables and11steps. Shared Option case simplification reduces proof5→3lines; signature/docs unchanged. Public12-theorem instance proposal remains pending/unapplied; broader generic additive-coefficient candidate independently compiles but is outside that menu and unapplied. Source616→614,29retained.

Frozen SHA256 `92ffb3a092b9a23fdedc0da16bdd954f57d4c979ddf469b1d4f36cefc8c20278`; worker ownership revoked/all requests drained before owner gates. Module63738exit0,independent original contract/proof+actual standardaxioms28197exit0,complete native unfiltered LSP0errors/32baselinewarnings,success=true/partial=false/timed_out=false. `/private/tmp/roth-separation-d02-lsp.json`. Worker standalone source-extracted timing78.513ms is supplemented by OWNER ACTUAL MODULE anchored profile2444exit0: command14.840+async83.286=98.126ms,below750/1000budget. `/private/tmp/roth-separation-d02-actual-profile.log{,.json}`. No scaffolding/limits.

Owner14103exit0: independent whole ORIGINAL30 proof bodies,all20 public original type/value recoveries and ALL29 actual retained standardaxioms. Actual probe47.29s,`/private/tmp/roth-separation-d02-compatibility.{lean,log,json}`. Owner22880 sequentialfull/separateLeanEval both exit0(122.05s/30.04s),sourcehashstable; `/private/tmp/roth-separation-d02-{full,leaneval}.log` and `...-builds.json`. Exact focused diff/docs/whitespace checked.

Separation2/30,overall153/264 after exact-path commit and successful cleanup-branch push,8/14files complete. Next fresh private some_mapDomain_add_single only after publication. Header remains user-preserved.


## Separation d03 checkpoint — some_mapDomain_add_single

[Dedicated audit](cleanup/Separation-some_mapDomain_add_single.md): all24/42/fiveactualsearches/everybinder+negativeprobes/private literature exemption/width/inequality/11steps. Redundant private restriction-extension wrapper deleted; exactly2callers directly use existing generic restriction/embedding API. Source614→611;28retained (20public/8private),all original public contracts/definition/docs preserved. No new helper,public omission or rename.

Source FROZEN SHA256 `0f24374fef7d2a0392679a8848e1ef5358fff49531082934a021ee6a50c2e622`; all leaf requests drained/source ownership revoked before owner gates. Actual module91161exit0; COMPLETE unfiltered native LSP0errors/32baselinewarnings,success=true/partial=false/timed_out=false,no faileddeps; `/private/tmp/roth-separation-d03-lsp.json`. Exact independent original and generic proofs pass; all8actualprivate +2affected public axioms standard-only. ACTUAL MODULE trace53646exit0: changed coeff_coeffNone51.006ms and coeff_rename_mul_aeval394.509ms; original target28.042ms from preceding actual-module profile,deleted target no finalcost. `/private/tmp/roth-separation-d03-final-profile.log{,.json}`.

Owner90175exit0 independently re-proves ALL30original declarations,recovers all20 original public type/value contracts and checks ALL28actualretained standardaxiom sets (43.10s); `/private/tmp/roth-separation-d03-compatibility.{lean,log,json}`. Owner94244 sequentialfull then separateLeanEval both exit0(124.01s/30.50s),frozen sourcehashstable; `/private/tmp/roth-separation-d03-{full,leaneval}.log` and `...-builds.json`. Owner original block-doc comparison and exact diff/whitespace checks pass.

Historical d02 arithmetic corrected against git: body5→3lines (saving2),file616→614; earlier six/613 counts were incorrect. No source,validation or original-declaration-count consequence. Separation3/30,overall154/264 after exact-path commit/successful cleanup-branch push;8/14files complete. Pending12-theorem public-instance proposal remains unapplied; header user-preserved. Next fresh original mapDomain_add_single_none follows publication.


## Separation d04 checkpoint — mapDomain_add_single_none

[Dedicated audit](cleanup/Separation-mapDomain_add_single_none.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Redundant private scalar-evaluation wrapper removed; exactly two uses inline terminal simp equality proofs after direct dependent-if expansion was tested and reverted. No public signature, definition, documentation or pin change; no new helper or rename. Source611→610;27retained. Separation4/30,overall155/264 original audits after successful publication;8/14files complete.

Actual module 35267 exit 0; complete unfiltered native LSP 0 errors/32 baseline warnings, success=true, partial=false, timed_out=false; `/private/tmp/roth-separation-d04-lsp.json`. Exact ORIGINAL independent proof 96354 exit 0, only standard axioms. Leaf additional cumulative original/actual-axiom probe 39457 passed; its temporary compatibility path is subsequently reused by the fresh owner probe, whose evidence below is authoritative.

ACTUAL repository module anchored profile 79783 exit 0: changed coeff_coeffNone 108.746 ms and coeff_rename_mul_aeval 524.749 ms, both below 750/1000 ms; `/private/tmp/roth-separation-d04-final-profile.log` and `...-profile-anchors.json`. Original unchanged target baseline 69.331 ms; deleted target has no final cost. No source profiler scaffolding or limits.

Source FROZEN SHA256 `1fd92ece12094dc1d71783cfcfe6b7f92e92cf019d409e048e70f1074208831d`; leaf ownership revoked and requests drained before owner gates. Owner probe `48051` exit0,39.71s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d04-compatibility.{lean,log,json}`. Owner build session `79342` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.27s/27.24s; source hash stable. `/private/tmp/roth-separation-d04-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## Separation d05 checkpoint — coeff_X_none_pow_mul_rename

[Dedicated audit](cleanup/Separation-coeff_X_none_pow_mul_rename.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Option-equivalence polynomial coefficient calculation replaces nested exponent-subtraction casework; both unused private Fintype/DecidableEq instances omitted. Target body 20 to 11 lines; no public contract, definition, documentation or other proof changed; no new helper or rename. Source610→602;27retained. Separation5/30,overall156/264 original audits after successful publication;8/14files complete.

Actual lake build Roth.Separation exits 0 (`/private/tmp/roth-separation-d05-build.log`). Complete native unfiltered LSP success=true/partial=false/timed_out=false, no failed dependencies, 0 errors/31 warnings (`...-final-lsp.json`). Two target warnings removed; coeff_rename_mul_aeval newly exposes one unusedSectionVars warning for its unchanged pending public instances: 32 - 2 + 1 = 31. Independent exact ORIGINAL proof/type and actual built target/affected public standard axioms pass (`...-independent.{lean,log}`, `...-axioms.{lean,log}`).

ACTUAL repository module anchored profile exits 0 (`/private/tmp/roth-separation-d05-final-profile.log`, `...-profile-anchors.json`): target before 248.710 ms, final outer omit 60.400 + async 209.913 = 270.313 ms. Actual affected callers eq_sum_X_none_pow_mul_coeffNone 157.857 ms and coeff_rename_mul_aeval 428.503 ms. All below 750/1000 ms; no speedup claim, scaffolding, limits or deferral.

Source FROZEN SHA256 `c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`; leaf ownership revoked and requests drained before owner gates. Owner probe `16920` exit0,48.70s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d05-compatibility.{lean,log,json}`. Owner build session `8141` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,139.72s/32.94s; source hash stable. `/private/tmp/roth-separation-d05-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## Separation d06 checkpoint — coeffNone

[Dedicated audit](cleanup/Separation-coeffNone.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Semantic coefficient definition retained byte-identically: existing coefficient/expansion/degree API and multiple uses justify it. Every effective binder, actual negative probes, public literature and definition type/value preservation audited. No source, visibility, API, documentation or import change. Source602→602;27retained. Separation6/30,overall157/264 original audits after successful publication;8/14files complete.

Actual module build exits 0. Native COMPLETE unfiltered LSP success=true/partial=false/timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`/private/tmp/roth-separation-d06-final-lsp.json`). Independent original type/value reconstruction imports only Mathlib and exits 0; actual built definition type/value and standard-axiom checks pass (`...-independent.{lean,log}`, `...-axioms.{lean,log}`). Six actual negative binder probes and arbitrary-universe positive base compile evidence in `...-binder-probes.json`.

Source and exact target are unchanged from ACTUAL repository-module profile `/private/tmp/roth-separation-d05-final-profile.log{,.json}`: coeffNone command 12.094 ms, no async proof; below 750/1000 ms. No redundant profiling run, scaffolding, limits, performance claim or deferral.

Source FROZEN SHA256 `c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`; leaf ownership revoked and requests drained before owner gates. Owner probe `43989` exit0,34.00s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d06-compatibility.{lean,log,json}`. Owner build session `69566` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.86s/2.87s; source hash stable. `/private/tmp/roth-separation-d06-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## Separation d07 checkpoint — coeff_coeffNone

[Dedicated audit](cleanup/Separation-coeff_coeffNone.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Direct optionEquivLeft_coeff_coeff calculation and coordinate extensionality replace embedding and inline scalar-evaluation rewrites. Current-start proof six to five physical lines; original public effective signature/docs preserved, no helper, import or other declaration change. Source602→601;27retained. Separation7/30,overall158/264 original audits after successful publication;8/14files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d07-module.log`). Complete native unfiltered LSP success=true/partial=false/timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Independent ORIGINAL definition/type recovery and non-self proof compile; actual built target and independent proof use only standard axioms (`...-independent.{lean,log}`). All eight effective binders drop-tested and Semiring weakening tested; initial import-race negatives retried and excluded from successful evidence. Individual/joint public instance omissions compile but remain pending/unapplied.

ACTUAL repository-module anchored profile exits 0 (`/private/tmp/roth-separation-d07-final-profile.log{,.json}`): command 9.753 + async 105.724 = 115.477 ms, below 750/1000 ms. Baseline 105.435 ms; no speedup claim, scaffolding, raised limit or deferral.

Source FROZEN SHA256 `a3a41139893974634024440f0897d72359502621f287671625d000e2bb3fc25b`; leaf ownership revoked and requests drained before owner gates. Owner probe `48331` exit0,44.71s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d07-compatibility.{lean,log,json}`. Owner build session `87726` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,139.54s/33.53s; source hash stable. `/private/tmp/roth-separation-d07-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## Separation d08 checkpoint — eq_sum_X_none_pow_mul_coeffNone

[Dedicated audit](cleanup/Separation-eq_sum_X_none_pow_mul_coeffNone.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Final support-zero branch now uses a direct degree-bound argument instead of contradiction, an anonymous have and omega; proof 11 to 9 lines, source 601 to 599. No public signature, documentation, import or helper changes. Source 601 → 599; 27 retained declarations. Separation 8/30, overall 159/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d08-module.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Independent exact original-type proof using polynomial equivalence transport and a counterexample to dropping hn compile; actual built target and independent proof use only standard axioms (`...-independent.{lean,log}`). All 11 binder probes completed; individual/joint instance omissions and Fintype-to-Finite weakening compile but remain pending and unapplied.

Actual repository-module profile exit 0 (`/private/tmp/roth-separation-d08-final-profile.log{,.json}`): command 26.740 + async proof 116.512 = 143.252 ms, below 750/1000 ms; baseline 137.595 ms. No speedup claim, profiler scaffolding, raised limits or deferral.

Source FROZEN SHA256 `24c37da51aee81b82da351937cb595a67679f2f566d475e8b72aecccad1a8a16`; leaf ownership revoked and requests drained before owner gates. Owner probe `19855` exit0,41.30s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d08-compatibility.{lean,log,json}`. Owner build session `64974` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,113.98s/26.46s; source hash stable. `/private/tmp/roth-separation-d08-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved.


## Separation d09 checkpoint — degreeOf_coeffNone_le

[Dedicated audit](cleanup/Separation-degreeOf_coeffNone_le.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; The coefficient support lemma replaces coefficient/multidegree rewriting; proof four to two physical lines, file 599 to 597. Public signature and documentation preserved; no helper, import or other declaration change. Source 599 → 597; 27 retained declarations. Separation 9/30, overall 160/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d09-build.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/32 warnings (`...-final-lsp.json`): one unusedSectionVars warning newly exposed because this proof no longer indirectly consumes the inherited public index instances. Their omission remains pending and unapplied. Independent exact original type/non-self Finset-sup proof and actual built target standard-axiom checks pass (`...-independent.{lean,log}`); every effective binder has actual native probe evidence.

Actual repository-module profile exits 0 (`/private/tmp/roth-separation-d09-final-profile.log{,.json}`): command 4.112 + async 36.412 = 40.524 ms, baseline 66.515 ms; one anchor each and below 750/1000 ms. No whole-project speedup claim, source profiler scaffolding or raised limits.

Source FROZEN SHA256 `72f715a6efc3664bfad5d760b598939f131a32393988c886da69206e67e1dc12`; leaf ownership revoked and requests drained before owner gates. Owner probe `68300` exit0,54.14s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d09-compatibility.{lean,log,json}`. Owner build session `50653` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,158.46s/38.75s; source hash stable. `/private/tmp/roth-separation-d09-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved.


## Separation d10 checkpoint — coeff_rename_mul_aeval

[Dedicated audit](cleanup/Separation-coeff_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Direct polynomial-equivalence coefficient calculation replaces the support expansion, sum and case split. Body 18 to 7 lines; source 597 to 586, 27 retained. Public signature/docs unchanged, no helper or other declaration edit. Source 597 → 586; 27 retained declarations. Separation 10/30, overall 161/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0; complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 warnings (`/private/tmp/roth-separation-d10-final-lsp.json`). One unusedSectionVars warning disappears because the new proof consumes the retained public coefficient bridge. Exact original type and independent non-self proof compile, actual target/bridge/caller use only standard axioms. All 12 binder suite cases finish; semantic instance omissions compile with an isolated probe-local bridge, whereas literal final-proof-only omission still depends on earlier retained public bridge instances. The grouped public proposal remains pending and unapplied.

Actual repository-module sweeps exit 0: preceding 842.772 ms borderline measurement is reswept at 490.631 ms unchanged baseline; final target 52.568 + 215.845 = 268.413 ms, below 750/1000 ms (`/private/tmp/roth-separation-d10-final-profile.log{,.json}`). Future original 21 exists_separated_representation measures 1342.091 ms and remains tracked for its dedicated audit, not claimed under budget here. No source profiler scaffolding, raised limits or target deferral.

Source FROZEN SHA256 `721b7cde6fe0430a6e37e3fd92be12f272ad38ed8409de2acfdb81567ca7dacb`; leaf ownership revoked and requests drained before owner gates. Owner probe `87314` exit0,40.79s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d10-compatibility.{lean,log,json}`. Owner build session `51365` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,123.85s/29.72s; source hash stable. `/private/tmp/roth-separation-d10-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved.


## Separation d11 checkpoint — aeval_X_eq_rename

[Dedicated audit](cleanup/Separation-aeval_X_eq_rename.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Existing Polynomial.toMvPolynomial_eq_rename_comp gives the proof directly via AlgHom.congr_fun. Body ten to one physical lines, declaration 13 to 4, source 586 to 577 (+2/−11 Git diff). Public type/docs preserved; no new helper or other source edit. Source 586 → 577; 27 retained declarations. Separation 11/30, overall 162/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d11-build.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Exact original effective type and independent non-self original proof compile after actual module build; actual target and independent proof use only standard three axioms (`...-independent.{lean,log}`). Every effective binder and parent weakening has actual probe evidence; original type has no τ/Fintype/DecidableEq section assumptions.

Actual repository-module profile exits 0 (`/private/tmp/roth-separation-d11-final-profile.log{,.json}`), command 24.091 + async 18.511 = 42.602 ms; baseline 201.535 ms, below 750/1000 ms. No profiler scaffolding, raised limit or performance deferral.

Source FROZEN SHA256 `9ca5d14b3bcfba066fa924fc0f6eca5aa5b13d88dbabeab9a281a749bbd689c1`; leaf ownership revoked and requests drained before owner gates. Owner probe `23627` exit0,42.59s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d11-compatibility.{lean,log,json}`. Owner build session `63999` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.32s/32.64s; source hash stable. `/private/tmp/roth-separation-d11-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved. D11 additionally identifies an optional public-wrapper deletion with two Theta rewrite substitutions. The retained public name is unchanged; coordinator notified, no API deletion or Theta edit applied.


## Separation d12 checkpoint — degreeOf_none_rename_some

[Dedicated audit](cleanup/Separation-degreeOf_none_rename_some.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Redundant private wrapper removed, exactly two callers use direct degree/rename simplification. Source 577 to 570 lines (11 removed, 4 added), 27 to 26 retained declarations. No public signature, definition, documentation or import change. Source 577 → 570; 26 retained declarations. Separation 12/30, overall 163/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d12-module.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Independent exact original type/non-self proof and actual two changed public caller axiom checks exit 0, only standard three axioms (`...-original-axioms.log`). All binder compiler probes and native requests completed and drained; private literature exemption recorded.

Actual final full-module profile exits 0, fully drained (`/private/tmp/roth-separation-d12-final-profile.log{,.json}`): changed hasseDeriv_rename_mul_aeval 65.655 + 182.016 = 247.671 ms; degreeOf_none_rename_mul_aeval 21.430 + 80.199 = 101.629 ms. Both below 750/1000 ms. Removed target baseline 95.394 ms, no final target cost; no profiler scaffolding or raised limits.

Source FROZEN SHA256 `1d7e167ce78eb18a4815866a71a286989095d26499f49534db6af2ee823d2137`; leaf ownership revoked and requests drained before owner gates. Owner probe `83868` exit0,63.55s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d12-compatibility.{lean,log,json}`. Owner build session `20284` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,113.27s/25.24s; source hash stable. `/private/tmp/roth-separation-d12-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved. Optional public renaming-wrapper removal is separate: two Theta uses plus five internal uses at four Separation sites require changes. The public API and all such uses remain in repository source; concrete scratch evidence is documented in Separation-wrapper-proposal.md.


## Separation d13 checkpoint — degreeOf_aeval_X_none_of_ne

[Dedicated audit](cleanup/Separation-degreeOf_aeval_X_none_of_ne.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private helper removed after testing direct degree/rename simplification at both actual callers; source 570 to 562 (Git +7/−15), 26 to 25 retained declarations. Public signatures, definitions, documentation and imports preserved. Source 570 → 562; 25 retained declarations. Separation 13/30, overall 164/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d13-build-removal.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 baseline warnings (`...-removal-lsp.json`). Exact original effective type and independent non-self original support proof compile; both actual changed caller axioms are standard three only (`...-independent-final.log`). All binder negatives have genuine compiler errors after three missing-olean races were retried; raced failures excluded from semantic evidence. All requests drained and source ownership revoked before owner gates.

Actual final repository-module profile exit 0 (`/private/tmp/roth-separation-d13-removal-profile.log{,.json}`): changed hasseDeriv_rename_mul_aeval 75.763 + 393.163 = 468.926 ms, degreeOf_rename_mul_aeval 49.778 + 95.879 = 145.657 ms; one command/async anchor each, below 750/1000 ms. Removed target baseline 53.178 ms, no final target cost. No performance improvement claim, profiler scaffolding or limit increase.

Source FROZEN SHA256 `ba6cdd854cc9e3ae0df16663905d80233ae16b8f2240e8c8326e5ea801b1e1d2`; leaf ownership revoked and requests drained before owner gates. Owner probe `86125` exit0,47.19s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d13-compatibility.{lean,log,json}`. Owner build session `25929` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.57s/30.90s; source hash stable. `/private/tmp/roth-separation-d13-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem instance omissions and optional aeval_X_eq_rename deletion. The public-wrapper scratch candidate is documented against its explicit D12 source hash; later proof cleanup moves its internal call sites, requiring a fresh scan/candidate before any approved application. Header remains user-preserved.


## Separation d14 checkpoint — rename_some_ne_zero

[Dedicated audit](cleanup/Separation-rename_some_ne_zero.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private renaming-nonzero wrapper removed; exactly two callers use rename_eq_zero_iff_of_injective directly. Source 562 to 559 (Git +4/−7), 25 to 24 retained declarations. No public API, definition, documentation or import change. Source 562 → 559; 24 retained declarations. Separation 14/30, overall 165/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d14-build.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-lsp.json`). Exact original type and independent arbitrary-injective-map proof compile; actual changed caller axioms and original-type proof use standard three only (`...-independent-final.log`). All five binder negative probes have actual exit 1 (`...-binders.json`); all requests drained and all source ownership revoked before owner gates.

Actual repository-module final profile exit 0 (`/private/tmp/roth-separation-d14-final-profile.log{,.json}`): degreeOf_rename_mul_aeval 28.381 + 71.092 = 99.473 ms, degreeOf_none_rename_mul_aeval 22.465 + 91.375 = 113.840 ms; one command/async anchor each, below 750/1000 ms. Removed target baseline 103.822 ms, no final target cost. No profiler scaffolding or raised limits.

Source FROZEN SHA256 `5ee248fa04d6ef74d0d6cccb17c898c52302215f62eb480dfa5944562ebe5ea1`; leaf ownership revoked and requests drained before owner gates. Owner probe `59421` exit0,57.83s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL24 actual retained standardaxiom checks. `/private/tmp/roth-separation-d14-compatibility.{lean,log,json}`. Owner build session `84208` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,142.29s/41.59s; source hash stable. `/private/tmp/roth-separation-d14-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem index-instance omissions and optional aeval_X_eq_rename removal. The latter records compiled historical D12 candidates; refresh actual source/caller inventory before eventual approved application. Header remains user-preserved.


## Separation d15 checkpoint — aeval_X_none_ne_zero

[Dedicated audit](cleanup/Separation-aeval_X_none_ne_zero.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private evaluation-nonzero wrapper removed; exactly two callers use mathlib toMvPolynomial injectivity via an explicit aeval hom argument. Source 559 to 555 (Git +4/−8), 24 to 23 retained declarations; public types/docs/definitions/imports unchanged. Source 559 → 555; 23 retained declarations. Separation 15/30, overall 166/264 original audits after successful publication; 8/14 files complete.

Actual corrected module build exits 0 (`/private/tmp/roth-separation-d15-module-build-fixed.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 baseline warnings (`...-final-lsp-fixed.json`). Independent exact original type/non-self proof, arbitrary-index strengthening, actual binder negatives and zero counterexample pass their expected compiler outcomes; actual built callers use standard three axioms only. An initial underscore hom argument folded toMvPolynomial and failed rw matching; explicit Polynomial.aeval fixes it. Failed initial build/profile requests are excluded; corrected successful gates and all request drain are recorded in the dedicated report.

Actual corrected final repository-module profile exits 0 (`/private/tmp/roth-separation-d15-final-profile-fixed.log{,.json}`): degreeOf_rename_mul_aeval 16.682 + 106.199 = 122.881 ms, degreeOf_none_rename_mul_aeval 27.223 + 171.228 = 198.451 ms. Both below 750/1000 ms; removed target baseline 128.446 ms and no final target cost. Caller timings increased relative to this prior sample; library reuse/removal is claimed, no speedup claim. No source profiler scaffolding or raised limits.

Source FROZEN SHA256 `7089df105ebdca3d3358741fa4a574aa44a6f07c870d24838028eb550cac6960`; leaf ownership revoked and requests drained before owner gates. Owner probe `89268` exit0,58.49s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d15-compatibility.{lean,log,json}`. Owner build session `10803` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,147.67s/37.60s; source hash stable. `/private/tmp/roth-separation-d15-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem instance omissions and optional aeval_X_eq_rename deletion. Refresh the latter historical D12 candidate/caller inventory against current source before any approved application. Header remains user-preserved.


## Separation d16 checkpoint — hasseDeriv_rename_mul_aeval

[Dedicated audit](cleanup/Separation-hasseDeriv_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; The support-disjointness side proof uses one simp instead of rintro plus simp; two proof lambda arrows normalized and signature whitespace packed. Proof one line shorter, source 555 to 553 (Git +6/−8), 23 retained. Exact original effective public type and all documentation preserved; no new helper. Source 555 → 553; 23 retained declarations. Separation 16/30, overall 167/264 original audits after successful publication; 8/14 files complete.

Actual final module build exits 0 (`/private/tmp/roth-separation-d16-final-build-fixed.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-native-lsp.json`). Fresh copied original type/non-self proof and actual target standard-axiom checks exit 0 (`...-final-independent.lean.verified.log`). All binder probes recorded; invalid racing Sort probes replaced by actual Type/Sort mismatch rechecks (`...-probes.json`, `...-recheck.json`). Individual/joint instance omissions and Finite replacement compile but remain pending/unapplied. All requests drained before source freeze and owner gates.

Actual final repository-module profile exits 0 (`/private/tmp/roth-separation-d16-final-profile-fixed.log{,.json}`): command 101.919 + async 602.561 = 704.480 ms, one anchor each, below 750/1000 ms. Prior actual target baseline 275.492 ms; no speedup claimed. No profiling scaffolding, raised limits or target deferral. File-wide final isolated sweeps remain mandatory.

Source FROZEN SHA256 `a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`; leaf ownership revoked and requests drained before owner gates. Owner probe `94037` exit0,34.72s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d16-compatibility.{lean,log,json}`. Owner build session `72373` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,111.23s/28.20s; source hash stable. `/private/tmp/roth-separation-d16-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem instance omissions and optional aeval_X_eq_rename deletion. Refresh historical wrapper-deletion candidate/caller inventory against current source before any approved application. Header remains user-preserved.


## Separation d17 checkpoint — coeff_uniqueAlgEquiv_symm

[Dedicated audit](cleanup/Separation-coeff_uniqueAlgEquiv_symm.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original coefficient specialization retained byte-identically after full audit. Existing MvPolynomial theorem and Finsupp.single_eq_same already prove it; no project caller uses the Roth wrapper. Full-module deletion candidate compiles but is a separate unapproved public API option. Source unchanged at 553 lines, 23 retained declarations. Source 553 → 553; 23 retained declarations. Separation 17/30, overall 168/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d17-build.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-lsp.json`). Exact original type and independent non-self proof compile natively and via final CLI; actual target and independent proof use standard three axioms (`...-independent-final.log`). All binder/search/literature/width/inequality/completion evidence in dedicated report. Full-module deletion proposal `...-delete-proposal.{lean,log}` compiles exit 0, source untouched. Owner independently verifies every project coefficient reference is explicitly MvPolynomial-qualified.

Unchanged source and target reuse the valid actual repository-module profile `/private/tmp/roth-separation-d16-final-profile-fixed.log{,.json}`: command 11.337 + async 10.160 = 21.497 ms, one anchor each, below 750/1000 ms. No unnecessary repeated profile, profiler scaffolding, raised limit or performance deferral.

Source FROZEN SHA256 `a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`; leaf ownership revoked and requests drained before owner gates. Owner probe `80848` exit0,37.50s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d17-compatibility.{lean,log,json}`. Owner build session `63509` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,6.89s/3.08s; source hash stable. `/private/tmp/roth-separation-d17-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Three public options remain pending and unapplied: 12-theorem instance omissions, optional aeval_X_eq_rename deletion, and optional unused coeff_uniqueAlgEquiv_symm deletion. The latter needs no caller edit and has a full compiled module candidate. Refresh historical wrapper-removal candidates against current source before any approved application. Header remains user-preserved.


## Separation d18 checkpoint — degreeOf_uniqueAlgEquiv_symm

[Dedicated audit](cleanup/Separation-degreeOf_uniqueAlgEquiv_symm.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Coefficient-vanishing criterion replaces the zero/nonzero leading-coefficient branch. Final proof uses mathlib coefficient/support lemmas directly, preserving independence from the pending unused public wrapper deletion. Proof 12 to 10 physical lines, declaration 14 to 12, source 553 to 551; 23 retained declarations. Public type/docs unchanged, no helper. Source 553 → 551; 23 retained declarations. Separation 18/30, overall 169/264 original audits after successful publication; 8/14 files complete.

Actual final module build exits 0 (`/private/tmp/roth-separation-d18-build-final.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 baseline warnings (`...-direct-final-lsp.json`). Explicit original effective type and independent non-self proof compile; actual built target and independent proof use only standard three axioms (`...-direct-independent-retry.log`). All binder, five-search and public literature evidence recorded. A superseded 549-line proof used the public wrapper; owner requested direct mathlib reuse, compiled and applied before fresh final gates. Earlier 13-to-11 line estimate corrected by actual Git arithmetic.

Actual accepted final repository-module profile exits 0 (`/private/tmp/roth-separation-d18-direct-final-profile.log{,.json}`): command 12.344 + async 23.659 = 36.003 ms, baseline 72.019 ms, one anchor each and below 750/1000 ms. Earlier 74.166 ms belongs to the superseded wrapper-dependent candidate and is excluded as final evidence. No profiler scaffolding or raised limits.

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `59024` exit0,45.72s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d18-compatibility.{lean,log,json}`. Owner build session `2299` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.62s/29.26s; source hash stable. `/private/tmp/roth-separation-d18-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

All three public options remain pending and unapplied: 12-theorem instance omissions and the two optional public wrapper deletions. Fresh owner rg confirms coefficient references remain explicitly MvPolynomial-qualified; the unused Roth wrapper gained no caller. Refresh historical deletion candidates before any approved application. Header remains user-preserved.


## Separation d19 checkpoint — degreeOf_rename_mul_aeval

[Dedicated audit](cleanup/Separation-degreeOf_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Proof retained byte-identically after full direct-API/automation audit; no source edit or helper. Stronger generality is compiled as an unapproved grouped public option, not applied. Source unchanged at 551 lines and 23 declarations, all original public types/docs retained. Source 551 → 551; 23 retained declarations. Separation 19/30, overall 170/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d19-build.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 warnings (`...-final-lsp.json`). Exact original type and independent non-self proof compile; actual target and independent proof use standard three axioms (`...-independent.{lean,log}`). Every binder probe completed; no-zero-divisors condition tested, hV removal independently refuted by compiled V=0/U=X integer counterexample. Full-module grouped coefficient proposal (`...-domain-proposal.{lean,log}`) exits 0 with both actual printed weaker types and standard axioms: only Domain section CommRing/IsDomain changed to CommSemiring/NoZeroDivisors, Fintype/DecidableEq and both existing proofs retained. Arbitrary-τ combined isolated candidate also passes (`...-weakest.{lean,log}`).

Unchanged actual source/target reuses valid repository-module profile `/private/tmp/roth-separation-d18-direct-final-profile.log{,.json}`: command 13.297 + async 118.049 = 131.346 ms, one anchor each, below 750/1000 ms. No unnecessary repeat profile, source scaffolding, raised limits or target deferral.

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `75014` exit0,34.54s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d19-compatibility.{lean,log,json}`. Owner build session `45446` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.75s/2.65s; source hash stable. `/private/tmp/roth-separation-d19-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Four public options remain pending/unapplied: 12-theorem index-instance omissions, two optional public wrapper deletions, and grouped Domain coefficient weakening for d19+d20 to CommSemiring/NoZeroDivisors. The coefficient option is independently compiled with original variable instances retained. No approval inferred from successful probes. Header remains user-preserved.


## Separation d20 checkpoint — degreeOf_none_rename_mul_aeval

[Dedicated audit](cleanup/Separation-degreeOf_none_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Distinguished-variable product-degree proof retained unchanged after full direct-API, automation and transport review. Original nonzero hU, effective public type and docs preserved; no helper or source edit. Source 551 lines, 23 retained declarations. Source 551 → 551; 23 retained declarations. Separation 20/30, overall 171/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d20-build.log`). Fresh complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-lsp.json`). Exact original type/non-self proof, separate hU=0 counterexample and actual built target/independent standard-axiom checks exit 0 (`...-independent.{lean,log}`). All 15 binder probes completed (`...-probe-results.json`): weaker coefficient and index-instance options compile but remain pending; Ring/dropped coefficient/dropped domain structures fail with actual diagnostics. All requests drained before freeze.

Unchanged actual source/target reuses repository-module profile `/private/tmp/roth-separation-d18-direct-final-profile.log{,.json}`: command 17.385 + async 182.839 = 200.224 ms, anchors 216610/219922, below 750/1000 ms. No unnecessary profile repeat, source scaffolding, raised limits or performance deferral.

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `76196` exit0,34.50s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d20-compatibility.{lean,log,json}`. Owner build session `12121` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.58s/2.79s; source hash stable. `/private/tmp/roth-separation-d20-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

All four public options remain pending/unapplied: 12-theorem instance omissions, two public wrapper deletions, and grouped Domain coefficient weakening to CommSemiring/NoZeroDivisors (full-module d19 candidate already compiled). Header remains user-preserved. Original 21 performance/decomposition and fresh audits of any added helpers remain next, with original counts preserved.


## Separation d21 checkpoint — exists_separated_representation

[Dedicated audit](cleanup/Separation-exists_separated_representation.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Decomposed original64-line public proof into30-line proof and two freshly independently audited private helpers. A third newly added helper was independently audited and removed in favor of imported restrictSupport. Original public type/docs retained; no original-count inflation. Source 551 → 573; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Original21 and all three new-helper fresh audits completed full24/42/five-search/binder/width/inequality/11step workflow. Actual module builds, exact-original independent non-self proofs and actual built standard-axiom checks passed. Final fresh helper complete unfiltered LSP0errors/31warnings; owner complete native diagnostics likewise0/31. Final SHA36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17; all leaf ownership revoked and all requests drained.

Actual isolated final owner sweep /private/tmp/roth-separation-d21-owner-profile.log exit0: independence312.549ms, reconstruction718.272ms, public main895.154ms. Same-final-source preceding isolated main repeats844.929/853.337ms meet the >=750 repeat rule; every affected declaration below1000ms. No raised limits, source profiler scaffolding or deferral.

Source FROZEN SHA256 `36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17`; leaf ownership revoked and requests drained before owner gates. Owner probe `88657` exit0,37.80s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d21-compatibility.{lean,log,json}`. Owner build session `56384` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,115.49s/28.60s; source hash stable. `/private/tmp/roth-separation-d21-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

User explicitly approved exact12-theorem instance menu during helper audits. None applied in this frozen batch: nine already-audited targets will receive separate dependency/source-ordered revisit checkpoints next; three upcoming targets at ordinary audit. Optional public-wrapper deletions and Domain coefficient weakening remain unapproved/unapplied; header preserved.


## Separation r01 checkpoint — eq_mapDomain_some_add_single

[Dedicated audit](cleanup/Separation-approved-instances-eq_mapDomain_some_add_single.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT1/9 (original2): removed both Fintypeτ and DecidableEqτ by one scoped omit before preserved docstring. Proof byte-identical, no local classical or caller repair needed; original audit count remains21/30. Source 573 → 574; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh dedicated full24/42/five-search/binder/literature/width/inequality/11step audit. Actual module build93323 exit0; complete unfiltered native LSPsuccess=true partial=false timed_out=false no failed dependencies,0errors28warnings (31→28). Fresh independent exact NEW arbitraryτ proof, original snapshot proof with explicit ORIGINAL class-argument adapter, infinite-index use and actual built target+expansion-caller standard3axiom checks15138 exit0; /private/tmp/roth-separation-r01-verify.{lean,log}. All jobs drained and ALL leaf source ownership revoked; SHAb0d740f0e8638621a0fcbe68ac01235846bdde1ef27fb27b756d310b4af2dd0d.

Actual isolated repository-module profile10704 exit0 /private/tmp/roth-separation-r01-profile.log{,.json}: target21.552+94.276=115.828ms; affected expansion caller23.539+74.836=98.375ms. Both below750/1000ms; no repeat required, limits or scaffolding.

Source FROZEN SHA256 `b0d740f0e8638621a0fcbe68ac01235846bdde1ef27fb27b756d310b4af2dd0d`; leaf ownership revoked and requests drained before owner gates. Owner probe `63261` exit0,48.96s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r01-compatibility.{lean,log,json}`. Owner build session `8377` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.57s/29.09s; source hash stable. `/private/tmp/roth-separation-r01-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-theorem instance menu USER APPROVED; this is first application, remaining targets retain their individual validation/checkpoint sequence. Other public API options remain unapproved/unapplied; no original-count increment. Next coeff_coeffNone approved instance revisit. Header unchanged.


## Separation r02 checkpoint — coeff_coeffNone

[Dedicated audit](cleanup/Separation-approved-instances-coeff_coeffNone.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT2/9 (original7): one scoped omit removes Fintypeτ/DecidableEqτ; proof and original docs unchanged. Original audit count remains21/30. User decisions closing optional wrapper deletions and coefficient-domain widening are recorded as considered/declined. Source 574 → 575; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual module exit0 /private/tmp/roth-separation-r02-module.log. Complete native final-lsp.json0errors27warnings: three target warnings removed, two already-approved future caller unusedSectionVars warnings exposed in eq_sum_X_none_pow_mul_coeffNone and coeff_rename_mul_aeval. Independent exact NEW arbitraryτ type/nonself proof/explicit ORIGINAL class-order adapter and built target+two callers standard3axioms pass; ...-independent.{lean,log}. Fresh10binderprobes ...-probes.json. All requests drained/ALL leaf ownership revoked; SHAe3da33d7e951239837ba563ea0e8d6bb8fa783ef9bf6c0781bdce51588dce029.

Actual isolated /private/tmp/roth-separation-r02-profile.log{,.json} exit0: outeromit7.736ms+async79.367ms=87.103ms, anchors55949/55975. Inner6.833ms command excluded from sum. Below750/1000ms; no resweep, limits or scaffolding.

Source FROZEN SHA256 `e3da33d7e951239837ba563ea0e8d6bb8fa783ef9bf6c0781bdce51588dce029`; leaf ownership revoked and requests drained before owner gates. Owner probe `25584` exit0,42.40s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r02-compatibility.{lean,log,json}`. Owner build session `72584` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.83s/27.79s; source hash stable. `/private/tmp/roth-separation-r02-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

USER DECISION: both optional public-wrapper deletions (aeval_X_eq_rename and Roth.coeff_uniqueAlgEquiv_symm) and two-theorem CommSemiring/NoZeroDivisors widening considered/DECLINED; preserve names and CommRing/IsDomain assumptions. No pending required API decision. Nat codomain unchanged. Exact12instance menu remainsapproved; next expansion bridge revisit.


## Separation r03 checkpoint — eq_sum_X_none_pow_mul_coeffNone

[Dedicated audit](cleanup/Separation-approved-instances-eq_sum_X_none_pow_mul_coeffNone.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT3/9 (original8): removed both Fintypeτ/DecidableEqτ with one scoped omit; existing proof/localclassical/docstring unchanged. Original audit count remains21/30. Source 575 → 576; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual module exit0 ...-r03-module.log; complete native final-lsp.json0errors25warnings0infos. Exact NEW arbitraryτ independent nonself proof, explicit ORIGINAL classadapter and9actual suffixresolved standardaxiom checks exit0 (...-independent.{lean,log},...-actual-axioms.{lean,log});11binderprobes plus corrected dropτ retry. All jobs drained/ALL sourceownership revoked; SHA695da96521c7eb9a07f5f8271868cd37360e9db65a0c5ca0398aa609ee62e507.

Two sequential isolated actual repository sweeps /private/tmp/roth-separation-r03-profile{,-repeat}.log{,.json} exit0: target92.703/96.229ms; directcaller exists_separated_representation847.714/767.519ms; basishelper795.787/709.339ms; exists_det495.352/444.682ms. Required>=750repeat satisfied;25anchored rows each, no>=1000. Repeat raw3invalidUTF8bytes in nestedtrace handled by documented replacement parser without alteringASCIIanchors; no source scaffolding/limits.

Source FROZEN SHA256 `695da96521c7eb9a07f5f8271868cd37360e9db65a0c5ca0398aa609ee62e507`; leaf ownership revoked and requests drained before owner gates. Owner probe `75432` exit0,47.70s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r03-compatibility.{lean,log,json}`. Owner build session `20590` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,122.33s/31.92s; source hash stable. `/private/tmp/roth-separation-r03-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved, three dependency-ordered revisits applied. Optional wrapper deletions and Domain coefficient widening explicitly considered/DECLINED, Natcodomain unchanged. No requireduserinput pending. NextdegreeOf_coeffNone_le approvedrevisit; originalcount unchanged.


## Separation r04 checkpoint — degreeOf_coeffNone_le

[Dedicated audit](cleanup/Separation-approved-instances-degreeOf_coeffNone_le.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT4/9 (original9): removed both index instances with a single scoped omit; proof/docstring unchanged. Original audit count remains21/30. Source 576 → 577; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual module build exit0 ...-r04-build.log; complete native final-lsp.json0errors22warnings (25baseline). Independent exact NEW arbitraryτ type and independent NEW/ORIGINAL supremum proofs, explicit ORIGINAL ft/de/cs adapter and actualtarget/conservative downstream standardaxioms pass (...-independent.{lean,log}). All jobs drained/ALL sourceownership revoked; SHA3c5bbe4d1706e8c7f0c392ceabc1f23565e5e70f295d6dd5f65d5deee3637eac.

Actual isolated repository-module /private/tmp/roth-separation-r04-profile.log{,.json} exit0: targetoutercommand3.629+outerasync29.701=33.330ms. All25retainedrows below750ms; no repeat required and no1000msviolations, profiler scaffolding or limitraise.

Source FROZEN SHA256 `3c5bbe4d1706e8c7f0c392ceabc1f23565e5e70f295d6dd5f65d5deee3637eac`; leaf ownership revoked and requests drained before owner gates. Owner probe `12312` exit0,50.42s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r04-compatibility.{lean,log,json}`. Owner build session `24948` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,118.53s/31.91s; source hash stable. `/private/tmp/roth-separation-r04-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved; four revisits applied. Optional wrapper deletions and Domain coefficient widening considered/DECLINED, Natcodomain unchanged, no requireduserinput pending. Nextcoeff_rename_mul_aeval approvedrevisit.


## Separation r05 checkpoint — coeff_rename_mul_aeval

[Dedicated audit](cleanup/Separation-approved-instances-coeff_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT5/9 (original10): one scoped omit removes both index instances; proof/docs unchanged, no classical/helper/caller repair. Original audit count remains21/30. Source 577 → 578; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual Roth.Separation and Roth.Theta builds exit0; complete native Separation0errors20warnings and Theta0errors28warnings (...-final-lsp.json,...-theta-lsp.json). Three targetwarnings removed, one future exists_int_factors unusedSectionVars warning exposed. Exact NEW arbitraryτ assignment/nonself proof/explicit ORIGINAL classadapter and actualtarget/bridges/exists_int_factors/index_det_le standardaxioms pass (...-independent.{lean,log},...-caller-axioms.{lean,log}). Complete external Theta result independently checked by owner; source/contracts untouched. All jobs drained and sourceownership revoked; SHA9893814b3228a24b031753f740a8755c7feabd522791ab5563fe74b09c2e0b01.

Actual isolated /private/tmp/roth-separation-r05-profile.log{,.json} exit0: targetoutercommand31.048+outerasync152.492=183.540ms, two command/oneproof anchors with nested command excluded. Below750/1000ms; no resweep, raisedlimits or scaffolding.

Source FROZEN SHA256 `9893814b3228a24b031753f740a8755c7feabd522791ab5563fe74b09c2e0b01`; leaf ownership revoked and requests drained before owner gates. Owner probe `60429` exit0,42.21s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r05-compatibility.{lean,log,json}`. Owner build session `21232` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,79.22s/28.12s; source hash stable. `/private/tmp/roth-separation-r05-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved; five dependency/source-ordered revisits applied. Optional wrapper deletions and Domain coefficient widening considered/DECLINED; Natcodomain unchanged; no requiredinputpending. NexthasseDeriv_rename_mul_aeval approvedrevisit.


## Separation r06 checkpoint — hasseDeriv_rename_mul_aeval

[Dedicated audit](cleanup/Separation-approved-instances-hasseDeriv_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT6/9 (original16): removed both ambient index instances with scoped omit and minimal local classical; mathematical proof and original docs otherwise unchanged. Original audit count remains21/30. Source 578 → 580; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full audit covers all 24 audit items, 42 golf rules, five actual searches, effective binders, literature, width/inequality checks and 11 completion steps. Actual module build exits 0; complete native LSP reports 0 errors/18 warnings (20 baseline): three target warnings removed and one upcoming determinant caller unusedSectionVars warning exposed; its contract stays unchanged. Exact NEW arbitrary-τ proof and explicit ORIGINAL class adapters pass native/compiler; the initial scratch universe mismatch is excluded and its corrected result retained. Actual target and determinant caller axioms are exactly the standard three. Fifteen corrected binder probes have actual results. Evidence: /private/tmp/roth-separation-r06-{independent.lean,independent.log,native-independent-fixed.json,probes.json}. All requests drained and ALL leaf source ownership revoked; SHA187f69cba6b1e16d665130375348c4038f3aa5cd7a3cb8d650e3e055b2a5bf7d.

Actual isolated repository-module /private/tmp/roth-separation-r06-profile.log{,.json} exit0: target40.276+341.592=381.868ms; direct determinant caller84.137+405.262=489.399ms. Both below750/1000ms; no repeat required, limits or source scaffolding.

Source FROZEN SHA256 `187f69cba6b1e16d665130375348c4038f3aa5cd7a3cb8d650e3e055b2a5bf7d`; leaf ownership revoked and requests drained before owner gates. Owner probe `98402` exit0,43.30s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r06-compatibility.{lean,log,json}`. Owner build session `84517` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.76s/28.80s; source hash stable. `/private/tmp/roth-separation-r06-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved; six revisits applied. Optional wrapper deletions and Domain coefficient widening considered/DECLINED; Nat codomain unchanged; no required user input pending. Next degreeOf_rename_mul_aeval approved revisit; preserve current coefficient assumptions.


## Separation r07 checkpoint — degreeOf_rename_mul_aeval

[Dedicated audit](cleanup/Separation-approved-instances-degreeOf_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Approved instance revisit 7/9 (original19): scoped omit and local classical remove both ambient index instances. Current CommRing/IsDomain assumptions, nonzero hypothesis, proof and original docs otherwise preserved. Original audit count remains21/30. Source 580 → 582; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh audit covers all24 items,42 golf rules,five actual searches,every effective binder,literature,width/inequalities and11 steps. Actual module build exits0; complete native LSP0errors/15warnings/0infos, partial=false/timed_out=false and no failed dependencies. Exact NEW arbitrary-τ @type/nonself proof, explicit ORIGINAL Fintype/DecEq adapter and built target/exists_det_eq_mul standard-three axioms pass (...-independent.lean/.log). All16 compiler probes drained; counterexample confirms hV cannot be dropped. No external direct caller or helper. ALL source ownership revoked and requests drained; SHA700e71b2e6acaec6767a0bd483fd17ee0e029340a4b3e745831542b8cc720ab5.

Actual isolated /private/tmp/roth-separation-r07-profile.log{,.json} exit0: outer omit command17.912ms at200422 + outer async110.900ms at200459 =128.812ms. Inner16.381ms command excluded. Below750/1000ms; no repeat, raised limits or scaffolding.

Source FROZEN SHA256 `700e71b2e6acaec6767a0bd483fd17ee0e029340a4b3e745831542b8cc720ab5`; leaf ownership revoked and requests drained before owner gates. Owner probe `55892` exit0,42.65s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r07-compatibility.{lean,log,json}`. Owner build session `59964` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.36s/27.69s; source hash stable. `/private/tmp/roth-separation-r07-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-instance menu approved; seven revisits applied. Both wrapper deletions and coefficient-domain widening considered/declined, Nat codomain unchanged; no required input pending. Next degreeOf_none_rename_mul_aeval approved revisit.


## Separation r08 checkpoint — degreeOf_none_rename_mul_aeval

[Dedicated audit](cleanup/Separation-approved-instances-degreeOf_none_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Approved instance revisit 8/9 (original20): scoped omit plus local classical remove both ambient index instances. All other source bytes, coefficient assumptions and docs preserved. Original audit count stays21/30. Source 582 → 584; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/five-search/binder/literature/width/inequality/11-step audit. Actual module build exits0; complete native LSP0errors/12warnings/0infos, no partial/timeout/failed dependencies. Exact NEW arbitrary-τ type/nonself proof, explicit full ORIGINAL binder-order forall adapter, independent ORIGINAL proof, hU counterexample and actual target/exists_det_eq_mul standard axioms pass. Evidence ...-r08-{contract.lean,contract-final.log,probe-results.json}. All requests drained; ALL source ownership revoked; SHA49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74.

Two isolated actual repository sweeps exit0: /private/tmp/roth-separation-r08-profile{,-final}.log{,.json}. Target194.041→166.317ms (final23.747+142.570; anchors225752/225790); caller488.675ms final. Reconstruction770.520→699.921ms, main824.040→814.956ms; both repeated below1000. Untouched upcoming exists_int_factors679.320→754.519ms remains for ordinary29/final-file sweep. All25 command and24 theorem-proof anchors present. First raw trace has3 malformed nested UTF8 bytes handled by documented replacement-only parser; final raw is validUTF8 and supplied strict parser passes. No limit raise/scaffolding.

Source FROZEN SHA256 `49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74`; leaf ownership revoked and requests drained before owner gates. Owner probe `60715` exit0,39.76s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r08-compatibility.{lean,log,json}`. Owner build session `5802` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,118.81s/28.04s; source hash stable. `/private/tmp/roth-separation-r08-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-instance menu approved; eight revisits applied. Both public-wrapper deletions and coefficient-domain widening considered/declined; Nat codomain unchanged. No required input pending. Next final approved revisit exists_separated_representation, then ordinary original22.


## Separation r09 checkpoint — exists_separated_representation

[Dedicated audit](cleanup/Separation-approved-instances-exists_separated_representation.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Approved instance revisit9/9 (original21): only one scoped omit line; proof and both previously independently audited helpers unchanged. Original audit count remains21/30. Explicit structure flag retained for the30-line named headline theorem; a dedicated private refactor/fresh helper audit will close the15-line target before final file completion. Source 584 → 585; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/five actual searches/every binder/literature/width/inequality/11-step audit. Module build exits0; complete unfiltered native LSP0errors/9warnings/0infos with no partial/timeout/failed dependencies. Independent arbitrary-τ proof with copied audited helpers, original64-line proof, full ORIGINAL binder-order adapter and actual target/twohelpers/exists_det_eq_mul standard axioms pass (...-r09-contract-final.log,...-original-independent.log). All13 binder probes and valid explicit IsField equivalent pass/fail as documented; no external direct caller. All requests drained and ALL source ownership revoked; SHAd30464cac2d8d49bcaeb4f7edc0d35469af4c36189acbe93edf4a7ea0f1b1b91.

Two sequential isolated actual repository sweeps /private/tmp/roth-separation-r09-profile{,-repeat}.log{,.json} exit0, validUTF8 with all25 anchored declarations, none>=1000. Main29.717+762.489=792.206ms then30.633+738.006=768.639ms (repeat anchors413876/413965). Coordinatehelper270.805/274.433; reconstruction699.461/686.714; actualcaller473.548/506.194. >=750 repeat satisfied; no raised limits or scaffolding.

Source FROZEN SHA256 `d30464cac2d8d49bcaeb4f7edc0d35469af4c36189acbe93edf4a7ea0f1b1b91`; leaf ownership revoked and requests drained before owner gates. Owner probe `56755` exit0,39.91s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r09-compatibility.{lean,log,json}`. Owner build session `81056` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,119.01s/32.93s; source hash stable. `/private/tmp/roth-separation-r09-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

All nine already-audited approved instance revisits now applied. Remaining approved targets are ordinary22det_hasseDeriv_separated and29exists_int_factors (both instances),30exists_det_eq_mul (DecEq only, retainFintype). Dedicated private headline-proof decomposition will close the explicit structure flag; all added helpers require fresh audits and all affected gates before publication. Both wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged, no required user input.


## Separation s21 checkpoint — exists_separated_representation

[Dedicated audit](cleanup/Separation-structure-exists_separated_representation.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private structure completion for original21: main30→14 bodylines, new exists_coeffNone_basis_aux21 bodylines; public type/docs and existing helpers unchanged, shared expansion reused. New helper receives full fresh independent audit and is retained unchanged. Headline15-line flag closed; correlated existential conjunction splitting is mathematically inapplicable, not pending. Original audit count remains21/30. Source 585 → 597; 26 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Dedicated structure and fresh independent helper audits complete all24/42/five searches/binders/width/inequality/11steps, with public literature/private exemption respectively. Actual module builds, exact current public arbitrary-τ nonself proof, original helper type+independent proof, actual helper/existinghelpers/main/caller standard axioms pass. Complete fresh unfiltered native LSP0errors9preservedwarnings. Evidence /private/tmp/roth-separation-s21-{build.log,independent.log,axioms.log}, /private/tmp/roth-s21-helper-{module-build.log,type-axioms.log,native-final.json}. All requests drained; ALL leaf source ownership revoked; SHAdc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e.

Actual final isolated /private/tmp/roth-separation-s21-final-profile.log{,.json} exit0: newhelper55.134+591.316=646.450ms; main58.943+292.125=351.068ms; caller97.288+385.275=482.563ms. All affected below750/1000; unchanged fresh audit validly reuses this exact-source baseline. Earlier preliminary import-overlap profile excluded. No limits/scaffolding/deferral.

Source FROZEN SHA256 `dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`; leaf ownership revoked and requests drained before owner gates. Owner probe `99185` exit0,53.66s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-s21-compatibility.{lean,log,json}`. Owner build session `68108` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.18s/31.57s; source hash stable. `/private/tmp/roth-separation-s21-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Structure flag closed and all four historical added helpers independently audited (three retained, degree helper removed). Exact12-instance menu: nine revisits complete; upcoming ordinary22/29 remove both,30removeDecEq only retainFintype. Wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged. No required input pending. Next ordinary original22 with headline<=15 target.


## Separation d22 checkpoint — det_hasseDeriv_separated

[Dedicated audit](cleanup/Separation-det_hasseDeriv_separated.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original22 direct AlgHom.map_det proof shortens20→11 lines including :=by (19→10 lines below it), no helper. Declaration26→16 lines, plus approved scoped omit of both τ instances. Headline<=15 target met; docs/math/coefficient contract preserved. Source 597 → 588; 26 retained declarations. Separation 22/30, overall 173/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual native searches/every binder/literature/width/inequality/11step audit. Actual module build exits0 (...-s22-build.log); complete unfiltered native LSPsuccess=true,partial=false,timed_out=false,no failed dependencies,0errors/6preservedwarnings/0info/0hint. Independent arbitrary-τ nonself proof, EXACT ORIGINAL full-class-order adapter and explicit Unit/ℚ full-instance application compile0 (...-s22-independent.lean/.log); built target/internal exists_det_eq_mul caller and independent/adapter axioms standard only. No external direct caller by whole-repository search. No new helper. All requests drained and ALL source ownership revoked; SHA4784c8e32e2e6662d5283fed9aebd68d72b4ce7ba0054b65b11d7a210e595449.

Final isolated actual repository /private/tmp/roth-s22-final-profile.log{,.json} exit0: target56.067+382.136=438.203ms vs baseline420.030ms; caller132.609+377.792=510.401ms. Both below750/1000, no repeat required. No timing speedup claimed, limits/scaffolding/deferral.

Source FROZEN SHA256 `4784c8e32e2e6662d5283fed9aebd68d72b4ce7ba0054b65b11d7a210e595449`; leaf ownership revoked and requests drained before owner gates. Owner probe `99849` exit0,40.15s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d22-compatibility.{lean,log,json}`. Owner build session `46326` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,121.58s/28.20s; source hash stable. `/private/tmp/roth-separation-d22-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact instance menu now10/12 applied: nine revisits plus original22; remaining29both and30DecEq-only/retainFintype at ordinary audits. CommRing probe fails current statement at Field-bound wronskian, not mathematical impossibility; no upstream widening applied. Both wrapper deletions and two Domain coefficient widenings considered/declined; Nat codomain unchanged, no required input. Next original23 exists_sum_mul_eq_gcd.


## Separation d23 checkpoint — exists_sum_mul_eq_gcd

[Dedicated audit](cleanup/Separation-exists_sum_mul_eq_gcd.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original23 replaces18-line induction with one simpa using imported Finset.gcd_eq_sum_mul. Public type/docs retained, no helper or new omission. Source588→571, diff+1/-18. Source 588 → 571; 26 retained declarations. Separation 23/30, overall 174/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual native searches/every effective binder/literature/width/inequality/11step audit. Actual module build exits0; complete unfiltered native LSP0errors/6existing outside-target warnings, no partial/timeout/failed dependencies. Exact ORIGINAL copied nonself induction proof compiles and original/actual target equality rfl checks type; built target/direct same-file exists_int_eq_of_gcd_eq_one caller/independent proof standard-three axioms pass (...-s23-original-nonself.log). All requests drained and ALL source ownership revoked; SHAf03aa9bb53b186f2d5a5de7d7397589894aacf28f8c2cea2bbd3f0d1d2529f20.

Final isolated actual repository /private/tmp/roth-s23-final-profile.log{,.json} exit0: command9.730+outerasync87.199=96.929ms,1command/1proof anchor. Baseline122.345ms; both below750/1000. No repeat required or whole-project speedup claim; no raised limits/scaffolding.

Source FROZEN SHA256 `f03aa9bb53b186f2d5a5de7d7397589894aacf28f8c2cea2bbd3f0d1d2529f20`; leaf ownership revoked and requests drained before owner gates. Owner probe `30041` exit0,52.04s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d23-compatibility.{lean,log,json}`. Owner build session `55314` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.36s/30.76s; source hash stable. `/private/tmp/roth-separation-d23-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Concrete optional public-wrapper deletion candidate /private/tmp/roth-s23-deletion-candidate.lean compiled0 with full-file caller repair; .log/.diff and direct-references.log retained. Public deletion not approved/applied. Recommendation is to retain now-one-line orientation wrapper rather than remove public name for little code benefit; no required input/blocker. Prior two wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged. Menu remaining29both/30DecEq-only; next original24 exists_nat_smul_eq_map.


## Separation d24 checkpoint — exists_nat_smul_eq_map

[Dedicated audit](cleanup/Separation-exists_nat_smul_eq_map.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original24 inlines single-use hN0 and updates lambda arrows. Declaration22→21, source571→570. Public type/docs byte-preserved; no helper, public omission or proposal. Source 571 → 570; 26 retained declarations. Separation 24/30, overall 175/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual searches/every binder/literature/width/inequality/11step audit. Actual lake build Roth.Separation exits0 (...-d24-build.log). Corrected exact-original nonself proof, original compatibility and actual target/direct caller standard axioms exit0 (...-d24-independent-final.log); earlier scratch appendix with missing G argument excluded from successful evidence. Final complete unfiltered native LSPsuccess=true,partial=false,timed_out=false,no failed dependencies,0errors/6knownwarnings (...-d24-final-complete-lsp.json). No external direct caller. All requests drained and ALL source ownership revoked; SHA39e0e38b16b6b9b3b1feabe00fd135a8746c5f4cf60622c0b8fb46b9cf9f79ca.

Actual isolated repository /private/tmp/roth-d24-final-profile.log{,.json} exit0: target16.223+292.695=308.918ms, baseline380.252ms, below750/1000. Later corrected scratch harness/native checks did not change repository source or overlap profiler; valid exact-source sample retained. No repeat, limits, scaffolding or whole-project speedup claim.

Source FROZEN SHA256 `39e0e38b16b6b9b3b1feabe00fd135a8746c5f4cf60622c0b8fb46b9cf9f79ca`; leaf ownership revoked and requests drained before owner gates. Owner probe `16927` exit0,40.74s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d24-compatibility.{lean,log,json}`. Owner build session `70044` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,126.18s/28.72s; source hash stable. `/private/tmp/roth-separation-d24-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

No new public proposal/input. Exact instance menu remaining ordinary29both and30DecEq-only/retainFintype. Both earlier public-wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged. Optional d23 deletion compiled/unapplied, retention recommended, not required input. Next original25 exists_primitive_smul_eq; >30-line proof must decompose if still long and every new helper gets fresh audit.


## Separation d25 checkpoint — exists_primitive_smul_eq

[Dedicated audit](cleanup/Separation-exists_primitive_smul_eq.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original25 proof golf36→30 physical body lines (dispatch~38 was approximate), source570→564, diff+12/-18. Uses support_nonempty and shorter coefficient/support cases; no helper, API/type/doc change. Ordinary<=30 structure target met; branches remain<=10 and correlated existential outputs share witnesses. Source 570 → 564; 26 retained declarations. Separation 25/30, overall 176/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual searches/every effective binder/literature/width/inequality/11step audit. Actual module build exits0 (1876jobs; ...-d25-build.log). Independent exact ORIGINAL nonself proof/type and zero counterexample compile0; actual target/exists_int_factors direct caller standard-three axioms pass (...-d25-independent.lean/.log). Complete unfiltered native LSP0errors/6inheritedwarnings/0info, success=true,partial=false,timed_out=false,no failed dependencies. No external direct caller or new helper/proposal. All requests drained and ALL source ownership revoked; SHA3e4987354099a50db25afe7b1cd0c65b72ce37bd406fc4f62493b87ad624eafb.

Final isolated actual repository /private/tmp/roth-d25-final-profile.log{,.json} exit0: target26.260+637.051=663.311ms,1command/1proof anchors; directcaller84.313+625.115=709.428ms. Both below750/1000; no repeat required, raised limits or scaffolding. No proof-length-to-speedup inference.

Source FROZEN SHA256 `3e4987354099a50db25afe7b1cd0c65b72ce37bd406fc4f62493b87ad624eafb`; leaf ownership revoked and requests drained before owner gates. Owner probe `17212` exit0,40.75s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d25-compatibility.{lean,log,json}`. Owner build session `22435` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.51s/28.24s; source hash stable. `/private/tmp/roth-separation-d25-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

No new proposal/input. Exact instance menu remaining29both and30DecEq-only/retainFintype. Prior two wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged. Optional d23 deletion unapproved/unapplied and retention recommended. Next original26 exists_int_eq_of_gcd_eq_one.


## Separation d26 checkpoint — exists_int_eq_of_gcd_eq_one

[Dedicated audit](cleanup/Separation-exists_int_eq_of_gcd_eq_one.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original26 proof13→10 physical body lines, declaration15→12, source564→561. Removes intermediate sum equality/ring and uses mul_assoc with coefficient witnesses directly; only proof changes, no new helper/API/doc change. Source 564 → 561; 26 retained declarations. Separation 26/30, overall 177/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual searches/every binder/literature/width/inequality/11step audit. Actual final module build exit0 (...-d26-build-final.log). Independent exact ORIGINAL nonself proof and actual target/two public callers standard-three axioms compile0 (...-d26-independent.lean/.log). Complete unfiltered native LSP0errors/6known warnings, success=true,partial=false,timed_out=false,no failed dependencies (...-d26finaldiag-final.json). All requests drained, ALL source ownership revoked; SHA93d969933c89724c1c9d7a9ca23a76290e4af8bd3793307c34e95d3fbd1624dc.

Final isolated actual repository /private/tmp/roth-d26-final-profile.log{,.json} exit0: target15.045+104.543=119.588ms, baseline252.962ms; downstream anchors638.750/494.950ms. Below750/1000, no repeat trigger, limits or scaffolding. No whole-project speedup claim.

Source FROZEN SHA256 `93d969933c89724c1c9d7a9ca23a76290e4af8bd3793307c34e95d3fbd1624dc`; leaf ownership revoked and requests drained before owner gates. Owner probe `49673` exit0,40.60s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d26-compatibility.{lean,log,json}`. Owner build session `79694` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.15s/27.37s; source hash stable. `/private/tmp/roth-separation-d26-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Optional Ring-generalization exact candidate /private/tmp/roth-d26-generalized.lean freshly CLI compiled0 (...-generalized.log); no commutativity/CharZero needed. Public ℚ contract retained, proposal unapplied; separate enhancement recommended, no blocker. Earlier two wrapper deletions/Domain widenings declined; optional d23 deletion unapplied/retention recommended; remaining approved menu29both/30DecEq-onlyretainFintype. Next original27 private map_aeval_X_none.


## Separation d27 checkpoint — map_aeval_X_none

[Dedicated audit](cleanup/Separation-map_aeval_X_none.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original27 duplicate private evaluation-map lemma removed; sole exists_int_factors caller uses Polynomial.map_aeval_eq_aeval_map with Subsingleton.elim and map_X. Source561→553, retained26→25. No new helper/public contract/doc change. Source 561 → 553; 25 retained declarations. Separation 27/30, overall 178/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual searches/every binder/private literature exemption/width/inequality/11step audit. Actual module build exit0 (...-d27-module-build.log). Exact ORIGINAL private proposition independent native proof success (...-d27-independent-native.json). Fresh actual-built shell axioms exit0 (...-d27-actual-axioms.log): removed suffix0, caller/downstream/replacement standard only; stale native-import probe explicitly superseded. Complete unfiltered native LSP0errors/6knownwarnings/0info, complete/no failed dependencies (...-d27-final-lsp.json). All requests drained and ALL source ownership revoked; SHAf8eda96bc0bc19d15d9137243f08cbac7d3d5ad2e031077526262520abfcac23.

Final isolated actual repository /private/tmp/roth-d27-final-profile.log{,.json} exit0: removed target has no final cost; changed exists_int_factors64.279+606.011=670.290ms, unchanged downstream529.463ms. Below750/1000; no repeat, limits/scaffolding or whole-project speedup claim.

Source FROZEN SHA256 `f8eda96bc0bc19d15d9137243f08cbac7d3d5ad2e031077526262520abfcac23`; leaf ownership revoked and requests drained before owner gates. Owner probe `73423` exit0,39.39s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d27-compatibility.{lean,log,json}`. Owner build session `66697` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.48s/30.65s; source hash stable. `/private/tmp/roth-separation-d27-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

No new proposal/helper. Approved instance menu remains29both/30DecEq-onlyretainFintype. Prior two wrapper deletions/Domain widenings declined; optional d23 deletion and d26Ringwidening compiled/unapplied, retention recommended, no blocker. Next original28 private degreeOf_map_intCast.


## Separation d28 checkpoint — degreeOf_map_intCast

[Dedicated audit](cleanup/Separation-degreeOf_map_intCast.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original28 duplicate private degree-preservation wrapper removed; two callers use degrees_map_of_injective directly, second via degreeOf_def to avoid differing decidability reductions. Source553→551, retained25→24, diff+5/-7. No newhelper/publicsignature/docschange. Source 553 → 551; 24 retained declarations. Separation 28/30, overall 179/264 original audits after successful publication; 8/14 files complete.

Full fresh24/42/five actual searches/every binder/private literature exemption/width/inequality/11step audit. Actual final module build exit0 (...-d28-packed-build.log). Independent EXACT ORIGINAL private-type proof plus generic CommSemiring/injective-map proof and actual two callers standard-three axioms compile0 (...-d28-proof.log); suffix confirms removedconstant absent. Complete unfiltered native freezeLSP0errors/6unchangedwarnings/0info, success=true,partial=false,timed_out=false,no failed dependencies (...-d28-freeze_lsp.json). Allrequestsdrained, ALLsourceownershiprevoked; SHA4a1043e85ba9f8cc40be0801aa9bbc8e733f3ebc7beaf60449c884bad858e3b3.

Final isolated actual repository /private/tmp/roth-d28-final-profile.log{,.json} exit0: removed target has no finalcost; changedcaller exists_int_factors67.978+666.075=734.053ms, exists_det_eq_mul111.276+434.620=545.896ms. Both below750/1000; no repeat, limits/scaffolding or whole-project speedupclaim.

Source FROZEN SHA256 `4a1043e85ba9f8cc40be0801aa9bbc8e733f3ebc7beaf60449c884bad858e3b3`; leaf ownership revoked and requests drained before owner gates. Owner probe `18565` exit0,40.91s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL24 actual retained standardaxiom checks. `/private/tmp/roth-separation-d28-compatibility.{lean,log,json}`. Owner build session `84237` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.05s/28.75s; source hash stable. `/private/tmp/roth-separation-d28-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

No new proposal/helper. Approved menu remains29both/30DecEq-onlyretainFintype. Prior two wrapperdeletions/Domainwidenings declined; optional d23deletion/d26Ringwidening compiled/unapplied, retentionrecommended, no blocker. Next headline original29 exists_int_factors; <=15body target, fresh independent audit for any newprivatehelper BEFORE publication.


## Separation d29 checkpoint — exists_int_factors

[Dedicated audit](cleanup/Separation-exists_int_factors.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original29 headline proof46→15 physical body lines, all branches<=10; approved BOTH τ-instance removal and width repacking preserve remaining public contract/docs. Source551→548, retained24→26. Three new private stages received distinct fresh full independent audits: rescale retained/generalized privately to Field K/direct polynomials; coefficient stage15→8 via verified Polynomial.mem_map_range and its defining import; equality stage independently audited then removed/inlined (4-line branch). Only TWO added factor helpers retained; no unaudited helper or unresolved structure flag. Source 551 → 548; 26 retained declarations. Separation 29/30, overall 180/264 original audits after successful publication; 8/14 files complete.

Original29 leaf and all3 fresh helper audits passed full24/42/five actual searches/binders/private exemptions or public literature/width/inequality/11step workflow. Actual module builds, exact original29 fullclass-order and arbitraryτ NONSELF proofs, every newhelper INITIAL type independent proof, all affected actual standard axioms and removed equality-suffix absence pass. Complete final unfiltered native LSP0errors/3inheritedwarnings/0info (/private/tmp/roth-equality-final-lsp.json), success=true,partial=false,timed_out=false,no failed dependencies. Earlier overlapping rescale profile explicitly excluded; only drained evidence accepted. All leaf source ownership revoked and requests drained before OWNERfreeze SHA625a4b282d0e0e7ecb78a2e9f4eb3aec52ac14cc3cafae9eb1d21285d50977fc.

Fresh owner two uncontended actual repository sweeps /private/tmp/roth-separation-d29-owner-profile{1,2}.log(.json), profiles.json: both exit0, ALL26 command/proof anchors valid, raw UTF8 valid/no decoding replacements. Max741.362/699.251ms, all26 below750/1000. Actual main584.170/574.304; rescale479.379/472.941; coefficient327.013/318.693; caller30 518.777/538.195ms. Both final sweeps follow all helper changes; earlier borderline basis helper fully resampled, no performance deferral/limits/scaffolding or whole-project speedup claim.

Source FROZEN SHA256 `625a4b282d0e0e7ecb78a2e9f4eb3aec52ac14cc3cafae9eb1d21285d50977fc`; leaf ownership revoked and requests drained before owner gates. Owner probe `13106` exit0,51.21s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d29-compatibility.{lean,log,json}`. Owner build session `15497` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,116.89s/44.45s; source hash stable. `/private/tmp/roth-separation-d29-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact approved menu11/12 now applied; only upcoming original30 removes DecidableEq τ, RETAINS Fintype τ. All other public contracts/coefficient hypotheses preserved. Prior two public-wrapper deletions/Domain widenings declined; optional d23deletion/d26Ringwidening compiled/unapplied, retentionrecommended, no blocker. Next finalheadline original30 exists_det_eq_mul; <=15body and any newprivatehelpers require freshindependentaudit before publication.


## Separation d30 checkpoint — exists_det_eq_mul

[Dedicated audit](cleanup/Separation-exists_det_eq_mul.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original30 finalheadline proof27→11 bodylines, declaration35→18, two3linedegreebranches; approved ONLYDecidableEq τ omission while RETAININGFintype τ. Source548→560, retained26→27. ONEnewprivate rationalconstruction helper[Finiteτ]/20body independentlyfreshlyaudited/retainedunchanged; no otherhelper/Theta sourcechange. All public witnessorder/math/nonzero/degree/coefficient contracts/docs preserved. Source 548 → 560; 27 retained declarations. Separation 30/30, overall 181/264 original audits after successful publication; 8/14 files complete.

Original30leaf and distinctfreshhelper leaf full24/42/five actual searches/everybinder/literature-or-privateexemption/width/inequality/11steps complete. ActualSeparation andTheta modulebuilds0; exactORIGINAL bothclasses and approvednewtype independentNONSELFproofs0; INITIALhelper exact independentproof0; actualtarget/helper/index_det_le and REALdirectcaller index_le_lem6 standard-threeaxioms0. CompleteunfilteredLSPSeparation0errors/2preservedwarnings (...-d30-fresh-probe3.json), Theta0/28knownwarnings, success=true,partial=false,timed_out=false,nofaileddependencies. Allleafsourceownershiprevoked/requestsdrained; SHA2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1.

AcceptedisolatedactualSeparation threshold0 /private/tmp/roth-separation-d30-profile.log(.json): main173.686+133.513=307.199ms, newhelper118.975+377.575=496.550ms; exactsourceunchangedthroughfreshhelperaudit. Ownerparsedall27retainedanchors: max705.265ms, all27below750/1000,norepeattrigger. ExternalTheta actualthreshold0stalled/terminated130; boundedverifiedthreshold1ms runexit1(default200000heartbeat linarithsimplex in unchangedindex_le_lem6 lines604/617). DiagnosticONLY failed-runanchors index_det_le2055.175ms, directcaller index_le_lem610015.925ms; NOTaccepted successfulprofiles. OrdinaryTheta builds/completeLSP pass. NoThetaedits/limitraises; explicit NEXTTheta dedicatedperformancefollowup, no wholeprojectperformanceclaim.

Source FROZEN SHA256 `2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1`; leaf ownership revoked and requests drained before owner gates. Owner probe `26845` exit0,48.43s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d30-compatibility.{lean,log,json}`. Owner build session `71967` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,93.75s/32.91s; source hash stable. `/private/tmp/roth-separation-d30-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-instance menu nowALLapplied; publicFintype in exists_det_eq_mul deliberatelyretained. Prior two publicwrapperdeletions/Domainwidenings declined; optionald23deletion/d26Ringwidening compiled/unapplied, retentionrecommended. No requiredinput. Original30auditcountcompleteONLYaftersuccessfulpush; filefinalphasesstillrequired:freshindependentsimplifyreview, finalallprofiles/contracts/axioms/callerLSP/builds/report/push. NextfileTheta includesrecordedinstrumentedlinarithperformancework.


## Completed final file checkpoint

[Final phase report](cleanup/Separation-final.md): all30 original declaration audits,all8 historical
new-helper audits,all12 approved instance amendments and every final file phase complete
after successful publication. Source618→556;27 retained(20public,7private). Fresh independent
simplify applied direct rescale rewrites/import removal; owner normalized3ordinary lambdas.
FinalSHAdf4193795f1618f8f5cdbd71869583fc45d20a0a45c21f4b5eaf5f824133f37a. Alloriginal30 independentlyreproved,public20 recovered,actual27 standardaxioms
checked; ALL29 originalTheta public contracts/axioms additionallypass. Complete6-fileLSP
0errors,warningcounts2/28/3/4/0/0; full38.96s THEN separateLeanEval
51.62s both0. Actualtwofinalall27profiles maxima793.891/
717.493ms(<1000);46newreferencechecks compile. No unauditedhelper/structureflag.
Overall181/264 original declarations;9/14 files complete after finalpush. Header/Fintype
warnings intentionallyretained; actualexternalTheta instrumentedprofilefailure and
overbudgetdiagnostics explicitlyassignednextTheta file,notcalledsuccessfulsamples.
Project-endIndexrename remainsparentqueue. No requiredinputpending; nextfileTheta.


## Theta published history through original 19

The central Current status above is updated at every published declaration. This appended
history makes the Theta checkpoints visible alongside the earlier file history. At published
commit `4fd80e70d4da2022f1fd97875322e95f99549aa3`: **200/264 original declarations**,
**Theta 19/35**, **9/14 files complete**. Theta remains in progress; its inventory is
29 public plus 6 private original declarations. Eight approved revisits below do not increase
original counts. Full details and evidence are in [Theta's file report](cleanup/Theta.md)
and its linked dedicated audits.

| Original | Declaration | Overall originals after publication | Actual published commit |
|---:|---|---:|---|
| 1 | `RSet` | 182/264 | [08ab073](https://github.com/SmwYin/Roth/commit/08ab073cf398fea8f93cfdba17f6610b7eb61d05) |
| 2 | `indexSet` | 183/264 | [2f5160b](https://github.com/SmwYin/Roth/commit/2f5160ba344b3d5f023497a97ffdca773dd2cfbd) |
| 3 | `Θ` | 184/264 | [79b262c](https://github.com/SmwYin/Roth/commit/79b262cdf52b5db9b07e870d3ee4925ab138ba1d) |
| 4 | `map_intCast_real_ne_zero` (private wrapper deleted) | 185/264 | [7c36b31](https://github.com/SmwYin/Roth/commit/7c36b3129bc7b18d42a907e1a969add38db15157) |
| 5 | `degreeOf_map_intCast_real` (private wrapper deleted) | 186/264 | [dbfe215](https://github.com/SmwYin/Roth/commit/dbfe215f15e0ca4a5481ecd5bbd0434a81603c61) |
| 6 | `one_mem_RSet` | 187/264 | [a460063](https://github.com/SmwYin/Roth/commit/a4600633fbc0c15c131ec6e0d85fbe644a15303b) |
| 7 | `indexSet_nonempty` | 188/264 | [a4d22a3](https://github.com/SmwYin/Roth/commit/a4d22a3d162e1e93cd4a735c0eb66d16fb8e87b4) |
| 8 | `indexSet_bddAbove` | 189/264 | [692d63c](https://github.com/SmwYin/Roth/commit/692d63c0fcc4d064239cd7ebc3043e83841c7621) |
| 9 | `index_le_Θ` | 190/264 | [132df63](https://github.com/SmwYin/Roth/commit/132df630f7f677ae8afb08c57645ff7a3071d06b) |
| 10 | `Θ_nonneg` | 191/264 | [3dc739a](https://github.com/SmwYin/Roth/commit/3dc739abcf1291966e13b8223bdadc3bdad195ff) |
| 11 | `Θ_le_card` | 192/264 | [81ceeab](https://github.com/SmwYin/Roth/commit/81ceeab76d55cf73710d93ceee4b69294624f7bf) |
| 12 | `Θ_le_of_forall_index_le` | 193/264 | [4f15ff1](https://github.com/SmwYin/Roth/commit/4f15ff1ee078bdc4a63491b77bdb09500d8743d5) |
| 13 | `Θ_mono` | 194/264 | [1ca2873](https://github.com/SmwYin/Roth/commit/1ca2873855c5200fb62f203694821159b7f5bf2e) |
| 14 | `indexSet_comp_subset` | 195/264 | [e777d0a](https://github.com/SmwYin/Roth/commit/e777d0a740a8c39ee7acdd618eaad67e98ae613d) |
| 15 | `Θ_equiv` | 196/264 | [69a7271](https://github.com/SmwYin/Roth/commit/69a7271b5c0be978b59cb0fcd253a8545b89a163) |
| 16 | `isPrimitive_linear` | 197/264 | [7c5bc39](https://github.com/SmwYin/Roth/commit/7c5bc39f4a2542eb7283c84f8b2387117d682640) |
| 17 | `isPrimitive_pow` | 198/264 | [b7806ac](https://github.com/SmwYin/Roth/commit/b7806acc3b5fa15eef3f5424cbc2451b67162ff2) |
| 18 | `exists_eq_pow_mul_of_rootMultiplicity` | 199/264 | [ab9c01a](https://github.com/SmwYin/Roth/commit/ab9c01a9913d5309b27f35db846cfda82cf8977d) |
| 19 | `pow_rootMultiplicity_le` | 200/264 | [4fd80e7](https://github.com/SmwYin/Roth/commit/4fd80e70d4da2022f1fd97875322e95f99549aa3) |

Every published original received a fresh dedicated full audit, target module and complete
unfiltered diagnostics, independent immutable-original proof/type/value or authorized adapter
checks, actual standard-axiom checks, real accepted target profiling, then frozen sequential
full project build and separate LeanEval. Exact-path staging, commit and successful cleanup-branch
push preceded the next original edit. Evidence is target/caller scoped where stated; these
checkpoints do not claim final all-Theta profiling or a completed file-wide review.

Original 15 applied both approved DecEq omissions during its own audit. The eight subsequent
revisits of originals 6–13 were separately freshly audited and published, while original counts
remained at Theta 15/35 and overall 196/264:

| Revisited original | Exact applied scope | Actual published commit |
|---:|---|---|
| 6 | one_mem_RSet: DecEq σ and Fintype σ | [a646c9b](https://github.com/SmwYin/Roth/commit/a646c9b4393690e0c6501e9521f86cadf4b900d5) |
| 7 | indexSet_nonempty: DecEq σ | [3f577ac](https://github.com/SmwYin/Roth/commit/3f577acbfe25a9a11c829f334a0353fbc0432439) |
| 8 | indexSet_bddAbove: DecEq σ and hr | [c12193f](https://github.com/SmwYin/Roth/commit/c12193f2322542c9415892ee26354bf46532c74f) |
| 9 | index_le_Θ: DecEq σ, hr retained | [bbd4d8a](https://github.com/SmwYin/Roth/commit/bbd4d8a1d49b0527a8070f4b1412f1716cd60391) |
| 10 | Θ_nonneg: DecEq σ, hB/hr retained | [adaa875](https://github.com/SmwYin/Roth/commit/adaa87542f06102a2ef0364d63df2a817aff712f) |
| 11 | Θ_le_card: DecEq σ and hr, hB retained | [74fd327](https://github.com/SmwYin/Roth/commit/74fd327fad902ff31fe45f37a7ee4a6d7f75d2d0) |
| 12 | Θ_le_of_forall_index_le: DecEq σ | [85d940c](https://github.com/SmwYin/Roth/commit/85d940cc22e24a4eeb33e568d8b08c3456727698) |
| 13 | Θ_mono: DecEq σ, hB/hr retained | [f9be46d](https://github.com/SmwYin/Roth/commit/f9be46d32024200bf5cff25fbacf26d7b2625773) |

The explicit user decision selected all A removals (15 DecEq binders across 14 public
theorems), B's Fintype removal only for one_mem_RSet, and C's first five rows:
indexSet_bddAbove.hr; Θ_le_card.hr; exists_eq_pow_mul_of_rootMultiplicity.hR;
sum_max_sub_le_index_det.hR; index_det_le.hl′/hδ/unused implicitδ. Original 18 applied its
selected C.hR removal; the future original 27/28/29/30 rows still await their dedicated audits.
The user retained hq in index_le_lem6/Θ_option_le, Θ_nonneg.hB/hr, Θ_le_card.hB, and
Θ_mono.hB/hr; the extra D/E/F broadenings remain declined and unapplied.

The standing authorization was then updated: “From now on implement all changes that you
recommend. Only ask me if you can't decide.” It supersedes the earlier per-change approval
policy while preserving explicit earlier choices and all validation gates. Under that authority,
original 19 localized pow_rootMultiplicity_le.hB to the absolute leading coefficient after
concrete candidate, full-original adapter and caller evidence compiled. This strengthens the
theorem and is separate from the declined Θ-bound hypotheses. The old uniform coefficient
premise recovers the new premise at R.natDegree; Θ_unique_le's full old contract is retained.
See [the exact decision and application ledger](cleanup/Theta-contract-proposal.md).

Latest original 19 gates: module and complete unfiltered LSP: 0 errors / 18 warnings; immutable
independent original target/caller proofs, exact authorized new premise/full-old adapter/other
metadata and actual standard axioms pass. Repeated final prefix timings target 352.542/366.074 ms,
caller 820.803/829.009 ms; ≥750ms caller repeats pass below 1000 ms, with no speedup claim.
Frozen full build 77.364 s then separate LeanEval 24.504 s both exit 0, all 17 project/pin hashes stable.
Original 20 and any new-helper audits remain unpublished work at this historical snapshot.

Theta's final file phases and actual whole-module profiling are still outstanding. The known
late index_le_lem6 instrumented default-heartbeat failure and earlier index_det_le over-budget
diagnostics remain assigned to their dedicated audits; failed diagnostic samples are not
successful profiles. Header metadata and all earlier explicitly retained public wrappers/domains
remain unchanged. No new helper was introduced in published originals 1–19.


## Theta original20 checkpoint — one-variable bound and fresh helper audit

The headline `Θ_unique_le` proof is29→3 lines; only approved DecidableEq σ is removed.
Every other public hypothesis/domain/name/order/BinderInfo, including hB/hr/Fintype, remains.
The ONE new private `index_unique_le_log_div` has its own distinct fresh full audit: body26→23,
private positive-weight premise removed, coefficient premise localized to the univariate leading
coefficient. Initial-helper and immutable-original public contracts are independently reproved
and recovered by explicit adapters; actual selected type AST/retained metadata/standard axioms
all pass. No unaudited helper remains in this batch, and helper audits do not increase originals.
[Original audit](cleanup/Theta-Theta_unique_le.md),
[fresh helper audit](cleanup/Theta-index_unique_le_log_div-helper.md).

Final SHA `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`; complete native unfiltered LSP0errors17warnings
(success=true,partial=false,timed_out=false,faileddeps[]), with the intentional unused public hr
warning retained. Accepted final same-source prefix helper481.521ms/public73.124ms; combined
554.645ms, each below750/1000ms. Frozen full build39.883s then separate LeanEval15.025s both
exit0, all17project/pin hashes stable. Exact source/report staging and successful push publish
original20 before original21 edits. After publication: **201/264 originals,Theta20/35,9/14files**.
Actual whole-Theta profiling and15remaining originals/final file phases remain outstanding.
Next: public definition lem6M. The exact source-checkpoint commit link is appended immediately
after committing this validated batch, before its atomic branch push.

Original20 validated source/audit checkpoint: [7e27859](https://github.com/SmwYin/Roth/commit/7e27859b95d3a8c12b41559836262e6ddd5a13b9).
This following central-log metadata commit changes no Lean source; both commits are published
together in one push before original21 edits. Counts remain201/264,Theta20/35,9/14files.


## Theta original21 checkpoint — lem6M

Retained the one-line real coefficient-bound constant unchanged: it matches the paper’s equation (16), is reused by the main statements, and needs no extra abstraction or naming/API change. No source, caller, definition-value or documentation edits.

Fresh 24-item/42-rule audit, five actual searches, all four compiled binder deletions/value-sensitivity certificates, semiring assessment and public literature pass. Independently elaborated immutable type/value, kernel definitional equality and both rfl comparisons protect the exact definition; actual built axioms are standard only. [Dedicated audit](cleanup/Theta-lem6M.md).
Final Theta SHA256 `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`. Module and complete unfiltered LSP:0 errors/17 warnings;
accepted real prefix profile:37.516 ms. Frozen full build5.980s then
separate LeanEval3.018s both exit0; all17project/pin/source hashes stable.
No new production helper; the previously added helper remains separately audited. After successful publication:Theta21/35,overall202/264,9/14files.
Next:original 22, public definition lem6Φ. Actual whole-Theta profiling and final file phases remain outstanding.

Original21 validated source/audit checkpoint: [c366f7c](https://github.com/SmwYin/Roth/commit/c366f7c61ac742abde10c91713b73dc5c7b7243b).
The following central-log metadata commit changes no Lean source; both commits publish
together before original22 edits. Counts remain 202/264, Theta 21/35, 9/14 files.


## Theta original22 checkpoint — lem6Φ

Normalized three ordinary lambda arrows to ↦ in the one-line Φ definition. Its complete original telescope, mathematical value, public API, paper documentation and all callers remain unchanged; no helper introduced.

Fresh 24-item/42-rule audit, five actual searches, all six effective binder probes, literature/inversion and measured tables pass. Independently elaborated immutable RSet/indexSet/Θ/Φ definitions, exact telescope metadata, type/value definitional equality and kernel rfl checks pass against the rebuilt actual constant; actual axioms remain standard only. [Dedicated audit](cleanup/Theta-lem6Phi.md).
Final Theta SHA256 `ad8d2553390a9af55ecec731f216e8bab23702ec79229af1331cfe87e6f1079f`. Module and complete unfiltered LSP:0 errors/17 warnings;
accepted real prefix profile:19.752 ms. Frozen full build65.683s then
separate LeanEval26.314s both exit0; all17project/pin/source hashes stable.
No new production helper; the prior helper remains separately audited. After successful publication:Theta22/35,overall203/264,9/14files.
Next:original 23, one_le_lem6M. Actual whole-Theta profiling and final file phases remain outstanding.

Original22 validated source/audit checkpoint: [30814e0](https://github.com/SmwYin/Roth/commit/30814e00237eb0802eac8ffa96b7a69bde92b9e9).
The following central-log metadata commit changes no Lean source; both commits publish
together before original23 edits. Counts remain 203/264, Theta 22/35, 9/14 files.


## Theta original23 checkpoint — one_le_lem6M

Shortened the M lower-bound proof from eight to six body lines, replacing linarith with ordered-add nonnegativity and direct existing product/power lemmas. All public arguments, conclusion, name, documentation and callers remain unchanged.

Dedicated 24-item/42-rule audit, five actual searches, all five effective binder probes with independent counterexamples, literature/inversion and measured tables pass. Immutable independent original nonself proof, exact complete original type AST/binder metadata and actual built standard-axiom checks pass. [Dedicated audit](cleanup/Theta-one_le_lem6M.md).
Final Theta SHA256 `5c4aa2d1347aba94a182fdbe58a06e78f19ada9568e8f0b33876469ce8781cea`. Module and complete unfiltered LSP:0 errors/17 warnings;
accepted real prefix profile:131.343 (conservative including tiny lazy definition-equation tasks <133; baseline 284.544, conservatively <286) ms. Frozen full build73.770s then
separate LeanEval26.327s both exit0; all17project/pin/source hashes stable.
No new production helper; the prior helper remains separately audited. After successful publication:Theta23/35,overall204/264,9/14files.
Next:original 24, floor_sq_div_two_le_sum. Actual whole-Theta profiling and final file phases remain outstanding.

Original23 validated source/audit checkpoint: [e5f28a0](https://github.com/SmwYin/Roth/commit/e5f28a07323b41272721234fd3770b728d658c13).
The following central-log metadata commit changes no Lean source; both commits publish
together before original24 edits. Counts remain 204/264, Theta 23/35, 9/14 files.


## Theta original24 checkpoint — floor_sq_div_two_le_sum

Shortened the floor-sum proof from eleven to six body lines using the directly cast Gauss sum identity and the floor bound. Removed the local floor name and nested cast-equality boilerplate; the exact public real-number statement, documentation and sole caller remain unchanged.

Dedicated 24-item/42-rule audit, five actual searches, both effective binder probes, a certified negative-input counterexample, literature/inversion and measured tables pass. The compiled ordered-floor-field candidate was assessed and not recommended for public API churn. Immutable independent original nonself proof, complete original type recovery and actual built standard axioms pass. [Dedicated audit](cleanup/Theta-floor_sq_div_two_le_sum.md).
Final Theta SHA256 `3522af0920e133d0f34f3da6c162e288d3987a0fb948ded6d3a89ef87ee1d62f`. Module and complete unfiltered LSP:0 errors/17 warnings;
accepted real prefix profile:414.955 (baseline 503.277) ms. Frozen full build83.621s then
separate LeanEval29.992s both exit0; all17project/pin/source hashes stable.
No new production helper; the prior helper remains separately audited. After successful publication:Theta24/35,overall205/264,9/14files.
Next:original 25, sq_div_three_lt_floor_sq_div_two. Actual whole-Theta profiling and final file phases remain outstanding.

Original24 validated source/audit checkpoint: [4ee4acc](https://github.com/SmwYin/Roth/commit/4ee4acc839e971d63927958b802372d811f183c6).
The following central-log metadata commit changes no Lean source; both commits publish
together before original25 edits. Counts remain 205/264, Theta 24/35, 9/14 files.


## Theta original25 checkpoint — sq_div_three_lt_floor_sq_div_two

Reduced the floor-square comparison from five proof lines to one nlinarith application using the direct natural-floor upper bound. The exact original real-number API, strict threshold 10, docstring and sole caller remain unchanged.

Dedicated 24-item/42-rule audit, five actual searches, both effective binder probes, compiled weaker thresholds/generic field candidates and certified counterexamples, literature/inversion and measured tables pass. Broader variants were assessed and not recommended for public API churn. Independent immutable original nonself proof, exact full telescope metadata/conclusion recovery and actual built standard axioms pass. [Dedicated audit](cleanup/Theta-sq_div_three_lt_floor_sq_div_two.md).
Final Theta SHA256 `c24f9782e08680eaaebf16b134c8b86cbe13e05c9778d1606119f28f392cc7b9`. Module and complete unfiltered LSP:0 errors/17 warnings;
accepted real prefix profile:349.782 (baseline 376.779, corrected disjoint kernel/linter accounting) ms. Frozen full build89.100s then
separate LeanEval28.568s both exit0; all17project/pin/source hashes stable.
No new production helper; the prior helper remains separately audited. After successful publication:Theta25/35,overall206/264,9/14files.
Next:original 26, min_le_sum_max. Actual whole-Theta profiling and final file phases remain outstanding.

Original25 validated source/audit checkpoint: [7342f45](https://github.com/SmwYin/Roth/commit/7342f4587c85a1c05e3b953b232782ffa704289e).
The following central-log metadata commit changes no Lean source; both commits publish
together before original26 edits. Counts remain 206/264, Theta 25/35, 9/14 files.


## Theta original26 checkpoint — min_le_sum_max

Strengthened the positive-part arithmetic-sum bound by removing both public positivity/size hypotheses hrp and hθ; its exact real/natural domains and conclusion remain. Public proof46→7lines. The sole index_le_lem6 caller receives named θ/rp arguments and retains its entire original contract, including hq and DecidableEq.

Fresh original audit plus three separate fresh helper audits complete: all24/42/5-search, effective-binder compiled probes, literature/inversion and measured tables. Independently replayed immutable original min and ENTIRE index_le_lem6 proofs; exact old telescopes/adapters, BinderInfo/value and actual built standard axioms pass. Private linear hr removal, quadratic hr removal/weak cutoff and separate positive-core proof are independently verified. [Dedicated audit](cleanup/Theta-min_le_sum_max.md).
Final Theta SHA256 `e6360c9acdc9d7be22356ba3a26006e24cc1b0b667b5992395759228e1087530`. Module and complete unfiltered LSP:0 errors/17 warnings;
accepted real prefix profile:public165.806; linear460.921, positivecore543.552, quadraticwrapper304.757 (all four <750) ms. Frozen full build92.510s then
separate LeanEval33.553s both exit0; all17project/pin/source hashes stable.
Three new private helpers each received separate fresh dedicated audits; final bodies linear15, positivecore22, quadraticwrapper7. Helpers add0 original declarations. After successful publication:Theta26/35,overall207/264,9/14files.
Next:original27, sum_max_sub_le_index_det (approved DecidableEqτ and hR removal). Actual whole-Theta profiling and final file phases remain outstanding.

Original26 validated source/audit checkpoint: [9bf5ca8](https://github.com/SmwYin/Roth/commit/9bf5ca8bec00e85c3800de82627eeedae2facad8).
The following central-log metadata commit changes no Lean source; both commits publish
together before original27 edits. Counts remain 207/264, Theta 26/35, 9/14 files.


## Theta original27 checkpoint — sum_max_sub_le_index_det

Applied exactly the approved DecidableEqτ and hR removals from the determinant-index lower bound, retaining the degree/weight interface and all other original arguments. Proof25→24lines with explicit nonnegativity and restricted linear arithmetic. The sole index_le_lem6 caller drops the obsolete argument/local proof and retains its entire original public contract.

Fresh24-item/42-rule audit, five actual searches, every effective binder compiled probe, literature/inversion and measured tables complete. Broader finite-family/strict-degree and generic determinant alternatives compiled but are not recommended for API churn. Independent immutable complete original target AND entire index_le_lem6 proof/type replay, exact old adapters/names/BinderInfo/value/universes/conclusions and actual standard axiom sets pass. [Dedicated audit](cleanup/Theta-sum_max_sub_le_index_det.md).
Final Theta SHA256 `ac43e6d19ce869213d3d0f6a260ffc92ab8f419d9b2be320483539746e5434a9`. Module and complete unfiltered LSP:0 errors/14 warnings;
accepted real prefix profile:746.452 (clean baseline779.542, required clean repeat831.962; discarded closing-scope-error run excluded) ms. Frozen full build110.300s then
separate LeanEval32.749s both exit0; all17project/pin/source hashes stable.
No new production helper; all prior helpers remain separately audited. After successful publication:Theta27/35,overall208/264,9/14files.
Next:original28, index_det_le (approved DecidableEqτ, hl′, hδ and unused implicitδ removal; proof/performance cleanup). Actual whole-Theta profiling and final file phases remain outstanding.

Original27 validated source/audit checkpoint: [8768665](https://github.com/SmwYin/Roth/commit/87686659b0839593a4a2070b06ce02cf5492b2f5).
The following central-log metadata commit changes no Lean source; both commits publish
together before original28 edits. Counts remain 208/264, Theta 27/35, 9/14 files.


## Theta original28 checkpoint — index_det_le

Applied approved DecidableEqτ/δ/hl′/hδ removals and the supported redundant hB removal under standing authorization. Uniform coefficient bounds imply the needed nonnegativity. Public proof94→24 physical lines including all3 Step comments; sole caller drops only obsolete application arguments and retains its entire original public contract.

Fresh24-item/42-rule/five-actual-search/every-effective-binder/literature/inversion/packing/inequality/11-step audits complete. Independent immutable complete original target AND entire index_le_lem6 proof/value/type replay, exact old adapters/names/BinderInfo/universes/conclusions and actual standard axiom sets pass. Both initially extracted private helpers received separate fresh audits; the coefficient helper was deleted using the existing constant-degree bound specialization, with actual built and trace absence checked. [Dedicated audit](cleanup/Theta-index_det_le.md).
Final Theta SHA256 `c6e59b0ff252c0cdfc0e00070bb7c0c5bea3a53e0786889767f4b1594f5e6ee3`. Module and complete unfiltered LSP:0 errors/11 warnings;
accepted real prefix profile:public742.222; retained helper655.221 (original public baseline2083.744; both final<750) ms. Frozen full build91.138s then
separate LeanEval30.612s both exit0; all17project/pin/source hashes stable.
One retained private separated-product helper26lines, separately freshly audited; the initially added coefficient helper was separately freshly audited and deleted. New helpers and revisits add no original count. After successful publication:Theta28/35,overall209/264,9/14files.
Next:original29, index_le_lem6 (approved DecidableEqτ removal, explicit hq retention, ordinary≤30 structuring and actual instrumented performance repair). Actual whole-Theta profiling and final file phases remain outstanding.

Original28 validated source/audit checkpoint: [6a1e668](https://github.com/SmwYin/Roth/commit/6a1e668bd056b14c513e6e994192c327fd169348).
The following central-log metadata commit changes no Lean source; both commits publish
together before original29 edits. Counts remain 209/264, Theta 28/35, 9/14 files.


## Theta original29 checkpoint — index_le_lem6

Removed approved DecidableEqτ and extended the coordinate ratio from strict to nonstrict after concrete old-contract/caller verification. Replaced the default-heartbeat-failing broad arithmetic with a 22-line public assembly and separately audited weight, mapped-determinant and numeric arguments. Explicit hq remains; the entire original strict Θ_option_le caller contract is preserved.

Fresh full24/42/five-actual-search/every-binder/literature/inversion/packing/inequality/11-step audits complete. Immutable independent entire original29 and original30 proofs, exact original adapter, retained names/types/BinderInfo/universes/conclusions, actual opaque proof values and standard axiom sets pass. Each of the three new private helpers received its own separate fresh audit, including exact first-proof recovery and generalized private-contract adapters; no original count inflation. [Dedicated audit](cleanup/Theta-index_le_lem6.md).
Final Theta SHA256 `47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`. Module and complete unfiltered LSP:0 errors/10 warnings;
accepted real prefix profile:public895.050/854.163; weight408.013/361.605; mapped707.126/651.477; numeric939.576/873.525 (first/required-repeat; all<1000) ms. Frozen full build92.063s then
separate LeanEval29.415s both exit0; all17project/pin/source hashes stable.
Three substantive retained private helpers separately freshly audited: numeric16lines (δ≤1,rp≥3, noδ positivity premise), weight12lines (no weight-positivity premise), mapped determinant14lines (same signature). No new public domain or conclusion change. After successful publication:Theta29/35,overall210/264,9/14files.
Next:fresh dedicated supported original29 arithmetic-boundary revisit K (counts unchanged), then original30 Θ_option_le. Actual whole-Theta profiling and final file phases remain outstanding.

Original29 validated source/audit checkpoint: [6ac4373](https://github.com/SmwYin/Roth/commit/6ac4373f79e3d1fab6350f6f4bb4dae1ef8041ca).
The following central-log metadata commit changes no Lean source; both commits publish
together before original30 edits. Counts remain 210/264, Theta 29/35, 9/14 files.


## Theta supported original29 boundary revisit — K

Applied the supported weakδ/rp3 boundary and derived-away index_le_lem6.hr0/hB under the
standing instruction to implement recommended changes. Explicit hq and protected globalΘ
hB/hr preferences remain. Entire original29+original30 independent proofs/oldadapters,
actual metadata/opaquevalues/standardaxioms and the entire new caller proof's dependency pass.
All three private helpers and outside-scope source are unchanged; no new helper/original.
[Dedicated audit](cleanup/Theta-index_le_lem6-boundary-revisit.md).
Final source SHA256 `59fc1479999b47953aff7aee6bf8be17a325e9523ca94375d8b48b273618e427`.
Module34.272s/actual50.088s/complete unfiltered nativeLSP0errors11warnings pass. Both real
exact-prefix sweeps pass: public996.125/936.382,numeric918.885/829.176,weight455.974/355.065,
mapped722.709/634.434ms. No whole-module performance claim. Frozen full build92.105s THEN
separateLeanEval29.557s both exit0 with all17 source/pin hashes stable.
Counts unchanged210/264,Theta29/35,9/14files; validated revisits9 (eight prior approved scope,
this one under standing recommendation authority). Next original30 Θ_option_le; reserved new
caller hr0 warning and selected DecidableEq removal receive its own fresh audit.

Supported K29 validated source/audit checkpoint: [e0784cf](https://github.com/SmwYin/Roth/commit/e0784cf931052862a49e9d618c3408a95438616e).
The following central-log metadata commit changes no Lean source; both publish together
before original30 edits. Counts remain210/264,Theta29/35,9/14files; validated revisits9.


## Theta original30 checkpoint — Θ_option_le

Removed approved `[DecidableEq τ]` and the derived `hr0` premise from `Θ_option_le`, extending its unchanged conclusion to closed δ bounds, `3 ≤ r none` and weak coordinate ratios. Retained `hq` and `hB`. The headline proof is five lines; the entire `Θ_lt` caller contract is preserved with minimal forwarding.

Fresh 24-item audit, 42 golf rules, five actual searches, every-binder probes, literature/inversion, packing, inequality and 11-step checks pass. Independent entire original30 and original Θ_lt proofs/adapters, actual new caller dependency, retained metadata and standard axioms pass. Owner cumulative recovery of all29 public contracts and all five definition values passes, including29 explicit old adapters,87 opaque body-type checks and87 actual standard axiom checks; both immutable original proof blocks are byte-identical. [Dedicated audit](cleanup/Theta-Theta_option_le.md).
Final Theta SHA256 `c488d3189154ae0da29fd6d798c3b1d016e44fa588ab4ab32a5ea7c93c3837fd`. Module and complete unfiltered LSP:0 errors/8 warnings;
accepted real prefix profile:Θ_option158.615/144.368; public29 901.577/925.763; weight401.279/399.404; mapped693.423/723.578; numeric903.545/922.672 (first/required repeat; all<1000) ms. Frozen full build113.288s then
separate LeanEval37.676s both exit0; all17project/pin/source hashes stable.
No new private helper; all three previously audited helpers unchanged. Original counts exclude revisits and helper audits. After successful publication:Theta30/35,overall211/264,9/14files.
Next:original31 private one_lt_of_log_pos (assess direct existing Real.log_pos_iff replacement and actual deleted-wrapper absence/caller proofs). Actual whole-Theta profiling and final file phases remain outstanding.

Original30 validated source/audit checkpoint: [b2e29b5](https://github.com/SmwYin/Roth/commit/b2e29b589e54b42db53803b718a9c4b71249bb9a).
The following central-log metadata commit changes no Lean source; both commits publish
together before original31 edits. Counts remain 211/264, Theta 30/35, 9/14 files.


## Theta original31 checkpoint — one_lt_of_log_pos

Deleted the five-line private `one_lt_of_log_pos` wrapper and used `Real.log_pos_iff` with the direct cast at its three `Θ_lt` call sites. All public contracts and every other helper remain unchanged.

Fresh private24/42/five actual searches/every-binder/counterexample/inversion/packing/inequality/11-step checks and exact independent FIRST/replacement/value/standard-axiom gates pass. The built wrapper is absent; the entire original Θ_lt type/value/standard axioms and exactly three direct log_pos_iff proof uses are checked. The bounded final actual-caller attempt stalled and was interrupted130 after four identical-output checks; no explicit Lean error or finite caller timing was observed. [Dedicated audit](cleanup/Theta-one_lt_of_log_pos.md).
Final Theta SHA256 `30a8d16687baacb2c21383934dcbb22cb0e8458da0392504d81acf9eadf6b0d7`. Module and complete unfiltered LSP:0 errors/8 warnings;
Scoped direct-replacement certificate:86.921 (real exact old-contract certificate; the deleted production declaration has no timing) ms. Frozen full build103.738s then
separate LeanEval34.051s both exit0; all17project/pin/source hashes stable.
Deleted one original private wrapper; no new helper. This still reviews one original declaration and adds no count from helpers/revisits. After successful publication:Theta31/35,overall212/264,9/14files.
Next:original32 lem6M_lt (ordinary proof≤30; every new helper requires a separate fresh audit). Actual whole-Theta profiling and final file phases remain outstanding.

Original31 validated source/audit checkpoint: [b654ab8](https://github.com/SmwYin/Roth/commit/b654ab84fc3f86231421a033a62cdc774bb26adb).
The following central-log metadata commit changes no Lean source; both commits publish
together before original32 edits. Counts remain 212/264, Theta 31/35, 9/14 files.


## Theta original32 checkpoint — lem6M_lt

Simplified lem6M_lt from53 to21 proof lines using two substantive independently audited private estimates. Weakened p≥2 to p>0 and the logarithmic bound to≤, removed the derived positive-r₁ argument, and preserved the strict conclusion and entire Θ_lt caller contract.

Original32 and BOTH new helpers completed separate fresh24/42/five-search/every-binder/inversion/packing/inequality/11-step audits. Exact immutable old32 adapter, ENTIRE original/current Θ_lt independent proof/type/value/standard axioms, both INITIAL helper contracts and actual built opaque values/standard axioms pass. Current private bounds accept l≤2^r₁ and q≥0 while public32 retains its documented assumptions. Owner final-state cumulative verification passed47.118s: all29 exact original-public adapters,87 opaque body-type checks and87 actual standard-axiom sets; both full immutable proof blocks byte-identical. [Dedicated audit](cleanup/Theta-lem6M_lt.md).
Final Theta SHA256 `edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`. Module and complete unfiltered LSP:0 errors/8 warnings;
Accepted real prefix profile:lem6M_lt675.914, factorial_coefficient_le_two_pow_aux290.063, two_pow_lt_rpow_aux597.526 (all below750; no threshold repeat required) ms. Frozen full build91.810s then
separate LeanEval31.678s both exit0; all17project/pin/source hashes stable.
Two substantive private estimates have separate fresh completed audits: coefficient proof9lines with l≤2^r₁, exponential proof21lines with q≥0. Helper audits and supported revisits do not inflate original counts. After successful publication:Theta32/35,overall213/264,9/14files.
Next:original33 lem7_Φ_bound, then34/35 and every final file phase. Actual whole-Theta profiling and final file phases remain outstanding.

Original32 validated source/audit checkpoint: [ceaef4d](https://github.com/SmwYin/Roth/commit/ceaef4d11cd4ab4d007e48c865ca1d0a40bc0d2e).
The following central-log metadata commit changes no Lean source; both commits publish
together before original33 edits. Counts remain 213/264, Theta 32/35, 9/14 files.


## Theta original33 checkpoint — lem7_Φ_bound

Extended lem7_Φ_bound to the closed upper boundary δ≤1 while preserving its strict conclusion. Replaced broad nonlinear arithmetic with direct scaled bounds and restricted arithmetic, removed dead locals and one-use bounds, and forwarded the Θ_lt caller by.le. Proof22→20lines; no new helper.

Fresh24/42/five actual searches/every-binder/certified-counterexample/public-literature/inversion/packing/inequality/11-step gates pass. Exact immutable independent old33 proof, actual ROOT old-contract adapter and ENTIRE original/current Θ_lt independent proof/type/value/standard axioms pass. Final real target first/repeat876.021/757.251ms pass versus baseline1489.059ms. Owner final-state cumulative verification passed51.807s: all29 original-public adapters, all5 definition values,87 opaque body-type checks and87 actual standard-axiom sets, with both complete original proof blocks byte-identical. [Dedicated audit](cleanup/Theta-lem7_Phi_bound.md).
Final Theta SHA256 `fc354913a6695d434020810dd37299614daa2bd7ca345b0e8bac489492679337`. Module and complete unfiltered LSP:0 errors/8 warnings;
Accepted real prefix profile:876.021 / 757.251 (required same-source repeat passed; baseline1489.059) ms. Frozen full build105.519s then
separate LeanEval38.323s both exit0; all17project/pin/source hashes stable.
No new helper; existing separately audited private helpers are unchanged. After successful publication:Theta33/35,overall214/264,9/14files.
Next:original34 lem7_numeric, then35 Θ_lt and all final file phases. Actual whole-Theta profiling and final file phases remain outstanding.

Original33 validated source/audit checkpoint: [b80bf83](https://github.com/SmwYin/Roth/commit/b80bf8386bb88f518b743aa2b30f27813314ed62).
The following central-log metadata commit changes no Lean source; both commits publish
together before original34 edits. Counts remain 214/264, Theta 33/35, 9/14 files.


## Theta original34 checkpoint — lem7_numeric

Extended lem7_numeric to δ≤1 and the closed Φ upper bound, removed the unnecessary Φ≥0 premise, and preserved its strict conclusion. Explicit scaled-square comparisons replace broad nonlinear search; proof25→29lines with no helper. The Θ_lt call is minimally adapted and its full public contract preserved.

Fresh24/42/five actual searches/every-binder/public-literature/inversion/packing/inequality/11-step gates pass. Exact immutable old34 adapter, ENTIRE old/current/independent Θ_lt effective type, opaque proof value, standard axioms and actual dependency pass. Owner cumulative d34-values passed29 original-public adapters/all5 definition values/87 opaque body types/87 actual standard-axiom sets, with both complete immutable original proof blocks unchanged. [Dedicated audit](cleanup/Theta-lem7_numeric.md).
Final Theta SHA256 `a98740b5b006547f5deafca6cbb12c6b4972dbfc130eae64645e67bdd9b8d800`. Module and complete unfiltered LSP:0 errors/8 warnings;
Accepted real prefix profile:757.682 and required same-source repeat865.831 (baseline1429.265) ms. Frozen full build108.121s then
separate LeanEval33.707s both exit0; all17project/pin/source hashes stable.
No new helper; existing separately audited helpers unchanged. No original-count inflation from helper/revisit audits. After successful publication:Theta34/35,overall215/264,9/14files.
Next:original35 headline Θ_lt, every newhelper separate fresh audit, then mandatory performance repairs and all final file phases. Actual whole-Theta profiling and final file phases remain outstanding.

Original34 validated source/audit checkpoint: [61b5c67](https://github.com/SmwYin/Roth/commit/61b5c67554a444fe1926d76883316cb41798c7f3).
The following central-log metadata commit changes no Lean source; both commits publish
together before original35 edits. Counts remain 215/264, Theta 34/35, 9/14 files.


## Theta original35 checkpoint — Θ_lt

Factored Θ_lt into substantive numerical, transport, base and successor stages. Removed its δ upper bound and derived positive-weight/denominator premises, weakened the last weight to3≤rLast, closed adjacent product and log bounds, and preserved the strict conclusion. Headline stays within15lines (currently15 after base-helper contract cleanup); MainLemma receives only the necessary proof-call adaptation and keeps its entire public contract.

All ELEVEN introduced helper obligations freshly and separately audited (eight retained, three introduced/deleted), followed by the additional measured prefix performance repair. Frozen current-source359 checks preserve the entire original Index/Theta, original2b MainLemma and independent current MainLemma proof blocks, publicTheta9/Main26 contracts, exact original helper adapters/deletion AST checks and actual standard axioms. Owner cumulative29 probe passes29 full old-public adapters,87 opaque value/type checks,87 actual standard-axiom sets and all five definition equality recoveries; independent all50 actual retained declaration values/types/axioms also pass. [Dedicated audit](cleanup/Theta-Theta_lt.md).
Final Theta SHA256 `cfa05489380deeae6eb1bc63202249c3754b791357912aabff24e29e1cae4788`. Module and complete unfiltered LSP:0 errors/8 warnings;
Accepted actual whole-source scoped final pair:public Θ_lt413.535/330.244; prefix757.698/767.127; phi887.425/641.027; successor852.192/728.387; all eight retained35 helpers below1000 in both captures ms. Frozen full build61.547s then
separate LeanEval31.863s both exit0; all17project/pin/source hashes stable.
All11 introduced obligations complete: retained scaled_unique,delta_succ,prefix_lt,base,denominators,phi,successor,large_delta; introduced/deleted fin_option,prefix_log,last_lt_first each have their own fresh generic original-contract/deletion-replacement audit. No helper or revisit count inflation. After successful publication:Theta35/35,overall216/264,9/14files.
Next:dedicated sequential numeric/index29 performance repairs, fresh independent filewide simplify review, all cumulative semantic/native/import/actual whole-file profile/full+separateLeanEval gates before Theta file-final publication. Actual whole-Theta profiling and final file phases remain outstanding.

Original35 validated source/audit checkpoint: [6bf343c](https://github.com/SmwYin/Roth/commit/6bf343c4b91f530522cc2dbb19ad472cdd548ac4).
The following central-log metadata commit changes no Lean source; both commits publish
together before subsequent performance revisit edits. Counts remain 216/264, Theta 35/35, 9/14 files.


## Validated Theta revisit — mul_sq_div_three_le_sum_max_of_pos_aux

Replaced arithmetic search with an explicit nonnegative polynomial certificate and broad field_simp with eq_div_iff plus ring. The exact six-binder private contract, callers and22-line proof length remain unchanged; no new helper. Deterministic heartbeats2624→2111. [Dedicated audit](cleanup/Theta-mul_sq_div_three_le_sum_max_of_pos_aux-performance.md).
Revisit source/audit commit `b9af0098b1241483aa01a4ea56c61368c4da0549`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/b9af0098b1241483aa01a4ea56c61368c4da0549).
Frozen Theta SHA256 `e94ada9acfbd31f74bf65a04ea750e022c117d5e8d6e0ffb32ff6a8e56fb2ad5`. All owner gates passed as recorded in the audit.
This belongs to original26 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated sum_max_sub_le_index_det performance revisit, then remaining six older repairs and independent filewide review/final gates. Seven older performance failures remain queued; no whole-file performance pass. MainLemma actual finite caller timing remains unmeasured before main_lemma.


## Validated Theta revisit — index_le_lem6

Replaced weight-cutoff arithmetic search with an exact Nat subtraction certificate, shared positive initial degree, and restricted terminal mul_add simplification. Exact public statement, explicit hq, shared existential witness and surrounding source remain unchanged; no new helper. Heartbeats4825→1946; proof27→26 noncomment lines. [Dedicated audit](cleanup/Theta-index_le_lem6-performance.md).
Revisit source/audit commit `45d50ba0a5355cb403701aae5c8b1b299ff8eb87`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/45d50ba0a5355cb403701aae5c8b1b299ff8eb87).
Frozen Theta SHA256 `5458997a96e7dfd6c5a86d35e210f86c533b3c4b62a5e532a163b5c80c34fe1a`. All owner gates passed as recorded in the audit.
This belongs to original29 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated index_det_le performance revisit, then index_separated, index_numeric, sum_max, lem7_Φ_bound and lem7_numeric repairs, followed by independent filewide review/final gates. Six older performance failures remain queued; no whole-file performance pass. MainLemma finite actual caller timing remains unmeasured before main_lemma.


## Validated Theta revisit — index_det_le

Replaced broad determinant coefficient-bound normalization with pinned finite-product, sum, cardinality, cast and power rewrites. Exact public contract, caller, surrounding source and all three Step comments remain unchanged; no new helper or import. Heartbeats4996→3357. [Dedicated audit](cleanup/Theta-index_det_le-performance.md).
Revisit source/audit commit `51dc3bbfc5957ba6223f02ab148ccb6877bf49ab`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/51dc3bbfc5957ba6223f02ab148ccb6877bf49ab).
Frozen Theta SHA256 `2760ef227eb2d729381057ad02c2a0ac54c3fdc49e99a3a5a22c025b3fb6c145`. All owner gates passed as recorded in the audit.
This belongs to original28 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated index_separated_mul_le_aux performance revisit, then index_numeric, sum_max, lem7_Φ_bound and lem7_numeric plus newly required second theta_prefix_lt_aux repair, followed by independent filewide review/final gates. Five older performance failures remain queued. New theta_prefix_lt_aux1047.277ms failure is preserved and requires a separate fresh repair even though its repeat is lower; no whole-file performance pass. MainLemma finite actual caller timing remains unmeasured before main_lemma.


## Validated Theta revisit — index_separated_mul_le_aux

Pinned the real coefficient and rename homomorphisms, retained two typed nonzero certificates, and replaced terminal simplification with direct rewrite/division bounds. Exact private FIRST contract and entire public caller remain unchanged; no new helper or import. Heartbeats6894→2410; proof26→30 lines. [Dedicated audit](cleanup/Theta-index_separated_mul_le_aux-performance.md).
Revisit source/audit commit `ebb1021e9d72fc5aade7a9657a4a4b3e27c63616`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/ebb1021e9d72fc5aade7a9657a4a4b3e27c63616).
Frozen Theta SHA256 `3631ff20d25efdec5d9a846640a8c5a4f5efcac876a37dfee83e39c638fcfcde`. All owner gates passed as recorded in the audit.
This belongs to original28 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated index_numeric_bound_aux performance revisit, then sum_max, lem7_Φ_bound and lem7_numeric plus the mandatory second theta_prefix_lt_aux repair, followed by independent filewide review/final gates. Four older performance repairs and the historical prefix1047.277ms failure remain mandatory. The rejected intermediate1001.920ms sample is preserved with its own source, and a substantive second repair passed on a new source; no third unchanged-source sample. No whole-file performance pass. MainLemma finite actual caller timing remains unmeasured before main_lemma.


## Validated Theta revisit — index_numeric_bound_aux

Replaced three nonlinear arithmetic searches with explicit coefficient, multiplication and square certificates. The exact private contract still permits negative δ; the entire public index29 caller and all surrounding source stay byte-identical. No new helper/API/import. Heartbeats4206→1954; proof remains16 lines. [Dedicated audit](cleanup/Theta-index_numeric_bound_aux-performance.md).
Revisit source/audit commit `305442a9a0daef17dcfc800333a63a669ad5cc21`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/305442a9a0daef17dcfc800333a63a669ad5cc21).
Frozen Theta SHA256 `f458cf85b2746b8d155074c3aaaccd8e8c0708bd2d7fa78787184d76ae008875`. All owner gates passed as recorded in the audit.
This belongs to original29 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated sum_max_sub_le_index_det performance revisit, then lem7_Φ_bound and lem7_numeric plus the mandatory second theta_prefix_lt_aux repair, followed by independent filewide review/final gates. Three older repairs and the historical prefix1047.277ms failure remain mandatory; no whole-file performance pass. MainLemma finite actual caller timing remains unmeasured before main_lemma.


## Validated Theta revisit — sum_max_sub_le_index_det

Replaced duplicated sign-case simplification with existing nonzero-scalar index invariance and local arithmetic search with direct subtraction order transport. Exact public contract, complete index29 caller and all surrounding source remain unchanged; no new helper/API/import. Heartbeats4759→3263; ordinary proof27 lines. [Dedicated audit](cleanup/Theta-sum_max_sub_le_index_det-performance.md).
Revisit source/audit commit `25fd68dadaaaf1d803c1e9787bf5d73d282ae760`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/25fd68dadaaaf1d803c1e9787bf5d73d282ae760).
Frozen Theta SHA256 `c0e8edc37192227f56814c674480b56143e2923e588a750dca5d7f3ecf03c2a8`. All owner gates passed as recorded in the audit.
This belongs to original27 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated lem7_Φ_bound performance revisit, then lem7_numeric and the mandatory second theta_prefix_lt_aux repair, followed by independent filewide review/final gates. Two older Lemma7 repairs and historical prefix1047.277ms failure remain mandatory; no whole-file performance pass. MainLemma finite actual caller timing remains unmeasured before main_lemma.


## Validated Theta revisit — lem7_Φ_bound

Replaced nonlinear closure with the explicit weighted scalar certificate and direct reciprocal order transport. Full public contract/docstring and entire private phi caller unchanged; no helper or API change. Ordinary proof22 lines. [Dedicated audit](cleanup/Theta-lem7_Phi_bound-performance.md).
Revisit source/audit commit `a51d377bbeaa9cf4c11eef90b414a01777f5e2a1`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/a51d377bbeaa9cf4c11eef90b414a01777f5e2a1).
Frozen Theta SHA256 `ff96424900db697abbba3c3a4b6fe6356abf774b55c08d2b582dc31a21b1e629`. All owner gates passed as recorded in the audit.
This belongs to original33 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh dedicated lem7_numeric repair, then mandatory second prefix and second summax repairs, independent filewide review and final gates. Numeric1254.575/1129.895 remains; historical prefix1047.277 and fresh summax1004.335/809.108 require separate repairs. No whole-file pass; MainLemma finite actual timing remains unmeasured before main_lemma.


## Validated Theta revisit — lem7_numeric

Replaced general arithmetic solvers with exact product/order terms and a fixed2+2+2 weighted certificate, and narrowed the measured terminal power simplification. Public contract/docstring and entire private phi caller unchanged; proof29 lines, no helper/API change. [Dedicated audit](cleanup/Theta-lem7_numeric-performance.md).
Revisit source/audit commit `8bc2fd91e011f8fe9de5b7379ecde58bbc85306c`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/8bc2fd91e011f8fe9de5b7379ecde58bbc85306c).
Frozen Theta SHA256 `70465cb863f51a834bd0bf203bc14776e7492270ad4c345536d8fa8a06cc7b25`. All owner gates passed as recorded in the audit.
This belongs to original34 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:mandatory second theta_prefix_lt_aux performance repair, then mandatory second sum_max_sub_le_index_det repair, independent filewide review and final gates. All eight original older performance repairs have checkpoints, but second prefix historical1047.277 and second summax1004.335 plus1131.027/1065.136 failures remain mandatory. No whole-file pass; MainLemma finite actual timing remains unmeasured before main_lemma.


## Validated Theta revisit — theta_prefix_lt_aux (second performance repair)

Replaced two measured nonnegativity searches with direct certificates and a multiplication ring search with mul_left_comm. Exact private contract and entire phi caller unchanged; proof30 lines/branch8, no helper. Heartbeats2886→2463. [Dedicated audit](cleanup/Theta-theta_prefix_lt_aux-performance-second.md).
Revisit source/audit commit `3f4ab498398f79e9bad037de6df98b0ee5abfa2d`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/3f4ab498398f79e9bad037de6df98b0ee5abfa2d).
Frozen Theta SHA256 `3f9c23b83cd5bb8eaf9deb2b6d8c9182d0309464c5c76a3568c30eb1f86100ce`. All owner gates passed as recorded in the audit.
This belongs to original35 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:mandatory second sum_max_sub_le_index_det performance repair, then fresh independent filewide review and final gates. Second summax remains mandatory from1004.335/809.108 and1131.027/1065.136 failure pairs, despite incidental passing rows in this scope. No whole-file performance pass; MainLemma finite actual timing remains unmeasured before main_lemma.


## Validated Theta revisit — sum_max_sub_le_index_det (second performance repair)

Replaced broad constant-sum simp with Fin.sum_const/nsmul_eq_mul and shared a typed Matrix.of entry nonzero certificate. Exact public contract and entire direct index29 caller remain unchanged; proof28 lines/subproof9, no helper. Heartbeats3263→2581 (20.90% reduction). [Dedicated audit](cleanup/Theta-sum_max_sub_le_index_det-performance-second.md).
Revisit source/audit commit `360815c908b578504b2724ed78a7ea2c01a66150`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/360815c908b578504b2724ed78a7ea2c01a66150).
Frozen Theta SHA256 `2a41e042e8a363fd01a5038dadd04e3ddbd5d6e9ff57d788aa418e389ff7cd52`. All owner gates passed as recorded in the audit.
This belongs to original27 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:mandatory mapped_det_ne_zero_aux performance repair, then fresh independent filewide review and final gates. New mapped_det_ne_zero_aux failure1049.976ms remains mandatory despite829.583ms repeat. MainLemma finite actual timing remains unmeasured before main_lemma; no whole-file/project performance pass.


## Validated Theta revisit — mapped_det_ne_zero_aux performance repair

Replaced three placeholder-heavy nonzero-map refinements with goal-directed map_eq_zero_iff rewrites and merged consecutive rewrites. Original determinant rw/congr/ext certificate retained; exact private contract unchanged, proof14→12, no helper or caller edits. Heartbeats3266→3283; actual timing, rather than deterministic work, establishes improvement. [Dedicated audit](cleanup/Theta-mapped_det_ne_zero_aux-performance.md).
Revisit source/audit commit `4b9fdf66fa1162e87d50883d1c650ab44b5865c8`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/4b9fdf66fa1162e87d50883d1c650ab44b5865c8).
Frozen Theta SHA256 `1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc`. All owner gates passed as recorded in the audit.
This belongs to original29 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh independent filewide simplify/quality review, then final original/caller/allactual/native/all-declaration performance/full+LeanEval gates. All50 rows in both scoped captures are below1000, but whole-file final phases remain pending. MainLemma actual finite timing remains unmeasured before main_lemma; no whole-project timing claim.


## Validated Theta revisit — index_le_Θ technical hr removal

Removed only unused index_le_Θ.hr, exposing zero weights and removing three caller obligations. Original one-line proof unchanged; two internal index_separated calls and one MainLemma call delete exactly that argument. Fresh filewide review recommended this under standing authorization; Θ_unique_le.hr remains for its next checkpoint. [Dedicated audit](cleanup/Theta-index_le_Theta-technical-hr.md).
Revisit source/audit commit `34102b2ba52a952cecd11df7d030b44454697ece`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/34102b2ba52a952cecd11df7d030b44454697ece).
Frozen Theta SHA256 `0afac9d3af66eb80eab0bc2d8aa9c50dd2f61d693ff0868663b274a550509763`. All owner gates passed as recorded in the audit.
This belongs to original9 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:dedicated Θ_unique_le.hr checkpoint, then fresh final independent filewide review and owner finalgates. All50 below1000 once, with unrelated750–1000 rows awaiting finalwholefile repeated profiling; no finalwholefile performancepass. MainLemma actualtiming unavailable after fresh60s pretargetcutoff(5/27).


## Validated Theta revisit — Θ_unique_le technical hr removal

Removed only unused public Θ_unique_le.hr, admitting zero natural weights with the same logarithmic bound. Two private caller arguments removed; their positivity contracts retained and existing base denominator nonzero evidence made explicit. Original three-line target proof unchanged, no new helper, MainLemma unchanged. [Dedicated audit](cleanup/Theta-Theta_unique_le-technical-hr.md).
Revisit source/audit commit `367508ced3cb06f20874c08d30361a261b14a1a9`: [GitHub checkpoint](https://github.com/SmwYin/Roth/commit/367508ced3cb06f20874c08d30361a261b14a1a9).
Frozen Theta SHA256 `ff85b7f132cf83c980323449b38558699e7e39d5a1b8bd895ac3374d78310207`. All owner gates passed as recorded in the audit.
This belongs to original20 batch; original counts remainTheta35/35,
overall216/264,9/14files. No count inflation from helper/revisit audits.
Next:fresh final independent filewide assessment of both resolved hr recommendations, then owner finalcumulative/allactual/native/all-declaration profile/full+LeanEval gates. All50 below750 in this scoped capture, but final filewide assessment/ownergates pending. MainLemma actualtiming remains unavailable after prior60s pretargetcutoff; unchanged MainLemma has no direct Θ_unique_le call and that timeout was not gratuitously repeated.


### Theta final file phases — immutable source ff85b7f1

Fresh final independent review and owner cumulative/allactual/native/affectedmodule/whole50profile/fullTHENseparateEval gates pass; all17pins remain exact. See[Theta-final.md](cleanup/Theta-final.md) for actual commands/timings/all50table, warnings and evidence hashes. Original counts unchanged216/264; completed files advance9→10after successful finalpublication. Standing implementrecommended authorization and explicit retained choices remain. NextMainLemma; actualcaller timing limitation and single authorized globalIndexrename carried honestly. Finalaudit commit hash is recorded in the following publication entry.


### Theta final publication — a2e286bbf82d22dd11c25c34c5879495342820a2

Final audit commit `a2e286bbf82d22dd11c25c34c5879495342820a2` completes all Theta file phases on unchanged source
SHA256 `ff85b7f132cf83c980323449b38558699e7e39d5a1b8bd895ac3374d78310207`.
Fresh final semantics: 1,223 checks and all 50 actual proof-body/type/standard-axiom sets.
Complete unfiltered diagnostics: zero errors, warnings 6/3/4/0/0. Actual whole-file first
and required repeat maxima 778.325/907.046 ms; all 50 declarations pass both sweeps.
Affected-module build 4.802 s, full build 6.695 s THEN separate LeanEval 3.353 s; all exit 0
and all 17 source/configuration pins remain identical. All compiler/native requests drained.
Counts are 216/264 original declarations, Theta 35/35 and 10/14 completed files.
[Final audit](cleanup/Theta-final.md) and [independent review](cleanup/Theta-final-simplify-final.md).
Next file: MainLemma; its unavailable actual caller timing and existing warnings remain
explicit next-file work. The single authorized Index rename remains in the global pass queue.
Successful push and a clean HEAD=origin are required before the owner releases source,
shared reports and Git to the next file owner.


### MainLemma original1 checkpoint — lam

Source/audit commit `1a0c4a2d3b1d32c83ca0dd4867a16c2c890b254b`; this following metadata child records that exact
checkpoint and is pushed with it before original2 edits. MainLemma1/27originals,overall217/264,
10/14fully completefiles. Phase0/1/2/3 preparation and full fresh lam24audit/42golf/5search/
11verification checklist complete. Definition,public docs and contract unchanged. Exact
independent original formula/typeAST/universes/binder names/order/BinderInfo/value and only
standard3axioms pass. Actual affectedmodule+Main and fullfile commands exit0; complete unfiltered
native MainLemma/Main diagnostics succeed(nonpartial,nontimeout,no faileddependencies),0errors,
3/4preservedwarnings. Anchored lam profile87.948ms (allrawUTF8/prefix/sourcehashes retained).
Owner all-artifact rehash/exact-anchor/original checks pass; fullbuild31.136s THEN separate
LeanEval31.436s exit0,17pins immutable. Source708→709lines solely import grouping. Reports:
`cleanup/MainLemma.md`,`cleanup/MainLemma-lam.md`; owner evidence
`/private/tmp/roth-mainlemma-owner/lam-owner-checkpoint.json`. All processes drained before
publication;nextoriginalgam remains unedited. MainLemma finalfile/simplify/fullprofile pending.


### MainLemma original2 checkpoint — gam

Source/audit commit `29aefe0e10fa69110d755f3e7aa0a1ab4f1b5be5`; the following metadata child records and publishes this
exact checkpoint before the next original edit. MainLemma2/27,overall218/264,
10/14fullycompletedfiles. [Dedicated audit](cleanup/MainLemma-gam.md) contains all
24audit/42golf/5search/11verification steps,exact independent original reimplementation/
effectivecontract/universe/binder/type/value/standard-axiom evidence,actual affectedmodule/
fullfile and complete unfiltered native successes. Actual anchored profile22.088ms;
raw evidence and required repeat/failure history are preserved. The gam formula,public documentation and complete call contract remain unchanged.
Owner fullbuild6.346s THEN separateLeanEval3.305s,both exit0,all17pins immutable;sourceSHA256`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`,
current709lines. Owner rehash/review and sourcefreeze checks pass. All owned processes
and native requests drained before publication;nextoriginaleta remains unedited.
MainLemma finalfile/simplify/completeprofile phases pending. Metadata child changes only
this checkpoint record,not source or verification inputs.


### MainLemma original3 checkpoint — eta

Source/audit commit `0b4426496fb9da24234435a3f4000ad7fb5161d7`; the following metadata child records and publishes this
exact checkpoint before the next original edit. MainLemma3/27,overall219/264,
10/14fullycompletedfiles. [Dedicated audit](cleanup/MainLemma-eta.md) contains all
24audit/42golf/5search/11verification steps,exact independent original reimplementation/
effectivecontract/universe/binder/type/value/standard-axiom evidence,actual affectedmodule/
fullfile and complete unfiltered native successes. Actual anchored profile14.910ms;
raw evidence and required repeat/failure history are preserved. The eta formula,public documentation and complete call contract remain unchanged.
Owner fullbuild6.262s THEN separateLeanEval2.937s,both exit0,all17pins immutable;sourceSHA256`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`,
current709lines. Owner rehash/review and sourcefreeze checks pass. All owned processes
and native requests drained before publication;nextoriginalB₁ remains unedited.
MainLemma finalfile/simplify/completeprofile phases pending. Metadata child changes only
this checkpoint record,not source or verification inputs.


### MainLemma original4 checkpoint — B₁

Source/audit commit `4169f41db8fbbe28fc2146e037493816a062ce85`; the following metadata child records and publishes this
exact checkpoint before the next original edit. MainLemma4/27,overall220/264,
10/14fullycompletedfiles. [Dedicated audit](cleanup/MainLemma-B₁.md) contains all
24audit/42golf/5search/11verification steps,exact independent original reimplementation/
effectivecontract/universe/binder/type/value/standard-axiom evidence,actual affectedmodule/
fullfile and complete unfiltered native successes. Actual anchored profile29.417ms;
raw evidence and required repeat/failure history are preserved. Formula and domains unchanged; queued B₁→mainCoeffBound for the final project-wide rename pass,with the prior Index entry preserved.
Owner fullbuild5.439s THEN separateLeanEval5.054s,both exit0,all17pins immutable;sourceSHA256`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`,
current709lines. Owner rehash/review and sourcefreeze checks pass. All owned processes
and native requests drained before publication;nextoriginalexists_delta_bound remains unedited.
MainLemma finalfile/simplify/completeprofile phases pending. Metadata child changes only
this checkpoint record,not source or verification inputs.


### MainLemma original5 checkpoint — exists_delta_bound

Source/audit commit `e124c7aa8f941f9ebc94d4a09c359455c5c770e8`; the following metadata child records and publishes this
exact checkpoint before the next original edit. MainLemma5/27,overall221/264,
10/14fullycompletedfiles. [Dedicated audit](cleanup/MainLemma-exists_delta_bound.md) contains all
24audit/42golf/5search/11verification steps,exact independent original reimplementation/
effectivecontract/universe/binder/type/value/standard-axiom evidence,actual affectedmodule/
fullfile and complete unfiltered native successes. Actual anchored profile765.392ms;
raw evidence and required repeat/failure history are preserved. Removed hn and strengthened the uniform interval to 0≤δ≤δ₀; proof30→15lines,0helpers. Necessary Pow.Continuity import; two exact Main calls and approved one-line explicit-premise linarith repair. Final target765.392/739.630ms; Main consumer1430.559/1459.407ms improves on original3926.336/3727.365 but remains in the Main-nextfile performance queue,with no Main audit credit. Fresh owner root/LeanEval native closure is complete,zero messages/errors. Explicit prior-parameter measurement addenda correct root accounting to lam87.929,gam22.074,eta14.891,B₁29.399ms;all raw evidence retained.
Owner fullbuild6.304s THEN separateLeanEval3.290s,both exit0,all17pins immutable;sourceSHA256`37ac02db4702d7c91a21f66ee1f7f22bdf8b6c6c23e3ab740cc7d1a9c679fefc`,
current694lines. Owner rehash/review and sourcefreeze checks pass. All owned processes
and native requests drained before publication;nextoriginaleta_lt_gam_iff remains unedited.
MainLemma finalfile/simplify/completeprofile phases pending. Metadata child changes only
this checkpoint record,not source or verification inputs.


### MainLemma original1–4 profile-accounting correction

Source/audit commit `e124c7aa8f941f9ebc94d4a09c359455c5c770e8` includes explicit append-only corrections to the four
earlier reports and MainLemma ledger. Exact target command/async roots give lam87.929ms
(previous87.948),gam22.074ms(previous22.088),eta14.891ms(previous14.910),B₁29.399ms
(previous29.417). Earlier sums included unindented internal Meta.whnf events; corrected
sums exclude those internal/nested events and following end-command/lint work. All
four budget results remain passes. Raw evidence and both old/new sums are retained;
no earlier checkpoint history was silently rewritten. Owner evidence:
`/private/tmp/roth-mainlemma-owner/prior-profile-root-reaudit.json`. Future workers and
final whole-file gates must use exact anchored Elab.command/Elab.async roots.
