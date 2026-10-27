---
decl: Roth.sq_div_three_lt_floor_sq_div_two
file: Roth/Theta.lean
line: 300
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Dead code since commit 9bf5ca8 (its only caller, the old Theta positive-part bound, was replaced by the inline sharper bound in mul_sq_div_three_le_sum_max_of_pos_aux); it is a one-tactic nlinarith consequence of mathlib's Nat.lt_floor_add_one, so Step 8 REMOVE fires the Step 9a pre-filter.
action: Delete Roth.sq_div_three_lt_floor_sq_div_two from Roth/Theta.lean:298-302 together with the equally dead floor_sq_div_two_le_sum (l.287-296), or make it private if blueprint fidelity to the source's second FACT is wanted; needs user sign-off.
---

# Roth.sq_div_three_lt_floor_sq_div_two

## Inventory entry

### `theorem Roth.sq_div_three_lt_floor_sq_div_two`
- **Type**: `∀ {a : ℝ}, 10 < a → a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2`
- **What**: For real `a > 10`, `a²/3 < ⌊a⌋²/2`. This is the second FACT in the proof of Lemma 6 (§5, clean.tex l.878–889).
- **How**: A single `nlinarith [Nat.lt_floor_add_one a]`. The source's argument (`n ≥ 10`, so `a < n + 1 ≤ (11/10) n`, so `a² < (121/100) n² < (3/2) n²`) is left to nlinarith.
- **Hypotheses**: `ha : 10 < a`. Some threshold is needed: for `a` in `[1, 2)`, `⌊a⌋²/2 = 1/2` while `a²/3` can reach about `4/3`. The constant 10 matches the source, but it is not sharp.
- **Uses from project**: `[]`
- **Used by**: unused in project. `grep -rn sq_div_three_lt_floor_sq_div_two Roth Roth.lean` finds only the declaration at Roth/Theta.lean:300. The diff of `git show 9bf5ca8` removes its last call, `(div_le_div_iff_of_pos_right hrp').2 (sq_div_three_lt_floor_sq_div_two hθ).le`.
- **Visibility**: public
- **Lines**: 298–302 (docstring 298–299, statement 300–301, proof 302), proof length 1 line
- **Notes**: It became dead code in 9bf5ca8, along with its companion `floor_sq_div_two_le_sum`.

## Junk check (Step 8)
- Used anywhere? No, it has been orphaned since 9bf5ca8.
- Wrapper of 1–2 mathlib calls? Yes. It is `nlinarith` fed the single mathlib fact `Nat.lt_floor_add_one`.
- Does mathlib have it? Not verbatim. A leansearch for "for real a > 10, a^2/3 < (floor a)^2 / 2" returns only the related shapes `Int.div_two_lt_floor`, `Nat.mul_lt_floor` and `Behrend.div_lt_floor`, which are linear floor lower bounds. Mathlib grep for the name: no hit. The content follows immediately from mathlib's floor API.
- Too specific (inline?)? Yes. It is a numeric FACT with an arbitrary constant, and its former caller is gone.
- Conclusion: `REMOVE`. Delete l.298–302 of Roth/Theta.lean, or make it private if the user wants the source FACT recorded for the blueprint. This needs user sign-off, because earlier passes kept public API on the user's instruction.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: Step 8 said REMOVE. The declaration is unused, and it is a one-line `nlinarith` from `Nat.lt_floor_add_one`, which fires the Step 9a pre-filter. The other pre-filter checks were also run. The declaration is not private, its name does not end in `_aux`, and its docstring does not start with internal or auxiliary. The qualified name is absent from mathlib (grep of `.lake/packages/mathlib/Mathlib/`). Even if it were used, it would at best be NO-composable-from-mathlib.

## Evidence
- `grep -rn sq_div_three_lt_floor_sq_div_two Roth Roth.lean`: only l.300.
- `git log -S sq_div_three_lt_floor_sq_div_two -- Roth`: 3cab03b (introduced) and 9bf5ca8 (last call removed).
- Mathlib grep for the name: no hits.
- lean_leansearch as recorded above: no match.
- Source: `.mathlib-quality/references/clean.tex` l.878–889.
- No Lean runs were made and no evidence files were written. The existing one-line proof already shows the composition.
