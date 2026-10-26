# /overview progress record

Run: `mathlib-quality:overview` on the whole repository, including Step 9 (full
`/mathlibable` per non-skipped public declaration).  Branch `ramin-cleanup-2`.
Production Lean sources are not modified; experiments live under
`.mathlib-quality/overview/evidence/`.

Restart protocol: read this file, then continue with **Next declaration**.  A
declaration is complete only when its report passes
`python3 .mathlib-quality/overview/scripts/assemble.py check <Decl>`.

Last regenerated: 2026-10-26

- Declarations completed: **84/293**
- Next declaration: **#85 `Roth.normOne_prod_le`** (Roth/CoeffNorm.lean:105)
- Project-wide synthesis (Steps 3–8 cross-declaration analyses): pending (runs after the last declaration)

## Completed declarations

| # | Declaration | File:line | Verdict | Report |
|---|---|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | Roth/HasseDeriv.lean:50 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseCoeff.md) |
| 2 | `MvPolynomial.hasseDeriv` | Roth/HasseDeriv.lean:57 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv.md) |
| 3 | `MvPolynomial.hasseDeriv_monomial` | Roth/HasseDeriv.lean:66 | INHERITED-YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_monomial.md) |
| 4 | `MvPolynomial.hasseDeriv_apply` | Roth/HasseDeriv.lean:73 | INHERITED-YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_apply.md) |
| 5 | `MvPolynomial.hasseCoeff_eq_zero_iff` | Roth/HasseDeriv.lean:80 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md) |
| 6 | `MvPolynomial.coeff_hasseDeriv` | Roth/HasseDeriv.lean:89 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.coeff_hasseDeriv.md) |
| 7 | `MvPolynomial.hasseCoeff_eq_prod` | Roth/HasseDeriv.lean:106 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseCoeff_eq_prod.md) |
| 8 | `MvPolynomial.hasseDeriv_zero_apply` | Roth/HasseDeriv.lean:112 | YES-add-as-is | [report](mathlibable/MvPolynomial.hasseDeriv_zero_apply.md) |
| 9 | `MvPolynomial.hasseDeriv_zero` | Roth/HasseDeriv.lean:120 | INHERITED-YES-add-as-is | [report](mathlibable/MvPolynomial.hasseDeriv_zero.md) |
| 10 | `MvPolynomial.hasseDeriv_C` | Roth/HasseDeriv.lean:126 | YES-add-as-is | [report](mathlibable/MvPolynomial.hasseDeriv_C.md) |
| 11 | `MvPolynomial.hasseDeriv_map` | Roth/HasseDeriv.lean:134 | YES-add-as-is | [report](mathlibable/MvPolynomial.hasseDeriv_map.md) |
| 12 | `MvPolynomial.hasseDeriv_rename` | Roth/HasseDeriv.lean:143 | YES-add-as-is | [report](mathlibable/MvPolynomial.hasseDeriv_rename.md) |
| 13 | `MvPolynomial.hasseCoeff_mul_hasseCoeff` | Roth/HasseDeriv.lean:153 | SKIP | [report](mathlibable/MvPolynomial.hasseCoeff_mul_hasseCoeff.md) |
| 14 | `MvPolynomial.hasseDeriv_hasseDeriv` | Roth/HasseDeriv.lean:175 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_hasseDeriv.md) |
| 15 | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | Roth/HasseDeriv.lean:185 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint.md) |
| 16 | `MvPolynomial.hasseCoeff_mul_succ` | Roth/HasseDeriv.lean:191 | SKIP | [report](mathlibable/MvPolynomial.hasseCoeff_mul_succ.md) |
| 17 | `MvPolynomial.pderiv_hasseDeriv` | Roth/HasseDeriv.lean:200 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.pderiv_hasseDeriv.md) |
| 18 | `MvPolynomial.degreeOf_hasseDeriv_le` | Roth/HasseDeriv.lean:210 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.degreeOf_hasseDeriv_le.md) |
| 19 | `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | Roth/HasseDeriv.lean:219 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md) |
| 20 | `MvPolynomial.hasseDeriv_monomial_mul` | Roth/HasseDeriv.lean:225 | SKIP | [report](mathlibable/MvPolynomial.hasseDeriv_monomial_mul.md) |
| 21 | `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | Roth/HasseDeriv.lean:243 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero.md) |
| 22 | `MvPolynomial.hasseDeriv_single_aeval_X` | Roth/HasseDeriv.lean:253 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseDeriv_single_aeval_X.md) |
| 23 | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | Roth/HasseDeriv.lean:266 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.uniqueAlgEquiv_hasseDeriv.md) |
| 24 | `MvPolynomial.hasseCoeff_le_two_pow` | Roth/HasseDeriv.lean:276 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.hasseCoeff_le_two_pow.md) |
| 25 | `MvPolynomial.factorial_smul_hasseDeriv_single` | Roth/HasseDeriv.lean:286 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.factorial_smul_hasseDeriv_single.md) |
| 26 | `Roth.box` | Roth/Box.lean:47 | NO-mathlib-has-it | [report](mathlibable/Roth.box.md) |
| 27 | `Roth.mem_box` | Roth/Box.lean:51 | NO-mathlib-has-it | [report](mathlibable/Roth.mem_box.md) |
| 28 | `Roth.card_box` | Roth/Box.lean:57 | NO-composable-from-mathlib | [report](mathlibable/Roth.card_box.md) |
| 29 | `Roth.card_le_card_box` | Roth/Box.lean:65 | NO-composable-from-mathlib | [report](mathlibable/Roth.card_le_card_box.md) |
| 30 | `Roth.weight` | Roth/Box.lean:71 | NO-mathlib-has-it | [report](mathlibable/Roth.weight.md) |
| 31 | `Roth.weight_nonneg` | Roth/Box.lean:75 | NO-composable-from-mathlib | [report](mathlibable/Roth.weight_nonneg.md) |
| 32 | `Roth.weight_zero` | Roth/Box.lean:80 | NO-mathlib-has-it | [report](mathlibable/Roth.weight_zero.md) |
| 33 | `Roth.weight_add` | Roth/Box.lean:85 | NO-mathlib-has-it | [report](mathlibable/Roth.weight_add.md) |
| 34 | `Roth.weight_eq_zero_iff` | Roth/Box.lean:91 | YES-but-generalise-first | [report](mathlibable/Roth.weight_eq_zero_iff.md) |
| 35 | `Roth.weight_single` | Roth/Box.lean:96 | NO-mathlib-has-it | [report](mathlibable/Roth.weight_single.md) |
| 36 | `Roth.weight_le_card` | Roth/Box.lean:103 | NO-composable-from-mathlib | [report](mathlibable/Roth.weight_le_card.md) |
| 37 | `Roth.weight_mul_left` | Roth/Box.lean:110 | NO-composable-from-mathlib | [report](mathlibable/Roth.weight_mul_left.md) |
| 38 | `Roth.weight_le_degree_div` | Roth/Box.lean:118 | SKIP | [report](mathlibable/Roth.weight_le_degree_div.md) |
| 39 | `Roth.weight_mapDomain` | Roth/Box.lean:127 | NO-mathlib-has-it | [report](mathlibable/Roth.weight_mapDomain.md) |
| 40 | `Roth.wronskianMatrix` | Roth/Wronskian.lean:56 | YES-but-generalise-first | [report](mathlibable/Roth.wronskianMatrix.md) |
| 41 | `Roth.wronskian` | Roth/Wronskian.lean:60 | YES-but-generalise-first | [report](mathlibable/Roth.wronskian.md) |
| 42 | `Roth.wronskian_eq_zero_of_not_linearIndependent` | Roth/Wronskian.lean:65 | YES-but-generalise-first | [report](mathlibable/Roth.wronskian_eq_zero_of_not_linearIndependent.md) |
| 43 | `Roth.det_choose_eq` | Roth/Wronskian.lean:79 | YES-but-generalise-first | [report](mathlibable/Roth.det_choose_eq.md) |
| 44 | `Roth.coeff_prod_of_natDegree_le'` | Roth/Wronskian.lean:93 | SKIP | [report](mathlibable/Roth.coeff_prod_of_natDegree_le'.md) |
| 45 | `Roth.sum_range_le_sum_of_injective` | Roth/Wronskian.lean:107 | SKIP | [report](mathlibable/Roth.sum_range_le_sum_of_injective.md) |
| 46 | `Roth.coeff_wronskian_of_natDegree_injective` | Roth/Wronskian.lean:122 | YES-but-generalise-first | [report](mathlibable/Roth.coeff_wronskian_of_natDegree_injective.md) |
| 47 | `Roth.wronskian_ne_zero_of_natDegree_injective` | Roth/Wronskian.lean:148 | YES-but-generalise-first | [report](mathlibable/Roth.wronskian_ne_zero_of_natDegree_injective.md) |
| 48 | `Roth.wronskian_update_sub_smul` | Roth/Wronskian.lean:158 | YES-but-generalise-first | [report](mathlibable/Roth.wronskian_update_sub_smul.md) |
| 49 | `Roth.linearIndependent_update_sub_smul` | Roth/Wronskian.lean:170 | YES-but-generalise-first | [report](mathlibable/Roth.linearIndependent_update_sub_smul.md) |
| 50 | `Roth.sum_natDegree_update_lt` | Roth/Wronskian.lean:182 | NO-composable-from-mathlib | [report](mathlibable/Roth.sum_natDegree_update_lt.md) |
| 51 | `Roth.wronskian_ne_zero_of_linearIndependent` | Roth/Wronskian.lean:205 | YES-but-generalise-first | [report](mathlibable/Roth.wronskian_ne_zero_of_linearIndependent.md) |
| 52 | `Roth.wronskian_eq_zero_iff` | Roth/Wronskian.lean:219 | YES-but-generalise-first | [report](mathlibable/Roth.wronskian_eq_zero_iff.md) |
| 53 | `MvPolynomial.taylor` | Roth/Taylor.lean:42 | YES-add-as-is | [report](mathlibable/MvPolynomial.taylor.md) |
| 54 | `MvPolynomial.taylor_apply` | Roth/Taylor.lean:46 | INHERITED-YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_apply.md) |
| 55 | `MvPolynomial.taylor_X` | Roth/Taylor.lean:51 | INHERITED-YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_X.md) |
| 56 | `MvPolynomial.taylor_C` | Roth/Taylor.lean:55 | INHERITED-YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_C.md) |
| 57 | `MvPolynomial.taylor_monomial` | Roth/Taylor.lean:59 | INHERITED-YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_monomial.md) |
| 58 | `MvPolynomial.coeff_aeval_X_mul` | Roth/Taylor.lean:63 | SKIP | [report](mathlibable/MvPolynomial.coeff_aeval_X_mul.md) |
| 59 | `MvPolynomial.hasseCoeff_single_add_eq` | Roth/Taylor.lean:82 | SKIP | [report](mathlibable/MvPolynomial.hasseCoeff_single_add_eq.md) |
| 60 | `MvPolynomial.prod_pow_single_add_tsub` | Roth/Taylor.lean:92 | SKIP | [report](mathlibable/MvPolynomial.prod_pow_single_add_tsub.md) |
| 61 | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | Roth/Taylor.lean:101 | SKIP | [report](mathlibable/MvPolynomial.coeff_taylor_monomial_single_add_aux.md) |
| 62 | `MvPolynomial.coeff_taylor_monomial_aux` | Roth/Taylor.lean:120 | SKIP | [report](mathlibable/MvPolynomial.coeff_taylor_monomial_aux.md) |
| 63 | `MvPolynomial.coeff_taylor` | Roth/Taylor.lean:134 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.coeff_taylor.md) |
| 64 | `MvPolynomial.eval_taylor` | Roth/Taylor.lean:141 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.eval_taylor.md) |
| 65 | `MvPolynomial.taylor_taylor` | Roth/Taylor.lean:146 | YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_taylor.md) |
| 66 | `MvPolynomial.taylor_zero` | Roth/Taylor.lean:152 | INHERITED-YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_zero.md) |
| 67 | `MvPolynomial.taylor_map` | Roth/Taylor.lean:157 | YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_map.md) |
| 68 | `MvPolynomial.taylor_rename` | Roth/Taylor.lean:164 | YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_rename.md) |
| 69 | `MvPolynomial.degreeOf_taylor_le` | Roth/Taylor.lean:170 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.degreeOf_taylor_le.md) |
| 70 | `MvPolynomial.taylor_neg_taylor` | Roth/Taylor.lean:182 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.taylor_neg_taylor.md) |
| 71 | `MvPolynomial.taylor_injective` | Roth/Taylor.lean:187 | YES-add-as-is | [report](mathlibable/MvPolynomial.taylor_injective.md) |
| 72 | `MvPolynomial.taylor_eq_zero_iff` | Roth/Taylor.lean:192 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.taylor_eq_zero_iff.md) |
| 73 | `MvPolynomial.eq_sum_box_hasseDeriv` | Roth/Taylor.lean:197 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md) |
| 74 | `MvPolynomial.eval_eq_sum_box` | Roth/Taylor.lean:217 | YES-but-generalise-first | [report](mathlibable/MvPolynomial.eval_eq_sum_box.md) |
| 75 | `Roth.normOne` | Roth/CoeffNorm.lean:47 | YES-but-generalise-first | [report](mathlibable/Roth.normOne.md) |
| 76 | `Roth.normOne_nonneg` | Roth/CoeffNorm.lean:50 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_nonneg.md) |
| 77 | `Roth.normOne_eq_sum_of_support_subset` | Roth/CoeffNorm.lean:54 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_eq_sum_of_support_subset.md) |
| 78 | `Roth.normOne_monomial` | Roth/CoeffNorm.lean:59 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_monomial.md) |
| 79 | `Roth.normOne_zero` | Roth/CoeffNorm.lean:66 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_zero.md) |
| 80 | `Roth.abs_coeff_le_normOne` | Roth/CoeffNorm.lean:71 | YES-but-generalise-first | [report](mathlibable/Roth.abs_coeff_le_normOne.md) |
| 81 | `Roth.normOne_add_le` | Roth/CoeffNorm.lean:77 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_add_le.md) |
| 82 | `Roth.normOne_neg` | Roth/CoeffNorm.lean:86 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_neg.md) |
| 83 | `Roth.normOne_sum_le` | Roth/CoeffNorm.lean:90 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_sum_le.md) |
| 84 | `Roth.normOne_mul_le` | Roth/CoeffNorm.lean:96 | YES-but-generalise-first | [report](mathlibable/Roth.normOne_mul_le.md) |

## Remaining declarations (in processing order)

- #85 `Roth.normOne_prod_le` (Roth/CoeffNorm.lean:105, public theorem)
- #86 `Roth.normOne_le_card_mul` (Roth/CoeffNorm.lean:113, public theorem)
- #87 `Roth.normOne_det_le` (Roth/CoeffNorm.lean:119, public theorem)
- #88 `Roth.abs_coeff_hasseDeriv_le` (Roth/CoeffNorm.lean:134, public theorem)
- #89 `Roth.normOne_hasseDeriv_le` (Roth/CoeffNorm.lean:148, public theorem)
- #90 `Roth.diag` (Roth/CoeffNorm.lean:161, public def)
- #91 `Roth.diag_eq_sum` (Roth/CoeffNorm.lean:164, public theorem)
- #92 `Roth.abs_coeff_diag_le` (Roth/CoeffNorm.lean:174, public theorem)
- #93 `Roth.natDegree_diag_le` (Roth/CoeffNorm.lean:183, public theorem)
- #94 `Roth.eval_diag` (Roth/CoeffNorm.lean:193, public theorem)
- #95 `Roth.diag_sub` (Roth/CoeffNorm.lean:199, public theorem)
- #96 `Roth.geom_sum_le_one_add_pow` (Roth/CoeffNorm.lean:205, public theorem)
- #97 `Roth.sum_box_prod_pow_le_aux` (Roth/CoeffNorm.lean:214, private theorem)
- #98 `Roth.abs_eval_le` (Roth/CoeffNorm.lean:223, public theorem)
- #99 `Roth.degreeOf_det_hasseDeriv_le` (Roth/CoeffNorm.lean:245, public theorem)
- #100 `Roth.abs_coeff_det_hasseDeriv_le` (Roth/CoeffNorm.lean:258, public theorem)
- #101 `Roth.genWronskian` (Roth/GenWronskian.lean:32, public def)
- #102 `Roth.genWronskian_eq_zero_of_not_linearIndependent` (Roth/GenWronskian.lean:41, public theorem)
- #103 `Roth.kronecker` (Roth/GenWronskian.lean:53, public def)
- #104 `Roth.kroneckerExp` (Roth/GenWronskian.lean:57, public def)
- #105 `Roth.kronecker_monomial` (Roth/GenWronskian.lean:60, public theorem)
- #106 `Roth.kroneckerExp_injOn` (Roth/GenWronskian.lean:69, public theorem)
- #107 `Roth.coeff_kronecker` (Roth/GenWronskian.lean:88, public theorem)
- #108 `Roth.kronecker_eq_zero_iff` (Roth/GenWronskian.lean:106, public theorem)
- #109 `Roth.linearIndependent_kronecker` (Roth/GenWronskian.lean:117, public theorem)
- #110 `Roth.derivative_aeval` (Roth/GenWronskian.lean:133, public theorem)
- #111 `Roth.kronHasse` (Roth/GenWronskian.lean:145, private def)
- #112 `Roth.kronSpan` (Roth/GenWronskian.lean:149, private def)
- #113 `Roth.derivative_kronHasse_aux` (Roth/GenWronskian.lean:153, private lemma)
- #114 `Roth.derivative_mem_kronSpan` (Roth/GenWronskian.lean:162, private lemma)
- #115 `Roth.hasseDeriv_kronecker_mem` (Roth/GenWronskian.lean:190, private lemma)
- #116 `Roth.exists_hasseDeriv_kronecker_eq_sum` (Roth/GenWronskian.lean:214, public theorem)
- #117 `Roth.det_sum_rows` (Roth/GenWronskian.lean:228, public theorem)
- #118 `Roth.wronskian_kronecker_eq_sum_aux` (Roth/GenWronskian.lean:238, private lemma)
- #119 `Roth.exists_genWronskian_ne_zero` (Roth/GenWronskian.lean:254, public theorem)
- #120 `Roth.sqrt_one_sub_inv_lt` (Roth/Lattice.lean:29, public theorem)
- #121 `Roth.inv_add_inv_le` (Roth/Lattice.lean:40, private lemma)
- #122 `Roth.sum_inv_le` (Roth/Lattice.lean:47, private lemma)
- #123 `Roth.sum_inv_lt` (Roth/Lattice.lean:68, public theorem)
- #124 `Roth.extend_apply_castSucc` (Roth/Lattice.lean:92, private lemma)
- #125 `Roth.extend_apply_last` (Roth/Lattice.lean:96, private lemma)
- #126 `Roth.card_filter_box_fiber_aux` (Roth/Lattice.lean:100, private lemma)
- #127 `Roth.card_filter_box_last` (Roth/Lattice.lean:131, public theorem)
- #128 `Roth.filter_weight_le_eq_empty` (Roth/Lattice.lean:143, private lemma)
- #129 `Roth.card_filter_fiber_eq` (Roth/Lattice.lean:147, private lemma)
- #130 `Roth.card_filter_weight_le_of_le_sqrt_aux` (Roth/Lattice.lean:158, private lemma)
- #131 `Roth.card_filter_weight_le_succ_aux` (Roth/Lattice.lean:166, private lemma)
- #132 `Roth.card_filter_weight_le` (Roth/Lattice.lean:202, public theorem)
- #133 `Roth.index` (Roth/Index.lean:58, public def)
- #134 `Roth.mem_support_taylor_iff` (Roth/Index.lean:62, private lemma)
- #135 `Roth.index_le_weight` (Roth/Index.lean:69, public theorem)
- #136 `Roth.exists_weight_eq_index` (Roth/Index.lean:76, public theorem)
- #137 `Roth.le_index_iff` (Roth/Index.lean:85, public theorem)
- #138 `Roth.index_nonneg` (Roth/Index.lean:93, public theorem)
- #139 `Roth.index_eq_zero_iff` (Roth/Index.lean:98, public theorem)
- #140 `Roth.index_sub_weight_le_index_hasseDeriv` (Roth/Index.lean:109, public theorem)
- #141 `Roth.le_index_sum` (Roth/Index.lean:118, public theorem)
- #142 `Roth.weight_eq_finsuppWeight_div` (Roth/Index.lean:130, public theorem)
- #143 `Roth.index_eq_weightedOrder_div` (Roth/Index.lean:143, public theorem)
- #144 `Roth.index_mul` (Roth/Index.lean:162, public theorem)
- #145 `Roth.index_prod` (Roth/Index.lean:175, public theorem)
- #146 `Roth.index_neg` (Roth/Index.lean:190, public theorem)
- #147 `Roth.index_C_mul` (Roth/Index.lean:195, public theorem)
- #148 `Roth.index_mul_left_weights` (Roth/Index.lean:200, public theorem)
- #149 `Roth.index_rename` (Roth/Index.lean:212, public theorem)
- #150 `Roth.index_le_card` (Roth/Index.lean:224, public theorem)
- #151 `Roth.index_unique` (Roth/Index.lean:234, public theorem)
- #152 `Roth.eq_mapDomain_some_add_single` (Roth/Separation.lean:57, public theorem)
- #153 `Roth.coeff_X_none_pow_mul_rename` (Roth/Separation.lean:64, private lemma)
- #154 `Roth.coeffNone` (Roth/Separation.lean:80, public def)
- #155 `Roth.coeff_coeffNone` (Roth/Separation.lean:85, public theorem)
- #156 `Roth.eq_sum_X_none_pow_mul_coeffNone` (Roth/Separation.lean:98, public theorem)
- #157 `Roth.degreeOf_coeffNone_le` (Roth/Separation.lean:114, public theorem)
- #158 `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:123, public theorem)
- #159 `Roth.aeval_X_eq_rename` (Roth/Separation.lean:137, public theorem)
- #160 `Roth.hasseDeriv_rename_mul_aeval` (Roth/Separation.lean:146, public theorem)
- #161 `Roth.coeff_uniqueAlgEquiv_symm` (Roth/Separation.lean:169, public theorem)
- #162 `Roth.degreeOf_uniqueAlgEquiv_symm` (Roth/Separation.lean:174, public theorem)
- #163 `Roth.degreeOf_rename_mul_aeval` (Roth/Separation.lean:197, public theorem)
- #164 `Roth.degreeOf_none_rename_mul_aeval` (Roth/Separation.lean:213, public theorem)
- #165 `Roth.linearIndependent_coordinate_polynomials_aux` (Roth/Separation.lean:235, private lemma)
- #166 `Roth.eq_sum_aeval_basis_coeffNone_aux` (Roth/Separation.lean:265, private lemma)
- #167 `Roth.exists_coeffNone_basis_aux` (Roth/Separation.lean:291, private lemma)
- #168 `Roth.exists_separated_representation` (Roth/Separation.lean:325, public theorem)
- #169 `Roth.det_hasseDeriv_separated` (Roth/Separation.lean:351, public theorem)
- #170 `Roth.exists_sum_mul_eq_gcd` (Roth/Separation.lean:374, public theorem)
- #171 `Roth.exists_nat_smul_eq_map` (Roth/Separation.lean:380, public theorem)
- #172 `Roth.exists_primitive_smul_eq` (Roth/Separation.lean:406, public theorem)
- #173 `Roth.exists_int_eq_of_gcd_eq_one` (Roth/Separation.lean:443, public theorem)
- #174 `Roth.rescale_separated_factor_aux` (Roth/Separation.lean:457, private lemma)
- #175 `Roth.exists_int_polynomial_of_primitive_factor_aux` (Roth/Separation.lean:466, private lemma)
- #176 `Roth.exists_int_factors` (Roth/Separation.lean:485, public theorem)
- #177 `Roth.exists_rat_factors_det_hasseDeriv_aux` (Roth/Separation.lean:510, private lemma)
- #178 `Roth.exists_det_eq_mul` (Roth/Separation.lean:542, public theorem)
- #179 `Roth.RSet` (Roth/Theta.lean:56, public def)
- #180 `Roth.indexSet` (Roth/Theta.lean:62, public def)
- #181 `Roth.Θ` (Roth/Theta.lean:68, public def)
- #182 `Roth.one_mem_RSet` (Roth/Theta.lean:73, public theorem)
- #183 `Roth.indexSet_nonempty` (Roth/Theta.lean:80, public theorem)
- #184 `Roth.indexSet_bddAbove` (Roth/Theta.lean:87, public theorem)
- #185 `Roth.index_le_Θ` (Roth/Theta.lean:99, public theorem)
- #186 `Roth.Θ_nonneg` (Roth/Theta.lean:107, public theorem)
- #187 `Roth.Θ_le_card` (Roth/Theta.lean:114, public theorem)
- #188 `Roth.Θ_le_of_forall_index_le` (Roth/Theta.lean:124, public theorem)
- #189 `Roth.Θ_mono` (Roth/Theta.lean:134, public theorem)
- #190 `Roth.indexSet_comp_subset` (Roth/Theta.lean:141, private lemma)
- #191 `Roth.Θ_equiv` (Roth/Theta.lean:159, public theorem)
- #192 `Roth.isPrimitive_linear` (Roth/Theta.lean:167, private lemma)
- #193 `Roth.isPrimitive_pow` (Roth/Theta.lean:175, private lemma)
- #194 `Roth.exists_eq_pow_mul_of_rootMultiplicity` (Roth/Theta.lean:184, public theorem)
- #195 `Roth.pow_rootMultiplicity_le` (Roth/Theta.lean:206, public theorem)
- #196 `Roth.index_unique_le_log_div` (Roth/Theta.lean:223, private lemma)
- #197 `Roth.Θ_unique_le` (Roth/Theta.lean:256, public theorem)
- #198 `Roth.lem6M` (Roth/Theta.lean:270, public def)
- #199 `Roth.lem6Φ` (Roth/Theta.lean:275, public def)
- #200 `Roth.one_le_lem6M` (Roth/Theta.lean:279, public theorem)
- #201 `Roth.floor_sq_div_two_le_sum` (Roth/Theta.lean:289, public theorem)
- #202 `Roth.sq_div_three_lt_floor_sq_div_two` (Roth/Theta.lean:300, public theorem)
- #203 `Roth.mul_div_two_le_sum_max_aux` (Roth/Theta.lean:304, private lemma)
- #204 `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` (Roth/Theta.lean:322, private lemma)
- #205 `Roth.mul_sq_div_three_le_sum_max_aux` (Roth/Theta.lean:347, private lemma)
- #206 `Roth.min_le_sum_max` (Roth/Theta.lean:362, public theorem)
- #207 `Roth.sum_max_sub_le_index_det` (Roth/Theta.lean:376, public theorem)
- #208 `Roth.index_separated_mul_le_aux` (Roth/Theta.lean:414, private lemma)
- #209 `Roth.index_det_le` (Roth/Theta.lean:457, public theorem)
- #210 `Roth.weight_le_delta_aux` (Roth/Theta.lean:494, private lemma)
- #211 `Roth.mapped_det_ne_zero_aux` (Roth/Theta.lean:511, private lemma)
- #212 `Roth.index_numeric_bound_aux` (Roth/Theta.lean:531, private lemma)
- #213 `Roth.index_le_lem6` (Roth/Theta.lean:556, public theorem)
- #214 `Roth.Θ_option_le` (Roth/Theta.lean:593, public theorem)
- #215 `Roth.factorial_coefficient_le_two_pow_aux` (Roth/Theta.lean:609, private lemma)
- #216 `Roth.two_pow_lt_rpow_aux` (Roth/Theta.lean:621, private lemma)
- #217 `Roth.lem6M_lt` (Roth/Theta.lean:649, public theorem)
- #218 `Roth.lem7_Φ_bound` (Roth/Theta.lean:678, public theorem)
- #219 `Roth.lem7_numeric` (Roth/Theta.lean:709, public theorem)
- #220 `Roth.theta_scaled_unique_le_aux` (Roth/Theta.lean:742, private lemma)
- #221 `Roth.theta_delta_succ_lt_aux` (Roth/Theta.lean:767, private lemma)
- #222 `Roth.theta_prefix_lt_aux` (Roth/Theta.lean:776, private lemma)
- #223 `Roth.theta_lt_base_aux` (Roth/Theta.lean:818, private lemma)
- #224 `Roth.theta_denominators_one_lt_aux` (Roth/Theta.lean:833, private lemma)
- #225 `Roth.theta_phi_lt_aux` (Roth/Theta.lean:840, private lemma)
- #226 `Roth.theta_lt_succ_aux` (Roth/Theta.lean:891, private lemma)
- #227 `Roth.theta_lt_of_large_delta_aux` (Roth/Theta.lean:932, private lemma)
- #228 `Roth.Θ_lt` (Roth/Theta.lean:962, public theorem)
- #229 `Roth.lam` (Roth/MainLemma.lean:60, public def)
- #230 `Roth.gam` (Roth/MainLemma.lean:63, public def)
- #231 `Roth.eta` (Roth/MainLemma.lean:66, public def)
- #232 `Roth.mainCoeffBound` (Roth/MainLemma.lean:69, public def)
- #233 `Roth.exists_delta_bound` (Roth/MainLemma.lean:77, public theorem)
- #234 `Roth.eta_lt_gam_iff` (Roth/MainLemma.lean:100, public theorem)
- #235 `Roth.sqrt_lt_nat_floor_aux` (Roth/MainLemma.lean:104, private lemma)
- #236 `Roth.sqrt_lt_floor` (Roth/MainLemma.lean:115, public theorem)
- #237 `Roth.four_lt_rpow` (Roth/MainLemma.lean:122, public theorem)
- #238 `Roth.mul_log_div_two_lt_log_mainCoeffBound` (Roth/MainLemma.lean:149, public theorem)
- #239 `Roth.two_lt_rpow_aux` (Roth/MainLemma.lean:156, private lemma)
- #240 `Roth.three_small_factors` (Roth/MainLemma.lean:180, public theorem)
- #241 `Roth.exists_norm_coeff_reduction_aux` (Roth/MainLemma.lean:212, private lemma)
- #242 `Roth.norm_coeff_modByMonic_le` (Roth/MainLemma.lean:252, public theorem)
- #243 `Roth.boxFamily` (Roth/MainLemma.lean:275, public def)
- #244 `Roth.boxFamily_eq_image_finsupp_aux` (Roth/MainLemma.lean:280, private lemma)
- #245 `Roth.boxFamily_finite` (Roth/MainLemma.lean:301, public theorem)
- #246 `Roth.ncard_boxFamily` (Roth/MainLemma.lean:311, public theorem)
- #247 `Roth.floor_rpow_count_lt_aux` (Roth/MainLemma.lean:320, private lemma)
- #248 `Roth.pigeonhole_count` (Roth/MainLemma.lean:334, public theorem)
- #249 `Roth.exists_ne_modByMonic_eq` (Roth/MainLemma.lean:359, public theorem)
- #250 `Roth.sub_mem_RSet` (Roth/MainLemma.lean:388, public theorem)
- #251 `Roth.eval_hasseDeriv_sub_eq_zero` (Roth/MainLemma.lean:402, public theorem)
- #252 `Roth.le_index_of_forall_eval_eq_zero` (Roth/MainLemma.lean:419, public theorem)
- #253 `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul` (Roth/MainLemma.lean:433, public theorem)
- #254 `Roth.exists_hasseDeriv_eval_ne_zero` (Roth/MainLemma.lean:454, public theorem)
- #255 `Roth.abs_eval_iterated_hasseDeriv_lt_aux` (Roth/MainLemma.lean:459, private lemma)
- #256 `Roth.exists_hasseDeriv_index_eval_bound_aux` (Roth/MainLemma.lean:477, private lemma)
- #257 `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` (Roth/MainLemma.lean:497, private lemma)
- #258 `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` (Roth/MainLemma.lean:515, private lemma)
- #259 `Roth.exists_mem_RSet_le_index_aux` (Roth/MainLemma.lean:550, private lemma)
- #260 `Roth.mul_card_filter_weight_le_aux` (Roth/MainLemma.lean:569, private lemma)
- #261 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (Roth/MainLemma.lean:581, private lemma)
- #262 `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (Roth/MainLemma.lean:618, private lemma)
- #263 `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (Roth/MainLemma.lean:643, private lemma)
- #264 `Roth.theta_lt_eta_of_sq_log_bound_aux` (Roth/MainLemma.lean:671, private lemma)
- #265 `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (Roth/MainLemma.lean:692, private lemma)
- #266 `Roth.main_lemma` (Roth/MainLemma.lean:735, public theorem)
- #267 `Roth.approxSet` (Roth/Main.lean:55, public def)
- #268 `Roth.exists_nat_mul_isIntegral` (Roth/Main.lean:62, public theorem)
- #269 `Roth.approxSet_den_le_finite` (Roth/Main.lean:73, public theorem)
- #270 `Roth.eventually_div_rpow_lt` (Roth/Main.lean:103, public theorem)
- #271 `Roth.reduction` (Roth/Main.lean:118, public theorem)
- #272 `Roth.exists_monic_aeval_eq_zero` (Roth/Main.lean:142, public theorem)
- #273 `Roth.approxSet_num_den_mem_aux` (Roth/Main.lean:149, private theorem)
- #274 `Roth.exists_reduced_approx` (Roth/Main.lean:164, public theorem)
- #275 `Roth.exists_m` (Roth/Main.lean:196, public theorem)
- #276 `Roth.exists_delta` (Roth/Main.lean:227, public theorem)
- #277 `Roth.exists_approximants` (Roth/Main.lean:256, public theorem)
- #278 `Roth.exists_degrees` (Roth/Main.lean:282, public theorem)
- #279 `Roth.one_le_prod_pow_mul_abs_eval` (Roth/Main.lean:324, public theorem)
- #280 `Roth.abs_prod_pow_le_rpow_of_le_weight` (Roth/Main.lean:347, private lemma)
- #281 `Roth.abs_eval_lt_of_le_index` (Roth/Main.lean:380, public theorem)
- #282 `Roth.exists_roth_parameters_aux` (Roth/Main.lean:410, private lemma)
- #283 `Roth.exists_roth_approximants_aux` (Roth/Main.lean:429, private lemma)
- #284 `Roth.one_lt_roth_eval_bound_aux` (Roth/Main.lean:453, private lemma)
- #285 `Roth.roth_product_bound_aux` (Roth/Main.lean:481, private lemma)
- #286 `Roth.roth_log_bound_aux` (Roth/Main.lean:505, private lemma)
- #287 `Roth.roth_of_isIntegral` (Roth/Main.lean:547, public theorem)
- #288 `Roth.roth` (Roth/Main.lean:573, public theorem)
- #289 `Roth.roth_rat` (Roth/Main.lean:581, public theorem)
- #290 `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine` (Roth/LeanEval.lean:16, public def)
- #291 `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux` (Roth/LeanEval.lean:20, private lemma)
- #292 `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` (Roth/LeanEval.lean:42, public theorem)
- #293 `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` (Roth/LeanEval.lean:61, public theorem)
