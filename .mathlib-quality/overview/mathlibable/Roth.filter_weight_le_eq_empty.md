---
decl: Roth.filter_weight_le_eq_empty
file: Roth/Lattice.lean
line: 143
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 3-line helper saying the filter of box r by weight r d ≤ (m - lam)/2 is empty when m < lam (negative threshold vs. weight_nonneg); used twice in the base cases of card_filter_weight_le, project-specific (weight is a Roth def), nothing to upstream.
action: Keep as private helper for its two uses in Roth.card_filter_weight_le (Roth/Lattice.lean:208 and 214); optional polish only (state for any Finset s and any negative threshold), no upstream target.
---

# Roth.filter_weight_le_eq_empty

## Inventory entry

### `theorem Roth.filter_weight_le_eq_empty`
- **Type**: `∀ {m : ℕ} (r : Fin m → ℕ) {lam : ℝ}, (m : ℝ) < lam → (box r).filter (fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2) = ∅` (declared `private lemma`).
- **What**: If `λ > m`, then no multi-index in the box `∏ [0, r_j]` has weight at most `(m - λ)/2`, because that threshold is negative while every weight `∑ d_j / r_j` is nonnegative. This is the trivial (empty) case of the Lemma 8 lattice count.
- **How**: Term proof `Finset.filter_eq_empty_iff.2 fun d _ h ↦ by linarith [weight_nonneg r d]`: for each `d`, the filter condition `h : weight r d ≤ (m - lam)/2` together with `hlam : m < lam` and `Roth.weight_nonneg r d : 0 ≤ weight r d` is contradictory by `linarith`.
- **Hypotheses**: `hlam : (m : ℝ) < lam` is used (it makes the threshold negative); it is strict, and needed: at `lam = m` the zero multi-index has weight `0 ≤ 0` and lies in the filter. Membership in `box r` (the `_` binder) is not used, so the statement holds for any `Finset (Fin m →₀ ℕ)`; `Fin m` could be any `Fintype σ` with `Fintype.card σ` in place of `m`. Neither generalisation is needed by the call sites.
- **Uses from project**: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71), `Roth.weight_nonneg` (Roth/Box.lean:75).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_weight_le` only, twice: l.208 (`zero` case of the induction on `m`, `m = 0`, from `0 < lam`) and l.214 (`succ` case with `n = 0` and `lam > 2 √1 = 2 > 1`). `grep -rn filter_weight_le_eq_empty Roth/` returns only the definition (l.143) and these two uses.
- **Visibility**: private
- **Lines**: 143–145, proof length 1 line (145)
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, twice, both in the public Lemma 8 `Roth.card_filter_weight_le` (l.208, l.214).
- Wrapper of 1–2 mathlib calls? Essentially yes: `Finset.filter_eq_empty_iff` (Mathlib/Data/Finset/Filter.lean:159; equivalently `Finset.filter_false_of_mem`, l.169) plus `linarith` with the project lemma `Roth.weight_nonneg`.
- Does mathlib have it? No: `weight` is a project definition (`∑ j, (d j : ℝ) / r j`, Roth/Box.lean:71), so no mathlib statement can mention it; the generic content is just `Finset.filter_eq_empty_iff`/`Finset.filter_false_of_mem`. `grep -rn "weight.*eq_empty" Mathlib/`: no relevant hits.
- Too specific / inline? It could be inlined, but it is used twice, and the second use (l.214) supplies a non-trivial `hlam` argument (`norm_num at h ⊢; linarith`); inlining would duplicate the filter expression and the `linarith [weight_nonneg r d]` step at both sites. Keeping the named helper is cleaner.
- Well-chosen? Yes; the statement matches the exact filter expression in `card_filter_weight_le`, so `rw` applies directly. Minor optional polish: the box-membership binder is unused, so it could be stated for an arbitrary finset (or for any negative threshold `c < 0`), but the current form is what the `rw` call sites want.
- Conclusion: `KEEP`. Action: none required; keep private next to `card_filter_weight_le`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:143). Independently, it concerns the project-specific `Roth.weight` and its generic content is already mathlib's `Finset.filter_eq_empty_iff`, so there is nothing upstreamable.

## Evidence
- `grep -rn filter_weight_le_eq_empty Roth/`: definition l.143, uses l.208 and l.214 (both in `Roth.card_filter_weight_le`).
- Read Roth/Lattice.lean l.143–145 and l.196–222, and Roth/Box.lean l.40–80 (`box`, `mem_box`, `weight`, `weight_nonneg`).
- `grep -rn "theorem filter_eq_empty_iff\|theorem filter_false_of_mem" .lake/packages/mathlib/Mathlib/`: both in Mathlib/Data/Finset/Filter.lean (l.159, l.169).
- `grep -rn "weight.*eq_empty" .lake/packages/mathlib/Mathlib`: no relevant hits.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated. The necessity of strict `hlam` was checked by hand (zero multi-index at `lam = m`).
