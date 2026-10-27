---
decl: Roth.exists_rat_factors_det_hasseDeriv_aux
file: Roth/Separation.lean
line: 510
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private rational half of Lemma 2 (the Hasse-derivative determinant of a nonzero integer P factors over Q as U(x_tau) V(x_none) with nonzero factors), used once in exists_det_eq_mul; no mathlib counterpart (mathlib has no multivariate Hasse derivative or generalized Wronskian).
action: Keep as private helper for its single call site Roth/Separation.lean:551 (exists_det_eq_mul); inlining would add ~22 lines to Lemma 2 and blur the Q-factorisation / Z-integrality split.
---

# Roth.exists_rat_factors_det_hasseDeriv_aux

## Inventory entry

### `theorem Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Type**: `∀ {τ : Type*} [Finite τ] {P : MvPolynomial (Option τ) ℤ}, P ≠ 0 → ∀ {n : ℕ}, degreeOf none P ≤ n → ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℚ) (V : Polynomial ℚ), U ≠ 0 ∧ V ≠ 0 ∧ map (Int.castRingHom ℚ) (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) P).det = rename some U * Polynomial.aeval (X none) V`
- **What**: Rational form of Roth's Lemma 2. For a nonzero integer polynomial P in the variables x_τ and x_none with degree at most n in x_none, there are 1 ≤ l ≤ n + 1 and differential operators Δ_μ (multi-indices D μ in the x_τ variables of order at most μ) such that the l×l determinant det(Δ_μ ∂_{x_none}^ν P / ν!) (Hasse derivatives), viewed over ℚ, factors as U(x_τ) V(x_none) with U, V nonzero.
- **How**: Map P to ℚ (PQ); transfer the degree bound via `degrees_map_of_injective`; obtain a separated representation PQ = Σ_ν φ_ν(x_none) ψ_ν(x_τ) with both families linearly independent from `exists_separated_representation` (nonvanishing of PQ via `MvPolynomial.map_injective` + `Int.cast_injective`); choose D with generalized Wronskian of ψ nonzero by `exists_genWronskian_ne_zero` (Lemma 1); rewrite the mapped determinant via `RingHom.map_det`, `hasseDeriv_map` and `det_hasseDeriv_separated` into `rename some (genWronskian D ψ) * aeval (X none) (wronskian φ)`; nonvanishing of V by `wronskian_ne_zero_of_linearIndependent`.
- **Hypotheses**: `[Finite τ]` (needed by `exists_genWronskian_ne_zero`); `hP : P ≠ 0`; `hn : degreeOf none P ≤ n`. Section variables `[Fintype τ] [DecidableEq τ]` omitted (`omit ... in`). All hypotheses used.
- **Uses from project**: `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `Roth.exists_separated_representation` (Roth/Separation.lean:325), `Roth.det_hasseDeriv_separated` (Roth/Separation.lean:351), `Roth.exists_genWronskian_ne_zero` (Roth/GenWronskian.lean:254), `Roth.genWronskian` (Roth/GenWronskian.lean:32), `Roth.wronskian` (Roth/Wronskian.lean:60), `Roth.wronskian_ne_zero_of_linearIndependent` (Roth/Wronskian.lean:205)
- **Used by**: Roth/Separation.lean: `exists_det_eq_mul` (Lemma 2, l.542; call at l.551 `exists_rat_factors_det_hasseDeriv_aux hP (hr none)`). `grep -rn exists_rat_factors_det_hasseDeriv_aux Roth/` gives only the definition (l.510) and this use. Transitively everything downstream of Lemma 2.
- **Visibility**: private
- **Lines**: 510–534 (with `omit` line 509), proof length 19 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). The existential conclusion is the full Lemma 2 shape minus integrality and degree bounds; the witnesses are U = genWronskian D ψ and V = wronskian φ, but these are hidden behind the existential, which is fine because exists_det_eq_mul only needs nonvanishing plus the factorisation. No docstring (private helper).

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_det_eq_mul` (Roth/Separation.lean:551).
- Wrapper of 1–2 mathlib calls? No. It composes four substantive project results (separated representation, Lemma 1 on generalized Wronskians, the determinant factorisation `det_hasseDeriv_separated`, Wronskian nonvanishing) with a mathlib-level transfer from ℤ to ℚ.
- Does mathlib have it? No. Mathlib has only univariate `Polynomial.hasseDeriv` (Mathlib/Algebra/Polynomial/HasseDeriv.lean); no multivariate Hasse derivative, no (generalized) Wronskian determinant factorisation. `lean_leansearch` for the statement returned only unrelated items (`Matrix.det_mvPolynomialX_ne_zero`, `Polynomial.hasseDeriv`, `Polynomial.hasseDeriv_mul`, `Matrix.det_matrixOfPolynomials`).
- Too specific / inline? It is specific to Lemma 2, but it cleanly isolates the rational-factorisation step from the integrality step (`exists_int_factors`) and degree bounds in `exists_det_eq_mul`. Inlining would make `exists_det_eq_mul` ~35 lines and mix the ℚ and ℤ worlds; keeping the split is the better structure.
- Well-chosen? Yes. Minor possible golf (not required): the `hdeg` transfer could use a `degreeOf`-level map lemma, but mathlib has no `degreeOf_map_of_injective` (grep finds only `degreeOf_rename_of_injective`), so the current `degrees_map_of_injective` route is appropriate.
- Conclusion: `KEEP` — action: keep as private helper for `exists_det_eq_mul`; no change needed.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:510). The Step 9a pre-filter also fires on the name suffix `_aux`.

Note for the parent: if Roth's Lemma 2 (`exists_det_eq_mul`) or the multivariate Hasse-derivative API is ever upstreamed, this step would travel with it as a private helper; it has no standalone mathlib value.

## Evidence
- `grep -rn exists_rat_factors_det_hasseDeriv_aux Roth/`: definition l.510, single use l.551.
- grep of definitions of each project identifier in the body (locations listed under Uses from project).
- `grep -rn "theorem degreeOf_map"` over mathlib: no hits (only `degreeOf_rename_of_injective` in Mathlib/Algebra/MvPolynomial/Degrees.lean:419).
- `grep` for `MvPolynomial.hasseDeriv` in mathlib MvPolynomial dirs: no hits.
- `lean_leansearch` (statement query, 6 results): none matches.
- `lean_local_search` unavailable (ripgrep not on PATH); replaced by direct grep.
- No Lean runs and no evidence Lean files (private SKIP; project builds clean so the lemma compiles as stated).
