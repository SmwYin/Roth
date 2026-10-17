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
