---
decl: Roth.coeff_X_none_pow_mul_rename
file: Roth/Separation.lean
line: 64
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private coefficient formula coeff_e(X_none^ν * rename some Q) = [e none = ν] Q_{e.some}, used once (simp_rw in eq_sum_X_none_pow_mul_coeffNone); mathlib has only the ingredients (optionEquivLeft_coeff_some_coeff_none, optionEquivLeft_X_none) and no rename-some / optionEquivLeft compatibility lemma.
action: Keep as private helper for its single call site Roth/Separation.lean:104 (eq_sum_X_none_pow_mul_coeffNone); optionally factor the duplicated fact optionEquivLeft (rename some Q) = C Q (here l.67-70 and in coeff_rename_mul_aeval l.124-126) into one lemma, a candidate for Mathlib/Algebra/MvPolynomial/Equiv.lean.
---

# Roth.coeff_X_none_pow_mul_rename

## Inventory entry

### `theorem Roth.coeff_X_none_pow_mul_rename`
- **Type**: `∀ {τ R : Type*} [CommSemiring R] (ν : ℕ) (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ), (X none ^ ν * rename some Q).coeff e = if e none = ν then Q.coeff (Finsupp.some e) else 0`
- **What**: In polynomials over the variables `Option τ` (with `none` the distinguished variable), the coefficient of the monomial `x^e` in `x_none^ν · Q(x_τ)` is the coefficient of `Q` at the restriction of `e` to `τ` when the `none`-exponent of `e` equals `ν`, and zero otherwise. Separation-of-variables coefficient formula for a pure power of the distinguished variable times a polynomial in the other variables.
- **How**: Shows `(optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom` by `ext i; simp`, hence `optionEquivLeft R τ (rename some Q) = Polynomial.C Q` (`AlgHom.congr_fun`). Then rewrites the coefficient through `optionEquivLeft_coeff_some_coeff_none` (backwards), `map_mul`, `map_pow`, `optionEquivLeft_X_none`, `Polynomial.X_pow_mul_C`, `Polynomial.C_mul_X_pow_eq_monomial`, `Polynomial.coeff_monomial`, and finishes by `by_cases he : e none = ν` with `simp`.
- **Hypotheses**: `[CommSemiring R]` only (the section's `[Fintype τ] [DecidableEq τ]` are omitted); `classical` inside the proof.
- **Uses from project**: `[]` (only mathlib lemmas)
- **Used by**: Roth/Separation.lean: `eq_sum_X_none_pow_mul_coeffNone` (l.104, `simp_rw [coeff_X_none_pow_mul_rename]`) only; `grep -rn coeff_X_none_pow_mul_rename Roth/` gives the definition (l.64) and that single use. Transitively everything downstream of `eq_sum_X_none_pow_mul_coeffNone` (the separated representation in Lemma 2, `exists_separated_representation`, `exists_det_eq_mul`).
- **Visibility**: private
- **Lines**: 63–77, proof length 12 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). The auxiliary fact `optionEquivLeft R τ (rename some Q) = Polynomial.C Q` is proved verbatim again inside `coeff_rename_mul_aeval` (l.124–127); mathlib has no lemma for it (it is derivable from `optionEquivLeft_symm_apply` + `Polynomial.aevalTower_C`).

## Junk check (Step 8)
- Used anywhere? Yes, once: `eq_sum_X_none_pow_mul_coeffNone` (Roth/Separation.lean:104), where it evaluates each summand's coefficient before `Finset.sum_ite_eq`.
- Wrapper of 1–2 mathlib calls? No: it needs the `optionEquivLeft`/`rename some` compatibility (proved in place) plus a 7-step `rw` chain and a case split.
- Does mathlib have it? No. `grep` of `.lake/packages/mathlib/Mathlib/` for `rename some` finds only the definition of `optionEquivLeft` (Equiv.lean:469); loogle `MvPolynomial.optionEquivLeft, MvPolynomial.rename` returns only `optionEquivLeft_symm_apply`, `degreeOf_eq_natDegree`, `finSuccEquiv_rename_finSuccEquiv`; leansearch for the statement returns `optionEquivLeft_coeff_some_coeff_none`, `optionEquivLeft_coeff_coeff`, `coeff_monomial`, `coeff_X'` — ingredients, not the result. No `coeff_X_pow_mul`-style lemma in `Mathlib/Algebra/MvPolynomial/`.
- Too specific / inline? Inlining into `eq_sum_X_none_pow_mul_coeffNone` would replace a clean `simp_rw` by a 12-line block under a binder (the use is inside a `Finset.sum`, which is why it is a rewrite lemma); separate helper is the right factoring.
- Well-chosen? Yes as a private helper. Minor improvement: extract the shared fact `optionEquivLeft R τ (rename some Q) = Polynomial.C Q` (duplicated in `coeff_rename_mul_aeval`) as its own lemma; that would shorten both proofs and is a natural mathlib simp lemma (`optionEquivLeft_rename_some`) for Mathlib/Algebra/MvPolynomial/Equiv.lean.
- Conclusion: `KEEP` — action: keep as private helper for l.104; optionally factor out the duplicated `optionEquivLeft (rename some Q) = C Q` step.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:64).

Note: if the parent material (`coeffNone`, `eq_sum_X_none_pow_mul_coeffNone`) is upstreamed, this would travel with it; the more reusable piece is the missing mathlib lemma `optionEquivLeft R σ (rename some p) = Polynomial.C p`.

## Evidence
- `grep -rn coeff_X_none_pow_mul_rename Roth/`: definition l.64, single use l.104.
- `grep -rn "rename some" .lake/packages/mathlib/Mathlib/`: only Equiv.lean:469 (definition of `optionEquivLeft`); `grep` of `optionEquivLeft` theorems in Equiv.lean: `optionEquivLeft_X_some/X_none/C/monomial`, `optionEquivLeft_coeff_some_coeff_none` (l.509), `optionEquivLeft_coeff_coeff` (l.610), none about `rename`.
- `lean_loogle "MvPolynomial.optionEquivLeft, MvPolynomial.rename"`: 3 results, none the statement or the rename-some compatibility.
- `lean_leansearch` (query: coefficient of X none ^ n times rename some Q): ingredients only (listed above).
- No Lean runs and no evidence Lean files (private SKIP; project builds clean so the lemma compiles as stated).
