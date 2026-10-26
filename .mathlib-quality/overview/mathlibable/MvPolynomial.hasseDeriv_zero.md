---
decl: MvPolynomial.hasseDeriv_zero
file: Roth/HasseDeriv.lean
line: 120
kind: theorem
visibility: public
verdict: INHERITED-YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Bundled form hasseDeriv 0 = LinearMap.id, proved as pure glue LinearMap.ext hasseDeriv_zero_apply exactly like mathlib's univariate Polynomial.hasseDeriv_zero; ships with the pointwise lemma and the parent operator.
action: Upstream as @[simp] MvPolynomial.hasseDeriv_zero beside hasseDeriv_zero_apply in the new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean PR of MvPolynomial.hasseDeriv; locally keep (simp lemma, no named call sites).
---

# MvPolynomial.hasseDeriv_zero

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_zero`
- **Type**: `∀ {σ R : Type*} [CommSemiring R], hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)`
- **What**: The Hasse derivative of order zero is the identity linear map: `Δ_0 = id`.
- **How**: `LinearMap.ext hasseDeriv_zero_apply` (bundles the pointwise lemma `Δ_0 P = P`).
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply`
- **Used by**: no explicit call site in `Roth/` (`grep -rn hasseDeriv_zero Roth/` finds only the declaration and the docstring of `hasseDeriv_zero_apply`); it is `@[simp]`, so it may fire implicitly in `simp` calls on `hasseDeriv 0 _` (e.g. the `simpa` calls in Roth/Index.lean:104-105, `index_eq_zero_iff`).
- **Visibility**: public
- **Lines**: 120–121 (docstring 116–118, `@[simp]` 119), proof length 1 line
- **Notes**: Name, statement shape and proof are identical to mathlib's univariate `Polynomial.hasseDeriv_zero` (Mathlib/Algebra/Polynomial/HasseDeriv.lean:86-87, `LinearMap.ext <| hasseDeriv_zero'`) and parallel to `LaurentSeries.hasseDeriv_zero`.

## Junk check (Step 8)
- Used anywhere? No named use; it is the `@[simp]` normalisation lemma, so its uses are implicit through `simp`.
- Wrapper of 1–2 mathlib calls? It is `LinearMap.ext` applied to a project lemma; this is the standard bundled/pointwise pair that mathlib keeps for every operator family (`Polynomial.hasseDeriv_zero` / `hasseDeriv_zero'`), not a removable wrapper.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `hasseDeriv_zero` finds only `Polynomial.hasseDeriv_zero(')` and `LaurentSeries.hasseDeriv_zero`; no file in `Mathlib/Algebra/MvPolynomial` or `Mathlib/RingTheory/MvPowerSeries` mentions `hasseDeriv`.
- Too specific / inline? No, basic API.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: keep; upstream with the parent definition.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.hasseDeriv_zero_apply

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.hasseDeriv_zero` absent from mathlib, so no SKIP. The declaration is a pure glue lemma: its whole proof is `LinearMap.ext hasseDeriv_zero_apply`, i.e. the bundled restatement of the already-assessed pointwise lemma, with no mathematical content beyond it (conversely `LinearMap.congr_fun hasseDeriv_zero P` recovers the pointwise form; both directions compile in the evidence file). The parent `MvPolynomial.hasseDeriv_zero_apply` was assessed `YES-add-as-is` (full Phase 0–8 run: literature `D_0 = id` normalisation of Hasse–Schmidt derivations, absent from mathlib, maximally general since `CommSemiring R` is forced by `MvPolynomial`), so the re-aim rule does not apply and the verdict is `INHERITED-YES-add-as-is`. That report already designates this bundled `@[simp]` lemma as part of the same upstream PR.

Mathlib precedent for the exact form: `Polynomial.hasseDeriv_zero : hasseDeriv 0 = LinearMap.id := LinearMap.ext <| hasseDeriv_zero'`, used by `rw` in `Polynomial.factorial_smul_hasseDeriv` and `Polynomial.taylor_coeff_zero`. The generalise-first change of the grandparent `MvPolynomial.hasseDeriv` (coefficient via `Finsupp.choose`) does not touch this statement or its one-line proof. Cost CHEAP. Next step: include in the parent's upstream PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean), keeping `@[simp]` on the bundled form as mathlib does.

## Evidence
- `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_zero/glue_check.lean` (compiles with `lake env lean`, no errors; output only the `#check` of `Polynomial.hasseDeriv_zero`): bundled form = `LinearMap.ext fun P ↦ hasseDeriv_zero_apply P`, pointwise form = `LinearMap.congr_fun hasseDeriv_zero P`.
- `grep -rn hasseDeriv_zero .lake/packages/mathlib/Mathlib/`: only Algebra/Polynomial/HasseDeriv.lean (l.82, 86-87, 135), Algebra/Polynomial/Taylor.lean:80, RingTheory/LaurentSeries.lean:139; no multivariate version.
- `grep -rn hasseDeriv_zero Roth/` and `grep -rn "hasseDeriv 0\|hasseDeriv (0" Roth/`: no named use besides the declaration itself.
- Parent report `.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero_apply.md` (verdict YES-add-as-is) reused.
