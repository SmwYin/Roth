---
decl: Roth.approxSet_num_den_mem_aux
file: Roth/Main.lean
line: 149
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private helper showing that reducing h/q to lowest terms keeps a pair in approxSet (den divides q, so the bound 1/q^κ weakens to 1/den^κ for κ ≥ 0); used once in exists_reduced_approx; mathlib has no approxSet and no direct den-of-quotient-le lemma.
action: Keep as private helper for its single call site Roth/Main.lean:174 (exists_reduced_approx); optionally inline there, no change required.
---

# Roth.approxSet_num_den_mem_aux

## Inventory entry

### `theorem Roth.approxSet_num_den_mem_aux`
- **Type**: `∀ {α κ : ℝ}, 0 ≤ κ → ∀ {h : ℤ} {q : ℕ}, (h, q) ∈ approxSet α κ → (((h : ℚ) / q).num, ((h : ℚ) / q).den) ∈ approxSet α κ`
- **What**: If h/q is a solution of `0 < q`, `|α - h/q| < 1/q^κ`, then so is its reduced form `num/den`: the reduced denominator is at most q, so for κ ≥ 0 the bound only gets weaker, while the value of the fraction is unchanged.
- **How**: Sets `x := (h : ℚ) / q`. Proves `x.den ≤ q` via `Nat.le_of_dvd hq.1` and `Int.natCast_dvd_natCast.1` applied to mathlib's `Rat.den_dvd h q` (after `simpa [x, Rat.divInt_eq_div]`). Positivity of the new denominator is `x.den_pos`. For the inequality, rewrites `(x.num : ℝ) / x.den` back to `(x : ℝ)` with `← Rat.cast_def`, `Rat.cast_div`, `Rat.cast_intCast`, `Rat.cast_natCast`, then `hq.2.trans_le` with `gcongr` (monotonicity of `1 / t ^ κ` in `t`, using `hκ` and `hden`).
- **Hypotheses**: `hκ : 0 ≤ κ` is genuinely needed (for κ < 0, `1/q^κ` is increasing in q, so shrinking the denominator could break the bound); `hq` membership provides `0 < q` (used for `Nat.le_of_dvd`) and the approximation inequality.
- **Uses from project**: `Roth.approxSet` (Roth/Main.lean:55).
- **Used by**: Roth/Main.lean:174 `Roth.exists_reduced_approx` only (`grep -rn approxSet_num_den_mem_aux Roth/` gives the definition l.149 and that use). Transitively everything downstream of `exists_reduced_approx` in Roth/Main.lean (the §7 main argument).
- **Visibility**: private
- **Lines**: 149–156, proof length 6 lines
- **Notes**: Name ends in `_aux`; no docstring (private). Corresponds to the source §7 first paragraph remark that the reduced form of a solution is again a solution.

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_reduced_approx` (Roth/Main.lean:174), where it shows the reduced form of every solution is a reduced solution.
- Wrapper of 1–2 mathlib calls? No. It combines `Rat.den_dvd`, a divisibility-to-inequality step, cast rewriting, and a `gcongr` monotonicity step; about 6 lines.
- Does mathlib have it? No. `approxSet` is a project def. The generic ingredient `((h : ℚ) / q).den ≤ q` is also absent as a single lemma: `lean_loogle "Rat.den (_ / _) ≤ _"` returned nothing; `lean_leansearch` returned only `Rat.den_dvd`, `Rat.den_div_natCast_eq_one_iff`, `Rat.den_div_eq_of_coprime`, `Rat.den_mk`; grep of `Mathlib/Data/Rat/` finds only `den_div_eq_of_coprime`, `den_div_intCast_eq_one_iff`, `den_div_natCast_eq_one_iff`.
- Too specific / inline? It is specific to `approxSet` and used once; it could be inlined as a `have` in `exists_reduced_approx`, but as a separate lemma it keeps that already-long proof readable. Either choice is fine.
- Well-chosen? Yes: minimal hypotheses (κ ≥ 0 needed, see above), statement exactly what the call site consumes.
- Conclusion: `KEEP`. Action: keep as private helper of `exists_reduced_approx`; no change (optional inline).

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private theorem` at Roth/Main.lean:149; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Side note: if anything here were upstreamed it would be the generic fact `((h : ℚ) / q).den ≤ q` for `0 < q` (follows from `Rat.den_dvd` + `Nat.le_of_dvd`), which mathlib lacks as a named lemma; not pursued since this declaration is private.

## Evidence
- `grep -rn approxSet_num_den_mem_aux Roth/`: definition l.149, single use l.174.
- `grep -n "def approxSet" Roth/*.lean`: Roth/Main.lean:55.
- `lean_leansearch` ("denominator of the rational number a / b is at most b for natural b positive", 6 results): `NNRat.den`, `Rat.pnatDen`, `Rat.den_dvd`, `Rat.den_div_natCast_eq_one_iff`, `Rat.num_div_eq_of_coprime`, `Rat.den_mk`; no inequality lemma.
- `lean_loogle "Rat.den (_ / _) ≤ _"`: no results.
- `grep` of `.lake/packages/mathlib/Mathlib/Data/Rat/` for `den_div_*`: only the coprime and eq-one-iff lemmas (Lemmas.lean:240,272,279).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean.
