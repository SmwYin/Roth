# Completed-only overview progress

Status: **in_progress**, 2026-10-27. Branch: `ramin-cleanup`.
Production Lean files and all pins match baseline `99f19fd`.

**Completed: 85 / 293 written declarations.**
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
| 45 | `Roth.sum_range_le_sum_of_injective` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.sum_range_le_sum_of_injective.md) |
| 46 | `Roth.coeff_wronskian_of_natDegree_injective` | full-mathlibable; accepted complete | YES-but-generalise-first | [Detailed report](mathlibable/Roth.coeff_wronskian_of_natDegree_injective.md) |
| 47 | `Roth.wronskian_ne_zero_of_natDegree_injective` | full-mathlibable; accepted complete | YES-but-generalise-first | [Detailed report](mathlibable/Roth.wronskian_ne_zero_of_natDegree_injective.md) |
| 48 | `Roth.wronskian_update_sub_smul` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.wronskian_update_sub_smul.md) |
| 49 | `Roth.linearIndependent_update_sub_smul` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.linearIndependent_update_sub_smul.md) |
| 50 | `Roth.sum_natDegree_update_lt` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.sum_natDegree_update_lt.md) |
| 51 | `Roth.wronskian_ne_zero_of_linearIndependent` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.wronskian_ne_zero_of_linearIndependent.md) |
| 52 | `Roth.wronskian_eq_zero_iff` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.wronskian_eq_zero_iff.md) |
| 53 | `MvPolynomial.taylor` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.taylor.md) |
| 54 | `MvPolynomial.taylor_apply` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.taylor_apply.md) |
| 55 | `MvPolynomial.taylor_X` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/MvPolynomial.taylor_X.md) |
| 56 | `MvPolynomial.taylor_C` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/MvPolynomial.taylor_C.md) |
| 57 | `MvPolynomial.taylor_monomial` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/MvPolynomial.taylor_monomial.md) |
| 58 | `MvPolynomial.coeff_aeval_X_mul` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.coeff_aeval_X_mul.md) |
| 59 | `MvPolynomial.hasseCoeff_single_add_eq` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.hasseCoeff_single_add_eq.md) |
| 60 | `MvPolynomial.prod_pow_single_add_tsub` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.prod_pow_single_add_tsub.md) |
| 61 | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.coeff_taylor_monomial_single_add_aux.md) |
| 62 | `MvPolynomial.coeff_taylor_monomial_aux` | overview-private-prefilter; accepted complete | SKIP | [Detailed report](mathlibable/MvPolynomial.coeff_taylor_monomial_aux.md) |
| 63 | `MvPolynomial.coeff_taylor` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.coeff_taylor.md) |
| 64 | `MvPolynomial.eval_taylor` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.eval_taylor.md) |
| 65 | `MvPolynomial.taylor_taylor` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.taylor_taylor.md) |
| 66 | `MvPolynomial.taylor_zero` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.taylor_zero.md) |
| 67 | `MvPolynomial.taylor_map` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.taylor_map.md) |
| 68 | `MvPolynomial.taylor_rename` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.taylor_rename.md) |
| 69 | `MvPolynomial.degreeOf_taylor_le` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.degreeOf_taylor_le.md) |
| 70 | `MvPolynomial.taylor_neg_taylor` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.taylor_neg_taylor.md) |
| 71 | `MvPolynomial.taylor_injective` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/MvPolynomial.taylor_injective.md) |
| 72 | `MvPolynomial.taylor_eq_zero_iff` | full-mathlibable; accepted complete | YES-but-generalise-first | [Detailed report](mathlibable/MvPolynomial.taylor_eq_zero_iff.md) |
| 73 | `MvPolynomial.eq_sum_box_hasseDeriv` | full-mathlibable; accepted complete | YES-but-generalise-first | [Detailed report](mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md) |
| 74 | `MvPolynomial.eval_eq_sum_box` | full-mathlibable; accepted complete | YES-but-generalise-first | [Detailed report](mathlibable/MvPolynomial.eval_eq_sum_box.md) |
| 75 | `Roth.normOne` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.normOne.md) |
| 76 | `Roth.diag` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.diag.md) |
| 77 | `Roth.normOne_nonneg` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.normOne_nonneg.md) |
| 78 | `Roth.normOne_eq_sum_of_support_subset` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.normOne_eq_sum_of_support_subset.md) |
| 79 | `Roth.normOne_monomial` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.normOne_monomial.md) |
| 80 | `Roth.normOne_zero` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.normOne_zero.md) |
| 81 | `Roth.abs_coeff_le_normOne` | full-mathlibable; accepted complete | NO-mathlib-has-it | [Detailed report](mathlibable/Roth.abs_coeff_le_normOne.md) |
| 82 | `Roth.normOne_add_le` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.normOne_add_le.md) |
| 83 | `Roth.normOne_neg` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/Roth.normOne_neg.md) |
| 84 | `Roth.normOne_sum_le` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.normOne_sum_le.md) |
| 85 | `Roth.normOne_mul_le` | full-mathlibable; accepted complete | BORDERLINE-needs-human | [Detailed report](mathlibable/Roth.normOne_mul_le.md) |

**Next declaration: `Roth.normOne_prod_le`**, `Roth/CoeffNorm.lean:105`.
Only the listed assessments are complete. No partial assessment was committed.

On restart: read [README](README.md), [machine progress](progress.json), and
[declaration order](declaration-order.json); verify source/pin hashes and accepted evidence,
then continue with the first unfinished declaration. Reports and evidence are tracked.
