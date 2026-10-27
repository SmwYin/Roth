---
decl: Roth.sqrt_lt_nat_floor_aux
file: Roth/MainLemma.lean
line: 104
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private two-line helper giving the strict half sqrt X < natfloor X (for X at least 2) of the public Roth.sqrt_lt_floor; elementary consequence of Real.sqrt_lt' and Nat.lt_floor_add_one with no mathlib counterpart, private and _aux so not upstreamed.
action: Keep as private helper for its sole use in Roth.sqrt_lt_floor (Roth/MainLemma.lean:116); no upstream action.
---

# Roth.sqrt_lt_nat_floor_aux

## Inventory entry

### `theorem Roth.sqrt_lt_nat_floor_aux`
- **Type**: `∀ {X : ℝ}, 2 ≤ X → √X < (⌊X⌋₊ : ℝ)` (declared `private lemma`; `⌊X⌋₊` is `Nat.floor`, cast to `ℝ`).
- **What**: For a real `X ≥ 2`, the square root of `X` is strictly smaller than the natural floor of `X`. This is the strict inequality `B₁ = ⌊X⌋ > √X` of the source's §6 (with `X = q₁^{δ r₁}`), isolated as the first component of `Roth.sqrt_lt_floor`.
- **How**: Term-mode proof. First `hfloor : 2 ≤ (⌊X⌋₊ : ℝ)` by `exact_mod_cast Nat.le_floor hX`. Then reduce `√X < ⌊X⌋₊` to `X < ⌊X⌋₊ ^ 2` via `Real.sqrt_lt'` (positivity of the floor from `hfloor` by `positivity`), and close with `nlinarith only [Nat.lt_floor_add_one X, hfloor]` (from `X < f + 1` and `f ≥ 2` one gets `X < f + 1 ≤ f²`).
- **Hypotheses**: `hX : 2 ≤ X`. Needed in some form: for `X ∈ [1, 2)` the floor is `1` while `√X ≥ 1`, so the strict inequality fails (e.g. `X = 1`: `√1 = 1 = ⌊1⌋₊`); for `X < 1` the floor is `0`. The threshold `2` is not sharp (the claim holds iff `⌊X⌋₊ ≥ 2`, i.e. `X ≥ 2`, since for `X ∈ [2,3)` one has `X < 3 < 4 = 2²`), so `2 ≤ X` is exactly the right hypothesis.
- **Uses from project**: `[]` (only mathlib: `Nat.le_floor`, `Nat.lt_floor_add_one`, `Real.sqrt_lt'`; tactics `exact_mod_cast`, `positivity`, `nlinarith`).
- **Used by**: Roth/MainLemma.lean `Roth.sqrt_lt_floor` only (l.116, `⟨sqrt_lt_nat_floor_aux hX, Nat.floor_le (by positivity)⟩`). `grep -rn sqrt_lt_nat_floor_aux Roth/` returns only the definition (l.104) and this use. (Indirectly, through `sqrt_lt_floor`, it feeds Roth/MainLemma.lean l.154 and l.201 and Roth/Main.lean l.494.)
- **Visibility**: private
- **Lines**: 104–106, proof length 2 lines (105–106)
- **Notes**: Name ends in `_aux`, so the Step 9a pre-filter would also fire. Introduced in commit 9bebcd0 ("Clean up and sharpen the square-root floor bound"), which also weakened `sqrt_lt_floor`'s hypothesis from `4 < X` to `2 ≤ X`; the cleanup audit `.mathlib-quality/cleanup/MainLemma-sqrt_lt_nat_floor_aux.md` recorded the split and the elaboration speed-up (about 129 ms to 96 ms).

## Junk check (Step 8)
- Used anywhere? Yes, once: the public `Roth.sqrt_lt_floor` (Roth/MainLemma.lean:116), which itself has three downstream uses (MainLemma l.154, l.201; Main l.494).
- Wrapper of 1–2 mathlib calls? Essentially a short composition of three mathlib lemmas (`Nat.le_floor`, `Real.sqrt_lt'`, `Nat.lt_floor_add_one`) plus `nlinarith`; it is not a rename of a single mathlib lemma.
- Does mathlib have it? No. loogle `Real.sqrt _ < (Nat.floor _ : ℝ)` returned no results; leansearch ("square root of x is less than floor of x for x at least 2") returned only `Real.sqrt_lt'`, `Real.sqrt_lt`, `Real.real_sqrt_lt_nat_sqrt_succ`, `Nat.sqrt_mul_sqrt_lt_succ'`, none of which is this statement. The ingredients live in Mathlib/Analysis/Real/Sqrt.lean:235 (`Real.sqrt_lt'`), Mathlib/Algebra/Order/Floor/Defs.lean:141 (`Nat.le_floor`), Mathlib/Algebra/Order/Floor/Semiring.lean:63 (`Nat.lt_floor_add_one`).
- Too specific / inline? It could be inlined into the first component of `sqrt_lt_floor` (its only consumer, whose sole extra content is `Nat.floor_le`); that would be an acceptable but cosmetic change. Keeping the strict half as a separate private helper keeps `sqrt_lt_floor` a one-line pairing and was a deliberate cleanup choice with a measured elaboration gain, so no change is warranted.
- Well-chosen? Yes: the hypothesis `2 ≤ X` is the sharp threshold (see Hypotheses), and the statement is the natural one.
- Conclusion: `KEEP`. Action: none (optional: inline into `Roth.sqrt_lt_floor` if the project prefers fewer private helpers).

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:104); additionally the name ends in `_aux`.

Side note: if anything here were upstreamed, it would be the public `Roth.sqrt_lt_floor` (assessed separately), not this helper; the general ingredients are already in mathlib.

## Evidence
- `grep -rn "sqrt_lt_nat_floor_aux\|sqrt_lt_floor" Roth/`: definition l.104, sole use l.116 (`sqrt_lt_floor`); `sqrt_lt_floor` used at MainLemma l.154, l.201 and Main l.494.
- `git log -S sqrt_lt_nat_floor_aux` and `git show 9bebcd0`: helper introduced in the cleanup commit that also weakened `sqrt_lt_floor` from `4 < X` to `2 ≤ X`.
- lean_loogle `Real.sqrt _ < (Nat.floor _ : ℝ)`: no results. lean_leansearch natural-language query: no matching lemma (results listed in the junk check).
- `grep` of `.lake/packages/mathlib/Mathlib/`: `Real.sqrt_lt'` (Analysis/Real/Sqrt.lean:235), `Nat.le_floor` (Algebra/Order/Floor/Defs.lean:141), `Nat.lt_floor_add_one` (Algebra/Order/Floor/Semiring.lean:63).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated. Sharpness of `2 ≤ X` checked by hand (`X = 1` gives `√1 = 1 = ⌊1⌋₊`; for `X ∈ [2,3)`, `X < 4 = ⌊X⌋₊²`).
