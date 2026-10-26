---
decl: MvPolynomial.taylor_monomial
file: Roth/Taylor.lean
line: 59
kind: theorem
visibility: public
verdict: INHERITED-YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Computation rule of MvPolynomial.taylor on monomials (taylor α (monomial k a) = C a * k.prod (X j + C (α j))^n), proved by pure unfolding of taylor := aeval plus mathlib's aeval_monomial; multivariate analogue of mathlib's Polynomial.taylor_monomial, ships with the parent.
action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean; locally keep as is (used by name at Roth/Taylor.lean:212 in eq_sum_box_hasseDeriv).
---

# MvPolynomial.taylor_monomial

## Inventory entry

### `theorem MvPolynomial.taylor_monomial`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (k : σ →₀ ℕ) (a : R), taylor α (monomial k a) = C a * k.prod fun j n ↦ (X j + C (α j)) ^ n`
- **What**: The translate `P(X + α)` of the monomial `a X^k` is `a ∏_j (X_j + α_j)^{k_j}`.
- **How**: term `aeval_monomial _ _ _` (mathlib's `MvPolynomial.aeval_monomial : aeval g (monomial d r) = algebraMap _ _ r * d.prod fun i k => g i ^ k`, Mathlib/Algebra/MvPolynomial/Eval.lean:681), after `taylor α` unfolds definitionally to `aeval fun j ↦ X j + C (α j)` and `algebraMap R (MvPolynomial σ R)` is definitionally `C`.
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: Roth/Taylor.lean:212 (`eq_sum_box_hasseDeriv`, in a `rw` chain turning each `taylor (-α) (monomial d c)` into a product over `Fintype σ`). Not `@[simp]`; no other uses (the private `coeff_taylor_monomial_*_aux` lemmas only share the name prefix).
- **Visibility**: public
- **Lines**: 57–60, proof length 1 line
- **Notes**: Name and shape mirror mathlib's univariate `Polynomial.taylor_monomial : taylor r (monomial i k) = C k * (X + C r) ^ i` (Mathlib/Algebra/Polynomial/Taylor.lean:64).

## Junk check (Step 8)
- Used anywhere? Yes, by name at Roth/Taylor.lean:212 (Taylor expansion, polynomial form).
- Wrapper of 1–2 mathlib calls? Yes (`aeval_monomial`), but it is the standard computation lemma of a project def, the role `Polynomial.taylor_monomial` plays in mathlib; it spares users from unfolding `taylor` and rewriting `algebraMap` to `C`.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `theorem taylor_monomial` finds only the univariate `Polynomial.taylor_monomial`.
- Too specific? No.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: keep; upstream with the parent.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.taylor

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.taylor_monomial` absent from mathlib (only univariate `Polynomial.taylor_monomial`), so no SKIP.

Glue classification: the statement is the computation rule of `taylor` on monomials and the proof is pure unfolding: `taylor α` is by definition `aeval fun j ↦ X j + C (α j)` (rfl, see `taylor_apply`), and `aeval_monomial` is mathlib's computation rule of `aeval` on `monomial`, with `algebraMap R (MvPolynomial σ R) a` definitionally `C a` (the term proof typechecks without any rewrite). No mathematical content beyond the definition. Same classification as the sibling `MvPolynomial.taylor_X` (via `aeval_X`) and `MvPolynomial.taylor_C` (via `algHom_C`), both `INHERITED-YES-add-as-is`. The parent `MvPolynomial.taylor` is `YES-add-as-is` (not `NO-mathlib-has-it`), so the re-aim rule does not apply, and the parent report already lists `taylor_monomial` in its PR grouping. Verdict `INHERITED-YES-add-as-is`, cost CHEAP.

Next step: include in the parent's upstream PR (Mathlib/Algebra/MvPolynomial/Taylor.lean), mirroring `Polynomial.taylor_monomial`.

## Evidence
- Source read: Roth/Taylor.lean:57-60 and the use at l.212 (compiles as part of the clean project build; no separate evidence file needed).
- `grep -rn taylor_monomial Roth/`: declaration (l.59), use (l.212); other hits are the private `coeff_taylor_monomial_*_aux` lemmas (different names).
- `grep -rn "theorem taylor_monomial\|theorem aeval_monomial" .lake/packages/mathlib/Mathlib/`: `Polynomial.taylor_monomial` (Mathlib/Algebra/Polynomial/Taylor.lean:64, univariate), `MvPolynomial.aeval_monomial` (Mathlib/Algebra/MvPolynomial/Eval.lean:681), `Polynomial.aeval_monomial`.
- Parent report: .mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md (YES-add-as-is; PR grouping includes taylor_monomial). Sibling precedents: MvPolynomial.taylor_X.md, MvPolynomial.taylor_C.md.
