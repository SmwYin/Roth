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
