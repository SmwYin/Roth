---
decl: Roth.one_mem_RSet
file: Roth/Theta.lean
line: 73
kind: theorem
visibility: public
verdict: INHERITED-NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Basic membership lemma (1 ∈ RSet B r for 1 ≤ B) proved by one simp unfolding RSet and evaluating coeff_one; glue about the project-local paper notation RSet, which is NO-composable-from-mathlib, so there is nothing to upstream.
action: Do not upstream; keep in Roth/Theta.lean next to RSet as its nonemptiness witness (sole caller indexSet_nonempty at Roth/Theta.lean:81); no call-site changes.
---

# Roth.one_mem_RSet

## Inventory entry

### `theorem Roth.one_mem_RSet`
- **Type**: `∀ {σ : Type*} {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), (1 : MvPolynomial σ ℤ) ∈ Roth.RSet B r`
- **What**: If `1 ≤ B`, the constant polynomial `1` lies in `ℛ_m(B; r)`: it is nonzero, has degree 0 in every variable, and every coefficient is 0 or 1, hence at most `B` in absolute value.
- **How**: `classical; simp [RSet, coeff_one, apply_ite, ite_apply, hB, zero_le_one.trans hB]`. It unfolds the three-way conjunction. The degree clause closes by simp (`degreeOf` of `1`). The coefficient clause becomes `|if 0 = d then 1 else 0| ≤ B` and is split by `apply_ite`, closed by `hB` and `0 ≤ B`.
- **Hypotheses**: `hB : 1 ≤ B`. The section instances `[Fintype σ] [DecidableEq σ]` are omitted (`omit ... in`).
- **Uses from project**: `Roth.RSet`
- **Used by**: `Roth.indexSet_nonempty` (Roth/Theta.lean:81). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 73–75, proof length 2 lines
- **Notes**: Source: clean.tex §5, where the paper says the constant polynomial 1 with every `h_i = 1` is allowed. The paper assumes `B ≥ 1` in the definition of `ℛ_m`. Lean drops that from `RSet` and adds it here as a hypothesis.

## Junk check (Step 8)
- Used anywhere? Yes, once: it is the witness in `indexSet_nonempty`, which is what makes `Θ` a well-defined supremum.
- Wrapper of 1–2 mathlib calls? No. It is a basic membership fact about the project def `RSet`, proved by unfolding.
- Does mathlib have it? No. `RSet` is project-local, and no `namespace Roth` exists under `.lake/packages/mathlib/Mathlib/`.
- Too specific (inline?)? It could be inlined into its one caller, but as the nonemptiness witness of `RSet` it is a natural API lemma. It mirrors the source sentence, and it keeps `indexSet_nonempty` a one-line term. Inlining would save nothing.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)
Inherited from: Roth.RSet

Pre-filter: the lemma is public, its name does not end in `_aux`, its docstring is not internal, Step 8 said KEEP, and the qualified name is absent from mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`). No SKIP.

Glue check: the proof is a single `simp` that unfolds `RSet` and evaluates the coefficients of `1` (`coeff_one`). It adds no mathematics beyond the definition, the same kind of simp-unfolding lemma this run has treated as glue (for example `MvPolynomial.hasseDeriv_monomial`). The parent `Roth.RSet` is `NO-composable-from-mathlib`, not `NO-mathlib-has-it`, so the re-aim rule does not apply. `RSet` is proof-internal notation of Roth/Ridout/Yamada, written as a set-builder over mathlib primitives (`≠ 0`, `degreeOf` / `degreesLE`, `coeff`), and it is not going to mathlib. A lemma saying `1` belongs to it has no independent upstream value. The mathlib facts it uses (`MvPolynomial.coeff_one`, `one_ne_zero`, `degreeOf` of a constant) already exist. Verdict: `INHERITED-NO-composable-from-mathlib`. Next step: none. Keep it next to `RSet`.

## Evidence
- `grep -rn one_mem_RSet Roth/`: the definition at Theta.lean:73 and one use at Theta.lean:81 (`indexSet_nonempty`).
- `grep -rln "namespace Roth" .lake/packages/mathlib/Mathlib/`: no hits.
- I reused the parent report `.mathlib-quality/overview/mathlibable/Roth.RSet.md` and its evidence file `.mathlib-quality/overview/evidence/Roth.RSet/RSet_vs_mathlib.lean`. I wrote no new evidence files and ran no Lean.
