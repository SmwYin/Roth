---
decl: Roth.theta_scaled_unique_le_aux
file: Roth/Theta.lean
line: 742
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-variable step of the Lemma 7 induction (Theta_1(M; q2; l r2) at most delta from Lemma 5 plus monotonicity in B and the balanced-log condition); about the project-specific Theta, so nothing upstreamable.
action: Keep as private helper for its sole use in theta_phi_lt_aux (Roth/Theta.lean:883); optionally add a short docstring citing the source chain in the proof of Lemma 7.
---

# Roth.theta_scaled_unique_le_aux

## Inventory entry

### `theorem Roth.theta_scaled_unique_le_aux`
- **Type**: `∀ {δ M : ℝ} {q₁ q₂ r₁ r₂ l : ℕ}, 1 < q₁ → 0 < r₁ → 0 < l → (r₁ : ℝ) * Real.log q₁ ≤ r₂ * Real.log q₂ → 1 ≤ M → M ≤ (q₁ : ℝ) ^ (δ * (l * r₁)) → Θ M (fun _ : Unit ↦ q₂) (fun _ ↦ l * r₂) ≤ δ` (declared `private lemma`).
- **What**: In one variable (index type `Unit`), if `q₁ > 1`, `r₁, l > 0`, the balanced-logarithm inequality `r₁ log q₁ ≤ r₂ log q₂` holds and `1 ≤ M ≤ q₁^{δ l r₁}`, then `Θ_1(M; q₂; l r₂) ≤ δ`. This is exactly the displayed chain in the source proof of Lemma 7: `Θ_1(M; q_p; l r_p) ≤ Θ_1(q_1^{δ_1 l r_1}; q_p; l r_p) ≤ log(q_1^{δ_1 l r_1})/(l r_p log q_p) ≤ δ_1` (clean.tex, around l.985), with `δ` playing the role of `δ_1`.
- **How**: First derives side facts: `0 ≤ δ` from `1 ≤ M ≤ q₁^{δ l r₁}` via `Real.rpow_le_rpow_left_iff` and `nonneg_of_mul_nonneg_left`; `0 < r₂ log q₂` from `hqr` and `Real.log_pos`; hence `0 < log q₂` (`pos_of_mul_pos_right`), `0 < r₂` (`pos_of_mul_pos_left`) and `1 < q₂` (`Real.log_pos_iff`). Then chains `Roth.Θ_mono` (to raise `M` to `q₁^{δ l r₁}`) with `Roth.Θ_unique_le` (Lemma 5, `Θ_1(B; q; r) ≤ log B / (r log q)`), rewrites with `Real.log_rpow` and `div_le_iff₀`, and closes with `nlinarith only [mul_le_mul_of_nonneg_left hqr ...]`.
- **Hypotheses**: All six are used in the proof. `hq₁` gives `log q₁ > 0` (needed for `δ ≥ 0` and `q₂ > 1`); `hr₁`, `hl` are needed because if `r₁ = 0` or `l = 0` then `hM` forces `M ≤ 1` with `δ` unconstrained (possibly negative), while `Θ` is nonnegative-valued in that regime, so the conclusion would fail; `hM1` is required by `Θ_mono`/`Θ_unique_le` and also rules out `M < 1` with negative `δ`; `hqr` is the balanced-log comparison that converts the `q₂, r₂` denominator to `q₁, r₁`. (Necessity argued informally from the proof; no weakening experiment run, as the lemma is private.)
- **Uses from project**: `Roth.Θ` (Roth/Theta.lean:68), `Roth.Θ_mono` (Roth/Theta.lean:134), `Roth.Θ_unique_le` (Roth/Theta.lean:256).
- **Used by**: Roth/Theta.lean `Roth.theta_phi_lt_aux` only (l.883, the one-variable term of `Φ`, applied with `δ := ε = δ(1 + 1/(n+2))` via `hM.le`). `grep -rn theta_scaled_unique_le_aux Roth/` returns only the definition (l.742) and this use. Transitively: `theta_phi_lt_aux` → `theta_lt_succ_aux` (l.930) → public `Roth.Θ_lt` (Lemma 7, l.978).
- **Visibility**: private
- **Lines**: 742–765, proof length 21 lines (745–765)
- **Notes**: No docstring (unlike the neighbouring `lem6M_lt`, `lem7_Φ_bound`, `lem7_numeric`, which cite the source). Name ends in `_aux`, so the Step 9a pre-filter would also fire.

## Junk check (Step 8)
- Used anywhere? Yes, once: the one-variable summand in the private `theta_phi_lt_aux` (l.883), on the path to the public `Roth.Θ_lt` (Lemma 7).
- Wrapper of 1–2 mathlib calls? No. It combines two project lemmas (`Θ_mono`, `Θ_unique_le`) with about ten lines of positivity/side-condition derivations (`q₂ > 1`, `r₂ > 0`, `δ ≥ 0`) and a real-arithmetic finish.
- Does mathlib have it? No: it is about the project-defined `Roth.Θ` (a supremum of polynomial indices), which has no mathlib counterpart. The arithmetic ingredients (`Real.log_rpow`, `div_le_iff₀`, `Real.rpow_le_rpow_left_iff`, `Real.log_pos_iff`) are already mathlib lemmas and are used directly.
- Too specific / inline? Could be inlined into `theta_phi_lt_aux` (single use), but that proof is already a long `exact` combining several terms; extracting this step mirrors one display of the source proof and keeps the caller readable. Keeping it separate is the better style.
- Well-chosen? Yes. The statement is the minimal form needed at the call site: derived facts (`q₂ > 1`, `r₂ > 0`, `δ ≥ 0`) are proved inside rather than demanded as hypotheses, so the caller passes only data it already has.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring citing "§5, proof of Lemma 7 (`Θ_1(M; q_p; l r_p) ≤ ... ≤ δ_1`)" for consistency with the neighbouring `lem7_*` lemmas.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:742); additionally the name ends in `_aux`.

Side note: the statement concerns the project-specific `Roth.Θ`, so even a public version would have no mathlib home; any upstreaming question belongs to `Roth.Θ` / `Roth.Θ_unique_le`, assessed separately.

## Evidence
- `grep -rn theta_scaled_unique_le_aux Roth/`: definition l.742, sole use l.883 (inside `theta_phi_lt_aux`, l.840).
- `grep -rn theta_phi_lt_aux Roth/` and `grep -rn theta_lt_succ_aux Roth/`: chain to `Roth.Θ_lt` (l.930, l.978).
- Read `Roth.Θ` (l.68), `Roth.Θ_mono` (l.134), `Roth.Θ_unique_le` (l.256) to confirm the dependencies and their hypotheses.
- Read `.mathlib-quality/references/clean.tex` around l.964–990: the displayed chain `Θ_1(M; q_p; l r_p) ≤ ... ≤ δ_1` "by Lemma roth:lem5" matches this lemma exactly.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
