---
decl: Roth.one_lt_roth_eval_bound_aux
file: Roth/Main.lean
line: 453
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private step of the proof of Roth's theorem (section 7) combining main_lemma (Lemma 9) with the integrality lower bound one_le_prod_pow_mul_abs_eval and the Taylor upper bound abs_eval_lt_of_le_index into the inequality 1 < (prod q_j^r_j) * upper bound; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
action: Keep as private helper of its single call site Roth/Main.lean:562 (roth_of_isIntegral); no change.
---

# Roth.one_lt_roth_eval_bound_aux

## Inventory entry

### `theorem Roth.one_lt_roth_eval_bound_aux`
- **Type**: `∀ {α κ : ℝ} {f : Polynomial ℤ}, f.Monic → Polynomial.aeval α f = 0 → ∀ {A : ℝ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m : ℕ} [NeZero m] {δ : ℝ}, 0 ≤ δ → δ ≤ 1 / m → ∀ {r : Fin m → ℕ}, (∀ j, 0 < r j) → 3 ≤ r (Fin.rev 0) → (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) → ∀ {q : Fin m → ℕ}, (∀ j, 0 < q j) → 0 ≤ κ → ∀ {h : Fin m → ℤ}, (∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ) → (∀ j, IsCoprime (h j) (q j : ℤ)) → 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → 1 < (∏ j, (q j : ℝ) ^ r j) * ((∏ j, ((r j : ℝ) + 1)) * (mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ) * (q 0 : ℝ) ^ (-(r 0 : ℝ) * (gam δ f.natDegree m - eta δ m) * κ))`
- **What**: Let α be a root of a monic integer polynomial f with coefficients bounded by A, let δ, m, the degrees r_j, the denominators q_j and the coprime approximations h_j/q_j (with |α − h_j/q_j| ≤ q_j^{−κ}) satisfy the hypotheses (31b), (32), (33) of Lemma 9 of the source. Then 1 < (∏_j q_j^{r_j}) · (∏_j (r_j + 1)) · B^{1+3δ} · q_0^{−r_0 (γ − η) κ}, where B = ⌊q_0^{δ r_0}⌋, γ = gam δ n m, η = eta δ m. This is the "the nonzero integer value is at least 1 but at most the Taylor bound" comparison of §7 of the source, stated before taking logarithms.
- **How**: `Roth.main_lemma` (Lemma 9, Roth/MainLemma.lean:735) yields Q ∈ ℤ[X_1..X_m], Q ≠ 0, with degreeOf j Q ≤ r j, index of Q at (α,…,α) > γ − η, Q(h/q) ≠ 0, and all Hasse derivatives at α bounded by B^{1+3δ}. Degree bounds transfer to `map (Int.castRingHom ℝ) Q` via mathlib's `MvPolynomial.degreeOf_eq_sup` and `MvPolynomial.support_map_of_injective` with `Int.cast_injective`. The size condition q_0^{r_0/r_j} ≤ q_j is derived from h33 via `Real.rpow_le_iff_le_log`, `div_mul_eq_mul_div`, `div_le_iff₀` and `linarith`. Finally `Roth.one_le_prod_pow_mul_abs_eval` (1 ≤ ∏ q_j^{r_j} · |Q(h/q)|) is chained with `mul_lt_mul_of_pos_left` applied to `Roth.abs_eval_lt_of_le_index` (Taylor upper bound) and positivity of the product via `Finset.prod_pos`/`pow_pos`.
- **Hypotheses**: hf, hfα, hA, hδ0, hδm, hrlast, h31b, h32, h33, hcop are all passed to `main_lemma`; hr0 is used for `hqr` (division by r j; not derivable from h31b since δ = 0 is allowed, making h31b vacuous); hq0 for positivity and for both bounding lemmas; hκ0 and happ for `abs_eval_lt_of_le_index`. All used, none redundant.
- **Uses from project**: `Roth.main_lemma` (Roth/MainLemma.lean:735), `Roth.one_le_prod_pow_mul_abs_eval` (Roth/Main.lean:324), `Roth.abs_eval_lt_of_le_index` (Roth/Main.lean:380), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.eta` (Roth/MainLemma.lean:66); indirectly through the main_lemma conclusion `Roth.index` and `Roth.hasseDeriv` (destructured, not named in the body except as `hidx_strict`/`hC`).
- **Used by**: Roth/Main.lean:562 `Roth.roth_of_isIntegral` (supplies the `hone` argument of `roth_log_bound_aux`). `grep -rn one_lt_roth_eval_bound_aux Roth/` gives only the definition (l.453) and this use. Transitively feeds `Roth.roth` (main theorem).
- **Visibility**: private
- **Lines**: 453–478, proof length 15 lines (464–478; statement 453–463)
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; preceded by a plain `--` comment, not a docstring (acceptable for private). The three-line `hdmap` (degreeOf preserved under injective coefficient map) has no direct mathlib lemma (`degreeOf_map*` absent; only `MvPolynomial.degrees_map_of_injective`, Mathlib/Algebra/MvPolynomial/Degrees.lean:196, exists) and the same `support_map_of_injective` idiom appears at Roth/Main.lean:333; a small candidate upstream lemma `MvPolynomial.degreeOf_map_of_injective`, but not worth a project lemma for two uses.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Main.lean:562 in `roth_of_isIntegral`, where it produces the key inequality fed to `roth_log_bound_aux`.
- Wrapper of 1–2 mathlib calls? No. It combines three substantial project results (`main_lemma`, `one_le_prod_pow_mul_abs_eval`, `abs_eval_lt_of_le_index`) plus two small derived facts (`hdmap`, `hqr`).
- Does mathlib have it? No: the statement is phrased in terms of Roth-specific quantities (`mainCoeffBound`, `gam`, `eta`) and the conclusion of Lemma 9; no general content. `lean_local_search`-style check unnecessary beyond grep: mathlib has no `degreeOf_map` lemma (grep over `.lake/packages/mathlib/Mathlib/` for `degreeOf_map` empty), so `hdmap` is not replaceable by a single call.
- Too specific (inline?)? It is specific to its one call site and could be inlined into `roth_of_isIntegral`, but it was deliberately factored out together with its sibling `_aux` lemmas (`exists_roth_parameters_aux`, `exists_roth_approximants_aux`, `roth_product_bound_aux`, `roth_log_bound_aux`) so that the main proof reads as a short chain mirroring §7 of the source. Keep factored.
- Well-chosen statement? Yes: hypotheses are exactly those consumed by `main_lemma` plus what the two bounding lemmas need; the conclusion is shaped to match the `hone` hypothesis of `roth_log_bound_aux` verbatim (with B := mainCoeffBound …, G := gam − eta). The non-strict forms (`hδ0 : 0 ≤ δ`, `happ` with `≤`) are the weakest that work; the caller passes `.le` weakenings.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site (Roth/Main.lean:562); no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Main.lean:453; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable-looking ingredients are assessed under their own entries (`Roth.main_lemma.md`, `Roth.one_le_prod_pow_mul_abs_eval.md`, `Roth.abs_eval_lt_of_le_index.md`).

## Evidence
- `grep -rn one_lt_roth_eval_bound_aux Roth/`: definition Roth/Main.lean:453, single use Roth/Main.lean:562.
- Read the body (Roth/Main.lean:452–478), the call site (Roth/Main.lean:547–563) and the dependency statements: `main_lemma` (Roth/MainLemma.lean:735–746), `one_le_prod_pow_mul_abs_eval` (Roth/Main.lean:324), `abs_eval_lt_of_le_index` (Roth/Main.lean:380), `gam`/`eta`/`mainCoeffBound` (Roth/MainLemma.lean:63, 66, 69).
- `grep -rn "degreeOf_map"` over `.lake/packages/mathlib/Mathlib/`: no results; `degrees_map_of_injective` at Mathlib/Algebra/MvPolynomial/Degrees.lean:196, `degreeOf_eq_sup` at l.223, `support_map_of_injective` at Mathlib/Algebra/MvPolynomial/Eval.lean:466.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
