---
decl: LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux
file: Roth/LeanEval.lean
line: 20
kind: lemma
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private helper that turns finiteness of Roth.approxSet x κ for irrational x into a uniform positive constant C with C / q^κ < |x - p/q|; used once by isDiophantine_iff, has no direct mathlib counterpart, and is too long to inline cleanly.
action: Keep as is in Roth/LeanEval.lean (sole caller isDiophantine_iff, line 54); no upstreaming since it is private and harness-specific; if Roth is upstreamed in LiouvilleWith form this helper is no longer needed.
---

# LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux

## Inventory entry

### `lemma LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`
- **Type**: `{x κ : ℝ} (hx : Irrational x) (hs : (Roth.approxSet x κ).Finite) : ∃ C : ℝ, 0 < C ∧ ∀ (p q : ℤ), 0 < q → C / (q : ℝ) ^ κ < |x - (p : ℝ) / q|`
- **What**: If `x` is irrational and there are only finitely many `(p, q)` with `q > 0` and `|x - p/q| < 1/q^κ`, then there is a uniform `C > 0` with `C / q^κ < |x - p/q|` for every integer `p` and positive integer `q`. This is the "finitely many good approximations gives a uniform lower bound" step.
- **How**: Set `f (p, q) = |x - p/q| * q^κ`. Take a minimiser `a` of `f` over the finite nonempty set `insert (0, 1) (approxSet x κ)` with `Set.exists_min_image`. Then `f a > 0` by `Irrational.ne_rational` (via `abs_pos`, `sub_ne_zero`) and `Real.rpow_pos_of_pos`. Choose `C = min (1/2) (f a / 2)`. After `lift q to ℕ` and `div_lt_iff₀`, split on `(p, q) ∈ approxSet x κ`. If it is a member, use `min_le_right`, `half_lt_self` and minimality `hmin`. If not, use `min_le_left`, `1/2 < 1` and the negated membership, unfolded with `lt_div_iff₀`.
- **Hypotheses**: `hx : Irrational x` (needed so that `f a > 0`; without it the minimum could be `0`); `hs : (Roth.approxSet x κ).Finite`. `κ` is arbitrary real (no sign hypothesis needed).
- **Uses from project**: `Roth.approxSet` (Roth/Main.lean:55). No other project identifiers. The `Set.exists_min_image`, `Irrational.ne_rational`, `Real.rpow_pos_of_pos`, `div_lt_iff₀`, `lt_div_iff₀`, `half_lt_self`, `min_le_left/right` calls are all mathlib.
- **Used by**: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` (Roth/LeanEval.lean:54, reverse direction) only. `grep -rn exists_pos_div_rpow_lt_aux Roth/ Roth.lean` gives just the declaration (line 20) and that call (line 54).
- **Visibility**: private
- **Lines**: 20–39, proof length 17 lines (23–39)
- **Notes**: Lives in the external lean-eval harness file Roth/LeanEval.lean (namespace fixed by the harness). The insertion of `(0, 1)` is a trick to make the set nonempty even if `approxSet x κ` is empty. The `1/2` branch of the `min` handles pairs outside `approxSet`, where `|x - p/q| * q^κ ≥ 1`.

## Junk check (Step 8)
- Used anywhere? Yes, exactly once, in `isDiophantine_iff` (line 54), where it gives the `IsDiophantine` direction from finiteness of `approxSet x (2 + ε)`.
- Wrapper of 1–2 mathlib calls? No. It is a 17-line argument that combines a finite-set minimum, irrationality and a case split.
- Does mathlib have it? No direct counterpart. `lean_leansearch` on the statement returned only `Liouville`, `LiouvilleWith`, `Liouville.frequently_exists_num`, `forall_liouvilleWith_iff`, `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` and `setOf_liouville_eq_irrational_inter_iInter_iUnion`, none of which gives a uniform lower bound from finiteness. The `LiouvilleWith.lean` API (`exists_pos`, `mono`, `frequently_lt_rpow_neg`, arithmetic closure lemmas) works in the opposite direction: it extracts approximations from `LiouvilleWith`, not a lower bound from their absence. The closest idiom is `¬ LiouvilleWith p x`, but turning that into a uniform `C` would also need a minimisation argument like this one.
- Too specific (inline?)? It is specific to the harness's `IsDiophantine` shape, but inlining 17 lines into the second bullet of `isDiophantine_iff` would make that proof harder to read. As a separate private helper it reads cleanly.
- Well-chosen? Yes. The statement is the natural "finite exceptional set implies uniform constant" step, and it is stated for general `κ`, not just `2 + ε`, which is the right level of generality for its one use.

Conclusion: KEEP. No action. Leave it private in Roth/LeanEval.lean next to its sole caller `isDiophantine_iff`.

## Mathlibable assessment (Step 9)

Skip reason: private

Verdict: SKIP. The declaration is `private`, and its name also ends in `_aux`, so the Step 9a pre-filter fires either way. It is a helper for the external lean-eval harness predicate `IsDiophantine` (assessed separately as NO-composable-from-mathlib). If the Thue–Siegel–Roth result is upstreamed, it would be stated with `LiouvilleWith` (see the `Roth.roth` and `IsDiophantine` reports), and this helper would not be needed.

## Evidence
- `sed -n 1,60p Roth/LeanEval.lean`: read the declaration, the whole proof and its caller.
- `grep -rn exists_pos_div_rpow_lt_aux Roth/ Roth.lean`: found only the definition (line 20) and the use at line 54.
- `sed -n 50,75p Roth/Main.lean`: definition of `Roth.approxSet` (line 55).
- `lean_leansearch` with the natural-language statement: no matching mathlib lemma (results listed in the Junk check).
- `grep -n "theorem\|lemma\|def " .lake/packages/mathlib/Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean`: no lower-bound-from-finiteness lemma.
- `grep -rn "theorem.*exists_min_image\b"` in mathlib: confirmed `Set.exists_min_image` (Mathlib/Data/Set/Finite/Lemmas.lean:75) is the mathlib lemma used.
- No Lean compilation was needed (SKIP verdict, no weakening claimed); no evidence files written.
