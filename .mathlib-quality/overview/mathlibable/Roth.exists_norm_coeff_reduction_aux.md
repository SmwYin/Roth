---
decl: Roth.exists_norm_coeff_reduction_aux
file: Roth/MainLemma.lean
line: 212
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-step leading-term elimination for modByMonic (deg f in (0, s], Q of degree at most s-1 with coefficient norms at most (1+A)C and the same remainder), the inductive step of norm_coeff_modByMonic_le; mathlib has no coefficient-norm bounds for modByMonic.
action: Keep as private helper for its single call site Roth/MainLemma.lean:264 (norm_coeff_modByMonic_le); optionally shorten hmod via Polynomial.modByMonic_eq_of_dvd_sub instead of unfolding divModByMonicAux.
---

# Roth.exists_norm_coeff_reduction_aux

## Inventory entry

### `theorem Roth.exists_norm_coeff_reduction_aux`
- **Type**: `∀ {R : Type*} [SeminormedRing R] {f P : Polynomial R} {A C : ℝ}, (∀ i, ‖f.coeff i‖ ≤ A) → (∀ i, ‖P.coeff i‖ ≤ C) → ∀ {s : ℕ}, P.natDegree ≤ s → f ≠ 1 → P %ₘ f ≠ P → 0 < f.natDegree ∧ f.natDegree ≤ s ∧ ∃ Q : Polynomial R, Q.natDegree ≤ s - 1 ∧ (∀ i, ‖Q.coeff i‖ ≤ (1 + A) * C) ∧ P %ₘ f = Q %ₘ f`
- **What**: One step of polynomial long division with coefficient-size control. If f has coefficients of norm at most A, P has coefficients of norm at most C and degree at most s, f is not 1 and reducing P modulo f actually changes P, then f is monic of degree between 1 and s, and subtracting the appropriate multiple f · lc(P) X^{deg P - deg f} gives a polynomial Q of degree at most s - 1 with coefficient norms at most (1 + A) C and the same remainder modulo f.
- **How**: From `hself` derives `Nontrivial R` (`Polynomial.Nontrivial.of_polynomial_ne`), monicity of f (contrapositive of `Polynomial.modByMonic_eq_of_not_monic`), `P ≠ 0`, and `f.degree ≤ P.degree` (contrapositive of `Polynomial.modByMonic_eq_self_iff`). Sets `Q := P - f * (C lc(P) * X^(deg P - deg f))`; `hmod` by unfolding `Polynomial.modByMonic` and one step of `Polynomial.divModByMonicAux` (`dite_eq_left`). Degree facts: `Polynomial.eq_one_of_monic_natDegree_zero`, `Polynomial.natDegree_le_natDegree`, and `Polynomial.div_wf_lemma` + `Polynomial.natDegree_lt_natDegree` for `deg Q < deg P`. Coefficient bound: `Polynomial.coeff_sub`, `Polynomial.coeff_mul_X_pow'`, `Polynomial.coeff_mul_C`, `norm_sub_le`, `norm_mul_le`, `mul_le_mul`, with `split_ifs` on the shifted index.
- **Hypotheses**: `[SeminormedRing R]` (no commutativity); coefficient bounds `hfA`, `hP`; `hs : P.natDegree ≤ s`; `hf1 : f ≠ 1`; `hself : P %ₘ f ≠ P` (encodes f monic and deg f ≤ deg P, P ≠ 0). Nonnegativity of A, C is derived from the norm bounds at index 0.
- **Uses from project**: `[]` (only mathlib lemmas)
- **Used by**: Roth/MainLemma.lean: `norm_coeff_modByMonic_le` (l.264, `obtain ⟨hn, hfs, Q, hQdeg, hQc, hmod⟩ := exists_norm_coeff_reduction_aux hfA hP hs hf1 hself`, the strong-induction step) only — `grep -rn exists_norm_coeff_reduction_aux Roth/` gives the definition and that use. Transitively everything downstream of `norm_coeff_modByMonic_le` (Lemma 9 remainder-coefficient bound in the main lemma).
- **Visibility**: private
- **Lines**: 212–246, proof length 31 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). The conclusions `0 < f.natDegree` and `f.natDegree ≤ s` are returned only to feed the `lia` arithmetic `s + 1 - deg f = (s - 1) + 1 - deg f + 1` in the caller. `hmod` could likely be proven more robustly by `Polynomial.modByMonic_eq_of_dvd_sub hf` (P - Q = f * (...) is divisible by f) rather than unfolding the internal `divModByMonicAux`; not tested here (style suggestion only).

## Junk check (Step 8)
- Used anywhere? Yes, once: `norm_coeff_modByMonic_le` (Roth/MainLemma.lean:264), as the inductive step.
- Wrapper of 1–2 mathlib calls? No: a 31-line proof combining monicity/degree extraction from `hself`, one long-division step, degree drop via `div_wf_lemma`, and a coefficient-norm estimate.
- Does mathlib have it? No. `grep` of `Mathlib/Algebra/Polynomial/Div.lean` for modByMonic lemmas finds only algebraic facts (`modByMonic_eq_sub_mul_div`, `modByMonic_add_div`, `dvd_modByMonic_sub`, `modByMonic_eq_of_dvd_sub`, `div_wf_lemma`); a project-wide grep of mathlib for norm bounds on coefficients of `%ₘ` (`‖.*coeff.*%ₘ`, `norm.*modByMonic`) returns nothing. No coefficient-size control of polynomial division exists in mathlib.
- Too specific / inline? Inlining into the strong induction of `norm_coeff_modByMonic_le` would bloat an induction body that is currently short; the existential packaging is a clean factoring of the induction step. It is specific to that induction, which is appropriate for a private helper.
- Well-chosen? Yes as a private helper. Minor possible cleanup: prove `hmod` via `Polynomial.modByMonic_eq_of_dvd_sub` instead of unfolding `Polynomial.divModByMonicAux` (implementation detail of mathlib, fragile across bumps).
- Conclusion: `KEEP` — action: keep as private helper of `norm_coeff_modByMonic_le`; optionally replace the `divModByMonicAux` unfolding in `hmod` by `modByMonic_eq_of_dvd_sub`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:212; also the name ends in `_aux`).

Note: if the parent `Roth.norm_coeff_modByMonic_le` is upstreamed, this lemma would travel with it as a private helper of its proof.

## Evidence
- `grep -rn exists_norm_coeff_reduction_aux Roth/`: definition l.212, single use l.264.
- `grep -rn "theorem .*modByMonic"` in mathlib `Algebra/Polynomial/Div.lean` and `grep -rn "add_mul_modByMonic|mul_modByMonic|sub_modByMonic|modByMonic_eq_of_dvd_sub|modByMonic_add|add_modByMonic"` over mathlib: only algebraic remainder lemmas (`modByMonic_eq_sub_mul_div` l.238, `modByMonic_add_div` l.261, `dvd_modByMonic_sub` l.264, `modByMonic_eq_of_dvd_sub` l.689).
- `grep -rln "‖.*coeff.*%ₘ|norm.*modByMonic"` over mathlib: no results.
- No Lean runs and no evidence Lean files (private SKIP; the project builds clean so the lemma compiles as stated; the `hmod` simplification is an untested suggestion).
