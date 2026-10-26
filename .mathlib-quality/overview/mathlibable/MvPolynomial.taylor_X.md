---
decl: MvPolynomial.taylor_X
file: Roth/Taylor.lean
line: 51
kind: theorem
visibility: public
verdict: INHERITED-YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Defining simp equation of MvPolynomial.taylor on generators (taylor α (X j) = X j + C (α j)), proved by pure unfolding of taylor := aeval plus mathlib's aeval_X; multivariate analogue of mathlib's Polynomial.taylor_X, ships with the parent.
action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean (keep @[simp]); locally keep as is (used by name at Roth/Taylor.lean:114 in coeff_taylor_monomial_single_add_aux).
---

# MvPolynomial.taylor_X

## Inventory entry

### `theorem MvPolynomial.taylor_X`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (j : σ), taylor α (X j) = X j + C (α j)`
- **What**: The translation `P ↦ P(X + α)` sends the variable `X j` to `X j + α j`.
- **How**: term `aeval_X _ _` (mathlib's `MvPolynomial.aeval_X : aeval f (X n) = f n`), after `taylor α` unfolds definitionally to `aeval fun j ↦ X j + C (α j)`.
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: Roth/Taylor.lean:114 (`coeff_taylor_monomial_single_add_aux`, private, in a `rw` chain). It is `@[simp]`, but no project `simp` call is on a goal containing `taylor α (X j)` in normal form (the simp calls mentioning `taylor` in Roth/Taylor.lean l.143-166 unfold `taylor` itself; Roth/Index.lean simp calls go through `coeff_taylor`), so no implicit uses found.
- **Visibility**: public
- **Lines**: 49–51, proof length 1 line
- **Notes**: Name, shape and `@[simp]` attribute mirror mathlib's univariate `Polynomial.taylor_X : taylor r X = X + C r` (Mathlib/Algebra/Polynomial/Taylor.lean:47, proved `X_comp`).

## Junk check (Step 8)
- Used anywhere? Yes, by name at Roth/Taylor.lean:114 (key step of Taylor's theorem on monomials), and as a simp lemma of the API.
- Wrapper of 1–2 mathlib calls? Yes (`aeval_X`), but it is the standard computation lemma of a project def, exactly the role `Polynomial.taylor_X` plays in mathlib; it spares users from unfolding `taylor`.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `taylor_X` finds only `Polynomial.taylor_X` and `Polynomial.taylor_X_pow` (univariate).
- Too specific? No.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: keep; upstream with the parent.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.taylor

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.taylor_X` absent from mathlib (only univariate `Polynomial.taylor_X`), so no SKIP.

Glue classification: the statement is the defining equation of `taylor` on generators, and the proof is pure unfolding: `taylor α` is by definition `aeval fun j ↦ X j + C (α j)` (rfl, see `taylor_apply`), and `aeval_X` is mathlib's computation rule of `aeval` on `X`. There is no mathematical content beyond the definition (it is not literally `rfl` only because `aeval`/`eval₂` on `X j = monomial (single j 1) 1` reduces through a classical `Finsupp.single` support). This matches the precedent `MvPolynomial.hasseDeriv_monomial` (defining equation proved by `simp [hasseDeriv]`, treated as INHERITED). The parent `MvPolynomial.taylor` is `YES-add-as-is` (not `NO-mathlib-has-it`), so the re-aim rule does not apply, and the parent report already lists `taylor_X` in its PR grouping. Verdict `INHERITED-YES-add-as-is`, cost CHEAP.

Next step: include in the parent's upstream PR (Mathlib/Algebra/MvPolynomial/Taylor.lean), with `@[simp]`, mirroring `Polynomial.taylor_X`.

## Evidence
- Source read: Roth/Taylor.lean:49-51 and the use at l.114 (compiles as part of the clean project build; no separate evidence file needed).
- `grep -rn taylor_X Roth/`: declaration (l.51) and use (l.114).
- `grep -rn "theorem taylor_X" .lake/packages/mathlib/Mathlib/`: only Mathlib/Algebra/Polynomial/Taylor.lean l.47 (`taylor_X`) and l.50 (`taylor_X_pow`), univariate.
- `grep -rn simp Roth/ | grep taylor`: no simp call that would fire `taylor_X` implicitly.
- Parent report: .mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md (YES-add-as-is; PR grouping includes taylor_X). Precedent: MvPolynomial.hasseDeriv_monomial.md.
