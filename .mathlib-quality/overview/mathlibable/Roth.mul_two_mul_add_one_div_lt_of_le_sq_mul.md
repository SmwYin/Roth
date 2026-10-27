---
decl: Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
file: Roth/MainLemma.lean
line: 433
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Dead code - no caller anywhere in the project since commit 6c41716 replaced its only use with an inline variant (weak delta*m at most 1, conclusion at most L) at MainLemma l.681 that this strict statement cannot serve; a one-off ordered-field arithmetic step with no literature or mathlib standing, so Step 8 REMOVE triggers the Step 9a pre-filter.
action: Delete Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul from Roth/MainLemma.lean (l.426-443, no call sites to update); optional alternative - restate it as the non-strict variant (delta*m at most 1 and 2m+1 at most delta^2 L give m(2m+1)/delta at most L) and use it for the have hq inside theta_lt_eta_of_sq_log_bound_aux (MainLemma l.681); either way project-local, no mathlib PR.
---

# Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul

## Inventory entry

### `theorem Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`
- **Type**: `∀ {K : Type*} [Semifield K] [LinearOrder K] [IsStrictOrderedRing K] [ExistsAddOfLE K] {δ m L : K}, 0 < 2 * m + 1 → δ * m < 1 → 2 * m + 1 ≤ δ ^ 2 * L → m * (2 * m + 1) / δ < L`
- **What**: In a linearly ordered semifield, from `0 < 2m+1`, `δm < 1` and `2m+1 ≤ δ²L`, deduce `m(2m+1)/δ < L`. With `L = log q₁` this is the source's Lemma `lem:lem7-satisfied` ("verify δ log q₁ > m(2m+1)", from (29) and (32)), i.e. the hypothesis of Lemma 7.
- **How**: Shows `δ ≠ 0` (else `0 < 2m+1 ≤ 0`), multiplies both sides by `δ² > 0` via `mul_lt_mul_iff_of_pos_right` and `sq_pos_of_ne_zero`, then a `calc`: `field_simp` rewrites the LHS to `(δm)(2m+1)`, `mul_lt_of_lt_one_left hm hδm` gives `< 2m+1`, and `h32` closes `≤ Lδ²`.
- **Hypotheses**: `hm : 0 < 2m+1` (positivity of the factor), `hδm : δm < 1` (strict, from (29) `δ < 1/m` style bound), `h32 : 2m+1 ≤ δ²L` (weak form of (32)).
- **Uses from project**: `[]`
- **Used by**: unused in project (grep of `Roth/`, `Roth.lean`, `Main.lean` and the whole repo outside `.lake`/`.mathlib-quality`: only the definition at Roth/MainLemma.lean:433 and an inventory heading in PROJECT_OVERVIEW.md). Its former caller (as `lem7_hyp_of_h32 (K := ℝ)`) was removed in commit 6c41716 ("Simplify Roth main lemma and weaken its hypotheses"); the needed bound is now re-derived inline as `have hq : M * (2 * M + 1) / δ ≤ Real.log (q 0)` in the private `theta_lt_eta_of_sq_log_bound_aux` (Roth/MainLemma.lean:681-685), under the weaker `δ * m ≤ 1` with non-strict conclusion.
- **Visibility**: public
- **Lines**: 426-443 (docstring 426-432, statement 433-435), proof length 8 lines
- **Notes**: Renamed from `lem7_hyp_of_h32` in commit 846f8f2. The cleanup log (commit 6c41716 notes) records that the strict-`δm`/weak-square contract cannot replace the weak-`δm`/strict-square need at `δ = 1/m`, which is why the caller stopped using it.

## Junk check (Step 8)
- Used anywhere? No. Zero call sites project-wide (see Used by); the one place that needs this kind of bound (MainLemma l.681) re-derives a different, non-strict variant inline because this statement's strict `δ * m < 1` hypothesis fails at the boundary `δ = 1/m` that the main lemma now allows.
- Wrapper of 1-2 mathlib calls? Essentially: `mul_lt_mul_iff_of_pos_right` + `mul_lt_of_lt_one_left` after a `field_simp` normalisation; an 8-line ordered-field computation.
- Does mathlib have it? No: Loogle `?a * ?b / ?c < ?d, ?c ^ 2` no hits; LeanSearch "if δ m < 1 and 2m+1 ≤ δ^2 L then m(2m+1)/δ < L" returned only unrelated results (Finset.mulConst_le_divConst_sq, Besicovitch.goodδ_lt_one, ...); namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for the name: no hit. It is a problem-specific numeric inequality, not a general lemma.
- Too specific (inline?)? Yes: the expression `m(2m+1)` is the exact constant of the source's Lemma 7 and has no meaning outside it.
- Well-chosen? It names the source lemma, but its hypothesis contract no longer matches the project's actual use, so it is dead.
- Conclusion: `REMOVE`. Concrete action: delete the theorem (no call sites to update). Optional alternative if the source-lemma anchor is wanted: restate as `δ * m ≤ 1 → 2 * m + 1 ≤ δ ^ 2 * L → 0 < δ → m * (2 * m + 1) / δ ≤ L` (or with `0 < 2m+1` and deriving `δ ≠ 0` as now) and replace the inline `have hq` at MainLemma l.681-685 with a call to it.

## Mathlibable assessment (Step 9)

Skip reason: Step 8 said REMOVE (dead code: unused anywhere in the project since commit 6c41716; the remaining need is served by a different inline variant). Step 9a pre-filter fires, so no full /mathlibable run. For the record: public; name does not end `_aux`; docstring starts "The bound"; qualified name not in mathlib. Even ignoring the pre-filter, the content is a one-off arithmetic step tied to the constant `m(2m+1)` of the source's Lemma 7, with no literature standing beyond that paper, so it would not be a mathlib candidate.

## Evidence
- `grep -rn mul_two_mul_add_one_div_lt_of_le_sq_mul` over Roth/, Roth.lean, Main.lean and the whole repo excluding .lake/.mathlib-quality/.git: only the definition (Roth/MainLemma.lean:433) and PROJECT_OVERVIEW.md:3853 (inventory heading).
- `git log -S` for the current and old name (`lem7_hyp_of_h32`): introduced in 3cab03b, caller removed in 6c41716 (diff line removing `(lem7_hyp_of_h32 (K := ℝ)`), renamed in 846f8f2.
- Inline replacement read at Roth/MainLemma.lean:671-689 (`theta_lt_eta_of_sq_log_bound_aux`, `have hq : M * (2 * M + 1) / δ ≤ Real.log (q 0)` under `hδm : δ * (m : ℝ) ≤ 1`).
- Source checked: .mathlib-quality/references/clean.tex l.1330-1335 (Lemma lem:lem7-satisfied).
- Loogle `?a * ?b / ?c < ?d, ?c ^ 2`: no results. LeanSearch natural-language query: no relevant results. grep of .lake/packages/mathlib/Mathlib for the name: no hit.
- No Lean evidence files written (no weakening claimed; SKIP via pre-filter).
