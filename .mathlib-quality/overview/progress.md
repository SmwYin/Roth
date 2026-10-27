# Completed-only overview progress

Status: **in_progress**, 2026-10-26. Branch: `ramin-cleanup`.
Production Lean files and all pins match baseline `99f19fd`.

**Completed: 18 / 293 written declarations.**
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

**Next declaration: `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`**, `Roth/HasseDeriv.lean:219`.
Only the listed assessments are complete. No partial assessment was committed.

On restart: read [README](README.md), [machine progress](progress.json), and
[declaration order](declaration-order.json); verify source/pin hashes and accepted evidence,
then continue with the first unfinished declaration. Reports and evidence are tracked.
