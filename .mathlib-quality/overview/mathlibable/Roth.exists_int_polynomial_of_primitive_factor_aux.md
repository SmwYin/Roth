---
decl: Roth.exists_int_polynomial_of_primitive_factor_aux
file: Roth/Separation.lean
line: 466
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private separated-variables Gauss-lemma step (primitive integral U and integral F = U(x_tau) V'(x_none) force V' integral) used once in exists_int_factors; mathlib's Gauss lemma is univariate and needs both factors primitive, so it does not cover this.
action: Keep as private helper for its single call site Roth/Separation.lean:493 (exists_int_factors); no change needed.
---

# Roth.exists_int_polynomial_of_primitive_factor_aux

## Inventory entry

### `theorem Roth.exists_int_polynomial_of_primitive_factor_aux`
- **Type**: `∀ {τ : Type u_1} {U : MvPolynomial τ ℤ} {V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ}, U.support.gcd ⇑U.coeff = 1 → map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) * Polynomial.aeval (X none) V' → ∃ V : Polynomial ℤ, Polynomial.map (Int.castRingHom ℚ) V = V'`
- **What**: Integrality of the second factor in a separated factorisation. If U is an integral polynomial in the variables x_τ whose coefficients have gcd 1, and the integral polynomial F in x_τ, x_none equals U(x_τ) V'(x_none) over ℚ, then V' has integral coefficients. (Coefficient of x^a x_none^b in F is u_a v_b; primitivity of U gives an integral combination of the u_a equal to 1.)
- **How**: Reduces via `Polynomial.mem_map_range (Int.castRingHom ℚ)` to showing each coefficient `V'.coeff b` lies in the range of the cast; for each b applies the project lemma `exists_int_eq_of_gcd_eq_one hgcd` with witness `F.coeff (a.mapDomain some + Finsupp.single none b)`, obtained by taking that coefficient of `hF` and simplifying with the project lemma `coeff_rename_mul_aeval` and `MvPolynomial.coeff_map`.
- **Hypotheses**: `hgcd : U.support.gcd U.coeff = 1` (primitivity of U); `hF` the rational factorisation of the integral F. Section variables `[Fintype τ] [DecidableEq τ]` are omitted (`omit ... in`). No nonvanishing hypotheses are needed (all used).
- **Uses from project**: `Roth.exists_int_eq_of_gcd_eq_one` (Roth/Separation.lean:443), `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:123). Mathlib: `Polynomial.mem_map_range`, `MvPolynomial.coeff_map`.
- **Used by**: Roth/Separation.lean: `exists_int_factors` (l.493, `obtain ⟨V, hVmap⟩ := exists_int_polynomial_of_primitive_factor_aux hgcd hF'`). `grep -rn exists_int_polynomial_of_primitive_factor_aux Roth/` gives only the definition (l.466) and that use. Transitively: `exists_det_eq_mul` (Lemma 2) and downstream.
- **Visibility**: private
- **Lines**: 466–478 (with `omit` line 465), proof length 9 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). Consumes the output `hF'` of `rescale_separated_factor_aux`. This is the mathematical heart of the "U, V integral" step of the source's proof of Lemma 2 (§2), the local Gauss-lemma argument specialised to separated variables. No docstring (private helper).

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_int_factors` (Roth/Separation.lean:493).
- Wrapper of 1–2 mathlib calls? No: combines `Polynomial.mem_map_range` with two project lemmas and a coefficient computation; genuine (if small) mathematical content.
- Does mathlib have it? No. `lean_leansearch` ("if a primitive integer polynomial times a rational polynomial has integer coefficients then the rational polynomial has integer coefficients") returns `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`, `IsPrimitive.dvd_primPart_iff_dvd`, `primPart_mul`, `IsPrimitive.mul`, `isIntegral_coeff_prod`: all univariate and requiring both polynomials primitive (or phrased as divisibility of integral polynomials), not the separated multivariate shape with a rational V'. Mathlib has no multivariate content / Gauss lemma for `MvPolynomial` stated this way.
- Too specific / inline? Specific to `exists_int_factors`, but inlining would add ~9 lines plus a long `have` statement to an already long proof; the split mirrors the source's argument and keeps the caller readable.
- Well-chosen? Yes. Hypotheses are minimal (no nonzero assumptions), statement uses `rename some`/`aeval (X none)` consistently with the rest of the file.
- Conclusion: `KEEP` — action: keep as private helper for `exists_int_factors`; no change needed.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:466). The Step 9a pre-filter also fires on the name suffix `_aux`.

Note for the parent: if `exists_int_factors` is ever upstreamed, the natural mathlib form of this step would be a multivariate Gauss-lemma statement (content of a product over a GCD domain), of which this is the separated-variables special case.

## Evidence
- `grep -rn exists_int_polynomial_of_primitive_factor_aux Roth/`: definition l.466, single use l.493.
- `grep -rn "coeff_rename_mul_aeval\|theorem exists_int_eq_of_gcd_eq_one" Roth/`: project deps at Roth/Separation.lean:123 and :443.
- `lean_hover_info` at Roth/Separation.lean:466: full type recorded above, no diagnostics.
- `grep` in mathlib for `mem_map_range` (Mathlib/Algebra/Polynomial/Eval/Subring.lean:49) and Gauss-lemma API (Mathlib/RingTheory/Polynomial/GaussLemma.lean:324, Content.lean:215): univariate only.
- `lean_leansearch` (query above, 6 results): none matches the statement.
- No Lean runs and no evidence Lean files (no experiments needed for a private SKIP; the project builds clean).
