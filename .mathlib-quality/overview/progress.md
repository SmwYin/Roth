# Completed-only overview progress

Status: **in_progress**, 2026-10-26. Branch: `ramin-cleanup`.
Production Lean files and all pins match baseline `99f19fd`.

**Completed: 44 / 293 written declarations.**
This counts the current overview assessments, separately from the earlier code cleanup.

| # | Completed declaration | Applicable workflow | Verdict | Report |
|---|---|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.hasseCoeff.md) |
| 2 | `MvPolynomial.hasseDeriv` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv.md) |
| 3 | `MvPolynomial.hasseDeriv_monomial` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_monomial.md) |
| 4 | `MvPolynomial.hasseDeriv_apply` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_apply.md) |
| 5 | `MvPolynomial.hasseCoeff_eq_zero_iff` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md) |
| 6 | `MvPolynomial.coeff_hasseDeriv` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.coeff_hasseDeriv.md) |
| 7 | `MvPolynomial.hasseCoeff_eq_prod` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.hasseCoeff_eq_prod.md) |
| 8 | `MvPolynomial.hasseDeriv_zero_apply` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_zero_apply.md) |
| 9 | `MvPolynomial.hasseDeriv_zero` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_zero.md) |
| 10 | `MvPolynomial.hasseDeriv_C` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_C.md) |
| 11 | `MvPolynomial.hasseDeriv_map` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_map.md) |
| 12 | `MvPolynomial.hasseDeriv_rename` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_rename.md) |
| 13 | `MvPolynomial.hasseCoeff_mul_hasseCoeff` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.hasseCoeff_mul_hasseCoeff.md) |
| 14 | `MvPolynomial.hasseDeriv_hasseDeriv` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_hasseDeriv.md) |
| 15 | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint.md) |
| 16 | `MvPolynomial.hasseCoeff_mul_succ` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.hasseCoeff_mul_succ.md) |
| 17 | `MvPolynomial.pderiv_hasseDeriv` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.pderiv_hasseDeriv.md) |
| 18 | `MvPolynomial.degreeOf_hasseDeriv_le` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.degreeOf_hasseDeriv_le.md) |
| 19 | `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md) |
| 20 | `MvPolynomial.hasseDeriv_monomial_mul` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_monomial_mul.md) |
| 21 | `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero.md) |
| 22 | `MvPolynomial.hasseDeriv_single_aeval_X` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_single_aeval_X.md) |
| 23 | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.uniqueAlgEquiv_hasseDeriv.md) |
| 24 | `MvPolynomial.hasseCoeff_le_two_pow` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.hasseCoeff_le_two_pow.md) |
| 25 | `MvPolynomial.factorial_smul_hasseDeriv_single` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.factorial_smul_hasseDeriv_single.md) |
| 26 | `Roth.box` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.box.md) |
| 27 | `Roth.weight` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.weight.md) |
| 28 | `Roth.mem_box` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.mem_box.md) |
| 29 | `Roth.card_box` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.card_box.md) |
| 30 | `Roth.card_le_card_box` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.card_le_card_box.md) |
| 31 | `Roth.weight_nonneg` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.weight_nonneg.md) |
| 32 | `Roth.weight_zero` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.weight_zero.md) |
| 33 | `Roth.weight_add` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.weight_add.md) |
| 34 | `Roth.weight_eq_zero_iff` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.weight_eq_zero_iff.md) |
| 35 | `Roth.weight_single` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.weight_single.md) |
| 36 | `Roth.weight_le_card` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.weight_le_card.md) |
| 37 | `Roth.weight_mul_left` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.weight_mul_left.md) |
| 38 | `Roth.weight_le_degree_div` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.weight_le_degree_div.md) |
| 39 | `Roth.weight_mapDomain` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.weight_mapDomain.md) |
| 40 | `Roth.wronskianMatrix` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.wronskianMatrix.md) |
| 41 | `Roth.wronskian` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.wronskian.md) |
| 42 | `Roth.wronskian_eq_zero_of_not_linearIndependent` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.wronskian_eq_zero_of_not_linearIndependent.md) |
| 43 | `Roth.det_choose_eq` | full-mathlibable; accepted complete | YES-but-generalise-first | [Detailed report](mathlibable/Roth.det_choose_eq.md) |
| 44 | `Roth.coeff_prod_of_natDegree_le'` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/Roth.coeff_prod_of_natDegree_le'.md) |

**Next declaration: `Roth.sum_range_le_sum_of_injective`**, `Roth/Wronskian.lean:107`.
Only the listed assessments are complete. No partial assessment was committed.

On restart: read [README](README.md), [machine progress](progress.json), and
[declaration order](declaration-order.json); verify source/pin hashes and accepted evidence,
then continue with the first unfinished declaration. Reports and evidence are tracked.
