---
decl: Roth.floor_sq_div_two_le_sum
file: Roth/Theta.lean
line: 289
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Dead code since commit 9bf5ca8 (the strengthened positive-part bound mul_sq_div_three_le_sum_max_of_pos_aux re-derives a sharper (θr)²/3 bound inline and no longer calls it); its content is a 4-step consequence of mathlib's Finset.sum_range_id_mul_two plus Nat.floor_le, so Step 8 REMOVE fires the Step 9a pre-filter.
action: Delete Roth.floor_sq_div_two_le_sum from Roth/Theta.lean:287-296 (no call sites; delete together with the equally dead sq_div_three_lt_floor_sq_div_two at l.298-302 after checking it too), or make it private if blueprint fidelity to the source's first FACT is wanted; needs user sign-off.
---

# Roth.floor_sq_div_two_le_sum

## Inventory entry

### `theorem Roth.floor_sq_div_two_le_sum`
- **Type**: `∀ {a : ℝ}, 0 ≤ a → (⌊a⌋₊ : ℝ) ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ν)`
- **What**: For real `a ≥ 0`, `∑_{0 ≤ ν ≤ ⌊a⌋} (a − ν) ≥ ⌊a⌋²/2`. This is the first FACT in the proof of Lemma 6 (§5, clean.tex l.857–875).
- **How**: It casts the Gauss sum identity `Finset.sum_range_id_mul_two (⌊a⌋₊ + 1)` to ℝ. It then splits the sum with `Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_range` and `nsmul_eq_mul`, and closes with `nlinarith [Nat.floor_le ha]`.
- **Hypotheses**: `ha : 0 ≤ a`, used for `Nat.floor_le`. It is needed: for negative `a`, `⌊a⌋₊ = 0` and the right side is `a < 0`.
- **Uses from project**: `[]`
- **Used by**: unused in project. `grep -rn floor_sq_div_two_le_sum Roth Roth.lean` finds only the declaration at Roth/Theta.lean:289. `git show 9bf5ca8` shows that the old proof of the Θ positive-part bound called it (together with `sq_div_three_lt_floor_sq_div_two`). That commit ("Strengthen Theta positive-part sum bound") replaced the call with the inline `hbound` in the private `mul_sq_div_three_le_sum_max_of_pos_aux` (l.320–334), which proves the sharper `(θ r)²/3 ≤ ∑ (θ r − ν)` directly.
- **Visibility**: public
- **Lines**: 287–296 (docstring 287–288, statement 289–290, proof 291–296), proof length 6 lines
- **Notes**: It became dead code in 9bf5ca8. The companion `sq_div_three_lt_floor_sq_div_two` (l.300) looks equally orphaned.

## Junk check (Step 8)
- Used anywhere? No, there are no call sites in `Roth/` or `Roth.lean`. It has been orphaned since 9bf5ca8.
- Wrapper of 1–2 mathlib calls? Essentially yes. It is one cast of `Finset.sum_range_id_mul_two` (Mathlib/Algebra/BigOperators/Intervals.lean:171), the bookkeeping lemmas `Finset.sum_sub_distrib` / `Finset.sum_const`, and `nlinarith` with `Nat.floor_le`.
- Does mathlib have it? Not verbatim. leansearch ("sum over nu from 0 to floor a of (a - nu) is at least floor(a)^2/2") and loogle (`Nat.floor, Finset.sum, Finset.range`) return nothing relevant: only the FloorPow and StrongLaw auxiliaries and `Real.ofDigits_digits_sum_eq`. A grep of mathlib for floor sums together with `sum_range_id` also finds nothing. The content is a direct composition of mathlib's Gauss sum (`Finset.sum_range_id_mul_two` / `Finset.sum_range_id` / `Gauss_sum`-style lemmas) with `Nat.floor_le`.
- Too specific (inline?)? Yes. It is a single numeric FACT from one source proof. There is nothing left to inline into, because its only former caller now proves a stronger bound inline.
- Well-chosen statement? It faithfully states the source FACT, but the formalisation no longer uses it.
- Conclusion: `REMOVE`. Delete l.287–296 of Roth/Theta.lean. It can be kept as `private` only if the user wants the source FACT recorded for the blueprint. Earlier passes kept public API on the user's instruction that lack of callers is not authorization to delete, so the deletion needs the user's sign-off.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: Step 8 said REMOVE. The declaration is unused in the project, and its content is an immediate composition of mathlib's `Finset.sum_range_id_mul_two` with `Nat.floor_le`. This fires the Step 9a pre-filter. The other pre-filter checks were also run. The declaration is not private, its name does not end in `_aux`, and its docstring does not start with internal or auxiliary. The qualified name `Roth.floor_sq_div_two_le_sum` is absent from mathlib (grep of `.lake/packages/mathlib/Mathlib/`: no hit). Even if it were used, it would at best be NO-composable-from-mathlib: a single-use numeric inequality with a 6-line proof from the Gauss sum.

## Evidence
- `grep -rn floor_sq_div_two_le_sum Roth Roth.lean`: only l.289.
- `git log -S floor_sq_div_two_le_sum -- Roth`: introduced in 3cab03b. Its last use was removed in 9bf5ca8, where the diff shows the deleted call `(div_le_div_iff_of_pos_right hrp').2 (floor_sq_div_two_le_sum hθr)`.
- Mathlib grep: `Finset.sum_range_id_mul_two` (Algebra/BigOperators/Intervals.lean:171) and `Finset.sum_range_id` (l.181). No floor-sum lemma.
- lean_leansearch and lean_loogle queries as recorded in the Junk check: no match.
- Source: `.mathlib-quality/references/clean.tex` l.857–875 (first FACT of the Lemma 6 proof).
- No Lean runs were made and no evidence files were written. The SKIP verdict needs no compiled weakening, and the existing proof already shows the composition from mathlib.
