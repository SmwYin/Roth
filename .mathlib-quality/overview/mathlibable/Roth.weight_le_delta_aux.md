---
decl: Roth.weight_le_delta_aux
file: Roth/Theta.lean
line: 494
kind: lemma
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private helper (Step 9a SKIP); it is the real-ratio weight bound used once in index_le_lem6 to feed sum_max_sub_le_index_det, it has real content (about 10 lines), mathlib has no Finsupp.weight-by-degree upper bound, and it is the live replacement for the unused public Roth.weight_le_degree_div.
action: Keep in Roth/Theta.lean:493-508 (sole call site Roth/Theta.lean:577 in index_le_lem6); optional consolidation, not verified here, is to generalise Roth.weight_le_degree_div (Roth/Box.lean:118) to a real lower bound 0 < c with c at most r j and derive this helper from it with c = r none / delta, or delete weight_le_degree_div as its own report recommends.
---

# Roth.weight_le_delta_aux

## Inventory entry

### `lemma Roth.weight_le_delta_aux`
- **Type**: `{τ : Type*} [Fintype τ] {δ : ℝ} (hδ : 0 ≤ δ) {r : Option τ → ℕ} (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {d : τ →₀ ℕ} (hd : d.degree ≤ r none) : Roth.weight (r ∘ some) d ≤ δ`
- **What**: If every parameter `r (some j)` of the first `p - 1` variables satisfies `r_p ≤ δ r_j` (the source's ratio condition, with `r_p = r none`), then every multi-index `d` in those variables of total degree at most `r_p` has weight `∑ j, d j / r_j ≤ δ`. This is the source's estimate `∑_{j<p} i_j / r_j ≤ w / r_{p-1}`-style step in the proof of Lemma 6, recast with a real ratio `δ`.
- **How**: Case split on `r none = 0`: then `hd` forces `d.degree = 0`, so `d = 0` by `Finsupp.degree_eq_zero_iff` and the weight is `0 ≤ δ` (`simpa [weight] using hδ`). Otherwise `r none > 0`, and a four-step `calc`: unfold `weight` (`rfl`); termwise `d j / r_j ≤ d j * δ / r_p` via `Finset.sum_le_sum`, `div_le_div_iff₀` (positivity of `r_j` from `pos_of_mul_pos_right` applied to `hratio j`) and `mul_le_mul_of_nonneg_left (hratio j)`; regroup to `δ * d.degree / r_p` with `Finset.sum_div`, `Finset.sum_mul`, `Finsupp.degree_eq_sum`, `Nat.cast_sum`; conclude with `div_le_iff₀` and `mul_le_mul_of_nonneg_left hd hδ`.
- **Hypotheses**: `hδ : 0 ≤ δ` (needed: with `δ < 0` and `d = 0` the conclusion `0 ≤ δ` fails); `hratio` (the ratio condition, needed for the termwise comparison and also yields `r (some j) > 0` when `r none > 0`); `hd : d.degree ≤ r none`. Section variable `[Fintype τ]` (needed for the finite sum in `weight`); `[DecidableEq τ]` is omitted via `omit ... in`.
- **Uses from project**: `Roth.weight` (Roth/Box.lean:71). All other identifiers are mathlib (`Finsupp.degree_eq_zero_iff`, `Finsupp.degree_eq_sum`, `Finset.sum_le_sum`, `Finset.sum_div`, `Finset.sum_mul`, `Nat.cast_sum`, `div_le_div_iff₀`, `div_le_iff₀`, `pos_of_mul_pos_right`, `mul_le_mul_of_nonneg_left`, `Nat.pos_of_ne_zero`, `Nat.eq_zero_of_le_zero`, `Nat.cast_nonneg`).
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:577), where `fun d hd ↦ weight_le_delta_aux hδ0 hratio (hd.trans (Nat.sub_le_iff_le_add.2 hl'))` discharges the hypothesis `hδ : ∀ d, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ` of `Roth.sum_max_sub_le_index_det`. No other uses project-wide (`grep -rn weight_le_delta_aux Roth/`: declaration line 494 and call line 577 only).
- **Visibility**: private
- **Lines**: 493–508 (`omit` line 493, statement 494–496, proof 497–508), proof length 12 lines
- **Notes**: No docstring (private). The `r none = 0` branch is unreachable from the only call site (there `hrp : 3 ≤ r none`), but it keeps the lemma free of a positivity hypothesis at negligible cost. Relationship to `Roth.weight_le_degree_div` (Roth/Box.lean:118, public, unused): that lemma states the same kind of bound with a natural-number common lower bound `m ≤ r j` and conclusion `weight r d ≤ d.degree / m`; it cannot express the real ratio `r_p ≤ δ r_j`, which is why Lemma 6 uses this helper instead (its report, Roth.weight_le_degree_div.md, flags this helper as the one actually used and recommends REMOVE for the Box lemma).

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: `Roth.index_le_lem6` (Roth/Theta.lean:577), a load-bearing step of Lemma 6.
- Wrapper of 1–2 mathlib calls? No. A case split plus a four-step `calc` combining about ten mathlib lemmas; not a thin wrapper.
- Does mathlib have it? No. `Roth.weight r d` is `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d` (see Roth.weight.md / Roth.weight_eq_finsuppWeight_div.md). The theorem list of Mathlib/Data/Finsupp/Weight.lean has only lower bounds (`le_weight`, `le_weight_of_ne_zero`, `le_degree`) and structural facts (`weight_eq_sum`, `degree_eq_sum`, `degree_eq_weight_one`, `degree_mono`), no upper bound of a weight by degree times a bound on the weights. `lean_leansearch` ("sum over i of d i / r i is at most degree of d divided by min r, Finsupp weight bounded by degree") returned only `Finsupp.degree`, `Finsupp.le_degree`, `MvPolynomial.le_weightedTotalDegree`, `Finsupp.le_weight`, `Finsupp.degree_eq_sum`, all irrelevant. A mathlib-general form (`weight w f ≤ c • degree f` given `∀ i, w i ≤ c`) would be composable via `Finset.sum_le_sum` after `weight_eq_sum`/`degree_eq_sum`, but is not present and is not what the project needs in this exact form.
- Too specific (inline)? It is specific to Lemma 6's ratio condition and has one caller, but inlining a 12-line case-split-plus-calc into the already long `index_le_lem6` proof would hurt readability; as a private helper it is well placed.
- Well-chosen? Yes. The statement is exactly the hypothesis shape `sum_max_sub_le_index_det` consumes (after `d.degree ≤ l - 1 ≤ r none`), and it uses the paper's real ratio `δ` directly.
- Consolidation note: the project currently carries two lemmas for the same estimate, this one (used) and `Roth.weight_le_degree_div` (unused). The clean resolution is either to delete `weight_le_degree_div` (its report's REMOVE) or to generalise it to a real lower bound `0 < c ≤ r j` and reprove this helper from it with `c = r none / δ` (when `δ > 0`; the `δ = 0` and `r none = 0` cases need separate handling, so the saving is small). Not verified in Lean here.
- Conclusion: `KEEP` — action: keep as is at Roth/Theta.lean:493–508; no change needed at the call site Roth/Theta.lean:577.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private

(Additionally the name ends in `_aux`, which would also fire the Step 9a pre-filter. For the record: the content is a Roth-specific ratio-condition bound on `Roth.weight`; the only plausible upstream form, an upper bound of `Finsupp.weight` by `degree` times a bound on the weights, is a two-line composition of `Finsupp.weight_eq_sum`, `Finsupp.degree_eq_sum` and `Finset.sum_le_sum`, and the project does not need it.)

## Evidence
- `sed -n 440,600p Roth/Theta.lean`: read the declaration, its neighbours (`index_det_le`, `mapped_det_ne_zero_aux`, `index_numeric_bound_aux`) and the call site in `index_le_lem6`.
- `grep -rn weight_le_delta_aux Roth/`: Roth/Theta.lean:494 (declaration), Roth/Theta.lean:577 (only use).
- `grep -n "theorem sum_max_sub_le_index_det" -A8 Roth/*.lean`: confirmed the consumed hypothesis shape `∀ d, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ`.
- `grep -n "theorem\|lemma" .lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean`: no weight-by-degree upper bound.
- `lean_leansearch` (one query, recorded above): no matching mathlib lemma.
- Read `.mathlib-quality/overview/mathlibable/Roth.weight_le_degree_div.md` for the cross-reference.
- `git log -S weight_le_delta_aux`: introduced and refined in the Theta cleanup commits (e.g. 49e593d, a2e286b).
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP/KEEP; the project builds clean so the lemma compiles as stated).
