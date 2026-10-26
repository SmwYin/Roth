---
decl: MvPolynomial.taylor_C
file: Roth/Taylor.lean
line: 55
kind: theorem
visibility: public
verdict: INHERITED-YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Defining simp equation of MvPolynomial.taylor on constants (taylor α (C a) = C a), a direct instance of mathlib's MvPolynomial.algHom_C for the R-algebra hom taylor α; multivariate analogue of mathlib's Polynomial.taylor_C, ships with the parent.
action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean (keep @[simp]); locally keep as is (used by name at Roth/Index.lean:197 in index_C_mul).
---

# MvPolynomial.taylor_C

## Inventory entry

### `theorem MvPolynomial.taylor_C`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (a : R), taylor α (C a) = C a`
- **What**: The translation `P ↦ P(X + α)` fixes constant polynomials.
- **How**: term `algHom_C _ _` (mathlib's `MvPolynomial.algHom_C : f (C r) = C r` for any `R`-algebra hom `f : MvPolynomial σ R →ₐ[R] A`, Mathlib/Algebra/MvPolynomial/Basic.lean:441), applied to the `AlgHom` `taylor α`.
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: Roth/Index.lean:197 (`index_C_mul`, in a `rw` chain). It is `@[simp]`, but no project `simp` call is on a goal containing `taylor α (C a)` (the simp calls mentioning `taylor` in Roth/Taylor.lean l.143-166 unfold `taylor` itself; Roth/Index.lean simp calls go through `coeff_taylor`), so no implicit uses found.
- **Visibility**: public
- **Lines**: 53–55, proof length 1 line
- **Notes**: Name, shape and `@[simp]` attribute mirror mathlib's univariate `Polynomial.taylor_C : taylor r (C x) = C x` (Mathlib/Algebra/Polynomial/Taylor.lean:53, proved `C_comp`).

## Junk check (Step 8)
- Used anywhere? Yes, by name at Roth/Index.lean:197 (`index_C_mul`, scaling invariance of the index), and as a simp lemma of the API.
- Wrapper of 1–2 mathlib calls? Yes (`algHom_C`), but it is the standard computation lemma of a project def, the role `Polynomial.taylor_C` plays in mathlib; it lets `rw`/`simp` fire without the user knowing `taylor α` is an `AlgHom` instance of `algHom_C` (which `simp` would not find by itself since `algHom_C` is not simp). One could write `algHom_C` at the single call site instead, but the parallel with the univariate API argues for keeping it.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `taylor_C` finds only univariate `Polynomial.taylor_C`.
- Too specific? No.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: keep; upstream with the parent.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.taylor

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.taylor_C` absent from mathlib (only univariate `Polynomial.taylor_C`), so no SKIP.

Glue classification: the statement is the defining equation of `taylor` on constants and the proof is a direct instantiation of mathlib's generic `algHom_C` at the `AlgHom` `taylor α` (pure unfolding of the fact that `taylor α` is an `R`-algebra hom; no mathematical content beyond the definition). Same treatment as the sibling `MvPolynomial.taylor_X` (INHERITED-YES-add-as-is, proved by `aeval_X _ _`). The parent `MvPolynomial.taylor` is `YES-add-as-is` (not `NO-mathlib-has-it`), so the re-aim rule does not apply, and the parent report already lists `taylor_C` in its PR grouping. Verdict `INHERITED-YES-add-as-is`, cost CHEAP.

Next step: include in the parent's upstream PR (Mathlib/Algebra/MvPolynomial/Taylor.lean), with `@[simp]`, mirroring `Polynomial.taylor_C`.

## Evidence
- Source read: Roth/Taylor.lean:53-55 and the use at Roth/Index.lean:197 (compiles as part of the clean project build; no separate evidence file needed).
- `grep -rn taylor_C Roth/`: declaration (Taylor.lean:55) and use (Index.lean:197).
- `grep -rn "theorem algHom_C\|theorem taylor_C" .lake/packages/mathlib/Mathlib/`: `MvPolynomial.algHom_C` (Algebra/MvPolynomial/Basic.lean:441) and univariate `Polynomial.taylor_C` (Algebra/Polynomial/Taylor.lean:53) only.
- `grep -rn "simp.*taylor" Roth/`: no simp call that would fire `taylor_C` implicitly.
- Parent report: .mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md (YES-add-as-is; PR grouping includes taylor_C). Sibling: MvPolynomial.taylor_X.md.
