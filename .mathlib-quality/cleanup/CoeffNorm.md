# CoeffNorm initial file audit

Source baseline `e63b156a9d2faabc1bf569f0e86eb8fe82569b96`, 320 lines, 26 originals (25 public, 1 private). Both skills and complete cleanup/cleanup-all workflow read. Classic dialect.

## Baseline (Phase 0)

[1] cache: skipped (built dependencies warm).
[2] `/Users/ramin/.elan/bin/lake build` session14707 exit0,2587jobs; log `/private/tmp/roth-coeffnorm-baseline.log`.
[3] Native complete diagnostics responsive, success=true,partial=false,timed_out=false,no failed dependencies or errors.
[4] No standalone runLinter configured; standard mathlib linters run in normal compilation.

## Phase 2 audit punch-list

A.1 COPYRIGHT: missing authoritative metadata; explicit user decision preserve unchanged; no suppression or invented holder/license.
A.2 MODULE DOCSTRING: present immediately after imports, references and main API listed; preserved.
A.3 IMPORTS: reorder Mathlib alphabetically first, then project alphabetically, blank line between.
A.4 SECTION HEADERS: no contentless headers; module headings have content and preserved.
A.5 FILE LENGTH:320lines, below split threshold.
A.6 SET_OPTION: none.
A.7 MECHANICAL: no λ, dollar, push_neg; ordinary lambda ASCII arrows deferred to each declaration.

B.1 Header warning L1:2, user preserved.
B.2 unusedDecidableInType normOne_mul_le at L91.
B.3 unusedDecidableInType normOne_prod_le at L106.
B.4 unusedDecidableInType normOne_det_le at L124.
B.5 unusedVariables hC normOne_det_le at L127:14.
B.6 unusedDecidableInType abs_coeff_det_hasseDeriv_le at L296.
Warnings refer to docstring locations as returned by LSP. Instance removals and hC affect public signatures: compile evidence and seek scoped approval before application. No approval inferred from earlier Box/Wronskian decisions.

Per-declaration light scan:

| # | Declaration | Original lines | Lines | Scan |
|---:|---|---|---:|---|
| 1 | `normOne` | 41–41 | 1 | naming descriptive; docs public present; existing signature/API preserved |
| 2 | `normOne_nonneg` | 44–45 | 2 | naming descriptive; docs public present; existing signature/API preserved |
| 3 | `normOne_eq_sum_of_support_subset` | 48–50 | 3 | naming descriptive; docs public present; existing signature/API preserved |
| 4 | `normOne_monomial` | 53–56 | 4 | naming descriptive; docs public present; existing signature/API preserved |
| 5 | `normOne_zero` | 60–61 | 2 | naming descriptive; docs public present; existing signature/API preserved |
| 6 | `abs_coeff_le_normOne` | 65–70 | 6 | naming descriptive; docs public present; existing signature/API preserved |
| 7 | `normOne_add_le` | 74–80 | 7 | naming descriptive; docs public present; existing signature/API preserved |
| 8 | `normOne_neg` | 83–84 | 2 | naming descriptive; docs public present; existing signature/API preserved |
| 9 | `normOne_sum_le` | 87–89 | 3 | naming descriptive; docs public present; existing signature/API preserved |
| 10 | `normOne_mul_le` | 93–104 | 12 | naming descriptive; docs public present; existing signature/API preserved |
| 11 | `normOne_prod_le` | 107–114 | 8 | naming descriptive; docs public present; existing signature/API preserved |
| 12 | `normOne_le_card_mul` | 119–122 | 4 | naming descriptive; docs public present; existing signature/API preserved |
| 13 | `normOne_det_le` | 126–136 | 11 | naming descriptive; docs public present; existing signature/API preserved |
| 14 | `abs_coeff_hasseDeriv_le` | 142–153 | 12 | naming descriptive; docs public present; existing signature/API preserved |
| 15 | `normOne_hasseDeriv_le` | 158–180 | 23 | naming descriptive; docs public present; existing signature/API preserved |
| 16 | `diag` | 184–184 | 1 | naming descriptive; docs public present; existing signature/API preserved |
| 17 | `diag_eq_sum` | 187–193 | 7 | naming descriptive; docs public present; existing signature/API preserved |
| 18 | `abs_coeff_diag_le` | 199–206 | 8 | naming descriptive; docs public present; existing signature/API preserved |
| 19 | `natDegree_diag_le` | 210–216 | 7 | naming descriptive; docs public present; existing signature/API preserved |
| 20 | `eval_diag` | 220–223 | 4 | naming descriptive; docs public present; existing signature/API preserved |
| 21 | `diag_sub` | 226–227 | 2 | naming descriptive; docs public present; existing signature/API preserved |
| 22 | `geom_sum_le_one_add_pow` | 232–238 | 7 | naming descriptive; docs public present; existing signature/API preserved |
| 23 | `sum_box_prod_pow` | 240–243 | 4 | naming descriptive; docs private none; existing signature/API preserved |
| 24 | `abs_eval_le` | 248–275 | 28 | naming descriptive; docs public present; existing signature/API preserved |
| 25 | `degreeOf_det_hasseDeriv_le` | 281–294 | 14 | naming descriptive; docs public present; existing signature/API preserved |
| 26 | `abs_coeff_det_hasseDeriv_le` | 299–318 | 20 | naming descriptive; docs public present; existing signature/API preserved |

No forbidden abbreviation/scheme-number names or reversed inequalities. normOne and diag have substantial APIs and external callers; no junk data definition. sum_box_prod_pow is private, no docstring, mathematical helper name. Main-results normOne_hasseDeriv_le,abs_eval_le,abs_coeff_det_hasseDeriv_le exceed15bodylines initially; dedicated workers must attempt golf/extraction. abs_eval_le has31bodylines and requires structure work; no conjunction result or private trivial existence lemma. All public docstrings preserved under Lean skill RuleA/user API policy. Public visibility preserved; no speculative export removal.

## Phase 3 file-level fixes

Reordered four imports by approved file-level style action. No metadata/docs/options/mechanical batch change. Complete diagnostics/module verification proceeds with declaration1 checkpoint; no future declaration edits included.
