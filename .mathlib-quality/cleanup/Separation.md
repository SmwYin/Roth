# Separation — active file audit

Baseline commit `a39317e`; source618lines,30original declarations.

## Baseline (Phase 0)

- Optional cache fetch skipped: pinned dependencies already cached.
- Actual `lake build`,session11782 exit0; `/private/tmp/roth-separation-baseline-full.log`.
- Complete native LSP: success=true,partial=false,timed_out=false,0errors,32warnings; `/private/tmp/roth-separation-baseline-lsp.json`.
- No separate project runLinter executable; complete Lean diagnostics supply linter results.

## Phase 2 punch-list

| Item | Finding / action |
|---|---|
| A.1 header | Missing metadata; preserve per explicit user decision. |
| A.2 module doc | Present, substantial source references; preserve. |
| A.3 imports | Six imports alphabetized; add group blank line during final file pass. |
| A.4 section headers | No contentless headers. Named General/Domain/Field/Integrality sections preserve structure. |
| A.5 size | 618lines; below1000. |
| A.6 options | No limit raises/debug/lint suppressions. |
| A.7 mechanical | No legacy lambda/dollar/push_neg; Unicode lambda and per-proof changes audited individually. |

### Full baseline warnings

| Line | Diagnostic |
|---|---|
| 1 | * `-/`: |
| 53 | automatically included section variable(s) unused in theorem `Roth.eq_mapDomain_some_add_single`: |
| 100 | automatically included section variable(s) unused in theorem `Roth.coeff_coeffNone`: |
| 52 | `eq_mapDomain_some_add_single` does not use the following hypothesis in its type: |
| 52 | `eq_mapDomain_some_add_single` does not use the following hypothesis in its type: |
| 99 | `coeff_coeffNone` does not use the following hypothesis in its type: |
| 99 | `coeff_coeffNone` does not use the following hypothesis in its type: |
| 125 | `degreeOf_coeffNone_le` does not use the following hypothesis in its type: |
| 125 | `degreeOf_coeffNone_le` does not use the following hypothesis in its type: |
| 106 | `eq_sum_X_none_pow_mul_coeffNone` does not use the following hypothesis in its type: |
| 106 | `eq_sum_X_none_pow_mul_coeffNone` does not use the following hypothesis in its type: |
| 72 | `coeff_X_none_pow_mul_rename` does not use the following hypothesis in its type: |
| 72 | `coeff_X_none_pow_mul_rename` does not use the following hypothesis in its type: |
| 257 | automatically included section variable(s) unused in theorem `Roth.degreeOf_rename_mul_aeval`: |
| 268 | automatically included section variable(s) unused in theorem `Roth.degreeOf_none_rename_mul_aeval`: |
| 207 | automatically included section variable(s) unused in theorem `Roth.hasseDeriv_rename_mul_aeval`: |
| 134 | `coeff_rename_mul_aeval` does not use the following hypothesis in its type: |
| 134 | `coeff_rename_mul_aeval` does not use the following hypothesis in its type: |
| 204 | `hasseDeriv_rename_mul_aeval` does not use the following hypothesis in its type: |
| 204 | `hasseDeriv_rename_mul_aeval` does not use the following hypothesis in its type: |
| 254 | `degreeOf_rename_mul_aeval` does not use the following hypothesis in its type: |
| 254 | `degreeOf_rename_mul_aeval` does not use the following hypothesis in its type: |
| 266 | `degreeOf_none_rename_mul_aeval` does not use the following hypothesis in its type: |
| 266 | `degreeOf_none_rename_mul_aeval` does not use the following hypothesis in its type: |
| 361 | `det_hasseDeriv_separated` does not use the following hypothesis in its type: |
| 361 | `det_hasseDeriv_separated` does not use the following hypothesis in its type: |
| 579 | `exists_det_eq_mul` does not use the following hypothesis in its type: |
| 579 | `exists_det_eq_mul` does not use the following hypothesis in its type: |
| 284 | `exists_separated_representation` does not use the following hypothesis in its type: |
| 284 | `exists_separated_representation` does not use the following hypothesis in its type: |
| 521 | `exists_int_factors` does not use the following hypothesis in its type: |
| 521 | `exists_int_factors` does not use the following hypothesis in its type: |

### Original declaration inventory

| # | Name | Line | Visibility / light scan |
|---|---|---:|---|
| 1 | `mapDomain_some_none` | 49 | Private helper; no docstring required; naming describes mathematics; span≤4lines. |
| 2 | `eq_mapDomain_some_add_single` | 53 | Public; docstring present; naming describes mathematics; span≤9lines. |
| 3 | `some_mapDomain_add_single` | 62 | Private helper; no docstring required; naming describes mathematics; span≤6lines. |
| 4 | `mapDomain_add_single_none` | 68 | Private helper; no docstring required; naming describes mathematics; span≤4lines. |
| 5 | `coeff_X_none_pow_mul_rename` | 72 | Private helper; no docstring required; naming describes mathematics; span≤24lines. |
| 6 | `coeffNone` | 96 | Public; docstring present; naming describes mathematics; span≤4lines. |
| 7 | `coeff_coeffNone` | 100 | Public; docstring present; naming describes mathematics; span≤10lines. |
| 8 | `eq_sum_X_none_pow_mul_coeffNone` | 110 | Public; docstring present; naming describes mathematics; span≤17lines. |
| 9 | `degreeOf_coeffNone_le` | 127 | Public; docstring present; naming describes mathematics; span≤10lines. |
| 10 | `coeff_rename_mul_aeval` | 137 | Public; docstring present; naming describes mathematics; span≤21lines. |
| 11 | `aeval_X_eq_rename` | 158 | Public; docstring present; naming describes mathematics; span≤15lines. |
| 12 | `degreeOf_none_rename_some` | 173 | Private helper; no docstring required; naming describes mathematics; span≤9lines. |
| 13 | `degreeOf_aeval_X_none_of_ne` | 182 | Private helper; no docstring required; naming describes mathematics; span≤12lines. |
| 14 | `rename_some_ne_zero` | 194 | Private helper; no docstring required; naming describes mathematics; span≤5lines. |
| 15 | `aeval_X_none_ne_zero` | 199 | Private helper; no docstring required; naming describes mathematics; span≤8lines. |
| 16 | `hasseDeriv_rename_mul_aeval` | 207 | Public; docstring present; naming describes mathematics; span≤21lines. |
| 17 | `coeff_uniqueAlgEquiv_symm` | 228 | Public; docstring present; naming describes mathematics; span≤5lines. |
| 18 | `degreeOf_uniqueAlgEquiv_symm` | 233 | Public; docstring present; naming describes mathematics; span≤24lines. |
| 19 | `degreeOf_rename_mul_aeval` | 257 | Public; docstring present; naming describes mathematics; span≤11lines. |
| 20 | `degreeOf_none_rename_mul_aeval` | 268 | Public; docstring present; naming describes mathematics; span≤22lines. |
| 21 | `exists_separated_representation` | 290 | Public; docstring present; naming describes mathematics; span≤75lines—structure review required. |
| 22 | `det_hasseDeriv_separated` | 365 | Public; docstring present; naming describes mathematics; span≤33lines—structure review required. |
| 23 | `exists_sum_mul_eq_gcd` | 398 | Public; docstring present; naming describes mathematics; span≤23lines. |
| 24 | `exists_nat_smul_eq_map` | 421 | Public; docstring present; naming describes mathematics; span≤27lines. |
| 25 | `exists_primitive_smul_eq` | 448 | Public; docstring present; naming describes mathematics; span≤43lines—structure review required. |
| 26 | `exists_int_eq_of_gcd_eq_one` | 491 | Public; docstring present; naming describes mathematics; span≤17lines. |
| 27 | `map_aeval_X_none` | 508 | Private helper; no docstring required; naming describes mathematics; span≤9lines. |
| 28 | `degreeOf_map_intCast` | 517 | Private helper; no docstring required; naming describes mathematics; span≤8lines. |
| 29 | `exists_int_factors` | 525 | Public; docstring present; naming describes mathematics; span≤59lines—structure review required. |
| 30 | `exists_det_eq_mul` | 584 | Public; docstring present; naming describes mathematics; span≤35lines—structure review required. |

## Work policy

Fresh dedicated worker per original declaration and independently audited added helpers. No public contract change before scoped user approval. Each source freeze requires owner sequential full and separate LeanEval builds, exact-path staged set, commit and successful cleanup-branch push before the next declaration. Original d01 validated and published by its checkpoint;1/30 originals audited,overall152/264 after successful publication. Source616lines,29retained. Public12-theorem instance proposal remains pending approval.

## d01 completed declaration checkpoint

[mapDomain_some_none](Separation-mapDomain_some_none.md): private library wrapper deleted;four direct specialisations. All20 original public contracts/definition/docs preserved. Owner complete ORIGINAL30 reproof/public20 exact type-value comparisons/all29 actual standard axioms73355exit0; sequential full/separateLeanEval39911exit0(127.65/32.76s),hash stable. Actual source618→616; target103.002ms before deletion. Exact-path commit and successful push precede next declaration.

## d02 completed declaration checkpoint

[eq_mapDomain_some_add_single](Separation-eq_mapDomain_some_add_single.md):5→3prooflines; original public contract/docs preserved. Owner14103 independent ORIGINAL30/public20/actual29standardaxioms pass; sequentialfull/separateLeanEval22880exit0(122.05/30.04s),stable hashes. ACTUAL module anchored profile2444exit0:98.126ms. Source614lines;2/30 originals,overall153/264 after successful publication. Public omission menu and optional generic coefficient generalization remain unapplied.

## d03 completed declaration checkpoint

[some_mapDomain_add_single](Separation-some_mapDomain_add_single.md): private wrapper removed,exactly2callers use generic existing API. Source614→611;28retained (20public/8private). Owner90175 independent ORIGINAL30/public20type-value/ALL28actualstandardaxioms pass. Sequentialfull/separateLeanEval94244exit0(124.01/30.50s),frozen hashes stable. Actual module changed callers51.006/394.509ms. All original block docs byte-identical.3/30 originals,overall154/264 after successful publication. Historical d02 counts corrected from git to proof5→3/file616→614; checks/counts unaffected. No public omission applied.


## d04 completed declaration checkpoint — mapDomain_add_single_none

[Dedicated audit](Separation-mapDomain_add_single_none.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Redundant private scalar-evaluation wrapper removed; exactly two uses inline terminal simp equality proofs after direct dependent-if expansion was tested and reverted. No public signature, definition, documentation or pin change; no new helper or rename. Source611→610;27retained. Separation4/30,overall155/264 original audits after successful publication;8/14files complete.

Actual module 35267 exit 0; complete unfiltered native LSP 0 errors/32 baseline warnings, success=true, partial=false, timed_out=false; `/private/tmp/roth-separation-d04-lsp.json`. Exact ORIGINAL independent proof 96354 exit 0, only standard axioms. Leaf additional cumulative original/actual-axiom probe 39457 passed; its temporary compatibility path is subsequently reused by the fresh owner probe, whose evidence below is authoritative.

ACTUAL repository module anchored profile 79783 exit 0: changed coeff_coeffNone 108.746 ms and coeff_rename_mul_aeval 524.749 ms, both below 750/1000 ms; `/private/tmp/roth-separation-d04-final-profile.log` and `...-profile-anchors.json`. Original unchanged target baseline 69.331 ms; deleted target has no final cost. No source profiler scaffolding or limits.

Source FROZEN SHA256 `1fd92ece12094dc1d71783cfcfe6b7f92e92cf019d409e048e70f1074208831d`; leaf ownership revoked and requests drained before owner gates. Owner probe `48051` exit0,39.71s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d04-compatibility.{lean,log,json}`. Owner build session `79342` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.27s/27.24s; source hash stable. `/private/tmp/roth-separation-d04-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## d05 completed declaration checkpoint — coeff_X_none_pow_mul_rename

[Dedicated audit](Separation-coeff_X_none_pow_mul_rename.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Option-equivalence polynomial coefficient calculation replaces nested exponent-subtraction casework; both unused private Fintype/DecidableEq instances omitted. Target body 20 to 11 lines; no public contract, definition, documentation or other proof changed; no new helper or rename. Source610→602;27retained. Separation5/30,overall156/264 original audits after successful publication;8/14files complete.

Actual lake build Roth.Separation exits 0 (`/private/tmp/roth-separation-d05-build.log`). Complete native unfiltered LSP success=true/partial=false/timed_out=false, no failed dependencies, 0 errors/31 warnings (`...-final-lsp.json`). Two target warnings removed; coeff_rename_mul_aeval newly exposes one unusedSectionVars warning for its unchanged pending public instances: 32 - 2 + 1 = 31. Independent exact ORIGINAL proof/type and actual built target/affected public standard axioms pass (`...-independent.{lean,log}`, `...-axioms.{lean,log}`).

ACTUAL repository module anchored profile exits 0 (`/private/tmp/roth-separation-d05-final-profile.log`, `...-profile-anchors.json`): target before 248.710 ms, final outer omit 60.400 + async 209.913 = 270.313 ms. Actual affected callers eq_sum_X_none_pow_mul_coeffNone 157.857 ms and coeff_rename_mul_aeval 428.503 ms. All below 750/1000 ms; no speedup claim, scaffolding, limits or deferral.

Source FROZEN SHA256 `c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`; leaf ownership revoked and requests drained before owner gates. Owner probe `16920` exit0,48.70s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d05-compatibility.{lean,log,json}`. Owner build session `8141` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,139.72s/32.94s; source hash stable. `/private/tmp/roth-separation-d05-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## d06 completed declaration checkpoint — coeffNone

[Dedicated audit](Separation-coeffNone.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Semantic coefficient definition retained byte-identically: existing coefficient/expansion/degree API and multiple uses justify it. Every effective binder, actual negative probes, public literature and definition type/value preservation audited. No source, visibility, API, documentation or import change. Source602→602;27retained. Separation6/30,overall157/264 original audits after successful publication;8/14files complete.

Actual module build exits 0. Native COMPLETE unfiltered LSP success=true/partial=false/timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`/private/tmp/roth-separation-d06-final-lsp.json`). Independent original type/value reconstruction imports only Mathlib and exits 0; actual built definition type/value and standard-axiom checks pass (`...-independent.{lean,log}`, `...-axioms.{lean,log}`). Six actual negative binder probes and arbitrary-universe positive base compile evidence in `...-binder-probes.json`.

Source and exact target are unchanged from ACTUAL repository-module profile `/private/tmp/roth-separation-d05-final-profile.log{,.json}`: coeffNone command 12.094 ms, no async proof; below 750/1000 ms. No redundant profiling run, scaffolding, limits, performance claim or deferral.

Source FROZEN SHA256 `c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`; leaf ownership revoked and requests drained before owner gates. Owner probe `43989` exit0,34.00s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d06-compatibility.{lean,log,json}`. Owner build session `69566` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.86s/2.87s; source hash stable. `/private/tmp/roth-separation-d06-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## d07 completed declaration checkpoint — coeff_coeffNone

[Dedicated audit](Separation-coeff_coeffNone.md): all24/42/fiveactualsearches/everybinder/width/inequality/11steps; Direct optionEquivLeft_coeff_coeff calculation and coordinate extensionality replace embedding and inline scalar-evaluation rewrites. Current-start proof six to five physical lines; original public effective signature/docs preserved, no helper, import or other declaration change. Source602→601;27retained. Separation7/30,overall158/264 original audits after successful publication;8/14files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d07-module.log`). Complete native unfiltered LSP success=true/partial=false/timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Independent ORIGINAL definition/type recovery and non-self proof compile; actual built target and independent proof use only standard axioms (`...-independent.{lean,log}`). All eight effective binders drop-tested and Semiring weakening tested; initial import-race negatives retried and excluded from successful evidence. Individual/joint public instance omissions compile but remain pending/unapplied.

ACTUAL repository-module anchored profile exits 0 (`/private/tmp/roth-separation-d07-final-profile.log{,.json}`): command 9.753 + async 105.724 = 115.477 ms, below 750/1000 ms. Baseline 105.435 ms; no speedup claim, scaffolding, raised limit or deferral.

Source FROZEN SHA256 `a3a41139893974634024440f0897d72359502621f287671625d000e2bb3fc25b`; leaf ownership revoked and requests drained before owner gates. Owner probe `48331` exit0,44.71s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d07-compatibility.{lean,log,json}`. Owner build session `87726` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,139.54s/33.53s; source hash stable. `/private/tmp/roth-separation-d07-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public12-theorem instance menu remains pending/unapplied; header remains user-preserved.


## d08 completed declaration checkpoint — eq_sum_X_none_pow_mul_coeffNone

[Dedicated audit](Separation-eq_sum_X_none_pow_mul_coeffNone.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Final support-zero branch now uses a direct degree-bound argument instead of contradiction, an anonymous have and omega; proof 11 to 9 lines, source 601 to 599. No public signature, documentation, import or helper changes. Source 601 → 599; 27 retained declarations. Separation 8/30, overall 159/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d08-module.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Independent exact original-type proof using polynomial equivalence transport and a counterexample to dropping hn compile; actual built target and independent proof use only standard axioms (`...-independent.{lean,log}`). All 11 binder probes completed; individual/joint instance omissions and Fintype-to-Finite weakening compile but remain pending and unapplied.

Actual repository-module profile exit 0 (`/private/tmp/roth-separation-d08-final-profile.log{,.json}`): command 26.740 + async proof 116.512 = 143.252 ms, below 750/1000 ms; baseline 137.595 ms. No speedup claim, profiler scaffolding, raised limits or deferral.

Source FROZEN SHA256 `24c37da51aee81b82da351937cb595a67679f2f566d475e8b72aecccad1a8a16`; leaf ownership revoked and requests drained before owner gates. Owner probe `19855` exit0,41.30s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d08-compatibility.{lean,log,json}`. Owner build session `64974` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,113.98s/26.46s; source hash stable. `/private/tmp/roth-separation-d08-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved.


## d09 completed declaration checkpoint — degreeOf_coeffNone_le

[Dedicated audit](Separation-degreeOf_coeffNone_le.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; The coefficient support lemma replaces coefficient/multidegree rewriting; proof four to two physical lines, file 599 to 597. Public signature and documentation preserved; no helper, import or other declaration change. Source 599 → 597; 27 retained declarations. Separation 9/30, overall 160/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d09-build.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/32 warnings (`...-final-lsp.json`): one unusedSectionVars warning newly exposed because this proof no longer indirectly consumes the inherited public index instances. Their omission remains pending and unapplied. Independent exact original type/non-self Finset-sup proof and actual built target standard-axiom checks pass (`...-independent.{lean,log}`); every effective binder has actual native probe evidence.

Actual repository-module profile exits 0 (`/private/tmp/roth-separation-d09-final-profile.log{,.json}`): command 4.112 + async 36.412 = 40.524 ms, baseline 66.515 ms; one anchor each and below 750/1000 ms. No whole-project speedup claim, source profiler scaffolding or raised limits.

Source FROZEN SHA256 `72f715a6efc3664bfad5d760b598939f131a32393988c886da69206e67e1dc12`; leaf ownership revoked and requests drained before owner gates. Owner probe `68300` exit0,54.14s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d09-compatibility.{lean,log,json}`. Owner build session `50653` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,158.46s/38.75s; source hash stable. `/private/tmp/roth-separation-d09-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved.


## d10 completed declaration checkpoint — coeff_rename_mul_aeval

[Dedicated audit](Separation-coeff_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Direct polynomial-equivalence coefficient calculation replaces the support expansion, sum and case split. Body 18 to 7 lines; source 597 to 586, 27 retained. Public signature/docs unchanged, no helper or other declaration edit. Source 597 → 586; 27 retained declarations. Separation 10/30, overall 161/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0; complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 warnings (`/private/tmp/roth-separation-d10-final-lsp.json`). One unusedSectionVars warning disappears because the new proof consumes the retained public coefficient bridge. Exact original type and independent non-self proof compile, actual target/bridge/caller use only standard axioms. All 12 binder suite cases finish; semantic instance omissions compile with an isolated probe-local bridge, whereas literal final-proof-only omission still depends on earlier retained public bridge instances. The grouped public proposal remains pending and unapplied.

Actual repository-module sweeps exit 0: preceding 842.772 ms borderline measurement is reswept at 490.631 ms unchanged baseline; final target 52.568 + 215.845 = 268.413 ms, below 750/1000 ms (`/private/tmp/roth-separation-d10-final-profile.log{,.json}`). Future original 21 exists_separated_representation measures 1342.091 ms and remains tracked for its dedicated audit, not claimed under budget here. No source profiler scaffolding, raised limits or target deferral.

Source FROZEN SHA256 `721b7cde6fe0430a6e37e3fd92be12f272ad38ed8409de2acfdb81567ca7dacb`; leaf ownership revoked and requests drained before owner gates. Owner probe `87314` exit0,40.79s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d10-compatibility.{lean,log,json}`. Owner build session `51365` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,123.85s/29.72s; source hash stable. `/private/tmp/roth-separation-d10-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved.


## d11 completed declaration checkpoint — aeval_X_eq_rename

[Dedicated audit](Separation-aeval_X_eq_rename.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Existing Polynomial.toMvPolynomial_eq_rename_comp gives the proof directly via AlgHom.congr_fun. Body ten to one physical lines, declaration 13 to 4, source 586 to 577 (+2/−11 Git diff). Public type/docs preserved; no new helper or other source edit. Source 586 → 577; 27 retained declarations. Separation 11/30, overall 162/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d11-build.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Exact original effective type and independent non-self original proof compile after actual module build; actual target and independent proof use only standard three axioms (`...-independent.{lean,log}`). Every effective binder and parent weakening has actual probe evidence; original type has no τ/Fintype/DecidableEq section assumptions.

Actual repository-module profile exits 0 (`/private/tmp/roth-separation-d11-final-profile.log{,.json}`), command 24.091 + async 18.511 = 42.602 ms; baseline 201.535 ms, below 750/1000 ms. No profiler scaffolding, raised limit or performance deferral.

Source FROZEN SHA256 `9ca5d14b3bcfba066fa924fc0f6eca5aa5b13d88dbabeab9a281a749bbd689c1`; leaf ownership revoked and requests drained before owner gates. Owner probe `23627` exit0,42.59s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d11-compatibility.{lean,log,json}`. Owner build session `63999` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.32s/32.64s; source hash stable. `/private/tmp/roth-separation-d11-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved. D11 additionally identifies an optional public-wrapper deletion with two Theta rewrite substitutions. The retained public name is unchanged; coordinator notified, no API deletion or Theta edit applied.


## d12 completed declaration checkpoint — degreeOf_none_rename_some

[Dedicated audit](Separation-degreeOf_none_rename_some.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Redundant private wrapper removed, exactly two callers use direct degree/rename simplification. Source 577 to 570 lines (11 removed, 4 added), 27 to 26 retained declarations. No public signature, definition, documentation or import change. Source 577 → 570; 26 retained declarations. Separation 12/30, overall 163/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d12-module.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 unchanged warnings (`...-final-lsp.json`). Independent exact original type/non-self proof and actual two changed public caller axiom checks exit 0, only standard three axioms (`...-original-axioms.log`). All binder compiler probes and native requests completed and drained; private literature exemption recorded.

Actual final full-module profile exits 0, fully drained (`/private/tmp/roth-separation-d12-final-profile.log{,.json}`): changed hasseDeriv_rename_mul_aeval 65.655 + 182.016 = 247.671 ms; degreeOf_none_rename_mul_aeval 21.430 + 80.199 = 101.629 ms. Both below 750/1000 ms. Removed target baseline 95.394 ms, no final target cost; no profiler scaffolding or raised limits.

Source FROZEN SHA256 `1d7e167ce78eb18a4815866a71a286989095d26499f49534db6af2ee823d2137`; leaf ownership revoked and requests drained before owner gates. Owner probe `83868` exit0,63.55s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d12-compatibility.{lean,log,json}`. Owner build session `20284` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,113.27s/25.24s; source hash stable. `/private/tmp/roth-separation-d12-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Public 12-theorem instance menu remains pending and unapplied; header remains user-preserved. Optional public renaming-wrapper removal is separate: two Theta uses plus five internal uses at four Separation sites require changes. The public API and all such uses remain in repository source; concrete scratch evidence is documented in Separation-wrapper-proposal.md.


## d13 completed declaration checkpoint — degreeOf_aeval_X_none_of_ne

[Dedicated audit](Separation-degreeOf_aeval_X_none_of_ne.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private helper removed after testing direct degree/rename simplification at both actual callers; source 570 to 562 (Git +7/−15), 26 to 25 retained declarations. Public signatures, definitions, documentation and imports preserved. Source 570 → 562; 25 retained declarations. Separation 13/30, overall 164/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d13-build-removal.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 baseline warnings (`...-removal-lsp.json`). Exact original effective type and independent non-self original support proof compile; both actual changed caller axioms are standard three only (`...-independent-final.log`). All binder negatives have genuine compiler errors after three missing-olean races were retried; raced failures excluded from semantic evidence. All requests drained and source ownership revoked before owner gates.

Actual final repository-module profile exit 0 (`/private/tmp/roth-separation-d13-removal-profile.log{,.json}`): changed hasseDeriv_rename_mul_aeval 75.763 + 393.163 = 468.926 ms, degreeOf_rename_mul_aeval 49.778 + 95.879 = 145.657 ms; one command/async anchor each, below 750/1000 ms. Removed target baseline 53.178 ms, no final target cost. No performance improvement claim, profiler scaffolding or limit increase.

Source FROZEN SHA256 `ba6cdd854cc9e3ae0df16663905d80233ae16b8f2240e8c8326e5ea801b1e1d2`; leaf ownership revoked and requests drained before owner gates. Owner probe `86125` exit0,47.19s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d13-compatibility.{lean,log,json}`. Owner build session `25929` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.57s/30.90s; source hash stable. `/private/tmp/roth-separation-d13-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem instance omissions and optional aeval_X_eq_rename deletion. The public-wrapper scratch candidate is documented against its explicit D12 source hash; later proof cleanup moves its internal call sites, requiring a fresh scan/candidate before any approved application. Header remains user-preserved.


## d14 completed declaration checkpoint — rename_some_ne_zero

[Dedicated audit](Separation-rename_some_ne_zero.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private renaming-nonzero wrapper removed; exactly two callers use rename_eq_zero_iff_of_injective directly. Source 562 to 559 (Git +4/−7), 25 to 24 retained declarations. No public API, definition, documentation or import change. Source 562 → 559; 24 retained declarations. Separation 14/30, overall 165/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d14-build.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-lsp.json`). Exact original type and independent arbitrary-injective-map proof compile; actual changed caller axioms and original-type proof use standard three only (`...-independent-final.log`). All five binder negative probes have actual exit 1 (`...-binders.json`); all requests drained and all source ownership revoked before owner gates.

Actual repository-module final profile exit 0 (`/private/tmp/roth-separation-d14-final-profile.log{,.json}`): degreeOf_rename_mul_aeval 28.381 + 71.092 = 99.473 ms, degreeOf_none_rename_mul_aeval 22.465 + 91.375 = 113.840 ms; one command/async anchor each, below 750/1000 ms. Removed target baseline 103.822 ms, no final target cost. No profiler scaffolding or raised limits.

Source FROZEN SHA256 `5ee248fa04d6ef74d0d6cccb17c898c52302215f62eb480dfa5944562ebe5ea1`; leaf ownership revoked and requests drained before owner gates. Owner probe `59421` exit0,57.83s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL24 actual retained standardaxiom checks. `/private/tmp/roth-separation-d14-compatibility.{lean,log,json}`. Owner build session `84208` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,142.29s/41.59s; source hash stable. `/private/tmp/roth-separation-d14-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem index-instance omissions and optional aeval_X_eq_rename removal. The latter records compiled historical D12 candidates; refresh actual source/caller inventory before eventual approved application. Header remains user-preserved.


## d15 completed declaration checkpoint — aeval_X_none_ne_zero

[Dedicated audit](Separation-aeval_X_none_ne_zero.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private evaluation-nonzero wrapper removed; exactly two callers use mathlib toMvPolynomial injectivity via an explicit aeval hom argument. Source 559 to 555 (Git +4/−8), 24 to 23 retained declarations; public types/docs/definitions/imports unchanged. Source 559 → 555; 23 retained declarations. Separation 15/30, overall 166/264 original audits after successful publication; 8/14 files complete.

Actual corrected module build exits 0 (`/private/tmp/roth-separation-d15-module-build-fixed.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 baseline warnings (`...-final-lsp-fixed.json`). Independent exact original type/non-self proof, arbitrary-index strengthening, actual binder negatives and zero counterexample pass their expected compiler outcomes; actual built callers use standard three axioms only. An initial underscore hom argument folded toMvPolynomial and failed rw matching; explicit Polynomial.aeval fixes it. Failed initial build/profile requests are excluded; corrected successful gates and all request drain are recorded in the dedicated report.

Actual corrected final repository-module profile exits 0 (`/private/tmp/roth-separation-d15-final-profile-fixed.log{,.json}`): degreeOf_rename_mul_aeval 16.682 + 106.199 = 122.881 ms, degreeOf_none_rename_mul_aeval 27.223 + 171.228 = 198.451 ms. Both below 750/1000 ms; removed target baseline 128.446 ms and no final target cost. Caller timings increased relative to this prior sample; library reuse/removal is claimed, no speedup claim. No source profiler scaffolding or raised limits.

Source FROZEN SHA256 `7089df105ebdca3d3358741fa4a574aa44a6f07c870d24838028eb550cac6960`; leaf ownership revoked and requests drained before owner gates. Owner probe `89268` exit0,58.49s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d15-compatibility.{lean,log,json}`. Owner build session `10803` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,147.67s/37.60s; source hash stable. `/private/tmp/roth-separation-d15-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem instance omissions and optional aeval_X_eq_rename deletion. Refresh the latter historical D12 candidate/caller inventory against current source before any approved application. Header remains user-preserved.


## d16 completed declaration checkpoint — hasseDeriv_rename_mul_aeval

[Dedicated audit](Separation-hasseDeriv_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; The support-disjointness side proof uses one simp instead of rintro plus simp; two proof lambda arrows normalized and signature whitespace packed. Proof one line shorter, source 555 to 553 (Git +6/−8), 23 retained. Exact original effective public type and all documentation preserved; no new helper. Source 555 → 553; 23 retained declarations. Separation 16/30, overall 167/264 original audits after successful publication; 8/14 files complete.

Actual final module build exits 0 (`/private/tmp/roth-separation-d16-final-build-fixed.log`). Complete native unfiltered LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-native-lsp.json`). Fresh copied original type/non-self proof and actual target standard-axiom checks exit 0 (`...-final-independent.lean.verified.log`). All binder probes recorded; invalid racing Sort probes replaced by actual Type/Sort mismatch rechecks (`...-probes.json`, `...-recheck.json`). Individual/joint instance omissions and Finite replacement compile but remain pending/unapplied. All requests drained before source freeze and owner gates.

Actual final repository-module profile exits 0 (`/private/tmp/roth-separation-d16-final-profile-fixed.log{,.json}`): command 101.919 + async 602.561 = 704.480 ms, one anchor each, below 750/1000 ms. Prior actual target baseline 275.492 ms; no speedup claimed. No profiling scaffolding, raised limits or target deferral. File-wide final isolated sweeps remain mandatory.

Source FROZEN SHA256 `a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`; leaf ownership revoked and requests drained before owner gates. Owner probe `94037` exit0,34.72s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d16-compatibility.{lean,log,json}`. Owner build session `72373` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,111.23s/28.20s; source hash stable. `/private/tmp/roth-separation-d16-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Both public proposals remain pending and unapplied: 12-theorem instance omissions and optional aeval_X_eq_rename deletion. Refresh historical wrapper-deletion candidate/caller inventory against current source before any approved application. Header remains user-preserved.


## d17 completed declaration checkpoint — coeff_uniqueAlgEquiv_symm

[Dedicated audit](Separation-coeff_uniqueAlgEquiv_symm.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Original coefficient specialization retained byte-identically after full audit. Existing MvPolynomial theorem and Finsupp.single_eq_same already prove it; no project caller uses the Roth wrapper. Full-module deletion candidate compiles but is a separate unapproved public API option. Source unchanged at 553 lines, 23 retained declarations. Source 553 → 553; 23 retained declarations. Separation 17/30, overall 168/264 original audits after successful publication; 8/14 files complete.

Actual module build exits 0 (`/private/tmp/roth-separation-d17-build.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-lsp.json`). Exact original type and independent non-self proof compile natively and via final CLI; actual target and independent proof use standard three axioms (`...-independent-final.log`). All binder/search/literature/width/inequality/completion evidence in dedicated report. Full-module deletion proposal `...-delete-proposal.{lean,log}` compiles exit 0, source untouched. Owner independently verifies every project coefficient reference is explicitly MvPolynomial-qualified.

Unchanged source and target reuse the valid actual repository-module profile `/private/tmp/roth-separation-d16-final-profile-fixed.log{,.json}`: command 11.337 + async 10.160 = 21.497 ms, one anchor each, below 750/1000 ms. No unnecessary repeated profile, profiler scaffolding, raised limit or performance deferral.

Source FROZEN SHA256 `a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`; leaf ownership revoked and requests drained before owner gates. Owner probe `80848` exit0,37.50s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d17-compatibility.{lean,log,json}`. Owner build session `63509` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,6.89s/3.08s; source hash stable. `/private/tmp/roth-separation-d17-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Three public options remain pending and unapplied: 12-theorem instance omissions, optional aeval_X_eq_rename deletion, and optional unused coeff_uniqueAlgEquiv_symm deletion. The latter needs no caller edit and has a full compiled module candidate. Refresh historical wrapper-removal candidates against current source before any approved application. Header remains user-preserved.


## d18 completed declaration checkpoint — degreeOf_uniqueAlgEquiv_symm

[Dedicated audit](Separation-degreeOf_uniqueAlgEquiv_symm.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Coefficient-vanishing criterion replaces the zero/nonzero leading-coefficient branch. Final proof uses mathlib coefficient/support lemmas directly, preserving independence from the pending unused public wrapper deletion. Proof 12 to 10 physical lines, declaration 14 to 12, source 553 to 551; 23 retained declarations. Public type/docs unchanged, no helper. Source 553 → 551; 23 retained declarations. Separation 18/30, overall 169/264 original audits after successful publication; 8/14 files complete.

Actual final module build exits 0 (`/private/tmp/roth-separation-d18-build-final.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 baseline warnings (`...-direct-final-lsp.json`). Explicit original effective type and independent non-self proof compile; actual built target and independent proof use only standard three axioms (`...-direct-independent-retry.log`). All binder, five-search and public literature evidence recorded. A superseded 549-line proof used the public wrapper; owner requested direct mathlib reuse, compiled and applied before fresh final gates. Earlier 13-to-11 line estimate corrected by actual Git arithmetic.

Actual accepted final repository-module profile exits 0 (`/private/tmp/roth-separation-d18-direct-final-profile.log{,.json}`): command 12.344 + async 23.659 = 36.003 ms, baseline 72.019 ms, one anchor each and below 750/1000 ms. Earlier 74.166 ms belongs to the superseded wrapper-dependent candidate and is excluded as final evidence. No profiler scaffolding or raised limits.

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `59024` exit0,45.72s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d18-compatibility.{lean,log,json}`. Owner build session `2299` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.62s/29.26s; source hash stable. `/private/tmp/roth-separation-d18-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

All three public options remain pending and unapplied: 12-theorem instance omissions and the two optional public wrapper deletions. Fresh owner rg confirms coefficient references remain explicitly MvPolynomial-qualified; the unused Roth wrapper gained no caller. Refresh historical deletion candidates before any approved application. Header remains user-preserved.


## d19 completed declaration checkpoint — degreeOf_rename_mul_aeval

[Dedicated audit](Separation-degreeOf_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Proof retained byte-identically after full direct-API/automation audit; no source edit or helper. Stronger generality is compiled as an unapproved grouped public option, not applied. Source unchanged at 551 lines and 23 declarations, all original public types/docs retained. Source 551 → 551; 23 retained declarations. Separation 19/30, overall 170/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d19-build.log`). Complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 warnings (`...-final-lsp.json`). Exact original type and independent non-self proof compile; actual target and independent proof use standard three axioms (`...-independent.{lean,log}`). Every binder probe completed; no-zero-divisors condition tested, hV removal independently refuted by compiled V=0/U=X integer counterexample. Full-module grouped coefficient proposal (`...-domain-proposal.{lean,log}`) exits 0 with both actual printed weaker types and standard axioms: only Domain section CommRing/IsDomain changed to CommSemiring/NoZeroDivisors, Fintype/DecidableEq and both existing proofs retained. Arbitrary-τ combined isolated candidate also passes (`...-weakest.{lean,log}`).

Unchanged actual source/target reuses valid repository-module profile `/private/tmp/roth-separation-d18-direct-final-profile.log{,.json}`: command 13.297 + async 118.049 = 131.346 ms, one anchor each, below 750/1000 ms. No unnecessary repeat profile, source scaffolding, raised limits or target deferral.

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `75014` exit0,34.54s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d19-compatibility.{lean,log,json}`. Owner build session `45446` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.75s/2.65s; source hash stable. `/private/tmp/roth-separation-d19-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Four public options remain pending/unapplied: 12-theorem index-instance omissions, two optional public wrapper deletions, and grouped Domain coefficient weakening for d19+d20 to CommSemiring/NoZeroDivisors. The coefficient option is independently compiled with original variable instances retained. No approval inferred from successful probes. Header remains user-preserved.


## d20 completed declaration checkpoint — degreeOf_none_rename_mul_aeval

[Dedicated audit](Separation-degreeOf_none_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Distinguished-variable product-degree proof retained unchanged after full direct-API, automation and transport review. Original nonzero hU, effective public type and docs preserved; no helper or source edit. Source 551 lines, 23 retained declarations. Source 551 → 551; 23 retained declarations. Separation 20/30, overall 171/264 original audits after successful publication; 8/14 files complete.

Actual module build exit 0 (`/private/tmp/roth-separation-d20-build.log`). Fresh complete unfiltered native LSP success=true, partial=false, timed_out=false, no failed dependencies, 0 errors/31 existing warnings (`...-final-lsp.json`). Exact original type/non-self proof, separate hU=0 counterexample and actual built target/independent standard-axiom checks exit 0 (`...-independent.{lean,log}`). All 15 binder probes completed (`...-probe-results.json`): weaker coefficient and index-instance options compile but remain pending; Ring/dropped coefficient/dropped domain structures fail with actual diagnostics. All requests drained before freeze.

Unchanged actual source/target reuses repository-module profile `/private/tmp/roth-separation-d18-direct-final-profile.log{,.json}`: command 17.385 + async 182.839 = 200.224 ms, anchors 216610/219922, below 750/1000 ms. No unnecessary profile repeat, source scaffolding, raised limits or performance deferral.

Source FROZEN SHA256 `1c58b8b35fe3c01d326d802b94c54dbc8ed0349e1ca388f87e9b34aa2a0278d4`; leaf ownership revoked and requests drained before owner gates. Owner probe `76196` exit0,34.50s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d20-compatibility.{lean,log,json}`. Owner build session `12121` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.58s/2.79s; source hash stable. `/private/tmp/roth-separation-d20-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

All four public options remain pending/unapplied: 12-theorem instance omissions, two public wrapper deletions, and grouped Domain coefficient weakening to CommSemiring/NoZeroDivisors (full-module d19 candidate already compiled). Header remains user-preserved. Original 21 performance/decomposition and fresh audits of any added helpers remain next, with original counts preserved.


## d21 completed declaration checkpoint — exists_separated_representation

[Dedicated audit](Separation-exists_separated_representation.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Decomposed original64-line public proof into30-line proof and two freshly independently audited private helpers. A third newly added helper was independently audited and removed in favor of imported restrictSupport. Original public type/docs retained; no original-count inflation. Source 551 → 573; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Original21 and all three new-helper fresh audits completed full24/42/five-search/binder/width/inequality/11step workflow. Actual module builds, exact-original independent non-self proofs and actual built standard-axiom checks passed. Final fresh helper complete unfiltered LSP0errors/31warnings; owner complete native diagnostics likewise0/31. Final SHA36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17; all leaf ownership revoked and all requests drained.

Actual isolated final owner sweep /private/tmp/roth-separation-d21-owner-profile.log exit0: independence312.549ms, reconstruction718.272ms, public main895.154ms. Same-final-source preceding isolated main repeats844.929/853.337ms meet the >=750 repeat rule; every affected declaration below1000ms. No raised limits, source profiler scaffolding or deferral.

Source FROZEN SHA256 `36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17`; leaf ownership revoked and requests drained before owner gates. Owner probe `88657` exit0,37.80s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d21-compatibility.{lean,log,json}`. Owner build session `56384` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,115.49s/28.60s; source hash stable. `/private/tmp/roth-separation-d21-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

User explicitly approved exact12-theorem instance menu during helper audits. None applied in this frozen batch: nine already-audited targets will receive separate dependency/source-ordered revisit checkpoints next; three upcoming targets at ordinary audit. Optional public-wrapper deletions and Domain coefficient weakening remain unapproved/unapplied; header preserved.


## r01 completed declaration checkpoint — eq_mapDomain_some_add_single

[Dedicated audit](Separation-approved-instances-eq_mapDomain_some_add_single.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT1/9 (original2): removed both Fintypeτ and DecidableEqτ by one scoped omit before preserved docstring. Proof byte-identical, no local classical or caller repair needed; original audit count remains21/30. Source 573 → 574; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh dedicated full24/42/five-search/binder/literature/width/inequality/11step audit. Actual module build93323 exit0; complete unfiltered native LSPsuccess=true partial=false timed_out=false no failed dependencies,0errors28warnings (31→28). Fresh independent exact NEW arbitraryτ proof, original snapshot proof with explicit ORIGINAL class-argument adapter, infinite-index use and actual built target+expansion-caller standard3axiom checks15138 exit0; /private/tmp/roth-separation-r01-verify.{lean,log}. All jobs drained and ALL leaf source ownership revoked; SHAb0d740f0e8638621a0fcbe68ac01235846bdde1ef27fb27b756d310b4af2dd0d.

Actual isolated repository-module profile10704 exit0 /private/tmp/roth-separation-r01-profile.log{,.json}: target21.552+94.276=115.828ms; affected expansion caller23.539+74.836=98.375ms. Both below750/1000ms; no repeat required, limits or scaffolding.

Source FROZEN SHA256 `b0d740f0e8638621a0fcbe68ac01235846bdde1ef27fb27b756d310b4af2dd0d`; leaf ownership revoked and requests drained before owner gates. Owner probe `63261` exit0,48.96s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r01-compatibility.{lean,log,json}`. Owner build session `8377` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.57s/29.09s; source hash stable. `/private/tmp/roth-separation-r01-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-theorem instance menu USER APPROVED; this is first application, remaining targets retain their individual validation/checkpoint sequence. Other public API options remain unapproved/unapplied; no original-count increment. Next coeff_coeffNone approved instance revisit. Header unchanged.


## r02 completed declaration checkpoint — coeff_coeffNone

[Dedicated audit](Separation-approved-instances-coeff_coeffNone.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT2/9 (original7): one scoped omit removes Fintypeτ/DecidableEqτ; proof and original docs unchanged. Original audit count remains21/30. User decisions closing optional wrapper deletions and coefficient-domain widening are recorded as considered/declined. Source 574 → 575; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual module exit0 /private/tmp/roth-separation-r02-module.log. Complete native final-lsp.json0errors27warnings: three target warnings removed, two already-approved future caller unusedSectionVars warnings exposed in eq_sum_X_none_pow_mul_coeffNone and coeff_rename_mul_aeval. Independent exact NEW arbitraryτ type/nonself proof/explicit ORIGINAL class-order adapter and built target+two callers standard3axioms pass; ...-independent.{lean,log}. Fresh10binderprobes ...-probes.json. All requests drained/ALL leaf ownership revoked; SHAe3da33d7e951239837ba563ea0e8d6bb8fa783ef9bf6c0781bdce51588dce029.

Actual isolated /private/tmp/roth-separation-r02-profile.log{,.json} exit0: outeromit7.736ms+async79.367ms=87.103ms, anchors55949/55975. Inner6.833ms command excluded from sum. Below750/1000ms; no resweep, limits or scaffolding.

Source FROZEN SHA256 `e3da33d7e951239837ba563ea0e8d6bb8fa783ef9bf6c0781bdce51588dce029`; leaf ownership revoked and requests drained before owner gates. Owner probe `25584` exit0,42.40s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r02-compatibility.{lean,log,json}`. Owner build session `72584` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.83s/27.79s; source hash stable. `/private/tmp/roth-separation-r02-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

USER DECISION: both optional public-wrapper deletions (aeval_X_eq_rename and Roth.coeff_uniqueAlgEquiv_symm) and two-theorem CommSemiring/NoZeroDivisors widening considered/DECLINED; preserve names and CommRing/IsDomain assumptions. No pending required API decision. Nat codomain unchanged. Exact12instance menu remainsapproved; next expansion bridge revisit.


## r03 completed declaration checkpoint — eq_sum_X_none_pow_mul_coeffNone

[Dedicated audit](Separation-approved-instances-eq_sum_X_none_pow_mul_coeffNone.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT3/9 (original8): removed both Fintypeτ/DecidableEqτ with one scoped omit; existing proof/localclassical/docstring unchanged. Original audit count remains21/30. Source 575 → 576; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual module exit0 ...-r03-module.log; complete native final-lsp.json0errors25warnings0infos. Exact NEW arbitraryτ independent nonself proof, explicit ORIGINAL classadapter and9actual suffixresolved standardaxiom checks exit0 (...-independent.{lean,log},...-actual-axioms.{lean,log});11binderprobes plus corrected dropτ retry. All jobs drained/ALL sourceownership revoked; SHA695da96521c7eb9a07f5f8271868cd37360e9db65a0c5ca0398aa609ee62e507.

Two sequential isolated actual repository sweeps /private/tmp/roth-separation-r03-profile{,-repeat}.log{,.json} exit0: target92.703/96.229ms; directcaller exists_separated_representation847.714/767.519ms; basishelper795.787/709.339ms; exists_det495.352/444.682ms. Required>=750repeat satisfied;25anchored rows each, no>=1000. Repeat raw3invalidUTF8bytes in nestedtrace handled by documented replacement parser without alteringASCIIanchors; no source scaffolding/limits.

Source FROZEN SHA256 `695da96521c7eb9a07f5f8271868cd37360e9db65a0c5ca0398aa609ee62e507`; leaf ownership revoked and requests drained before owner gates. Owner probe `75432` exit0,47.70s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r03-compatibility.{lean,log,json}`. Owner build session `20590` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,122.33s/31.92s; source hash stable. `/private/tmp/roth-separation-r03-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved, three dependency-ordered revisits applied. Optional wrapper deletions and Domain coefficient widening explicitly considered/DECLINED, Natcodomain unchanged. No requireduserinput pending. NextdegreeOf_coeffNone_le approvedrevisit; originalcount unchanged.


## r04 completed declaration checkpoint — degreeOf_coeffNone_le

[Dedicated audit](Separation-approved-instances-degreeOf_coeffNone_le.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT4/9 (original9): removed both index instances with a single scoped omit; proof/docstring unchanged. Original audit count remains21/30. Source 576 → 577; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual module build exit0 ...-r04-build.log; complete native final-lsp.json0errors22warnings (25baseline). Independent exact NEW arbitraryτ type and independent NEW/ORIGINAL supremum proofs, explicit ORIGINAL ft/de/cs adapter and actualtarget/conservative downstream standardaxioms pass (...-independent.{lean,log}). All jobs drained/ALL sourceownership revoked; SHA3c5bbe4d1706e8c7f0c392ceabc1f23565e5e70f295d6dd5f65d5deee3637eac.

Actual isolated repository-module /private/tmp/roth-separation-r04-profile.log{,.json} exit0: targetoutercommand3.629+outerasync29.701=33.330ms. All25retainedrows below750ms; no repeat required and no1000msviolations, profiler scaffolding or limitraise.

Source FROZEN SHA256 `3c5bbe4d1706e8c7f0c392ceabc1f23565e5e70f295d6dd5f65d5deee3637eac`; leaf ownership revoked and requests drained before owner gates. Owner probe `12312` exit0,50.42s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r04-compatibility.{lean,log,json}`. Owner build session `24948` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,118.53s/31.91s; source hash stable. `/private/tmp/roth-separation-r04-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved; four revisits applied. Optional wrapper deletions and Domain coefficient widening considered/DECLINED, Natcodomain unchanged, no requireduserinput pending. Nextcoeff_rename_mul_aeval approvedrevisit.


## r05 completed declaration checkpoint — coeff_rename_mul_aeval

[Dedicated audit](Separation-approved-instances-coeff_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT5/9 (original10): one scoped omit removes both index instances; proof/docs unchanged, no classical/helper/caller repair. Original audit count remains21/30. Source 577 → 578; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/fiveactualsearch/binder/literature/width/inequality/11step audit. Actual Roth.Separation and Roth.Theta builds exit0; complete native Separation0errors20warnings and Theta0errors28warnings (...-final-lsp.json,...-theta-lsp.json). Three targetwarnings removed, one future exists_int_factors unusedSectionVars warning exposed. Exact NEW arbitraryτ assignment/nonself proof/explicit ORIGINAL classadapter and actualtarget/bridges/exists_int_factors/index_det_le standardaxioms pass (...-independent.{lean,log},...-caller-axioms.{lean,log}). Complete external Theta result independently checked by owner; source/contracts untouched. All jobs drained and sourceownership revoked; SHA9893814b3228a24b031753f740a8755c7feabd522791ab5563fe74b09c2e0b01.

Actual isolated /private/tmp/roth-separation-r05-profile.log{,.json} exit0: targetoutercommand31.048+outerasync152.492=183.540ms, two command/oneproof anchors with nested command excluded. Below750/1000ms; no resweep, raisedlimits or scaffolding.

Source FROZEN SHA256 `9893814b3228a24b031753f740a8755c7feabd522791ab5563fe74b09c2e0b01`; leaf ownership revoked and requests drained before owner gates. Owner probe `60429` exit0,42.21s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r05-compatibility.{lean,log,json}`. Owner build session `21232` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,79.22s/28.12s; source hash stable. `/private/tmp/roth-separation-r05-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved; five dependency/source-ordered revisits applied. Optional wrapper deletions and Domain coefficient widening considered/DECLINED; Natcodomain unchanged; no requiredinputpending. NexthasseDeriv_rename_mul_aeval approvedrevisit.


## r06 completed declaration checkpoint — hasseDeriv_rename_mul_aeval

[Dedicated audit](Separation-approved-instances-hasseDeriv_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; APPROVED INSTANCE REVISIT6/9 (original16): removed both ambient index instances with scoped omit and minimal local classical; mathematical proof and original docs otherwise unchanged. Original audit count remains21/30. Source 578 → 580; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full audit covers all 24 audit items, 42 golf rules, five actual searches, effective binders, literature, width/inequality checks and 11 completion steps. Actual module build exits 0; complete native LSP reports 0 errors/18 warnings (20 baseline): three target warnings removed and one upcoming determinant caller unusedSectionVars warning exposed; its contract stays unchanged. Exact NEW arbitrary-τ proof and explicit ORIGINAL class adapters pass native/compiler; the initial scratch universe mismatch is excluded and its corrected result retained. Actual target and determinant caller axioms are exactly the standard three. Fifteen corrected binder probes have actual results. Evidence: /private/tmp/roth-separation-r06-{independent.lean,independent.log,native-independent-fixed.json,probes.json}. All requests drained and ALL leaf source ownership revoked; SHA187f69cba6b1e16d665130375348c4038f3aa5cd7a3cb8d650e3e055b2a5bf7d.

Actual isolated repository-module /private/tmp/roth-separation-r06-profile.log{,.json} exit0: target40.276+341.592=381.868ms; direct determinant caller84.137+405.262=489.399ms. Both below750/1000ms; no repeat required, limits or source scaffolding.

Source FROZEN SHA256 `187f69cba6b1e16d665130375348c4038f3aa5cd7a3cb8d650e3e055b2a5bf7d`; leaf ownership revoked and requests drained before owner gates. Owner probe `98402` exit0,43.30s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r06-compatibility.{lean,log,json}`. Owner build session `84517` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.76s/28.80s; source hash stable. `/private/tmp/roth-separation-r06-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12instance menu approved; six revisits applied. Optional wrapper deletions and Domain coefficient widening considered/DECLINED; Nat codomain unchanged; no required user input pending. Next degreeOf_rename_mul_aeval approved revisit; preserve current coefficient assumptions.


## r07 completed declaration checkpoint — degreeOf_rename_mul_aeval

[Dedicated audit](Separation-approved-instances-degreeOf_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Approved instance revisit 7/9 (original19): scoped omit and local classical remove both ambient index instances. Current CommRing/IsDomain assumptions, nonzero hypothesis, proof and original docs otherwise preserved. Original audit count remains21/30. Source 580 → 582; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh audit covers all24 items,42 golf rules,five actual searches,every effective binder,literature,width/inequalities and11 steps. Actual module build exits0; complete native LSP0errors/15warnings/0infos, partial=false/timed_out=false and no failed dependencies. Exact NEW arbitrary-τ @type/nonself proof, explicit ORIGINAL Fintype/DecEq adapter and built target/exists_det_eq_mul standard-three axioms pass (...-independent.lean/.log). All16 compiler probes drained; counterexample confirms hV cannot be dropped. No external direct caller or helper. ALL source ownership revoked and requests drained; SHA700e71b2e6acaec6767a0bd483fd17ee0e029340a4b3e745831542b8cc720ab5.

Actual isolated /private/tmp/roth-separation-r07-profile.log{,.json} exit0: outer omit command17.912ms at200422 + outer async110.900ms at200459 =128.812ms. Inner16.381ms command excluded. Below750/1000ms; no repeat, raised limits or scaffolding.

Source FROZEN SHA256 `700e71b2e6acaec6767a0bd483fd17ee0e029340a4b3e745831542b8cc720ab5`; leaf ownership revoked and requests drained before owner gates. Owner probe `55892` exit0,42.65s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r07-compatibility.{lean,log,json}`. Owner build session `59964` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.36s/27.69s; source hash stable. `/private/tmp/roth-separation-r07-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-instance menu approved; seven revisits applied. Both wrapper deletions and coefficient-domain widening considered/declined, Nat codomain unchanged; no required input pending. Next degreeOf_none_rename_mul_aeval approved revisit.


## r08 completed declaration checkpoint — degreeOf_none_rename_mul_aeval

[Dedicated audit](Separation-approved-instances-degreeOf_none_rename_mul_aeval.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Approved instance revisit 8/9 (original20): scoped omit plus local classical remove both ambient index instances. All other source bytes, coefficient assumptions and docs preserved. Original audit count stays21/30. Source 582 → 584; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/five-search/binder/literature/width/inequality/11-step audit. Actual module build exits0; complete native LSP0errors/12warnings/0infos, no partial/timeout/failed dependencies. Exact NEW arbitrary-τ type/nonself proof, explicit full ORIGINAL binder-order forall adapter, independent ORIGINAL proof, hU counterexample and actual target/exists_det_eq_mul standard axioms pass. Evidence ...-r08-{contract.lean,contract-final.log,probe-results.json}. All requests drained; ALL source ownership revoked; SHA49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74.

Two isolated actual repository sweeps exit0: /private/tmp/roth-separation-r08-profile{,-final}.log{,.json}. Target194.041→166.317ms (final23.747+142.570; anchors225752/225790); caller488.675ms final. Reconstruction770.520→699.921ms, main824.040→814.956ms; both repeated below1000. Untouched upcoming exists_int_factors679.320→754.519ms remains for ordinary29/final-file sweep. All25 command and24 theorem-proof anchors present. First raw trace has3 malformed nested UTF8 bytes handled by documented replacement-only parser; final raw is validUTF8 and supplied strict parser passes. No limit raise/scaffolding.

Source FROZEN SHA256 `49790c37e35777ce2c4668975e173e5e7c7ae5af353ba151d800df0472892f74`; leaf ownership revoked and requests drained before owner gates. Owner probe `60715` exit0,39.76s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r08-compatibility.{lean,log,json}`. Owner build session `5802` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,118.81s/28.04s; source hash stable. `/private/tmp/roth-separation-r08-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Exact12-instance menu approved; eight revisits applied. Both public-wrapper deletions and coefficient-domain widening considered/declined; Nat codomain unchanged. No required input pending. Next final approved revisit exists_separated_representation, then ordinary original22.


## r09 completed declaration checkpoint — exists_separated_representation

[Dedicated audit](Separation-approved-instances-exists_separated_representation.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Approved instance revisit9/9 (original21): only one scoped omit line; proof and both previously independently audited helpers unchanged. Original audit count remains21/30. Explicit structure flag retained for the30-line named headline theorem; a dedicated private refactor/fresh helper audit will close the15-line target before final file completion. Source 584 → 585; 25 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Fresh full24/42/five actual searches/every binder/literature/width/inequality/11-step audit. Module build exits0; complete unfiltered native LSP0errors/9warnings/0infos with no partial/timeout/failed dependencies. Independent arbitrary-τ proof with copied audited helpers, original64-line proof, full ORIGINAL binder-order adapter and actual target/twohelpers/exists_det_eq_mul standard axioms pass (...-r09-contract-final.log,...-original-independent.log). All13 binder probes and valid explicit IsField equivalent pass/fail as documented; no external direct caller. All requests drained and ALL source ownership revoked; SHAd30464cac2d8d49bcaeb4f7edc0d35469af4c36189acbe93edf4a7ea0f1b1b91.

Two sequential isolated actual repository sweeps /private/tmp/roth-separation-r09-profile{,-repeat}.log{,.json} exit0, validUTF8 with all25 anchored declarations, none>=1000. Main29.717+762.489=792.206ms then30.633+738.006=768.639ms (repeat anchors413876/413965). Coordinatehelper270.805/274.433; reconstruction699.461/686.714; actualcaller473.548/506.194. >=750 repeat satisfied; no raised limits or scaffolding.

Source FROZEN SHA256 `d30464cac2d8d49bcaeb4f7edc0d35469af4c36189acbe93edf4a7ea0f1b1b91`; leaf ownership revoked and requests drained before owner gates. Owner probe `56755` exit0,39.91s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r09-compatibility.{lean,log,json}`. Owner build session `81056` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,119.01s/32.93s; source hash stable. `/private/tmp/roth-separation-r09-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

All nine already-audited approved instance revisits now applied. Remaining approved targets are ordinary22det_hasseDeriv_separated and29exists_int_factors (both instances),30exists_det_eq_mul (DecEq only, retainFintype). Dedicated private headline-proof decomposition will close the explicit structure flag; all added helpers require fresh audits and all affected gates before publication. Both wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged, no required user input.


## s21 completed declaration checkpoint — exists_separated_representation

[Dedicated audit](Separation-structure-exists_separated_representation.md): All 24 audit items, 42 golf rules, five actual search methods, every binder, width/inequality checks and 11 completion steps; Private structure completion for original21: main30→14 bodylines, new exists_coeffNone_basis_aux21 bodylines; public type/docs and existing helpers unchanged, shared expansion reused. New helper receives full fresh independent audit and is retained unchanged. Headline15-line flag closed; correlated existential conjunction splitting is mathematically inapplicable, not pending. Original audit count remains21/30. Source 585 → 597; 26 retained declarations. Separation 21/30, overall 172/264 original audits after successful publication; 8/14 files complete.

Dedicated structure and fresh independent helper audits complete all24/42/five searches/binders/width/inequality/11steps, with public literature/private exemption respectively. Actual module builds, exact current public arbitrary-τ nonself proof, original helper type+independent proof, actual helper/existinghelpers/main/caller standard axioms pass. Complete fresh unfiltered native LSP0errors9preservedwarnings. Evidence /private/tmp/roth-separation-s21-{build.log,independent.log,axioms.log}, /private/tmp/roth-s21-helper-{module-build.log,type-axioms.log,native-final.json}. All requests drained; ALL leaf source ownership revoked; SHAdc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e.

Actual final isolated /private/tmp/roth-separation-s21-final-profile.log{,.json} exit0: newhelper55.134+591.316=646.450ms; main58.943+292.125=351.068ms; caller97.288+385.275=482.563ms. All affected below750/1000; unchanged fresh audit validly reuses this exact-source baseline. Earlier preliminary import-overlap profile excluded. No limits/scaffolding/deferral.

Source FROZEN SHA256 `dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`; leaf ownership revoked and requests drained before owner gates. Owner probe `99185` exit0,53.66s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-s21-compatibility.{lean,log,json}`. Owner build session `68108` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.18s/31.57s; source hash stable. `/private/tmp/roth-separation-s21-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.

Structure flag closed and all four historical added helpers independently audited (three retained, degree helper removed). Exact12-instance menu: nine revisits complete; upcoming ordinary22/29 remove both,30removeDecEq only retainFintype. Wrapper deletions and Domain coefficient widening considered/declined; Nat codomain unchanged. No required input pending. Next ordinary original22 with headline<=15 target.
