---
decl: Roth.isPrimitive_pow
file: Roth/Theta.lean
line: 175
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 2-line helper saying a power of a primitive polynomial in Z[X] is primitive; a direct Nat.rec over mathlib Polynomial.IsPrimitive.mul, and mathlib has no IsPrimitive.pow or content_pow lemma (checked by grep and loogle); used once.
action: Keep as private helper for its single call site Roth/Theta.lean:196 (exists_eq_pow_mul_of_rootMultiplicity); if ever upstreamed, the NormalizedGCDMonoid form (compiled in evidence) belongs next to IsPrimitive.mul in Mathlib/RingTheory/Polynomial/Content.lean.
---

# Roth.isPrimitive_pow

## Inventory entry

### `theorem Roth.isPrimitive_pow`
- **Type**: `∀ {p : Polynomial ℤ}, p.IsPrimitive → ∀ (t : ℕ), (p ^ t).IsPrimitive`
- **What**: Every natural power of a primitive integer polynomial is primitive (the t-fold form of Gauss's lemma on products).
- **How**: Induction on `t` via `Nat.rec`: base case `Polynomial.isPrimitive_one` (since `p ^ 0 = 1`), step `simpa [pow_succ] using ih.mul hp` with mathlib's `Polynomial.IsPrimitive.mul` (Mathlib/RingTheory/Polynomial/Content.lean:373).
- **Hypotheses**: `hp : p.IsPrimitive`; `t : ℕ` explicit. No hypothesis is superfluous; the base ring ℤ is more specific than needed (any `CommRing` with `NormalizedGCDMonoid` works, see Evidence).
- **Uses from project**: `[]` (only mathlib: `Polynomial.isPrimitive_one`, `Polynomial.IsPrimitive.mul`, `pow_succ`)
- **Used by**: Roth/Theta.lean:196 `exists_eq_pow_mul_of_rootMultiplicity` (as `isPrimitive_pow (isPrimitive_linear hcop) t`, the primitivity input to `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`) only; `grep -rn isPrimitive_pow Roth/` gives the definition (l.175) and that use. Transitively `pow_rootMultiplicity_le` (Roth/Theta.lean:206) and the §5 Lemma 5 chain.
- **Visibility**: private
- **Lines**: 175–177, proof length 1 line (term-mode `Nat.rec`)
- **Notes**: Declared `private lemma` (kind recorded as theorem) inside `section Lemma5`. Implements "(q_1 x_1 − h_1)^t is primitive" from the source's Gauss-lemma argument (§5, proof of Lemma 5), together with `isPrimitive_linear`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_eq_pow_mul_of_rootMultiplicity` (Roth/Theta.lean:196).
- Wrapper of 1–2 mathlib calls? Yes: an induction over `Polynomial.IsPrimitive.mul` with base `Polynomial.isPrimitive_one`. That is the natural shape of a `pow` corollary of a `mul` lemma.
- Does mathlib have it? No. Checked: `grep -rnE "(theorem|lemma) .*(IsPrimitive\.mul|IsPrimitive\.pow|IsPrimitive\.prod|isPrimitive_pow|isPrimitive_prod|content_pow)"` over `.lake/packages/mathlib/Mathlib` finds only `IsPrimitive.mul` (Content.lean:373) and `IsPrimitive.mul_map_mem_lifts_iff` (GaussLemma.lean:238, unrelated); no `IsPrimitive.pow`, `IsPrimitive.prod`, `content_pow`, or a primitive-polynomials submonoid. `lean_loogle "Polynomial.IsPrimitive (_ ^ _)"`: no results. The closest mathlib route is `isPrimitive_iff_content_eq_one` + `content_mul` (ℤ is a `StrongNormalizedGCDMonoid`) by induction (compiled, evidence (3)), which is longer than the current proof. `Monic.isPrimitive` does not apply (q X − h is not monic for q ≠ 1).
- Too specific / inline? Could be inlined at l.196 as a `have` (one line), but a named helper is clearer and costs nothing; inlining would gain nothing.
- Well-chosen? Yes for a private helper. Specialised to ℤ only because the call site is; the general `NormalizedGCDMonoid` statement compiles with the same proof.
- Conclusion: `KEEP` — action: keep as private helper for Roth/Theta.lean:196; nothing in mathlib replaces it.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:175).

Note: this is a genuine (small) mathlib gap. If upstreamed, the form `theorem Polynomial.IsPrimitive.pow {R} [CommRing R] [NormalizedGCDMonoid R] {p : R[X]} (hp : p.IsPrimitive) (n : ℕ) : (p ^ n).IsPrimitive` (compiled, evidence (2)) would go right after `IsPrimitive.mul` in Mathlib/RingTheory/Polynomial/Content.lean, ideally with an `IsPrimitive.prod` companion and `content_pow` for `StrongNormalizedGCDMonoid`.

## Evidence
- `grep -rn "isPrimitive_pow" Roth/`: definition l.175, single use l.196.
- mathlib grep (pattern in junk check): only `Polynomial.IsPrimitive.mul` exists; no pow/prod/content_pow lemma. `grep content_pow` / `contentHom` over mathlib: no hits.
- `lean_loogle "Polynomial.IsPrimitive (_ ^ _)"`: empty.
- Evidence file `.mathlib-quality/overview/evidence/Roth.isPrimitive_pow/mathlib_routes.lean` (imports only `Mathlib.RingTheory.Polynomial.Content`), compiled clean with `lake env lean` (no errors or warnings, after replacing one `simpa using isPrimitive_one` by `simp` per the unnecessarySimpa linter): (1) project statement with the project proof; (2) generalisation to any `CommRing R` with `NormalizedGCDMonoid R`; (3) alternative route via `isPrimitive_iff_content_eq_one` + `content_mul` + `IsPrimitive.content_eq_one`.
