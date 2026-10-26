# Completed-only overview progress

Status: **in_progress**, 2026-10-26. Branch: `ramin-cleanup`.
Production Lean files and all pins match baseline `99f19fd`.

**Completed: 3 / 293 written declarations.**
This counts the current overview assessments, separately from the earlier code cleanup.

| # | Completed declaration | Applicable workflow | Verdict | Report |
|---|---|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.hasseCoeff.md) |
| 2 | `MvPolynomial.hasseDeriv` | full-mathlibable; accepted complete | YES-add-as-is | [Detailed report](mathlibable/MvPolynomial.hasseDeriv.md) |
| 3 | `MvPolynomial.hasseDeriv_monomial` | full-mathlibable; accepted complete | NO-composable-from-mathlib | [Detailed report](mathlibable/MvPolynomial.hasseDeriv_monomial.md) |

**Next declaration: `MvPolynomial.hasseDeriv_apply`**, `Roth/HasseDeriv.lean:73`.
Only the listed assessments are complete. No partial assessment was committed.

On restart: read [README](README.md), [machine progress](progress.json), and
[declaration order](declaration-order.json); verify source/pin hashes and accepted evidence,
then continue with the first unfinished declaration. Reports and evidence are tracked.
