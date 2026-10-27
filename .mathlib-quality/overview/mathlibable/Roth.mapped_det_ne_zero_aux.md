---
decl: Roth.mapped_det_ne_zero_aux
file: Roth/Theta.lean
line: 511
kind: lemma
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private helper (Step 9a SKIP) transporting the integer factorisation F = U(x_tau) V(x_p) of the Lemma 6 determinant to nonvanishing of the real determinant; used once in index_le_lem6, a short composition of mathlib injectivity lemmas, Roth-specific in shape.
action: Keep at Roth/Theta.lean:510-529 (sole call site Roth/Theta.lean:576 in index_le_lem6); optional golf verified by lean_multi_attempt - replace the last two lines (528-529) by exact (map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective (R := ℤ) none)).2 hV, dropping the use of Roth.aeval_X_eq_rename.
---

# Roth.mapped_det_ne_zero_aux

## Inventory entry

### `lemma Roth.mapped_det_ne_zero_aux`
- **Type**: `{τ : Type*} {R : MvPolynomial (Option τ) ℤ} {l : ℕ} {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0) (hF : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det = rename some U * Polynomial.aeval (X none) V) : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det ≠ 0`
- **What**: In the proof of Lemma 6 (source §5), the `l × l` determinant `F = det(Δ_{(D μ, ν)} R)` of Hasse derivatives of the integer polynomial `R` factors as `U(x_1,…,x_{p-1}) · V(x_p)` with `U, V ≠ 0` (from `exists_det_eq_mul`). This lemma concludes that the same determinant built from `R` viewed over `ℝ` is nonzero, which is the hypothesis `hdet` that `sum_max_sub_le_index_det` (the lower bound for `ind F`) requires.
- **How**: First `hmapdet`: mapping the integer determinant along `Int.castRingHom ℝ` gives the real determinant, via `RingHom.map_det` and entrywise `MvPolynomial.hasseDeriv_map` (project, Roth/HasseDeriv.lean:134). Then rewrite the goal with `← hmapdet`, use injectivity of `MvPolynomial.map` (`map_injective _ Int.cast_injective`, `map_eq_zero_iff`) to reduce to the integer determinant, substitute `hF`, split `mul_eq_zero`/`not_or`, kill the `U` factor with `rename_injective _ (Option.some_injective _)`, and the `V` factor with `Roth.aeval_X_eq_rename` (Roth/Separation.lean:137) plus injectivity of `rename (fun _ : Unit ↦ none)` (`Subsingleton.elim`) and of `(MvPolynomial.uniqueAlgEquiv ℤ Unit).symm`.
- **Hypotheses**: `hU : U ≠ 0`, `hV : V ≠ 0` (both needed: either factor zero makes the determinant zero); `hF` the factorisation. Section variables `[Fintype τ] [DecidableEq τ]` are omitted (`omit ... in`), so the lemma holds for arbitrary `τ`. Implicitly uses that `ℤ` and `ℝ` are domains (via `mul_eq_zero` in `MvPolynomial (Option τ) ℤ`) and that `Int.cast : ℤ → ℝ` is injective.
- **Uses from project**: `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `MvPolynomial.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `Roth.aeval_X_eq_rename` (Roth/Separation.lean:137). All other identifiers are mathlib (`RingHom.map_det`, `Matrix.ext`, `map_eq_zero_iff`, `MvPolynomial.map_injective`, `Int.cast_injective`, `MvPolynomial.rename_injective`, `Option.some_injective`, `mul_eq_zero`, `not_or`, `MvPolynomial.uniqueAlgEquiv`, `AlgEquiv.injective`, `Subsingleton.elim`).
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:576), as the `hdet` argument of `Roth.sum_max_sub_le_index_det`. No other uses project-wide (`grep -rn mapped_det_ne_zero_aux Roth/`: declaration line 511 and call line 576 only).
- **Visibility**: private
- **Lines**: 510–529 (`omit` line 510, statement 511–517, proof 518–529), proof length 12 lines
- **Notes**: No docstring (private). The last two proof lines re-derive, via the project lemma `aeval_X_eq_rename`, the injectivity of `Polynomial.aeval (X i)`, which mathlib already provides as `Polynomial.toMvPolynomial_injective` (Mathlib/Algebra/MvPolynomial/Equiv.lean:897; `Polynomial.toMvPolynomial i` is by definition `aeval (X i)`). Verified in place with `lean_multi_attempt`: replacing line 528 by `exact (map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective (R := ℤ) none)).2 hV` closes the goal (the only remaining error is "No goals" on the then-redundant line 529).

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: `Roth.index_le_lem6` (Roth/Theta.lean:576), load-bearing for Lemma 6 (it supplies the nonvanishing hypothesis of the index lower bound).
- Wrapper of 1–2 mathlib calls? No. It chains about eight mathlib facts (determinant commutes with ring homs, injectivity of `map`, `rename`, `toMvPolynomial`, integral-domain product rule) plus the project's `hasseDeriv_map`; it is a short but genuine composition.
- Does mathlib have it? No: the statement is about the project's specific Hasse-derivative matrix. The generic ingredients are all in mathlib (`RingHom.map_det`, `MvPolynomial.map_injective`, `MvPolynomial.rename_injective`, `Polynomial.toMvPolynomial_injective`); there is no mathlib lemma "a determinant that factors into nonzero separated factors over ℤ stays nonzero over ℝ", nor should there be.
- Too specific (inline?)? Specific to Lemma 6 with one caller, but inlining a 12-line injectivity argument into the already long `index_le_lem6` would hurt readability; as a private helper it isolates a purely algebraic side condition cleanly.
- Well-chosen? Yes; the statement matches exactly the `hdet` hypothesis shape of `sum_max_sub_le_index_det` and the output of `exists_det_eq_mul`. Small improvement available: use mathlib's `Polynomial.toMvPolynomial_injective` for the `V` factor (verified, see Notes), which also removes this lemma's dependence on `Roth.aeval_X_eq_rename`. The `refine ⟨hU, ?_⟩` plus closing line could then become a single `exact ⟨hU, (map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective (R := ℤ) none)).2 hV⟩` (not separately tested beyond the line-528 replacement).
- Conclusion: `KEEP` — action: keep at Roth/Theta.lean:510–529; optionally golf lines 528–529 to the verified one-liner above.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private

(The name also ends in `_aux`, which independently fires the Step 9a pre-filter. For the record: the content is a Roth-specific transfer of a factorisation along `ℤ → ℝ`; every generic ingredient is already in mathlib, so there is nothing to upstream.)

## Evidence
- `sed -n 470,600p Roth/Theta.lean`: read the declaration, neighbours and the call site in `index_le_lem6`.
- `grep -rn mapped_det_ne_zero_aux Roth/`: Roth/Theta.lean:511 (declaration), Roth/Theta.lean:576 (only use).
- `grep` for project identifiers: `hasseDeriv` (Roth/HasseDeriv.lean:57), `hasseDeriv_map` (Roth/HasseDeriv.lean:134), `aeval_X_eq_rename` (Roth/Separation.lean:137); `uniqueAlgEquiv` is mathlib (Mathlib/Algebra/MvPolynomial/Equiv.lean:67).
- `grep -n "theorem sum_max_sub_le_index_det" -A10 Roth/*.lean`: confirmed the consumed `hdet` hypothesis shape.
- `sed -n 870,910p .lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Equiv.lean`: found `Polynomial.toMvPolynomial` (= `aeval (X i)`) and `Polynomial.toMvPolynomial_injective`.
- `lean_multi_attempt` on Roth/Theta.lean line 528 (no file modified): both `exact (map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective (R := ℤ) none)).2 hV` and the variant with the hom given explicitly close the goal; only diagnostic is "No goals to be solved" at the redundant line 529.
- `git log -S mapped_det_ne_zero_aux`: introduced in the Theta cleanup commits (e.g. af23763, a2e286b, 49e593d).
- No evidence Lean files written (the single experiment ran in place through the LSP; no weakening experiments needed for a private SKIP/KEEP).
