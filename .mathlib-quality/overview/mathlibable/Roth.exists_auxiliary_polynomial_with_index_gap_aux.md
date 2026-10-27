---
decl: Roth.exists_auxiliary_polynomial_with_index_gap_aux
file: Roth/MainLemma.lean
line: 692
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 assembly step combining the auxiliary polynomial (exists_auxiliary_polynomial_of_log_bound_aux) with Lemma 7 (theta_lt_eta_of_sq_log_bound_aux) to get the strict gap gam - eta + Theta < index; single call site in main_lemma; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:747 (Roth.main_lemma); optionally add a docstring citing Lemmas 7-9 and drop the duplicated delta > 0 derivation shared with theta_lt_eta_of_sq_log_bound_aux (l.679-680 vs l.709-710); no other change.
---

# Roth.exists_auxiliary_polynomial_with_index_gap_aux

## Inventory entry

### `theorem Roth.exists_auxiliary_polynomial_with_index_gap_aux`
- **Type**: `∀ {α : ℝ} {f : Polynomial ℤ}, f.Monic → Polynomial.aeval α f = 0 → ∀ {A : ℝ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m : ℕ} [NeZero m] {δ : ℝ}, 0 ≤ δ → δ ≤ 1 / m → ∀ {r : Fin m → ℕ}, 3 ≤ r (Fin.rev 0) → (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) → ∀ {q : Fin m → ℕ}, 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → ∃ W : MvPolynomial (Fin m) ℤ, W ∈ RSet ((q 0 : ℝ) ^ (δ * r 0)) r ∧ gam δ f.natDegree m - eta δ m + Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < index (map (Int.castRingHom ℝ) W) (fun _ ↦ α) r ∧ ∀ i k : Fin m →₀ ℕ, |eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k W)))| < (mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ)`
- **What**: Under the hypotheses of Roth's Lemma 9 (α a root of a monic integer polynomial f with coefficients bounded by A, m ≥ 1, 0 ≤ δ ≤ 1/m, r_m ≥ 3, chain condition (31) r_{j+1}/δ ≤ r_j, log bound (32), and (33) r_1 log q_1 ≤ r_j log q_j), there is an integer polynomial W in the set R_m(q_1^{δ r_1}; r) whose index at (α, …, α) strictly exceeds γ − η + Θ_m(q_1^{δ r_1}; q; r), and all of whose iterated Hasse derivatives ∂_i ∂_k W at (α, …, α) are bounded in absolute value by B_1^{1+3δ}, where B_1 = ⌊q_1^{δ r_1}⌋. This is the "index gap" step of Lemma 9 before the derivative-shifting step (Lemma 8 style) that produces Q.
- **How**: Writes m = m' + 1 (`Nat.exists_eq_succ_of_ne_zero`). Drops the A- and α-log terms of (32) (nonnegative by `Real.log_nonneg`, `le_add_of_nonneg_right`, `abs_nonneg`) to get h32' : 2m+1 ≤ δ² log q_1; deduces δ > 0 from h32'. Shows `r` is antitone via `Fin.antitone_iff_succ_le` using δ ≤ 1/m ≤ 1 (`le_div_self`, `div_le_one`) and h31b, hence ∑ r_j ≤ m·r_1 (`Finset.sum_le_card_nsmul`) and r_j ≥ r_m ≥ 3 > 0 (`Fin.le_last`). Applies `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (Roth/MainLemma.lean:643) to get W ∈ RSet with γ ≤ index and the Hasse-derivative bound, then closes the strict gap by `linarith only` with `Roth.theta_lt_eta_of_sq_log_bound_aux` (Roth/MainLemma.lean:671; Θ < η), after rewriting δ ≤ 1/m as δ·m ≤ 1 via `le_div_iff₀`.
- **Hypotheses**: `hf`, `hfα`, `hA` (passed to exists_auxiliary_polynomial_of_log_bound_aux; `hA 0` also used for log(1+A) ≥ 0); `hδ0` (upgraded to δ > 0); `hδm` (antitonicity of r and Lemma 7's δm ≤ 1); `hrlast` (positivity of all r_j and Lemma 7); `h31b` (antitonicity and Lemma 7); `h32` (auxiliary polynomial and, weakened, Lemma 7); `h33` (Lemma 7). All used.
- **Uses from project**: `Roth.RSet` (Roth/Theta.lean:56), `Roth.Θ` (Roth/Theta.lean:68), `Roth.index` (Roth/Index.lean:58), `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.eta` (Roth/MainLemma.lean:66), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (Roth/MainLemma.lean:643), `Roth.theta_lt_eta_of_sq_log_bound_aux` (Roth/MainLemma.lean:671). Mathlib names used: `Nat.exists_eq_succ_of_ne_zero`, `NeZero.ne`, `le_add_of_nonneg_right`, `mul_nonneg`, `Real.log_nonneg`, `abs_nonneg`, `Nat.succ_le_succ`, `Fin.antitone_iff_succ_le`, `le_div_self`, `div_le_one`, `Finset.sum_le_card_nsmul`, `Fin.zero_le`, `Fin.le_last`, `le_div_iff₀`, `MvPolynomial.map`, `MvPolynomial.eval`, `Int.castRingHom`.
- **Used by**: Roth/MainLemma.lean:747 `Roth.main_lemma` (l.735). `grep -rn exists_auxiliary_polynomial_with_index_gap_aux Roth/` gives only l.692 (definition) and l.747 (use).
- **Visibility**: private
- **Lines**: 692–725, proof length 23 lines (703–725)
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. The δ > 0 derivation from the log bound is duplicated in the callee `theta_lt_eta_of_sq_log_bound_aux` (l.679–680), and the m = m'+1 reindex is done in both. The output conclusion (RSet membership, index gap, Hasse bound) is exactly what `main_lemma` feeds into `exists_hasseDeriv_index_eval_bound_aux` (l.477) and `Roth.index_le_Θ` (Roth/Theta.lean:99).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:747 in `Roth.main_lemma`.
- Wrapper of 1–2 mathlib calls? No. It combines two project lemmas (`exists_auxiliary_polynomial_of_log_bound_aux`, `theta_lt_eta_of_sq_log_bound_aux`) with genuine glue: antitonicity of r from (31) and δ ≤ 1, the bound ∑ r_j ≤ m r_1, positivity of r_j, and weakening (32).
- Does mathlib have it? No. The statement is about project-defined `RSet`, `Θ`, `index`, `gam`, `eta`, `mainCoeffBound` (Roth's auxiliary-polynomial machinery); mathlib has no Roth index theory. Grep of `.lake/packages/mathlib/Mathlib/` for `auxiliary_polynomial`/`index_gap`: no hits.
- Too specific (inline?)? Single call site. Inlining into `main_lemma` (currently 23 lines of proof after the statement) would produce a ~45-line proof mixing the hypothesis bookkeeping with the derivative-shift step; the split mirrors the paper (first get W with large index, then shift by derivatives to get Q non-vanishing at h/q). Keep.
- Well-chosen statement? Yes: its hypotheses are verbatim those of `main_lemma`, so the call is a direct application, and its conclusion is phrased for the immediate `linarith` in the caller. A docstring citing Lemmas 7 and 9 would help; the duplicated δ > 0 derivation with the callee could be removed by passing δ > 0 in, a cosmetic improvement only.
- Conclusion: `KEEP`. Action: keep as private helper of Roth/MainLemma.lean:747; optionally add a docstring.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:692; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the public result it serves, `Roth.main_lemma`, is assessed under its own entry.

## Evidence
- `grep -rn exists_auxiliary_polynomial_with_index_gap_aux Roth/`: definition Roth/MainLemma.lean:692, single use Roth/MainLemma.lean:747.
- Read the body (Roth/MainLemma.lean:692–725), the callees `exists_auxiliary_polynomial_of_log_bound_aux` (l.643), `theta_lt_eta_of_sq_log_bound_aux` (l.671), the caller `main_lemma` (l.735–762) and its other helpers `exists_hasseDeriv_index_eval_bound_aux` (l.477), `index_le_Θ` (Roth/Theta.lean:99), and the defs `gam`, `eta`, `mainCoeffBound`, `RSet`, `Θ`, `index`.
- `grep -rln "auxiliary_polynomial\|index_gap" .lake/packages/mathlib/Mathlib/`: no matches.
- Earlier reports consulted: `Roth.theta_lt_eta_of_sq_log_bound_aux.md`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux.md`.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
