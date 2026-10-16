# GenWronskian initial file audit

## Phase 0 — baseline

Baseline commit `21318b11fc132a3a2b800e55e22db5a48092492d`, branch `ramin-cleanup`; clean working tree. Full `lake build` session95276 exit0, log `/private/tmp/roth-genwronskian-baseline-full.log`. Complete LSP session41268:success=true,partial=false,timed_out=false,zero errors/no failed imports; artifact `/private/tmp/roth-genwronskian-baseline-lsp.json`. Cache skipped: populated. Standalone runLinter unavailable; mathlibStandardSet enabled during build. Missing authoritative header metadata remains user-preserved.

## Phase 1 — preparation

Classic dialect,292 lines,19 original declarations (13 public,6 private). Entire file, both installed skills, cleanup/cleanup-all workflows and relevant reference catalogues read. Temporary original source `/private/tmp/roth-genwronskian-baseline.lean`. Generalized determinant and Kronecker substitution implement source clean.tex §2 Lemma1; final two results are headline theorem families. Existing docs/comments protected by authorization.

| # | Declaration | Original line | Original declaration lines |
|---|---|---:|---:|
| 1 | `genWronskian` | 27 | 3 |
| 2 | `genWronskian_eq_zero_of_not_linearIndependent` | 35 | 10 |
| 3 | `kronecker` | 48 | 2 |
| 4 | `kroneckerExp` | 52 | 1 |
| 5 | `kronecker_monomial` | 55 | 6 |
| 6 | `digits_unique` | 62 | 5 |
| 7 | `kroneckerExp_injOn` | 72 | 11 |
| 8 | `coeff_kronecker` | 88 | 14 |
| 9 | `kronecker_eq_zero_iff` | 107 | 8 |
| 10 | `linearIndependent_kronecker` | 120 | 13 |
| 11 | `derivative_aeval` | 138 | 14 |
| 12 | `kronHasse` | 154 | 2 |
| 13 | `kronSpan` | 158 | 3 |
| 14 | `kronSpan_mono` | 162 | 3 |
| 15 | `derivative_mem_kronSpan` | 166 | 35 |
| 16 | `hasseDeriv_kronecker_mem` | 202 | 20 |
| 17 | `exists_hasseDeriv_kronecker_eq_sum` | 230 | 10 |
| 18 | `det_sum_rows` | 246 | 12 |
| 19 | `exists_genWronskian_ne_zero` | 265 | 26 |

## Phase 2 — punch-list before fixes

A.1 Header metadata missing: explicitly leave unchanged, no invented attribution or linter suppression.
A.2 Module docstring present directly after imports, source reference present; preserve.
A.3 Five imports alphabetized within groups; missing group separator will add one blank line. Redundancy testing reserved for final review.
A.4 No section headers/contentless blocks.
A.5 292 lines, below file limit.
A.6 No options/debug/heartbeat overrides.
A.7 No λ/$/push_neg. Ordinary lambda arrows require per-declaration normalization; match arrows retained.

B.1 L1 missing metadata warning, user-preserved.
B.2 L35 unused Fintype section parameter in genWronskian_eq_zero_of_not_linearIndependent.
B.3 L31 unused Fintype in same theorem type.
B.4 L241 unused public DecidableEq parameter in det_sum_rows.
B.5 L259 unused public Fintype parameter in exists_genWronskian_ne_zero.
All public changes require a compiled reviewable proposal before application; independent proof cleanup continues.

C.1–C.19: declaration names describe mathematical content, no forbidden numeric patterns/abbreviations. Definitions lowerCamelCase; theorem names include existing subject identifiers. Six private implementation declarations remain private; public API protected. All public declarations already documented. Two private definitions have docstrings protected by prior preservation instruction. Generic direct constructions must satisfy keep/API test individually. derivative_mem_kronSpan has34 proof lines and a >10-line branch: golf/extract or explicit decomposition action required. exists_genWronskian_ne_zero has conjunction in existential statement and >15-line body: preserve public statement, attempt proof decomposition. Each declaration requires fresh dedicated24-item/42-rule/5-search/generalization/literature/signature/inequality audit and11-step report.

## Phase 3 — file-level fixes

Added one blank line between Mathlib/project import groups. All other file-level items either already satisfy rules or remain explicitly user-preserved. No metadata/options/docstring changes.
