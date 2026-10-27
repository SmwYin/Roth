---
decl: Roth.boxFamily_eq_image_finsupp_aux
file: Roth/MainLemma.lean
line: 280
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private set identity rewriting boxFamily r B as the ofCoeff-image of Finset.finsupp over the monomial box Iic r with coefficient range Icc 0 B; shared step of boxFamily_finite and ncard_boxFamily, with no mathlib counterpart (mathlib's univariate ncard_boxPoly uses an ad hoc toFn/ofFn bijection instead).
action: Keep as private helper for boxFamily_finite (Roth/MainLemma.lean:304) and ncard_boxFamily (Roth/MainLemma.lean:313); optionally turn the plain comment at l.278 into an accurate docstring and drop the redundant `classical` at l.284; revisit only if a multivariate boxPoly generalisation is upstreamed (then this becomes its card/finite proof step).
---

# Roth.boxFamily_eq_image_finsupp_aux

## Inventory entry

### `theorem Roth.boxFamily_eq_image_finsupp_aux`
- **Type**: `∀ {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ), boxFamily r B = AddMonoidAlgebra.ofCoeff '' ↑((Finset.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))).finsupp fun _ ↦ Finset.Icc (0 : ℤ) B)` (declared `private lemma` under `open scoped Classical in`; the image lives in `Set ((σ →₀ ℕ) →₀ ℤ)` coerced to `MvPolynomial σ ℤ`).
- **What**: The box family (integer polynomials with `degreeOf j W ≤ r j` for all `j` and all coefficients in `[0, B]`) equals the set of polynomials whose coefficient function is a finitely supported map supported in the monomial box `{d : d ≤ r}` (as `Finset.Iic` of `r` viewed as a finsupp) with values in `Icc 0 B`; i.e. the box family is the image of the finite set `Finset.finsupp (Iic r) (fun _ ↦ Icc 0 B)` under the coefficient-to-polynomial map.
- **How**: `ext W`, two directions. (→) witness `W.coeff`; membership via `Finset.mem_finsupp_iff`, support condition from `MvPolynomial.monomial_le_degreeOf` composed with the degree bound and `Finset.mem_Iic`, value condition from `Finset.mem_Icc`. (←) from `Finset.mem_finsupp_iff` get support and value conditions; degree bound by `MvPolynomial.degreeOf_le_iff`; coefficient bound by case split on `d ∈ Iic r`, using `Finset.mem_Icc` inside and `Finsupp.notMem_support_iff` (coefficient zero) outside.
- **Hypotheses**: `[Finite (Function.support r)]` is needed to form `Finsupp.ofSupportFinite r` and hence the finite box `Finset.Iic`; without it `boxFamily r B` can be infinite (e.g. `σ = ℕ`, `r = 1`, `B = 1`), so no finset image exists. No other hypotheses. All used.
- **Uses from project**: `Roth.boxFamily` (Roth/MainLemma.lean:275).
- **Used by**: Roth/MainLemma.lean only: `Roth.boxFamily_finite` (l.304, `rw`) and `Roth.ncard_boxFamily` (l.313, `rw` before `Set.ncard_image_of_injective` / `Finset.card_finsupp`). `grep -rn boxFamily_eq_image_finsupp_aux Roth/` returns only the declaration and these two uses.
- **Visibility**: private
- **Lines**: 280–298 (statement 280–283), proof length 15 lines (284–298)
- **Notes**: Name ends in `_aux` (would also trigger the Step 9a pre-filter). The preceding comment at l.278 is a plain `/- ... -/` comment, not a docstring, and its text ("The polynomial with coefficient `c d` at each monomial `d` of the box") describes the image map rather than the lemma. `classical` at l.284 is redundant given `open scoped Classical in` on the declaration (style nit only).

## Junk check (Step 8)
- Used anywhere? Yes, twice: the finiteness lemma `boxFamily_finite` and the counting lemma `ncard_boxFamily` both start by rewriting with it.
- Wrapper of 1–2 mathlib calls? No: a 15-line two-direction set extensionality combining `Finset.mem_finsupp_iff`, `monomial_le_degreeOf`, `degreeOf_le_iff` and `Finsupp.notMem_support_iff`.
- Does mathlib have it? No. `boxFamily` itself is project-local (see the `Roth.boxFamily` report: a composition of `MvPolynomial.restrictSupport` with a coefficient box). Mathlib's univariate analogue `Polynomial.boxPoly` / `Polynomial.ncard_boxPoly` (Mathlib/NumberTheory/MahlerMeasure.lean:55–57) proves its count by a direct `Set.ncard_congr'` bijection with `Finset.Icc` in `Fin (n+1) → ℤ` via `toFn`/`ofFn`, with no image-of-`Finset.finsupp` lemma. `Finset.finsupp`, `Finset.mem_finsupp_iff`, `Finset.card_finsupp` exist (Mathlib/Data/Finset/Finsupp.lean:46–78) but nothing identifies a coefficient-bounded `restrictSupport` set with them; grep for finiteness of `restrictSupport` sets found nothing.
- Too specific / inline? Shared by two public lemmas, so inlining would duplicate the 15-line proof; keeping it as one private lemma is the right factoring.
- Well-chosen? Yes: the image-of-a-finset form gives finiteness (`Finset.finite_toSet.image`) and cardinality (`ncard_image_of_injective` + `card_finsupp`) in one stroke.
- Conclusion: `KEEP`. Action: none required; optional polish: replace the l.278 comment with an accurate docstring and drop the redundant `classical`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:280); additionally the name ends in `_aux`.

Side note: any upstreaming should target a multivariate generalisation of `Polynomial.boxPoly` / `ncard_boxPoly` (polynomials supported in a finite set of monomials with coefficients in per-monomial intervals), as recommended in the `Roth.boxFamily` report; this lemma would then be the natural proof step of its finiteness and cardinality results.

## Evidence
- `grep -rn boxFamily_eq_image_finsupp_aux Roth/`: declaration l.280, uses l.304 (`boxFamily_finite`) and l.313 (`ncard_boxFamily`).
- Read Roth/MainLemma.lean l.270–320 (the declaration, `boxFamily`, `boxFamily_finite`, `ncard_boxFamily`).
- Read Mathlib/NumberTheory/MahlerMeasure.lean l.49–70: `boxPoly`, `ncard_boxPoly` proved by `Set.ncard_congr'` with `toFn`/`ofFn`, no finsupp-image lemma.
- `grep` in Mathlib/Data/Finset/Finsupp.lean: `Finset.finsupp` (l.46), `mem_finsupp_iff` (l.49), `card_finsupp` (l.78) exist, used here as building blocks.
- `grep -rn "Finite.*restrictSupport|restrictSupport.*Finite"` over Mathlib: no hits.
- Consulted `.mathlib-quality/overview/mathlibable/Roth.boxFamily.md` (parent def, NO-composable-from-mathlib).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
