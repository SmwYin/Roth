---
decl: Roth.exists_roth_approximants_aux
file: Roth/Main.lean
line: 429
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private step of the proof of Roth's theorem choosing m reduced approximants h_j/q_j and balanced degrees r_j (source eqs. 31-33, 50-53) by chaining exists_approximants and exists_degrees plus an antitonicity argument; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
action: Keep as private helper of its single call site Roth/Main.lean:557 (roth_of_isIntegral); no change.
---

# Roth.exists_roth_approximants_aux

## Inventory entry

### `theorem Roth.exists_roth_approximants_aux`
- **Type**: `∀ {α κ : ℝ}, Irrational α → 0 < κ → (approxSet α κ).Infinite → ∀ (m : ℕ) [NeZero m] {δ : ℝ}, 0 < δ → δ ≤ 1 → ∀ (A : ℝ), ∃ (h : Fin m → ℤ) (q r : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧ (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ (∀ j, 0 < r j) ∧ 3 ≤ r (Fin.rev 0) ∧ (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) ∧ (∀ j, r j ≤ r 0) ∧ (2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) < δ ^ 2 * Real.log (q 0)) ∧ (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧ ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))`
- **What**: Let α be irrational, κ > 0, and suppose α has infinitely many approximations h/q with |α − h/q| < q^{−κ}. Then for every m ≥ 1, 0 < δ ≤ 1 and real A there are m reduced approximations h_j/q_j (gcd(h_j, q_j) = 1, q_j > 1) and positive integer degrees r_j such that: the last degree r_{m−1} is ≥ 3; r_{j+1}/δ ≤ r_j (so r is non-increasing and r_j ≤ r_0); log q_0 is so large that 2m + 1 + 2m log(1 + A) + 2m log(1 + |α|) < δ² log q_0 (eq. (32)); and the r_j log q_j are balanced: r_0 log q_0 ≤ r_j log q_j < (1 + δ/10) r_0 log q_0 (eqs. (33), (53)). This is the approximant-and-degree choice of §7 of the source, packaged for the contradiction argument.
- **How**: `Roth.exists_approximants` with L := (2m + 1 + 2m log(1 + A) + 2m log(1 + |α|))/δ² gives h, q, membership, coprimality, q_j > 1, L < log q_0, and the growth (50) `2/δ · log q_i < log q_j`; `Roth.exists_degrees` (fed the weakened growth) gives r with r_j > 0, 10/δ < r_j, r_{j+1}/δ < r_j, (33) and (53). Antitonicity of r is proved by writing m = n + 1 and using mathlib's `Fin.antitone_iff_succ_le` with `le_div_self` (r_{i+1} ≤ r_{i+1}/δ < r_i); then r_j ≤ r_0 from `Fin.zero_le`. Eq. (32) follows from L < log q_0 via `div_lt_iff₀'`; 3 ≤ r_{m−1} from 3 ≤ 10 ≤ 10/δ < r_{m−1} (`le_div_self`, `exact_mod_cast`).
- **Hypotheses**: `hα : Irrational α`, `hκ : 0 < κ`, `hinf` (all three passed to `exists_approximants`); `hδ0 : 0 < δ`, `hδ1 : δ ≤ 1` (needed by `exists_degrees` and by both `le_div_self` steps); `[NeZero m]` (needed for `Fin m` indexing at 0 and for `exists_degrees`). `A` is a free parameter only entering the constant L. No redundant hypothesis.
- **Uses from project**: `Roth.approxSet` (Roth/Main.lean:55), `Roth.exists_approximants` (Roth/Main.lean:256), `Roth.exists_degrees` (Roth/Main.lean:282).
- **Used by**: Roth/Main.lean:557 `Roth.roth_of_isIntegral` (destructured into h, q, r and all ten facts, each of which is consumed: happ via `(happ j).2.le` into `one_lt_roth_eval_bound_aux`, hcop/hr0/hrlast/h31b/h33 into `one_lt_roth_eval_bound_aux`, hq1/h53 into `roth_log_bound_aux`, hr0max and h32 into `roth_product_bound_aux`). `grep -rn exists_roth_approximants_aux Roth/` gives only the definition (l.429) and this use. Transitively feeds `Roth.roth` (main theorem).
- **Visibility**: private
- **Lines**: 429–450, proof length 14 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; preceded by a plain `--` comment rather than a docstring (fine for a private lemma). The strict inequality in the (32) conjunct is only ever consumed as `≤` (`h32.le` at both uses); harmless, the strict form is what `exists_approximants` naturally gives. Likewise the strict r_{j+1}/δ < r_j from `exists_degrees` is weakened to `≤` here because that is the form `one_lt_roth_eval_bound_aux` / `main_lemma` take.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Main.lean:557 in `roth_of_isIntegral`; every conjunct of the conclusion is used downstream.
- Wrapper of 1–2 mathlib calls? No. It chains two project lemmas (`exists_approximants`, `exists_degrees`) and adds a genuine small argument (antitonicity of r via `Fin.antitone_iff_succ_le`, the bound 3 ≤ r_{m−1}, and the rearrangement of (32)).
- Does mathlib have it? No: it is a pure parameter-choice existence statement using the project set `approxSet` and Roth-specific constants (2m + 1 + 2m log(1 + A) + …, 1 + δ/10, 10/δ). The mathlib ingredients (`Fin.antitone_iff_succ_le`, Mathlib/Order/Fin/Basic.lean:163; `le_div_self`, Mathlib/Algebra/Order/Field/Basic.lean:38; `div_lt_iff₀'`) are used directly. No search for a mathlib equivalent is meaningful.
- Too specific (inline?)? Specific to one call site and could be inlined into `roth_of_isIntegral`, but it was deliberately factored out (with siblings `exists_roth_parameters_aux`, `one_lt_roth_eval_bound_aux`, `roth_product_bound_aux`, `roth_log_bound_aux`) so the main proof reads as a short chain mirroring §7 and elaborates fast. Keep factored.
- Well-chosen statement? Yes: hypotheses minimal, conclusion shaped exactly to what the caller destructures, and the derived facts (antitone bound r_j ≤ r_0, 3 ≤ r_{m−1}) are proved once here rather than at the consumers. Minor: the (32) conjunct could be stated with `≤` since both consumers use `h32.le`; not worth a change.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site (Roth/Main.lean:557); no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Main.lean:429; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable-looking ingredients are assessed under their own entries (`Roth.exists_approximants.md`, `Roth.exists_degrees.md`).

## Evidence
- `grep -rn exists_roth_approximants_aux Roth/`: definition Roth/Main.lean:429, single use Roth/Main.lean:557.
- Read the body (Roth/Main.lean:428–450), the call site (Roth/Main.lean:547–567) and the dependency statements: `approxSet` (Roth/Main.lean:55), `exists_approximants` (l.256), `exists_degrees` (l.282).
- `grep -rn antitone_iff_succ_le` / `le_div_self` in mathlib: Mathlib/Order/Fin/Basic.lean:163 and Mathlib/Algebra/Order/Field/Basic.lean:38.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
