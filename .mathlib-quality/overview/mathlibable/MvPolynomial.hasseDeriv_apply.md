---
decl: MvPolynomial.hasseDeriv_apply
file: Roth/HasseDeriv.lean
line: 73
kind: theorem
visibility: public
verdict: INHERITED-YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Definitional expansion of MvPolynomial.hasseDeriv as a sum over the support (closes by rfl; current proof simp [hasseDeriv, sum_def]); multivariate analogue of mathlib's Polynomial.hasseDeriv_apply, ships with the parent.
action: Upstream with MvPolynomial.hasseDeriv in a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, coefficient spelled (k.choose d : R) per the hasseCoeff report; locally keep (used in Roth/CoeffNorm.lean:151 normOne_hasseDeriv_le).
---

# MvPolynomial.hasseDeriv_apply

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_apply`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (d : σ →₀ ℕ) (P : MvPolynomial σ R), hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k)`
- **What**: Expands the Hasse derivative `Δ_d P` as the sum, over the monomials `a_k X^k` of `P`, of `binom(k, d) a_k X^(k - d)`.
- **How**: `simp [hasseDeriv, sum_def]`: unfolds the `Finsupp.lsum ∘ₗ AddMonoidAlgebra.coeffLinearEquiv` definition and rewrites the resulting `Finsupp.sum` with `MvPolynomial.sum_def`. The statement is in fact definitional (closes by `rfl`, see Evidence).
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`
- **Used by**: `MvPolynomial.normOne_hasseDeriv_le` (Roth/CoeffNorm.lean:151); no other occurrence in `Roth/`.
- **Visibility**: public
- **Lines**: 73–75, proof length 1 line
- **Notes**: Name and shape mirror mathlib's univariate `Polynomial.hasseDeriv_apply` (`hasseDeriv k f = f.sum fun i r => monomial (i - k) (↑(i.choose k) * r)`, Mathlib/Algebra/Polynomial/HasseDeriv.lean:62). The project states it with an explicit `Finset` sum over `P.support` rather than the `Finsupp.sum` form; both are `rfl`-equal.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/CoeffNorm.lean:151, the `normOne` bound for Hasse derivatives).
- Wrapper of 1–2 mathlib calls? It is the unfolding lemma of a project def, the standard `_apply` API lemma that mathlib also provides for the univariate operator; not a removable wrapper.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds only `Polynomial.hasseDeriv_apply` (univariate); no `MvPolynomial` file mentions `hasseDeriv`.
- Too specific? No, it is the basic expansion lemma.
- Well-chosen? Yes; matches the univariate API naming.
- Conclusion: `KEEP`. Action: none locally; upstream together with the parent definition.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.hasseDeriv

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.hasseDeriv_apply` absent from mathlib, so no SKIP. The statement is definitionally equal to the definition of `hasseDeriv` applied to `P` (verified: `rfl` closes it, evidence file below), and the project proof is a pure `simp` unfolding, so this is a glue lemma about an already-assessed parent. The parent `MvPolynomial.hasseDeriv` is `YES-but-generalise-first` (not `NO-mathlib-has-it`), so the re-aim rule does not apply and the verdict is `INHERITED-YES-but-generalise-first`.

The generalise-first part carries over directly: with the parent's coefficient restated via the multi-index binomial `Finsupp.choose` (parent and `hasseCoeff` reports), this lemma reads `hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((k.choose d : R) * P.coeff k)`, parallel to `Polynomial.hasseDeriv_apply`. For mathlib one may prefer the `Finsupp.sum` form `(AddMonoidAlgebra.coeff P).sum fun k a ↦ monomial (k - d) (… * a)` to mirror the univariate lemma; both spellings are `rfl` (evidence). Cost CHEAP. Next step: include in the parent's upstream PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean).

## Evidence
- `grep -rn hasseDeriv_apply .lake/packages/mathlib/Mathlib/`: only Mathlib/Algebra/Polynomial/HasseDeriv.lean (univariate `Polynomial.hasseDeriv_apply`, l.62, and its uses).
- `grep -rn hasseDeriv_apply Roth/ Roth.lean`: declaration plus Roth/CoeffNorm.lean:151.
- `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_apply/unfold_check.lean` (compiles with `lake env lean`, no errors): both the project's `Finset`-sum statement and the `(AddMonoidAlgebra.coeff P).sum` form are proved by `rfl`, confirming the lemma is pure unfolding.
- Parent evidence reused: `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/generalise_mvpowerseries.lean` (`Finsupp.choose` spelling `rfl`-equal).
