---
decl: Roth.isPrimitive_linear
file: Roth/Theta.lean
line: 167
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 6-line helper showing q X - h in Z[X] is primitive when h and q are coprime; mathlib has no direct lemma (only Monic.isPrimitive, isPrimitive_iff_content_eq_one and the Irreducible.isPrimitive plus irreducible_C_mul_X_add_C route, which needs the extra hypothesis q ne 0); used once.
action: Keep as private helper for its single call site Roth/Theta.lean:196 (exists_eq_pow_mul_of_rootMultiplicity); optional cosmetic generalisation to any CommRing with C a * X + C b (compiled in evidence) only if the lemma is ever upstreamed to Mathlib/RingTheory/Polynomial/Content.lean.
---

# Roth.isPrimitive_linear

## Inventory entry

### `theorem Roth.isPrimitive_linear`
- **Type**: `∀ {h : ℤ} {q : ℕ}, IsCoprime h (q : ℤ) → (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h).IsPrimitive`
- **What**: If the integers h and q are coprime, the linear integer polynomial q·X − h is primitive, i.e. its only constant divisors in ℤ[X] are units.
- **How**: Unfolds `IsPrimitive` (`intro c hc`), turns `C c ∣ p` into divisibility of every coefficient by `Polynomial.C_dvd_iff_dvd_coeff`, then applies `IsCoprime.isUnit_of_dvd'` to c ∣ coeff 0 = −h (`simpa`) and c ∣ coeff 1 = q (`simpa only [Polynomial.coeff_sub, Polynomial.coeff_C_mul, Polynomial.coeff_X_one, Polynomial.coeff_C, ...]`).
- **Hypotheses**: `hcop : IsCoprime h (q : ℤ)`. No positivity of q is needed (q = 0 forces h to be a unit, still primitive).
- **Uses from project**: `[]` (only mathlib lemmas)
- **Used by**: Roth/Theta.lean:196 `exists_eq_pow_mul_of_rootMultiplicity` (as `isPrimitive_pow (isPrimitive_linear hcop) t`, feeding `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`) only; `grep -rn isPrimitive_linear Roth/` gives the definition (l.167) and that use. Transitively `pow_rootMultiplicity_le` (Roth/Theta.lean:206, uses it at l.209) and the §5 Lemma 5 chain downstream.
- **Visibility**: private
- **Lines**: 167–173, proof length 6 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem) inside `section Lemma5`. Implements the "(q_1 x_1 − h_1) is primitive" step of the source's Gauss-lemma argument (§5, proof of Lemma 5).

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_eq_pow_mul_of_rootMultiplicity` (Roth/Theta.lean:196).
- Wrapper of 1–2 mathlib calls? Close to it but not literally: `C_dvd_iff_dvd_coeff` + `IsCoprime.isUnit_of_dvd'` plus two coefficient `simp` computations (6 lines).
- Does mathlib have it? No direct lemma. Checked the whole `Polynomial.IsPrimitive` API (grep of `.lake/packages/mathlib/Mathlib` for `IsPrimitive` theorems; Mathlib/RingTheory/Polynomial/Content.lean, ContentIdeal.lean, GaussLemma.lean): `isPrimitive_iff_isUnit_of_C_dvd`, `isPrimitive_one`, `Monic.isPrimitive` (not applicable: q X − h is not monic unless q = 1), `isPrimitive_of_dvd`, `Irreducible.isPrimitive`, `isPrimitive_iff_ne_zero` (fields), `isPrimitive_iff_content_eq_one` / `IsPrimitive.content_eq_one` (would require computing `content` of a linear polynomial, no lemma for that), `isPrimitive_iff_contentIdeal_eq_top` (Bézout rings; would require computing `contentIdeal` = span of `coeffs`, no linear-case lemma), `IsPrimitive.mul`, `cyclotomic.isPrimitive`. Loogle `Polynomial.IsPrimitive, Polynomial.X, IsCoprime`: no results. Leansearch ("linear polynomial C a * X + C b is primitive if a and b are coprime") surfaced `Polynomial.irreducible_C_mul_X_add_C` (Mathlib/Algebra/Polynomial/RingDivision.lean:280, needs `a ≠ 0` and `IsRelPrime a b`) and `irreducible_of_degree_eq_one_of_isRelPrime_coeff`. Composing these with `Irreducible.isPrimitive` and `natDegree_linear` gives the statement, but only under the extra hypothesis `q ≠ 0` and in 4 lines (compiled, see Evidence) — no shorter than the current proof and strictly weaker. So mathlib does not cover it as stated.
- Too specific / inline? Inlining is possible (6 lines into a 15-line proof) but the separate helper names a clear mathematical fact and keeps `exists_eq_pow_mul_of_rootMultiplicity` readable; fine as is.
- Well-chosen? Yes for a private helper. The natural mathlib-level statement would be over any `CommRing R`: `IsCoprime a b → (C a * X + C b).IsPrimitive` (compiled with a 3-line proof in the evidence file); this is only relevant if upstreaming.
- Conclusion: `KEEP` — action: keep as private helper for Roth/Theta.lean:196; no replacement available in mathlib without adding a `q ≠ 0` hypothesis.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:167).

Note: if ever upstreamed, the general form `theorem Polynomial.isPrimitive_C_mul_X_add_C {R} [CommRing R] {a b : R} (h : IsCoprime a b) : (C a * X + C b).IsPrimitive` would sit in Mathlib/RingTheory/Polynomial/Content.lean next to `Monic.isPrimitive`; mathlib currently has only the irreducibility analogue `irreducible_C_mul_X_add_C` (domain, `a ≠ 0`, `IsRelPrime`).

## Evidence
- `grep -rn "isPrimitive_linear\|isPrimitive_pow" Roth/`: definition l.167, single use l.196 (inside `exists_eq_pow_mul_of_rootMultiplicity`); `exists_eq_pow_mul_of_rootMultiplicity` used at l.209 by `pow_rootMultiplicity_le`.
- `grep -rnE "(theorem|lemma) [A-Za-z_.]*[iI]sPrimitive"` over mathlib: full `Polynomial.IsPrimitive` API listed in the junk check; no linear/coprime lemma.
- `lean_loogle "Polynomial.IsPrimitive, Polynomial.X, IsCoprime"`: no results. `lean_leansearch` (query above, 6 results): `irreducible_C_mul_X_add_C`, `irreducible_of_degree_eq_one_of_isRelPrime_coeff`, `IsPrimitive`, `isPrimitive_iff_isUnit_of_C_dvd`, `IsPrimitive.mul`, `Monic.isPrimitive`.
- Evidence file `.mathlib-quality/overview/evidence/Roth.isPrimitive_linear/mathlib_routes.lean` (imports only `Mathlib.RingTheory.Polynomial.Content` and `Mathlib.Algebra.Polynomial.RingDivision`), compiled clean with `lake env lean` (second run, after replacing a wrong lemma name with `natDegree_linear`): (1) project statement re-proved; (2) generalisation to any `CommRing R` with `C a * X + C b` and `IsCoprime a b`; (3) mathlib composition route via `irreducible_C_mul_X_add_C` + `Irreducible.isPrimitive` + `natDegree_linear`, requiring the extra hypothesis `q ≠ 0`.
