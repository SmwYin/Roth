---
decl: Roth.theta_lt_succ_aux
file: Roth/Theta.lean
line: 891
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private induction step of Lemma 7 (dimension n+2, small delta case) applying Lemma 6 via finSuccEquivLast transport and closing with theta_phi_lt_aux; project-specific Theta estimate, no mathlib home.
action: Keep as private helper for its sole use in Roth.Θ_lt (Roth/Theta.lean:978); optionally add a docstring citing clean.tex l.969-1021.
---

# Roth.theta_lt_succ_aux

## Inventory entry

### `theorem Roth.theta_lt_succ_aux`
- **Type**: `∀ {n : ℕ} {δ : ℝ}, 0 < δ → δ ≤ 1 / ((n : ℝ) + 1 + 1) → ∀ {r q : Fin (n + 2) → ℕ}, 3 ≤ (r (Fin.last (n + 1)) : ℝ) → (∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc) → ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → (ih: Lemma 7 in dimension n+1 for every δ with 0 < δ ≤ 1/(n+1), every r q : Fin (n + 1) → ℕ satisfying the analogous hypotheses) → Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 2) * δ ^ ((1 / 2 : ℝ) ^ (n + 2))` (declared `private lemma`).
- **What**: The induction step of Lemma 7 for `p = n + 2` variables in the case `δ ≤ 1/p`: assuming Lemma 7 in `p - 1` variables, `Θ_p(q_1^{δ r_1}; q; r) < 10^p δ^{(1/2)^p}`. Source: clean.tex l.969–1021 (proof of `roth:lem7`, inductive step: apply Lemma 6, estimate `M` and `Φ` for every allowed `l`).
- **How**: Derives `δ < 1` from `hδ` (`div_lt_one`), `Antitone r` from `hratio` via `Fin.antitone_iff_succ_le` and `mul_le_of_le_one_left`, `1 < q j` via `theta_denominators_one_lt_aux`, and the Lemma 6 ratio hypothesis `r_last ≤ δ r_j` (`hratio'`, via `Fin.succ_last`, `mul_le_mul_of_nonneg_left`). Transports `Θ` along `finSuccEquivLast : Fin (n + 2) ≃ Option (Fin (n + 1))` with `Θ_equiv`, applies Lemma 6 `Θ_option_le` (with `r₁ = r 0`, `B = q_0^{δ r_0} ≥ 1` by `Real.one_le_rpow`), unfolds `lem6Φ`, rewrites with `lt_div_iff₀'` and `Finset.sup'_lt_iff`, and closes each `l` by `theta_phi_lt_aux`.
- **Hypotheses**: All used. `hδ0`, `hδ` give `δ < 1` and feed `Θ_option_le` and `theta_phi_lt_aux`; `hrlast`, `hratio` give antitonicity, positivity and the Lemma 6 ratio condition; `hq1`, `hqr` give `1 < q j` and are forwarded; `ih` is forwarded to `theta_phi_lt_aux`. The `ih` hypothesis carries an upper bound `δ ≤ 1/(n+1)` that the caller discards (`fun {δ} hδ0 _ ↦ ih hδ0`), i.e. it is weaker than the full IH available; this is a deliberate narrowing, no redundancy.
- **Uses from project**: `Roth.Θ` (Roth/Theta.lean:68), `Roth.Θ_equiv` (l.159), `Roth.lem6Φ` (l.275), `Roth.Θ_option_le` (l.593, Lemma 6), `Roth.theta_denominators_one_lt_aux` (l.833), `Roth.theta_phi_lt_aux` (l.840). Mathlib names: `div_lt_one`, `Fin.antitone_iff_succ_le`, `mul_le_of_le_one_left`, `Fin.zero_le`, `Fin.le_last`, `Fin.succ_last`, `Fin.castSucc_le_castSucc_iff`, `mul_le_mul_of_nonneg_left`, `finSuccEquivLast`, `finSuccEquivLast_symm_none`, `finSuccEquivLast_symm_some`, `Nat.zero_lt_of_lt`, `Real.one_le_rpow`, `Fintype.card_fin`, `lt_div_iff₀'`, `Finset.sup'_lt_iff`, `Function.comp_def`.
- **Used by**: Roth/Theta.lean `Roth.Θ_lt` only (l.978, `succ` case of the induction when `δ ≤ 1/(n+2)`). `grep -rn theta_lt_succ_aux Roth/` returns only the definition (l.891) and this use. Transitively feeds every user of the public Lemma 7 `Roth.Θ_lt`.
- **Visibility**: private
- **Lines**: 891–930, proof length 28 lines (903–930; statement 891–902)
- **Notes**: No docstring. Name ends in `_aux`. Faithful to the source inductive step; the indexing transport `Fin (n+2) ≃ Option (Fin (n+1))` (last variable becomes `none`) is a formalisation artefact matching the `Option τ` form of Lemma 6.

## Junk check (Step 8)
- Used anywhere? Yes, once: in public `Roth.Θ_lt` (Lemma 7, l.978).
- Wrapper of 1–2 mathlib calls? No. It is a 28-line assembly of project Lemma 6 (`Θ_option_le`), `Θ_equiv` transport and the per-`l` helper `theta_phi_lt_aux`, about the project-defined `Θ`.
- Does mathlib have it? No: the head symbol `Roth.Θ` (index supremum from the proof of Roth's theorem) is a project definition with no mathlib counterpart, so no search can match.
- Too specific / inline? Specific, but inlining into the `induction` of `Θ_lt` would make that proof ~60 lines against style guidance; the extraction mirrors the source's inductive-step paragraph and is clean.
- Well-chosen? Yes. The derived facts `hδ1`, `hanti` are computed here once and passed to `theta_phi_lt_aux`, a reasonable split.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring citing clean.tex l.969–1021.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:891); additionally the name ends in `_aux`.

Side note: even public, it is an internal induction step about the project-specific quantity `Θ` from the proof of Roth's theorem; no mathlib home.

## Evidence
- Read Roth/Theta.lean l.860–980 (declaration, preceding helper `theta_phi_lt_aux`, the sole use in `Θ_lt`), plus signatures of `Θ_equiv` (l.159), `lem6Φ` (l.275), `Θ_option_le` (l.590–597).
- `grep -rn theta_lt_succ_aux Roth/`: definition l.891, sole use l.978.
- `grep -n` for `lem7`/`lem6` labels in `.mathlib-quality/references/clean.tex`: inductive step at l.969–1021 matches this lemma with `p = n + 2`.
- Prior report read: `.mathlib-quality/overview/mathlibable/Roth.theta_phi_lt_aux.md`.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
