---
decl: MvPolynomial.hasseDeriv_monomial
file: Roth/HasseDeriv.lean
line: 66
kind: theorem
visibility: public
verdict: INHERITED-YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Defining equation of MvPolynomial.hasseDeriv on monomials proved by simp [hasseDeriv] (pure unfolding); it is the multivariate analogue of mathlib's Polynomial.hasseDeriv_monomial and ships with the parent.
action: Upstream with MvPolynomial.hasseDeriv in a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, restating the coefficient as (k.choose d : R) per the hasseCoeff report; locally keep as is (used in coeff_hasseDeriv, hasseDeriv_C, hasseDeriv_monomial_mul, Taylor.lean coeff_taylor_monomial_single_add_aux).
---

# MvPolynomial.hasseDeriv_monomial

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_monomial`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (d k : σ →₀ ℕ) (a : R), hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a)`
- **What**: The Hasse derivative `Δ_d` sends `a X^k` to `binom(k, d) a X^(k - d)`, where `binom(k, d) = ∏ j (k j).choose (d j)`; the defining equation of `hasseDeriv` on monomials. Tagged `@[simp]`.
- **How**: `simp [hasseDeriv]` unfolds the `Finsupp.lsum` / `AddMonoidAlgebra.coeffLinearEquiv` composition and evaluates it on a single monomial (`Finsupp.lsum_single`-style simp).
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`
- **Used by**: `MvPolynomial.coeff_hasseDeriv` (Roth/HasseDeriv.lean:94), `MvPolynomial.hasseDeriv_C` (Roth/HasseDeriv.lean:127), private `MvPolynomial.hasseDeriv_monomial_mul` (Roth/HasseDeriv.lean:233), private `coeff_taylor_monomial_single_add_aux` (Roth/Taylor.lean:111, 116); also available as a simp lemma project-wide.
- **Visibility**: public
- **Lines**: 66–68, proof length 1 line
- **Notes**: Name matches mathlib's univariate `Polynomial.hasseDeriv_monomial` (`hasseDeriv k (monomial n r) = monomial (n - k) (↑(n.choose k) * r)`), so the multivariate statement is uniform with it.

## Junk check (Step 8)
- Used anywhere? Yes, four call sites in two files plus `@[simp]`.
- Wrapper of 1–2 mathlib calls? It is the unfolding lemma of a project def; mandatory API, not a wrapper.
- Does mathlib have it? No: the qualified name `MvPolynomial.hasseDeriv_monomial` does not exist (namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds only `Polynomial.hasseDeriv_monomial` in Mathlib/Algebra/Polynomial/HasseDeriv.lean:104; no file in namespace `MvPolynomial` mentions `hasseDeriv`).
- Too specific? No, it is the basic characterising lemma.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: none locally; upstream together with the parent definition.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.hasseDeriv

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name absent from mathlib, so no SKIP. The proof is `simp [hasseDeriv]`, a pure unfolding of the parent definition on a monomial, so this is a glue lemma about an already-assessed parent. The parent `MvPolynomial.hasseDeriv` is `YES-but-generalise-first` (not `NO-mathlib-has-it`), so the re-aim rule does not apply and the verdict is `INHERITED-YES-but-generalise-first`.

The generalise-first part carries over directly: with the parent restated using the multi-index binomial `Finsupp.choose`, this lemma reads `hasseDeriv d (monomial k a) = monomial (k - d) ((k.choose d : R) * a)`, exactly parallel to mathlib's `Polynomial.hasseDeriv_monomial`; the parent's evidence file shows the `Finsupp.choose`-spelled definition is `rfl`-equal, so the restated lemma has the same one-line proof. Cost CHEAP: one-token change of the coefficient. Next step: include in the parent's upstream PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean).

## Evidence
- `grep -rn "theorem hasseDeriv_monomial" .lake/packages/mathlib/Mathlib/`: only Mathlib/Algebra/Polynomial/HasseDeriv.lean:104 (univariate).
- `grep -rln "namespace MvPolynomial" .lake/packages/mathlib/Mathlib/ | xargs grep -ln hasseDeriv`: no hits.
- `grep -rn hasseDeriv_monomial Roth/` for Used-by.
- Parent evidence reused: `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/generalise_mvpowerseries.lean` (`Finsupp.choose` spelling `rfl`-equal). No new evidence files.
