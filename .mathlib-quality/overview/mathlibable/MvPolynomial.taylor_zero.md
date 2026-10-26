---
decl: MvPolynomial.taylor_zero
file: Roth/Taylor.lean
line: 152
kind: theorem
visibility: public
verdict: INHERITED-YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Glue simp lemma for MvPolynomial.taylor (translation by 0 is the identity), proved by unfolding taylor plus mathlib's aeval_X_left_apply; multivariate analogue of Polynomial.taylor_zero, ships with the YES-add-as-is parent, but should be restated with Pi zero since the current fun-form LHS does not fire on taylor 0 P.
action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean stated as @[simp] taylor 0 P = P (plus bundled taylor_zero' : taylor 0 = AlgHom.id R _), both compiled in evidence; locally keep (fires implicitly in simp of taylor_neg_taylor, Roth/Taylor.lean:184).
---

# MvPolynomial.taylor_zero

## Inventory entry

### `theorem MvPolynomial.taylor_zero`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (P : MvPolynomial σ R), (taylor fun _ ↦ (0 : R)) P = P`
- **What**: Translation by the zero vector is the identity: `P(X + 0) = P`.
- **How**: `simp [taylor, aeval_X_left_apply]` — unfolds `taylor` to `aeval (fun j ↦ X j + C 0)`, simp normalises `C 0 = 0`, `X j + 0 = X j`, then mathlib's `MvPolynomial.aeval_X_left_apply : aeval X p = p` (Mathlib/Algebra/MvPolynomial/Eval.lean:604) closes it.
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: no use by name in `Roth/` (`grep -rn taylor_zero Roth/` finds only the declaration). It is `@[simp]` and fires implicitly in `MvPolynomial.taylor_neg_taylor` (Roth/Taylor.lean:184, `simp [taylor_taylor]`): evidence item 4 shows that `simp [taylor_taylor, -taylor_zero]` leaves `taylor (fun j ↦ 0) P = P` unsolved.
- **Visibility**: public
- **Lines**: 150–153, proof length 1 line
- **Notes**: Mirrors mathlib's univariate `Polynomial.taylor_zero : taylor 0 f = f` (Mathlib/Algebra/Polynomial/Taylor.lean:55) and `taylor_zero'`, but states the translation vector as `fun _ ↦ 0` rather than the Pi zero `0`; as a simp lemma it then does not fire on `taylor 0 P` (evidence item 1).

## Junk check (Step 8)
- Used anywhere? Yes, implicitly as a simp lemma in `taylor_neg_taylor` (Roth/Taylor.lean:184); no use by name.
- Wrapper of 1–2 mathlib calls? Yes (`aeval_X_left_apply` after unfolding), but it is the standard identity-translation lemma of the API, the role `Polynomial.taylor_zero` plays in mathlib, and simp cannot find it without unfolding `taylor`.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `taylor_zero` finds only univariate `Polynomial.taylor_zero` / `Polynomial.taylor_zero'`.
- Too specific? No.
- Well-chosen? Mostly; the LHS should use Pi `0` (`taylor 0 P`), matching mathlib and the simp normal form (evidence items 1–2).
- Conclusion: `KEEP`. Action: keep; on upstreaming restate as `taylor 0 P = P`.

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.taylor

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.taylor_zero` absent from mathlib (only univariate `Polynomial.taylor_zero`), so no SKIP.

Glue classification: the statement is the trivial value of the defining family `taylor α` at `α = 0`, and the proof is pure unfolding of `taylor := aeval (fun j ↦ X j + C (α j))` followed by mathlib's `aeval_X_left_apply`; no mathematical content beyond the definition. Same treatment as the siblings `MvPolynomial.taylor_X` and `MvPolynomial.taylor_C` (both INHERITED-YES-add-as-is). The parent `MvPolynomial.taylor` is `YES-add-as-is` (not `NO-mathlib-has-it`), so the re-aim rule does not apply, and the parent report already lists `taylor_zero` in its PR grouping.

Statement-shape note (compiled, evidence items 1–3): the current form `taylor (fun _ ↦ 0) P = P` is not keyed on the Pi zero, so `simp` makes no progress on `taylor 0 P`. Upstream it should be stated as `@[simp] theorem taylor_zero (P) : taylor 0 P = P` (same proof works), with the bundled companion `taylor_zero' : taylor (0 : σ → R) = AlgHom.id R _`, matching `Polynomial.taylor_zero` / `taylor_zero'`. This pairs with the `taylor_taylor` report's recommendation to state the RHS as `taylor (α + β)`; with both restated, `taylor_neg_taylor` would simp via `neg_add_cancel` to `taylor 0`. Locally the fun-form is what `simp [taylor_taylor]` produces today, so the project version should only change together with `taylor_taylor`.

Verdict `INHERITED-YES-add-as-is`, cost CHEAP.

Next step: include in the parent's upstream PR (Mathlib/Algebra/MvPolynomial/Taylor.lean) as `@[simp] taylor_zero : taylor 0 P = P` plus `taylor_zero'`.

## Evidence
- Source read: Roth/Taylor.lean:150-153, and `taylor_neg_taylor` at Roth/Taylor.lean:182-185.
- `grep -rn taylor_zero Roth/`: declaration only (Taylor.lean:152).
- `grep -rn taylor_zero .lake/packages/mathlib/Mathlib`: only `Polynomial.taylor_zero` (Algebra/Polynomial/Taylor.lean:55), `Polynomial.taylor_zero'` (l.58) and a use at l.211.
- `grep aeval_X_left_apply`: Mathlib/Algebra/MvPolynomial/Eval.lean:604.
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_zero/checks.lean` (imports `Roth.Taylor`; compiles clean with `lake env lean`):
  1. `fail_if_success simp` on `taylor 0 P = P` succeeds: the current simp lemma does not fire on the Pi-zero form.
  2. `taylor_zero_pi : taylor 0 P = P` by `simp [taylor, aeval_X_left_apply]`: compiles.
  3. `taylor_zero_pi' : taylor (0 : σ → R) = AlgHom.id R _` by `AlgHom.ext taylor_zero_pi`: compiles.
  4. `taylor_neg_taylor` goal: `simp [taylor_taylor, -taylor_zero]; done` fails (implicit use confirmed), `simp [taylor_taylor]` closes it.
- Parent report: .mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md (YES-add-as-is; PR grouping includes taylor_zero). Siblings: MvPolynomial.taylor_C.md, MvPolynomial.taylor_X.md, MvPolynomial.taylor_taylor.md.
