---
decl: Roth.theta_prefix_lt_aux
file: Roth/Theta.lean
line: 776
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private induction-step helper of Lemma 7 bounding the (p-1)-variable term Theta_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}) via monotonicity in M and the induction hypothesis at delta_1; tied to the project-specific Theta, no mathlib home.
action: Keep as private helper for its sole use in theta_phi_lt_aux (Roth/Theta.lean:886); optionally weaken hanti to the single inequality r (Fin.last (n+1)) at most r (Fin.last n).castSucc and add a docstring citing the source step (clean.tex l.989-1007).
---

# Roth.theta_prefix_lt_aux

## Inventory entry

### `theorem Roth.theta_prefix_lt_aux`
- **Type**: `∀ {n : ℕ} {δ ε M : ℝ}, 0 < δ → δ ≤ ε → ∀ {r q : Fin (n + 2) → ℕ}, (∀ j, r (Fin.last (n + 1)) ≤ r j) → 3 ≤ (r (Fin.last (n + 1)) : ℝ) → (∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc) → ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → ∀ {l : ℕ}, 1 ≤ l → 1 ≤ M → M ≤ (q 0 : ℝ) ^ (ε * (l * r 0)) → (IH for dimension n+1 at parameter ε: for all r q : Fin (n + 1) → ℕ satisfying the four Lemma 7 hypotheses with ε, Θ ((q 0) ^ (ε * r 0)) q r < 10 ^ (n + 1) * ε ^ ((1/2) ^ (n + 1))) → Θ M (fun j : Fin (n + 1) ↦ q j.castSucc) (fun j ↦ l * r j.castSucc) < 10 ^ (n + 1) * ε ^ ((1 / 2 : ℝ) ^ (n + 1))` (declared `private lemma`).
- **What**: In the induction step of Lemma 7 (dimension `p = n + 2`), bounds the `(p-1)`-variable term of `Φ` in Lemma 6: if `1 ≤ M ≤ q_1^{ε l r_1}` (with `ε = δ_1 = δ(1+1/p)` at the call site), then `Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1}) < 10^{p-1} ε^{(1/2)^{p-1}}`. This is the source passage clean.tex l.989–1007: monotonicity of `Θ` in `M`, then verifying the four induction hypotheses for dimension `p-1`, parameter `δ_1`, degrees `l r_j`, then applying the induction hypothesis.
- **How**: `Θ_mono hM1 hM` reduces to `M = q_1^{ε l r_1}`; a `simp [Nat.cast_mul]` rewrite `hCeq` puts the bound in the shape `(q' 0)^(ε * r' 0)` for the truncated tuples `q' = q ∘ castSucc`, `r' = l * r ∘ castSucc`; then `refine ih …` with four obligations: (1) final-degree bound `3 ≤ l r_{p-1}` from `hrlast`, `hanti` and `le_mul_of_one_le_left`; (2) degree ratios `l r_{i+1} ≤ ε l r_i` by a `calc` with `mul_le_mul_of_nonneg_left (hratio _)`, `mul_left_comm`, `mul_le_mul_of_nonneg_right hδε`; (3) the log bound `(n+1)(2(n+1)+1)/ε ≤ log q_1` via `div_le_div₀` (numerator decreases from `p(2p+1)`, denominator increases `δ ≤ ε`) composed with `hq1`; (4) balanced logs scaled by `l` via `mul_le_mul_of_nonneg_left (hqr _)` and `simpa only [mul_assoc, Fin.castSucc_zero]`.
- **Hypotheses**: `hδ0` is needed for `div_le_div₀` (positivity of the smaller denominator). `hδε` drives obligations (2) and (3). `hanti` is used only at `j = (Fin.last n).castSucc`, so it could be weakened to that single inequality (cosmetic; the call site passes `fun j ↦ hanti (Fin.le_last j)`). `hl : 1 ≤ l` is needed for (1). `hM1`, `hM` feed `Θ_mono`. `ih` is the induction hypothesis already specialised to parameter `ε`. All hypotheses are used.
- **Uses from project**: `Roth.Θ` (def, Roth/Theta.lean:68), `Roth.Θ_mono` (Roth/Theta.lean:134). All other names are mathlib (`div_le_div₀`, `le_mul_of_one_le_left`, `mul_le_mul_of_nonneg_left`, `mul_le_mul_of_nonneg_right`, `mul_left_comm`, `mul_nonneg`, `add_nonneg`, `Nat.cast_nonneg`, `Nat.cast_mul`, `Fin.castSucc_zero`, `Fin.last`, `Fin.castSucc`; tactics `push_cast`, `linarith`, `norm_num`, `simp`, `simpa`, `exact_mod_cast`).
- **Used by**: Roth/Theta.lean `Roth.theta_phi_lt_aux` only (l.886, inside the final `exact`, as the `(p-1)`-variable summand of `Φ`, with `ε := δ(1 + 1/(n+2))` and `ih hε0 (theta_delta_succ_lt_aux n hδ).le`). `grep -rn theta_prefix_lt_aux Roth/` returns only the definition (l.776) and this use. Transitively: `theta_phi_lt_aux` (l.840) → `theta_lt_succ_aux` (l.891, use at l.930) → public `Roth.Θ_lt` (Lemma 7, l.962).
- **Visibility**: private
- **Lines**: 776–816, proof length 27 lines (790–816; statement 776–789)
- **Notes**: No docstring. Name ends in `_aux`, so the Step 9a pre-filter would also fire. Faithful to the source step (clean.tex l.989–1007); the source's strict inequality `log q_1 > δ_1^{-1}(p-1)(2p-1)` is used here in non-strict form, which is all the IH needs.

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: in the private `theta_phi_lt_aux` (l.886), on the path to the public `Roth.Θ_lt` (Lemma 7).
- Wrapper of 1–2 mathlib calls? No. It is a 27-line verification of four induction hypotheses plus a monotonicity step about the project's own `Θ`; mathlib has no `Θ`.
- Does mathlib have it? No: the statement is about `Roth.Θ` (a sup of indices over the project's polynomial class `RSet`), which does not exist in mathlib. A `lean_local_search`/mathlib check is moot since the conclusion's head symbol is project-defined.
- Too specific / inline? Very specific, but inlining 27 lines into the already long final `exact` term of `theta_phi_lt_aux` would badly hurt readability; extraction mirrors a self-contained paragraph of the source proof. Better as a separate helper.
- Well-chosen? Yes, modulo a cosmetic weakening: `hanti : ∀ j, r (Fin.last (n + 1)) ≤ r j` is only used at one index; it could be the single inequality `r (Fin.last (n + 1)) ≤ r (Fin.last n).castSucc`. Not worth churn for a private helper. Taking `ih` already specialised to `ε` (rather than the universally quantified IH) keeps the helper independent of `theta_delta_succ_lt_aux`, a reasonable split.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring citing clean.tex l.989–1007 and narrow `hanti`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:776); additionally the name ends in `_aux`.

Side note: even public, it is an internal induction-step lemma about the project-specific quantity `Θ` from Roth's theorem proof; no mathlib home.

## Evidence
- Read Roth/Theta.lean l.740–900 (declaration, neighbouring helpers, sole use site in `theta_phi_lt_aux`) and l.125–140 (`Θ_mono`), l.68 (`Θ` def).
- `grep -rn theta_prefix_lt_aux Roth/`: definition l.776, sole use l.886.
- `grep -n` for `theta_phi_lt_aux`, `theta_lt_succ_aux`, `Θ_lt`: chain l.840 → l.891 (use l.930) → l.962.
- Read `.mathlib-quality/references/clean.tex` l.985–1007: the monotonicity step, the verification of the four induction hypotheses at `δ_1 = δ(1+1/p)` with degrees `l r_j`, and the IH application match this lemma with `p = n + 2`.
- Hypothesis usage determined by reading the proof (no `lean_minimal_hypotheses` run); no Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
