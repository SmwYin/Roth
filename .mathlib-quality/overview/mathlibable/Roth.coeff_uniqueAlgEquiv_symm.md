---
decl: Roth.coeff_uniqueAlgEquiv_symm
file: Roth/Separation.lean
line: 169
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Unused anywhere in the project and merely the d = single default n instance of mathlib's MvPolynomial.coeff_uniqueAlgEquiv_symm (proof is that lemma plus Finsupp.single_eq_same); it also reuses mathlib's short name inside namespace Roth, so every caller already writes MvPolynomial.coeff_uniqueAlgEquiv_symm explicitly.
action: Delete the theorem at Roth/Separation.lean:169-171 (no call sites; the uses at Separation.lean:179, 182 and Theta.lean:429 already cite MvPolynomial.coeff_uniqueAlgEquiv_symm); no mathlib PR.
---

# Roth.coeff_uniqueAlgEquiv_symm

## Inventory entry

### `theorem Roth.coeff_uniqueAlgEquiv_symm`
- **Type**: `∀ {R : Type*} [CommSemiring R] {σ : Type*} [Unique σ] (f : Polynomial R) (n : ℕ), ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n`
- **What**: Viewing a univariate polynomial `f` as a polynomial in one variable indexed by a singleton type `σ`, the coefficient of the monomial `x^n` is the `n`-th coefficient of `f`.
- **How**: `rw [MvPolynomial.coeff_uniqueAlgEquiv_symm, Finsupp.single_eq_same]` -- mathlib's lemma gives `f.coeff ((single default n) default)`, which evaluates to `f.coeff n`.
- **Hypotheses**: `R` a commutative semiring, `σ` with `[Unique σ]`; no others.
- **Uses from project**: `[]`
- **Used by**: unused in project (`grep -rn coeff_uniqueAlgEquiv_symm Roth/` finds only the declaration itself and three uses that are explicitly qualified `MvPolynomial.coeff_uniqueAlgEquiv_symm`: Roth/Separation.lean:179, Roth/Separation.lean:182, Roth/Theta.lean:429)
- **Visibility**: public
- **Lines**: 169-171, proof length 1 line
- **Notes**: Same short name as mathlib's `MvPolynomial.coeff_uniqueAlgEquiv_symm` (Mathlib/Algebra/MvPolynomial/Equiv.lean:115). Inside `namespace Roth` that invites ambiguity, which is presumably why all callers spell out the `MvPolynomial.` prefix. The docstring cites Source §5, proof of Lemma 6, but the only use for that lemma (Theta.lean:429) calls the mathlib lemma directly.

## Junk check (Step 8)
- Used anywhere? No. Zero call sites project-wide (all occurrences of the name resolve to the mathlib lemma via explicit qualification).
- Wrapper of 1-2 mathlib calls? Yes: one `rw` of `MvPolynomial.coeff_uniqueAlgEquiv_symm` plus `Finsupp.single_eq_same`.
- Does mathlib have it? Effectively yes. Mathlib's `MvPolynomial.coeff_uniqueAlgEquiv_symm (P : Polynomial R) (d : σ →₀ ℕ) : ((uniqueAlgEquiv R σ).symm P).coeff d = P.coeff (d default)` is strictly more general (arbitrary `d`); the project lemma is its `d := Finsupp.single default n` instance. (Mathlib's lemma does not need the `single` form because on a `Unique` index every `d` equals `single default (d default)`, cf. `Finsupp.unique_single`.)
- Too specific? Yes. It is an instance of a mathlib lemma, and it is not used.
- Well-chosen definition? n/a (theorem).
- **Conclusion: `REMOVE`.** Delete Roth/Separation.lean:169-171. Nothing has to be migrated because no caller references it.

## Mathlibable assessment (Step 9)
Skip reason: Step 8 said REMOVE (unused; it is the `d = Finsupp.single default n` specialisation of mathlib's `MvPolynomial.coeff_uniqueAlgEquiv_symm` in Mathlib/Algebra/MvPolynomial/Equiv.lean:115, so mathlib already has the general form and nothing here should be upstreamed).

Not INHERITED: this is not a glue lemma about a project definition. `uniqueAlgEquiv` is a mathlib definition, and the related assessed report MvPolynomial.uniqueAlgEquiv_hasseDeriv.md concerns a different statement (the Hasse-derivative bridge).

## Evidence
- `grep -rn "uniqueAlgEquiv\|pUnitAlgEquiv" .lake/packages/mathlib/Mathlib/` found `MvPolynomial.coeff_uniqueAlgEquiv_symm` (Equiv.lean:115), `coeff_uniqueAlgEquiv` (Equiv.lean:103) and `uniqueAlgEquiv_symm_monomial` (Equiv.lean:96). `pUnitAlgEquiv` is deprecated (2026-04-15) in favour of `uniqueAlgEquiv`.
- `grep -rn coeff_uniqueAlgEquiv_symm Roth/ Roth.lean` turned up no unqualified (that is, `Roth.`) uses.
- Evidence file `.mathlib-quality/overview/evidence/Roth.coeff_uniqueAlgEquiv_symm/specialisation.lean` (imports only `Mathlib.Algebra.MvPolynomial.Equiv`, with no Roth import) proves the statement both by `rw [MvPolynomial.coeff_uniqueAlgEquiv_symm, Finsupp.single_eq_same]` and as a term `(MvPolynomial.coeff_uniqueAlgEquiv_symm R f _).trans ...`. It was checked with `lean_run_code` and compiles with no diagnostics. (An earlier try with plain `simp [MvPolynomial.coeff_uniqueAlgEquiv_symm]` failed because simp unfolds `symm` to `eval₂` first. That is recorded in the file's comment and is why the file uses `rw`.)
