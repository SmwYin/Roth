---
decl: Roth.rescale_separated_factor_aux
file: Roth/Separation.lean
line: 457
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-step rescaling identity (if U = g U' with g nonzero then rename U' * V'(x_none) = rename U * (g^-1 V')(x_none)) used once in exists_int_factors; mathlib has only the generic pieces (rename is an AlgHom, aeval_C, smul_eq_C_mul).
action: Keep as private helper for its single call site Roth/Separation.lean:492 (exists_int_factors, result hF' reused at l.493 and l.502); optional inline as a have would need the long equation retyped, so not worth it.
---

# Roth.rescale_separated_factor_aux

## Inventory entry

### `theorem Roth.rescale_separated_factor_aux`
- **Type**: `∀ {τ K : Type*} [Field K] {U' U : MvPolynomial τ K} {V' : Polynomial K} {F : MvPolynomial (Option τ) K} {g : K}, g ≠ 0 → U = g • U' → F = rename some U' * Polynomial.aeval (X none) V' → F = rename some U * Polynomial.aeval (X none) (Polynomial.C g⁻¹ * V')`
- **What**: Rescaling of a separated factorisation. If F = U'(x_τ) V'(x_none) and U = g U' with g a nonzero scalar, then F = U(x_τ) (g⁻¹ V')(x_none): the scalar moved into the first factor is compensated by its inverse in the second.
- **How**: A single `rw` chain: substitute `hF`, `hUmap`; `map_mul` and `Polynomial.aeval_C` + `algebraMap_eq` turn `aeval (X none) (C g⁻¹ * V')` into `C g⁻¹ * aeval (X none) V'`; `smul_eq_C_mul`, `map_mul`, `rename_C` turn `rename some (g • U')` into `C g * rename some U'`; then `mul_mul_mul_comm`, `← C_mul`, `mul_inv_cancel₀ hg`, `C_1`, `one_mul`.
- **Hypotheses**: `[Field K]` (only `g⁻¹` with `mul_inv_cancel₀` and commutativity are needed, so a `Semifield` would suffice); `hg : g ≠ 0`; `hUmap : U = g • U'`; `hF` the given factorisation. Section variables `[Fintype τ] [DecidableEq τ]` are omitted (`omit ... in`).
- **Uses from project**: `[]` (only mathlib lemmas: `map_mul`, `Polynomial.aeval_C`, `MvPolynomial.algebraMap_eq`, `MvPolynomial.smul_eq_C_mul`, `MvPolynomial.rename_C`, `mul_mul_mul_comm`, `MvPolynomial.C_mul`, `mul_inv_cancel₀`, `MvPolynomial.C_1`, `one_mul`)
- **Used by**: Roth/Separation.lean: `exists_int_factors` (l.484; `have hF' := rescale_separated_factor_aux hg hUmap hF` at l.492, with `K := ℚ`, `U := map (Int.castRingHom ℚ) U`). `grep -rn rescale_separated_factor_aux Roth/` gives only the definition (l.457) and that use. Transitively: `exists_det_eq_mul` (Lemma 2, l.540) and downstream.
- **Visibility**: private
- **Lines**: 457–463 (with `omit` line 456), proof length 2 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). The output `hF'` is consumed twice in `exists_int_factors`: by `exists_int_polynomial_of_primitive_factor_aux` (l.493) and in the `map_injective` rewrite (l.502). Generic over a field K although only instantiated at ℚ.

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_int_factors` (Roth/Separation.lean:492).
- Wrapper of 1–2 mathlib calls? Not literally: a ~13-rewrite chain combining `aeval_C`, `smul_eq_C_mul`, `rename_C` and cancellation of `g * g⁻¹`. It is a bookkeeping identity with no mathematical content beyond that.
- Does mathlib have it? No. `lean_leansearch` ("rename of scalar multiple of multivariate polynomial equals scalar multiple of rename") returns only `MvPolynomial.rename` (an `AlgHom`, so `map_smul` applies), `rename_X`, `rename_rename`, `renameEquiv`; grep for `rename_smul` / `smul_rename` in mathlib's `Algebra/MvPolynomial` finds nothing named that (the fact is covered by `map_smul` for the AlgHom). No lemma about rescaling the factors of `rename some U * aeval (X none) V`; it is too specific for mathlib.
- Too specific / inline? It is specific to this proof, but inlining at l.492 would require restating the long equation `map (Int.castRingHom ℚ) F = rename some (map _ U) * Polynomial.aeval (X none) (C g⁻¹ * V')` as a `have` type (the result is used twice), which is longer than the current helper call. Keeping it separate keeps `exists_int_factors` readable.
- Well-chosen? Yes as a private helper; the generic field `K` makes the statement cleaner than a ℚ-specific one. Minor: could take `[Semifield K]`, irrelevant for a private helper.
- Conclusion: `KEEP` — action: keep as private helper for `exists_int_factors`; no change needed.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:457). The Step 9a pre-filter also fires on the name suffix `_aux`.

Note for the parent: if `exists_int_factors` (Gauss-lemma-style integrality of a separated factorisation) is ever upstreamed, this identity would go along as a private step or be replaced by an inline `rw`/`simp` with `map_smul`, `Polynomial.aeval_C`, `smul_eq_C_mul`.

## Evidence
- `grep -rn rescale_separated_factor_aux Roth/`: definition l.457, single use l.492.
- `grep -rn "rename_smul\|theorem smul_rename\|aeval_C_mul\b"` over mathlib `Algebra/MvPolynomial` and `Algebra/Polynomial`: no hits.
- `lean_leansearch` (query above, 6 results): `MvPolynomial.rename`, `renameEquiv_apply`, `renameEquiv`, `rename_X`, `eval₂_cast_comp`, `rename_rename` — none is the statement.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
