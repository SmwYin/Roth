---
decl: Roth.sum_range_le_sum_of_injective
file: Roth/Wronskian.lean
line: 107
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Unused anywhere in the project (the Wronskian degree argument uses truncated ℕ subtraction, so D ≥ 0 is never needed) and its 4-line proof is just a specialisation of mathlib's Finset.sum_range_le_sum (ℤ, Mathlib/Algebra/Order/Group/Int/Sum.lean:72); Step 8 REMOVE fires the Step 9a pre-filter.
action: Delete Roth.sum_range_le_sum_of_injective from Roth/Wronskian.lean:105-114 (no call sites; then check whether the import Mathlib.Algebra.Order.Group.Int.Sum is still needed); if the user wants the source step D ≥ 0 recorded, mention it in the docstring of coeff_wronskian_of_natDegree_injective instead.
---

# Roth.sum_range_le_sum_of_injective

## Inventory entry

### `theorem Roth.sum_range_le_sum_of_injective`
- **Type**: `∀ {l : ℕ} (d : Fin l → ℕ), Function.Injective d → ∑ ν : Fin l, (ν : ℕ) ≤ ∑ ν, d ν`
- **What**: `l` pairwise distinct natural numbers sum to at least `0 + 1 + ⋯ + (l − 1) = l(l−1)/2`. This is the source's `D = ∑ d_ν − l(l−1)/2 ≥ 0` (clean.tex l.183).
- **How**: Casts to ℤ (`exact_mod_cast`). It then applies mathlib's `Finset.sum_range_le_sum` with `c := 0` to the finset `(univ.image d).map Nat.castEmbedding` of integers, and simplifies with `Finset.card_image_of_injective`, `Finset.sum_image hd.injOn`, `Fin.sum_univ_eq_sum_range` and `Nat.cast_sum`.
- **Hypotheses**: `hd : Function.Injective d`. This is needed: for `l = 2` and `d = 0` the claim reads `1 ≤ 0`. The counterexample was kernel-checked in the earlier cleanup report `.mathlib-quality/cleanup/Wronskian-sum_range_le_sum_of_injective.md` and also appears in `.mathlib-quality/decomposition.md` R4.4.
- **Uses from project**: `[]`
- **Used by**: unused in project. `grep -rn sum_range_le_sum_of_injective Roth Roth.lean` finds only the declaration at Roth/Wronskian.lean:107. Outside `.lean` files the name appears only in planning and cleanup notes (`tickets.md`, `decomposition.md`, `cleanup/*.md`, `PROJECT_OVERVIEW.md`, `overview/decls.tsv`).
- **Visibility**: public
- **Lines**: 105–114 (docstring 105–106, statement 107–108, proof 109–114), proof length 6 lines
- **Notes**: It was planned (tickets.md step 1) as the reason `D := ∑ natDegree − ∑ ν` is well defined. The final `coeff_wronskian_of_natDegree_injective` states the coefficient index with truncated ℕ subtraction and holds for any family, so this lemma became dead code.

## Junk check (Step 8)
- Used anywhere? No. There are no call sites in `Roth/` or `Roth.lean`.
- Wrapper of 1–2 mathlib calls? Essentially yes. The proof is one application of `Finset.sum_range_le_sum` (ℤ, `∑ n ∈ range #s, (c + n) ≤ ∑ x ∈ s, x` for `s : Finset ℤ` bounded below by `c`) with `c = 0`, plus cast and image bookkeeping.
- Does mathlib have it? The mathematical content does: `Finset.sum_range_le_sum` and `Finset.sum_Ico_le_sum` in Mathlib/Algebra/Order/Group/Int/Sum.lean:57–80. Mathlib has no ℕ / `Fin l → ℕ` injective-function version (grep for `range #s` sum bounds and for `sum_range_id_le` in mathlib: none). The specialisation is a 4-line composition, as this proof shows.
- Too specific (inline?)? There is nothing to inline into, because there are no callers.
- Well-chosen statement? It is a clean statement, but it serves no purpose in the formalisation.
- Conclusion: `REMOVE`. Delete the theorem from Roth/Wronskian.lean (lines 105–114). After deleting it, check whether `import Mathlib.Algebra.Order.Group.Int.Sum` (l.7) is still needed by any other declaration in the file. If the user wants to keep it for blueprint fidelity to the source's `D ≥ 0`, the minimal alternative is `private`. Note that the earlier cleanup pass kept the public API by explicit user instruction ("lack of callers is not authorization to delete"), so the deletion needs the user's sign-off.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: Step 8 said REMOVE (the declaration is unused in the project, and its content is a direct specialisation of mathlib's `Finset.sum_range_le_sum`). This fires the Step 9a pre-filter. The other pre-filter checks were also run. The declaration is not private, its name does not end in `_aux`, and its docstring does not start with internal or auxiliary. The qualified name `Roth.sum_range_le_sum_of_injective` is absent from mathlib (namespace-aware grep of `.lake/packages/mathlib/Mathlib/`: no hit).

Note for a possible future upstream: if anyone wanted a ℕ analogue in mathlib, the natural form is `Finset.sum_range_card_le_sum {s : Finset ℕ} : ∑ i ∈ range #s, i ≤ ∑ x ∈ s, x`, next to the ℤ lemmas in Mathlib/Algebra/Order/Group/Int/Sum.lean. The project's injective-function form follows from it via `Finset.sum_image`. This is an at-most-borderline convenience lemma, and it was not pursued because the project does not use it.

## Evidence
- `grep -rn "sum_range_le_sum_of_injective\|sum_range_le_sum" Roth Roth.lean`: only l.107 (the declaration) and l.113 (its own use of mathlib's `Finset.sum_range_le_sum`).
- `git log -S sum_range_le_sum_of_injective -- Roth`: introduced in `3cab03b` (initial autoformalisation). There is no current caller.
- Mathlib grep in `.lake/packages/mathlib/Mathlib`: `Finset.sum_range_le_sum` (Algebra/Order/Group/Int/Sum.lean:72), `sum_Ico_le_sum` (l.57) and `sum_le_sum_range` (l.46), all over ℤ. There is no ℕ / injective-function version and no `Roth.`-qualified name.
- Source: `.mathlib-quality/references/clean.tex` l.183 ("set D = ∑ d_ν − l(l−1)/2 ≥ 0").
- Prior search evidence (Lean-Finder, Loogle, source grep) and the injectivity-necessity counterexample are in `.mathlib-quality/cleanup/Wronskian-sum_range_le_sum_of_injective.md`.
- No Lean runs were made and no evidence files were written. The SKIP verdict needs no compiled weakening, and the existing proof already shows the composition from mathlib.
