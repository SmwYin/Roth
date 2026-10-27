---
decl: Roth.indexSet_comp_subset
file: Roth/Theta.lean
line: 141
kind: lemma
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-direction inclusion used twice (with e and e.symm) to prove Θ_equiv; it is about the project-local indexSet, so it does not belong in mathlib, and a helper is warranted because both directions reuse it.
action: Keep as is in Roth/Theta.lean as the helper for Θ_equiv (Theta.lean:162-163); nothing to upstream.
---

# Roth.indexSet_comp_subset

## Inventory entry

### `lemma Roth.indexSet_comp_subset`
- **Type**: `∀ {σ : Type u_1} [Fintype σ] {τ : Type u_2} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ), indexSet B (q ∘ ⇑e) (r ∘ ⇑e) ⊆ indexSet B q r`
- **What**: Renaming variables along an equivalence `e : σ ≃ τ` maps the set of indices `{ind(R; h/(q∘e); r∘e)}` over `R ∈ ℛ_σ(B; r∘e)` into the corresponding set for `(q, r)` over `τ`. A witness `(R, h)` is sent to `(rename e R, h ∘ e.symm)`.
- **How**: Destructure a membership witness `⟨R, ⟨hR0, hRd, hRc⟩, h, hh, rfl⟩` and provide `rename e R` and `h ∘ e.symm`. The five goals are closed as follows. Nonzero: `rename_eq_zero_iff_of_injective`. Degree bound: surject with `e.surjective`, then `degreeOf_rename_of_injective`. Coefficient bound: surject on exponents with `Finsupp.mapDomain_surjective e.surjective`, then `coeff_rename_mapDomain`. Coprimality: `hh (e.symm j)`. Index equality: `simp [map_rename, index_rename e.injective, Function.comp_def]`.
- **Hypotheses**: `e : σ ≃ τ`. Only injectivity is needed for the index, nonzero, degree and coefficient goals. Surjectivity is needed to transport the degree bound to every `j : τ` and the coefficient bound to every exponent `d : τ →₀ ℕ`. Coprimality uses `e.symm`, so a full equivalence is the natural hypothesis. `[DecidableEq σ]` is omitted. `B`, `q` and `r` are unconstrained.
- **Uses from project**: `Roth.indexSet`, `Roth.RSet` (destructured through `indexSet`), `Roth.index` (through `indexSet`), `Roth.index_rename` (Roth/Index.lean:212)
- **Used by**: Roth/Theta.lean:162 and Roth/Theta.lean:163, both in `Roth.Θ_equiv`, once with `e` and once with `e.symm`. Found with `grep -rn indexSet_comp_subset Roth/`. There are no other uses.
- **Visibility**: private
- **Lines**: 140–154 (the `omit` line is 140, the statement is 141–142, the proof is 143–154), proof length 12 lines
- **Notes**: The lemma has no docstring, which is acceptable for a private lemma. `Θ_equiv` is used at Roth/Theta.lean:919 in Lemma 7.

## Junk check (Step 8)
- **Used anywhere?** Yes. It is used twice in `Roth.Θ_equiv` (Theta.lean:162–163), which proves both inclusions of `subset_antisymm`.
- **Wrapper of 1–2 mathlib calls?** No. It is a 12-line transport proof that combines four mathlib `rename` lemmas (`rename_eq_zero_iff_of_injective`, `degreeOf_rename_of_injective`, `coeff_rename_mapDomain`, `map_rename`) with the project's `index_rename`.
- **Does mathlib have it?** No. It concerns the project-local `indexSet`. The generic ingredients already exist in `Mathlib/Algebra/MvPolynomial/Rename.lean` and related files. leansearch for the generic rename-invariance found only `rename`, `renameEquiv` and `finSuccEquiv` facts, and nothing about this set. No `namespace Roth` exists in mathlib, and the name does not occur in mathlib.
- **Too specific (inline?)?** No. Inlining it would duplicate the 12-line proof in `Θ_equiv`, because both directions use it (the second with `e.symm`). Factoring out one direction and applying it to `e.symm` is the standard pattern.
- **Well-chosen?** Yes. A possible alternative states the equality `indexSet B (q ∘ e) (r ∘ e) = indexSet B q r` directly as the private lemma, which would absorb `Θ_equiv`'s `subset_antisymm` step. That gains nothing, because `Θ_equiv` is already 3 lines.
- **Conclusion:** `KEEP`. No action is needed.

## Mathlibable assessment (Step 9)
Skip reason: private

The lemma is a private helper about the project-local `Roth.indexSet`. Its public consumer `Roth.Θ_equiv` is the API that would be assessed in its own right.

## Evidence
- `grep -rn indexSet_comp_subset Roth/` found the definition at Theta.lean:141 and uses at Theta.lean:162 and 163.
- `grep -rn Θ_equiv Roth/` found the definition at Theta.lean:159, a use at Theta.lean:919 and a docstring mention at Theta.lean:34.
- `lean_hover_info` at Theta.lean:141 confirmed the signature, with no diagnostics.
- One `lean_leansearch` query ("renaming variables of a multivariate polynomial by an equivalence preserves degreeOf and coefficients bound") returned only generic `rename`, `renameEquiv` and `finSuccEquiv` declarations.
- A grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` and for `indexSet_comp_subset` found no matches.
- `lean_local_search` was unavailable because ripgrep is not on PATH, so grep was used instead.
- No evidence Lean files were written, because no weakening was claimed.
