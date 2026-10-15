# Roth cleanup progress

Started: 2026-10-14 (America/Chicago).

## Scope and preservation

- Work in the existing checkout, on `ramin-cleanup`, created from local `main` at
  `d2eb5e9a1806e12e66db25d15d8954ade4be9874`.
- The working tree was clean at entry; the previous branch, `ramin-edits`, remains intact.
- Preserve mathematical meaning, theorem contracts, and the pinned Lean/mathlib versions.
- Validate, commit, and push each completed declaration cleanup before proceeding.
- No pushes to `main`, force pushes, or merges.
- User-approved deferral policy (2026-10-15): record proposed changes that need user
  input and why approval is needed, leave them unapplied, and continue independent
  cleanup in declaration order. Mark those declarations reviewed with deferral.
  Required system approvals remain mandatory.

## Current status

Build/tool setup completed; GitHub browser authentication and branch publication succeeded. The first file audit
(`Roth/HasseDeriv.lean`, 26 declarations) is in progress. The first thirteen declarations,
through private `choose_mul_choose_eq`, have completed their audits and
validation; 13 of 264 declarations reviewed, including seven
with deferred API proposals. File-level final
review and profiling remain pending.

Active cleanup resumed at the user's request after the ninth checkpoint. Continue
sequential declaration validation, commit, and push through every remaining file in
the inventory order below, without waiting for a new prompt at file boundaries.
Each file still requires its final independent review, profiling, and full build.
Next declaration: private `hasseCoeff_mul_hasseCoeff`. The file and project cleanup remain
incomplete; optional substantive proposals remain unapplied.

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
| lean-lsp-mcp | 0.31.0 | 22 native tools are now registered. Native Loogle and LeanFinder requests succeeded; LeanSearch returned HTTP 500. Direct-client local search, goal inspection, file diagnostics, and code execution also succeeded. Not all 22 tools have been individually tested. |
| GitHub CLI | 2.102.0 | Browser authentication and branch push succeeded |
| ask_chatgpt_math | Skipped | Optional, as authorized |

The Lean LSP server is configured in `~/.codex/config.toml` using its absolute executable
path. Native tools became registered during this session and native remote search was
verified successfully. Older worker sessions can still use the tested direct stdio MCP
client as a fallback. The first 45-second diagnostic request timed out; a retry with
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
| `Roth/HasseDeriv.lean` | 329 | In progress: 13/26 declarations reviewed; next private `hasseCoeff_mul_hasseCoeff` |
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

## Validation and deferrals

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
- File-level profiling and final project verification remain pending.
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
