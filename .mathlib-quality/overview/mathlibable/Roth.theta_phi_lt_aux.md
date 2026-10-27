---
decl: Roth.theta_phi_lt_aux
file: Roth/Theta.lean
line: 840
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private induction-step helper of Lemma 7 bounding Phi + sqrt Phi + sqrt delta below half the target for each admissible l in Lemma 6; assembles project-specific Theta and lem6M estimates, no mathlib home.
action: Keep as private helper for its sole use in theta_lt_succ_aux (Roth/Theta.lean:930); optionally drop the derivable hypotheses hanti and hδ1 (both follow from hδ and hratio, as theta_lt_succ_aux shows) and add a docstring citing clean.tex l.969-1018.
---

# Roth.theta_phi_lt_aux

## Inventory entry

### `theorem Roth.theta_phi_lt_aux`
- **Type**: `∀ {n : ℕ} {δ : ℝ}, 0 < δ → δ ≤ 1 / ((n : ℝ) + 1 + 1) → δ < 1 → ∀ {r q : Fin (n + 2) → ℕ}, Antitone r → 3 ≤ (r (Fin.last (n + 1)) : ℝ) → (∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc) → ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → (IH: Lemma 7 for dimension n+1, universally quantified over δ, r, q) → ∀ {l : ℕ}, l ∈ Finset.Icc 1 (r (Fin.last (n + 1)) + 1) → let M := lem6M (n + 2) (r 0) ((q 0 : ℝ) ^ (δ * r 0)) l; let Φ := Θ M (fun _ : Unit ↦ q (Fin.last (n + 1))) (fun _ ↦ l * r (Fin.last (n + 1))) + Θ M (fun j : Fin (n + 1) ↦ q j.castSucc) (fun j ↦ l * r j.castSucc); Φ + √Φ + √δ < (10 ^ (n + 2) * δ ^ ((1 / 2 : ℝ) ^ (n + 2))) / 2` (declared `private lemma`).
- **What**: The per-`l` core of the induction step of Lemma 7 (dimension `p = n + 2`): for every admissible `l ∈ [1, r_p + 1]`, with `M` and `Φ` as in Lemma 6, `Φ + Φ^{1/2} + δ^{1/2} < 10^p δ^{(1/2)^p} / 2`. Source: clean.tex l.969–1018 (estimate of `M`, of the one-variable term by `δ_1`, of the `(p-1)`-variable term by the IH at `δ_1 = δ(1+1/p)`, then the numeric absorption `Φ < 3·10^{p-1} δ^{(1/2)^{p-1}}` and the final bound).
- **How**: Derives `0 < r j` from `hrlast` + `hanti`, `1 < q 0` via `theta_denominators_one_lt_aux`; sets `ε = δ(1 + 1/(n+2))`; `one_le_lem6M` gives `1 ≤ M`; `lem6M_lt` (with `l ≤ r 0` obtained from `l ≤ r_p + 1`, `r_p ≤ r_1 ≤ δ r_0 < r_0` via `hratio 0`, `mul_lt_of_lt_one_left`) gives `M < q_1^{ε l r_1}`; `lem7_Φ_bound` gives `ε + 10^{p-1} ε^{(1/2)^{p-1}} < 3·10^{p-1} δ^{(1/2)^{p-1}}`; then `lt_div_iff₀'` and `lem7_numeric` reduce the goal to `Φ ≤ 3·10^{p-1}δ^{…}`, closed by `add_lt_add_of_le_of_lt` of `theta_scaled_unique_le_aux` (one-variable term `≤ ε`) and `theta_prefix_lt_aux` (prefix term `< 10^{p-1} ε^{…}`, fed `ih hε0 (theta_delta_succ_lt_aux n hδ).le`).
- **Hypotheses**: All are used. `hδ1` and `hanti` are redundant given the others: `hδ1` follows from `hδ` (as derived in `theta_lt_succ_aux`, l.903–904) and `hanti` follows from `hratio` + `hδ1` (as derived via `Fin.antitone_iff_succ_le` at l.905–906); the caller passes them already computed, so this is a deliberate split, cosmetic only. `hl` bounds both sides of `l`; `ih` is the full universally quantified Lemma 7 IH.
- **Uses from project**: `Roth.Θ` (Roth/Theta.lean:68), `Roth.lem6M` (l.270), `Roth.one_le_lem6M` (l.279), `Roth.lem6M_lt` (l.649), `Roth.lem7_Φ_bound` (l.678), `Roth.lem7_numeric` (l.709), `Roth.theta_scaled_unique_le_aux` (l.742), `Roth.theta_delta_succ_lt_aux` (l.767), `Roth.theta_prefix_lt_aux` (l.776), `Roth.theta_denominators_one_lt_aux` (l.833). Mathlib names: `Finset.mem_Icc`, `Fin.le_last`, `Real.one_le_rpow`, `mul_pos`, `add_pos`, `mul_nonneg`, `Nat.cast_nonneg`, `Nat.succ_le_succ`, `Nat.succ_le_of_lt`, `Nat.zero_lt_succ`, `mul_lt_of_lt_one_left`, `lt_div_iff₀'`, `add_lt_add_of_le_of_lt`, `le_mul_of_one_le_right`, `le_add_of_nonneg_right`, `Nat.add_sub_cancel`, `Nat.cast_add`, `Nat.cast_one`.
- **Used by**: Roth/Theta.lean `Roth.theta_lt_succ_aux` only (l.930, `exact fun l hl ↦ theta_phi_lt_aux … ih hl` after `Finset.sup'_lt_iff`). `grep -rn theta_phi_lt_aux Roth/` returns only the definition (l.840) and this use. Transitively: `theta_lt_succ_aux` (l.891) → public `Roth.Θ_lt` (Lemma 7, l.962).
- **Visibility**: private
- **Lines**: 840–889, proof length 33 lines (857–889; statement 840–856)
- **Notes**: No docstring. Name ends in `_aux`. Faithful to the source step; the `let`-bound `M`, `Φ` in the statement are removed by `dsimp only` and match the `lem6Φ` unfolding produced at the call site.

## Junk check (Step 8)
- Used anywhere? Yes, once: in the private `theta_lt_succ_aux` (l.930), on the path to public `Roth.Θ_lt`.
- Wrapper of 1–2 mathlib calls? No. It is a 33-line assembly of six project lemmas (`lem6M_lt`, `lem7_Φ_bound`, `lem7_numeric`, `theta_scaled_unique_le_aux`, `theta_prefix_lt_aux`, `theta_delta_succ_lt_aux`) about the project-defined `Θ` and `lem6M`.
- Does mathlib have it? No: head symbols `Roth.Θ` and `Roth.lem6M` are project definitions with no mathlib counterpart, so no search can match.
- Too specific / inline? Very specific, but it is the per-`l` body of a `Finset.sup'_lt_iff` closure; inlining it into `theta_lt_succ_aux` (already ~40 lines) would create a ~75-line proof against the style guidance. Extraction mirrors the source's "estimate M and Φ" paragraph.
- Well-chosen? Yes. Cosmetic: `hδ1` and `hanti` could be derived internally from `hδ` and `hratio` (shortening the signature and call), at the cost of re-deriving them; not worth churn for a private helper.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring citing clean.tex l.969–1018 and drop the derivable hypotheses.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:840); additionally the name ends in `_aux`.

Side note: even public, it is an internal induction-step lemma about the project-specific quantities `Θ` and `lem6M` from the proof of Roth's theorem; no mathlib home.

## Evidence
- Read Roth/Theta.lean l.800–940 (declaration, neighbouring helpers, sole use site in `theta_lt_succ_aux`), plus signatures at l.270, 279, 649, 678, 709.
- `grep -rn theta_phi_lt_aux Roth/`: definition l.840, sole use l.930.
- `grep -n` for each project helper used in the body to confirm locations.
- Read `.mathlib-quality/references/clean.tex` l.969–1018: estimate of `M < q_1^{δ_1 l r_1}`, the two `Θ` terms, and the numeric absorption match this lemma with `p = n + 2`.
- Prior reports read: `.mathlib-quality/overview/mathlibable/Roth.theta_prefix_lt_aux.md`.
- Hypothesis usage and redundancy determined by reading the proof and the caller (no `lean_minimal_hypotheses` run); no Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
